import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.5,2.1])

# plt.scatter(x, y)
# plt.grid(True)
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)

import numpy.linalg as lin
weight, bias = lin.lstsq(A, y)[0]
print(weight, ' ', bias)
print()
print(0.96 * 0 + -0.989999999999999999998)
print(0.96 * 1 + -0.989999999999999999998)
print(0.96 * 2 + -0.989999999999999999998)
print(0.96 * 3 + -0.989999999999999999998)
print(0.96 * 4 + -0.989999999999999999998)
print(0.96 * 5 + -0.989999999999999999998)

plt.scatter(x, y, marker='o', label='실제값')
plt.plot(x, weight * x + bias, 'r', label='최적화된 선형직선')
plt.grid(True)

new_x = 7.5
yhat = weight * new_x + bias
print('예측 결과 : ', yhat)
print()
new_x = 1.2345678
yhat = weight * new_x + bias
print('예측 결과 : ', yhat)

print('---------------------------------------------')
class MySimpleLinearRegression:
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, x:np.ndarray, y:np.ndarray):
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        bunja = np.sum((x - x_mean) * (y - y_mean))
        bunmo = np.sum((x - x_mean) ** 2)
        self.w = bunja / bunmo
        self.b = y_mean - (self.w * x_mean)

    def predict(self, new_x:np.ndarray):
        return self.w * new_x + self.b

np.random.seed(42)
x_height = np.random.normal(175, 5, 50)
y_weight = np.random.normal(70, 10, 50)
print(x_height)
print(y_weight)

model = MySimpleLinearRegression()
model.fit(x_height, y_weight)

print("추정된 w(기울기) : ", model.w)
print("추정된 b(절편) : ", model.b)
print()
y_pred = model.predict(x_height)

for i in range(len(x_height)):
    print(f"키:{x_height[i]:.2f}cm의 실제 몸무게:{y_weight[i]:.2f}, 예측몸무게:{y_pred[i]:.2f}")

print()
new_height = np.array([198])
new_weight = model.predict(new_height)
print(f'키 {new_height}cm인 경우 몸무게는 대략 {new_weight}kg')

plt.figure(figsize=(9, 6))
plt.scatter(x_height, y_weight, color='blue', label='실제 데이터')
x_line = np.linspace(x_height.min(), x_height.max())
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', linewidth=0.5)
plt.xlabel('키(cm)')
plt.ylabel('몸무게(kg)')
plt.title('키에 따른 몸무게 선형 회귀 분석')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()