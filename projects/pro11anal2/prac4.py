# [ANOVA 예제 1]

# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.

# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.

# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 수집된 자료 :  

# kind quantity

# 1 64

# 2 72

# 3 68

# 4 77

# 2 56

# 1 NaN

# 3 95

# 4 78

# 2 55

# 1 91

# 2 63

# 3 49

# 4 70

# 1 80

# 2 90

# 1 33

# 1 44

# 3 55

# 4 66

# 2 77
from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request
import os
import pymysql
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from pingouin import welch_anova


data = pd.DataFrame({
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1,
            2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91,
                63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
})

print(data.head(3))
print(data.info())


print('결측치 확인 : ', data.isnull().sum())


data['quantity'] = data['quantity'].fillna(data['quantity'].mean())

print(data.head(6))
print('결측치 확인 : ', data.isnull().sum())


x1 = np.array(data[data['kind'] == 1].quantity)
x2 = np.array(data[data['kind'] == 2].quantity)
x3 = np.array(data[data['kind'] == 3].quantity)
x4 = np.array(data[data['kind'] == 4].quantity)

print('\n정규성 검정')
print(stats.shapiro(x1).pvalue)
print(stats.shapiro(x2).pvalue)
print(stats.shapiro(x3).pvalue)
print(stats.shapiro(x4).pvalue)

print('\n등분산 검정')
print(stats.levene(x1, x2, x3, x4).pvalue)

print('\n기름 종류별 평균 흡수량')
np.set_printoptions(suppress=True)

spp = data.loc[:, ['kind', 'quantity']]

print(spp.groupby('kind').mean())
print(np.mean(x1))
print(np.mean(x2))
print(np.mean(x3))
print(np.mean(x4))


group1, group2, group3, group4 = x1, x2, x3, x4

print('\nANOVA 검정')
print(stats.f_oneway(group1, group2, group3, group4))


print('\nWelch ANOVA 검정')
print(welch_anova(dv='quantity', between='kind', data=data))


print('\n사후 검정')

tukResult = pairwise_tukeyhsd(
    endog=spp['quantity'],
    groups=spp['kind']
)

print(tukResult)

tukResult.plot_simultaneous(
    xlabel='기름 흡수량 평균',
    ylabel='기름 종류'
)

plt.show()

print("---------------------------------------------------------------")



# [ANOVA 예제 2]

# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123',  # 본인 DB 비밀번호로 변경
    database='test',
    port=3306,
    charset='utf8mb4'
)

sql = """
    SELECT b.busername, j.jikwonpay
    FROM jikwon j
    INNER JOIN buser b
        ON j.busernum = b.buserno
    WHERE b.busername IN ('총무부', '영업부', '전산부', '관리부')
"""

data = pd.read_sql(sql, conn)
conn.close()

print(data.head(3))
print(data.info())


print('\n결측치 확인 : ', data.isnull().sum())


data['jikwonpay'] = pd.to_numeric(
    data['jikwonpay'], errors='coerce'
)
data = data.dropna(subset=['jikwonpay']).copy()

print('\n결측치 제거 후 : ', data.isnull().sum())
x1 = np.array(data[data['busername'] == '총무부'].jikwonpay)
x2 = np.array(data[data['busername'] == '영업부'].jikwonpay)
x3 = np.array(data[data['busername'] == '전산부'].jikwonpay)
x4 = np.array(data[data['busername'] == '관리부'].jikwonpay)

print('\n부서별 직원 수')
print(len(x1), len(x2), len(x3), len(x4))


print('\n=== Shapiro 정규성 검정 ===')
print('총무부 : ', stats.shapiro(x1).pvalue)
print('영업부 : ', stats.shapiro(x2).pvalue)
print('전산부 : ', stats.shapiro(x3).pvalue)
print('관리부 : ', stats.shapiro(x4).pvalue)


print('\n=== Levene 등분산 검정 ===')
print(stats.levene(x1, x2, x3, x4).pvalue)


print('\n=== 부서별 평균 연봉 ===')
np.set_printoptions(suppress=True)

spp = data.loc[:, ['busername', 'jikwonpay']]

print(spp.groupby('busername').mean())
print('총무부 : ', np.mean(x1))
print('영업부 : ', np.mean(x2))
print('전산부 : ', np.mean(x3))
print('관리부 : ', np.mean(x4))


group1, group2, group3, group4 = x1, x2, x3, x4

print('\n=== ANOVA 검정 ===')
anova_result = stats.f_oneway(
    group1, group2, group3, group4
)

print('F 통계량 : ', anova_result.statistic)
print('p-value : ', anova_result.pvalue)

# Welch ANOVA
print('\n=== Welch ANOVA 검정 ===')
print(welch_anova(
    dv='jikwonpay',
    between='busername',
    data=data
))


if anova_result.pvalue < 0.05:
    print('\n귀무가설 기각')
    print('부서별 평균 연봉에 유의한 차이가 있다.')
else:
    print('\n귀무가설 기각 실패')
    print('부서별 평균 연봉에 유의한 차이가 있다고 볼 수 없다.')

# Tukey 사후 검정
print('\n=== 사후 검정 ===')

tukResult = pairwise_tukeyhsd(
    endog=spp['jikwonpay'],
    groups=spp['busername']
)

print(tukResult)

tukResult.plot_simultaneous(
    xlabel='평균 연봉',
    ylabel='부서명'
)

plt.show()
