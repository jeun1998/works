-- 주석
-- C(insert), R(select), U(update), D(delete) 잠깐 연습

CREATE TABLE good(no INT PRIMARY key, name VARCHAR(10) NOT NULL, tel VARCHAR(10),
inwon INT, addr TEXT);

DESC good;

--자료 추가
-- 형식: insert into 테이블명(칼럼명 타입, ..NO.) values(자료,...)
INSERT INTO good(no, name, tel, inwon, addr) VALUES(1, '인사과', '123-4567', 5, '삼성1동');
INSERT INTO good VALUES(2, '영업과', '123-2222', 12, '역삼2동');
INSERT INTO good(no, name, inwon) VALUES('3','자재과','7');
INSERT INTO good(addr, no, name, inwon) VALUES('역삼3동', '4','자재2과','7');

SELECT * FROM good;

--오류인 경우
INSERT INTO good(NO, NAME) VALUES(3, '자재3과');  --NO 중복 에러
INSERT INTO good(NO, tel) VALUES(5, '자재3과'); --NAME은 NOT NULL : 반드시 입력
INSERT INTO good(NAME, NO) VALUES(5, '자재3과'); --입력자료와 칼럼의 순서가 불잁치
INSERT INTO good(NO, NAME) VALUES('오', '자재3과'); --입력자료 타입 불일치
INSERT INTO good(addr, NO, NAME, inwon) VALUES(5, '우리회사에서 가장 매출이 좋은 부러운 부서'); --입력자료 크기 오류

--자료 수정
--형식: update 테이블명 set 칼럼명=수정값, ...where 조건
UPDATE good SET inwon 100 WHERE NO=1;
UPDATE good SET inwon=70, tel='777-7777' WHERE NO=2;
UPDATE good SET inwon=2, tel=null WHERE NO=2;

SELECT * FROM good;

--오류인 경우
UPDATE good SET name=null WHERE NO=2;   --NAME 은 NOT NULL: 반드시 입력
UPDATE good SET NO=2 WHERE NO=1; -- no 중복 오류

-- 자료 삭제
-- 형식 : delete from 테이블명 where 조건
DELETE FROM good WHERE NO=2;
SELECT * FROM good;

-- 형식2: truncate table 테이블명  - where 조건 없음.행 모두 삭제. 구조만 남음
TRUNCATE TABLE good;
SELECT * FROM good;

DROP TABLE good;   ---테이블 삭제

SHOW TABLES; 

-------------------------------------------------------------
--데이터베이스 무결성은 저장된 데이터가 정확하고 일관되며,
--손상되지 않고 신뢰할 수 있는 상태를 유지하는 것을 뜻한다.
--데이터의 품질을 지키고 오류를 막기 위해 데이터베이스 관리 시스템이 지키는 핵심 규칙,
--주요 무결성 제약 조건
--- 개체 무결성(entity integrity): 모든 테이블은 기본 키를 가져야 한다.
--  기본 키는 빈 값이나 중복 값을 가질 수 없습니다.
--- 도메인 무결성(domain integrity): 필드에 들어가는 값이 지정된 자료형, 범위, 조건에 맞아야 한다.
--- 사용자 정의 무결성 (user-defined integrity): 업무 규칙에 맞게 사용자가 직접 만든 조건이나트리
--- 참조 무결성(referential integrity): 테이블 간의 관계를 뜻한다.
--- 외래 키 값은 참조하는 테이블의 기본 키와 일치하거나 빈 값이어야 한다.

--무결성이 중요한 이유중복 데이터나
--- 잘못된 입력 값을 막는다.
--- 부모와 자식 데이터의 연결이 끊어지지 않게 돕는다.
--- 시스템 오류를 줄이고 데이터 신뢰도를 높인다.

--기본키 제약 조건 - entity integrity
--기본 키는 빈값이나 중복 값을 가질 수 없다. 자동으로 인덱스가 생성됨.

--참고 : 테이블 작성시 칼럼의 이름, 타입은 중요. 순서는 마음대로. 
--       계산에 의해 처리될 수 있는 값은 칼럼으로 작성x
--       예) 국어, 영어 따위는 칼럼으로 작성. 총점, 평균은 칼럼으로 작성x
--방법1) 칼럼 레벨

CREATE TABLE aa(bun INT PRIMARY KEY, irum CHAR(10));
DESC aa;
INSERT INTO aa VALUES(1, 'tom');
INSERT INTO aa VALUES(2, 'tom');
INSERT INTO aa VALUES(3, 'tom');  -- pk err : 중복 불가
INSERT INTO aa(irum) VALUES('tom')  -- pk err : not null
SELECT * FROM aa;


-- 제약 조건 확인
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='aa';

DROP TABLE aa;

-- 방법2) 테이블 레벨
CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_bun_pk PRIMARY KEY(bun));
DESC aa;
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='aa'; 

alter TABLE aa DROP CONSTRAINT aa_bun_pk; -- pk 제약조건 삭제
alter TABLE aa DROP PRIMARY KEY;  -- pk 제약조건 삭제  
DROP TABLE aa;

-- check 제약 조건 - domain integrity :  입력 값 조건 부여
CREATE TABLE aa(bun INT, irum CHAR(10), nai INT CHECK(nai >= 20));
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='aa'
INSERT INTO aa VALUES(1, 'tom', 25);
INSERT INTO aa VALUES(2, 'tom', 15);  -- chk err : nai 조건 불만족

ALTER TABLE aa ADD constraint ck_name CHECK(irum IN('tom', 'john'));  -- check 조건 추가
INSERT INTO aa VALUES(2, 'john', 25);
INSERT INTO aa VALUES(2, 'james', 25);
DROP TABLE aa;

-- unique 제약 조건 - Domain Integrity : 입력 값 조건 부여
CREATE TABLE aa(bun INT, irum CHAR(10) UNIQUE);
INSERT INTO aa VALUES(1, 'john');
INSERT INTO aa VALUES(2, 'tom');
INSERT INTO aa VALUES(3, 'tom'):  -- unique err: 중복 불가
DROP TABLE aa;

-- referential integrity (참조키, foreign key, fk, 외래키) 제약 조건
-- 다른 테이블의 칼럼값을 참조 (fk의 대상은 다른 테이블의 pk 또는 unique 가능)

testCREATE TABLE jikwon(bun INT PRIMARY KEY, irum VARCHAR(10) NOT NULL, buser CHAR(10));
INSERT INTO jikwon VALUES(1, '한송이', '인사과');
INSERT INTO jikwon VALUES(2, '박치기', '인사과');
INSERT INTO jikwon VALUES(3, '한송이', '총무과');
SELECT * FROM jikwon;

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10), birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun));

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10), birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun) ON DELETE RESTRICT ON UPDATE RESTRICT);  --위와 동일 
-- 부모 데이터를 자식이 참조하고 있으면 부모의 삭제나 키 변경을 막는다.

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10), birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun) ON DELETE CASCADE ON UPDATE SET NULL);
-- CASCADE : 부모 삭제시 자식도 삭제
-- SET NULL : 부모 참조키 변경시 자식의 FK 칼럼 값은 NULL이됨
-- 대개의 경우 부모의 pk는 변경이 흔하지 않으므로 SET NULL은 자주 사용되지 않는다.

DESC gajok;
INSERT INTO gajok VALUES(10, '가나다', NOW(), 1);
INSERT INTO gajok VALUES(20, '이겨라', '2000-5-5', 2);
INSERT INTO gajok VALUES(30, '한국인', '2010-5-15', 1);

-- INSERT INTO gajok VALUES(40, '지구인', '2010-5-15', 5); --fk err: 5번 직원없음
SELECT * FROM gajok;

-- 직원 자료 삭제
DELETE FROM jikwon WHERE bun = 3;
DELETE FROM jikwon WHERE bun = 2;  -- err : 2번 직원의 가족이 있기 때문
DELETE FROM gajok WHERE CODE=20; -- 2번 직원의 가족 삭제
DELETE FROM jikwon WHERE bun = 2;  --성공: 가족이 없기 때문 testtest

SELECT * FROM jikwon;

DROP TABLE jikwon;  -- err 테이블 삭제 불가 - 참조되고 있는 자식 테이블 때문
DROP TABLE gajok;
DROP TABLE jikwon;

SHOW TABLES;

-- default : 특정 칼럼에 초기값 부여 - null 방지 목적
CREATE TABLE aa(bun INT AUTO_INCREMENT PRIMARY KEY, irum CHAR(10),
juso VARCHAR(50) DEFAULT '역삼동');  
-- AUTO_INCREMENT : 번호 자동 증가
-- Oracle은 AUTO_INCREMENT X : SEQUENCE를 사용
DESC aa;
INSERT INTO aa(irum, juso) VALUES('길동', '서초동');
INSERT INTO aa(irum, juso) VALUES('나라', '익선동');
INSERT INTO aa(irum) VALUES('국가');
ALTER TABLE aa AUTO_INCREMENT=100;
INSERT INTO aa(irum, juso) VALUES('순신', '필동');
INSERT INTO aa(irum, juso) VALUES('철수', '대치동');
SELECT * FROM aa;

DROP TABLE aa;

-- 연습문제

-- 1. 교수 테이블 생성
CREATE TABLE professer(
    pk INT PRIMARY KEY,
    irum VARCHAR(20),
    room INT CHECK (room BETWEEN 100 AND 500)
);
DESC professer;

-- 2. 교수 데이터 입력
INSERT INTO professer(pk, irum, room)
VALUES(541, '홍교교수', 201);

INSERT INTO professer(pk, irum, room)
VALUES(542, '이교수', 305);


-- 교수 확인
SELECT * FROM professer;


-- 3. 과목 테이블 생성
CREATE TABLE subj(
    pk INT AUTO_INCREMENT PRIMARY KEY,
    uq VARCHAR(30) UNIQUE,
    bookname VARCHAR(30),
    fk INT,
    FOREIGN KEY(fk) REFERENCES professer(pk)
);
DESC subj;


-- 4. 과목 데이터 입력
-- pk는 AUTO_INCREMENT이므로 입력하지 않음
INSERT INTO subj(uq, bookname, fk)
VALUES('신소재공학개론', '재료과학과공학', 541);

INSERT INTO subj(uq, bookname, fk)
VALUES('세라믹공학', '세라믹재료학', 542);


-- 과목 확인
SELECT * FROM subj;


-- 5. 학생 테이블 생성
CREATE TABLE stu(
    pk INT PRIMARY KEY,
    stuname VARCHAR(20),
    fk INT,
    grnum INT DEFAULT 1 CHECK (grnum BETWEEN 1 AND 4),
    FOREIGN KEY(fk) REFERENCES subj(pk)
);
DESC subj;

-- 6. 학생 데이터 입력
INSERT INTO stu(pk, stuname, fk, grnum)
VALUES(1001, '전재현', 1, 3);

INSERT INTO stu(pk, stuname, fk, grnum)
VALUES(1002, '박보근', 2, 2);


-- 학년을 생략하면 DEFAULT 1 적용
INSERT INTO stu(pk, stuname, fk)
VALUES(1003, '이진련', 1);


-- 학생 확인
SELECT * FROM stu; -- 다시 점검 해보기



-- 인덱스 : 쉽게 말하면 책의 목차나 색인과 비슷하다. 검색 속도 향상이 목표
-- 인덱스 없음 -> 처음부터 끝까지 데이터를 확인
-- 인덱스 있음 -> 위치를 빠르게 찾아서 데이터 접근  

CREATE TABLE aa (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20),
age INT, city VARCHAR(30));

INSERT INTO aa(name, age, city) VALUES
('홍길동', 25, '서울'),
('김철수', 20, '부산'),
('이영희', 27, '서울'),
('박민수', 35, '대전'),
('최영희', 23, '인천'),
('강호동', 40, '서울'),
('유재석', 38, '부산'),
('신동엽', 42, '서울'),
('홍길동', 29, '수원'),
('김민지', 31, '대구');

SELECT * FROM aa;

SELECT * FROM aa WHERE NAME='강호동'; -- 인덱스가 없으므로 전체 테이블 검색

-- 실행 계획 확인
explain SELECT * FROM aa WHERE NAME='강호동'; -- type: ALL - FULL TABLE SCAN

-- 검색을 자주하는 name에 인덱스 생성 - 인덱스 테이블 별도 생성 
CREATE INDEX idx_aa_name ON aa(NAME); -- 이미 테이블이 있는 경우 
SHOW INDEX FROM aa; -- idx_aa_name와 pk(인덱스 자동생성) 인덱스 확인 가능 
SHOW KEYS FROM aa;

-- 테이블 생성시 인덱스 부여
CREATE TABLE aa (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20),
age INT, city VARCHAR(30), INDEX idx_aa_name (name));

-- 참고 :  인덱스가 여러개인 경우 '올티마이저'가 적당한 인덱스를 선택해 실행 
DESC aa;

-- idx_aa_name 테이블 생성
-- 강호동 -> 위치(pointer - pk값) pk가 없으면 내부적으로 ROW id를 만듦
-- 이영희 -> 위치

-- index 삭제
DROP INDEX idx_aa_name ON aa;
SHOW INDEX FROM aa;

-- index는 특정 칼럼의 검색 속도 증진이 목적이나 단점도 있다. 
-- insert, update, delete 등이 빈번한 경우에는 인덱스 재설정 비용이 든다. 

-- 참고 : 내장함수 now(), sysdate()의 차이
SELECT NOW(), SLEEP(2), NOW(); -- 결과가 같다.
SELECT NOW(), SLEEP(2), SYSDATE(); -- 결과가 다르다.
-- SYSDATE()는 동일 SQL 문장 내에서 호출되는 시점에 따라 결과값을 바로 반환 

-- 테이블 관련 명령
-- create table 테이블명 ~  생성
-- alter table 테이블명 ~   구조를 수정
-- drop table 테이블명 ~    삭제

CREATE TABLE aa(irum CHAR(10), juso VARCHAR(50));
ALTER TABLE aa RENAME kbs;  -- 테이블 이름 변경
SELECT * FROM aatest;  -- X
SELECT * FROM kbs;  -- O
ALTER TABLE kbs RENAME aa;

-- 칼럼 관련 명령
ALTER TABLE aa ADD (job_id INT DEFAULT 10);
DESC aa;
INSERT INTO aa VALUES('tom', 'seoul', 20);
INSERT INTO aa(irum, juso) VALUES('tom2', 'jeju');
SELECT * FROM aa;

ALTER TABLE aa CHANGE job_id job_number INT;  -- 칼럼명 변경 
SELECT * FROM aa;

ALTER TABLE aa MODIFY job_number VARCHAR(10); -- 칼럼 타입 변경
DESC aa;
SELECT * FROM aa;

DROP TABLE aa;

--  본격 실습 ---------------------------

CREATE TABLE sangdata (
    code INT PRIMARY KEY,
    sang VARCHAR(20),
    su INT,
    dan INT
);

INSERT INTO sangdata VALUES (1, '장갑', 3, 10000);
INSERT INTO sangdata VALUES (2, '벙어리장갑', 2, 12000);
INSERT INTO sangdata VALUES (3, '가죽장갑', 10, 50000);
INSERT INTO sangdata VALUES (4, '가죽점퍼', 5, 650000);
select * from sangdata;


CREATE TABLE buser (
    buserno INT PRIMARY KEY,
    busername VARCHAR(10) NOT NULL,
    buserloc VARCHAR(10),
    busertel VARCHAR(15)
);

INSERT INTO buser VALUES (10, '총무부', '서울', '02-100-1111');
INSERT INTO buser VALUES (20, '영업부', '서울', '02-100-2222');
INSERT INTO buser VALUES (30, '전산부', '서울', '02-100-3333');
INSERT INTO buser VALUES (40, '관리부', '인천', '032-200-4444');
UPDATE buser
SET busername = '전략기획부'
WHERE buserno = 50;
select * from buser;


-- 참고 : 만약 자동 증가를 원한다면 (PostgreSQL 방식) 
-- MariaDB의 AUTO_INCREMENT에 해당하는 PostgreSQL 방식은
CREATE TABLE buser (
    buserno INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    busername VARCHAR(10) NOT NULL,
    buserloc VARCHAR(10),
    busertel VARCHAR(15)
);
그리고 INSERT는 아래 처럼.
INSERT INTO buser (busername, buserloc, busertel) VALUES ('총무부', '서울', '02-100-1111');

CREATE TABLE jikwon (
    jikwonno INT PRIMARY KEY,
    jikwonname VARCHAR(10) NOT NULL,
    busernum INT NOT NULL,
    jikwonjik VARCHAR(10) DEFAULT '사원',
    jikwonpay INT,
    jikwonibsail DATE,
    jikwongen VARCHAR(4),
    jikwonrating CHAR(3),
    CONSTRAINT ck_jikwongen CHECK (jikwongen = '남' OR jikwongen = '여')
);

INSERT INTO jikwon VALUES
(1,'홍길동',10,'이사',9900,'2008-09-01','남','a'),
(2,'한송이',20,'부장',8800,'2010-01-03','여','b'),
(3,'이순신',20,'과장',7900,'2010-03-03','남','b'),
(4,'이미라',30,'대리',4500,'2014-01-04','여','b'),
(5,'이순라',50,'사원',3000,'2017-08-05','여','b'),
(6,'김이화',20,'사원',2950,'2019-08-05','여','c'),
(7,'김부만',40,'부장',8600,'2009-01-05','남','a'),
(8,'김기만',20,'과장',7800,'2011-01-03','남','a'),
(9,'채송화',30,'대리',5000,'2013-03-02','여','a'),
(10,'박치기',10,'사원',3700,'2016-11-02','남','a'),
(11,'김부해',30,'사원',3900,'2016-03-06','남','a'),
(12,'박별나',40,'과장',7200,'2011-03-05','여','b'),
(13,'박명화',10,'대리',4900,'2013-05-11','남','a'),
(14,'박궁화',40,'사원',3400,'2016-01-15','여','b'),
(15,'채미리',20,'사원',4000,'2016-11-03','여','a'),
(16,'이유가',20,'사원',3000,'2016-02-01','여','c'),
(17,'한국인',10,'부장',8000,'2006-01-13','남','c'),
(18,'이순기',30,'과장',7800,'2011-11-03','남','a'),
(19,'이유라',30,'대리',5500,'2014-03-04','여','a'),
(20,'김유라',20,'사원',2900,'2019-12-05','여','b'),
(21,'장비',20,'사원',2950,'2019-08-05','남','b'),
(22,'김기욱',40,'대리',5850,'2013-02-05','남','a'),
(23,'김기만',30,'과장',6600,'2015-01-09','남','a'),
(24,'유비',20,'대리',4500,'2014-03-02','남','b'),
(25,'박혁기',10,'사원',3800,'2016-11-02','남','a'),
(26,'김나라',10,'사원',3500,'2016-06-06','남','b'),
(27,'박하나',20,'과장',5900,'2012-06-05','여','c'),
(28,'박명화',20,'대리',5200,'2013-06-01','여','a'),
(29,'박가희',10,'사원',4100,'2016-08-05','여','a'),
(30,'최미숙',30,'사원',4000,'2015-08-03','여','b');
UPDATE jikwon
SET busernum = 50
WHERE jikwonname = '이순라';
select * from jikwon;

CREATE TABLE gogek (
    gogekno INT PRIMARY KEY,
    gogekname VARCHAR(10) NOT NULL,
    gogektel VARCHAR(20),
    gogekjumin CHAR(14),
    gogekdamsano INT,
    CONSTRAINT fk_gogekdamsano FOREIGN KEY (gogekdamsano) REFERENCES jikwon(jikwonno)
);

INSERT INTO gogek VALUES
(1,'이나라','02-535-2580','850612-1156777',5),
(2,'김혜순','02-375-6946','700101-1054777',3),
(3,'최부자','02-692-8926','890305-1065777',3),
(4,'김해자','032-393-6277','770412-2028777',13),
(5,'차일호','02-294-2946','790509-1062777',2),
(6,'박상운','032-631-1204','790623-1023777',6),
(7,'이분','02-546-2372','880323-2558777',2),
(8,'신영래','031-948-0283','790908-1063777',5),
(9,'장도리','02-496-1204','870206-2063777',4),
(10,'강나루','032-341-2867','780301-1070777',12),
(11,'이영희','02-195-1764','810103-2070777',3),
(12,'이소리','02-296-1066','810609-2046777',9),
(13,'배용중','02-691-7692','820920-1052777',1),
(14,'김현주','031-167-1884','800128-2062777',11),
(15,'송운하','02-887-9344','830301-2013777',2);
select * from gogek;


DESC buser;
DESC jikwon;
DESC gogek;

-- select 출발 : 다다음주 부터

-- SELECT [DISTINCT] db명.소유자명.테이블명.칼럼명 [AS별명]...information_schema[INTO 테이블명]
-- FROM 테이블명...
-- WHERE 조건...
-- ORDER BY 기준키 ASC[DESC]

-- select 조회방법
-- 행단위 조회 : selection
-- 열단위 조회 : projection

DESC jikwon;
SELECT * FROM jikwon; -- 모든 행, 열 읽기
SELECT jikwonno,jikwonname,jikwonpay FROM jikwon; -- 일부 칼럼만 읽기
SELECT jikwonpay,jikwonno,jikwonname FROM jikwon; -- 칼럼 순서 동적으로 읽기
SELECT jikwonno AS 사번,jikwonname 직원명 FROM jikwon; -- 칼럼에 별명 부여

SELECT 10,'안녕',12 / 3 AS result FROM DUAL; -- DUAL: 가상의 테이블
SELECT 10,'안녕',12 / 3 AS result;

SELECT jikwonname AS 직원명,jikwonpay AS 연봉,jikwonpay * 0.02 AS 세금 FROM jikwon -- 칼럼 연산 가능
SELECT concat(jikwonname,'님') AS 이름, jikwongem AS 성별 FROM jikwon; -- 문자열 더하기

SELECT test.jikwon.jikwonname FROM jikwon;
SELECT myjik.jikwonname FROM jikwon AS myjik; -- 테이블에 별명을 주고 별명.칼럼명 가능

-- 정렬(sort)
SELECT * FROM jikwon ORDER BY jikwonpay ASC;  -- jikwonpay별 오름차순 정렬
SELECT * FROM jikwon ORDER BY jikwonpay;
SELECT jikwonno,jikwonname,jikwongen FROM jikwon ORDER BY jikwongen;
SELECT jikwonno,jikwonname,jikwongen FROM jikwon ORDER BY jikwongen desc;
SELECT * FROM jikwon ORDER BY busernum ASC, jikwonjik DESC,jikwonpay asc;
SELECT jikwonname,jikwonpay / 100 * AS pay FROM jikwon ORDER BY pay DESC; -- 연산결과에 대한

SELECT distinct jikwonjik FROM jikwon; -- 중복 자료 배제
SELECT distinct jikwonjik, jikwonname FROM jikwon; -- 의미없음

-- 연산자 사용 : 우선순위 () > 산술 > 관계(비교) > is null, like, in > between, not > and > or
-- 행단위 조회 : selection
SELECT * FROM jikwon WHERE jikwonjik='대리';  -- 행(레코드) 제한
SELECT * FROM jikwon WHERE jikwonno <='5'; 
SELECT * FROM jikwon WHERE jikwonibsail='2010-01-03';
SELECT * FROM jikwon WHERE jikwonibsail >='17-01-03';
SELECT * FROM jikwon WHERE jikwonno=5 OR jikwonno=7;
SELECT * FROM jikwon WHERE jikwonno=5 and jikwonno=7; -- X
SELECT * FROM jikwon WHERE jikwonjik='사원' AND jikwongen='남' AND jikwonpay <= 4500;
SELECT * FROM jikwon WHERE jikwonjik='사원' AND jikwongen='여' OR jikwonbsail >= '2017-1-1';
SELECT * FROM jikwon WHERE jikwonjik='사원' AND (jikwongen='여' OR jikwonbsail >= '2017-1-1');

SELECT * FROM jikwon WHERE jikwonno >= 5 AND jikwonno <=10;
SELECT * FROM jikwon WHERE jikwonno BETWEEN 5 AND 10; -- 결과 위와 동일 (상동)
SELECT * FROM jikwon WHERE jikwonno < 5 AND jikwonno > 20;
SELECT * FROM jikwon WHERE jikwonno not BETWEEN 5 AND 10; -- 결과 위와 동일
-- 참고 : 조건은 긍정적 형태일 경우 속도가 빠름 

SELECT * FROM jikwon WHERE jikwonibsail BETWEEN '2015-1-1' AND '2016-12-31';

SELECT * FROM jikwon WHERE jikwonname='홍길동';
SELECT * FROM jikwon WHERE jikwonname >='한';  -- 이를 근거로 문자도 연산 가능 
SELECT ASCII('a'),ASCII('A'),ASCII('가'),ASCII('나');
SELECT * FROM jikwon WHERE jikwonname >='김' and jikwonname <='이';

-- in 멤버 조건 연산
SELECT * FROM jikwon WHERE jikwonjik ='대리' and jikwonjik ='과장' or jikwonjik ='부장';
SELECT * FROM jikwon WHERE jikwonjik IN ('대리','과장','부장');
SELECT * FROM jikwon WHERE busernum IN (10,30) ORDER BY busernum asc;

-- like 조건 연산: %(0개 이상의 문자열), _(한개 문자)
SELECT * FROM jikwon WHERE jikwonname LIKE '이%'; -- 이로 시작
SELECT * FROM jikwon WHERE jikwonname LIKE '%라'; -- 라로 끝나는
SELECT * FROM jikwon WHERE jikwonname LIKE '%순%'; -- 순이 포함된 
SELECT * FROM jikwon WHERE jikwonname LIKE '이%라'; -- 이로 시작 ~라로 끝나는

SELECT * FROM jikwon WHERE jikwonname LIKE '이_라'; -- 가운데 한 글자만 아무거나
SELECT * FROM jikwon WHERE jikwonname LIKE '__'; -- 이름이 두 글자만 

SELECT * FROM gogek;
SELECT * FROM gogek WHERE gogekname LIKE '__';
SELECT * FROM gogek WHERE gogekname LIKE '최%' OR gogekname LIKE '__라';

-- gogek 테이블에서 gogekjumin을 이용해 여성만 출력
SELECT * FROM gogek WHERE gogekjumin LIKE '%-2%' OR gogekjumin LIKE '%-4%';

SELECT * FROM jikwon WHERE jikwonpay LIKE '5%';

SELECT * FROM jikwon WHERE jikwonpay LIMIT 5, 4; -- 시작행, 행수: 현재 경우 5개를 건너뛰고 4개 읽기
SELECT * FROM jikwon WHERE jikwonpay LIKE '5%' LIMIT 3;

-- update, delete 에도 조건 연산자 사용 가능
UPDATE jikwon set jikwonpay=NULL WHERE jikwonno=5; - 5번 직원 연봉에 null
SELECT * FROM jikwon;
-- SELECT * FROM jikwon WHERE jikwonpay=NULL; --오류
SELECT * FROM jikwon WHERE jikwonpay IS NULL;
SELECT * FROM jikwon WHERE jikwonpay IS not NULL;

-- 다양한 연산자 조합
SELECT jikwonno AS 직원번호, jikwonname 직원명, jikwonjik, jikwonpay / 12 AS 보너스, mytab.jikwonibsail
FROM jikwon AS mytab
WHERE jikwonjik IN('과장','사원') AND
((jikwonpay >= 4000 AND jikwonibsail BETWEEN '2015-1-1' AND '2019-12-31'
ORDER BY jikwonjik ASC, jikwonpay DESC 
LIMIT 3;

SELECT JSON_OBJECT('jikwonno',jikwonno,'jikwonname',jikwonname) AS 'json data' FROM jikwon
WHERE jikwonjik='대리';

SELECT jikwonno,jikwonname,jikwonpay * 10000 INTO OUTFILE 'c:/works/jikdata.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
FROM jikwon WHERE jikwonjik='대리';

-- html 형식으로 파일에 저장
SELECT CONCAT(
'<table>'
'<tr>',
'<td>',jikwonno,'<td>',jikwonname,'</td>','<td>',jikwonpay * 10000,'</td>',
'</tr>'
'</table>'
) INTO OUTFILE 'c:/works/jikdata.html'
FROM jikwon WHERE jikwonjik='대리';

-- 내장 함수 호출 :  데이터 조작의 효율성 향상이 목적

-- 단일 행 함수 : 행 단위 처리
-- 문자 관련 함수
SELECT LOWER('Hello Sql'), UPPER('Hello Sql') FROM DUAL; -- 대,소문자로 변환
SELECT CONCAT('Hello' 'World');
SELECT SUBSTR('Hello World',3), SUBSTR('Hello World',3,3), SUBSTR('Hello World',-3,3); -- 문자열 일부 추출 
SELECT LENGTH('Hello World');
SELECT INSTR('Hello World', 'e'), INSTR('Hello World', 'k'); -- 특정 문자 위치를 반환 
SELECT TRIM(' aabb bbaa '), LTRIM(' aabb bbaa '), RTRIM(' aabb bbaa '); -- 앞뒤, 좌, 우의 공백 제거
SELECT REPLACE('011.1234.5678','.','-'), REPLACE('abc def abc', 'abc', 'ABC') FROM jikwon;  -- 문자열 치환 

SELECT jikwonname,jikwonjik,REPLACE(jikwonjik,'사원','평직원') FROM jikwon;

SELECT * FROM jikwon;
-- jikwon 테이블에서 이름에 '이'가 포함된 직원이 있다면 '이'부터 두글자 출력.
-- (마지막에 '이'가 있는 경우는 한 글자 출력)
SELECT jikwonname, SUBSTR(jikwonname, INSTR(jikwonname, '이'), 2) FROM jikwon
WHERE jikwonname LIKE '%이%';

-- 숫자 관련 함수 일부 체험
SELECT ROUND(12.3456),ROUND(12.3456, 0),ROUND(12.3456,1),ROUND(12.3456,-1),ROUND(17.345,-1);
SELECT CEIL(12.3456),FLOOR(17.345);
SELECT jikwonname,jikwonpay,ROUND(jikwonpay * 0.025, 0) AS tax FROM jikwon LIMIT 5;

SELECT TRUNCATE(45.678, 0),TRUNCATE(45.678, 1),TRUNCATE(45.678, -1); -- 자릿수 기준으로 정수 취하고 나타냄 
SELECT MOD(15, 2);
SELECT GREATEST(15.5,12,32),LEAST(15.5,12,32), POW(2, 3), SQRT(4);

-- 날짜 함수
SELECT CURDATE(), CURDATE() + 0;  -- 2026-09-07 
SELECT NOW(), NOW() + 0;
SELECT NOW(), SYSDATE();

-- 날짜 더하기/빼기
SELECT ADDDATE(DATE'2026-9-1',3), SUBDATE(DATE'2026-9-1',3);
SELECT DATE_ADD(NOW(),INTERVAL 1 MINUTE), DATE_ADD(NOW(),INTERVAL 5 DAY),DATE_ADD(NOW(),INTERVAL 1 MOUTH);
SELECT DATE_SUB(NOW(),INTERVAL 2 YEAR), DATE_SUB(NOW(),INTERVAL -2 YEAR);

SELECT DATEDIFF('2026-9-1','2023-6-1'), DATEDIFF(NOW(),'2030-6-1');
SELECT TIMEDIFF('2026-9-1','2023-6-1'), TIMEDIFF(NOW(),'2030-6-1');

-- 행 변환 함수 : DATE_FORMAT
SELECT DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%Y-%m-%d'), DATE_FORMAT(NOW(),'%Y년%m월%d일');
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%h:%S'),DATE_FORMAT(NOW(), '%y-%M-%D %h:%i:%S %W');
-- DATE_FORMAT 서식 검색을 이용

SELECT FORMAT(1234.567, 2), ROUND(1234.567, 2);  -- 숫자 타입이 문자열, 숫자 타입이 숫자

-- 기타 함수
-- rank() : 순위 결정
SELECT jikwonno,jikwonname,jikwonpay,
rank() OVER(ORDER BY jikwonpay),
dense_rank() OVER(ORDER BY jikwonpay)
FROM jikwon WHERE jikwonpay IS NOT null;

SELECT jikwonno,jikwonname,jikwonibsail,
rank() OVER(ORDER BY jikwonpay desc),
dense_rank() OVER(ORDER BY jikwonpay desc)
FROM jikwon;

-- nvl(value1, value2) : value1이 null이면 value2를 취함
UPDATE jikwon SET jikwonjik=NULL WHERE jikwonno=5;
SELECT * FROM jikwon WHERE jikwonno=5;
SELECT jikwonname,nvl(jikwonjik,'임시직'),nvl(jikwonpay,0) FROM jikwon;

-- nvl2(value1, value2, value3) : value1이 null이면 value3을 취하고 null이 아니면 value2를 취함
SELECT jikwonname,NVL2(jikwonjik, '정규직','임시직') AS jik,jikwongen,
NVL2(jikwonpay, jikwonpay, 0) AS pay
FROM jikwon;

-- nullif(value1, value2) : 두 개의 값이 일치하면 NULL을, 일치하지 않으면 value1을 취함
SELECT NULLIF(LENGTH('abcd'), LENGTH('123'));  -- 4
SELECT NULLIF(LENGTH('abc'), LENGTH('123'));  -- NULL
SELECT jikwonname,jikwonjik,NULLIF(jikwonjik,'사원') FROM jikwon WHERE jikwonjik IS NOT NULL;

-- 조건 표현식(Conditional Expressions)
-- 형식 1) case 표현식 when 비교값1 then 결과값1 when 비교값2 then 결과값2 ... [else 결과값n] end as 별명 
SELECT case 10 / 5 when 5 then '안녕' when 2 then '수고' else '잘가' END AS 결과 FROM DUAL;
SELECT jikwonname,jikwonpay,
case jikwonpay
when 3000 then '연봉3000'
when 3500 then '연봉3500'
else '기타연봉'
END AS result
FROM jikwon;

SELECT jikwonname,jikwonpay,jikwonjik,
case 
when '이사' then jikwonpay * 0.05
when '부장' then jikwonpay * 0.04
when '과장' then jikwonpay * 0.03
ELSE jikwonpay * 0.02
END AS donation
FROM jikwon;

-- 형식 2) case when 조건 1 then 결과값1 when 조건2 then 결과값2 ... [else 결과값n] end as 별명 
SELECT jikwonname,
case when jikwongen='남' then 'M' when jikwongen='여' then 'F' END AS gender
FROM jikwon;

SELECT jikwonname,jikwonpay,
case
when jikwonpay >= 7000 then '고액연봉'
when jikwonpay >= 5000 then '보통연봉'
ELSE '낮은연봉'
END AS result
FROM jikwon WHERE jikwonjik IN('대리','과장');

-- 조건 표현식(IF (조건) 참값, 거짓값 as 별명
SELECT jikwonname,jikwonpay,jikwonjik,
if(TRUNCATE(jikwonpay / 1000, 0) >= 5, 'good', 'normal') AS 'result'
from jikwon;

-- 문제 1
SELECT jikwonname AS 직원명, YEAR(NOW()) - YEAR(jikwonibsail) AS 근무년수,
case
when YEAR(NOW()) - YEAR(jikwonibsail) >= 10 then '감사합니다'
ELSE '열심히'
END AS 표현,
case
when YEAR(NOW()) - YEAR(jikwonibsail) >= 10 then ROUND(jikwonpay * 0.05)
ELSE ROUND(jikwonpay * 0.03)
END AS 특별수당
FROM jikwon WHERE jikwonibsail >= '2010-01-01';

-- 문제 2
SELECT jikwonname AS 직원명, jikwonjik AS 직급, DATE_FORMAT(jikwonibsail, '%Y-%m-%d') AS 입사년원일,
case
when YEAR(NOW()) - YEAR(jikwonibsail) >= 10 then '왕고참'
when YEAR(NOW()) - YEAR(jikwonibsail) >= 8 then '고참'
when YEAR(NOW()) - YEAR(jikwonibsail) >= 5 then '보통'
ELSE '일반'
END AS 구분,
case
when busernum=10 then '총무부'
when busernum=20 then '영업부'
when busernum=30 then '전산부'
when busernum=40 then '관리부'
END AS 부서
FROM jikwon
ORDER BY 입사년원일;

-- 문제 3
SELECT jikwonno AS 사번,jikwonname AS 직원명,busernum AS 부서,jikwonpay AS 연봉,
case
when busernum = 10 then ROUND(jikwonpay * 1.10)
when busernum = 30 then ROUND(jikwonpay * 1.20)
ELSE jikwonpay
END AS 인상연봉,
case
when YEAR(NOW()) - YEAR(jikwonibsail) >=10 then 'O'
ELSE 'X'
END AS 장기근속
FROM jikwon;

-- 복수행 함수 (집계 함수) : 전체 자료를 그룹별로 구분해 통계결과를 얻기 위한 함수
--                           NULL 값 무시 (count(*)는 예외)

SELECT sum(jikwonpay) AS 합, AVG(jikwonpay) AS 평균 FROM jikwon;
SELECT max(jikwonpay) AS 최대값, min(jikwonpay) AS 최소값 FROM jikwon;
SELECT * FROM jikwon;
SELECT AVG(jikwonpay), AVG(nvl(jikwonpay, 0)) FROM jikwon;
SELECT SUM(jikwonpay) / 29, SUM(jikwonpay) / 30 FROM jikwon;
SELECT COUNT(*), COUNT(jikwonno), COUNT(jikwonpay) FROM jikwon;
SELECT STDDEV(jikwonpay) AS 표준편차, STDDEV(jikwonpay) AS 표준편차 FROM jikwon;

-- 과장은 몇명?
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonjik='과장';

-- 2010년 이전에 입사한 남직원은 몇명?
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail < '2010-1-1' AND jikwongen='남';

-- 2015년 이후 입사한 여직원의 연봉합, 평균, 인원수?
SELECT sum(jikwonpay) 연봉합, sum(jikwonpay) 연봉평균, COUNT(*) AS 인원수
FROM jikwon WHERE jikwonibsail >= '2015-1-1' AND jikwongen='여';

-- 그룹 함수 - group by를 이용해 소계 출력
-- 형식 : select 그룹칼럼명, 계산함수 ...from 테이블명 where 조건
--        group by 그룹칼럼명 having 출력결과에 대한 조건
-- group by에 order by 할 수 없다.(내장됨) 단, 출력 결과는 order by 가능함

-- 성별 연봉의 평균, 인원수 출력
SELECT jikwongen, AVG(jikwonpay), COUNT(*) FROM jikwon GROUP BY jikwongen;
SELECT jikwongen, AVG(jikwonpay), COUNT(jikwonpay) FROM jikwon GROUP BY jikwongen;  -- NULL 제외
SELECT jikwongen, AVG(nvl(jikwonpay,0)), COUNT(*) FROM jikwon GROUP BY jikwongen;  -- NULL 처리

-- 부서별 연봉합
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

-- 부서별 연봉합 - 연봉합이 35000 이상
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;
SELECT busernum bun, SUM(jikwonpay) hap FROM jikwon GROUP BY busernum HAVING hap >= 35000;  -- 별명 사용 

-- 부서별 연봉합 - 연봉합이 15000 이상인 여직원이 대상
SELECT busernum, SUM(jikwonpay) FROM jikwon where jikwongen='여'
GROUP BY busernum HAVING SUM(jikwonpay) >= 15000;

-- SELECT busernum, SUM(jikwonpay) FROM jikwon ORDER BY busernum DESC GROUP BY busernum; -- 에러
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum 
ORDER BY SUM(jikwonpay) DESC; -- group by 결과에 대한 정렬은 가능 

-- 문제1
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon WHERE jikwonjik='사원';
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon WHERE jikwonjik='대리';
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon WHERE jikwonjik='과장';
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon WHERE jikwonjik='부장';
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon WHERE jikwonjik='이사';
SELECT jikwonjik, AVG(jikwonpay) FROM jikwon GROUP BY jikwonjik;

-- 문제2
SELECT jikwonjik, sum(jikwonpay) FROM jikwon WHERE jikwonjik='부장';
SELECT jikwonjik, sum(jikwonpay) FROM jikwon WHERE jikwonjik='과장';
SELECT jikwonjik, sum(jikwonpay) FROM jikwon WHERE jikwonjik IN('부장','과장') GROUP BY jikwonjik;

-- 문제3
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail < '2015-1-1';

-- 문제4
SELECT jikwonjik AS 직급, jikwongen AS 성별, COUNT(*) AS 인원수, SUM(jikwonpay) FROM jikwon group by jikwonjik, jikwongen;

-- 문제5
SELECT busernum, SUM(jikwonpay) FROM jikwon WHERE busernum = 10 or busernum = 20 GROUP BY busernum;

-- 문제6
SELECT jikwonjik, SUM(jikwonpay) hap FROM jikwon GROUP BY jikwonjik HAVING SUM(jikwonpay) >= 7000;

-- 문제7
SELECT jikwonjik, COUNT(*) AS 인원수, SUM(jikwonpay) FROM jikwon GROUP BY jikwonjik HAVING COUNT(*) >= 3;

-- join
-- 서로 다른 두 개 이상의 테이블에서 관련 있는 행을 연결해서 조회하는 기능
-- 서로 다른 테이블 간 공통 칼럼(성격이 같음)이 있어야 한다.

SELECT * FROM buser;
INSERT INTO buser(buserno,busername) VALUES(50,'전략기획부');

SELECT * FROM jikwon;
DESC jikwon; -- busernum 은 not null
-- 구조 변경
ALTER TABLE jikwon MODIFY busernum INT NULL;
UPDATE jikwon SET busernum=NULL WHERE jikwonno=5;
SELECT * FROM jikwon;

SELECT test.jikwon.jikwonname FROM jikwon;
SELECT jiktab.jikwonname FROM jikwon AS jiktab;

-- cross join: 두 테이블의 모든 행을 서로 한번씩 조합하는 조인 - 모든 경우의 수를 출력
-- 결과 행 수는 왼쪽행수*오른쪽행수
SELECT jikwonname,busername FROM jikwon,buser;
SELECT jikwonname,busername FROM jikwon cross join buser;
SELECT * FROM jikwon cross join buser;
SELECT jikwon.jikwonname,buser.busername FROM jikwon cross join buser; -- 동일 칼럼명 테이블 구분
SELECT j.jikwonname,b.busername FROM jikwon as j cross join buser as b; -- 별명 사용

-- self join: 한 개의 테이블로 cross join - 같은 테이블을 마치 다른 테이블처럼 별명을 붙여 연결
SELECT a.jikwonname, b.jikwonname FROM jikwon a, jikwon b;

-- EQUI join : 조인 조건식에 '='을 사용
SELECT jikwonname, busername FROM jikwon,buser
WHERE jikwon.busernum=buser.buserno;  -- 공통칼럼에 대해 '='을 사용 

-- NON-EQUI join : 조인 조건식에 '=' 이외의 관계 연산자를 사용
CREATE TABLE paygrade(grade INT PRIMARY KEY, lpay INT, hpay INT);
INSERT INTO paygrade VALUES(1, 0, 1999);
INSERT INTO paygrade VALUES(2, 2000, 2999);
INSERT INTO paygrade VALUES(3, 3000, 3999);
INSERT INTO paygrade VALUES(4, 4000, 4999);
INSERT INTO paygrade VALUES(5, 5000, 9999);
SELECT * FROM paygrade;

SELECT * FROM jikwon;
SELECT jikwonname, jikwonpay, grade
FROM jikwon, paygrade
WHERE jikwonpay >= lpay AND jikwonpay <= hpay;

SELECT J.jikwonname, J.jikwonpay, p.grade
FROM jikwon j JOIN paygrade p
ON j.jikwonpay >=p.lpay AND j.jikwonpay <=p.hpay;

SELECT J.jikwonname, J.jikwonpay, p.grade
FROM jikwon j JOIN paygrade p
ON j.jikwonpay between p.lpay AND p.hpay;

-- inner join: 두 테이블을 조인 할 때, 두 테이블에 모두 지정한 열의 데이터가 같아야 한다.
-- 조인 조건에 일치하는 데이터가 양쪽 테이블에 모두 존재하는 행만 조회하는 방식
-- 방법1: 테이블을 콤마(,)로 구분
SELECT jikwonno, jikwonname, busername FROM jikwon, buser
WHERE busernum = buserno;

SELECT jikwon.jikwonno,jikwon.jikwonname,buser.busername FROM jikwon, buser
WHERE jikwon.busernum = btab.buserno;  -- 별명 사용

SELECT jikwonno,jikwonname,busername FROM jikwon, buser
WHERE busernum = buserno AND jikwongen='남'; -- where에 조인 조건과 행 제한 조건이 함꼐 기술. 가독성이 하락

-- 방법2: ANSI JOIN 문법 - 조인 조건과 행 검색 조건을 분리 - 가독성 향상
SELECT jikwonno, jikwonname, busername
FROM jikwon INNER join buser ON busernum = buserno;

SELECT jikwonno, jikwonname, busername
FROM jikwon INNER join buser ON busernum = buserno
WHERE jikwongen='남';

-- outer join: 두 테이블을 조인 할 때, 조인 조건에 맞는 데이터뿐 아니라 한쪽 테이블에만 있는 데이터도
-- left ourte join: 왼쪽 테이블의 데이터는 모두 출력
SELECT jikwon.jikwonno,jikwon.jikwonname,buser.busername FROM jikwon, buser
WHERE jikwon.busernum = buser.buserno(+); -- 대응 안된 오른쪽 테이블에 null 허용.

SELECT jikwonno,jikwonname,busername
FROM jikwon LEFT OUTER JOIN buser ON jikwon.busernum = buser.buserno;
-- ANSI SQL
-- right outer join : 오른쪽 테이블의 데이터는 모두 출력
SELECT jikwon.jikwonno,jikwon.jikwonname,buser.busername FROM jikwon, buser
WHERE jikwon.busernum(+) = buser.buserno; -- 대응 안된 오른쪽 테이블에 null 허용.

SELECT jikwonno,jikwonname,busername
FROM jikwon RIGHT OUTER JOIN buser ON jikwon.busernum = buser.buserno;

-- full outer join: 양쪽 테이블의 모든 행을 조회하되 일치하지 않는 쪽의 칼럼은 null로 표시 
SELECT jikwonno,jikwonname,busername
FROM jikwon FULL OUTER JOIN buser ON jikwon.busernum = buser.buserno;

SELECT jikwonno,jikwonname,busername
FROM jikwon LEFT OUTER JOIN buser ON jikwon.busernum = buser.buserno
UNION
SELECT jikwonno,jikwonname,busername
FROM jikwon RIGHT OUTER JOIN buser ON jikwon.busernum = buser.buserno;

SELECT jikwonno,jikwonname,busername,busertel
FROM jikwon INNER JOIN buser ON jikwon.busernum = buser.buserno
WHERE jikwonname LIKE '김%';

SELECT SUM(jikwonpay) AS hap, COUNT(*) AS count
FROM jikwon INNER JOIN buser ON jikwon.busernum = buser.buserno
WHERE jikwonname LIKE '김%';

DESC buser;
DESC jikwon;  -- buserno, busernum 공통 칼럼
DESC gogek;  -- jikwonno, gogekdamsano 공통 칼럼. buser와 gogek은 공통 칼럼이 없어 직접 조인 불가 
SELECT * FROM gogek;

-- 문제1
SELECT j.jikwonno AS 사번, j.jikwonname AS 직원명, j.jikwonjik AS 직급, g.gogekname AS 고객명, g.gogektel AS 고객전화,
case
WHEN SUBSTR(g.gogekjumin, 8, 1) IN ('1', '3') THEN '남'
WHEN SUBSTR(g.gogekjumin, 8, 1) IN ('2', '4') THEN '여'
END AS 고객성별
FROM jikwon j
INNER JOIN gogek g ON j.jikwonno = g.gogekdamsano
WHERE j.jikwonno = '사원';

-- 문제2
SELECT j.jikwonno AS 사번, j.jikwonname AS 직원명, COUNT(g.gogekno) AS 고객수
FROM jikwon j
LEFT JOIN gogek g ON j.jikwonno = g.gogekdamsano
GROUP BY j.jikwonno, j.jikwonname
ORDER BY j.jikwonno;

-- 문제3
SELECT j.jikwonname AS 직원명, j.jikwonjik AS 직급
FROM gogek g
INNER JOIN jikwon j ON g.gogekdamsano = j.jikwonno
WHERE g.gogekname = '강나루';

-- 문제4
SELECT g.gogekname AS 고객명, g.gogektel AS 고객전화, g.gogekjumin AS 주민번호, TIMESTAMPDIFF(YEAR, STR_TO_DATE(CONCAT('19', LEFT(g.gogekjumin, 6)), '%Y%m%d'), CURDATE()) AS 나이
FROM jikwon j
INNER JOIN gogek g ON j.jikwonno = g.gogekdamsano
WHERE j.jikwonname = '이순신';

SELECT g.gogekname,g.gogektel,g.gogekjumin,
case
WHEN SUBSTR(g.gogekjumin, 8, 1) < 3 THEN DATE_FORMAT(NOW(), '%Y') - (SUBSTR(g.gogekjumin, 1, 2) + 1900)
ELSE DATE_FORMAT(NOW(), '%Y') - (SUBSTR(g.gogekjumin, 1, 2) + 2000)
END AS 나이
FROM jikwon j INNER JOIN gogek g
ON j.jikwonno = g.gogekdamsano
WHERE j.jikwonname = '이순신';

-- 세 개의 테이블 조인 
SELECT jikwonname,busername,gogekname FROM jikwon,buser,gogek
WHERE busernum=buserno AND jikwonno=gogekdamsano;

SELECT jikwonname,busername,gogekname
FROM jikwon
INNER JOIN buser ON busernum=buserno
INNER JOIN gogek ON jikwonno=gogekdamsano;

SELECT * FROM buser;
-- 서울에 근무하는 직원이 담당하는 고객출력
SELECT g.gogekname AS 고객명, j.jikwonname AS 담당직원, b.busername AS 부서명,b.buserloc AS 근무지역
FROM gogek g
INNER JOIN jikwon j ON j.jikwonno=g.gogekdamsano
INNER JOIN buser b ON j.busernum=b.buserno
WHERE b.buserloc='서울';

-- 담당 고객이 2명 이상인 직원 정보 출력
SELECT jikwonname AS 직원명,busername AS 부서명,COUNT(gogekno) AS 담당고객수
FROM jikwon j
INNER JOIN buser b ON j.busernum=b.buserno
INNER JOIN gogek g ON j.jikwonno=g.gogekdamsano
GROUP BY j.jikwonno, j.jikwonname, b.busername
HAVING 담당고객수 >= 2;


-- 문제5
SELECT COUNT(*) AS 고객수
FROM buser b
INNER JOIN jikwon j ON b.buserno = j.busernum
INNER JOIN gogek g ON j.jikwonno = g.gogekdamsano
WHERE b.busername = '총무부' AND TIMESTAMPDIFF(YEAR,STR_TO_DATE(CONCAT('19', LEFT(g.gogekjumin, 6)), '%Y%m%d'), CURDATE()) >= 30;

SELECT busername 부서명, COUNT(*) AS 고객수
FROM jikwon j
INNER JOIN buser b ON j.busernum = b.buserno
INNER JOIN gogek g ON j.jikwonno = g.gogekdamsano
WHERE b.busername = '총무부'
AND (case WHEN SUBSTR(g.gogekjumin,8,1) IN ('1','2')
THEN DATE_FORMAT(NOW(),'%Y') - (1900 + SUBSTR(g.gogekjumin,1,2))
ELSE DATE_FORMAT(NOW(),'%Y') - (2000 + SUBSTR(g.gogekjumin,1,2))
END) >= 30; -- 다른 분의 답

-- 문제6
SELECT IFNULL(b.busername, '무소속') AS 부서명, COUNT(g.gogekno) AS 고객수
FROM gogek g
LEFT JOIN jikwon j ON g.gogekdamsano = j.jikwonno
LEFT JOIN buser b ON j.busernum = b.buserno GROUP BY b.buserno, b.busername;


-- 문제7
SELECT j.jikwonname AS 직원명, j.jikwonjik AS 직급, IFNULL(b.busername, '무소속') AS 부서명, b.busertel AS 부서전화, j.jikwongen AS 성별
FROM gogek g
INNER JOIN jikwon j ON g.gogekdamsano = j.jikwonno
LEFT JOIN buser b ON j.busernum = b.buserno
WHERE g.gogekname = '강나루';

-- 문제8
SELECT g.gogekname AS 고객명, g.gogektel AS 고객전화,
case
WHEN SUBSTR(g.gogekjumin, 8, 1) IN ('1', '3') THEN '남'
WHEN SUBSTR(g.gogekjumin, 8, 1) IN ('2', '4') THEN '여'
ELSE '확인필요' END AS 성별 FROM buser b
INNER JOIN jikwon j ON b.buserno = j.busernum
INNER JOIN gogek g ON j.jikwonno = g.gogekdamsano WHERE b.busername = '영업부' AND j.jikwonname = '이순신';

-- 문제 9
SELECT j.jikwonno AS 사번, j.jikwonname AS 직원명 FROM jikwon j
LEFT JOIN gogek g ON j.jikwonno = g.gogekdamsano WHERE g.gogekno IS NULL;

-- 문제 10
SELECT IFNULL(b.busername, '무소속') AS 부서명, j.jikwonname AS 직원명, j.jikwonjik AS 직급, COUNT(g.gogekno) AS 담당고객수
FROM jikwon j
LEFT JOIN buser b ON j.busernum = b.buserno
LEFT JOIN gogek g ON j.jikwonno = g.gogekdamsano
GROUP BY b.buserno, b.busername, j.jikwonno, j.jikwonname, j.jikwonjik
ORDER BY 담당고객수 DESC, j.jikwonno ASC;

SELECT b.busername AS 부서명, j.jikwonname AS 직급, COUNT(g.gogekno) AS 담당고객수
FROM buser b
INNER JOIN jikwon j ON j.busernum = b.buserno
LEFT OUTER JOIN gogek g ON j.jikwonno = g.gogekdamsano
GROUP BY b.busername,j.jikwonno, j.jikwonname,j.jikwonjik
ORDER BY 담당고객수 DESC;

-- union : 구조가 일치하는 두 개 이상의 테이블 자료 합쳐보기
CREATE TABLE sangpum1(bun INT PRIMARY KEY,pummok VARCHAR(20) NOT NULL);
INSERT INTO sangpum1 VALUES(1,'귤');
INSERT INTO sangpum1 VALUES(2,'사과');
INSERT INTO sangpum1 VALUES(3,'배');
SELECT * FROM sangpum1;

CREATE TABLE sangpum2(num INT PRIMARY KEY,sangpum VARCHAR(20) NOT NULL);
INSERT INTO sangpum2 VALUES(10,'토마토');
INSERT INTO sangpum2 VALUES(20,'오이');
INSERT INTO sangpum2 VALUES(30,'피망');
INSERT INTO sangpum2 VALUES(40,'수박');
SELECT * FROM sangpum2;

SELECT bun AS 번호,pummok AS 상품명 FROM sangpum1
UNION
SELECT num AS 번호,sangpum AS 상품평 FROM sangpum2;

-- 참고: merge는 MariaDB X, Oracle O

-- subquery: SQL문 안에 포함된 또 다른 select 문의 사용
-- 일반적으로 안쪽 select문을 실행해서 그 결과를 구한 후 바깥쪽 SQL문에서 사용하는 방식

-- 사번 10번 박치기 직원과 직급이 같은 모든 직원 출력

SELECT jikwonjik FROM jikwon WHERE jikwonno=10;
SELECT * FROM jikwon WHERE jikwonjik='사원'; -- 결과를 위해 두 번의 SQL문 사용
-- subquery 사용
SELECT * FROM jikwon WHERE jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonno=10);

-- 직급이 대리 중 가장 먼저 입사한 직원은?
SELECT min(jikwonibsail) FROM jikwon WHERE jikwonjik='대리';
SELECT * FROM jikwon WHERE jikwonibsail='2013-02-05';
-- subquery 사용
SELECT * FROM jikwon WHERE jikwonjik='대리'
AND jikwonibsail=(SELECT min(jikwonibsail) FROM jikwon WHERE jikwonjik='대리');

-- 인천에 근무하는 직원 출력
SELECT * FROM jikwon WHERE busernum=(SELECT buserno FROM buser WHERE buserloc='인천');

-- 인천 이외에 근무하는 직원 출력
SELECT * FROM jikwon WHERE busernum IN (SELECT buserno FROM buser WHERE not buserloc='인천');

-- 서울에 근무하는 직원 출력
SELECT * FROM jikwon WHERE busernum IN (SELECT buserno FROM buser WHERE buserloc='서울');

SELECT * FROM gogek;
-- 고객 중 차일호와 나이가 같은 고객 모두를 출력
SELECT * FROM gogek WHERE SUBSTR(gogekjumin, 1, 2)=
(SELECT SUBSTR(gogekjumin, 1, 2) FROM gogek WHERE gogekname='차일호');

-- 고객을 담당하고 있는 직원은?
SELECT * FROM jikwon WHERE jikwonno IN(SELECT gogekdamsano FROM gogek);

-- 이순신 직원이 속한 부서의 평균 연봉보다 많이 받는 직원 출력 
SELECT * FROM jikwon 
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon 
WHERE busernum = (SELECT busernum FROM jikwon WHERE jikwonname='이순신'));

-- 문1) 2010년 이후에 입사한 남자 중 급여를 가장 많이 받는 직원은?
SELECT * FROM jikwon
WHERE jikwonibsail >= '2010-01-01' 
AND jikwongen = '남' 
AND jikwonpay = (SELECT MAX(jikwonpay) FROM jikwon 
WHERE jikwonibsail >= '2010-01-01' AND jikwongen = '남');


-- 문2)  평균급여보다 급여를 많이 받는 직원은?
SELECT * FROM jikwon
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon);
 

-- 문3) '이미라' 직원의 입사 이후에 입사한 직원은?
SELECT * FROM jikwon
WHERE jikwonibsail >= (SELECT jikwonibsail FROM jikwon
WHERE jikwonname = '이미라');
 

-- 문4) 2010 ~ 2015년 사이에 입사한 총무부(10),영업부(20),전산부(30) 직원 중 급여가 가장 적은 사람은?
SELECT * FROM jikwon
WHERE jikwonibsail BETWEEN '2010-01-01' AND '2015-12-31'
AND busernum IN (10, 20, 30) AND jikwonjik IS NOT NULL
AND jikwonpay = (SELECT MIN(jikwonpay) WHERE jikwonibsail BETWEEN '2010-01-01' AND '2015-12-31'
AND busernum IN (10, 20, 30) AND jikwonjik IS NOT NULL)
ORDER BY jikwonpay ASC
LIMIT 1;


-- (직급이 NULL인 자료는 작업에서 제외)

 

-- 문5) 한송이, 이순신과 직급이 같은 사람은 누구인가?
SELECT * FROM jikwon
WHERE jikwonjik IN (SELECT jikwonjik FROM jikwon
WHERE jikwonname IN ('한송이', '이순신'));
 

-- 문6) 과장 중에서 최대급여, 최소급여를 받는 사람은?
SELECT * FROM jikwon
WHERE jikwonjik = '과장'
AND (jikwonpay = (SELECT MAX(jikwonpay) FROM jikwon WHERE jikwonjik = '과장')
OR jikwonpay = (SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik = '과장'));
 

-- 문7) 30번 부서의 평균급여보다 급여가 많은 '대리' 는 몇명인가?
SELECT COUNT(*) AS 인원수 FROM jikwon
WHERE jikwonjik = '대리' AND jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum = 30);
 

-- 문8) 고객을 확보하고 있는 직원들의 이름, 직급, 부서명을 입사일 별로 출력하라.
SELECT j.jikwonname AS 직원명, j.jikwonjik AS 직급, IFNULL((SELECT b.busername FROM buser b WHERE b.buserno = j.busernum), '무소속') AS 부서명, jikwonibsail AS 입사일
FROM jikwon j
WHERE j.jikwonno IN(SELECT distinct(gogekdamsano) FROM gogek) ORDER BY j.jikwonibsail ASC;


 

-- 문9) 이순신과 같은 부서에 근무하는 직원과 해당 직원이 관리하는 고객 출력

-- (고객은 나이가 30 이하면 '청년', 50 이하면 '중년', 그 외는 '노년'으로 표시하고, 고객 연장자 부터 출력)

-- 출력 ==>  직원명    부서명     부서전화     직급      고객명    고객전화    고객구분
-- 
--           한송이    총무부     123-1111    사원      백송이    333-3333    청년   
SELECT j.jikwonname AS 직원명, b.busername AS 부서명,b.busertel AS 부서전화, j.jikwonjik AS 직급, g.gogekname AS 고객명, g.gogektel AS 고객전화, g.gogekjumin AS 주민번호,
CASE
WHEN  DATE_FORMAT(NOW(),'%Y') - (SUBSTR(g.gogekjumin, 1, 2) + 1900) <= 30 THEN '청년'
WHEN  DATE_FORMAT(NOW(),'%Y') - (SUBSTR(g.gogekjumin, 1, 2) + 1900) <= 50 THEN '중년'
ELSE '노년'
END AS 고객구분
FROM jikwon j
inner JOIN buser b ON j.busernum=b.buserno
inner JOIN gogek g ON j.jikwonno=g.gogekdamsano
WHERE j.busernum = (SELECT busernum FROM jikwon WHERE jikwonname='이순신') ORDER BY gogekjumin;
 

-- 문10) JIKWON, BUSER, GOGEK 테이블을 이용하여 담당 고객 수가 가장 많은 직원을 출력하시오.
-- 동일한 고객 수를 가진 직원이 여러 명이면 모두 출력한다.
-- 출력 ==>   부서명   직원명   직급   담당고객수

 

-- 힌트 :  GROUP BY ~ HAVING 사용
-- 직원별 고객 수 계산 --> 그중 가장 큰 고객 수 계산 --> 그 고객 수를 가진 직원 찾기


SELECT b.busername AS 부서명, j.jikwonname AS 직원명, j.jikwonjik AS 직급, COUNT(*) AS 담당고객수
FROM jikwon j
inner JOIN buser b ON j.busernum=b.buserno
LEFT OUTER JOIN gogek g ON j.jikwonno = g.gogekdamsano
GROUP BY j.jikwonno
HAVING COUNT(*) = (
	SELECT MAX(cnt)
	FROM (
		SELECT COUNT(*) AS cnt
		FROM jikwon j2
		LEFT OUTER JOIN gogek g2 ON j2.jikwonno = g2.gogekdamsano
		GROUP BY j2.jikwonno
	) AS gogek_count
);

-- AS gogke_count 는FROM 절의 서브쿼리 결과를 하나의 테이블처럼 사용하기 위해 붙인 가상 이름

-- 총무부에 근무하는 직원들이 관리하는 고객 출력하기
-- subquery 사용
SELECT gogekno,gogekname,gogektel FROM gogek
WHERE gogekdamsano IN (SELECT jikwonno FROM jikwon
WHERE busernum = (SELECT buserno FROM buser WHERE busername='총무주'));
-- 필요한 값을 단계적으로 찾는다. 총무부번호는? -> 직원번호는 -> 고객은?

-- join 사용
SELECT gogekno,gogekname,gogektel FROM gogek
INNER JOIN jikwon ON jikwonno=gogekdamno
INNER JOIN buser ON busernum=buserno
WHERE busername='총무부';
-- 관련 테이블을 연결한 뒤 조건으로 조회함. 여러 테이블의 칼럼을 함꼐 출력할 때 효과적 


-- subquery에서 any, all 연산자 : null 인 자료는 제외하고 작업함.
-- <any : subquery의 반환값 중 최대값보다 작은 ~  <=
-- >any : subquery의 반환값 중 최소값보다 큰 ~    >=
-- <all : subquery의 반환값 중 최소값보다 작은 ~  <=
-- >all : subquery의 반환값 중 최대값보다 큰 ~    >=

-- 직급 중 대리의 최대값보다 작은 연봉을 받는 직원은?
SELECT jikwonno,jikwonname,jikwonpay FROM jikwon
WHERE jikwonpay < ANY (SELECT jikwonpay FROM jikwon WHERE jikwonjik='대리');

-- 30번 부서의 최고 연봉자보다 연봉을 많이 받는 직원은?
SELECT jikwonno,jikwonname,jikwonpay FROM jikwon
WHERE jikwonpay < ALL (SELECT jikwonpay FROM jikwon WHERE busernum=30);

-- from 절에 사용하는 subquery
-- 전체 평균 연봉과 최대 연봉 사이의 연봉을 받는 직원은?
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon a, (SELECT AVG(jikwonpay) avgs, MAX(jikwonpay) maxs FROM jikwon) b
WHERE a.jikwonpay BETWEEN b.avgs AND b.maxs;

-- 각 부서별로 최고 연봉을 받는 직원 출력
SELECT a.jikwonno,a.jikwonname,a.jikwonpay,a.busernum FROM jikwon a,
(SELECT busernum, max(jikwonpay) maxpay FROM jikwon GROUP BY busernum) b
WHERE a.busernum = b.busernum AND a.jikwonpay = b.maxpay;
-- 같은 부서이면서 그 부서의 최고 연봉과 같은 직원을 찾음

-- GROUP BY의 HAVING 절에 포함된 subquery
-- 부서별 평균 연봉 중 30번 부서의 평균 연봉 보다 큰 부서 자료 출력
SELECT busernum, AVG(jikwonpay) FROM jikwon
GROUP BY busernum
HAVING AVG(jikwonpay) > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum=30);

-- exists 연산자 사용
-- 직원이 있는 부서 출력
SELECT busername,buserloc FROM buser bu
WHERE EXISTS (SELECT 'imsi' FROM jikwon WHERE busernum=bu,buserno); -- EXISTS : ture or false 반환

-- 상관 서브쿼리 : outer(main) query의 값을 inner query에서 참조하여 수행하는 서브쿼리
-- 상관 서브쿼리는 서브쿼리가 독립적으로 실행되지 않고, 바깥쿼리의 현재 행 값을 받아서 실행됨.
-- 연습1) 각 직원이 자기 부서의 평균 급여보다 많이 받는지 조회
SELECT a.jikwonno,a.jikwonname,a.jikwonpay,busernum FROM jikwon a
WHERE a.jikwonpay > (SELECT AVG(b.jikwonpay) FROM jikwon b WHERE b.busernum=a.busernum)
ORDER BY a.busernum ASC;

-- 연습2) 각 부서의 최고 연봉자는?
SELECT * FROM jikwon a WHERE a.jikwonpay =
(SELECT MAX(b.jikwonpay) FROM jikwon b WHERE a.busernum=b.busernum);

-- 연습3) 연봉 순위 3위 이내의 직원 출력(내림 차순)
SELECT a.jikwonno,a.jikwonname,a.jikwonpay FROM jikwon a
WHERE 3 > (SELECT COUNT(*) FROM jikwon b WHERE b.jikwonpay > a.jikwonpay)
AND a.jikwonpay IS NOT NULL ORDER BY a.jikwonpay DESC;

-- subquery를 이용한 table 생성 및 insert 수행
CREATE TABLE jik1 AS SELECT * FROM jikwon;  -- jikwon과 동일한 테이블이 생성됨 - pk는 적용은 안됨
DESC jikwon;
DESC jik1;
SELECT * FROM jik1;

CREATE TABLE jik2 AS SELECT * FROM jikwon WHERE 1=0; -- 구조만 가진 테이블 생성
SELECT * FROM jik2;
INSERT INTO jik2 SELECT * FROM jikwon WHERE jikwonjik = '과장';  -- query로 insert
INSERT INTO jik2(jikwonno,jikwonname,busernum) SELECT jikwonno,jikwonname,busernum FROM jikwon
WHERE jikwonjik='대리';  -- jikwonjik의 default가 사원이라서 대리가 사원으로 입력됨

SELECT * FROM jik2;

-- 일부 칼럼만 가진 테이블 생성
CREATE TABLE jik3 SELECT jikwonno AS bunho,jikwonname AS irum, jikwonpay AS pay FROM jikwon WHERE 1=0;
DESC jik3;
SELECT * FROM jik3;

-- update, delete 에서 subquery 사용
-- update : 총무부 직원의 급여를 10% 인상
SELECT * FROM jik1;
UPDATE jik1 SET jikwonpay = jikwonpay * 1.1 
WHERE busernum = (SELECT buserno FROM buser WHERE busername='총무부');
SELECT * FROM jik1;

-- delete: 고객이 있는 직원을 삭제
DELETE FROM jik1 WHERE jikwonno IN(SELECT DISTINCT gogekdamsano FROM gogek);
SELECT * FROM jik1;

-- 트랜잭션(Transaction)은 여러 SQL 작업을 하나의 작업 단위로 묶어 처리하는 것. 
-- 단위별 데이처 처리를 의미한다.
-- 예를 들어 '계좌이체'처럼
-- - A 계좌 출금
-- - B 계좌 입금
-- 두 작업이 모두 성공해야 하나의 정상 처리된다. 중간에 실패라면 원래의 작업으로 복귀.
-- 트랜잭션은 여러 SQL 문을 하나의 논리적인 작업 단위로 처리하며, 
-- 모두 성공하면 COMMIT, 문제가 생기면 ROLLBACK 한다.
-- INSERT, UPDATE, DELETE 같은 DML 문이 실행되면 트랜잭션이 시작되며, 
-- 명시적 트랜잭션에서는 COMMIT 또는 ROLLBACK을 만나면 종료된다.

-- MaiaDB는 묵시적으로 INSERT, UPDATE, DELETE 하면 자동 commit 된다. 
-- 즉, client의 자료를 근거로 db-server의 자료를 갱신한다.
-- 현재 설정 확인:  SELECT @@autocommit;   결과가 1이면 자동 커밋 상태임

CREATE TABLE jiktab AS SELECT * FROM jikwon;
SELECT * FROM jiktab;

SELECT @@autocommit;

-- 연습 1
SET autocommit = FALSE;
SELECT @@autocommit;
SELECT * FROM jiktab;
delete FROM jiktab WHERE jikwonno >= 6; -- 트렌젝션 시작 (local 자료만 삭제됨. 이 정보를 log로 기억)
SELECT * FROM jiktab;  -- 현재는 local 자료만 보임
ROLLBACK;  -- 트랜젝션 종료
SELECT * FROM jiktab;

-- 연습 2
SET autocommit = FALSE;
DELETE FROM jiktab WHERE jikwonno=2;
COMMIT;
SELECT * FROM jiktab;
DELETE FROM jiktab WHERE jikwonno=3;
ROLLBACK;
SELECT * FROM jiktab;
SET autocommit = TRUE;

-- 연습 3
SET autocommit = FALSE;  -- 수동
UPDATE jiktab SET jikwonpay = 8888 WHERE jikwonno=4;
SELECT * FROM jiktab WHERE jikwonno=4;
SAVEPOINT aa;  -- 저장 지점 선언 
UPDATE jiktab SET jikwonpay=7777 WHERE jikwonno=5;
ROLLBACK TO SAVEPOINT aa;
SELECT * FROM jikwon WHERE jikwonno IN(4, 5);
-- local에서 현재 상태: 5번 수정 취소, 4번은 수정상태
ROLLBACK; -- local 수정 모두 취소
SELECT * FROM jikwon WHERE jikwonno IN(4, 5);
UPDATE jiktab SET jikwonpay=7777 WHERE jikwonno=6;
COMMIT;
SELECT * FROM jiktab WHERE jikwonno IN(4, 5, 6);
SET autocommit = TRUE;  -- 자동

-- Deadlock (교착상태):
-- 두개 이상의 트랜잭션이 서로 상대방이 가진 자원의 잠금이 풀리기를 기다리면서 계속 진행하지 못하는 상태
-- 해결책은 충돌한 트랜잭션 하나를 commit 또는 rollback 하는 것이다.
-- 시간과 자원을 낭비함으로 주의 필요. 트랜잭션 완료 확인 필요.
SET autocommit = FALSE;
SELECT * FROM jiktab WHERE jikwonno=4;
UPDATE jiktab SET jikwonjik='주임' WHERE jikwonno=4;
SELECT * FROM jiktab WHERE jikwonno=4;
COMMIT;

-- view 파일(객체):
-- 실제 데이터를 별도로 저장하는 파일이 아니라,
-- SELECT 문을 저장하여 테이클처럼 사용할 수 있게 만든 데이터베이스 객체이다.
-- 실제 데이터를 별도로 복사해 저장하는 일반 테이블은 아님
-- 원본 테이블의 데이터를 기준으로 조회 결과를 보여줌
-- 복잡한 SELECT 문을 단순하게 재사용할 수 있음
-- 필요한 컬럼만 보여줘 보안에도 활용 가능

-- view 기본 형식 : create view 뷰이름 AS SELECT 컬럼명1, 컬럼명2, ... FROM 테이블명 WHERE 조건;
-- 조회 형식: SELECT * FROM 뷰이름;
-- 삭제 형식: DROP VIEW 뷰이름;

CREATE or REPLACE VIEW v_a AS
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

SHOW tables;
select * from v_a;
DESC v_a;
SELECT SUM(jikwonpay) FROM v_a;

CREATE VIEW v_b AS
SELECT * FROM jikwon WHERE jikwonname LIKE '김%' OR jikwonname LIKE '박%';
SELECT * FROM v_b;

ALTER TABLE jikwon RENAME kbs;
SELECT * FROM jikwon; -- err
SELECT * FROM v_a;  -- err
SELECT * FROM v_b;  -- err
ALTER TABLE kbs RENAME jikwon;
SELECT * FROM v_b;
SELECT * FROM v_a;

CREATE VIEW v_c AS SELECT * FROM jikwon ORDER BY jikwonpay DESC;
SELECT * FROM v_c;

CREATE VIEW v_d AS SELECT jikwonname, jikwonpay * 10000 AS ypay FROM jikwon;
SELECT * FROM v_d;

CREATE VIEW v_e AS SELECT * FROM v_d WHERE ypay >= 50000000;
SELECT * FROM v_e;
RENAME TABLE v_e TO mbc;  -- view 객체 이름 변경
SELECT * FROM mbc;

CREATE VIEW v_f AS SELECT * FROM jikwon WHERE jikwonpay >= 5000;
SELECT * FROM v_f;
UPDATE v_f SET jikwonname='사오정' WHERE jikwonname='홍길동';
SELECT * FROM v_f;
UPDATE v_f SET jikwonname='저팔계' WHERE jikwonno=30;  -- view에 존재하지 않으므로 원본 갱신 없음 
SELECT * FROM v_f;
SELECT * FROM jikwon;
DELETE FROM v_f WHERE jikwonno=27;
SELECT * FROM v_f;
DELETE FROM v_f WHERE jikwonno=30;
SELECT * FROM jikwon;

CREATE VIEW v_g AS SELECT jikwonno,jikwonname,busernum,jikwonpay FROM jikwon;
SELECT * FROM v_g;
INSERT INTO v_g VALUES(31, '손오공',10,7000); -- view를 이용해 원본 테이블에 자료를 저장 
SELECT * FROM v_g;
SELECT * FROM jikwon;

CREATE VIEW v_h AS
SELECT jikwonjik,SUM(jikwonpay) AS hap, AVG(jikwonpay) AS ave FROM jikwon
GROUP BY jikwonjik;  -- GROUP BY도 VIEW 작성 가능
SELECT * FROM v_h;

-- join도 가능

-- 문1) 사번   이름    부서  직급  근무년수  고객확보

--        1   홍길동  영업부 사원     6           O   or  X

-- 조건 : 직급이 없으면 임시직, 전산부 자료는 제외

-- 위의 결과를 위한 뷰파일 v_exam1을 작성

CREATE VIEW v_exam1 AS SELECT jikwonno AS '사번',
jikwonname AS '이름',busername AS '부서',
jikwonjik AS '직급',YEAR(CURDATE()) -YEAR(jikwonibsail) AS '근무년수',
case WHEN EXISTS(SELECT * FROM gogek WHERE gogekdamsano = jikwonno) THEN 'O' ELSE 'X' END AS 고객확보여부
FROM jikwon LEFT JOIN buser ON busernum = buserno
WHERE busername <> '전산부' OR busername IS NULL;
SELECT * FROM v_exam1;

CREATE view v_exam1 AS SELECT j.jikwonno AS 사번, j.jikwonname AS 이름, b.busername AS 부서, NVL(j.jikwonjik, '임시직') AS 직급,
TIMESTAMPDIFF(YEAR, j.jikwonibsail, CURDATE()) AS 근무년수,
CASE
WHEN j.jikwonno IN (SELECT DISTINCT gogekdamsano FROM gogek)
THEN 'O' ELSE 'X' END AS 고객확보
FROM jikwon j
LEFT OUTER JOIN buser b ON j.busernum = b.buserno WHERE b.busername <> '전산부' OR b.busername IS NULL;

SELECT * FROM v_exam1;
DROP VIEW v_exam1;

-- 문2) 부서명   인원수

--        영업부     7

-- 조건 : 직원수가 가장 많은 부서 출력

-- 위의 결과를 위한 뷰파일 v_exam2을 작성

CREATE VIEW v_exam2 AS SELECT busername AS '부서명', COUNT(*) AS '인원수' FROM buser
INNER JOIN jikwon ON buserno = busernum GROUP BY buserno, busername
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM jikwon INNER JOIN buser ON busernum = buserno
GROUP BY buserno);
SELECT * FROM v_exam2;

CREATE VIEW v_exam2 AS SELECT b.busername AS 부서명, COUNT(*) AS 인원수
FROM jikwon j
INNER JOIN buser b ON j.busernum = b.buserno
GROUP BY b.busername 
HAVING COUNT(*) = (SELECT COUNT(*) FROM jikwon GROUP BY busernum ORDER BY;

SELECT * FROM v_exam2 LIMIT 1;

DROP VIEW v_exam2;

-- 문3) 가장 많은 직원이 입사한 요일에 입사한 직원 출력

--     직원명   요일     부서명   부서전화

--     한국인  수요일   전산부   222-2222

-- 위의 결과를 위한 뷰파일 v_exam3을 작성  

CREATE VIEW v_exam3 AS SELECT j.jikwonname AS 직원명, 
case
DATE_FORMAT(j.jikwonibsail, '%W') 
when 'Monday' 		THEN '월요일'
WHEN 'Tuesday' 	THEN '화요일'
WHEN 'Wednsday' 	THEN '수요일'
WHEN 'Thursday' 	THEN '목요일'
WHEN 'Friday' 		THEN '금요일'
WHEN 'Saturday' 	THEN '토요일'
WHEN 'sunday' 		THEN '일요일'
end AS 요일,
b.busername AS 부서명, b.busertel AS 부서전화
FROM jikwon j
INNER JOIN buser b ON j.busernum = b.buserno 
WHERE DATE_FORMAT(j.jikwonibsail, '%W') = (SELECT DATE_FORMAT(jikwonibsail, '%W')
FROM jikwon
GROUP BY DATE_FORMAT(jikwonibsail, '%W') ORDER BY COUNT(*) DESC
LIMIT 1);

SELECT * FROM v_exam3;
DROP VIEW v_exam3;

CREATE OR REPLACE VIEW v_exam3 AS SELECT j.jikwonname AS 직원명, 
DATE_FORMAT(j.jikwonibsail, '%W') 요일,
b.busername AS 부서명, b.busertel AS 부서전화
FROM jikwon j
LEFT JOIN buser b ON j.busernum = b.buserno 
WHERE DATE_FORMAT(j.jikwonibsail, '%W') = (SELECT DATE_FORMAT(jikwonibsail, '%W')
FROM jikwon
GROUP BY DATE_FORMAT(jikwonibsail, '%W') ORDER BY COUNT(*) DESC
LIMIT 1);

SELECT * FROM v_exam3;
DROP VIEW v_exam3;

-- 저장 프로시저(Stored procedure)
-- : 자주 사용하는 SQL 작업을 DB 안데 이름을 붙여 저장해 두고, 필요할 때 실행하는 기능
-- : SQL + Programming - 절차적 프로그래밍이 가능

-- 기본 형태 확인
-- 실습 1
delimiter $$
CREATE or REPLACE PROCEDURE sp_1()
BEGIN
   SELECT '안녕 프로시저 세상방문을 환영합니다' AS 제목;
END $$
delimiter ;

CALL sp_1();  -- procedure 호출
SHOW PROCEDURE STATUS; -- procedure 목록 확인
SHOW CREATE PROCEDURE sp_1; -- 해당 procedure 정보 확인
DROP PROCEDURE sp_1;

-- 실습 2
delimiter $$
CREATE OR REPLACE PROCEDURE sp_2(IN a INT, IN b INT)
BEGIN
   DECLARE x, y INT DEFAULT 0; -- 변수 선언. 대소문자 구분 없음
   SET x = 10; -- 변수에 값 대임
   SELECT X, Y; -- 변수 값 출력
   SELECT a + b AS result;
END $$
delimiter ;

CALL sp_2(2, 3);

-- 실습 3: table 사용
delimiter $$
CREATE OR REPLACE PROCEDURE sp_3(IN para1 INT, IN para2 INT)
BEGIN
   SELECT * FROM jikwon WHERE jikwonno < 3;
   SELECT * FROM buser;
   SELECT * FROM gogek WHERE gogekno=para1;
   SELECT * FROM gogek WHERE gogekno=para2;
END $$
deimiter;
   
   
-- 실습 4: if 사용
delimiter $$
CREATE OR REPLACE PROCEDURE sp_4(IN jik VARCHAR(20), IN num INT)
BEGIN
   SELECT jik;
   SELECT * FROM jikwon WHERE jikwonjik=jik;
   if(num = 10) THEN
     SELECT * FROM jikwon WHERE busernum=num;
   elseif(num = 20) then
     SELECT * FROM jikwon WHERE busernum=num;
   else
     SELECT * FROM jikwon WHERE busernum NOT IN(10, 20);
   END if;
END $$
delimiter ;
CALL sp_4('대리', 20);


-- 실습 5: if 사용 - 고객번호 입력하면 고객정보 조회
-- 담당 직원번호를 입력하면 해당 직원이 관리하는 고객 출력 
-- 둘 다 입력 안하면 모든 고객 출력
delimiter $$
CREATE OR REPLACE PROCEDURE sp_5(IN p_gogekno INT, IN p_damsano INT)
BEGIN
   -- 특정 고객 조회
   if p_gogekno IS NOT NULL then 
      SELECT * FROM gogek WHERE gogekno=p_gogekno;
   -- 해당 직원이 관리하는 고객 출력
   ELSEIF p_damsano IS NOT NULL then
      SELECT * FROM gogek WHERE gogekdamsano=p_damsano;
   -- 모든 고객 출력
   else
      SELECT * FROM gogek
   END if;
END $$
delimiter ;

CALL sp_5(5, NULL); -- 고객번호 5번 조회
CALL sp_5(NULL, 3); -- 담당직원번호 3번이 관리하는 고객조회 
CALL sp_5(NULL, NULL);

-- 실습 6: while 사용
delimiter $$
CREATE or REPLACE PROCEDURE sp_6()
BEGIN
   DECLARE x INT;
   DECLARE str VARCHAR(255);
   SET X =1;
   SET str = '';
   
   while n <= 5 do
      SET str = CONCAT(str, n, ',');
      SET n = n + 1;
   END while;
   
   SELECT str;
END $$
delimiter ;
CALL sp_6();

-- 실습 7: while 사용
-- 입력한 시작번호, 끝번호까지 고객 재료 출력
delimiter $$
CREATE or REPLACE PROCEDURE sp_7(IN start_no INT, IN end_no INT)
BEGIN
   DECLARE current_no INT;
   SET current_no = start_no;
   
   while current_no <= end_no do
      SELECT * FROM gogek WHERE gogekno=current_no;
      SET current_no = current_no + 1;
   END while;
END $$
delimiter ;

CALL sp_7(3, 6);

-- 실습 8 : while 사용
-- jikwon 테이블을 이용해 입력한 직급의 직원수와 직원 목록 출력
delimiter $$
CREATE or REPLACE PROCEDURE sp_8(IN start_no INT, IN end_no INT)
BEGIN
   DECLARE cnt INT DEFAULT 0;
   
   -- 해당 직급의 직원수 저장
   SELECT COUNT(*) INTO cnt FROM jikwon WHERE jikwonjik=p_jik;
   SELECT p_jik AS 직급, cnt AS 인원수;
   -- 직원 수 만큼 반복
   while i < cnt do
      SELECT jikwonno,jikwonname,jikwonjik,jikwonpay FROM jikwon
      WHERE jikwonjik=p_jik ORDER BY jikwonno LIMIT i, 1;
      
      SET i = i + 1;
   END while;
END $$
delimiter ;

CALL sp_8('대리');

SELECT round(jikwonpay * 0.05) FROM jikwon; -- 전문가가 작성한 내장함수 
-- 사용자 정의 함수
-- bmi 지수 = 신장(cm단위) * 신장(cm단위) * 22 / 10000
delimiter $$
CREATE or REPLACE FUNCTION fu_1 (height INT, weight INT) RETURNS DOUBLE
BEGIN
   RETURN weight * 10000 / (height * height);
END $$
delimiter ;

SELECT fu_1(175, 65);

-- 사용자 정의 함수2: 전체 직원의 연봉 평균 반환
delimiter $$
CREATE or REPLACE FUNCTION fu_2 () RETURNS DOUBLE
BEGIN
   DECLARE r DOUBLE;
   SELECT AVG(jikwonpay) INTO r FROM jikwon;
END $$
delimiter ;

SELECT fu_2();
SELECT AVG(jikwonpay) FROM jikwon;

-- 사용자 정의 함수 3: 전체 직원의 연봉의 10% 반환값
delimiter $$
CREATE or REPLACE FUNCTION fu_3 (bun INT) RETURNS DOUBLE
BEGIN
   DECLARE pay INT;
   SET pay = 0;
   SELECT jikwonpay * 0.1 INTO pay FROM jikwon WHERE jikwonno=bun;
   RETURN pay;
END $$
delimiter ;

SELECT fu_3(1);
SELECT jikwonno,jikwonname,jikwonjik,fu_3(jikwonno) AS donate,jikwongen from jikwon;

-- 사용자 정의 함수4: 부서번호를 부서명
delimiter $$
CREATE or REPLACE FUNCTION fu_4(bun INT) RETURNS VARCHAR(10)
BEGIN
   DECLARE bname VARCHAR(10);
   SELECT busername INTO bname FROM buser WHERE buserno=bun;
   RETURN bname;
END $$
delimiter ;

select jikwonno,jikwonname,busernum,fu_4(busernum) FROM jikwon;

-- 문항 7

DELETE FROM buser
WHERE buserno IN ( SELECT busernum FROM jikwon GROUP BY busernum
HAVING COUNT(*) <= 2);

-- 문항 10
SELECT jikwonno,jikwonname,busername,jikwonjik FROM jikwon
INNER JOIN buser ON busernum=buserno
WHERE jikwonjik='과장';

-- 문항 11
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay >= 5000 AND jikwonpay <= 7000;

SELECT jikwonno, jikwonname, jikwonpay FROM jikwon
WHERE jikwonpay BETWEEN 5000 AND 7000;

-- 문항 12
 -- jikwon 테이블을 사용하여 평균 연봉보다 연봉이 높은 직원들을 모두 출력하는 뷰 파일을 작성하시오.

-- 조건1 : 실행은 SELECT * FROM v_jikwon_highpay;
-- 조건 2 : sub query를 사용하고 칼럼은 모두 출력.
CREATE OR REPLACE VIEW v_jikwon_highway AS SELECT * FROM jikwon
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon);
SELECT * FROM v_jikwon_highway;

-- 문항 14
-- 2015 ~ 2020 년 사이에 입사한 직원을 대상으로 년도별 인원수와 연봉평균을 출력하는 DML문을 기술하시오.
SELECT 
    YEAR(jikwonibsail) AS 입사년도,
    COUNT(*) AS 인원수,
    AVG(jikwonpay) AS 연봉평균
FROM jikwon
WHERE YEAR(jikwonibsail) BETWEEN 2015 AND 2020
GROUP BY YEAR(jikwonibsail)
ORDER BY 입사년도 ASC;

-- 문항 15
SELECT jikwonname AS 직원명, jikwonpay AS 급여, COUNT(gogekdamsano) AS 고객수
FROM jikwon 
LEFT OUTER JOIN gogek ON gogekdamsano = jikwonno
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon)
GROUP BY jikwonno, jikwonname, jikwonpay
ORDER BY 급여 DESC;
