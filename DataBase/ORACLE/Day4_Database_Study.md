# Day4

```sql
-- ANSI JOIN vs ORACLE JOIN 구문
--[ANSI JOIN]
(1)
SELECT
FROM 테이블1 JOIN 테이블2 USING (조인에사용할 컬럼명)
WHERE 행에 대한 조건
-- 등가 조인 할 것이면 USING 절을 사용한다.
(2)
SELECT
FROM 테이블1 JOIN 테이블2 ON (조인 조건식)
WHERE 행에 대한 조건
----------------------------------------
↓↓↓↓↓↓↓↓↓↓OUTER JON↓↓↓↓↓↓↓↓↓↓↓
(3)
SELECT
FROM 테이블1 LEFT JOIN 테이블2 USING (조인에사용할 컬럼명) 또는 ON (조인 조건식)
WHERE 행에 대한 조건
-- LEFT를 붙임으로써 왼쪽 TABLE이 기준이라는 것을 나타냄
(4)
SELECT
FROM 테이블1 RIGHT JOIN 테이블2 USING (조인에사용할 컬럼명) 또는 ON (조인 조건식)
WHERE 행에 대한 조건
-- RIGHT를 붙임으로써 오른쪽 TABLE이 기준이라는 것을 나타냄
(5)
SELECT
FROM 테이블1 FULL JOIN 테이블2 USING (조인에사용할 컬럼명) 또는 ON (조인 조건식)
WHERE 행에 대한 조건
-- FULL JOIN 가능
```

![image-20191230145418768](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191230145418768.png)

```sql
SELECT 컬럼리스트|*
FROM 테이블명
WHERE 컬럼 = 정해진값|이미알고있는값

SELECT 컬럼리스트|*
FROM 테이블명
WHERE 컬럼 = (select 명령)

SELECT *
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'ADAMS' OR ENAME = 'JONES'); -- ERROR
		   --2개 이상의 나올수 있는 서브쿼리를 다중행 서브쿼리 라고 한다.
SELECT *
FROM EMP
WHERE SAL > ALL (1200,2975); -- 2개의 값보다 커야돼

      >ALL, >ANY, <ALL, <ANY, IN(NOT IN) -- 다중행 연산자
      
      컬럼 < ANY (10, 5, 7, 6)
      컬럼 < ALL (10, 5, 7, 6)
```

**추출 하려는 행이 하나의 절로만 가능하면 JOIN 보다는 서브쿼리를 사용한다. 반대라면 JOIN을 사용하는것이 좋다.**