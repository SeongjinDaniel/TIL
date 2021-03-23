# Character Data

☘️표시는 안했지만 scott 계정에서 EMP데이터를 가져오는 것이 아니라면 반드시 ***FROM DUAL*** 써줘야 합니다! 



#### * UPPER, LOWER, INITCAP

| 함수    | 설명                                           |
| ------- | ---------------------------------------------- |
| UPPER   | 괄호 안에 모두다 대문자로                      |
| LOWER   | 괄호 안에 모두다 소문자로                      |
| INITCAP | 괄호 안에 첫 문자만 대문자로 나머지는 소문자로 |

~~~SQL
UPPER/LOWER/INITCAP(문자열데이터)

SELECT UPPER(ENAME), LOWER(ENAME), INITCAP(ENAME)
FROM EMP
~~~

~~~SQL
SELECT *
FROM EMP
-- example 1
WHERE UPPER(ENAME) = UPPER('scott')

-- example 2
WHERE UPPER(ENAME) = LIKE UPPER ('%scott%')

-- 이렇게 찾을 수도 있다! 
~~~



#### * LENGTH 

##### 문자열 길이를 구하는 

~~~sql
LENGTH(문자열데이터)

SELECT LENGTH(ENAME)
FROM EMP
-- 추가로
WHERE LENGTH(ENAME)>=5 --이렇게 조건을 줘서 찾을 수도 있다.
~~~

***LENGTH와 LENGTHB 함수 비교하기***

~~~SQL
SELECT LENGTH('한글'), LENGTHB('한글')
FROM DUAL
-- 출력
-- 2, 4
-- The reason is.....
-- 			length는 개수, lengthb는 한글 한 글자를 2 Byte로 잡아서
~~~



#### * SUBSTR

##### 문자열 일부를 추출하는

* When C is **positive.**
  * CASE 1. SUBSTR (A, B, C)
    							***A문자열 데이터***에서 ***B번 위치에서 시작***해서***C개 출력***
  * CASE 2. SUBSTR (A, B)

​      					 ***A문자열 데이터***에서 ***B번 위치에서 시작***해서***끝까지 출력***

***CASE 1,2 잘 비교하기***🥳

~~~sql
SELECT SUBSTR(JOB, 2, 4), SUBSTR(JOB, 2)
FROM EMP
~~~

* When C is **negative**
  * CASE 3. SUBSTR (A, B, C)
  * CASE 4. SUBSTR (A, B)

**negative** 부호가 붙으면 그저 뒤에서부터 counting한다고 생각하기!!!!! 그러면 이해가 쉬움 :)

*그 외에는 C가 없으면 **끝까지 다 출력 **한다고 생각하기*

***CASE 3,4 햇갈리니깐 이 친구들도 잘 비교하기***😋

~~~sql
SELECT 
	SUBSTR(JOB, -LENGHT(JOB))
	SUBSTR(JOB, -LENGTH(JOB), 2)
	SUBSTR(JOB, -3)
~~~



#### * INSTR

#####  문자열 데이터 안에서 특정 문자 위치를 찾는 

##### 즉, 몇 번째에 그 문자가 있니!!! ???? 

* CASE 1. INSTR('A', 'B')
* CASE 2. INSTR('A', 'B', 'C')
* CASE 3. INSTR('A', 'B', 'C', 'D')

~~~sql
INSTR (대상 문자 데이터,
       위치를 찾으려는 부분문자,
       위치를 찾기 시작할 대상 문자열 데이터의 위치,   -- 안쓰면 default 1
       시작 위치에서 찾으려는 문자가 몇 번째 인지 지정) -- 안쓰면 default 1
       
SELECT INSTR ('HELLO, ORACLE!', 'L')
--3
SELECT INSTR ('HELLO, ORACLE!', 'L', 5)
--12
SELECT INSTR ('HELLO, ORACLE!', 'L', 2, 2)
--4
~~~



#### REPLACE

##### 특정 문자를 다른 문자로 바꾸는 (치환)

~~~SQL
REPLACE (문자열데이터, '찾는문자', '대체할 문자')

SELECT 
			REPLACE ('010-2985-2154' ,'-', ' ') 
			-- 010 2985 2154
			REPLACE ('010-2985-2154' ,'-')
			-- 01029852154 뒤에 값이 없으면 지정한 문자를 삭제하라는 뜻! 
~~~



#### LPAD, RPAD

##### 데이터의 빈 공간을 특정 문자로 채우는

~~~sql
LPAD(문자열 데이터 또는 열이름, 데이터 자리수(숫자로), '빈공간에 채울 문자')
RPAD(문자열 데이터 또는 열이름, 데이터 자리수(숫자로), '빈공간에 채울 문자')

SELECT
			LPAD('ORACLE', 10, '#')
			--####ORACLE
			RPAD('ORACLE', 10, '#')
			--ORACLE####
			LPAD('ORACLE', 10)
			--    ORACLE
			RPAD('ORACLE', 10)
			--ORACLE    -
			
~~~

 개인정보 입력하는 방법도 RPAD로 사용된다!



#### TRIM, LTRIM, RTRIM

##### 특정문자를 지우는

When you only use **"TRIM"**

* 왼쪽에 있는 글자를 지우는 **LEADNING**

* 오른쪽에 있는 글자를 지우는 **TRAILING**

* 양쪽의 글자를 모두 지우는 **BOTH**

  ​	삭제할 문자가 없을때/있을때 두가지 케이스가 있다. 꼭 살펴보자!
  
  * 삭제할 문자가 없을때
  
  ~~~SQL
  TRIM (삭제기본옵션(선택사항) || 삭제할 문자(선택사항) )

  SELECT '['|| TRIM(' _ _Oracle_ _ ') || ']'
  --[__Oracle__]
  SELECT '['|| TRIM(LEADING FROM ' _ _Oracle_ _ ') || ']'
  --[__Oracle__]
  SELECT '['|| TRIM(TRAILING FROM ' _ _Oracle_ _ ') || ']'
  --[__Oracle__]
  SELECT '['|| TRIM(BOTH  FROM ' _ _Oracle_ _ ') || ']'
  --[__Oracle__]
  -- ||은 공백 문자가 제거 됐는지 확인하기 위해 ||연산자를 사용하여 대괄호 []로 문자열을 감싸도록 했다아
  ~~~
  
  
  
  * 삭제할 문자가 있을때
  
  ~~~SQL
  SELECT '[' || TRIM('_' FROM '_ _Oracle_ _') || ']'
  --[_Oracle_]
  SELECT '[' || TRIM(LEADING'_' FROM '_ _Oracle_ _') || ']'
  --[_Oracle__]
  SELECT '[' || TRIM(TRAILING'_' FROM '_ _Oracle_ _') || ']'
  --[__Oracle_]
  SELECT '[' || TRIM(BOTH'_' FROM '_ _Oracle_ _') || ']'
  --[_Oracle_]
  ~~~
  
  

**LTRIM, RTRIM**

~~~SQL
LTRIM (원본문자 문자열 데이터, 삭제할 문자 집합) 
TRTIM (원본문자 문자열 데이터, 삭제할 문자 집합)

--삭제할 문자 집합을 선택하지 않으면 공백이 제거된다.

SELECT '[' || TRIM(' _Oracle_ ') || ']'
--[_Oracle_]
SELECT '[' || LTRIM(' _Oracle_ ') || ']'
--[_Oracle_ ]
SELECT '[' || LRIM('<_Oracle_>', '_<') || ']'
--[Oracle_>]
SELECT '[' || RTRIM(' _Oracle_ ') || ']'
--[ _Oracle_]
SELECT '[' || RTRIM('<_Oracle_>', '>_') || ']'
----[<_Oracle]
~~~



