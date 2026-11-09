# pandas 문제 7)

#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성

#      - DataFrame의 자료를 파일로 저장

#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력

#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))

#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시

#      - 연봉 상위 20% 직원 출력  : quantile()
#      - SQL로 1차 필터링 후 pandas로 분석 

#             - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력

 

#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성

 

#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.

#      - pivot_table을 사용하여 성별 연봉의 평균을 출력

#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프

#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))

 

#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.

#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용

#      사번  직원명  부서명   직급  부서전화  성별

#      ...

#      인원수 : * 명

#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력



import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
from sqlalchemy import create_engine

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

conn = None

try: 
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay
        from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8mb4")
    df = pd.read_sql(sql, engine)
    df.columns = ['사번', '이름', '부서명', '직급', '성별', '연봉']
    print(df.head(3))

    pt = pd.pivot_table(df, index='성별', values='연봉', aggfunc='mean')
    print('성별 연봉의 평균 : \n', pt)
    print()

    pt.plot(kind='bar', legend=False, color=['steelblue', 'aqua'], rot=0)
    plt.title('성별 연봉이 평균')
    plt.xlabel('성별')
    plt.ylabel('연봉')
    plt.tight_layout()
    plt.show()

    ct = pd.crosstab(df['부서명'], df['성별'])
    print('부서명, 성별 교차 테이블 : \n', ct)
except Exception as e:
    print('처리 오류 : ', e)
finally:
    engine.dispose()