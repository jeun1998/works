# pro4web — HTTP와 Python 정적 웹 서버

> **학습 목표:** 브라우저가 서버에 HTTP 요청을 보내고 HTML 응답을 받는 과정을 이해한다.

## 1. 핵심 이론

### ① 웹의 기본 흐름

```text
브라우저 (클라이언트)
  └─ HTTP 요청: GET /abc.html
        ↓
     웹 서버
        ↓
  └─ HTTP 응답: 상태코드 + 헤더 + HTML 본문
```

- **URL:** 프로토콜(scheme), 호스트, 포트, 경로, 쿼리 문자열 등으로 구성된다.
- **HTTP 요청:** `GET`, `POST`, `PUT`, `DELETE` 등의 메소드와 헤더·본문을 담는다.
- **HTTP 응답:** 상태코드(`200`, `404`, `500` 등), 헤더, 본문을 담는다.
- **정적 파일 서비스:** 파일 내용을 그대로 반환한다. 서버 측 계산 결과를 만드는 동적 애플리케이션과 구별한다.
- `localhost` / `127.0.0.1`은 자기 컴퓨터를 의미하고, `0.0.0.0`은 서버 바인딩용 전체 인터페이스 주소이다.

### ② HTTPServer와 핸들러
- Python 표준 라이브러리의 `HTTPServer`는 요청을 수신한다.
- `SimpleHTTPRequestHandler`는 요청 경로에 대응하는 정적 파일을 제공한다.
- `serve_forever()`는 서버가 지속적으로 요청을 처리하도록 한다.

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(('127.0.0.1', 7777), SimpleHTTPRequestHandler)
server.serve_forever()
```

위 코드는 핵심 원리를 설명하는 예시다. 원본 `httpserver1.py`는 별도의 실습용 LAN IP를 사용하므로 다른 PC에서 실행할 때 바인딩 주소를 확인해야 한다.

## 2. 실제 코드와 개념 연결

| 파일 | 설명 |
|---|---|
| `httpserver1.py` | `HTTPServer`, `SimpleHTTPRequestHandler`를 이용한 서버 시작 |
| `abc.html` | 서버를 통해 표시하는 HTML 문서 |
| `def.html` | 정적 파일 경로에 따라 다른 응답 확인 |

## 3. 실행 방법

```bash
cd projects/pro4web
python httpserver1.py
```

원본의 서버 IP를 실행 PC에 맞게 조정한다. 원본 포트는 `7777`이므로 브라우저에서 `http://127.0.0.1:7777/abc.html` 등을 요청해 본다(로컬로 바인딩한 경우).

## 4. 확인할 개념

- 주소창에 파일 경로를 입력했을 때 서버가 어떤 순서로 응답하는가?
- 파일을 지우면 왜 `404 Not Found`가 발생하는가?
- 왜 `http.server`는 개발·학습용이고 운영 환경의 보안이 강화된 웹 서버를 대체하지 못하는가?
- 정적 파일 제공과 다음 단계의 CGI/Flask에서 동적 처리는 무엇이 다른가?

[⬅ 프로젝트 목록으로](../README.md)
