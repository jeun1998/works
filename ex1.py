# 분산 : 한개의 변수가 평균으로 부터 얼마나 떨어져 있는지
# 공분산(covarience): 한개의 변수가 함께 어떻게 변하는디
# 두 변수가 각각의 평균을 기준으로 함께 증가하거나 감소하는 경향이 있는지 나타내는 통계량
# 계산: 각 관측값이 평균보다 높은지 낮은지를 비교하여 두 편차의 곱을 계산

import numpy as np

print('변수1', np.arange(1, 6))
print('변수2', np.arange(2, 7))
print(np.cov(np.arange(1, 6, 1), np.arange(2, 7, 1)))
print(np.cov(np.arange(10, 60, 10), np.arange(20, 70, 10)))
print(np.cov(np.arange(1, 6, 1), (3,3,3,3,3)))
print(np.cov(np.arange(1, 6, 1), np.arange(6, 1, -1)))

# 상관 계수 : 공분산을 표준화한 값 -> 공분산을 두 변수의 표준편차곱으로 나눈 값
#          : 두 변수의 측정단위나 크기에 상관 없이 -1 ~ 1 사이의 값으로 

import matplotlib.pyplot as plt
x = [4,8,4,5,7,9,6,1,3]
y = [7,4,9,7,2,3,6,8,6]

plt.plot(x, y, 'o')
plt.show()
print('x, y의 공분산 : ', np.cov(x, y))
print('x, y의 공분산 : ', np.cov(x, y)[0, 1])

x2 = [80,30,60,60,90,40,30,90,30,40]
y2 = [60,20,40,60,90,50,10,80,40,50]
print('x2, y2의 공분산 : ', np.cov(x2, y2)[0, 1])
plt.plot(x2, y2, 'o')
plt.show()
print()

print('x, y의 상관계수 : ', np.corrcoef(x, y))
print('x, y의 상관계수 : ', np.corrcoef(x, y)[0, 1])
print('x2, y2의 상관계수 : ', np.corrcoef(x2, y2)[0, 1])

from scipy import stats
print("scipy 모듈 사용 r : ", stats.pearsonr(x, y))
print('-- 비선형 데이터인 경우 공분산, 상관계수는 의미 없다. ----')
m = [-3,-2,-1,0,1,2,3]
n = [9,4,1,0,1,4,9]
plt.plot(m, n, 'o')
plt.show()
print(np.cov(m, n)[0, 1])
print(np.corrcoef(m, n)[0, 1])