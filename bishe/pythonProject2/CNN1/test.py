import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib

# 加载模型和标准化器
model = load_model('model.h5')
scaler = joblib.load('scaler.pkl')


# 新观测数据
new_observation = {

    'acc_arm_x': [-0.129],
    'acc_arm_y': [0.2],
    'acc_arm_z': [1.001],
    'gyro_arm_x': [-81.909],
    'gyro_arm_y': [-36.377],
    'gyro_arm_z': [-28.87],
    'mag_arm_x': [-16.317],
    'mag_arm_y': [-28.417],
    'mag_arm_z': [15.567]
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
