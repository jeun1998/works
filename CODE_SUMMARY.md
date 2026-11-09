# pro1–pro11 코드별 설명

업로드한 `projects.zip`의 파일을 직접 확인해 작성한 요약입니다. 각 파일의 **학습 의도와 구현 중심 기능**을 설명하며, 정상 실행을 보증하거나 모든 입력·출력 케이스를 테스트한 문서는 아닙니다.

주요 데이터·이미지 파일은 코드 실행을 위한 보조 리소스이므로 아래 표에서는 실행/표시용 코드(`.py`, `.html`, `.css`, `.js`)를 중심으로 정리했습니다. 일부 `.py` 파일은 실제로 JSON 예시 데이터로 쓰이고 있으니 비고를 확인하세요.

## pro1 — Python 문법·객체지향

| 파일 | 내용 |
|---|---|
| `pack1/__init__.py` | 파이썬 패키지 인식용 초기화 파일 |
| `pack1/mymod1.py` | 패키지 내부의 사용자 정의 함수 및 모듈 가져오기 예제 |
| `pack1/subpack/sbs.py` | 하위 패키지 함수 작성 |
| `pack1_other/mymod2.py` | 합·차 함수로 모듈 재사용 실습 |
| `pack1_other/mymod3.py` | 곱셈 함수로 Python import 경로 실습 |
| `practice1.py` | 정수 누적합·구구단·자리수 등 조건문/반복문 응용문제 |
| `practice2.py` | 직원 정보 입력, 급여·근속 처리 함수 문제 |
| `practice2a.py` | 직원 급여·수당·근속 관련 계산 과제의 확장 풀이 |
| `practice3.py` | 자판기와 동전 투입을 클래스로 모델링 |
| `practice3a.py` | 커피 자판기 예제: 동전과 컵 수량, 거스름돈 연산 |
| `practice4.py` | 전자제품/TV/라디오의 클래스 상속과 메소드 재정의 |
| `practice5.py` | 동물 클래스로 다중 상속과 동작 재정의 연습 |
| `practice6.py` | 정규직·임시직 급여 계산을 추상클래스와 다형성으로 구현 |
| `test1.py` | 출력, 변수, 자료형, 기본 파이썬 실행 규칙 |
| `test2.py` | 산술·할당·비교 연산자와 연산자 우선순위 |
| `test3.py` | 문자열·리스트·튜플·집합·딕셔너리 자료구조 |
| `test4.py` | 정규표현식 패턴 매칭 기초 |
| `test5if.py` | if/elif/else 조건문과 분기 처리 |
| `test6while.py` | while 반복·break·continue·반복 종료 동작 |
| `test7for.py` | for 반복, 중첩 반복, 수치 합계·빈도 계산 |
| `test8f1.py` | 함수의 개념과 내장 함수 실습 |
| `test9f2.py` | 사용자 정의 함수, 인수·반환값·스코프 |
| `test10f3.py` | 위치·기본값·키워드·가변 매개변수 |
| `test11closure.py` | 지역·전역·nonlocal 변수, 중첩 함수와 클로저 |
| `test12deco.py` | @데코레이터로 함수 동작 감싸기 |
| `test13recursive.py` | 재귀 호출, 누적합, 팩토리얼 |
| `test14module.py` | 표준 모듈(math/random 등)과 모듈 사용 |
| `test15module.py` | 사용자 정의 모듈·패키지 import |
| `test16graphic.py` | Python 그래픽 모듈 사용 |
| `test17pygame.py` | Pygame 라이브러리 호출 실습 |
| `test18opencv.py` | OpenCV로 이미지 읽기·표시 기초 |
| `test19class.py` | 클래스/인스턴스, 생성자·소멸자, 멤버 메소드 |
| `test20class.py` | Car 예제로 객체 상태·멤버 변수/메소드 |
| `test21class.py` | 클래스 메소드와 변수의 범위 이해 |
| `test22class.py` | Singer 객체 생성과 클래스 자원 공유 |
| `test22singer.py` | 다른 파일에서 import할 Singer·Etc 클래스 |
| `test23class.py` | 점 좌표·거리·기울기 등 클래스 기반 수치 처리 |
| `test24pc.py` | 자동차와 핸들 객체의 포함(composition) 관계 |
| `test24ph.py` | 자동차 핸들 객체의 좌·우회전 메소드 |
| `test25fridge.py` | 냉장고에 음식 객체를 저장·조회하는 포함 관계 |
| `test26Lotto.py` | 공(ball) 객체와 LottoMachine으로 로또 번호 추출 |
| `test27inherit.py` | Animal/Dog로 기본 상속 이해 |
| `test28person.py` | Person/Employee 상속과 super 활용 |
| `test29over.py` | 부모·자식 메소드 오버라이딩 |
| `test30poly.py` | 카드·현금·포인트 결제 예제로 다형성 |
| `test31multi.py` | Tiger/Lion/Liger로 다중 상속·메소드 탐색 순서 |
| `test32abstract.py` | ABC 및 @abstractmethod를 이용한 추상클래스 |
| `test33abstract.py` | 정규직·임시직 유형의 추상 급여 인터페이스 |
| `test34abstract_poly.py` | 일반·퀵배송·픽업 방식별 배송비 계산 다형성 |

**확인된 코드 파일 수:** 49개

---

## pro2 — 예외처리·파일 입출력

| 파일 | 내용 |
|---|---|
| `ex1try.py` | 예외 처리 try/except/else/finally 및 예외 상황 |
| `ex2file.py` | 텍스트 파일 열기/읽기/쓰기 기초 |
| `ex3file.py` | with open 문과 파일 자동 닫기·파일 저장 |
| `ex4zipcode.py` | zipcode.txt에서 지역명 검색 후 주소 정보 출력 |
| `exam1.py` | Bicycle 클래스로 속성·출력 연습 |
| `practice7.py` | 판매 자료 집계, 중복 이름 합산 및 결과 파일 저장 |

**확인된 코드 파일 수:** 6개

---

## pro3db — SQLite·MariaDB·소켓 통신

| 파일 | 내용 |
|---|---|
| `db1.py` | SQLite 연결, 테이블 처리 및 cursor로 조회 |
| `db2maria.py` | MariaDB 연결 및 상품 테이블 조회·CRUD SQL 학습 |
| `db3maria.py` | 직원번호/이름을 받아 MariaDB에서 직원·부서 JOIN 로그인 조회 |
| `prac1.py` | 직원·부서·고객 JOIN, 성별 급여 집계와 로그인 등 DB 과제 |
| `socket1client.py` | TCP 서버에 연결해 메시지 전송하는 1회성 클라이언트 |
| `socket1server.py` | socket bind/listen/accept/recv 구현하는 1회용 서버 |
| `socket2client.py` | 지속형 서버와 통신하는 소켓 클라이언트 |
| `socket2server.py` | 반복 연결을 받아 응답하는 서버 |
| `socket_test.py` | IP/TCP 및 socket 주소·통신 메소드 연습 |
| `문제2_전재현_.py` | 직원 성별별 인원·평균급여 조회 SQL 과제 |

**확인된 코드 파일 수:** 10개

---

## pro4web — 기본 HTTP 서버

| 파일 | 내용 |
|---|---|
| `abc.html` | 서버에서 제공하는 기초 HTML 페이지 |
| `def.html` | 서버에서 제공하는 별도 HTML 페이지 |
| `httpserver1.py` | Python HTTPServer로 간단한 정적 HTML 페이지 서비스 |

**확인된 코드 파일 수:** 3개

---

## pro5web2 — CGI 기반 동적 웹

| 파일 | 내용 |
|---|---|
| `cgi-bin/friend.py` | GET/POST 친구 입력값 처리와 HTML 출력 |
| `cgi-bin/hello.py` | CGI로 응답 헤더와 동적 HTML 출력 |
| `cgi-bin/my.py` | 쿼리 스트링(GET) 데이터 파싱 |
| `cgi-bin/sangpum.py` | CGI에서 MariaDB 상품 테이블 조회 후 HTML 출력 |
| `cgi-bin/world.py` | CGI 동적 메인 페이지 출력 |
| `friend.html` | 친구정보 입력·전달을 위한 HTML 폼 |
| `httpserver2.py` | CGIHTTPRequestHandler로 정적/동적 요청을 서비스 |
| `index.html` | CGI 예제로 이동하는 시작 페이지 |

**확인된 코드 파일 수:** 8개

---

## pro6web3basic — HTML/CSS 기초

| 파일 | 내용 |
|---|---|
| `css/pro6.css` | 공통 CSS 선택자와 스타일 선언 |
| `kbs/sbs/aa.html` | 상대경로·하위 디렉터리 링크용 페이지 |
| `mbc/bb.html` | 폴더 이동·링크 실습용 HTML |
| `web1.html` | HTML 태그와 목록(ul/ol) 등 문서 구성 |
| `web2.html` | 링크·이미지·iframe 등 웹 문서 연결 |
| `web3.html` | 테이블과 입력 폼 요소 |
| `web4.html` | CSS 내부/외부 스타일 및 HTML 레이아웃 |

**확인된 코드 파일 수:** 7개

---

## pro7quiz — 다중 페이지 웹사이트 제작

| 파일 | 내용 |
|---|---|
| `home.html` | 초기 메인 화면과 이미지 출력 |
| `main.html` | 메뉴 영역과 본문 iframe을 구성한 홈페이지 |
| `menu1.html` | 첫 번째 메뉴의 콘텐츠(테이블 포함) |
| `menu2.html` | 두 번째 메뉴 콘텐츠 |
| `test.css` | 메뉴·본문·배경·여백·정렬 등 레이아웃 CSS |

**확인된 코드 파일 수:** 5개

---

## pro8js — JavaScript·DOM·AJAX

| 파일 | 내용 |
|---|---|
| `js1.html` | HTML 내 JavaScript 작성과 DOM 요소 접근 기초 |
| `js2.html` | 변수 let/const, 자료형, 참조형, 스코프 |
| `js3.html` | 문자열·숫자·형변환/입력과 조건 처리 |
| `js4for.html` | for 반복·중첩 반복 및 HTML 테이블 생성 |
| `js5while.html` | while 반복문 |
| `js6array.html` | 배열 생성·메소드·순회·가공 |
| `js7func.html` | 함수 선언/표현식과 지역·전역 변수 |
| `js8func.html` | 함수 호출 및 반환값 관련 연습 |
| `js9func.html` | 함수·스코프·엄격모드 등 응용 |
| `js10event.html` | HTML 이벤트 핸들러와 클릭 처리 |
| `js11event.html` | 폼·테이블 이벤트 및 화면 속성 변경 |
| `js12inner.html` | innerHTML/innerText 및 DOM 내용 업데이트 |
| `js13event.html` | 로드 이벤트와 addEventListener |
| `js14event.html` | DOM 이벤트·입력값 처리 |
| `js15errorchk.html` | 폼 검증과 오류 표시·Bootstrap 스타일 활용 |
| `js16.html` | JavaScript 객체 생성과 class 문법 |
| `js17object.html` | 주문 객체와 주문 금액 계산 |
| `js18.py` | 예제 JSON 응답 텍스트를 담은 파일 |
| `js18ajax.html` | XMLHttpRequest로 GET/POST 비동기 요청 |
| `js19ajax.html` | AJAX로 JSON·CSV 요청 후 출력 |
| `js20ajax_real.html` | fetch then, async/await, Axios 호출 방식 비교 |
| `js21ajax.html` | 상품 JSON fetch/Axios 조회·재고 필터링 |
| `prac1.html` | 입력 정보 검증 후 JSON 파일을 읽어 테이블 생성 |
| `sangpum.py` | 상품 JSON 샘플 파일(확장자와 내용 형식 확인 필요) |

**확인된 코드 파일 수:** 24개

---

## pro9flask — Flask·REST API·DB 연동

| 파일 | 내용 |
|---|---|
| `fpro1/app.py` | Flask 라우팅 및 URL 경로 변수·Waitress 실행 (서버 메인 진입점) |
| `fpro2/app.py` | Flask request/response 및 GET/POST 로그인 처리 (서버 메인 진입점) |
| `fpro3/app.py` | Flask render_template로 기본 HTML 렌더링 (서버 메인 진입점) |
| `fpro3/templates/hello.html` | Flask render_template로 기본 HTML 렌더링 (인사 템플릿) |
| `fpro3/templates/home.html` | Flask render_template로 기본 HTML 렌더링 (홈 템플릿) |
| `fpro3/templates/my.html` | Flask render_template로 기본 HTML 렌더링 (변수 출력 템플릿) |
| `fpro4/app.py` | Jinja2 템플릿 상속·반복·조건·필터 (서버 메인 진입점) |
| `fpro4/index.html` | Jinja2 템플릿 상속·반복·조건·필터 (메인 화면) |
| `fpro4/templates/base.html` | Jinja2 템플릿 상속·반복·조건·필터 (템플릿 공통 레이아웃) |
| `fpro4/templates/condition.html` | Jinja2 템플릿 상속·반복·조건·필터 (Jinja2 조건문) |
| `fpro4/templates/filter.html` | Jinja2 템플릿 상속·반복·조건·필터 (Jinja2 필터) |
| `fpro4/templates/index.html` | Jinja2 템플릿 상속·반복·조건·필터 (메인 화면) |
| `fpro4/templates/loop.html` | Jinja2 템플릿 상속·반복·조건·필터 (Jinja2 반복문) |
| `fpro5getpost/app.py` | GET/POST 폼 입력 처리 (서버 메인 진입점) |
| `fpro5getpost/templates/get_form.html` | GET/POST 폼 입력 처리 (GET 입력 폼) |
| `fpro5getpost/templates/get_result.html` | GET/POST 폼 입력 처리 (GET 결과 화면) |
| `fpro5getpost/templates/index.html` | GET/POST 폼 입력 처리 (메인 화면) |
| `fpro5getpost/templates/post_form.html` | GET/POST 폼 입력 처리 (POST 입력 폼) |
| `fpro5getpost/templates/post_result.html` | GET/POST 폼 입력 처리 (POST 결과 화면) |
| `fpro6cookie/app.py` | 쿠키 읽기·쓰기·삭제 (서버 메인 진입점) |
| `fpro7cookie/app.py` | 쿠키 기반 로그인·방문기록·로그아웃 (서버 메인 진입점) |
| `fpro7cookie/templates/index.html` | 쿠키 기반 로그인·방문기록·로그아웃 (메인 화면) |
| `fpro7cookie/templates/login.html` | 쿠키 기반 로그인·방문기록·로그아웃 (로그인 폼) |
| `fpro8session/app.py` | Flask 세션에 사용자 OS 선택값 저장·조회 (서버 메인 진입점) |
| `fpro8session/templates/main.html` | Flask 세션에 사용자 OS 선택값 저장·조회 (메인 화면) |
| `fpro8session/templates/setos.html` | Flask 세션에 사용자 OS 선택값 저장·조회 (setos 화면) |
| `fpro8session/templates/showos.html` | Flask 세션에 사용자 OS 선택값 저장·조회 (showos 화면) |
| `fpro9cart/app.py` | 세션을 활용한 장바구니 목록·추가·삭제·초기화 (서버 메인 진입점) |
| `fpro9cart/templates/base.html` | 세션을 활용한 장바구니 목록·추가·삭제·초기화 (템플릿 공통 레이아웃) |
| `fpro9cart/templates/cart.html` | 세션을 활용한 장바구니 목록·추가·삭제·초기화 (장바구니 목록) |
| `fpro9cart/templates/products.html` | 세션을 활용한 장바구니 목록·추가·삭제·초기화 (상품 목록) |
| `fpro10db-20261006T002350Z-1-001/fpro10db/app.py` | 상품 목록/추가/수정/삭제 Jinja2 + MariaDB CRUD (서버 메인 진입점) |
| `fpro10db-20261006T002350Z-1-001/fpro10db/static/validate_add.js` | 상품 목록/추가/수정/삭제 Jinja2 + MariaDB CRUD (브라우저 이벤트/AJAX 처리 JavaScript) |
| `fpro10db-20261006T002350Z-1-001/fpro10db/templates/form_add.html` | 상품 목록/추가/수정/삭제 Jinja2 + MariaDB CRUD (상품 등록 폼) |
| `fpro10db-20261006T002350Z-1-001/fpro10db/templates/form_edit.html` | 상품 목록/추가/수정/삭제 Jinja2 + MariaDB CRUD (상품 수정 폼) |
| `fpro10db-20261006T002350Z-1-001/fpro10db/templates/list.html` | 상품 목록/추가/수정/삭제 Jinja2 + MariaDB CRUD (목록 화면) |
| `fpro11guestbook-20261006T002800Z-1-001/fpro11guestbook/app.py` | MariaDB 방명록 CRUD·검색·플래시 메시지 (서버 메인 진입점) |
| `fpro11guestbook-20261006T002800Z-1-001/fpro11guestbook/templates/add.html` | MariaDB 방명록 CRUD·검색·플래시 메시지 (등록 폼) |
| `fpro11guestbook-20261006T002800Z-1-001/fpro11guestbook/templates/edit.html` | MariaDB 방명록 CRUD·검색·플래시 메시지 (수정 폼) |
| `fpro11guestbook-20261006T002800Z-1-001/fpro11guestbook/templates/main.html` | MariaDB 방명록 CRUD·검색·플래시 메시지 (메인 화면) |
| `fpro12login-20261006T002814Z-1-001/fpro12login/app.py` | 직원 로그인·세션·고객 목록 조회 (서버 메인 진입점) |
| `fpro12login-20261006T002814Z-1-001/fpro12login/templates/gogek_list.html` | 직원 로그인·세션·고객 목록 조회 (고객 목록 템플릿) |
| `fpro12login-20261006T002814Z-1-001/fpro12login/templates/jikwonlist.html` | 직원 로그인·세션·고객 목록 조회 (직원 목록 템플릿) |
| `fpro12login-20261006T002814Z-1-001/fpro12login/templates/login.html` | 직원 로그인·세션·고객 목록 조회 (로그인 폼) |
| `fpro13rest/app.py` | Flask REST GET API와 JavaScript fetch (서버 메인 진입점) |
| `fpro13rest/static/css/# style.css` | Flask REST GET API와 JavaScript fetch (스타일시트) |
| `fpro13rest/static/js/app.js` | Flask REST GET API와 JavaScript fetch (브라우저 이벤트/AJAX 처리 JavaScript) |
| `fpro13rest/templates/index.html` | Flask REST GET API와 JavaScript fetch (메인 화면) |
| `fpro14rest_ajax/app.py` | Ajax 방식 및 DB 상품 API (서버 메인 진입점) |
| `fpro14rest_ajax/templates/main.html` | Ajax 방식 및 DB 상품 API (메인 화면) |
| `fpro14rest_ajax/templates/show3.html` | Ajax 방식 및 DB 상품 API (AJAX 결과 템플릿) |
| `fpro14rest_ajax/templates/show4.html` | Ajax 방식 및 DB 상품 API (AJAX 결과 템플릿) |
| `fpro15rest_crud/app.py` | 상품 REST CRUD API와 프런트엔드 비동기 처리 (서버 메인 진입점) |
| `fpro15rest_crud/db.py` | 상품 REST CRUD API와 프런트엔드 비동기 처리 (DB 연결 모듈) |
| `fpro15rest_crud/static/js/myapp.js` | 상품 REST CRUD API와 프런트엔드 비동기 처리 (브라우저 이벤트/AJAX 처리 JavaScript) |
| `fpro15rest_crud/templates/index.html` | 상품 REST CRUD API와 프런트엔드 비동기 처리 (메인 화면) |
| `fpro16rest_select/app.py` | 직원·부서 조회 REST API (목록/상세/부서별) (서버 메인 진입점) |
| `fpro16rest_select/db.py` | 직원·부서 조회 REST API (목록/상세/부서별) (DB 연결 모듈) |
| `fpro16rest_select/static/js/app.js` | 직원·부서 조회 REST API (목록/상세/부서별) (브라우저 이벤트/AJAX 처리 JavaScript) |
| `fpro16rest_select/templates/index.html` | 직원·부서 조회 REST API (목록/상세/부서별) (메인 화면) |
| `fpro17/app.py` | 직원 데이터 JOIN·집계·그래프 Flask 분석 페이지 (서버 메인 진입점) |
| `fpro17/templates/db.html` | 직원 데이터 JOIN·집계·그래프 Flask 분석 페이지 (분석 결과 화면) |
| `fpro17/templates/index.html` | 직원 데이터 JOIN·집계·그래프 Flask 분석 페이지 (메인 화면) |
| `fpro_pandas_iris/app.py` | Iris 데이터 시각화 및 Chart.js 데이터 전달 (서버 메인 진입점) |
| `fpro_pandas_iris/templates/main.html` | Iris 데이터 시각화 및 Chart.js 데이터 전달 (메인 화면) |
| `fpro_pandas_iris/templates/show2.html` | Iris 데이터 시각화 및 Chart.js 데이터 전달 (추가 조회 결과 화면) |
| `fpro_pandas_iris/templates/show.html` | Iris 데이터 시각화 및 Chart.js 데이터 전달 (조회 결과 화면) |
| `fprodb/app.py` | 부서 검색과 DB 결과의 Pandas 표시 (서버 메인 진입점) |
| `fprodb/templates/dbshow.html` | 부서 검색과 DB 결과의 Pandas 표시 (DB 결과 화면) |
| `fprodb/templates/index.html` | 부서 검색과 DB 결과의 Pandas 표시 (메인 화면) |
| `test/app.py` | 간단한 GET 로그인 확인 페이지 (서버 메인 진입점) |
| `test/templates/aa.html` | 간단한 GET 로그인 확인 페이지 (로그인 예제 화면) |

**확인된 코드 파일 수:** 72개

---

## pro10anal1 — NumPy·Pandas·시각화·크롤링

| 파일 | 내용 |
|---|---|
| `abc.py` | 평균·분산·표준편차 등 기초 통계량 |
| `mplot1.py` | Matplotlib 기본 그래프 생성과 저장 |
| `mplot2.py` | Matplotlib 객체지향 인터페이스와 시각화 |
| `mplot3.py` | Seaborn으로 통계 데이터 시각화 |
| `mplot4.py` | Iris 데이터의 산점도·관계 시각화 |
| `mplot5.py` | Bike Sharing 데이터 탐색·그래프·상관 분석 |
| `nip_morph2.py` | 웹 문서 추출 후 명사 빈도를 DataFrame으로 분석 |
| `nip_morph3.py` | 뉴스 검색 결과의 명사 빈도·워드클라우드 시각화 |
| `nip_morph.py` | NLTK·KoNLPy 한국어/영어 형태소 처리 |
| `numpy1.py` | NumPy 배열 생성·자료형·차원·인덱싱 |
| `numpy2.py` | 배열 브로드캐스팅·산술/벡터 연산 |
| `numpy3.py` | 배열 조작과 무작위 수 활용 |
| `numpy4log.py` | 데이터 편차 축소를 위한 로그 변환 |
| `pandas1.py` | Series·DataFrame 기초와 생성 |
| `pandas2.py` | Series/DataFrame 인덱싱·재색인 |
| `pandas3.py` | 결측값·데이터 수정 및 처리 |
| `pandas4.py` | DataFrame 구조변환, stack/unstack 등 |
| `pandas5.py` | 파일 불러오기, CSV/DataFrame 조작·시각화 실습 |
| `pandas6.py` | 타이타닉 데이터 분석 과제 |
| `pandas7.py` | XML 파싱 및 외부 기상·웹 데이터 처리 |
| `pandas8bs4.py` | BeautifulSoup로 HTML 구조 파싱 |
| `pandas9.py` | BeautifulSoup find/find_all, 정규식과 웹페이지 파싱 |
| `pandas10.py` | CSS 선택자 select/select_one을 이용한 데이터 추출 |
| `pandas11.py` | BeautifulSoup로 XML 파싱·데이터프레임화 |
| `pandas12.py` | JSON dumps/loads, 웹 JSON 데이터 사용 |
| `pandas13.py` | SQLite 조회 결과를 Pandas DataFrame으로 변환 |
| `pandas14.py` | MariaDB JOIN 조회, CSV 내보내기, read_sql, 교차표·집계 |
| `pandas15.py` | 웹페이지 데이터 수집과 Playwright 사용 |
| `pandas16.py` | 판매 CSV를 pivot_table로 날짜·상품별 집계 |
| `pandas17.py` | MariaDB 직원·고객 데이터 분석과 SQLAlchemy 연동 |
| `prac1.py` | NumPy 배열·인덱싱·Pandas를 활용한 종합 분석 과제 |
| `test.py` | Pandas DataFrame 간단 테스트 |

**확인된 코드 파일 수:** 32개

---

## pro11anal2 — 통계 분석·설문 시스템

| 파일 | 내용 |
|---|---|
| `fpro_coffee/analysis.py` | 커피 설문 DataFrame 분석 및 막대차트 생성 |
| `fpro_coffee/app.py` | 설문 입력·DB 저장·통계분석 결과 렌더링을 담당하는 Flask 서버 |
| `fpro_coffee/db.py` | MariaDB 연결, 설문 저장 및 전체 조회 |
| `fpro_coffee/templates/coffee/coffeesurvey.html` | 기초 코딩 실습 (파일 내 세부 예제 확인 권장) |
| `fpro_coffee/templates/coffee/result.html` | 기초 코딩 실습 (파일 내 세부 예제 확인 권장) |
| `fpro_coffee/templates/index.html` | 기초 코딩 실습 (파일 내 세부 예제 확인 권장) |
| `prac1.py` | 진학여부/학력 등 범주형 변수의 카이제곱 문제 |
| `prac2.py` | 두 표본 t 검정 활용 과제(판매·직원데이터 등) |
| `prac3.py` | 중간·기말 점수로 대응표본 t 검정 |
| `prac4.py` | 유형별 평균 비교를 위한 ANOVA 실습 과제 |
| `test1.py` | 기술통계/분산 이해 및 집단 간 t 검정 예제 |
| `test2.py` | 범주형 교차분석·카이제곱 독립성 검정 |
| `test3.py` | 일원 카이제곱 적합도 검정 |
| `test4.py` | 관측도수·기대도수에 대한 카이제곱 적합도 검정 |
| `test5.py` | 이원 카이제곱 검정 |
| `test6.py` | 교차표를 이용한 범주형 연관성 검정 |
| `test7.py` | 일표본 t 검정 예제 |
| `test8.py` | Shapiro 정규성 검정, Wilcoxon·일표본 t 검정 |
| `test9.py` | 정규성 검사 후 일표본 t 검정 실습 |
| `test10.py` | 남녀 두 독립집단의 평균 t 검정 |
| `test11.py` | 정규성·등분산성 검정 후 독립표본 t 검정 |
| `test12.py` | 날씨/매출액 집단 비교: 독립표본 t 검정 |
| `test13.py` | 전후 측정값의 대응표본 t 검정 |
| `test14.py` | 일원 분산분석, 정규성·등분산성, Tukey 사후검정 |
| `test15.py` | 일원분산분석 ANOVA 실습 |
| `test16.py` | Welch ANOVA/등분산성 차이를 고려한 분산분석 |
| `test17.py` | 이원분산분석의 주효과·상호작용 효과 검정 |

**확인된 코드 파일 수:** 27개

---

## 데이터·이미지·환경 관련 참고

- `pro1/test18ani.jpeg`, `test18ani2.jpg`: OpenCV 이미지 예제용 자료
- `pro2/zipcode.txt`, `practice7data.txt`: 텍스트 검색·집계 실습 자료
- `pro3db/.env`, `pro3db/dbconnect.json`, `pro5web2/cgi-bin/.env`: **실제 저장소에는 올리지 말 것**
- `pro6web3basic/images/`, `pro7quiz/images/`: HTML 화면에서 참조하는 이미지
- `pro8js/*.json`, `sangpum.csv`: AJAX 테스트 데이터
- `pro10anal1/titanic_data.csv`, `pandas5student.csv`, `sales_data.csv`, XML·텍스트 자료: Pandas 실습 데이터
- `pro11anal2/cleanDescriptive.csv`, `pass_cross.csv`, `fpro_coffee/static/images/vbar.png`: 통계·웹 분석 예제 리소스

## 공개 저장소에 올리기 전에

`README.md`와 `GITHUB_UPLOAD_GUIDE.md`를 참고해 DB 비밀번호를 먼저 제거하고 `.gitignore`를 적용하세요. 특히 **파이썬 소스 안에 직접 작성된 비밀번호는 `.gitignore`만으로 보호되지 않습니다.**
