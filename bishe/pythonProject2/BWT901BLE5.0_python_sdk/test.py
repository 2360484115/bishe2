import asyncio
import bleak
from flask import Flask
import threading
import device_model
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
devices = []
device = None


# 扫描蓝牙设备并过滤名称
async def scan():
    global devices
    find = []
    print("Searching for Bluetooth devices...")
    try:
        devices = await bleak.BleakScanner.discover()
        print("Search ended")
        for d in devices:
            if d.name is not None and "WT" in d.name:
                find.append(d)
                print(d)
        if len(find) == 0:
            print("No devices found in this search!")
    except Exception as ex:
        print("Bluetooth search failed to start")
        print(ex)


# 数据更新时会调用此方法
def updateData(DeviceModel):
    print(DeviceModel.deviceData)


@app.route('/database/connect', methods=['POST'])
def connect_database():
    global device
    print("test")
    success = device.initialize_database_connection()
    if success:
        return "Database connected successfully."
    else:
        return "Failed to connect to the database."


@app.route('/database/disconnect', methods=['POST'])
def disconnect_database():
    global device
    success = device.disconnect_database()
    if success:
        return "Database disconnected successfully."
    else:
        return "No active database connection to close."


async def run_async_task():
    await asyncio.gather(
        scan(),
        device.openDevice()
    )


if __name__ == '__main__':
    # 搜索设备
    asyncio.run(scan())

    # 选择要连接的设备
    device_mac = None
    user_input = input("Please enter the Mac address you want to connect to (e.g. DF:E9:1F:2C:BD:59): ")
    for device in devices:
        if device.address == user_input:
            device_mac = device.address
            break
    if device_mac is not None:
        # 创建设备
        device = device_model.DeviceModel("MyBle5.0", device_mac, updateData)

        # 启动 Flask 应用程序和异步任务
        threading.Thread(target=lambda: app.run(port=5000)).start()
        asyncio.run(run_async_task())

    else:
        print("No Bluetooth device corresponding to Mac address found!!")
