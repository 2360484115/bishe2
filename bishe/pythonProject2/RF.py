import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 假设日志文件已经下载并指定了路径
data_path = 'MHEALTHDATASET/mHealth_subject4.log'

# 加载数据，选择合适的列
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

# 划分数据集
X = data.drop('activity_label', axis=1)
y = data['activity_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
new_observation = {
    'acc_chest_x': [-14.482],
    'acc_chest_y': [1.3741],
    'acc_chest_z': [-2.3921],
    'acc_ankle_l_x': [-0.037941],
    'acc_ankle_l_y': [-8.5464],
    'acc_ankle_l_z': [-3.1569],
    'gyro_ankle_l_x': [0.2115],
    'gyro_ankle_l_y': [-0.80675],
    'gyro_ankle_l_z': [-0.66405],  # 左脚踝角速度
    'mag_ankle_l_x': [217.97],
    'mag_ankle_l_y': [16.719],
    'mag_ankle_l_z': [-69.606],  # 左脚踝磁力计
    'acc_arm_x': [-18.814],
    'acc_arm_y': [-2.0883],
    'acc_arm_z': [3.1664],
    'gyro_arm_x': [-0.40196],
    'gyro_arm_y': [0.50103],
    'gyro_arm_z': [0.92241],  # 右下臂角速度
    'mag_arm_x': [-55.328],
    'mag_arm_y': [32.773],
    'mag_arm_z': [227.45],  # 右下臂磁力计
}

new_data_df = pd.DataFrame(new_observation)
# 数据标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
new_data_scaled = scaler.transform(new_data_df)

# 初始化并训练随机森林模型
model = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=45, bootstrap=True)
model.fit(X_train_scaled, y_train)

# 预测测试集
y_pred = model.predict(X_test_scaled)

print(y_pred)
# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
print("准确率：", accuracy)
print("\n正确的预测样本（部分）：")


# print(classification_report(y_test, y_pred))


# 使用模型进行预测
prediction = model.predict(new_data_scaled)
print("预测的活动类别：", prediction)
