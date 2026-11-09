# pro8js — JavaScript·DOM·이벤트·비동기 통신

> **학습 목표:** 브라우저에서 동작하는 프로그램을 작성하고 서버/파일의 데이터를 비동기로 불러와 화면에 표시한다.

## 1. 핵심 이론

### ① JavaScript 기본 문법
- `let`: 재할당 가능한 블록 스코프 변수. `const`: 재할당할 수 없는 바인딩(객체 내부 수정은 가능).
- `===`는 타입까지 비교하는 엄격한 동등 연산자다.
- 배열은 `map`, `filter`, `find`, `reduce`, `forEach` 등으로 가공할 수 있다.
- 함수 선언식·표현식·화살표 함수의 호출과 `this` 동작 차이를 이해한다.
- 객체는 속성과 메소드를 가지며 `class`는 객체 생성 패턴을 정의한다.

### ② DOM(Document Object Model)
- HTML은 브라우저에서 트리 형태의 DOM 객체로 표현된다.
- `document.querySelector()`로 요소를 찾고 `textContent`, `value`, `classList` 등으로 갱신한다.
- `innerHTML`은 HTML 문자열을 해석하므로 **검증되지 않은 사용자 입력을 직접 대입하면 XSS 위험**이 있다.

```javascript
const result = document.querySelector('#result');
result.textContent = '조회 완료';
```

### ③ 이벤트 처리와 입력 검증
- `addEventListener('click', callback)`으로 사용자 동작을 처리한다.
- 폼의 `submit` 이벤트에서 `event.preventDefault()`로 기본 제출을 막을 수 있다.
- `trim()`, 숫자 형식, 필수값 체크는 브라우저 사용자 경험을 개선하지만 서버에서도 반드시 재검증해야 한다.

### ④ AJAX·JSON·비동기
- **AJAX:** 페이지 전체를 새로고침하지 않고 HTTP 요청으로 데이터를 받아 일부 화면을 갱신하는 방식.
- `XMLHttpRequest`: 전통적인 비동기 HTTP 인터페이스.
- `fetch()`: Promise 기반 웹 API. `async/await`로 순차적인 형태로 작성할 수 있다.
- `Axios`: 요청·응답 처리에 편의 기능을 제공하는 HTTP 라이브러리.
- **JSON:** 서버와 클라이언트 간 데이터 교환에 자주 사용하는 텍스트 포맷. `JSON.parse()`와 `JSON.stringify()`를 구분한다.

```javascript
async function loadData() {
  const response = await fetch('/api/items');
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const data = await response.json();
  return data;
}
```

위의 `/api/items`는 개념 설명용 예시 URL이며, 실제 실습 파일의 요청 URL은 해당 코드에서 확인한다.

## 2. 실제 코드와 개념 연결

| 파일 | 핵심 내용 |
|---|---|
| `js1.html` ~ `js3.html` | 스크립트 작성, 변수, 자료형, 형 변환, 조건 처리 |
| `js4for.html` ~ `js6array.html` | 반복문과 배열 가공 |
| `js7func.html` ~ `js9func.html` | 함수, 매개변수, 반환값, 스코프 |
| `js10event.html` ~ `js14event.html` | DOM 조작, 이벤트 등록·처리 |
| `js15errorchk.html` | 폼 입력값 검증과 오류 표시 |
| `js16.html`, `js17object.html` | 객체·클래스와 주문 객체 처리 |
| `js18ajax.html`, `js19ajax.html` | XHR 요청과 다양한 데이터 형식 처리 |
| `js20ajax_real.html` | `fetch`, `async/await`, Axios 방식 비교 |
| `js21ajax.html` | 상품 정보 조회와 재고 필터링 |
| `prac1.html` | 로그인 조건 검사 후 JSON 데이터로 테이블 구성 |
| `js18.py`, `sangpum.py` | 확장자는 `.py`지만 JSON 응답 예시 자료로 활용되는 파일. 확장자·콘텐츠 타입 주의 |

## 3. 실행 방법과 주의

정적 예제는 HTML을 브라우저에서 열 수 있지만, `fetch`/XHR가 파일을 가져오는 예제는 브라우저의 `file://` 보안 정책 때문에 실패할 수 있다. HTTP 서버로 실행하는 것이 안정적이다.

```bash
cd projects/pro8js
python -m http.server 8000
# 브라우저: http://localhost:8000/js20ajax_real.html
```

서버 API를 호출하는 예제는 별도의 API/백엔드가 필요할 수 있다. 개발자 도구의 **Console/Network**에서 HTTP 상태·응답·CORS 오류를 확인한다.

## 4. 필수 점검

- `DOMContentLoaded`와 스크립트 실행 시점이 DOM 조회에 미치는 영향은?
- `fetch()`는 HTTP 404/500에 대해 기본적으로 Promise를 거부하지 않는다는 점을 알고 `response.ok`를 확인하는가?
- `innerHTML` 대신 `textContent`를 선택해야 하는 상황은?
- 동기·비동기 실행 흐름과 `await`의 의미를 설명할 수 있는가?

[⬅ 프로젝트 목록으로](../README.md)
