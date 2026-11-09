from scipy import stats
import pandas as pd
import numpy as np

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]
print(np.mean(male), ' ', np.mean(female))

two_sample = stats.ttest_ind(male, female)
two_sample = stats.ttest_ind(male, female, equal_var=True)
tv, pv, = two_sample
print('t 검정 통계량 : ', tv)
print('p 값 : ', pv)

print('male의 정규성 : ', stats.shapiro(male))
print('female의 정규성 : ', stats.shapiro(female))