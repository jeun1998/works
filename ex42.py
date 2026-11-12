import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression

data = load_breast_cancer()
x = data.data
y = data.target
print(x[:1], ' ', x.shape)
print(y[:1], ' ', np.unique(y))

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# 스케일링 필요
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

train_acc = []
test_acc = []
k_range = range(3, 12, 2)

for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train_scaled, y_train)
    y_train_pred = model.predict(x_train_scaled)
    y_test_pred = model.predict(x_test_scaled)
    train_acc.append(accuracy_score(y_train, y_train_pred))
    test_acc.append(accuracy_score(y_test, y_test_pred))

print(train_acc)
print(test_acc)

best_idx = np.argmax(test_acc)
best_k = list(k_range)[best_idx]
best_acc = test_acc[best_idx]
print('최적의 k값 : ', best_k)
print('최고 정확도 : ', best_acc)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(k_range, train_acc, marker='o', c='b', label='train_acc')
plt.plot(k_range, test_acc, marker='s', c='r', label='test_acc')
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()