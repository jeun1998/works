from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

baseline = [67.2, 67, 72, 77.6, 86, 89, 60, 82, 105]
followup = [62, 64, 70, 63, 80, 73, 58, 71, 101]

df = pd.DataFrame({
    '수술전':baseline,
    '수술후':followup,
})

df['감소량'] = df['수술전'] - df['수술후']
print(df)
print(df.describe())
print(f"수술 전 평균 : {df['수술전'].mean():.2f}kg")
print(f"수술 후 평균 : {df['수술후'].mean():.2f}kg")

result = stats.ttest_rel(baseline, followup)
print(f"t 통계량 : {result.statistic:.5f}")
print(f"p-value : {result.pvalue:.5f}")

alpha = 0.05
if result.pvalue < alpha:
    print('귀무 기각 : 수술 전후 평균 몸무게에 통계적으로 유의한 차이가 있다.')
else:
    print('귀무 채택 : 수술 전후 평균 몸무게에 차이가 있다는 근거가 부족하다.')

print('몸무게 감소량 정규성 : ', stats.shapiro(df['감소량']).pvalue)

stats.probplot(df['감소량'], dist='norm', plot=plt)
plt.grid()
plt.show()

plt.figure(figsize=(8, 5))
for before, after in zip(baseline, followup):
    plt.plot(['수술전','수술후'], [before, after], marker='o')
plt.title('수술 전후 몸무게 변화')
plt.ylabel('몸무게(kg)')
plt.grid(axis='y', alpha=0.3)
plt.show()