from sklearn.linear_model import LinearRegression
import statsmodels.api
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

mtcars = statsmodels.api.datasets.get_rdataset("mtcars").data
print(mtcars.head(3))
print('상관계수:\n', mtcars.corr(method='pearson'))
print()

x = mtcars[['hp']].values
print(x[:5])
y = mtcars['mpg'].values
print(y[:5])

lmodel = LinearRegression().fit(X=x, y=y)
print('slope : ', lmodel.coef_)
print('intercept : ', lmodel.intercept_)

plt.scatter(x, y)
plt.plot(x, lmodel.coef_ * x + lmodel.intercept_, c='r')
plt.show()

pred = lmodel.predict(x)
print('예측값 : ', np.round(pred[:5], 1))
print('실제값 : ', y[:5])

print('MSE : ', mean_squared_error(y, pred))
print('RMSE : ', np.sqrt(mean_squared_error(y, pred)))
print('r2_score(결정계수, 설명력) : ', r2_score(y, pred))

print('새로운 hp로 mpg 예측')
new_hp = [[100],[110],[120]]
new_pred = lmodel.predict(new_hp)
print('예측 결과 : ', np.round(new_pred.ravel(), 2))