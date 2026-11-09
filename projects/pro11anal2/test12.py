# 귀무 : 강수 여부에 따라 매출액의 평균에 차이가 없다.
# 대립 : 강수 여부에 따라 매출액의 평균에 차이가 있다.

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

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

# print(data['sumRn'] > 0)
data['nain_yn'] = (data['sumRn'] > 0)
print(data.head())

sp = np.array(data.iloc[:, [1, 4]])
print(sp)

tg1 = sp[sp[:, 1] == 0, 0]
tg2 = sp[sp[:, 1] == 1, 0]
print(tg1[:3])
print(tg2[:3])
print('tg1 : 강수 없을 때 매출액 평균 : ', np.mean(tg1))
print('tg2 : 강수 없을 때 매출액 평균 : ', np.mean(tg2))

plt.boxplot([tg1, tg2], meanline=True, showmeans=True, notch=True)
plt.show()

print(len(tg1), ' ', len(tg2))
print(stats.shapiro(tg1).pvalue)
print(stats.shapiro(tg2).pvalue)
print(stats.levene(tg1, tg2).pvalue)
print(stats.ttest_ind(tg1, tg2, equal_var=True))