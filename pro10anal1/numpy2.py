# 배열 연산
# 기본 수학함수는 배열에 요소별로 적용되고,
# +,-,*,/나 또는 add, substract, multiply, divide 함수를 사용
# 벡터화 연산을 하므로 for문을 사용하지 않고 바로 배열에 대한 연산 가능

import numpy as np

x = np.array([[1., 2], [3, 4]])
print(x, ' ', x.dtype)

y = np.arange(5, 9).reshape(2, 2)
print(y, ' ', y.dtype)

print(x.ndim, ' ', y.ndim)

print()
print(x + y)
print(np.add(x, y))
print()
print(x - y)
print(np.subtract(x, y))
print()
print(x * y)
print(np.multiply(x, y))
print()
print(x / y)
print(np.divide(x, y))
print()
print(np.sqrt(x), ' ', np.exp(x), ' ', np.log(x), ' ', np.cos(x), ' ')

print('\n내적 : dot()은 numpy 모듈의 인스턴스 메소드로 내적 연산이 가능')
v = np.array([9, 10])
w = np.array([11, 12])
print(v * w)
# 벡터의 내적 (행렬곱)
print(v.dot(w))
print(np.dot(v,w))

print()
print(x)
print(np.mean(x), ' ', np.var(x))
print(np.max(x), ' ', np.min(x))
print(np.argmax(x), ' ', np.argmin(x))
print(np.cumsum(x))
print(np.cumprod(x))

print()
names1 = np.array(['tom','james','tom','oscar'])
names2 = np.array(['tom','page','john'])
print(np.unique(names1))
print(np.intersect1d(names1, names2))
print(np.intersect1d(names1, names2, assume_unique=True))
print(np.union1d(names1, names2))

print('\n전치(Transpose) - 2차원 배열에서 행과 열의 위치를 바꿈')
print(x)
print(x.T)
print(x.transpose())
print(x.swapaxes(0, 1))

print('\nBroadcasting : 크기가 다른 배열 간의 연산'
                ' - 작은 배열을 여러 번 반복해 큰 배열과 연산')
x = np.arange(1, 10).reshape(3, 3)
y = np.array([1, 0, 1])
print(x)
print(y)
print(x + y)

print()
np.savetxt("numpy2.txt", x)
imsi = np.loadtxt("numpy2.txt")
print(imsi)