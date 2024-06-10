import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, Dropout, MaxPooling1D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input
import joblib
from scipy import stats

# 数据加载
data1_path = 'MHEALTHDATASET/mHealth_subject1.log'
data2_path = 'MHEALTHDATASET/mHealth_subject2.log'
data3_path = 'MHEALTHDATASET/mHealth_subject3.log'
data4_path = 'MHEALTHDATASET/mHealth_subject4.log'
data5_path = 'MHEALTHDATASET/mHealth_subject5.log'
data6_path = 'MHEALTHDATASET/mHealth_subject6.log'
data7_path = 'MHEALTHDATASET/mHealth_subject7.log'
data8_path = 'MHEALTHDATASET/mHealth_subject8.log'
columns = [
    'acc_chest_x', 'acc_chest_y', 'acc_chest_z',  # 胸部加速度
    'acc_ankle_l_x', 'acc_ankle_l_y', 'acc_ankle_l_z',  # 左脚踝加速度
    'gyro_ankle_l_x', 'gyro_ankle_l_y', 'gyro_ankle_l_z',  # 左脚踝角速度
    'mag_ankle_l_x', 'mag_ankle_l_y', 'mag_ankle_l_z',  # 左脚踝磁力计
    'acc_arm_x', 'acc_arm_y', 'acc_arm_z',
    'gyro_arm_x', 'gyro_arm_y', 'gyro_arm_z',  # 右下臂角速度
    'mag_arm_x', 'mag_arm_y', 'mag_arm_z',  # 右下臂磁力计
    'activity_label'
]

# 加载数据
data1 = pd.read_csv(data1_path, delimiter=r'\s+', header=None, names=columns)
data2 = pd.read_csv(data2_path, delimiter=r'\s+', header=None, names=columns)
data3 = pd.read_csv(data3_path, delimiter=r'\s+', header=None, names=columns)
data4 = pd.read_csv(data4_path, delimiter=r'\s+', header=None, names=columns)
data5 = pd.read_csv(data5_path, delimiter=r'\s+', header=None, names=columns)
data6 = pd.read_csv(data6_path, delimiter=r'\s+', header=None, names=columns)
data7 = pd.read_csv(data7_path, delimiter=r'\s+', header=None, names=columns)
data8 = pd.read_csv(data8_path, delimiter=r'\s+', header=None, names=columns)
data = pd.concat([data1, data2, data3, data4, data5, data6])
data_test = pd.concat([data7, data8])
# 数据预处理
X = data.drop('activity_label', axis=1)
y = data['activity_label'].values
X_test = data_test.drop('activity_label', axis=1)
y_test = data_test['activity_label'].values

# print(X.shape, y.shape, X_test.shape, y_test.shape)
# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.fit_transform(X_test)
joblib.dump(scaler, 'scaler.pkl')
print(X_scaled.shape, y.shape, X_test_scaled.shape, y_test.shape)


def windowz(data, size, step):
    start = 0
    while start < len(data):
        yield start, start + size
        start += step


def segment_opp(inputs, targets, window_size, step):
    segments = np.zeros(((len(inputs) - window_size) // step + 1, window_size, 21))
    labels = np.zeros(((len(targets) - window_size) // step + 1))
    i_segment = 0
    i_label = 0
    for (start, end) in windowz(inputs, window_size, step):
        if len(inputs[start:end]) == window_size:
            m = stats.mode(y[start:end])
            segments[i_segment] = X_scaled[start:end]
            labels[i_label] = m[0]
            i_label += 1
            i_segment += 1
    return segments, labels


# 定义窗口大小和步长
window_size = 50
step = 25
train_x, train_y = segment_opp(X_scaled, y, window_size, step)
test_x, test_y = segment_opp(X_test_scaled, y_test, window_size, step)
print("Shape of segmented train inputs: {}".format(train_x.shape))
print("Shape of segmented train labels: {}".format(train_y.shape))
print("Shape of segmented test inputs:  {}".format(test_x.shape))
print("Shape of segmented test labels:  {}".format(test_y.shape))



# 将标签转换为分类格式
y_train_categorical = to_categorical(train_y)
y_test_categorical = to_categorical(test_y)

# 模型定义
model = Sequential([
    Input(shape=(train_x.shape[1], train_x.shape[2])),  # 输入形状
    Conv1D(filters=64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
        # …重复多层增加深度，并提高卷积核个数
    Dropout(0.5),
    Flatten(),
    Dense(100, activation='relu'),
    Dense(y_train_categorical.shape[1], activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 模型摘要
model.summary()

# 训练模型
model.fit(train_x, y_train_categorical, epochs=200, batch_size=64, verbose=2)

# 评估模型
loss, accuracy = model.evaluate(test_x, y_test_categorical, verbose=0)
print("测试准确率: {:.2f}%".format(accuracy * 100))
print("测试损失值: {:.4f}".format(loss))
