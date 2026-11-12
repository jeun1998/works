import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.formula.api as smf

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(df.head(3))
print(df.corr())

model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
print(model.summary())

model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
print(model.summary())
print('parameters : ', model.params)
print('R-squared : ', model.rsquared)
print('p-value : ', model.pvalues)
print('예측값:', model.predict()[:5])
print('실제값:', df.만족도[:5].values)

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, slope * df.적절성 + intercept, c='b')
plt.show()

print('\n실제값과 예측값 비교')
result_df = pd.DataFrame(
    {'실제값':df['만족도'], '예측값':model.predict(), '잔차':model.resid}
)
print(result_df.head(10).round(3))

print(f'RSS : {model.ssr:.4f}')
print(f'MSE : {np.mean(model.resid ** 2):.4f}')
print(f'RMSE : {np.sqrt(np.mean(model.resid ** 2)):.4f}')

new_data = pd.DataFrame({'적절성':[3.123, 4.123, 5.123]})
new_pred = model.predict(new_data)
print(pd.DataFrame({'적절성':new_data['적절성'], '예측만족도':new_pred}).round(3))