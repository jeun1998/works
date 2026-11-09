from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import os
import pymysql

# [two-sample t 검정 : 문제1] 

# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 

# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

# 수집된 자료 :  

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print("파란색 평균:", np.mean(blue))
print("빨간색 평균:", np.mean(red))

print("파란색 정규성", stats.shapiro(blue))
print("빨간색 정규성", stats.shapiro(red))

levene_result = stats.levene(blue, red)
print("등분산 검정:", levene_result)
ttest_result = stats.ttest_ind(blue, red, equal_var=(levene_result.pvalue >= 0.05))

if ttest_result.pvalue < 0.05:
    print("귀무가설 기각: 포장지 색상에 따른 평균 매출액에 차이가 있다.")
else:
    print("귀무가설 기각 실패: 평균 매출액에 차이가 있다는 증거가 부족하다.")


print("---------------------------------------------------------------------------------------------------------------")

# [two-sample t 검정 : 문제2]  

# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 수집된 자료 :  

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]

female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

rng = np.random.default_rng(42)
male_sample = rng.choice(male, size=15, replace=False)
female_sample = rng.choice(female, size=15, replace=False)
print("남자 표본:", male_sample)
print("여자 표본:", female_sample)
print("남자 평균:", np.mean(male_sample))
print("여자 평균:", np.mean(female_sample))

print("남자 정규성:", stats.shapiro(male_sample))
print("여자 정규성:", stats.shapiro(female_sample))


levene_result = stats.levene(male_sample, female_sample)
print("등분산 검정:", levene_result)

ttest_result = stats.ttest_ind(
    male_sample,
    female_sample,
    equal_var=(levene_result.pvalue >= 0.05)
)

print("t검정 결과:", ttest_result)

if ttest_result.pvalue < 0.05:
    print("귀무가설 기각: 남녀 평균 콜레스테롤 양에 차이가 있다.")
else:
    print("귀무가설 기각 실패: 남녀 평균 콜레스테롤 양에 차이가 있다는 증거가 부족하다.")
print("-----------------------------------------------------------------------------------------------")
# [two-sample t 검정 : 문제3]

# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.

# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password=os.getenv("DB_PASSWORD", "123"),
    database="test",
    port=3306,
    charset="utf8mb4"
)

sql = """
    SELECT b.busername, j.jikwonpay
    FROM jikwon j
    INNER JOIN buser b
        ON j.busernum = b.buserno
    WHERE b.busername IN ('총무부', '영업부')
"""

try:
    df = pd.read_sql(sql, conn)
finally:
    conn.close()

print("원본 데이터")
print(df)


df["jikwonpay"] = pd.to_numeric(
    df["jikwonpay"],
    errors="coerce"
)


df["jikwonpay"] = df["jikwonpay"].fillna(
    df.groupby("busername")["jikwonpay"].transform("mean")
)


ch = df.loc[
    df["busername"] == "총무부", "jikwonpay"
].dropna()

yo = df.loc[
    df["busername"] == "영업부", "jikwonpay"
].dropna()

print("\n총무부 평균 연봉:", ch.mean())
print("영업부 평균 연봉:", yo.mean())
print("총무부 인원:", len(ch))
print("영업부 인원:", len(yo))

if len(ch) < 2 or len(yo) < 2:
    raise ValueError("각 부서에 최소 2명의 유효한 연봉 자료가 필요합니다.")


print("\n총무부 정규성:", stats.shapiro(ch))
print("영업부 정규성:", stats.shapiro(yo))


levene_result = stats.levene(ch, yo)
print("\n등분산 검정:", levene_result)

t_result = stats.ttest_ind(ch, yo, equal_var=(levene_result.pvalue >= 0.05))


print("\n독립표본 t검정:", ttest_result)
print("p-value:", ttest_result.pvalue)

if t_result.pvalue < 0.05:
    print("귀무가설 기각: 총무부와 영업부의 평균 연봉에 유의한 차이가 있다.")
else:
    print("귀무가설 기각 실패: 두 부서의 평균 연봉에 차이가 있다는 증거가 부족하다.")
