# DB스캔
# k-means와 같은 전통적인 클러스터링 방법과 달리, dbscan은 클러스터 수를 미리 지정할 필요 x
# 불규칙한 형태와 다양한 밀도를 가진 데이터셋에 적합
# dbscan은 밀도가 다양하거나 모양이 불규칙한 클러스터가 있는 데이터와 같이 모양이 잘 정의 x, 이상치가 많은 데이터 처리할때 유용하게 사용 가능

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

x, y = make_moons(n_samples=200, noise=0.05, shuffle=True, random_state=0)
print(x[:5], x.shape)
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()
print('KMeans로 군집화')
km = KMeans(n_clusters=2, init='k-means++', random_state=0)
pred1 = km.fit_predict(x)
print('km 예측 군집 id : ', pred1[:10])

def plotResult(x, pr):
    plt.scatter(x[pr==0, 0], x[pr==0, 1], c='blue', marker='o', s=40, label='cluster')
    plt.scatter(x[pr==1, 0], x[pr==1, 1], c='red', marker='s', s=40, label='cluster')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], \
                c='black', marker='+', label='centroid')
    plt.title('Clustering Result')
    plt.legend()
    plt.show()

plotResult(x, pred1)

print('DBSCAN으로 군집화')
dbs = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
pred2 = dbs.fit_predict(x)
print('DBSCAN 군집 id : ', pred2[:10])
print('군집 종류:', set(pred2))
plotResult(x, pred2)