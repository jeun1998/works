import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
print(iris.keys())
print(iris.target)
print(iris.data[:3])
print(np.corrcoef(iris.data[:, 2], iris.data[:, 3]))

x = iris.data[:, [2, 3]]
y = iris.target
print(x.shape, y.shape)
print(x[:3], y[:3], set(map(int, y)))

print('\ntrain / test split (7:3)')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[:3], x_test[:3], y_train[:3], y_test[:3])

"""
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
print(x_test[:3])
ori_x_train = sc.inverse_transform(x_train)
print("원복값 : ", ori_x_train[:3])
"""
print('분류 모델 생성 ----')
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
print(model)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print(f'총갯수:{len(y_test)}, 오류수:{(y_test != y_pred).sum()}')
print('분류 정확도')

print(f'분류 정확도 : {accuracy_score(y_test, y_pred)}')
conf_mat = confusion_matrix(y_test, y_pred)
print('혼동행렬 : \n', conf_mat)
print('분류 정확도 : ', np.trace(conf_mat) / np.sum(conf_mat))
print(f'train score : {model.score(x_train, y_train)}')
print(f'test score : {model.score(x_test, y_test)}')

import joblib
joblib.dump(model, 'ex20model.sav')

read_model = joblib.load('ex20model.sav')
print(read_model)
print('새 값으로 예측하기')
new_data = np.array([[5.5, 2.2], [0.8, 0.9], [8.5, 6.2]])
# sc = StandardScaler()
# sc.fit(new_data)
# new_data = sc.transform(new_data)

new_pred = read_model.predict(new_data)
print('예측 결과 : ', new_pred)
print(read_model.predict_proba(new_data))

import matplotlib.pyplot as plt

import koreanize_matplotlib
from matplotlib.colors import ListedColormap

def plot_decision_regionFunc(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')      # 마커 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)   # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)   
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], color=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regionFunc(X=x_combined_std, y=y_combined, classifier=read_model, test_idx=range(105, 150), title='scikit-learn제공')  