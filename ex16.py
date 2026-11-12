# • CRIM: 자치시(town)별 1인당 범죄율
# • ZN: 25,000평방피트(sq. ft.)를 초과하는 거주지역의 비율
# • INDUS: 비소매상업지역이 점유하고 있는 토지의 비율
# • CHAS: 찰스강(Charles River) 경계 위치 여부 (강의 경계에 위치하면 1, 아니면 0)
# • NOX: 산화질소 농도 (10ppm 단위)
# • RM: 주택 1가구당 평균 방의 개수
# • AGE: 1940년 이전에 건축된 자가 소유 주택의 비율
# • DIS: 5개의 보스턴 고용센터까지의 가중 거리
# • RAD: 방사형 고속도로까지의 접근성 지수
# • TAX: 10,000달러당 재산세율
# • PTRATIO: 자치시별 학생/교사 비율
# • B: 자치시별 흑인 비율 관련 공식값 1000(Bk - 0.63)^2
# • LSTAT: 모집단 중 하위계층의 비율(%)
# • MEDV: 본인 소유 주택가격의 중앙값 (단위: 1,000달러, 타겟 변수

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

pd.set_option('display.max_columns', None)
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/housing.data", header=None, sep=r'\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOS', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head(2))
print(df.corr())

x = df[['LSTAT']].values
y = df[['MEDV']].values
print(x[:3])
print(y[:3])

model = LinearRegression()
quad = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:3])
print(x_cubic[:3])

model.fit(x, y)
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
y_lin_fit = model.predict(x_fit)
# print('y_lin_fit : ', y_lin_fit)
model_r2 = r2_score(y, model.predict(x))
print('model_r2 : ', model_r2)

model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('q_r2 : ', q_r2)

model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('c_r2 : ', c_r2)

plt.scatter(x_fit, y_lin_fit,linestyle=':', label='linear fit(d=1), $R^2=%.2f'%model_r2, lw=3, c='b')
plt.scatter(x_fit, y_quad_fit,linestyle='-', label='quad fit(d=2), $R^2=%.2f'%model_r2, lw=3, c='r')
plt.scatter(x_fit, y_cubic_fit,linestyle='--', label='cubic fit(d=3), $R^2=%.2f'%model_r2, lw=3, c='k')
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()