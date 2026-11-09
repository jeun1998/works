
import numpy as np
import pandas as pd

# ==========================================
# 1. DataFrame 생성 및 stack(), unstack()
# ==========================================

df = pd.DataFrame(
    np.arange(6).reshape(2, 3),
    index=['대전', '서울'],
    columns=['2023', '2024', '2025']
)
print(df)

print()

# 열을 행 방향으로 변환
df_row = df.stack()
print(df_row)

print()

# 행으로 변환한 데이터를 다시 열로 변환
df_col = df_row.unstack()
print(df_col)


# ==========================================
# 2. 범주화 : pd.cut()
# ==========================================

print('\n범주화 ----------------')

price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]

result_cut = pd.cut(price, cut)
print(result_cut)

# 구간별 이름 지정
result_cut = pd.cut(
    price,
    bins=cut,
    labels=['저가', '중가', '고가']
)
print(result_cut)

# 범주별 데이터 개수 출력
print(pd.Series(result_cut).value_counts())


# ==========================================
# 3. Series 데이터 추출
# ==========================================

print('------')

datas = pd.Series(np.arange(1, 1001))

print(datas[:5])
print(datas.head())
print(datas.head(2))

print(datas[-2:])
print(datas.tail(2))


# ==========================================
# 4. groupby()와 agg() 함수
# ==========================================

print('\nagg 함수 : 범주의 그룹별 연산')

datas = pd.DataFrame({
    '부서': ['개발', '개발', '영업', '영업', '인사', '개발'],
    '이름': ['길동', '철수', '영희', '민수', '유리', '찬우'],
    '연봉': [4500, 4200, 4000, 4600, 3500, 3900],
    '성과점수': [90, 85, 70, 75, 88, 95]
})

print(datas)
print()

# 부서별 평균 연봉
print(datas.groupby('부서')['연봉'].mean())

# 부서별 직원 수
print(datas.groupby('부서')['이름'].count())

# 부서별 연봉과 성과점수 평균
print(datas.groupby('부서')[['연봉', '성과점수']].mean())

# 부서별 연봉 합계, 평균, 개수
print(datas.groupby('부서')['연봉'].agg(['sum', 'mean', 'count']))

# 부서를 기준으로 그룹화
group_col = datas.groupby('부서')

print('\n부서별 연봉 평균')
print(group_col['연봉'].mean())


# ==========================================
# 5. 사용자 정의 통계 함수
# ==========================================

data = pd.DataFrame({
    '연봉': [4500, 4200, 4000, 4600, 3500, 3900],
    '성과점수': [90, 85, 70, 75, 88, 95]
})

# 데이터의 개수, 평균, 표준편차, 최솟값 계산
def summaryFunc(gr):
    return {
        'count': gr.count(),
        'mean': gr.mean(),
        'std': gr.std(),
        'min': gr.min()
    }

# 연봉에 대한 기술통계량 출력
print('\n연봉 기술통계량')
print(summaryFunc(datas['연봉']))

# 성과점수에 대한 기술통계량 출력
print('\n성과점수 기술통계량')
print(summaryFunc(datas['성과점수']))

def summaryFunc(gr):
    return {
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
    }

print(data.apply(summaryFunc))
print('\nmerge : DataFrame 객체 병합')
df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)
print()
print(pd.merge(df1, df2, on='key'))
print()
print(pd.merge(df1, df2, on='key', how='inner'))
print()
print(pd.merge(df1, df2, on='key', how='outer'))
print()
print(pd.merge(df1, df2, on='key', how='left'))
print()
print(pd.merge(df1, df2, on='key', how='right'))

print()

df3 = pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(df3)
print(df1)
print(pd.merge(df1, df3, left_on='key', right_on='key2'))

print('----- concat : 상하 또는 좌우 ----------------')
print(pd.concat([df1, df3], axis=0))
print()
print(pd.concat([df1, df3], axis=1))

print('\nPIVOT 연산 : pivot과 groupby 명령의 중간적 성격')
data = {'city':['강남','강북','강남','강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }
df = pd.DataFrame(data)
print(df)
print(df['pop'].describe())
print()
print(df.pivot_table(index=['city']))
print(df.pivot_table(index=['city'], aggfunc='mean'))
print(df.pivot_table(index=['city','year'], aggfunc=[len,'sum']))

print(df.pivot_table(index=['city'], values='pop'))
print(df.pivot_table(index=['city'], values='pop', aggfunc='mean'))
print(df.pivot_table(index=['city'], values='pop', aggfunc=len))
print()
print(df.pivot_table(index=['year'], values='pop', columns=['city']))
print(df.pivot_table(index=['year'], values='pop', columns=['city'], margins=True))
print(df.pivot_table(index=['year'], values='pop', columns=['city'], margins=True, fill_value=0))

print()
hap = df.groupby(['city'])
print(hap)
print(hap.sum())
print(df.groupby(['city'].sum()))
print(df.groupby(['city'].mean()))