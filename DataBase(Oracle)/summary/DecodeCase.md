# Decode & Case

☘️표시는 안했지만 scott 계정에서 EMP데이터를 가져오는 것이 아니라면 반드시 ***FROM DUAL*** 써줘야 합니다! 



Switch Case랑 비슷하다



#### * DECODE 

기준이 되는 데이터를 먼저 지정한 후 해당 데이터 값에 따라 다른 결과값을 내보내는 함수

~~~sql
DECODE(검사 대상이 될 열 도는 데이터, 연산이나 함수의 결과,
      조건1, 데이터가 조건1과 일치할 때 반환할 결과,
      조건2, 데이터가 조건2와 일치할 때 반환할 결과
      - - -,
      위 조건과 일치한 경우가 없을때 반환할 결과)
      
      
SELECT EMPNO, ENAME, JOB, SAL,
					DECODE(JOB,
             'MANAGER', SAL*1.1,
             'SALESMAN', SAL*1.05,
             'ANALYST', SAL,
             SAL*1.03)
FROM EMP
~~~



#### *CASE

CASE문은 각 조건에 사용하는 데이터가 서로 상관없어도 된다.

또 기준 데이터 값이 같은 데이터 외에 다양한 조건을 사용할 수 있다.

~~~SQL
CASE [검사 대상이 될 열 또는 데이터, 연산이나 함수의 결과]
	WHEN 조건 1 THEN 조건 1의 결과 값이 true일 때, 반환할 결과
	WHEN 조건 2 THEN 조건 2의 결과 값이 true일 때, 반환할 결과
	- - - - - - - - - 
	ELSE 위 조건과 일치핳는 경우가 없을 때 반환할 결과
END


SELECT EMPNO, ENAME, JOB, SAL,
			CASE JOB
					WHEN 'MANAGER ' THEN SAL*1.1
					WHEN 'SALESMAN' THEN SAL*1.05
					WHEN 'ANALYST' THEN SAL
					ELSE SAL*1.03
			END 
FROM EMP;
~~~


