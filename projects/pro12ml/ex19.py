import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv")
print(data.head(2), data.shape)
print(data.info())
df = pd.DataFrame()
df = data.drop(['Date', 'RainToday'], axis=1)
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(df.head(2), df.shape)
print(df['RainTomorrow'].unique())
print('데이터 분리 : 학습용(train dataset), 검증용(test dataset)')
train, test = train_test_split(df, test_size=0.3, random_state=42)
print(train.shape, test.shape)
print(test.head(3))

col_select = "+".join(train.columns.difference(['RainTomorrow']))
print(col_select)
my_formula = 'RainTomorrow ~' + col_select
model = smf.logit(formula=my_formula, data=train).fit()
print(model.summary())
print(model.params)
print()
print('예측값 : ', np.rint(model.predict(test)[:5].values))
print('실제값 : ', test['RainTomorrow'][:5].values)

pred_mat = model.pred_table()
print(pred_mat)
print('분류 정확도 : ', (pred_mat[0][0] + pred_mat[1][1]) / len(train))

from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(test)
conf_mat = confusion_matrix(test['RainTomorrow'], np.rint(pred))
print(conf_mat)
print('분류 정확도 : ', (conf_mat[0][0] + conf_mat[1][1]) / len(test))
print('분류 정확도 : ', accuracy_score(test['RainTomorrow'], np.rint(pred)))
print('분류 정확도 : ', accuracy_score(test['RainTomorrow'], (pred >= 0.5).astype(int)))