import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import koreanize_matplotlib
import statsmodels.api 
import matplotlib.pyplot as plt

advdf = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv", usecols=[1,2,3,4])
print(advdf.head(3), advdf.shape)
print(advdf.info())
print(advdf.corr())

print()
lm = smf.ols(formula='sales ~ tv + radio + newspaper', data=advdf).fit()
print(f'coefficient:{lm.params}, p-value:{lm.pvalues}, r-squared:{lm.rsquared}')
print(lm.summary())
print(lm.summary().tables[1])
print()

x_new = advdf[['tv', 'radio', 'newspaper']][:3]

print('예측에 참여한 값 : ', x_new)
print('실제값 : ', advdf.sales[:3].values)
print('예측값 : ', lm.predict(x_new).values.round(1))

my_new = pd.DataFrame({
    'tv': [100, 350, 700],
    'radio': [20, 30, 40],
    'newspaper': [10, 20, 30]
})

print('예측 상품 판매량 : ', lm.predict(my_new).values)

plt.scatter(advdf.tv, advdf.sales)
plt.xlabel('tv 광고비')
plt.ylabel('상품 판매량')
plt.plot(advdf.tv, lm.predict(advdf), color='r')
plt.show()

print('\n모델의 적절성 선행 조건 확인 : 선형성, 정규성, 등분산성')
fitted = lm.predict(advdf)
residual = advdf['sales'] - fitted
print('실제값:', advdf['sales'][:5].values)
print('예측값:', fitted[:5].values)
print('잔차:', residual[:5].values)    
print('잔차의 평균 값 : ', np.mean(residual))
print('\n잔차의 정규성 : 잔차가 정규성을 따르는지 확인')



from scipy.stats import shapiro
import scipy.stats as stats
import statsmodels.api as sm

stat, pv = shapiro(residual)
print(f"통계량:{stat}, p값:{pv}")
print('정규성 만족' if pv >= 0.05 else '정규성 불만족')
sm.qqplot(residual, line='s')
plt.title('Q-Q Plot of Residuals으로 정규성 확인')
plt.show()

print("\n선형성 검정 : 독립변수의 변화에 따라 종속변수의 변화가 선형성을 따르는지 확인")
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print('선형성 만족' if pv >= 0.05 else '선형성 불만족')

sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0], color='blue', linestyle='--')
plt.show()

from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(advdf['tv']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f"브루쉬-파간 테스트 통계량: {bp_stat}, p값: {bp_pvalue}")
print('등분산성 만족' if bp_pvalue >= 0.05 else '등분산성 불만족')

sns.scatterplot(x=advdf['tv'], y=residual)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('tv 광고비')
plt.ylabel('잔차')
plt.grid(alpha=0.3)
plt.show()

from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance
print(cd.sort_values(ascending=False).head())

print()
print(advdf.head())
print()
print(advdf.iloc[[35,178,25,175,131]])
fig = sm.graphics.influence_plot(lm, alpha=0.05, criterion="cooks")
plt.show()