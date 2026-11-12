# [로지스틱 분류분석 문제3]
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#    - Daily Time Spent on Site : 사이트 이용 시간 (분)
#    - Age : 나이,
#    - Area Income : 지역 소득,
#    - Daily Internet Usage :일별 인터넷 사용량(분),
#    - Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간 단위가 큰 경우 표준화 작업을 시도한다.
# 모델 성능 출력 : 정확도, 정밀도, 재현율, ROC 커브와 AUC 출력
# 새로운 데이터로 분류 작업을 진행해 본다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/advertisement.csv")
print(df.head(3))
print(df.info())
print(df.columns)
print(df.isnull().sum())

x = df[['Daily Time Spent on Site',
        'Age',
        'Area Income',
        'Daily Internet Usage']]

y = df['Clicked on Ad']

print(x[:3])
print(y[:3])
print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0
)

print('\ntrain / test split')
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

sc = StandardScaler()

sc.fit(x_train)

x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

print('\n표준화 결과')
print(x_train[:3])
print(x_test[:3])

print('\n분류 모델 생성 ----')

model = LogisticRegression(random_state=0)
model.fit(x_train, y_train)

y_hat = model.predict(x_test)

print('예측값 : ', y_hat[:10])
print('실제값 : ', y_test.values[:10])

print('\n혼동 행렬')
cm = metrics.confusion_matrix(y_test, y_hat)
print(cm)

acc = metrics.accuracy_score(y_test, y_hat)
precision = metrics.precision_score(y_test, y_hat)
recall = metrics.recall_score(y_test, y_hat)

print('\n모델 성능 평가')
print('정확도 : ', acc)
print('정밀도 : ', precision)
print('재현율 : ', recall)

cl_rep = metrics.classification_report(y_test, y_hat)
print('분류모델 성능 평가 보고서 : \n', cl_rep)

f_value = model.decision_function(x_test)

fpr, tpr, thresholds = metrics.roc_curve(
    y_test, f_value
)

auc = metrics.roc_auc_score(y_test, f_value)

print('\nAUC : ', auc)

plt.figure(figsize=(8, 5))

plt.plot(fpr, tpr, 'o-',
        label='LogisticRegression (AUC:%.3f)' % auc)

plt.plot([0, 1], [0, 1], 'k--',
        label='Random Classifier (AUC:0.5)')

plt.xlabel('FPR(위양성률)')
plt.ylabel('TPR(재현율)')
plt.title('ROC Curve')
plt.grid(True)
plt.legend()
plt.show()

print('\n새로운 데이터로 예측하기 ----')

site = float(input('사이트 이용 시간(분) : '))
age = int(input('나이 : '))
income = float(input('지역 소득 : '))
internet = float(input('일별 인터넷 사용량(분) : '))

newdf = pd.DataFrame({
    'Daily Time Spent on Site': [site],
    'Age': [age],
    'Area Income': [income],
    'Daily Internet Usage': [internet]
})

print('\n입력 데이터')
print(newdf)

new_scaled = sc.transform(newdf)

new_pred = model.predict(new_scaled)
new_prob = model.predict_proba(new_scaled)

print('\n예측 결과 : ', new_pred)
print('광고 클릭 확률 : ', new_prob[0][1])

if new_pred[0] == 1:
    print('광고를 클릭할 것으로 예측됩니다. (1)')
else:
    print('광고를 클릭하지 않을 것으로 예측됩니다. (0)')
