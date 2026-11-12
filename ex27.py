import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/titanic_data.csv")
print(df.head(2))
print(df.info())
print(df.shape)
print(df.isnull().any())

df = df.dropna(subset=['Pclass','Age', 'Sex'])
print(df.shape)
df_x = df[['Pclass', 'Age', 'Sex']]
print(df_x.head(3))

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df_x['Sex'] = df_x['Sex'].astype('object')
df_x['Sex'] = encoder.fit_transform(df_x['Sex'])
print(df_x.head(3))

df_y = df['Survived']
print(df_y.head(3))
print()
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.3, random_state=1)
print()

model = RandomForestClassifier(criterion='gini', n_estimators=500, random_state=12)
print(model)
model.fit(train_x, train_y)
pred = model.predict(test_x)
print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))
print('맞춘 갯수 : ', sum(test_y == pred))
print('전체 대비 맞춘 비율 : ', sum(test_y == pred) / len(test_y))
print('분류 정확도 : ', accuracy_score(test_y, pred))

cross_vali = cross_val_score(model, df_x, df_y, cv=5)
print(cross_vali)
print('교차 검증 평균 정확도 : ', np.round(np.mean(cross_vali), 4))

print('중요 변수 확인하기 --- ')
print('특성(변수, feature) 중요도 : ', model.feature_importances_)

import matplotlib.pyplot as plt
import koreanize_matplotlib
n_features = df_x.shape[1]
plt.barh(range(n_features), model.feature_importances_, align='center')
plt.xlabel('변수별 중요도 점수')
plt.ylabel('독립 변수')
plt.show()
plt.close()

print('전체 변수 대상으로 중요도 확인')
df_imsi = df[['Pclass', 'Age', 'Sex', 'Fare', 'SibSp', 'Parch']].copy()
df_imsi['Sex'] = df.imsi['Sex'].astype('object')
df_imsi['Sex'] = encoder.fit_transform(df_imsi['Sex'])
train_x, test_x, train_y, test_y = train_test_split(df_imsi, df_y, test_size=0.3, random_state=1)
model.fit(train_x, train_y)

importances = model.feature_importances_

feature_df = pd.DataFrame({
    'feature':df_imsi.columns,
    'importance':importances
}).sort_values(by='importance', ascending=False)
print(feature_df)