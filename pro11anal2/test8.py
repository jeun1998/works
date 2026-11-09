import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/student.csv")
print(data.head(3))
print(data.describe())
print(data["국어"].mean())
print(len(data))
print(stats.shapiro(data["국어"]))

from scipy.stats import wilcoxon
wilcoxon_result = wilcoxon(data["국어"] - 80)
ttest_result = stats.ttest_1samp(data["국어"], popmean=80)
print('ttest_result : ', ttest_result)
print("------------------------------------------------------")

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/student.csv")
print(data2.head(3))
pd.set_option("display.max_columns", None)
print(data2.describe())
print()
fdata = data2[data2.gender == 1]
print(fdata, ' ', len(fdata))
print("여아 신생아 몸무게 평균:", np.mean(fdata.weight))
print("여아 신생아 몸무게 표준편차:", np.std(fdata.weight))

result2 = stats.ttest_1samp(fdata['weight'], popmean=2800)
print("result2 : ", result2)
print("t-test 선행 조건으로 정규성 확인 (n < 30)--------")
print(stats.shapiro(fdata['weight']))