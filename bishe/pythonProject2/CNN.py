import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, Dropout, MaxPooling1D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input
import joblib
# 数据加载
data_path = 'MHEALTHDATASET/mHealth_subject1.log'
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
data = pd.read_csv(data_path, delimiter=r'\s+', header=None,
                   usecols=[0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                   names=columns)

# 数据预处理
X = data.drop('activity_label', axis=1)
y = data['activity_label'].values  # 调整标签值以适应 to_categorical，从0开始编号

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'scaler.pkl')

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 将标签转换为分类格式
y_train_categorical = to_categorical(y_train)
y_test_categorical = to_categorical(y_test)

# 模型定义
model = Sequential([
    Input(shape=(X_train.shape[1], 1)),  # 使用Input层指定输入形状
    Conv1D(filters=64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Dropout(0.5),
    Flatten(),
    Dense(100, activation='relu'),
    Dense(y_train_categorical.shape[1], activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 模型摘要
model.summary()

# 数据扩展维度以适应模型输入 (batch, steps, channels)
X_train_expanded = np.expand_dims(X_train, axis=2)
X_test_expanded = np.expand_dims(X_test, axis=2)

# 训练模型
model.fit(X_train_expanded, y_train_categorical, epochs=10, batch_size=64, verbose=2)
model.save('model.h5')
# 评估模型
loss, accuracy = model.evaluate(X_test_expanded, y_test_categorical, verbose=0)
print("测试准确率: {:.2f}%".format(accuracy * 100))
print("测试损失值: {:.4f}".format(loss))
# 新观测数据



# new_observation = {
#     'acc_chest_x': [-7.67],
#     'acc_chest_y': [-0.33954],
#     'acc_chest_z': [-1.999],
#     'acc_ankle_l_x': [2.7197],
#     'acc_ankle_l_y': [-8.9036],
#     'acc_ankle_l_z': [-2.2409],
#     'gyro_ankle_l_x': [-0.087199],
#     'gyro_ankle_l_y': [0.090056],
#     'gyro_ankle_l_z': [0.72495],  # 左脚踝角速度
#     'mag_ankle_l_x': [9.6385],
#     'mag_ankle_l_y': [3.3899],
#     'mag_ankle_l_z': [-2.3912],  # 左脚踝磁力计
#     'acc_arm_x': [-2.0764],
#     'acc_arm_y': [-7.5394],
#     'acc_arm_z': [1.0605],
#     'gyro_arm_x': [-0.43725],
#     'gyro_arm_y': [0.1848],
#     'gyro_arm_z': [-0.25216],  # 右下臂角速度
#     'mag_arm_x': [-2.3009],
#     'mag_arm_y': [-14.654],
#     'mag_arm_z': [56.779],  # 右下臂磁力计
# }
#
# # 将新观测数据转换为DataFrame，使用相同的列名
# new_data_df = pd.DataFrame(new_observation)
#
# # 标准化新数据
# new_data_scaled = scaler.transform(new_data_df)
#
# # 为新数据增加一个维度以匹配CNN模型的输入要求
# new_data_expanded = np.expand_dims(new_data_scaled, axis=2)
#
# # 使用模型进行预测
# new_prediction = model.predict(new_data_expanded)
# new_predicted_class = np.argmax(new_prediction, axis=1)
#
# # 打印预测结果
# print("新数据的预测类别：", new_predicted_class)
