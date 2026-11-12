# 다항회귀분석 문제) 

# 데이터 로드 (Servo, UCI) : "https://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data"

# 제어 시스템(servo system), 특히 서보 제어기의 응답 속도(response time) 를 예측하기 위해 수집된 고전 데이터.
# 당시 뉴럴 네트워크와 회귀 분석 연구에 자주 쓰임.

# cols = ["motor", "screw", "pgain", "vgain", "class"]  # 모터 위치, 스크류 위치, P게인(비례 이득), V게인(속도 이득), 응답 시간(타깃)

#  - 타깃/피처 (숫자만 사용: pgain, vgain)
#    x = df[["pgain", "vgain"]].astype(float)   
#    y = df["class"].values
#  - 학습/테스트 분할 ( 8:2 )
#  - 스케일링 (StandardScaler)
#  - 다항 특성 (degree=2) + LinearRegression 또는 Ridge 학습
#  - 성능 평가 
#  - 시각화


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data"

cols = ["motor", "screw", "pgain", "vgain", "class"]
df = pd.read_csv(url, header=None, names=cols)

print(df.head(3))
print(df.info())
print(df.corr(numeric_only=True))


x = df[["pgain", "vgain"]].astype(float)
y = df["class"].values

print(x[:3])
print(y[:3])


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


quad = PolynomialFeatures(degree=2)

x_train_quad = quad.fit_transform(x_train_scaled)
x_test_quad = quad.transform(x_test_scaled)

print('\n다항 특성 변환 결과')
print(x_train_quad[:3])


model = LinearRegression()

model.fit(x_train_scaled, y_train)
y_lin_pred = model.predict(x_test_scaled)

lin_r2 = r2_score(y_test, y_lin_pred)
print('일반 선형회귀 R2 : ', lin_r2)


model.fit(x_train_quad, y_train)
y_quad_pred = model.predict(x_test_quad)

quad_r2 = r2_score(y_test, y_quad_pred)
print('2차 다항회귀 R2 : ', quad_r2)


print('\n모델 성능 평가')
print('MSE : ', mean_squared_error(y_test, y_quad_pred))
print('RMSE : ', np.sqrt(mean_squared_error(y_test, y_quad_pred)))


plt.scatter(y_test, y_lin_pred, c='b',
            label='linear fit(d=1), R2=%.2f' % lin_r2)

plt.scatter(y_test, y_quad_pred, c='r',
            label='quad fit(d=2), R2=%.2f' % quad_r2)

min_val = min(y_test.min(), y_lin_pred.min(), y_quad_pred.min())
max_val = max(y_test.max(), y_lin_pred.max(), y_quad_pred.max())

plt.plot([min_val, max_val], [min_val, max_val],
        color='black', linestyle='--')

plt.xlabel('Actual Response Time')
plt.ylabel('Predicted Response Time')
plt.title('Linear vs Polynomial Regression')
plt.legend()
plt.show()


new_df = pd.DataFrame({
    'pgain': [3, 4, 5],
    'vgain': [2, 3, 4]
})

new_scaled = scaler.transform(new_df)
new_quad = quad.transform(new_scaled)

new_pred = model.predict(new_quad)

print('\n새로운 값으로 예측')
print(new_df)
print('예상 응답 시간 : ', new_pred)
