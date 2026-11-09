# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.

# Django 또는 Flask 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.

 

#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)

#        : 부서번호, 직원명 순으로 오름 차순 정렬 

#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.

#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.

#    4) 성별, 직급별 빈도표를 출력하시오.

#    5) 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력 
#        출력 항목: 부서명, 직원명, 연봉
#    6) 부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율(%) 
#        비율 계산 (%)은 dept_ratio = (dept_count / total * 100).round(2)
#       결과를 DataFrame으로 출력
#       예: 총 인원: 30명
#            영업부 20%
#            총무부 30%
#            전산부 5%
#            ...


from flask import Flask, render_template
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import io
import base64

app = Flask(__name__)

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8mb4'
}

def get_connection():
    return pymysql.connect(**config)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/db")
def db():
    sql = """
        SELECT
            j.jikwonno AS 사번,
            j.jikwonname AS 직원명,
            b.busername AS 부서명,
            j.jikwonjik AS 직급,
            j.jikwonpay AS 연봉,
            TIMESTAMPDIFF(YEAR, j.jikwonibsail, CURDATE()) AS 근무년수,
            j.jikwongen AS 성별,
            b.buserno AS 부서번호
        FROM jikwon j
        INNER JOIN buser b
        ON j.busernum = b.buserno
        ORDER BY b.buserno ASC, j.jikwonname ASC
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            cols = [c[0] for c in cursor.description]

    df = pd.DataFrame(rows, columns=cols)

    
    df1 = df[
        ['사번', '직원명', '부서명', '직급', '연봉', '근무년수']
    ]
    table1 = df1.to_html(index=False)

    
    df2 = (
        df.groupby(['부서명', '직급'])['연봉']
        .agg(연봉합='sum', 연봉평균='mean')
        .round(2)
        .reset_index()
    )
    table2 = df2.to_html(index=False)

    
    df3 = (
        df.groupby('부서명')['연봉']
        .agg(연봉합='sum', 연봉평균='mean')
        .round(2)
    )

    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    df3['연봉합'].plot(
        kind='bar',
        ax=axes[0],
        color='steelblue',
        rot=0
    )
    axes[0].set_title('부서별 연봉 합계')
    axes[0].set_xlabel('부서명')
    axes[0].set_ylabel('연봉 합계')

    df3['연봉평균'].plot(
        kind='bar',
        ax=axes[1],
        color='orange',
        rot=0
    )
    axes[1].set_title('부서별 평균 연봉')
    axes[1].set_xlabel('부서명')
    axes[1].set_ylabel('평균 연봉')

    plt.tight_layout()

    
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    graph = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close(fig)

    
    df4 = pd.crosstab(
        df['성별'],
        df['직급'],
        margins=True
    )
    table4 = df4.to_html()

    
    df5 = (
        df.sort_values(
            by=['부서번호', '연봉', '사번'],
            ascending=[True, False, True]
        )
        .drop_duplicates(subset=['부서번호'])
        [['부서명', '직원명', '연봉']]
    )
    table5 = df5.to_html(index=False)

    
    dept_count = df.groupby('부서명').size()
    total = len(df)

    if total > 0:
        dept_ratio = (dept_count / total * 100).round(2)
    else:
        dept_ratio = dept_count.astype(float)

    df6 = pd.DataFrame({
        '직원수': dept_count,
        '비율(%)': dept_ratio
    }).reset_index()

    table6 = df6.to_html(index=False)

    return render_template(
        "db.html",
        table1=table1,
        table2=table2,
        graph=graph,
        table4=table4,
        table5=table5,
        table6=table6,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)
