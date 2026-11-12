# SVM 모델로 이미지 분류

from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import numpy as np
import pandas as pd


faces = fetch_lfw_people(min_faces_per_person=60, color=False, resize=0.5)
# print(faces.DESCR)
print(faces.data.shape)
print(faces.target)
print(faces.target_names)
print(faces.images.shape)
print()
print(faces.images[1])
print(faces.target_names[faces.target[1]])
plt.imshow(faces.images[1], cmap='bone')
plt.show()

fig, ax = plt.subplots(3, 5)
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[],
            xlabel=faces.target_names[faces.target[i]])
plt.show()

pca = PCA(n_components=0.95)
x_pca = pca.fit_transform(faces.data)
print(pca.n_components_)

n = 150
m_pca = PCA(n_components = n, whiten=True, random_state=0)
x_low = m_pca.fit_transform(faces.data)
print('x_low : ', x_low, ' ', x_low.shape)

fig, ax = plt.subplots(3, 5, figsize=(10, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(m_pca.components_[i].reshape(faces.images[0].shape), cmap='bone')
    axi.axis('off')
    axi.set_title(f'pc {i + 1}')
plt.suptitle('주성분 얼굴', fontsize=12)
plt.tight_layout()
plt.show()

print('주성분 설명력 : \n', m_pca.explained_variance_ratio_[:10])
print('누적 설명력 : ', m_pca.explained_variance_ratio_.sum())

x_reconst = m_pca.inverse_transform(x_low)
fig, ax = plt.subplots(2, 5, figsize=(10, 4))
for i in range(5):
    ax[0, i].imshow(faces.images[i], cmap='bone')
    ax[0, i].set_title('원본')
    ax[0, i].axis('off')

    ax[1, i].imshow(x_reconst[i].reshape(faces.images[0].shape), cmap='bone')
    ax[1, i].set_title('원본')
    ax[1, i].axis('off')

plt.suptitle('PCA 복원 비교', fontsize=12)
plt.tight_layout()
plt.show()

print()
svcmodel = SVC(C=1.0, random_state=1)
mymodel = make_pipeline(m_pca, svcmodel)
print('mymodel : ', mymodel)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    faces.data, faces.target, random_state=1, stratify=faces.target
)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[0])
print(y_train[0])

mymodel.fit(x_train, y_train)
pred = mymodel.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10])

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
confmat = confusion_matrix(y_test, pred)
print('confusion_matrix : \n', confmat)
print('accuracy : ', accuracy_score(y_test, pred))
print('classification_report : \n', classification_report(y_test, pred, \
                        target_names = faces.target_names))

print('분류 결과 시각화')
fig, axes = plt.subplots(4, 6)
for i, ax in enumerate(axes.flat):
    ax.imshow(x_test[i].reshape(faces.images.shape[1:]), cmap='bone')
    ax.set(xticks=[], yticks=[])
    ax.set_ylabel(faces.target_names[pred[i]].split()[-1], \
            color = 'blue' if pred[i] == y_test[i] else 'red',
            fontweight = 'bold')

fig.suptitle('예측 결과', fontsize=12)
plt.tight_layout()
plt.show()

import seaborn as sns
sns.heatmap(confmat, annot=True, fmt='d', cmap='Blues',
            xticklabels=faces.target_names, yticklabels=faces.target_names)
plt.xlabel('예측')
plt.ylabel('실제')
plt.title('혼동행렬')
plt.show()

print('\n새로운 이미지를 입력해 분류하기')
# 실습 1 : 기존 이미지로 분류 예측
test_img = faces.data[0].reshape(1, -1)
print('test_img : ', test_img)
test_pred = mymodel.predict(test_img)
print('실습 1 예측결과 : ', faces.target_names[test_pred[0]])
print('실습 1 제값 : ', faces.target_names[faces.target[0]], ', index:', faces.target[0])

# 실습 2 : 완전 새로운 이미지로 분류 예측

from PIL import Image
img = Image.open('bush.jpeg')
img = img.convert('L')
img = img.resize((47, 62))
img_np = np.array(img)
print('img_np : ', img_np)
img_flat = img_np.reshape(1, -1)
new_pred = mymodel.predict(img_flat)
print('실습 2 예측결과 : ', faces.target_names[new_pred[0]],
        ' index : ', new_pred[0])

plt.imshow(img_np, cmap='bone')
plt.title(f'예측 : {faces.target_names[new_pred[0]]}')
plt.axis('off')
plt.show()