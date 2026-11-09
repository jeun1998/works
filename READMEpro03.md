# pro3db — SQL·관계형 데이터베이스·TCP 소켓

> **학습 목표:** Python에서 SQLite/MariaDB를 다루고, TCP 기반 클라이언트·서버 통신 흐름을 이해한다.

## 1. 데이터베이스 핵심 이론

### ① 관계형 DB와 SQL
- 데이터는 **테이블(행/열)**에 저장된다. 기본키(PK)는 행을 구별하고, 외래키(FK)는 테이블 관계를 연결한다.
- **DDL:** `CREATE`, `ALTER`, `DROP`으로 구조 정의.
- **DML:** `SELECT`, `INSERT`, `UPDATE`, `DELETE`로 데이터 조회·변경.
- `WHERE`는 행 필터링, `ORDER BY`는 정렬, `GROUP BY`는 그룹 집계, `HAVING`은 집계 결과 조건이다.
- **JOIN:** 관계된 테이블을 연결한다. `INNER JOIN`은 일치하는 행, `LEFT JOIN`은 왼쪽 기준 행을 보존한다.
- **트랜잭션:** 여러 변경 작업을 논리적 단위로 처리한다. 변경 후 `commit()`, 오류 시 `rollback()`을 고려한다.

```sql
SELECT j.jikwonname, b.busername, j.jikwonpay
FROM jikwon AS j
JOIN buser AS b ON j.busernum = b.buserno
WHERE j.jikwonpay >= 3000
ORDER BY j.jikwonpay DESC;
```

### ② Python-DB 연결
- `sqlite3`는 별도 DB 서버 없이 로컬 파일 또는 메모리 DB를 사용할 수 있다.
- MariaDB 예제는 `MySQLdb`(`mysqlclient`) 드라이버를 사용한다.
- 일반적인 흐름: `connect → cursor → execute → fetchall → commit(변경 시) → close`.
- 사용자 입력을 SQL에 문자열 포맷팅으로 붙이지 않고 **바인딩 변수**를 사용해야 SQL Injection 위험을 줄일 수 있다.

```python
# MariaDB 커서 예시 (연결 정보는 환경변수로 구성)
cur.execute('SELECT jikwonname FROM jikwon WHERE jikwonno=%s', (emp_no,))
row = cur.fetchone()
```

### ③ 환경변수 관리
- `.env` 파일은 DB 비밀번호 등 민감한 정보를 저장하므로 **GitHub에 절대 업로드하지 않는다**.
- `python-dotenv`의 `load_dotenv()`와 `os.getenv()`로 연결 정보를 읽는 방식이 학습 코드에 등장한다.
- DB 설정 파일(`dbconnect.json`)에도 실제 계정 정보가 들어 있다면 공개하지 않는다.

## 2. 네트워크·소켓 이론

- **TCP:** 연결형 프로토콜. 데이터의 순서·전달을 보장하는 바이트 스트림 제공.
- 서버 흐름: `socket → bind → listen → accept → recv/send → close`.
- 클라이언트 흐름: `socket → connect → send/recv → close`.
- 네트워크 메시지는 바이트 단위로 주고받으므로 `.encode()` / `.decode()`가 필요하다.
- 한 번의 `recv()`가 메시지 한 건과 정확히 일치하지 않을 수 있으므로 실무에서는 메시지 경계를 정의한다.

## 3. 실제 코드와 개념 연결

| 파일 | 학습 포인트 |
|---|---|
| `db1.py` | SQLite 테이블 생성·조회 |
| `db2maria.py` | MariaDB 연결과 상품 SQL·CRUD |
| `db3maria.py` | 직원·부서 JOIN 기반 조회/로그인 실습 |
| `prac1.py` | JOIN, 그룹 집계, 성별·급여 분석 등의 응용 |
| `문제2_전재현_.py` | 성별 인원수 및 평균급여 집계 |
| `socket1server.py`, `socket1client.py` | 1회성 TCP 통신 |
| `socket2server.py`, `socket2client.py` | 반복 접속과 서버-클라이언트 상호작용 |
| `socket_test.py` | 소켓 주소와 포트 등 네트워크 기본기 |

## 4. 실행·준비

```bash
cd projects/pro3db
python db1.py
# MariaDB가 준비된 경우
python db3maria.py
# 소켓은 서버 실행 후 별도 터미널에서 클라이언트 실행
python socket1server.py
```

별도 터미널: `python socket1client.py`. MariaDB 예제는 동일한 DB 스키마와 테이블이 필요하고, 실습용 IP/포트는 로컬 환경에 맞게 수정해야 한다.

**보안 점검:** 하드코딩된 DB 비밀번호, `.env`, DB 덤프, 개인 데이터가 커밋에 포함되지 않았는지 확인한다.

[⬅ 프로젝트 목록으로](../README.md)
