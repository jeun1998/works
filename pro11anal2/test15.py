from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

url = "https://raw.githubusercontent.com/thomas-haslwanter/statsintro_python/master/ipynb/Data/data_altman/altman_910.txt"
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')

gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]
print(gr1, ' ', np.mean(gr1))
print(gr2, ' ', np.mean(gr2))
print(gr3, ' ', np.mean(gr3))

print()
print(stats.shapiro(gr1).pvalue)
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)
print()
print(stats.levene(gr1, gr2, gr3).pvalue)
print(stats.bartlett(gr1, gr2, gr3).pvalue)

# 일원분산분석
df = pd.DataFrame(data=data, columns=['pay','group'])
lmodel = ols('pay ~ C(group)', data=df).fit()
print(anova_lm(lmodel, type=1))

f_stat, pv = stats.f_oneway(gr1, gr2, gr3)
print('f_stat : ', f_stat)
print('p_value : ', pv)
print()

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tukResult)

tukResult.plot_simultaneous(xlabel='급여 평균', ylabel='지역')
plt.show()

