import pandas as pd


df = pd.read_csv('sales_data.csv')

df = df.pivot_table(
    index='날짜',      # 행(Row) 위치에 둘 열
    columns='제품',    # 열(Column) 위치에 둘 열
    values='판매수량',  # 집계할 데이터 열
    aggfunc='sum'     # 집계 함수 (합계)
)

print(df)
