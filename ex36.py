# PCA : 선형 대수 관점에서, 입력 데이터의 공분산 행렬을 고윳값 분해하고
# 이렇게 구한 고유 벡터에 입력 데이터를 선형변환
# 이 고유 벡터가 PCA의 주성분 벡터로서 입력 데이터의 분산이 큰 방향을 나타냄
# 입력 데이터의 성질을 최대한 유지한 상태로 고차원을 저차원 데이터로 변황


import numpy as np
img = np.random.randint(0, 256, (28, 28))
print(img.shape)
vector = img.flatten()
print(vector.shape)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
n = 10
x = iris.data[:n, :2]
print('차원 축소 전 x:', x, x.shape, type(x))
print(x.T)

# 시각화1 : 각 샘플의 두 특성 값을 선으로 연결해 비교
plt.plot(x.T, 'o:')
plt.xticks(range(2), ['꽃받침길이', '꽃받침너비'])
plt.grid(True)
plt.title('아이리스 크기 특성')
plt.xlabel('특성의 종류')
plt.ylabel('특성값')
plt.legend(['표본 {}'.format(i + 1) for i in range(n)])
plt.show()
plt.close()

df = pd.DataFrame(x)
print(df)

ax = sns.scatterplot(x=0, y=1, data=df, markers='s', s=100, color='red')
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.05, '표본 {}'.format(i + 1))
plt.title('아이리스 크기 특성')
plt.xlabel('꽃받침길이')
plt.ylabel('꽃받침너비')
plt.show()
plt.close()

pca1 = PCA(n_components=2)
x_low = pca1.fit_transform(x)
print('x_low : ', x_low, ' ', x_low.shape)

x2 = pca1.inverse_transform(x_low)
print('원복 후 x2 : ', x2, x2.shape)
print('원복 : ', x[0, :])
print('주성분 : ', x_low[0])
print('원복 : ', x2[0, :])

pc1 = pca1.components_[0]
mean = x.mean(axis=0)

df = pd.DataFrame(x)
ax = sns.scatterplot(x=0, y=1, data=df, markers='s', s=100, color='b')
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.05, '표본 {}'.format(i + 1))

plt.quiver(
    mean[0], mean[1],
    pc1[0], pc1[1],
    scale=3, color='r', width=0.01
)

plt.title('아이리스 크기 특성 + 제1주성분')
plt.xlabel('꽃받침길이')
plt.ylabel('꽃받침너비')
plt.axis('equal')
plt.grid(True)
plt.show()
plt.close()
print('***' * 10)

x = iris.data
print(x[0, :])
pca2 = PCA(n_components=2)
x_low2 = pca2.fit_transform(x)
print('x_low2 : ', x_low2[0, :], ' ', x_low2.shape)

print(pca2.explained_variance_ratio_)
x4 = pca2.inverse_transform(x_low2)
print('최초 자료 : ', x[0])
print('차원 축소 : ', x_low2[0])
print('차원 복귀 : ', x4[0, :])
print()

iris1 = pd.DataFrame(x, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
print(iris1.head(3))
iris2 = pd.DataFrame(x_low2, columns=['var1', 'var2'])
print(iris2.head(3))

from sklearn import svm, metrics
feature1 = iris1.values
print(feature1[:3])
label = iris.target
print(label[:3])

print('원본 데이터로 SVM 분류 모델 작성')
model1 = svm.SVC(C=0.1, random_state=0).fit(feature1, label)
pred1 = model1.predict(feature1)
print('model1 accuracy : ', metrics.accuracy_score(label, pred1))

print('PCA 데이터로 SVM분류 모델 작성')
feature2 = iris2.values
print(feature2[:3])

model2 = svm.SVC(C=0.1, random_state=0).fit(feature2, label)
pred2 = model2.predict(feature2)
print('model2 accuracy : ', metrics.accuracy_score(label, pred2))