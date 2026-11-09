# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오

#   예제파일 : cleanDescriptive.csv

#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부

#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

 

# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 

# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.

#   예제파일 : MariaDB의 jikwon table 

#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)

#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)

#   조건 : NA가 있는 행은 제외한다.


import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv("cleanDescriptive.csv")

data = df[['level', 'pass']].dropna()

ctab = pd.crosstab(data['level'], data['pass'])
print("부모 학력 수준과 자녀 대학 진학 여부")
print(ctab)
chi2, p, dof, expected = chi2_contingency(ctab)

print("\n카이제곱 통계량 :", chi2)
print("p-value :", p)
print("자유도 :", dof)

print("\n기대빈도")
print(pd.DataFrame(
    expected,
    index=ctab.index,
    columns=ctab.columns
))

alpha = 0.05

if p < alpha:
    print("귀무가설 기각")
    print("부모 학력 수준과 자녀 대학 진학 여부는 관련이 있다.")
else:
    print("귀무가설 기각 실패")
    print("부모 학력 수준과 자녀 대학 진학 여부의 관련성을 확인할 수 없다.")

print('===================================================================================')


import pymysql
import pandas as pd
from scipy.stats import chi2_contingency

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8mb4'
}

conn = pymysql.connect(**config)

sql = """
    SELECT jikwonjik, jikwonpay
    FROM jikwon
"""

try:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        cols = [c[0] for c in cur.description]
finally:
    conn.close()

df = pd.DataFrame(rows, columns=cols)

df = df[['jikwonjik', 'jikwonpay']].dropna()


jik_number = {
    '이사': 1,
    '부장': 2,
    '과장': 3,
    '대리': 4,
    '사원': 5
}

df['jik_code'] = df['jikwonjik'].map(jik_number)


df['jikwonpay'] = pd.to_numeric(
    df['jikwonpay'], errors='coerce'
)

df['pay_code'] = pd.cut(
    df['jikwonpay'],
    bins=[1000, 3000, 5000, 7000, float('inf')],
    labels=[1, 2, 3, 4],
    right=False
)

df = df.dropna(subset=['jik_code', 'pay_code'])

print("변환된 자료")
print(df.head())

ctab = pd.crosstab(df['jik_code'], df['pay_code'])

print("\n직급별 연봉 구간 교차표")
print(ctab)

chi2, p, dof, expected = chi2_contingency(ctab)

print("\n카이제곱 통계량 :", chi2)
print("p-value :", p)
print("자유도 :", dof)

print("\n기대빈도")
print(pd.DataFrame(
    expected,
    index=ctab.index,
    columns=ctab.columns
))


alpha = 0.05

if p < alpha:
    print("\n귀무가설 기각")
    print("직급과 연봉 구간 사이에 통계적으로 유의한 관련성이 있다.")
else:
    print("\n귀무가설 기각 실패")
    print("직급과 연봉 구간 사이에 통계적으로 유의한 관련성을 확인할 수 없다.")
