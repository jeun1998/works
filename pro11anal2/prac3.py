# [대응표본 t 검정 : 문제4]

# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.

# 수집된 자료 :  

#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80

#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95

# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

midterm = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

df = pd.DataFrame({
    '중간고사': midterm,
    '기말고사': final
})

df['점수차이'] = df['기말고사'] - df['중간고사']

print(df)
print(df.describe())

print("중간고사 평균:", np.mean(midterm))
print("기말고사 평균:", np.mean(final))
print("평균 점수 변화:", df['점수차이'].mean())

shapiro_result = stats.shapiro(df['점수차이'])
print("\nShapiro 검정:", shapiro_result)

t_result = stats.ttest_rel(midterm, final)

print("\n대응표본 t검정 결과")
print("t 통계량:", t_result.statistic)
print("p-value:", t_result.pvalue)

alpha = 0.05

if t_result.pvalue < alpha:
    print("귀무가설 기각")
    print("중간고사와 기말고사 평균 점수에 유의한 차이가 있다.")
else:
    print("귀무가설 기각 실패")
    print("평균 점수에 차이가 있다는 충분한 증거가 없다.")

# 학생별 점수 변화 시각화
plt.figure(figsize=(8, 5))

for before, after in zip(midterm, final):
    plt.plot(['중간고사', '기말고사'],
            [before, after], marker='o')

plt.title('학생별 중간고사와 기말고사 점수 변화')
plt.ylabel('시험 점수')
plt.grid(axis='y', alpha=0.3)
plt.show()

