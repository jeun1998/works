import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(data.head())
print(data.describe())

print('평균 / 표준편차')
print(np.mean(data.친밀도), ' ', np.std(data.친밀도))
print(np.mean(data.적절성), ' ', np.std(data.적절성))
print(np.mean(data.만족도), ' ', np.std(data.만족도))

print('공분산 ---')
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print()
print(data.cov())
print('상관계수 ---')
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
print()
print(data.corr())
print(data.corr(method='pearson'))

print('\n만족도에 따른 다른 특성 사이의 관계')
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))

data.plot(kind='scatter', x='만족도', y='적절성')
plt.show()

from pandas.plotting import scatter_matrix
attr = ['친밀도', '적절성', '만족도']
scatter_matrix(data[attr], figsize=(10, 6))
plt.show()
plt.close()

sns.heatmap(data.corr(), annot=True)
plt.show()
corr = data.corr()
mask =  np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="blue")

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5),
            corr.columns[i], ha="center", va="center", fontsize=10)

plt.title("상관계수 히트맵")
plt.tight_layout()
plt.show()