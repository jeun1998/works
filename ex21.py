from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123)

print(x[:3], x.shape)
print(y[:3], y.shape)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('y_hat : ', y_hat[:10])
print('real : ', y[:10])

f_value = model.decision_function(x)
print('f_value : ', f_value[:100])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f', 'y_hat', 'y'])
print(df.head())

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
acc = (44 + 44) / 100
recall = 44 / (44 + 4)
precision = 44 / (44 + 8)
specificity = 44 / (44 + 8)
fallout = 8 / (8 + 44)
print('acc : ', acc)
print('recall : ', recall)
print('precision : ', precision)
print('specificity : ', specificity)
print('fallout : ', fallout)
print('fallout : ', 1 - specificity)

print()
from sklearn import metrics
acc_score = metrics.accuracy_score(y, y_hat)
print('acc(정확도) : ', acc_score)

cl_rep = metrics.classification_report(y, y_hat)
print('분류모델 성능 평가 보고서 : \n', cl_rep)

# Precision : 예측한 것 중 맞힌 비율 (예측의 정확성)
# Recall    : 실제 정답 중 찾아낸 비율 (정답 탐지 능력)
# F1-score  : Precision과 Recall의 조화평균
# Support   : 실제 클래스별 데이터 개수
# Accuracy  : 전체 데이터 중 올바르게 분류한 비율
# Macro avg : 클래스별 성능의 단순평균
# Weighted avg : 클래스별 데이터 개수를 고려한 가중평균

f_value = model.decision_function(x)
print('f_value : ', f_value[:10])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f', 'y_hat', 'y'])
print(df.head())
fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0, 1], [0, 1], 'k--', label='landom classifier line(AUC:0.5)')

i=3
plt.plot([fpr[i]], [tpr[i]], 'ro', ms=6, label='선택한 임계값')

plt.xlabel('fpr(위양성률)')
plt.xlabel('tpr(재현률)')
plt.title('ROC Curve')
plt.legend()
plt.show()

print('AUC : ', metrics.auc(fpr, tpr))