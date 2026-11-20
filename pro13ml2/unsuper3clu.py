# 계층적 군집 분석 :  데이터를 단계적으로 묶어 군집을 형성하는 알고리즘
# 거리가 가까운 데이터부터 계속 묶어가는 방식
# 군집 수를 미리 정하지 않아도 됨. 구조는 덴드로 그램으로 확인

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
x = iris.data
y = iris.target
labels = iris.target_names

pd.set_option('display.max_columns', None)

df = pd.DataFrame(x, columns=iris.feature_names)
print(df.head(2))

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

z = linkage(x_scaled, method='ward')

plt.figure(figsize=(12, 5))
dendrogram(Z=z)
plt.title('아이리스로 계층적 군집 분석')
plt.xlabel('샘플')
plt.ylabel('거리(유클리드)')
plt.show()

# 덴드로그램을 분리해 최대 3개의 군집 만들기
clusters = fcluster(Z=z, t=3, criterion='maxclust')
df['cluster'] = clusters
print(df.head(3))

plt.figure(figsize=(6, 5))
sns.scatterplot(x=x_scaled[:, 0], y=x_scaled[:, 1], hue=clusters, palette='Set1')
# hue=clusters : clusters 기준으로 색을 달리 표시, palette='Set1' : 색상 스타일 지정
plt.title('군집결과')
plt.xlabel('feature1')
plt.ylabel('feature2')
plt.show()

print('실제 라벨 : ', y[:10])
print('군집 결과 : ', clusters[:10])
print('\n군집 결과 방증 ---')
print('교차표 - 실제 라벨 vs. 군집결과')
ct = pd.crosstab(y, clusters)
print(ct)

# row_0(실제 라벨): 0-setosa, 1-versicolor, 2-verginica
# col_0(군집 결과): cluster1, cluster2, cluster3
# setosa는 완벽 분리도이었고, versicolor, verginica는 일부 섞임

print('교차표 보조 설명 : 각 클래스가 가장 많이 속한 군집')
for i in range(ct.shape[0]):
    max_cluster = ct.iloc[i].idxmax()
    print(f'실제 클래스 {i} -> 군집 {max_cluster} (갯수:{ct.iloc[i].max})')

print()
from sklearn.metrics import adjusted_mutual_info_score, normalized_mutual_info_score
ari = adjusted_mutual_info_score(y, clusters)
print(f'평가지표:ARI ==> {ari:.4f}')

# 0.7이상이면 만족 0.5미만이면 문제 있음
# normalized_mutual_info_score : NMI(Normalized Mutual Info)
# - 정보량 기준으로 얼마나 유사한지 확인(군집및 그룹 간 얼마나 같은 정보를 고유하는가)
nmi = normalized_mutual_info_score(y, clusters)
print(f'평가지표:NMI ==> {nmi:.4f}')