import numpy as np
import pandas as pd
import scipy.stats as stats
data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print("표본 평균 수명 : ", np.mean(data))
print("표본 크기 : ", len(data))

result = stats.shapiro(data)
print("shapiro result : ", result)
t_result = stats.ttest_1samp(data, popmean=300)
print("t_result : ", t_result)

print("--------------------------------")

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/one_sample.csv")
print(data2.head(3))

data2['time'] = data2['time'].astype(str).str.strip()
data2['time'] = pd.to_numeric(data2['time'], errors='coerce')
data2 = data2.dropna(subset=['time'])

print("표본 평균 사용 시간 : ", data2['time'].mean())
print("표본 크기 : ", len(data2))

result2 = stats.shapiro(data2['time'])
print("time에 대한 shapiro result : ", result2)

t_result2 = stats.ttest_1samp(data2['time'], popmean=5.2)
print("t_result2 : ", t_result2)

print("-----------------------------------------------------")

import numpy as np
import pandas as pd
import scipy.stats as stats
from pathlib import Path

file_path = Path(
    r"C:\Users\acorn\Downloads\개인서비스지역별_동향[2026-09월]1026-5시31분.xls"
)

print("파일 존재 여부:", file_path.exists())

xls = pd.ExcelFile(file_path, engine="xlrd")
print("시트 목록:", xls.sheet_names)

df = pd.read_excel(file_path, sheet_name=0, engine="xlrd", header=None)

print(df.head(15).to_string())

column_name = "미용료"

data = (
    df[column_name]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

data = pd.to_numeric(data, errors="coerce").dropna()


popmean = 15000
alpha = 0.05

print("\n=== 기초 통계 ===")
print("표본 크기:", len(data))
print("표본 평균:", data.mean())
print("표본 표준편차:", data.std())


if 3 <= len(data) <= 5000:
    shapiro_result = stats.shapiro(data)
    print("\nShapiro 검정:", shapiro_result)

t_result = stats.ttest_1samp(data, popmean=popmean)

print("\n=== 단일표본 t검정 ===")
print("t 통계량:", t_result.statistic)
print("p-value:", t_result.pvalue)

if t_result.pvalue < alpha:
    print("귀무가설 기각")
    print("평균 미용 요금은 15,000원과 통계적으로 유의한 차이가 있다.")
else:
    print("귀무가설 기각 실패")
    print("평균 미용 요금이 15,000원과 다르다고 판단할 충분한 증거가 없다.")
