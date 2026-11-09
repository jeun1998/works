# Python · Web · Data Analysis 학습 기록 (pro1–pro11)

Python 기초 문법부터 데이터베이스, 웹 프런트엔드, Flask 백엔드, 데이터 분석 및 통계적 가설검정까지 진행한 **학습·실습 코드 모음**입니다.

> 이 저장소의 코드는 교육용 예제와 과제 풀이를 포함합니다. 서로 독립적으로 실행되는 파일이 많으며, 모든 파일을 하나의 애플리케이션으로 실행하는 구조는 아닙니다. 일부 예제는 실습 당시의 데이터베이스·외부 서비스·패키지 환경을 필요로 합니다.

## 📂 폴더별 학습 내용

| 디렉터리 | 주제 | 주요 실습 |
|---|---|---|
| [`pro1/`](pro1/) | Python 기본 문법과 OOP | 자료형, 반복문, 함수, 클로저, 데코레이터, 모듈, 클래스, 상속·다형성·추상 클래스 |
| [`pro2/`](pro2/) | 예외처리와 파일 처리 | `try/except`, 텍스트 입출력, `with`, 우편번호 검색, 판매기록 집계 |
| [`pro3db/`](pro3db/) | 데이터베이스 및 소켓 | SQLite, MariaDB CRUD/JOIN, DB 접속, 직원 조회, TCP 클라이언트·서버 |
| [`pro4web/`](pro4web/) | Python HTTP 서버 | HTTPServer를 사용한 간단한 HTML 파일 제공 |
| [`pro5web2/`](pro5web2/) | CGI 웹 프로그래밍 | CGI 요청 파라미터 처리, GET/POST, MariaDB 상품 출력 |
| [`pro6web3basic/`](pro6web3basic/) | HTML/CSS 기초 | HTML 태그, 링크·이미지·표·폼, CSS 선택자 |
| [`pro7quiz/`](pro7quiz/) | 웹 페이지 제작 연습 | 메뉴/본문 구성, iframe, 이미지, CSS 레이아웃 |
| [`pro8js/`](pro8js/) | JavaScript/AJAX | JS 문법, DOM, 이벤트, 데이터 검증, JSON/CSV, XMLHttpRequest·fetch·Axios |
| [`pro9flask/`](pro9flask/) | Flask 백엔드 | 라우팅, 템플릿, 폼, 쿠키·세션, 상품 CRUD, REST API, MariaDB·Pandas 연계 |
| [`pro10anal1/`](pro10anal1/) | 수치·데이터 분석 | NumPy, Pandas, Matplotlib, Seaborn, 크롤링, JSON/XML, 형태소 분석 |
| [`pro11anal2/`](pro11anal2/) | 통계·가설검정 | 기술통계, 카이제곱, t-검정, ANOVA, 사후검정, Flask 기반 커피 설문 분석 |

**세부 코드 설명:** [`CODE_SUMMARY.md`](CODE_SUMMARY.md)에서 파일별 역할과 실습 내용을 확인할 수 있습니다.

## 🛠 기술 스택

- **언어:** Python, SQL, HTML, CSS, JavaScript
- **백엔드/통신:** Flask, Jinja2, Python HTTPServer/CGI, REST API, AJAX, socket
- **DB:** SQLite, MariaDB/MySQL, PyMySQL, mysqlclient, SQLAlchemy(일부 예제)
- **분석/시각화:** NumPy, Pandas, SciPy, statsmodels, Matplotlib, Seaborn
- **웹 데이터 처리:** Requests, BeautifulSoup, JSON, XML, Playwright(일부 예제)
- **기타:** NLTK, KoNLPy, Chart.js, Axios 등(파일별 선택 사용)

## 🔍 대표 실습

### 1. Flask + MariaDB 상품 관리 (`pro9flask`)
- `fpro10db.../fpro10db/`: Jinja2 폼을 이용한 상품 목록·등록·수정·삭제
- `fpro15rest_crud/`: GET·POST·PUT·DELETE 엔드포인트로 상품 CRUD 구현, 프런트엔드에서 비동기 요청
- `fpro16rest_select/`: 직원 및 부서 정보 조회 REST API

### 2. 직원 데이터 분석 대시보드 예제 (`pro9flask/fpro17`)
- MariaDB `jikwon`, `buser` JOIN으로 직원 데이터를 불러와 Pandas DataFrame으로 변환
- 부서·직급별 연봉 집계, 성별·직급 빈도표, 부서별 최고 연봉자와 구성 비율 분석
- Matplotlib 차트를 브라우저에 표시하는 Flask 실습

### 3. 데이터 분석 (`pro10anal1`)
- 배열 연산·결측치·그룹 집계·피벗·교차표 등 NumPy/Pandas 사용
- 타이타닉·자전거 공유 데이터 등의 탐색 및 시각화 실습
- 웹 문서 크롤링, XML/JSON 파싱, 한국어 형태소 분석·워드클라우드 실습

### 4. 가설검정·커피 설문 (`pro11anal2`)
- 카이제곱 검정, 독립·대응표본 t-검정, 일원·이원 ANOVA
- `fpro_coffee/`: 설문 응답을 MariaDB에 저장하고 통계 분석 및 막대그래프 결과 페이지 제공

## ▶️ 실행 방법(예시)

**1.** Python 3 환경을 만들고 필요한 라이브러리를 설치합니다. 아래는 주요 패키지 예시이며, *모든 예제에 공통 적용되는 검증된 requirements 파일은 아닙니다.*

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install flask pymysql mysqlclient python-dotenv numpy pandas matplotlib seaborn scipy statsmodels requests beautifulsoup4 lxml sqlalchemy koreanize-matplotlib
```

**2.** 독립 실행형 `.py` 예제는 해당 폴더에서 실행합니다.

```bash
cd pro1
python test1.py
```

**3.** Flask 예제는 해당 앱 폴더에서 `app.py`를 실행합니다. DB 연동 예제는 사전에 MariaDB와 실습 테이블을 준비해야 합니다.

```bash
cd pro9flask/fpro15rest_crud
python app.py
```

**4.** `pro8js`의 AJAX 예제는 파일을 직접 더블클릭하는 대신 로컬 웹 서버 또는 VS Code Live Server 등에서 확인하는 것이 적절합니다. 일부 파일은 특정 백엔드가 있어야 동작합니다.

> 실행 전 각 코드에서 사용하는 파일 경로, DB 테이블, 패키지, 서버 포트를 확인하세요. 일부 실습용 코드는 경로·환경이 고정되어 있거나 수정 중인 상태일 수 있습니다.

## 🔐 공개 저장소 업로드 전 확인

- `.env`, DB 비밀번호가 포함된 `dbconnect.json`, 로컬 DB 파일, `__pycache__`, `.pyc`, `.git` 내부 파일은 업로드하지 않습니다.
- **`.gitignore`는 코드 안에 직접 작성된 접속 비밀번호를 숨기지 못합니다.** `pro3db`, `pro9flask`, `pro10anal1`, `pro11anal2` 일부 소스의 DB 설정값을 확인하고, 필요한 경우 환경변수로 바꾸세요.
- 실습 당시의 하드코딩된 Flask secret key와 `debug=True` 설정은 배포용으로 사용하면 안 됩니다.
- 업로드용 파일 정리는 [`GITHUB_UPLOAD_GUIDE.md`](GITHUB_UPLOAD_GUIDE.md)를 참고하세요.

## 📌 학습 포인트

기본 문법과 객체지향 설계, SQL 데이터 처리, 웹 요청·응답 구조, REST API, 데이터 전처리·시각화, 통계적 검정을 **직접 코드로 연습**한 과정입니다. 향후 백엔드 개발·데이터 분석 프로젝트의 기초 학습 기록으로 활용합니다.
