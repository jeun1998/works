# sigmoid function 적용 연습
# LogisticRegression 모델은 wx + b를 logit 변환한 값에 sigmoid function 처리한 값을 .......

import math
def MySigmoidFunc(num):
    return 1 / (1 + math.exp(-num))
print(MySigmoidFunc(3))
print(MySigmoidFunc(1.5))
print(MySigmoidFunc(-5.0))
print(MySigmoidFunc(-10))

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

print('\n로짓(logit) 변환된 값으로 시그모이드 함수 통과 후 결과 시각화')
x = np.linspace(-10, 10, 50)
print(x)

w = 1.5
b = -2
z = w * x + b

def OurSigmoidFunc(z):
    return 1 / (1 + np.exp(-z))

p = OurSigmoidFunc(z)
print('p : \n', p)
print('x[:3] : ', np.round(x[:3], 3))
print('z[:3](logit) : ', np.round(z[:3], 3))
print('p[:3](확률) : ', p[:3])

plt.figure(figsize=(8, 5))
plt.plot(x, p, label='sigmoid(z)', color='blue')
plt.axhline(0.5, color='red', linestyle='--')
plt.title('z=wx + b --> sigmoid --> 확률(이항)')
plt.xlabel('x(입력값)')
plt.ylabel('p(확률값)')
plt.grid(True)
plt.legend()
plt.show()