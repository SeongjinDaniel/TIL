# Day3

```sql
-- 단일행 함수
select to_char(sysdate, 'yyy"년"')
from dual;

select to_char(sysdate, 'mm"월" dd"일" day')
from dual;
               
select to_char(sysdate, 'yyyy"년" mm"월" dd"일" hh"시" mi"분" ss"초"')
from dual;
               
sal * 12 + comm
sal + 12 + nvl(comm, 0)
               
select ename, sal, comm from emp;

-- 열의 type의 통일성이 없다. -> type을 잘 맞춰줘야한다
select ename, sal, nvl(to_char(comm), '없음') from emp;
select ename, sal, nvl(comm, 0) from emp;

decode(대상, 비교값1, 처리식1, 비교값2, 처리식2, .... 비교값n, 처리식n)
switch(대상식, 비교값1, 처리식1, 비교값2, 처리식2, .... 비교값n, 처리식n)
```

@c:/temp/scott_create_table.sql

```sql
-- 다중행 함수
SELECT MAX(SAL), MIN(SAL), SUM(SAL), AVG(SAL), COUNT(SAL) FROM EMP;
SELECT EMPNO, ENAME FROM EMP;
SELECT EMPNO, ENAME, SAL, COMM FROM EMP;
SELECT ENAME, MAX(SAL) FROM EMP; -- 허용 하지 않음 error

SELECT COUNT(COMM), COUNT(*) FROM EMP; -- 전자는 NULL 개수 미포함, 후자는 모두 포함

SELECT *
FROM EMP
WHERE SAL > (전체 월급의 평균을 구하는 SELECT 명령)

-- WHERE절에서는 GROUP함수를 사용할 수 없다.
SELECT *
FROM EMP
WHERE SAL > (SELECT AVG(SAL) FROM EMP)

-- WHERE절에는 행에대한 조건 HAVING 절에는 GROUP에 대한 조건
```

```sql
-- 추가
drop table course1 purge;
drop table course2 purge;

create table course1 (
name varchar(15),
phone varchar(20),
age number(3)
);

create table course2 (
name varchar(15),
phone varchar(20),
age number(3)
);

insert into course1 values('둘리', '010-111-1111', 10);
insert into course1 values('또치', '010-222-2222', 11);
insert into course1 values('도우너', '010-333-3333', 12);
insert into course1 values('희동이', '010-444-4444', 6);

insert into course2 values('둘리', '010-111-1111', 10);
insert into course2 values('또치', '010-222-2222', 11);
insert into course2 values('토토로', '010-555-5555', 13);
insert into course2 values('짱구', '010-666-6666', 7);
insert into course2 values('듀크', '010-777-7777', 11);

commit;
```





