# 고수주의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 ... 등을 제공
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([3, 7, -5, 4, '일'])
print(obj, type(obj))

print()
obj2 = pd.Series([3, 7, -5, 4], index = ['a','b','c','d'])
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2))
print(obj2.std())

print(obj2.index)
print(obj2.values)
print(obj2['a'])
print(obj2[['a']])

print(obj2[['a', 'b']])
print(obj2['a':'c'])

print()
print(obj2.iloc[2])
print(obj2.loc['c'])

print()
print(obj2[1:3])
print(obj2.iloc[[2, 1]])
print(obj2.iloc[[1, 2]])

print()
print('a' in obj2)
print('k' in obj2)

print('\n파이썬 dict 자료를 Series 객체로 생성')
names = {'mouse':5000, 'keyboard':35000, 'monitor':5500}
print(names, type(names))
obj3 = Series(names)
print(obj3, type(obj3))

obj3.name = '상품가격'
print(obj3)
print('-------------------------------------------------')

df = pd.DataFrame(obj3)
print(df, type(df))
print()
data = {
    'irum':['홍길동','한국인','신기해','공기밥','한가해'],
    'juso':('역삼동','신당동','역삼동','역삼동','신사동'),
    'nai':[23, 25, 33, 30, 35]
}
frame = pd.DataFrame(data)
print(frame)

print()
print(frame['irum'], type(frame['irum']))
print(frame.irum, type(frame.irum))

print(DataFrame(data=data, columns=['juso','irum','nai']))

frame2 = pd.DataFrame(data, columns=['irum','nai','juso','tel'], index=['a','b','c','d','e'])
print(frame2)
val = pd.Series(['222-2222','333-3333','444-4444'], index=['b','c','e'])
print(val)
print()
frame['tel'] = val
print(frame2)

print()
print(frame.T)

print()
print(frame2.values, type(frame2.values))
print(frame2.values[0, 1])
print(frame2.values[0:2])
print()

frame3 = frame2.drop('d')
print(frame3)

frame4 = frame2.drop('tel', axis=1)
print(frame4)

print('------------------------')
print(frame2)
print(frame2.sort_index(axis=0, ascending=False))
print(frame2.sort_index(axis=1, ascendint=True))
print()
print(frame2.rank(axis=0))

counts = frame2['juso'].value_counts()
print(counts)

data = {
    'juso':['서초구 서초2동', '강남구 역삼동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
fr = pd.DataFrame(data)
print(fr)

result1 = Series(x.split()[0] for x in fr.juso)
result2 = Series(x.split()[1] for x in fr.juso)
print(result1)
print(result2)
print(result1.value_counts)