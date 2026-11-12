import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

print(np.corrcoef(x, y)[0, 1])
plt.scatter(x, y)
plt.show()

from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]
print(x)

model = LinearRegression().fit(x, y)
ypred = model.predict(x)
print('예측값 y : ', ypred)
print('결정계수 : ', r2_score(y, ypred))
plt.scatter(x, y)
plt.plot(x, ypred, c='red')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
x2 = poly.fit_transform(x)
print(x)
print(x2)

model2 = LinearRegression().fit(x2, y)
ypred2 = model2.predict(x2)
print('예측값 y : ', ypred2)
print('결정계수 : ', r2_score(y, ypred))
plt.scatter(x, y)
plt.plot(x, ypred2, c='red')
plt.show()