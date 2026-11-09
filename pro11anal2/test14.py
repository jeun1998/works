# 분산분석
# f값 = 집단간분산 / 집단내분산

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/three_sample.csv")
print(data.head(3), ' ', len(data))
print(data.describe())

# import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.show()

q1 = data['score'].quantile(0.25)
q3 = data['score'].quantile(0.75)
iqr = q3 -q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1:{q1}, Q3:{q3}, IQR:{iqr}")
print("이상치 하한 값 : ", lower)
print("이상치 상한 값 : ", upper)
outlier = data[(data['score'] < lower) | (data['score'] > upper)]
print('outlier : ', outlier)
print('outlier 갯수 : ', len(outlier))

print("\n컬럼명 확인:", data.columns.tolist())

group_col = "method"  # 실제 집단 구분 컬럼명 확인

# 분석 데이터 준비
df = data[[group_col, "score"]].copy()
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df = df.dropna()


print("\n=== 집단별 기초 통계 ===")
print(df.groupby(group_col)["score"].agg(
    ["count", "mean", "std", "var"]
))


print("\n=== Shapiro 정규성 검정 ===")

for name, group in df.groupby(group_col):
    if len(group) >= 3:
        result = stats.shapiro(group["score"])
        print(f"{name} : 통계량={result.statistic:.5f}, p-value={result.pvalue:.5f}")


groups = [
    group["score"].values
    for _, group in df.groupby(group_col)
]

levene_result = stats.levene(*groups)

print("\n=== Levene 등분산 검정 ===")
print("통계량:", levene_result.statistic)
print("p-value:", levene_result.pvalue)


model = ols(f"score ~ C({group_col})", data=df).fit()


anova_table = sm.stats.anova_lm(model, typ=2)

print("\n=== ANOVA 분산분석표 ===")
print(anova_table)

ss_between = anova_table.iloc[0]["sum_sq"]
ss_within = anova_table.iloc[1]["sum_sq"]

df_between = anova_table.iloc[0]["df"]
df_within = anova_table.iloc[1]["df"]

ms_between = ss_between / df_between
ms_within = ss_within / df_within

f_value = anova_table.iloc[0]["F"]
p_value = anova_table.iloc[0]["PR(>F)"]

ss_total = ss_between + ss_within
df_total = df_between + df_within

eta_squared = ss_between / ss_total

print("\n=== ANOVA 상세 결과 ===")
print(f"집단 간 제곱합(SSB): {ss_between:.5f}")
print(f"집단 내 제곱합(SSW): {ss_within:.5f}")
print(f"전체 제곱합(SST): {ss_total:.5f}")

print(f"집단 간 자유도: {df_between:.0f}")
print(f"집단 내 자유도: {df_within:.0f}")
print(f"전체 자유도: {df_total:.0f}")

print(f"집단 간 평균제곱(MSB): {ms_between:.5f}")
print(f"집단 내 평균제곱(MSW): {ms_within:.5f}")

print(f"F 통계량: {f_value:.5f}")
print(f"p-value: {p_value:.5f}")
print(f"효과크기(eta squared): {eta_squared:.5f}")
print(data.groupby('method')['score'].mean())

from statsmodels.stats.multicomp import pairwise_tukeyhsd
alpha = 0.05
tukResult = pairwise_tukeyhsd(endog=data['score'], groups=data['method'])
print("\n=== 가설 검정 결과 ===")

if p_value < alpha:
    print("귀무가설 기각")
    print("세 집단 중 적어도 한 집단의 평균에 유의한 차이가 있다.")

    
    print("\n=== Tukey HSD 사후검정 ===")
    tukey = pairwise_tukeyhsd(
        endog=df["score"],
        groups=df[group_col],
        alpha=0.05
    )
    print(tukey)

else:
    print("귀무가설 기각 실패")
    print("집단 간 평균에 차이가 있다는 충분한 증거가 없다.")

import matplotlib.pyplot as plt
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
