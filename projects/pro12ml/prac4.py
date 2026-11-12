# 회귀분석 문제 5) 

# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.

# testdata 폴더 : Consumo_cerveja.csv

 

# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset

# feature : Temperatura Media (C) : 평균 기온(C)

#             Precipitacao (mm) : 강수(mm)

# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오

 

# 조건 : NaN이 있는 경우 삭제!


# 회귀분석 문제 5)
# 맥주 소비량 예측 - LinearRegression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Consumo_cerveja.csv")

print(df.head(3))
print(df.info())
print(df.shape)
print(df.isnull().sum())

df = df[['Temperatura Media (C)',
        'Precipitacao (mm)',
        'Consumo de cerveja (litros)']].copy()


df = df.dropna()

# 숫자형으로 변환
# 데이터에 소수점 쉼표가 포함된 경우 처리
for col in df.columns:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(',', '.', regex=False),
        errors='coerce'
    )

# 숫자로 변환할 수 없는 값도 제거
df = df.dropna()

print('\n결측치 제거 후')
print(df.shape)
print(df.isnull().sum())


x = df[['Temperatura Media (C)', 'Precipitacao (mm)']]
y = df['Consumo de cerveja (litros)']

print('\n독립변수')
print(x.head(3))

print('\n종속변수')
print(y.head(3))


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(x_train, y_train)

print('\n회귀계수 : ', model.coef_)
print('절편 : ', model.intercept_)


y_pred = model.predict(x_test)

print('\n실제값 : ', y_test.values[:5])
print('예측값 : ', y_pred[:5])


print('\n모델 평가')
print('학습용 결정계수 : ', model.score(x_train, y_train))
print('검증용 결정계수 : ', model.score(x_test, y_test))
print('R2 Score : ', r2_score(y_test, y_pred))
print('MSE : ', mean_squared_error(y_test, y_pred))


plt.scatter(y_test, y_pred)

plt.xlabel('실제 맥주 소비량')
plt.ylabel('예측 맥주 소비량')
plt.title('실제값과 예측값 비교')

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red',
    linestyle='--'
)

plt.show()


new_df = pd.DataFrame({
    'Temperatura Media (C)': [20, 25, 30],
    'Precipitacao (mm)': [0, 5, 10]
})

new_pred = model.predict(new_df)

print('\n새로운 데이터 예측')
print(new_df)
print('맥주 소비량 예측 결과 : ', new_pred)
