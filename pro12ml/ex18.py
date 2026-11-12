# 독립변수 : 연속형, 종속변수 : 범주형
# 참고 : LogisticRegression을 근거로 뉴럴넷의 뉴런이 사용

import statsmodels.api as sm

mtcarsdata = sm.datasets.get_rdataset('mtcars')
print(mtcarsdata.keys())
mtcars = mtcarsdata.data
print(mtcars.head(2))
print(mtcars.info())
print()

mtcar = mtcars.loc[:, ['mpg','hp','am']]
print(mtcar.head(3))
print(mtcar['am'].unique())

import numpy as np
import statsmodels.formula.api as smf

formula = 'am ~ hp + mpg'
result = smf.logit(formula=formula, data=mtcar).fit()
print(result.summary())

pred = result.predict(mtcar[:10])
print('예측값 : ', pred.values)
print('예측값 : ', np.around(pred.values))
print('실제값 : ', mtcar['am'][:10].values)

print()
print('수치에 대한 집계표(혼동 행렬)')
conf_tab = result.pred_table()
print(conf_tab)
print('분류 정확도 : ', (16 + 10) / len(mtcar))
print('분류 정확도 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))

pred2 = result.predict(mtcar)
from sklearn.metrics import confusion_matrix, accuracy_score
pred_class = (pred2 > 0.5).astype(int)
conf_mat = confusion_matrix(mtcar['am'], pred_class)
print('confusion_matrix 혼동행렬 :\n', conf_mat)
print('분류 정확도 : ', (conf_mat[0][0] + conf_mat[1][1]) / len(mtcar))
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(pred2)))

print('**' * 10)
result2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()
print(result2.summary())
glm_pred = result2.predict(mtcar[:10])
print('glm 예측값 : ', np.around(glm_pred.values))
print('glm 실제값 : ', mtcar['am'][:10].values)

glm_pred2 = result2.predict(mtcar)
print('glm 분류 정확도 : ', accuracy_score(mtcar['am'], np.around(glm_pred2)))

print('새로운 값으로 예측하기 ----')
import pandas as pd
newdf = pd.DataFrame()
newdf['mpg'] = [10, 50, 120, 130]
newdf['hp'] = [100, 110, 80, 130]
print(newdf)
new_pred = result2.predict(newdf)
print('예측결과 : ', np.around(new_pred.values))
print('예측결과 : ', np.rint(new_pred.values))

# 머신러닝의 표용성
# 머신러닝 모델을 평가할 때는 훈련 데이터의 100% 정확도라는 숫자에 집착하기보다,
# "이 모델이 현실의 불확실성과 다양한 변수를 얼마나 유연하게 표용할 수 있는가?"를
# 고려해야 함. 수학에서는 100%의 답을 원하지만 ML은 정확도가 95%가 될지라도
# 주변 값을 포용하도록 하는 것이 중요하다.
# 예를 들어 고양이 분류 모델인 경우 꼬리가 없는 고양이도 분류할 수 있어야 한다.

