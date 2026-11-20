# 비계층적 군집 분석 :  학생 10명의 시험점수 사용

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.cluster import KMeans
import pandas as pd

students = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
scores = np.array([76,95,65,85,60,92,55,88,83,72]).reshape(-1, 1)
print('점수 : ', scores)

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
km_clusters = kmeans.fit_predict(scores)
print(km_clusters)

df = pd.DataFrame({
    'student':students,
    'score':scores.ravel(),
    'cluster':km_clusters
})
print(df)

print('\n군집별 평균 점수')
groupd = df.groupby('cluster')['score'].mean()
print('군집별 평균 : ', groupd)

x_position = np.arange(len(students))
y_scores = scores.ravel()
colors = {0:'red', 1:'blue', 2:'green'}
plt.figure(figsize=(10, 6))

for i, (x, y, cluster) in enumerate(zip(x_position, y_scores, km_clusters)):
    plt.scatter(x, y, color=colors[cluster], s=100)
    plt.text(x, y + 1.5, students[i], fontsize=10, ha='center')

centers = kmeans.cluster_centers_
for center in centers:
    plt.scatter(len(students) // 2)