# Oracle Day1

**[Study List]**

**Java 구문 - SQL - JDBC - HTML5 - CSS3 - JavaScript(jQuery) - Ajax - Servlet - JSP - Spring - Mybatis - D3.js(웹 기반 시각화) - 1day 게시판 프로젝 - 미니프로젝트**

**리눅스(CentOs7) - Hadoop 2.x.x(설치, 설정, HDFS, MapReduce) - Hive - Spark - R(구문, 데이터 수집(웹크롤링, 공공DB, SNS Open API), 통계분석, 데이터마이닝, 텍스트마이닝, 시각화), Java와 R연동**

**팀프로젝트 : 빅데이터를 가지고 분석하여 웹으로 서비스하는 모델 (e.g 1인가구가 살기 좋은 곳, 신문기사 복붙 한것 하나만 찾아서 List하기)**

----

## Oracle 설치

관리자계정(system) 암호: manager

https://coding-factory.tistory.com/28    -> 설치및 계정 생성 관련 블로그

-----------

DQL --> DML --> DDL

CRUD(Create Read Update Delete)

- Create : INSERT 명령어
- READ : SELECT 명령어(DQL)
- Update : UPDATE 명령어
- Delete : DELETE 명령어

-------

## 서버와 클라이언트

- 서버는 컴퓨터 On/Off시 Open/Close 된다.

1. cmd 창에 나가서 sqlplus 라는 명령을 수행시킨다.

   ->>> cmd 창에서 sqlplus -> username: system, password : manager -> select user from dual;(세미콜론 필수!) -> USER -------- SYSTEM이라고 뜸!!! -> 

   C:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin 의 path를 입력-> 

   [scott 계정 생성]

   -> @C:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin\scott.sql

   -> alter user scott identified by tiger;

   -> select user from dual; // scott 이라고 출력될 거임, 주석 --임

   -> select * from tab;			// scott 계정이 보유하고 있는 테이블 리스트

   -> connect system/manager

   [hr 계정 락(lock) 풀기]

   -> alter user hr account unlock;

   -> alter user hr identified by hr;

   -> connect hr/hr

   [jdbctest 계정 만들기 : JDBC 수업시간에 사용]

   -> create user jdbctest identified by jdbctest;

   -> grant connect, resource to jdbctest;

   ->quit 로 나감

   **create user 계정명 identified by 비밀번호; 이렇게 명령어를 입력하여 새로운 계정을 생성줍니다.**

   **grant connect, resource to 계정명; **

2. sqldeveloper라는 추가프로그램을 설치하여 사용. -> oraclec 사이트에서 다운 받을 수 있음

   jdk 설치 된곳 잘 찾아서! path 잘 선택하고 설치

   오라클 exe 가서 

학습용 일반계정 : scott(생성), hr(락 해제)

-----------

### SELECT 명령어

```sql
select 추출하려는 컬럼명리스트 또는 *
from 테이블이름
where 행의조건식 -- 이것을 만족하는 행들만 뽑아내서
			   -- select from where 가 있으면 먼저 1.from 2. where 3. select를 추출한다. 왜냐 먼저 테이블을 불러와야 데이터가 있으니까
[where 행의조건식]
[order by 컬럼명(별칭, 식) desc|asc]
-- 열을 추려내는것은 select 행을 추려내는 것은 where

---------------------------위에 from 까지는 필수로 작성해야한다.
select * from emp
↑
-----> 띄어 써도 같은것
↓
select *
from emp

select ename, sal from emp;
select sysdate from dual;
select user from dual;
select sysdate; --sysdate는 함수

select sysdate from emp; -- 라고 하면 form 절의 emp의 모든 행 만큼 출력 한다.
select 100+200 from dual; -- oracle이 가지고 있는 dummy 테이블은 dual
-- 한번만 처리 하고 싶을 때 dual을 사용하면 된다. 
-- dual은 1행 1열 -> 내용 : ('x')

select ename, sal
from emp
where sal > 2000
order by sal desc; -- desc는 descendent
                   -- 적은값에서 큰값으로 하고 싶으면 asc 아니면 생략
```

