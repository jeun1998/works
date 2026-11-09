import pandas as pd

# 1. CSV 파일 읽기
df = pd.read_csv('sales_data.csv')

# 2. pivot_table을 이용하여 날짜/제품별 판매수량 합 요약
output_df = df.pivot_table(
    index='날짜',      # 행(Row) 위치에 둘 열
    columns='제품',    # 열(Column) 위치에 둘 열
    values='판매수량',  # 집계할 데이터 열
    aggfunc='sum'     # 집계 함수 (합계)
)

# 3. 결과 출력
print(output_df)
