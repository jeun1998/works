
# [XGBoost 문제] 

# kaggle.com이 제공하는 'glass datasets'          testdata 폴더 : glass.csv

# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7 가지의 label(Type)로 분리된다.

# RI	Na	Mg	Al	Si	K	Ca	Ba	Fe	
#  Type

#                           ...

# glass.csv 파일을 읽어 분류 작업을 수행하시오.

# XGBoost 문제 : Glass 데이터 분류

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

# 1. 데이터 읽기
url = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/glass.csv"
df = pd.read_csv(url)

print(df.head(3))
print(df.info())
print(df.shape)
print(df.isnull().sum())

# 2. Type별 데이터 개수
print('\n유리 종류별 개수')
print(df['Type'].value_counts().sort_index())

# 3. 독립변수와 종속변수
x = df.drop('Type', axis=1)
y = df['Type']

print('\n독립변수')
print(x.head(3))
print('\n종속변수')
print(y.head(3))

# 4. 종속변수 인코딩
# 원래 Type : 1, 2, 3, 5, 6, 7
# 변환 Type : 0, 1, 2, 3, 4, 5

encoder = LabelEncoder()
y = encoder.fit_transform(y)

print('\n변환된 Type : ', np.unique(y))
print('원래 Type : ', encoder.classes_)

# 5. train / test split (8:2)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)

print('\ntrain / test split')
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

# 6. XGBoost 모델 생성
model = XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    objective='multi:softprob',
    random_state=12,
    eval_metric='mlogloss'
)

# 모델 학습
model.fit(x_train, y_train)

# 7. 예측
pred = model.predict(x_test)

# 원래 Type 번호로 복원
pred_original = encoder.inverse_transform(pred)
y_test_original = encoder.inverse_transform(y_test)

print('\n예측값 : ', pred_original[:20])
print('실제값 : ', y_test_original[:20])

# 8. 모델 성능 평가
print('\n분류 정확도 : ', accuracy_score(y_test, pred))

print('\n혼동 행렬')
print(confusion_matrix(y_test_original, pred_original))

print('\n분류모델 성능 평가 보고서')
print(classification_report(
    y_test_original, pred_original,
    zero_division=0
))

# 9. 변수 중요도
importance = model.feature_importances_

df_imp = pd.DataFrame({
    '변수': x.columns,
    '중요도': importance
})

df_imp = df_imp.sort_values('중요도', ascending=False)

print('\n변수 중요도')
print(df_imp)

# 10. 변수 중요도 시각화
plt.figure(figsize=(9, 5))

plt.barh(df_imp['변수'], df_imp['중요도'])
plt.gca().invert_yaxis()

plt.xlabel('변수 중요도')
plt.ylabel('유리 특성')
plt.title('XGBoost 변수 중요도')

plt.tight_layout()
plt.show()

# 11. 새로운 데이터로 분류
print('\n새로운 데이터로 예측하기 ----')

newdf = pd.DataFrame(
    [[1.52101, 13.64, 4.49, 1.10, 71.78,
    0.06, 8.75, 0.0, 0.0]],
    columns=x.columns
)

print(newdf)

new_pred = model.predict(newdf)
new_type = encoder.inverse_transform(new_pred)

print('예측한 유리 종류(Type) : ', new_type[0])
