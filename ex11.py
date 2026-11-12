# 회귀분석 문제 3)    

# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.

# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.

# 회귀분석모형의 적절성을 위한 조건도 체크하시오.

# 완성된 모델로 Sales를 예측


# 회귀분석 문제 3) Carseats

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import koreanize_matplotlib
import matplotlib.pyplot as plt

from scipy.stats import shapiro
from statsmodels.stats.diagnostic import linear_reset, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. 데이터 불러오기
df = pd.read_csv(
    "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Carseats.csv"
)

print(df.head(3), df.shape)
print(df.info())

# 필요 없는 열 제거
df = df.drop([df.columns[6], df.columns[9], df.columns[10]], axis=1)

print('\n상관계수')
print(df.corr())

# 2. 회귀분석 모델 작성
# sm.OLS가 아니라 smf.ols 사용
lm = smf.ols(
    formula='Sales ~ Income + Advertising + Price + Age',
    data=df
).fit()

print('\n회귀분석 결과')
print(lm.summary())
print(f'수정된 결정계수 : {lm.rsquared_adj:.4f}')

# 3. 예측값과 잔차
print('\n선형회귀 모델의 적절성 조건 확인')

df_lm = df[['Sales', 'Income', 'Advertising', 'Price', 'Age']]
print(df_lm.head(2))

fitted = lm.predict(df_lm)
residual = df_lm['Sales'] - fitted

print('실제값 : ', df_lm['Sales'][:5].values)
print('예측값 : ', fitted[:5].values)
print('잔차 : ', residual[:5].values)
print('잔차의 평균 : ', np.mean(residual))

# 4. 잔차의 정규성 검정
print('\n1) 잔차의 정규성 검정')

stat, pv = shapiro(residual)

print(f'통계량 : {stat:.5f}, p값 : {pv:.5f}')
print('정규성 만족' if pv >= 0.05 else '정규성 불만족')

sm.qqplot(residual, line='s')
plt.title('Q-Q Plot of Residuals')
plt.show()

# 5. 선형성 검정
print('\n2) 선형성 검정')

reset_result = linear_reset(lm, power=2, use_f=True)

print(f'p-value : {reset_result.pvalue:.5f}')
print('선형성 만족' if reset_result.pvalue >= 0.05 else '선형성 불만족')

sns.regplot(
    x=fitted,
    y=residual,
    lowess=True,
    line_kws={'color': 'red'}
)

plt.plot(
    [fitted.min(), fitted.max()],
    [0, 0],
    color='grey',
    linestyle='--'
)

plt.xlabel('예측값')
plt.ylabel('잔차')
plt.title('선형성 확인')
plt.show()

# 6. 등분산성 검정
print('\n3) 등분산성 검정')

x = df_lm[['Income', 'Advertising', 'Price', 'Age']]
x_const = sm.add_constant(x)

bp_test = het_breuschpagan(residual, x_const)
bp_stat, bp_pvalue = bp_test[0], bp_test[1]

print(f'p-value : {bp_pvalue:.5f}')
print('등분산성 만족' if bp_pvalue >= 0.05 else '등분산성 위배')

# 7. 잔차의 독립성 검정
print('\n4) 잔차의 독립성 검정')

dw = sm.stats.stattools.durbin_watson(residual)
print('Durbin-Watson 통계량 : ', dw)

plt.plot(np.arange(len(residual)), residual, marker='o', linestyle='--')
plt.axhline(0, color='red', linestyle='--')

plt.xlabel('관측순서')
plt.ylabel('잔차')
plt.title('잔차의 독립성 검정')
plt.grid(alpha=0.3)
plt.show()

# 8. 다중공선성 검정
print('\n5) 다중공선성 검정')

df_ind = df[['Income', 'Advertising', 'Price', 'Age']]
df_ind_const = sm.add_constant(df_ind)

vifdf = pd.DataFrame()
vifdf['변수'] = df_ind.columns

vifdf['vif_value'] = [
    variance_inflation_factor(df_ind_const.values, i)
    for i in range(1, df_ind_const.shape[1])
]

print(vifdf)

sns.barplot(x='변수', y='vif_value', data=vifdf)
plt.title('VIF Values of Independent Variables')
plt.ylabel('VIF')
plt.show()

# 9. 모델 저장 및 불러오기
print('====================')

# statsmodels의 모델 저장 기능
lm.save('carseat.pickle')

# 저장된 모델 불러오기
try:
    mymodel = sm.load('carseat.pickle')
    print('모델 불러오기 성공')
except Exception as e:
    print('모델 불러오기 오류 : ', e)
    mymodel = lm

print(mymodel.summary())

# 10. 새로운 값으로 Sales 예측
print('=====================')
print('새로운 값으로 예측')

new_df = pd.DataFrame({
    'Income': [35, 62],
    'Advertising': [6, 3],
    'Price': [105, 88],
    'Age': [32, 55]
})

new_pred = mymodel.predict(new_df)

print('Sales 예측 결과 : ', new_pred.values)

