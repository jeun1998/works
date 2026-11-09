from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

pd.set_option('display.max_columns', None)

sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv", dtype={'YMD':'object'})
print(sales_data.head(2))
print(sales_data.info())

wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(2))
print(wt_data.info())

print()
wt_data.tm = wt_data.tm.map(lambda x:x.replace("-", ""))
print(wt_data.head(2))

print()

frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.columns)
print(frame.head(3), ' ', len(frame))

data = frame.iloc[:, [0, 1, 7, 8]]
print(data.head())
print('결측치 확인 : ', data.isnull().sum())

data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3), ' ', data['ta_gubun'].unique())
x1 = np.array(data[data['ta_gubun']==0].AMT)
x2 = np.array(data[data['ta_gubun']==1].AMT)
x3 = np.array(data[data['ta_gubun']==2].AMT)
print(x1[:5])
print()
print(stats.shapiro(x1).pvalue)
print(stats.shapiro(x2).pvalue)
print(stats.shapiro(x3).pvalue)
print(stats.levene(x1, x2, x3).pvalue)

print("\n온도별 매출액 평균")
np.set_printoptions(suppress=True)
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
print(np.mean(x1))
print(np.mean(x2))
print(np.mean(x3))

group1, group2, group3 = x1, x2, x3
print(stats.f_oneway(group1, group2, group3, equal_var=False))

from pingouin import welch_anova
print(welch_anova(dv = 'AMT', between='ta_gubun', data=data))
print("\n사후 검정")
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'])
print(tukResult)

tukResult.plot_simultaneous(xlabel='매출액 평균', ylabel='온도 분류')
plt.show()