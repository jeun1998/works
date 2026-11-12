# [로지스틱 분류분석 문제2] 

# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.

# 안경 : 값0(착용X), 값1(착용O)

# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv

# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import metrics


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv")
print(df.head(3))
print(df.info())
print(df['안경유무'].unique())