# 차트 영역 객체 선언시 인터페이스 유형 두 가지
import numpy as np
import matplotlib.pyplot as plt

# 1) Matplotlib 스타일 인터페이스
x = np.arange(10)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()

# 2) '객체 지향' 인터페이스
fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()

fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0, 0].plot(x, np.sin(x))
ax[0, 1].plot(x, np.cos(x))
ax[1, 0].plot(x, np.tan(x))
ax[1, 1].plot(x, x ** 2)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(np.random.rand(1000), bins=100, alpha=0.5)
ax2.plot(np.random.rand(1000))
plt.show()

data = [5, 8, 10, 9, 7]
plt.bar(range(len(data)), data)
plt.show()

err = np.random.rand(len(data))
plt.barh(range(len(data)), data, alpha=0.8, xerr=err)
plt.show()

plt.pie(data, colors=['yellow', 'blue', 'red'], explode=(0, 0.2, 0, 0.1, 0))
plt.title('pie chart')
plt.show()

data = [1, 50, 80, 100, 90, 70, 500]
plt.boxplot(
    data,
    widths=0.4,
    showmeans=True,
    meanline=False,
    showfliers=True,
    whis=1.5
)
plt.ylabel('value')
plt.show()

n = 30
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (np.random.rand(n) * 15) ** 2
plt.scatter(x, y, c=color, s=scale)
plt.show()

import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4), 
                    index = pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
print(fdata.head())
print(fdata.tail())
fdata = fdata.cumsum()
print(fdata.head(3))
plt.plot(fdata)
plt.show()