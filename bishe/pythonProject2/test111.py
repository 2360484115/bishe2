import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib

# 加载模型和标准化器
model = load_model('model.h5')
scaler = joblib.load('scaler.pkl')


# 新观测数据
#数据集中21877
new_observation = {
    'acc_chest_x': [2.6184],
    'acc_chest_y': [0.39384],
    'acc_chest_z': [9.6986],
    'acc_ankle_l_x': [3.743],
    'acc_ankle_l_y': [1.9104],
    'acc_ankle_l_z': [8.8621],
    'gyro_ankle_l_x': [0.40816],
    'gyro_ankle_l_y': [0.65666],
    'gyro_ankle_l_z': [0.34381],
    'mag_ankle_l_x': [0.20238],
    'mag_ankle_l_y': [0.36495],
    'mag_ankle_l_z': [-0.7292],
    'acc_arm_x': [-7.2693],
    'acc_arm_y': [1.435],
    'acc_arm_z': [6.4988],
    'gyro_arm_x': [-0.21569],
    'gyro_arm_y': [0.6961],
    'gyro_arm_z': [0.78879],
    'mag_arm_x': [-0.18147],
    'mag_arm_y': [-0.19413],
    'mag_arm_z': [-1.4457]
}



# 转换为DataFrame
new_data_df = pd.DataFrame(new_observation)

# 标准化新数据
new_data_scaled = scaler.transform(new_data_df)

# 进行预测
new_prediction = model.predict(new_data_scaled.reshape(-1, new_data_scaled.shape[1], 1))
new_predicted_class = np.argmax(new_prediction, axis=1)

# 打印预测结果
print("新数据的预测类别：", new_predicted_class)
