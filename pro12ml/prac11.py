# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance


# 데이터 변수 설명 : 총 23개 변수가 사용됨.

# 여기서 종속변수(반응변수)는 class 이고 나머지 22개는 모두 입력변수(설명변수, 예측변수, 독립변수).
# 변수명 변수 설명
# class      edible = e, poisonous = p
# cap-shape    bell = b, conical = c, convex = x, flat = f, knobbed = k, sunken = s
# cap-surface  fibrous = f, grooves = g, scaly = y, smooth = s
# cap-color     brown = n, buff = b, cinnamon = c, gray = g, green = r, pink = p, purple = u, red = e, white = w, yellow = y
# bruises        bruises = t, no = f
# odor            almond = a, anise = l, creosote = c, fishy = y, foul = f, musty = m, none = n, pungent = p, spicy = s
# gill-attachment attached = a, descending = d, free = f, notched = n
# gill-spacing close = c, crowded = w, distant = d
# gill-size       broad = b, narrow = n
# gill-color      black = k, brown = n, buff = b, chocolate = h, gray = g, green = r, orange = o, pink = p, purple = u, red = e, white = w, yellow = y
# stalk-shape  enlarging = e, tapering = t
# stalk-root    bulbous = b, club = c, cup = u, equal = e, rhizomorphs = z, rooted = r, missing = ?
# stalk-surface-above-ring fibrous = f, scaly = y, silky = k, smooth = s
# stalk-surface-below-ring fibrous = f, scaly = y, silky = k, smooth = s
# stalk-color-above-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o, pink = p, red = e, white = w, yellow = y
# stalk-color-below-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o,pink = p, red = e, white = w, yellow = y
# veil-type      partial = p, universal = u
# veil-color     brown = n, orange = o, white = w, yellow = y
# ring-number none = n, one = o, two = t
# ring-type     cobwebby = c, evanescent = e, flaring = f, large = l, none = n, pendant = p, sheathing = s, zone = z
# spore-print-color black = k, brown = n, buff = b, chocolate = h, green = r, orange =o, purple = u, white = w, yellow = y
# population abundant = a, clustered = c, numerous = n, scattered = s, several = v, solitary = y
# habitat       grasses = g, leaves = l, meadows = m, paths = p, urban = u, waste = w, woods = d


# GaussianNB 문제 : 독버섯 / 식용버섯 분류

# GaussianNB : 독버섯 / 식용버섯 분류

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 데이터 읽기
df = pd.read_csv('mushrooms.csv')
print(df.head(3))
print(df.shape)
print(df['class'].value_counts())

# 독립변수와 종속변수
x = df.drop('class', axis=1)
labels = df['class']

# 문자형 데이터를 숫자로 변환
x = pd.get_dummies(x, dtype=int)

print(x.columns)
print(x.values[:5])
print(x.shape)

# 중요 변수 선택 (odor, spore-print-color 등)
selected = [col for col in x.columns
            if col.startswith(('odor_', 'spore-print-color_',
                            'gill-size_', 'gill-color_'))]

x = x[selected]
print('선택된 변수 : ', selected)

# 학습 / 테스트 데이터 분리
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, labels, test_size=0.2, random_state=12, stratify=labels
)

# GaussianNB 모델 생성 및 학습
model = GaussianNB()
model.fit(x_train, y_train)

pred = model.predict(x_test)
print('정확도 : ', accuracy_score(y_test, pred))

print()

# 테스트 데이터 2개로 예측
x_new = x_test.iloc[:2]
preds = model.predict(x_new)
probs = model.predict_proba(x_new)
class_names = model.classes_

for i, (pred, prob) in enumerate(zip(preds, probs)):
    prob_str = ", ".join([f'{cls}:{p:.4f}' for cls, p in zip(class_names, prob)])
    print(f'테스트 버섯 {i + 1} --> 예측:{pred} // 확률:[{prob_str}]')

print()
print('실제값 : ', y_test.iloc[:2].values)
