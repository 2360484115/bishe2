# coding:UTF-8
import threading
import time
from flask import Flask



import struct
import bleak
import asyncio
import pymysql
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
import StepDetector

model = load_model('D:/python-project/pythonProject2/CNN1/model.h5')
scaler = joblib.load('D:/python-project/pythonProject2/CNN1/scaler.pkl')


# 设备实例 Device instance
class DeviceModel:
    # region 属性 attribute
    # 设备名称 deviceName
    deviceName = "我的设备"

    # 设备数据字典 Device Data Dictionary
    deviceData = {}

    # 设备是否开启
    isOpen = False

    # 临时数组 Temporary array
    TempBytes = []

    # endregion

    def __init__(self, deviceName, mac, callback_method):
        print("Initialize device model")
        # 设备名称（自定义） Device Name
        self.deviceName = deviceName
        self.mac = mac
        self.client = None
        self.writer_characteristic = None
        self.isOpen = False
        self.callback_method = callback_method
        self.deviceData = {}
        self.initialize_database_connection()
        self.dataReady = {'acceleration': False, 'gyroscope': False, 'magnetometer': False}
        self.step_counter = StepDetector.StepDetector()

    def initialize_database_connection(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='20021001wyx',
                database='cxp',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Database connection successfully established.")
            return True
        except pymysql.MySQLError as e:
            print(f"Error connecting to MySQL Platform: {e}")
            return False

    def disconnect_database(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")
            return True
        else:
            print("No active database connection to close.")
            return False



    # region 获取设备数据 Obtain device data
    # 设置设备数据 Set device data
    def set(self, key, value):
        # 将设备数据存到键值 Saving device data to key values
        self.deviceData[key] = value

    # 获得设备数据 Obtain device data
    def get(self, key):
        # 从键值中获取数据，没有则返回None Obtaining data from key values
        if key in self.deviceData:
            return self.deviceData[key]
        else:
            return None

    # 删除设备数据 Delete device data
    def remove(self, key):
        # 删除设备键值
        del self.deviceData[key]

    # endregion

    # 打开设备 open Device
    async def openDevice(self):
        print("Opening device......")
        # 获取设备的服务和特征 Obtain the services and characteristic of the device
        async with bleak.BleakClient(self.mac) as client:
            self.client = client
            self.isOpen = True
            # 设备UUID常量 Device UUID constant
            target_service_uuid = "0000ffe5-0000-1000-8000-00805f9a34fb"
            target_characteristic_uuid_read = "0000ffe4-0000-1000-8000-00805f9a34fb"
            target_characteristic_uuid_write = "0000ffe9-0000-1000-8000-00805f9a34fb"
            notify_characteristic = None

            print("Matching services......")
            for service in client.services:
                if service.uuid == target_service_uuid:
                    print(f"Service: {service}")
                    print("Matching characteristic......")
                    for characteristic in service.characteristics:
                        if characteristic.uuid == target_characteristic_uuid_read:
                            notify_characteristic = characteristic
                        if characteristic.uuid == target_characteristic_uuid_write:
                            self.writer_characteristic = characteristic
                    if notify_characteristic:
                        break

            if self.writer_characteristic:
                # 读取磁场四元数 Reading magnetic field quaternions
                print("Reading magnetic field quaternions")
                asyncio.create_task(self.sendDataTh())

            if notify_characteristic:
                print(f"Characteristic: {notify_characteristic}")
                # 设置通知以接收数据 Set up notifications to receive data
                await client.start_notify(notify_characteristic.uuid, self.onDataReceived)
                await self.changev(0x08)
                # 保持连接打开 Keep connected and open
                try:
                    while self.isOpen:
                        await asyncio.sleep(1)
                except asyncio.CancelledError:
                    pass
                finally:
                    # 在退出时停止通知 Stop notification on exit
                    await client.stop_notify(notify_characteristic.uuid)
            else:
                print("No matching services or characteristic found")

    # 关闭设备  close Device
    def closeDevice(self):
        self.isOpen = False
        print("The device is turned off")
        self.connection.close()

    async def sendDataTh(self):
        time.sleep(3)
        while self.isOpen:
            await self.readReg(0x3A)
            time.sleep(0.01)
            # await self.readReg(0x51)
            # time.sleep(0.05)
            await self.readReg(0x40)
            time.sleep(0.01)

    # region 数据解析 data analysis
    # 串口数据处理  Serial port data processing
    def onDataReceived(self, sender, data):
        tempdata = bytes.fromhex(data.hex())
        for var in tempdata:
            self.TempBytes.append(var)
            if len(self.TempBytes) == 1 and self.TempBytes[0] != 0x55:
                del self.TempBytes[0]
                continue
            if len(self.TempBytes) == 2 and (self.TempBytes[1] != 0x61 and self.TempBytes[1] != 0x71):
                del self.TempBytes[0]
                continue
            if len(self.TempBytes) == 20:
                self.processData(self.TempBytes)
                self.TempBytes.clear()

    def insert_sensor_data(self):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    sql = """INSERT INTO data1 (accx, accy, accz, asx, asy, asz, angx, angy, angz,
                    predictedclass,hx,hy,hz,temp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"""
                    cursor.execute(sql, (self.get("AccX"), self.get("AccY"), self.get("AccZ"),
                                         self.get("AsX"), self.get("AsY"), self.get("AsZ"),
                                         self.get("AngX"), self.get("AngY"), self.get("AngZ"),
                                         self.get("predicted_class"),
                                         self.get("HX"), self.get("HY"), self.get("HZ"), self.get("T")))
                    self.connection.commit()
                    print("Sensor data inserted successfully.")
            except pymysql.MySQLError as e:
                print(f"Failed to insert data: {e}")
        else:
            print("No database connection available.")

    def predict(self, data):
        # 创建一个新字典，只包含模型需要的键
        data_for_prediction = {
            'acc_arm_x': data['AccX'],
            'acc_arm_y': data['AccY'],
            'acc_arm_z': data['AccZ'],
            'gyro_arm_x': data['AsX'],
            'gyro_arm_y': data['AsY'],
            'gyro_arm_z': data['AsZ'],
            'mag_arm_x': data['HX'],
            'mag_arm_y': data['HY'],
            'mag_arm_z': data['HZ']
        }

        # 转换为DataFrame
        df = pd.DataFrame([data_for_prediction])
        scaled_data = scaler.transform(df)

        # 进行预测
        prediction = model.predict(scaled_data.reshape(-1, scaled_data.shape[1], 1))
        predicted_class = np.argmax(prediction, axis=1)
        print("Predicted activity class:", predicted_class)

        # Optionally, return the prediction if you need to use it elsewhere
        return predicted_class

    # 数据解析 data analysis
    def processData(self, Bytes):
        if Bytes[1] == 0x61:
            Ax = self.getSignInt16(Bytes[3] << 8 | Bytes[2]) / 32768 * 16
            Ay = self.getSignInt16(Bytes[5] << 8 | Bytes[4]) / 32768 * 16
            Az = self.getSignInt16(Bytes[7] << 8 | Bytes[6]) / 32768 * 16
            Gx = self.getSignInt16(Bytes[9] << 8 | Bytes[8]) / 32768 * 2000
            Gy = self.getSignInt16(Bytes[11] << 8 | Bytes[10]) / 32768 * 2000
            Gz = self.getSignInt16(Bytes[13] << 8 | Bytes[12]) / 32768 * 2000
            AngX = self.getSignInt16(Bytes[15] << 8 | Bytes[14]) / 32768 * 180
            AngY = self.getSignInt16(Bytes[17] << 8 | Bytes[16]) / 32768 * 180
            AngZ = self.getSignInt16(Bytes[19] << 8 | Bytes[18]) / 32768 * 180
            self.set("AccX", round(Ax, 3))
            self.set("AccY", round(Ay, 3))
            self.set("AccZ", round(Az, 3))
            self.set("AsX", round(Gx, 3))
            self.set("AsY", round(Gy, 3))
            self.set("AsZ", round(Gz, 3))
            self.set("AngX", round(AngX, 3))
            self.set("AngY", round(AngY, 3))
            self.set("AngZ", round(AngZ, 3))
            self.dataReady['acceleration'] = True
            self.dataReady['gyroscope'] = True
            ax = round(Ax, 4)
            ay = round(Ay, 4)
            az = round(Az, 4)
            magnitude = (ax ** 2 + ay ** 2 + az ** 2) ** 0.5
            self.step_counter.add_data(magnitude * 9.8)



        else:
            # 磁场 magnetic field
            if Bytes[2] == 0x3A:
                Hx = self.getSignInt16(Bytes[5] << 8 | Bytes[4]) / 120
                Hy = self.getSignInt16(Bytes[7] << 8 | Bytes[6]) / 120
                Hz = self.getSignInt16(Bytes[9] << 8 | Bytes[8]) / 120
                self.set("HX", round(Hx, 3))
                self.set("HY", round(Hy, 3))
                self.set("HZ", round(Hz, 3))
                self.dataReady['magnetometer'] = True
            # 四元数 Quaternion
            # elif Bytes[2] == 0x51:
            #     Q0 = self.getSignInt16(Bytes[5] << 8 | Bytes[4]) / 32768
            #     Q1 = self.getSignInt16(Bytes[7] << 8 | Bytes[6]) / 32768
            #     Q2 = self.getSignInt16(Bytes[9] << 8 | Bytes[8]) / 32768
            #     Q3 = self.getSignInt16(Bytes[11] << 8 | Bytes[10]) / 32768
            #     self.set("Q0", round(Q0, 5))
            #     self.set("Q1", round(Q1, 5))
            #     self.set("Q2", round(Q2, 5))
            #     self.set("Q3", round(Q3, 5))
            elif Bytes[2] == 0x40:
                t = self.getSignInt16(Bytes[5] << 8 | Bytes[4]) / 100
                self.set("T", round(t, 5))
            else:
                pass
        if all(self.dataReady.values()):  # 检查所有所需数据是否都已更新
            self.callback_method(self)
            predicted_class = self.predict(self.deviceData)
            predicted_class = int(predicted_class[0])
            self.set("predicted_class", predicted_class)
            self.dataReady = {key: False for key in self.dataReady}
            self.insert_sensor_data()



    # 获得int16有符号数 Obtain int16 signed number
    @staticmethod
    def getSignInt16(num):
        if num >= pow(2, 15):
            num -= pow(2, 16)
        return num

    # endregion

    # 发送串口数据 Sending serial port data
    async def sendData(self, data):
        try:
            if self.client.is_connected and self.writer_characteristic is not None:
                await self.client.write_gatt_char(self.writer_characteristic.uuid, bytes(data))
        except Exception as ex:
            print(ex)

    # 读取寄存器 read register
    async def readReg(self, regAddr):
        # 封装读取指令并向串口发送数据 Encapsulate read instructions and send data to the serial port
        await self.sendData(self.get_readBytes(regAddr))


    # 写入寄存器 Write Register
    async def writeReg(self, regAddr, sValue):
        # 解锁 unlock
        self.unlock()
        # 延迟100ms Delay 100ms
        time.sleep(0.1)
        # 封装写入指令并向串口发送数据
        await self.sendData(self.get_writeBytes(regAddr, sValue))
        # 延迟100ms Delay 100ms
        time.sleep(0.1)
        # 保存 save
        self.save()

    async def changev(self, regAddr):
        cmd = self.Setv(regAddr)
        await self.sendData(cmd)

    # 读取指令封装 Read instruction encapsulation
    @staticmethod
    def get_readBytes(regAddr):
        # 初始化
        tempBytes = [None] * 5
        tempBytes[0] = 0xff
        tempBytes[1] = 0xaa
        tempBytes[2] = 0x27
        tempBytes[3] = regAddr
        tempBytes[4] = 0
        return tempBytes

    # 写入指令封装 Write instruction encapsulation
    @staticmethod
    def get_writeBytes(regAddr, rValue):
        # 初始化
        tempBytes = [None] * 5
        tempBytes[0] = 0xff
        tempBytes[1] = 0xaa
        tempBytes[2] = regAddr
        tempBytes[3] = rValue & 0xff
        tempBytes[4] = rValue >> 8
        return tempBytes

    # 解锁
    def unlock(self):
        cmd = self.get_writeBytes(0x69, 0xb588)
        self.sendData(cmd)

    # 保存
    def save(self):
        cmd = self.get_writeBytes(0x00, 0x0000)
        self.sendData(cmd)

    @staticmethod
    def Setv(regAddr):
        # 初始化
        tempBytes = [None] * 5
        tempBytes[0] = 0xff
        tempBytes[1] = 0xaa
        tempBytes[2] = 0x03
        tempBytes[3] = regAddr
        tempBytes[4] = 0
        return tempBytes





