# 이원 카이 제곱

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/smoke.csv")
print(data.head(3))
print(data.tail(3))
print(data['education'].unique())
print(data['smoking'].unique())

ctab = pd.crosstab(index=data['education'], columns=data['smoking'])
ctab.index = ['대학원졸', '대졸', '고졸']
ctab.columns = ['과흡연', '보통', '노담']
print(ctab)

# 이원카이제곱 검정 시작
chi_result = [ctab.loc['대학원졸'], ctab.loc['대졸'], ctab.loc['고졸']]
chi2, pv, dof, expected = stats.chi2_contingency

print(f"chi2:{chi2:.7f}, pv:{pv:.7f}, dof:{dof}")
print(f"expected:\n{expected}")

data = pd.DataFrame({
    "포카리스웨트":[30, 20],
    "칠성사이다":[20, 30],
    "비타오백":[10, 30]
}, index=["남성", "여성"])

print(data)

chi2, pv, dof, expected = stats.chi2_contingency(data)
print("p-value : ", pv)
print("chi2 : ", chi2)
print("dof : ", dof)
print("expected : ", expected)

import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
sns.heatmap(data=data, annot=True, fmt='d', cmap="Blues")
plt.title("성별에 따른 음료 선호 분석")
plt.xlabel("음료 종류")
plt.ylabel("성별")
plt.show()