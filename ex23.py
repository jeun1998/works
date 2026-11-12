from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

x = [[180,15],[177,42],[156,35],[174,65],[161,25],[160,45],[170,65],[155,55],[180,15],[176,32]]
y = ['man','woman','woman','man','woman','woman','man','woman','man','man']
print(x)
print(y)
feature_names = ['height', 'hair_length']
class_names = ['man', 'woman']

model = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
model.fit(x, y)

print('예측값 : ', model.predict(x))
print('실제값 : ', y)
print(f'정확도 : {model.score(x, y)}')

new_data = [[177, 78]]
print('new_data pred : ', model.predict(new_data))
plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=feature_names,
            class_names=model.classes_, filled=True,
            rounded=True, fontsize=12)
plt.title('Decision Tree')
plt.show()