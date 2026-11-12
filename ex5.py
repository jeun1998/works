# 전통적 방법의 선형 회귀
# 각 데이터에 대한 잔차제곱합이 최소가 되는 추세선 만들고 이를 통해 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계 분석하는 것

import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np

np.random.seed(12)

x = np.random.seed(1)

x = np.linspace(1, 10, 50).reshape(-1, 1)
print(x)
y = 5 * x.ravel() + 40 + np.random.normal(0, 3, 5)



x, y, _ = LinearRegression(n_samples=50, n_features=1, bias=50, coef=True, noise=40)
print(x)
print(y)
r = np.corrcoef(x.ravel(), y)[0, 1]
print(f'상관계수 : {r:.4f}')
print('\n모델 작성 방법 1 : LinearRegression 사용 - 모델 생성')
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(x, y)

print('기울기(가중치, weight, slope):', fit_model.coef_)
print('절편(편향, bias):', fit_model.intercept_)

y_newpred1 = fit_model.predict(x[[0]])
print('예측값1 : ', y_newpred1)

new_x = np.array([2.34], [6.21], [8.123])
y_new_preds = fit_model.predict(new_x)
for hour, score in zip(new_x.ravel(), y_new_preds):
    print(f'공부시간:{hour:.2f}시간 -> 예상 점수:{score:.2f}점')

print('\n모델 작성 방법 2: ols')

import statsmodels.formula.api as smf
import pandas as pd

data = np.array([x.ravel(), y])
df = pd.DataFrame(data.T)
df.columns = ['x','y']
print(df.head(3))

model2 = smf.ols(formula='y')
print(model2.summary())
print('가중치:', model2.params['x'])
print('편향:', model2.params['intercept'])

new_df = pd.DataFrame({'x': [2.34,6.21,8.123]})
print('편향:', model2.predict(new_df))