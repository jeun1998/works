# [로지스틱 분류분석 문제2] 

# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.

# 안경 : 값0(착용X), 값1(착용O)

# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv

# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import metrics


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv")
print(df.head(3))
print(df.info())
print(df['안경유무'].unique())

x = df[['게임', 'TV시청']]
y = df['안경유무']

print(x[:3])
print(y[:3])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0
)

print('\ntrain / test split')
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

model = LogisticRegression(random_state=0)
model.fit(x_train, y_train)

y_hat = model.predict(x_test)

print('\n예측값 : ', y_hat)
print('실제값 : ', y_test.values)
print('예측 확률 : ')
print(model.predict_proba(x_test))
print('\n혼동 행렬')
cm = confusion_matrix(y_test, y_hat, labels=[0, 1])
print(cm)

acc = accuracy_score(y_test, y_hat)
print('분류 정확도 : ', acc)


cl_rep = metrics.classification_report(
    y_test, y_hat, labels=[0, 1], zero_division=0
)

print('분류모델 성능 평가 보고서 : \n', cl_rep)

print('\n새로운 값으로 예측하기 ----')

game = float(input('게임 시간 입력 : '))
tv = float(input('TV 시청 시간 입력 : '))

if game >= 0 and tv >= 0:

    newdf = pd.DataFrame({
        '게임': [game],
        'TV시청': [tv]
    })

    print(newdf)

    new_pred = model.predict(newdf)
    new_prob = model.predict_proba(newdf)

    print('예측 결과 : ', new_pred)
    print('예측 확률 : ', new_prob)

    if new_pred[0] == 1:
        print('안경 착용으로 분류됩니다. (1)')
    else:
        print('안경 미착용으로 분류됩니다. (0)')

else:
    print('0 이상의 값을 입력하세요.')
