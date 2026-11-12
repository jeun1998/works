
# 과적합 방지 방법 이해
# train / test split
# k-fold : 안정적 평가
# gridsearchcv : 최적의 하이퍼파라미터 검색

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold
import numpy as np

iris = load_iris()
print(iris.keys())

train_data = iris.data
train_label = iris.target

print(train_data[:3])
print(train_label[:3])

# 1. 전체 데이터로 학습 및 평가
df_clf = DecisionTreeClassifier()
df_clf.fit(train_data, train_label)

pred = df_clf.predict(train_data)

print('예측값 : ', pred)
print('실제값 : ', train_label)
print('분류 정확도 : ', accuracy_score(train_label, pred))


# 2. train / test split
print('\n과적합 방지 목적 처리 1 : train / test split')

x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=12
)

df_clf.fit(x_train, y_train)

pred2 = df_clf.predict(x_test)

print('예측값 : ', pred2)
print('실제값 : ', y_test)
print('분류 정확도 : ', accuracy_score(y_test, pred2))


# 3. KFold 교차 검증
print('\n과적합 방지 목적 처리 2 : 교차 검증')

features = iris.data
label = iris.target

df_clf2 = DecisionTreeClassifier(
    criterion='gini',
    max_depth=3,
    random_state=12
)

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

cv_acc = []
n_iter = 0

print('iris shape : ', features.shape)

for train_index, test_index in kfold.split(features):

    xtrain = features[train_index]
    xtest = features[test_index]

    ytrain = label[train_index]
    ytest = label[test_index]

    df_clf2.fit(xtrain, ytrain)

    pred = df_clf2.predict(xtest)

    n_iter += 1

    acc = np.round(accuracy_score(ytest, pred), 5)

    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]

    print(f'반복수:{n_iter}, 교차검증 정확도:{acc}, '
        f'학습데이터크기:{train_size}, 검증크기:{test_size}')

    print(f'반복수:{n_iter}, 검증데이터 인덱스:{test_index}')

    cv_acc.append(acc)

print('cv_acc : ', np.array(cv_acc).astype(float))
print('평균 검증 정확도 : ', np.mean(cv_acc))

print('\n과적합 방지 목적 처리 2-1 : 교차 검증 단순화 함수 사용')
from sklearn.model_selection import cross_val_score
data = iris.data
label = iris.target

score = cross_val_score(df_clf2, data, label, scoring='scoring', cv=5)
print('교차 검증별 정확도 : ', np.round(score, 3))
print('평균 검증 정확도 : ', np.round(np.mean(score), 3))