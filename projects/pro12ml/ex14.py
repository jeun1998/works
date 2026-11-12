import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

iris = load_iris()
print(iris.keys())

pd.set_option('display.max_columns', None)
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df.head(2))
print(iris_df.shape)

train_set, test_set = train_test_split(iris_df, test_size=0.3, random_state=12)
print(train_set.shape, test_set.shape)
# print(train_set.head(3))
# print(test_set.head(3))
print(train_set.iloc[:, [2]])
print(train_set.iloc[:, [3]])

model_linear = LinearRegression().fit(
    X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]]
)

print('slope : ', model_linear.coef_)
print('bias : ', model_linear.intercept_)
pred = model_linear.predict(test_set.iloc[:, [2]])
print('예측값 : ', np.round(pred[:5].flatten(), 1))
print('실제값 : ', test_set.iloc[:, [3]][:5].values.flatten())
print(f'r2_score(결정계수) : {r2_score(test_set.iloc[:, [3]], pred)}')
plt.plot(np.array(test_set.iloc[:, [2]]), model_linear.predict(test_set.iloc[:, [2]]))
plt.show()