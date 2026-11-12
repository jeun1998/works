# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)

# dataset은 winequality-red.csv 

# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
 

# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv('winequality-red.csv')
print(df.head(3))
print(df.info())
print(df.shape)
print(df.isnull().sum())

print('\n품질 점수별 개수')
print(df['quality'].value_counts().sort_index())

x = df.drop('quality', axis=1)
y = df['quality']
print('\n독립변수')
print(x.head(3))
print('\n종속변수')
print(y.head(3))
print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)

print('\ntrain / test split')
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=12
)
model.fit(x_train, y_train)

pred = model.predict(x_test)
print('\n예측값 : ', pred[:20])
print('실제값 : ', y_test.values[:20])
print('\n분류 정확도 : ', accuracy_score(y_test, pred))
print('\n혼동 행렬')
print(confusion_matrix(y_test, pred))
print('\n분류모델 성능 평가 보고서')
print(classification_report(y_test, pred, zero_division=0))
print('\n5겹 교차검증')
cv_score = cross_val_score(
    model, x_train, y_train,
    cv = 5, scoring='accuracy'
)
print('교차검증 정확도 : ', cv_score)
print('평균 검증 정확도 : ', np.mean(cv_score))
print('n변수 중요도')

importance = model.feature_importances_
df_imp = pd.DataFrame({
    '변수': x.columns,
    '중요도': importance
})

df_imp = df_imp.sort_values('중요도', ascending=False)
print(df_imp)

plt.figure(figsize=(10, 6))
plt.barh(df_imp['변수'], df_imp['중요도'])
plt.xlabel('변수 중요도')
plt.ylabel('와인 특성')
plt.title('Randomforest 변수 중요도')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

print('\n 새로운 데이터 예측하기 ---')

newdf = x.iloc[[0]].copy()
print('새로운 입력 데이터')
print(newdf)
new_pred = model.predict(newdf)
print('예측한 와인 품질 점수 : ', new_pred[0])