from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/two_sample.csv")
print(data.head(3))
print(data['score'].isnull().sum())

ms = data[['method', 'score']]
m1 = ms[ms['method'] == 1]
m2 = ms[ms['method'] == 2]
print(m1.head(3))
print(m2.head(3))

score1 = m1['score']
score2 = m2['score']
print(score1.isnull().sum())
print(score2.isnull().sum())

score2 = score2.fillna(score2.mean())

print('score1 정규성 : ', stats.shapiro(score1).pvalue)
print('score2 정규성 : ', stats.shapiro(score2).pvalue)

sns.histplot(score1, kde=True, color='pink', alpha=0.5, label='교육방법1')
sns.histplot(score2, kde=True, color='navy', alpha=0.5, label='교육방법2')
plt.xlabel('시험점수')
plt.ylabel('빈도')
plt.legend()
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
stats.probplot(score1, dist='norm', plot=ax[0])
ax[0].set_title('교육방법 1')
ax[0].set_xlabel('이론적 분위수')
ax[0].set_ylabel('표본 분위수')
ax[0].grid()

stats.probplot(score2, dist='norm', plot=ax[1])
ax[1].set_title('교육방법 2')
ax[1].set_xlabel('이론적 분위수')
ax[1].set_ylabel('표본 분위수')
ax[1].grid()
plt.tight_layout()
plt.show()

from scipy.stats import levene
print('등분산 만족 여부 : ', levene(score1, score2).pvalue)

result = stats.ttest_ind(score1, score2, equal_var=True)
print('result : ', result)