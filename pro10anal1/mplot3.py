# seaborn : matplotlib의 기능 보충용, 통계 데이터 시각화에 특화

import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

titanic = sns.load_dataset('titanic')
print(titanic.info(max_cols=None))

sns.displot(titanic['age'])
plt.title('나이 차트')
plt.show()

sns.boxplot(y='age', data=titanic, palette='Paired')
plt.show()

sns.relplot(x='sex', y='age', data=titanic)
plt.show()

titanic_pivot = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
print(titanic_pivot)
sns.heatmap(titanic_pivot, cmap=sns.light_palette('gray'), annot=True, fmt='d')
plt.show()

import pandas as pd
data = [10,12,13,15,14,12,11,100]
df = pd.DataFrame({'score':data})
print(df)

q1 = df['score'].quantile(0.25)
q3 = df['score'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 - 1.5 * iqr

outliers = df[(df['score'] < lower_bound) | (df['score'] > upper_bound)]
filtered_df = df[(df['score'] >= lower_bound) & (df['score'] <= upper_bound)]

print('이상치 값 : ', outliers)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(y=df['score'], ax=axes[0], color='yellow')
axes[0].set_title('이상치 포함 데이터')
axes[0].set_ylabel('Score')
axes[0].grid(True)

plt.tight_layout()
plt.show()