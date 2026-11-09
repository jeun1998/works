# pro9flask — Flask 웹 백엔드·REST API·데이터 분석

> **학습 목표:** Python Flask로 요청을 처리하고, MariaDB CRUD·세션·AJAX·Pandas 분석 화면을 구현한다.

## 1. Flask 핵심 이론

### ① 라우팅과 요청/응답
- `Flask(__name__)`으로 앱 객체를 만들고 `@app.get()` / `@app.post()` 등으로 URL을 함수에 연결한다.
- `request.args`: URL 쿼리 문자열, `request.form`: HTML 폼 값, `request.get_json()`: JSON 요청 본문.
- `render_template()`은 Jinja2 템플릿을 HTML로 렌더링한다. `redirect(url_for(...))`는 다른 경로로 이동시킨다.
- `jsonify()`는 JSON 응답을 반환한다.

```python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.get('/api/ping')
def ping():
    return jsonify({'ok': True, 'message': 'pong'})
```

### ② Jinja2 템플릿
- `{{ value }}`는 변수 출력, `{% if %}`, `{% for %}`는 분기·반복이다.
- `{% extends 'base.html' %}`와 `{% block content %}`는 공통 레이아웃 재사용에 사용한다.
- Jinja2의 자동 이스케이프를 유지하고, 신뢰할 수 없는 데이터를 무분별하게 `|safe`로 출력하지 않는다.

### ③ 쿠키·세션과 상태 유지
- HTTP 자체는 무상태(stateless) 프로토콜이다.
- **쿠키:** 브라우저에 저장되는 작은 데이터. `HttpOnly`, `Secure`, `SameSite` 속성 이해가 중요하다.
- **Flask 세션:** 기본 구현에서 서명된 쿠키를 사용한다. **서명은 암호화가 아니므로** 비밀번호 같은 비밀 데이터를 세션에 넣지 않는다.
- 로그인·장바구니처럼 사용자별 상태를 유지하는 예제를 통해 개념을 학습한다.

### ④ 데이터베이스 CRUD와 트랜잭션
- CRUD = Create(등록) / Read(조회) / Update(수정) / Delete(삭제).
- MariaDB 접근은 `pymysql` 연결, 커서, SQL, 트랜잭션으로 이루어진다.
- SQL에는 매개변수 바인딩을 사용하고 DB 변경 후 적절히 `commit()`해야 한다.
- DB 비밀번호는 `.env`나 환경변수로 관리하고, 저장소 코드에 하드코딩하지 않는다.

### ⑤ REST API와 AJAX

| HTTP 메소드 | 의도 | 학습 코드 예시 |
|---|---|---|
| `GET` | 자원 조회 | `GET /api/sangdata` |
| `POST` | 신규 생성 | `POST /api/sangdata` |
| `PUT` | 자원 수정 | `PUT /api/sangdata/<code>` |
| `DELETE` | 자원 삭제 | `DELETE /api/sangdata/<code>` |

- API는 상태코드, 일관된 응답 구조, 입력 검증을 통해 예측 가능한 동작을 제공한다.
- 클라이언트는 JavaScript `fetch()`로 JSON을 받아 표를 새로 그릴 수 있다.
- API URL의 `<code>`는 경로 변수 개념이며 실제 Flask 코드에서는 `<int:code>`로 선언한다.

### ⑥ 분석 결과를 웹에 표시하기
- SQL JOIN 결과를 `pd.DataFrame()`으로 구성한다.
- `groupby(...).agg(...)`, `crosstab()`, 정렬·비율 계산으로 집계한다.
- Matplotlib 그래프를 이미지로 만들어 HTML에 전달하거나 Chart.js 등에 데이터로 전달할 수 있다.

## 2. 실제 실습 코드 안내

| 하위 프로젝트 | 학습·구현 내용 |
|---|---|
| `fpro1/` ~ `fpro3/` | 라우팅, 요청/응답, 템플릿 기초 |
| `fpro4/` | Jinja2의 상속·반복·조건·필터 |
| `fpro5getpost/` | GET/POST 요청과 폼 처리 |
| `fpro6cookie/`, `fpro7cookie/` | 쿠키 관리·쿠키 기반 방문/로그인 실습 |
| `fpro8session/` | 세션 값 저장·조회 |
| `fpro9cart/` | 세션 기반 장바구니 추가·삭제·초기화 |
| `fpro10db-20261006T002350Z-1-001/fpro10db/` | MariaDB 상품 등록·조회·수정·삭제 |
| `fpro11guestbook-20261006T002800Z-1-001/fpro11guestbook/` | 방명록 CRUD·검색·flash 메시지 |
| `fpro12login-20261006T002814Z-1-001/fpro12login/` | 직원 로그인, 세션, 고객·직원 목록 |
| `fpro13rest/`, `fpro14rest_ajax/` | JSON API와 AJAX 방식 |
| `fpro15rest_crud/` | 상품 REST CRUD API, JavaScript 비동기 UI |
| `fpro16rest_select/` | 직원/부서 전체·단건·조건별 조회 API |
| `fpro17/` | 직원·부서 JOIN, 연봉 합/평균, 교차표·비율·그래프 |
| `fprodb/` | DB 조회 데이터를 Pandas 표로 렌더링 |
| `fpro_pandas_iris/` | Iris 자료 Pandas·시각화 결과를 Flask에서 표시 |
| `test/` | 추가적인 Flask 요청 처리 실습 |

## 3. 대표 코드: `fpro17`의 분석 흐름

```text
브라우저에서 /db 요청
  → MariaDB(jikwon JOIN buser) 조회
  → Pandas DataFrame 생성
  → groupby/agg, crosstab, 비율/최고연봉 계산
  → Matplotlib 그래프를 base64로 변환
  → Jinja2 템플릿에 표와 그래프 전달
```

공정·품질·생산 데이터의 집계 대시보드에도 확장 가능한 패턴이다.

## 4. 실행 방법

각 하위 디렉터리는 **별개의 Flask 앱**이다. 실행할 디렉터리로 이동한 뒤 해당 `app.py`를 실행한다.

```bash
cd projects/pro9flask/fpro13rest
python app.py
```

대부분 Flask가 필요하며, 예제에 따라 `pymysql`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `koreanize-matplotlib`, `waitress` 등이 추가로 필요하다. DB 예제는 원본 MariaDB 테이블이 준비되어야 한다. 서버 시작 주소/포트는 각 `app.py`의 실행 설정을 확인한다.

## 5. 개선·보안 체크리스트

- DB 비밀번호와 Flask `SECRET_KEY`를 소스 코드가 아닌 환경변수에서 읽도록 개선.
- 디버그 모드(`debug=True`)는 로컬 학습에만 사용.
- 폼/JSON 값의 타입·누락 여부를 검증하고 DB 작업의 성공/실패를 구별.
- UPDATE 실행 후 커밋 여부를 확인하고, 적절한 상태코드(예: 201, 404)를 응답.
- `DataFrame.to_html()`의 결과를 템플릿에서 표시할 때 HTML 안전성을 점검.
- 다양한 하위 앱이 `app.py`라는 같은 이름을 사용하므로 **실행 폴더**를 혼동하지 않기.

[⬅ 프로젝트 목록으로](../README.md)
