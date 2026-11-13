# 비계층적 군집분석(Non-hierachical Clustering)은 주어진 데이터를 k개의 군집으로 나눈다. 
# 원하는 군집의 수 k는 사전에 지정 (알고 있다고 가정) 한다.
# k-평균 군집화(M-means Clustering) 알고리즘은 군집의 중심이 되는 k개의 seed 점들을 선택하여 
# 그 seed점(중심점)과 거리가 가까운 개체들을 그룹화하는 방법이다. 
# 알고리즘은 다음과 같다.
# 1) K개의 중심점을 임의로 배치한다.
# 2) 모든 자료와 K개의 중심점과 거리를 계산하여 가장 가까운 중심점의 군집으로 할당한다.
# 3) 군집의 중심을 구한다. (평균을 구한다.)
# 4) 정지규칙에 이를 때까지 2~3단계를 반복한다.
#   - 군집의 변화가 없을때
#   - 중심점의 이동이 임계값 이하일 때
#   - 왜곡값(distortion, 각각의 클러스터의 거리제곱의 총합) 줄어들었다가 다시 늘어나는 지점

# 1. make_blobs 사용

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm

x, _ = make_blobs(n_samples=150, n_features=2, centers=3, \
                cluster_std=0.5, shuffle=True, random_state=0)
print(x[:5], ' ', x.shape)

plt.scatter(x[:, 0], x[:, 1], c='gray', marker='o', s=50)
plt.grid()
plt.show()

# KMeans 모델 작성
# cluster의 중심 선택하는 방법
# init_centroid = 'random'
# cluster의 중심을 임의로 선택

init_centroid = 'k-means++'
# kmodel = KMeans(n_clusters=3, init=init_centroid, n_init=10, random_state=0)
# n_init=n : KMeans를 n번 실행

kmodel = KMeans(n_clusters=3, init=init_centroid, random_state=0)
pred = kmodel.fit_predict(x)
# print('pred : ', pred)

# print(x[pred == 0])
# print(x[pred == 1])
# print(x[pred == 2])

plt.scatter(x[pred == 0, 0], x[pred == 0, 1], c='red', marker='o', s=50, label='cluster')
plt.scatter(x[pred == 1, 0], x[pred == 1, 1], c='green', marker='s', s=50, label='cluster')
plt.scatter(x[pred == 2, 0], x[pred == 2, 1], c='blue', marker='v', s=50, label='cluster')
plt.scatter(kmodel.cluster_centers_[:, 0], kmodel.cluster_centers_[:, 1], \
            c='black', marker='+', s=70, label='center')
plt.legend()
plt.grid()
plt.show()

# KMeans 의 k값은?
# 1) elbow

def elbow(x):
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init=init_centroid, random_state=0)
        km.fit(x)
        sse.append(km.inertia_)
    plt.plot(range(1, 11), sse, marker='o')
    plt.xlabel('군집수')
    plt.ylabel('SSE')
    plt.show()

elbow(x)

def plotSilhouette(x, pred):
    cluster_labels = np.unique(pred)
    n_clusters = cluster_labels.shape[0]   # 클러스터 개수를 n_clusters에 저장
    sil_val = silhouette_samples(x, pred, metric='euclidean')  # 실루엣 계수를 계산
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []

    for i, c in enumerate(cluster_labels):
        # 각 클러스터에 속하는 데이터들에 대한 실루엣 값을 수평 막대 그래프로 그려주기
        c_sil_value = sil_val[pred == c]
        c_sil_value.sort()
        y_ax_upper += len(c_sil_value)

        plt.barh(range(y_ax_lower, y_ax_upper), c_sil_value, height=1.0, edgecolor='none')
        yticks.append((y_ax_lower + y_ax_upper) / 2)
        y_ax_lower += len(c_sil_value)

    sil_avg = np.mean(sil_val)         # 평균 저장

    plt.axvline(sil_avg, color='red', linestyle='--')  # 계산된 실루엣 계수의 평균값을 빨간 점선으로 표시
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 개수')
    plt.show() 

X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
km = KMeans(n_clusters=3, random_state=0) 
y_km = km.fit_predict(X)

plotSilhouette(X, y_km)