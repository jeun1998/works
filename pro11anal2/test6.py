import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/survey_method.csv")
print(data.head(3))
print(data['method'].unique())
print(data['survey'].unique())
ctab = pd.crosstab(index=data['method'], columns=data['survey'])
ctab.index = ["방법1","방법2","방법3"]
ctab.columns = ["매우만족","만족","보통","불만족","매우불만족"]
print(ctab)

chi2, pv, dof, expected = stats.chi2_contingency(ctab)
print(f"chi2:{chi2}, pv:{pv}, dof:{dof}")
print("expected: \n", expected)

print("--------------------------------------------")
data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/snsbyage.csv")
print(data2.head(3))
print(data2['age'].unique())
print(data2['service'].unique())
ctab2 = pd.crosstab(index=data['age'], columns=data['service'])
ctab2.index = ["20대","30대","40대"]
ctab2.columns = ["F","T","K","C","E"]
print(ctab2)

chi2, pv, dof, expected = stats.chi2_contingency(ctab)
print(f"chi2:{chi2}, pv:{pv}, dof:{dof}")
print("위 자료는 샘플 자료이지만 모집단이라 가정하고 샘플링 후 검정하기 ----")

print("--------------------------------------------")
print("전체 검수 : ", len(data2))
samp_data = data2.simple(n=500, replace=True, random_state=1) \
            .reset_index(drop=True)
print("샘플 건수 : ", len(samp_data))
ctab3 = pd.crosstab(index=data['age'], columns=data['service'])
ctab3.index = ["20대","30대","40대"]
ctab3.columns = ["F","T","K","C","E"]
print(ctab3)

chi2, pv, dof, expected = stats.chi2_contingency(ctab)
print(f"chi2:{chi2}, pv:{pv}, dof:{dof}")