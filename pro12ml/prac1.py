
# 상관관계 문제)

# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 

# 또한 sales와 관계를 알기 위해 sales에 상관 관계를 정렬한 후 TV, radio, newspaper에 대한 영향을 해석하시오.

# 그리고 이들의 관계를 heatmap 그래프로 표현하시오.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv")
print(data.head())
print(data.describe())
print(data.columns)

data = data[['tv', 'radio', 'newspaper', 'sales']]

print('\n공분산 ---')
print(data.cov())

print('\n상관계수 ---')
print(data.corr())
print(data.corr(method='pearson'))

print('\n광고 매체 간 상관관계')
print(data[['tv', 'radio', 'newspaper']].corr())

print('\nsales에 따른 다른 특성 사이의 관계')
co_re = data.corr()
print(co_re['sales'].sort_values(ascending=False))

data.plot(kind='scatter', x='tv', y='sales')
plt.show()

data.plot(kind='scatter', x='radio', y='sales')
plt.show()

data.plot(kind='scatter', x='newspaper', y='sales')
plt.show()

sns.heatmap(data.corr(), annot=True)
plt.title('광고 매체와 매출액의 상관관계')
plt.show()