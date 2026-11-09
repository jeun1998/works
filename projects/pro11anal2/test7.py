import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

one_sample = [167.0, 182.7, 169.7, 176.8, 185.0]
print(np.array(one_sample).mean())
result = stats.ttest_1samp(one_sample, popmean=177.0)
print(result)

print()
result2 = stats.ttest_1samp(one_sample, popmean=165.0)
print(result2)
sns.displot(one_sample, bins=10, kde=True)
plt.xlabel("data")
plt.ylabel("value")
plt.show()

sns.displot(one_sample, bins=10, kde=False, color='skyblue', edgecolor='black')
plt.axvline(np.mean(one_sample), color='green', linestyle='-', label='표본평균')
plt.axvline(177, color='red', linestyle='--', label='가설평균 177cm')
plt.title("교육생 키 분포")
plt.xlabel("키")
plt.ylabel("빈도")
plt.legend()
plt.show()