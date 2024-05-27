import pymysql


class StepDetector:
    def __init__(self):
        self.initialize_database_connection()
        self.window_size = 5
        self.raw_window = []  # 存储原始数据的窗口
        self.smoothed_window = []  # 存储平滑数据的窗口
        self.step_count = 0
        self.flag = 1
        self.threshold_peak = 12  # 波峰阈值，需要根据实际调整
        self.threshold_valley = 10  # 波谷阈值，需要根据实际调整
        self.zero = (self.threshold_peak + self.threshold_valley) / 2

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
        except pymysql.MySQLError as e:
            print(f"Error connecting to MySQL Platform: {e}")

    def add_data(self, magnitude):
        if len(self.raw_window) < self.window_size:
            self.raw_window.append(magnitude)
            self.smoothed_window.append(magnitude)
            return
        else:
            self.raw_window.pop(0)
            self.raw_window.append(magnitude)

        # 计算移动平均并更新平滑窗口
        if len(self.raw_window) == self.window_size:
            avg = sum(self.raw_window) / len(self.raw_window)
            self.smoothed_window.pop(0)
            self.smoothed_window.append(avg)

        # 打印窗口数据查看效果
        # print(f"Raw window: {self.raw_window}")
        # print(f"Smoothed window: {self.smoothed_window}")

    def check_steps(self):
        if len(self.smoothed_window) < self.window_size:
            return
        mid_index = len(self.smoothed_window) // 2  # 中间索引计算
        # print(f"Step detected. Total steps: {self.step_count}")
        # print(f"flag: {self.flag}")
        self.update_step_count(1, self.step_count)
        # 检查波峰条件
        if self.flag == 1:
            if all(x > self.threshold_peak for x in self.smoothed_window) and \
                    self.smoothed_window[mid_index] > max(self.smoothed_window[:mid_index] + self.smoothed_window[mid_index + 1:]):
                self.flag = 2
            else:
                return  # 提前退出，不满足波峰条件

        # 检查过零点条件
        if self.flag == 2:
            if self.smoothed_window[mid_index] < self.zero < self.smoothed_window[mid_index - 1]:
                self.flag = 3
            else:
                return  # 提前退出，不满足过零点条件

            # 检查波谷条件
        if self.flag == 3:
            if all(x < self.threshold_valley for x in self.smoothed_window) and \
                    self.smoothed_window[mid_index] < min(self.smoothed_window[:mid_index] + self.smoothed_window[mid_index + 1:]):
                self.flag = 1
                self.step_count += 1  # 步数加一
                # print(f"Step detected. Total steps: {self.step_count}")
                self.update_step_count(1, self.step_count)
            else:
                return  # 提前退出，不满足波谷条件

    def update_step_count(self, device_id, step_count):
        if not self.connection.open:
            self.initialize_database_connection()  # 确保连接已开启

        try:
            with self.connection.cursor() as cursor:
                sql = """
                UPDATE step_count SET step_count = %s WHERE id = %s
                """
                cursor.execute(sql, (step_count, device_id))
                self.connection.commit()
                print("Step count updated successfully.")
        except pymysql.MySQLError as e:
            print(f"Failed to update step count: {e}")
