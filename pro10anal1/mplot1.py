# 로팅 라이브러리. 그래프 작성을 위한 다양한 함수를 제공
# 데이터 시각화는 복잡하고 방대한 양의 데이터를 차트, 그래프, 지도 등의
# 시각적 형태로 표현하여 정보를 직관적으로 이해하고 빠를 의사결정을 돕는다.

# 시각화의 중요성 ......

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.rcParams['axes.unicode_minus'] = False
import koreanize_matplotlib

x = ['서울','인천','수원']
y = [5, 3, 7]
plt.xlabel('지역명')
plt.ylabel('투자액')
plt.xlim([-1, 3])
plt.ylim([0, 10])
plt.yticks(list(range(0, 11, 3)))
plt.plot(x, y)
plt.show()

data = np.arange(1, 11, 2)
plt.plot(data)
x = [0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(a, b, str(b))
plt.show()

x = np.arange(10)
y = np.sin(x)
print(x, y)
# plt.plot(x, y)
# plt.plot(x, y, 'bo')
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

# hold : 복수의 plot으로 여러 개의 차트를 겹쳐 그림
x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)
plt.legend(['사인', '코사인'])
plt.show()

print()

plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('sine')
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()

print()
irum = ['a','b','c','d','e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 90, 100]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50, 100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc=4)
plt.grid(True)

fig = plt.gcf()
plt.show()
fig.savefig('mplot1.png')
