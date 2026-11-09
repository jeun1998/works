# pro5web2 — CGI 기반 동적 웹 프로그래밍

> **학습 목표:** HTTP 요청에서 입력값을 추출하고, Python 코드로 동적 HTML 응답을 생성한다.

## 1. 핵심 이론

### ① 정적 웹과 동적 웹
- 정적 웹은 저장된 HTML 문서를 전달한다.
- **CGI(Common Gateway Interface)**는 웹 서버가 별도 프로그램을 실행해 요청마다 동적인 결과를 생성하는 방식이다.
- 기본 구조: `브라우저의 요청 → CGIHTTPRequestHandler → cgi-bin의 Python 코드 → HTML 응답`.

### ② GET·POST와 폼
- **GET:** 주로 조회에 사용한다. 입력값이 URL의 쿼리 스트링(`?name=Kim`)에 표현될 수 있다.
- **POST:** 주로 데이터를 제출한다. 양식 값이 요청 본문에 담긴다. POST라고 해서 자동으로 암호화되지는 않으므로 HTTPS가 필요하다.
- HTML의 `<form method="GET|POST" action="...">`을 통해 서버에 데이터를 제출한다.
- `urllib.parse.parse_qs()`는 쿼리 문자열을 딕셔너리 형태로 파싱할 수 있다.

```python
from urllib.parse import parse_qs
params = parse_qs('name=Kim&age=20')
print(params['name'][0])  # Kim
```

### ③ HTTP 응답 헤더
- CGI 프로그램은 본문 출력에 앞서 콘텐츠 타입 같은 헤더와 빈 줄을 출력해야 한다.
- HTML의 한글을 안전하게 출력하려면 `Content-Type: text/html; charset=utf-8` 표기를 정확히 사용한다.
- 웹에 출력하는 사용자 입력은 HTML 이스케이프가 필요하며, DB 질의에는 SQL 바인딩 변수를 사용한다.

### ④ 현재 기술 환경 주의
- 이 폴더는 **역사적 CGI 방식의 학습용 코드**다. Python 표준 라이브러리의 `cgi` 모듈은 Python 3.13에서 제거되었고, `CGIHTTPRequestHandler` 기반 접근도 최신 Python 환경에서 그대로 실행되지 않을 수 있다.
- 현대적인 신규 웹 서버 개발은 `pro9flask`의 Flask와 같은 WSGI/ASGI 프레임워크를 추천한다.
- 참고: [Python cgi 모듈 변경 안내](https://docs.python.org/3.13/library/cgi.html)

## 2. 실제 코드와 개념 연결

| 파일 | 내용 |
|---|---|
| `httpserver2.py` | `/cgi-bin`을 실행 대상으로 하는 CGI 기반 HTTP 서버 |
| `index.html`, `friend.html` | 링크 및 폼으로 CGI 프로그램 호출 |
| `cgi-bin/hello.py`, `cgi-bin/world.py` | 동적 HTML 출력 |
| `cgi-bin/my.py` | GET 쿼리 문자열 파싱 |
| `cgi-bin/friend.py` | GET/POST 입력값 처리 |
| `cgi-bin/sangpum.py` | DB에서 상품 데이터를 조회해 웹으로 출력 |

## 3. 실행 전 준비

1. 소스의 Python 버전·CGI 지원 여부를 확인한다(구형 예제용 호환 환경 필요).
2. `httpserver2.py`를 실행하고 `http://127.0.0.1:7777/`로 접속한다(원본 설정 기준).
3. DB 기반 예제는 MariaDB, 연결 환경변수, 상품 테이블을 별도로 준비한다.
4. `cgi-bin/.env` 등 비밀 설정 파일을 GitHub에 업로드하지 않는다.

## 4. 스스로 점검하기

- `GET`과 `POST`의 차이를 설명할 수 있는가?
- CGI 스크립트가 HTML을 생성한다는 의미는 무엇인가?
- 사용자 입력을 그대로 HTML에 넣거나 SQL 문자열에 연결할 때 어떤 문제가 생기는가?
- CGI 예제를 Flask 라우트로 바꾸려면 어떤 코드가 필요한가?

[⬅ 프로젝트 목록으로](../README.md)
