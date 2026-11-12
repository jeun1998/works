# decision tree

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

x, y = make_classification(n_samples=100, n_features=2,
                        n_redundant=0, n_informative=2,random_state=42)

print(x[:3])
print(y[:3])

model = DecisionTreeClassifier(criterion='gini', max_depth=3)
model.fit(x, y)

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=['x1', 'x2'], class_names=['0','1'], filled=True)
plt.show()

xx, yy = np.meshgrid(   # x축, y축 값을 조합해서 좌표격자를 생성
    np.linspace(x[:, 0].min(), x[:, 0].min(), 100),
    np.linspace(x[:, 1].min(), x[:, 1].min(), 100)
)

z = model.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
print(z)

plt.contour(xx, yy, z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.title('Decision Boundry')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
