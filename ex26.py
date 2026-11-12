
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from collections import Counter

# 1. 데이터 읽기
cancer = load_breast_cancer()
print(cancer.keys())

x, y = cancer.data, cancer.target

print(x[:2])
print(y[:2])
print(np.unique(y))
print(cancer.target_names)

print('악성 종양 수 : ', np.sum(y == 0))
print('양성 종양 수 : ', np.sum(y == 1))

# 2. 클래스 분포 확인
counter = Counter(y)
total = sum(counter.values())

for cls, cnt in counter.items():
    print(f'class {cls}:{cnt}개 ({cnt / total:.2f})')

# 3. train / test split
print()

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=12, stratify=y
)

y_li = y.tolist()
ytr_li = y_train.tolist()
yte_li = y_test.tolist()

print('전체 분포 : ', Counter(y_li))
print('train 분포 : ', Counter(ytr_li))
print('test 분포 : ', Counter(yte_li))

# 4. 개별 분류 모델 생성
print()

logi = make_pipeline(
    StandardScaler(),
    LogisticRegression(
        max_iter=1000,
        solver='lbfgs',
        random_state=12
    )
)

knn = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

tree = DecisionTreeClassifier(
    max_depth=5,
    random_state=12
)

# 5. VotingClassifier 생성
votingModel = VotingClassifier(
    estimators=[
        ('LR', logi),
        ('KNN', knn),
        ('DT', tree)
    ],
    voting='soft'
)

# 6. 개별 모델 정확도
named_models = [
    ('LR', logi),
    ('KNN', knn),
    ('DT', tree)
]

for name, clf in named_models:
    clf.fit(x_train, y_train)
    pred = clf.predict(x_test)

    print(f'{name} 정확도 : {accuracy_score(y_test, pred):.4f}')

# 7. 보팅 모델 정확도
votingModel.fit(x_train, y_train)

vpred = votingModel.predict(x_test)

print(f'votingModel 분류기 정확도 : {accuracy_score(y_test, vpred):.4f}')

# 8. 5겹 교차검증
print()

cvfold = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=12
)

cv_score = cross_val_score(
    votingModel, x_train, y_train,
    cv=cvfold, scoring='accuracy'
)

print(f'보팅 5겹 cv 정확도 평균 : {cv_score.mean():.4f} '
    f'(표준편차: +- {cv_score.std():.4f})')

# 9. 보팅 모델 상세 평가
print()

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

print('\n보팅 모델 상세 평가')

print(classification_report(y_test, vpred))

print('confusion_matrix : \n', confusion_matrix(y_test, vpred))

# 클래스 1(양성)의 예측 확률
vprob = votingModel.predict_proba(x_test)[:, 1]

print('roc_auc_score : ',
    roc_auc_score(y_test, vprob))
