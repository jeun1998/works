# pro10anal1 — NumPy·Pandas·시각화·크롤링·형태소 분석

> **학습 목표:** 여러 형식의 데이터를 수집·전처리·집계하고 그래프와 텍스트 분석 결과로 표현한다.

## 1. NumPy 핵심 이론

- `ndarray`: 동일 타입의 다차원 배열. `shape`, `ndim`, `dtype`으로 구조를 파악한다.
- **벡터화(vectorization):** Python 반복문 대신 배열 연산으로 한 번에 계산하는 방식.
- **브로드캐스팅(broadcasting):** 호환 가능한 서로 다른 모양의 배열끼리 연산하는 규칙.
- `reshape`, `axis`, 슬라이싱, 불리언 인덱싱, `dot`/`@` 연산은 중요하다.
- 로그 변환(`log`, `log1p`)은 오른쪽으로 긴 분포의 규모 차이를 줄일 때 사용할 수 있지만 0·음수 등 입력 범위를 고려한다.

```python
import numpy as np
arr = np.arange(12).reshape(3, 4)
print(arr.sum(axis=0))   # 열별 합계
print(arr.mean(axis=1))  # 행별 평균
```

## 2. Pandas 핵심 이론

- `Series`: 레이블이 있는 1차원 자료구조. `DataFrame`: 표 형태의 2차원 자료구조.
- `loc`는 레이블 기반, `iloc`는 정수 위치 기반 선택이다.
- 결측치: `isna()`, `dropna()`, `fillna()`.
- 집계: `groupby().agg()`, `value_counts()`, `pivot_table()`, `pd.crosstab()`.
- 자료 변형: `stack()`, `unstack()`, `melt()`, `cut()`.
- 정렬·필터: `sort_values()`, 조건식, `query()`.
- 자료 교환: `read_csv()`, `read_excel()`, `read_json()`, `read_sql()`, `to_csv()`.

```python
import pandas as pd
sales = pd.DataFrame({'부서':['A','A','B'], '판매':[10,20,15]})
print(sales.groupby('부서')['판매'].agg(['sum','mean']))
```

### 데이터 분석 표준 절차

```text
문제 정의 → 데이터 수집 → 자료형/결측치 확인 → 정제·변환
→ 탐색적 데이터 분석(EDA) → 시각화·집계 → 결과 해석
```

## 3. 수집·파싱·시각화 이론

### ① Matplotlib·Seaborn
- 막대그래프: 범주별 규모 비교. 히스토그램: 수치형 분포. 산점도: 두 연속형 변수 관계. 박스플롯: 중앙값·사분위수·이상치 관찰.
- `fig, ax = plt.subplots()`는 Figure와 Axes를 분리해 여러 그래프를 구성하기 좋다.
- 시각화 전 단위, 결측값, 범주 순서, 한글 폰트를 확인한다.

### ② XML·JSON·HTML 파싱
- CSV는 행·열 기반, JSON은 객체/배열 기반, XML은 태그 계층 구조다.
- **BeautifulSoup:** HTML/XML 파싱, `.find()`, `.select()`와 CSS 선택자로 필요한 노드 추출.
- `requests.get()`으로 응답을 받고 `status_code`와 인코딩을 검사한다.
- 스크래핑은 사이트 약관·robots 정책·요청 빈도를 확인해야 하고, JavaScript로 동적 로딩된 데이터는 일반 `requests`만으로 충분하지 않을 수 있다.

### ③ 자연어 처리(NLP)
- **토큰화:** 문장을 처리 단위(단어·형태소 등)로 분리한다.
- 한국어 형태소 분석기 `Okt`로 명사 등을 추출하고 `Counter`/`value_counts()`로 빈도 집계한다.
- 빈도 시각화는 워드클라우드나 막대그래프에 적용할 수 있으며, 불용어와 띄어쓰기·표기 변형이 결과를 크게 바꾼다.

## 4. 실제 코드와 개념 연결

| 파일 | 핵심 내용 |
|---|---|
| `numpy1.py` ~ `numpy3.py` | ndarray 생성·연산·차원·인덱싱 |
| `numpy4log.py` | 로그 변환과 값의 규모 조정 |
| `pandas1.py` ~ `pandas4.py` | Series/DataFrame, 결측치, 재구조화, 범주화 |
| `pandas5.py`, `pandas6.py` | CSV 및 외부 자료 처리, Titanic 데이터 분석 |
| `pandas7.py` | XML 구조 및 웹 데이터 읽기 |
| `pandas8bs4.py` ~ `pandas11.py` | BeautifulSoup를 이용한 HTML/XML 파싱 |
| `pandas12.py` | JSON 인코딩·디코딩과 도서관 정보 처리 |
| `pandas13.py` ~ `pandas14.py` | SQLite/MariaDB와 DataFrame 연동 |
| `pandas15.py` | 웹에서 주식 데이터 수집 실습 |
| `pandas16.py` | 날짜·제품별 판매량 피벗테이블 |
| `pandas17.py` | 직원·부서·고객 DB JOIN 결과를 집계·출력 |
| `mplot1.py` ~ `mplot4.py` | Matplotlib/Seaborn, Iris·Titanic 시각화 |
| `mplot5.py` | 자전거 공유 수요 데이터 탐색·시각화 |
| `nip_morph.py` ~ `nip_morph3.py` | 영어·한국어 토큰화/형태소·단어 빈도 분석 |
| `prac1.py` | NumPy·Pandas 연산과 데이터 분석 연습 |

## 5. 실행 환경

```bash
cd projects/pro10anal1
python numpy1.py
python pandas16.py
```

실습에 따라 설치해야 할 주요 패키지: `numpy`, `pandas`, `matplotlib`, `seaborn`, `requests`, `beautifulsoup4`, `lxml`, `pymysql`, `sqlalchemy`, `nltk`, `konlpy`, `koreanize-matplotlib`. 모든 파일에 전부 필요한 것은 아니다.

- 일부 파일은 CSV/XML/JSON 또는 MariaDB 데이터가 필요하고, 웹 예제는 인터넷 연결·사이트 구조에 의존한다.
- `pandas16.py`는 같은 작업 위치에 `sales_data.csv`가 있어야 한다.
- `nip_morph3.py`는 `pytagcloud`·`pygame` 등 설치가 까다로울 수 있다.
- DB 접속정보를 포함한 파일이 있으므로 **공개 저장소 업로드 전 민감정보를 제거**해야 한다.

## 6. 실무 연결 포인트

품질·공정 데이터에서도 `groupby()`와 `pivot_table()`은 공정별 평균/불량률 집계에, 산점도·박스플롯은 변수 관계와 분포 확인에 활용할 수 있다. 시각적인 차이를 발견한 뒤에는 `pro11anal2`의 통계 검정으로 **우연에 의한 차이인지** 추가 평가할 수 있다.

[⬅ 프로젝트 목록으로](../README.md)
