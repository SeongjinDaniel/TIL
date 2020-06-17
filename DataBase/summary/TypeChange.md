# Type Change Function

☘️표시는 안했지만 scott 계정에서 EMP데이터를 가져오는 것이 아니라면 반드시 ***FROM DUAL*** 써줘야 합니다! 



##### 문자와 숫자를 더하는 형식은 오류가 뜬다.

Ex.

~~~SQL
SELECT 'ABCD' + EMPNO
FROM EMP
-- 'ABCD'는 문자형
-- EMPNO 는 숫자형 이라서
~~~



| 종류      | 설명                                       |
| --------- | ------------------------------------------ |
| TO_CHAR   | 숫자 또는 날짜 데이터를 문자 데이터로 변환 |
| TO_NUMBER | 문자 데이터를 숫자 데이터로 변환           |
| TO_DATE   | 문자 데이터를 날짜 데이터로 볂환           |



숫자는 -> 문자만

날짜는 -> 문자만

문자는 -> 날짜만

문자는 -> 숫자만

데이터 형 변환 가능하다.



###### ⭐️TO_CHAR을 가장 많이 쓰는 것 같다. 설명이 제일 길다.⭐️

#### * TO_CHAR

##### 날짜, 숫자 데이터를 문자데이터로 변환하는 

~~~SQL
TO_CHAR(날짜데이터, '출력되길 원하는 문자형태')

SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD HH24:MI:SS')
FROM DUAL

-- 현재 시간이 출력된다.
~~~

| 형식       | 설명                        |
| ---------- | --------------------------- |
| CC         | 세기                        |
| YYYY, RRRR | 연(4자리 숫자)              |
| YY, RR     | 연(2자리 숫자)              |
| MM         | 월(2자리 숫자)              |
| MON        | 월( 언어별 월 이름 약자)    |
| MONTH      | 월( 언어별 월 이름 전체)    |
| DD         | 일(2자리 문자)              |
| DDD        | 1년 중 며칠(1~366)          |
| DY         | 요일(언어별 요일 이름 약자) |
| DAY        | 요일(언어별 요일 이름 전체) |
| W          | 이번달 몇째 주              |
| WW         | 이번년도 몇째 주            |

~~~SQL
SELECT TO_CHAR(SYSTAE, 'MM')
-- 07
SELECT TO_CHAR(SYSTAE, 'MON')
-- 7월
SELECT TO_CHAR(SYSTAE, 'MONTH')
-- 7월
SELECT TO_CHAR(SYSTAE, 'DD')
-- 14
SELECT TO_CHAR(SYSTAE, 'DY')
-- 토
SELECT TO_CHAR(SYSTAE, 'DAY')
-- 토요일
~~~

##### 여러 언어로 날짜 표현하기

~~~SQL

TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE=JAPANESE')
--TO_CHAR(날짜데이터, '출력되길 원하는 문자형태',
            'NLS_DATE_LANGUAGE = LAGUAGE')

SELECT TO_CHAR(SYSDATE, 'MM')
-- 07
SELECT TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE=JAPANESE')
-- 7 (한자로 월)
SELECT TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE=KOREAN')
-- 7월
SELECT TO_CHAR(SYSDATE, 'MON', 'NLS_DATE_LANGUAGE=ENGLISH')
-- JUL
SELECT TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE=JAPANESE')
-- 7 (한자로 월)
SELECT TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE=KOERAN')
-- 7월
SELECT TO_CHAR(SYSDATE, 'MONTH', 'NLS_DATE_LANGUAGE=ENGLISH')
-- JULY
~~~



##### 시간 형식으로 표현하기

| 형식               | 설명                   |
| ------------------ | ---------------------- |
| HH24               | 24시간으로 표현한 시간 |
| HH, HH12           | 12시간으로 표현한 시간 |
| MI                 | 분                     |
| SS                 | 초                     |
| AM, PM, A.M., P.M. | 오전, 오후 표시        |

~~~SQL
SELECT TO_CHAR(SYSDATE, 'HH24:MI:SS')
--00:03:49
SELECT TO_CHAR(SYSDATE, 'HH12:MI:SS AM')
--12:03:49 오전
SELECT TO_CHAR(SYSDATE, 'HH:MI:SS P.M.')
-- 12:03:49 오전
~~~



##### 숫자 데이터 형식을 지정하여 출력하기

| 형식 | 설명                                  |
| ---- | ------------------------------------- |
| 9    | 숫자의 한 자리를 의미함               |
| 0    | 빈 자리를 0으로 채움을 의미한다.      |
| $    | 달러($) 표시를 붙여서 출력            |
| L    | L(locale)지역 단위 기호를 붙여서 출력 |
| .    | 소수점을 표시함                       |
| ,    | 천 단위의 구분 기호를 표시            |

~~~SQL
SELECT SAL
-- 800
SELECT TO_CHAR(SAL, '$999,999')
-- $800
SELECT TO_CHAR(SAL, 'L999,999')
-- WON800
SELECT TO_CHAR(SAL, '999,999.00')
-- 800.00
SELECT TO_CHAR(SAL, '000,999,999.00')
-- 000,000,800.00
SELECT TO_CHAR(SAL, '000999999.00')
-- 000000800.00
SELECT TO_CHAR(SAL, '999,999,00')
-- 8,00
~~~



#### * TO_NUMBER

##### 문자데이터를 숫자 데이터로 변환하는

~~~sql
SELECT 1300 - '1500', '1300' + 1500
FROM DUAL
-- 200 , 2800
~~~

~~~sql
TO_NUMBER ('문자열 데이터', '인식될 숫자형태')

SELECT TO_NUMBER('1,300', '999,999')- TO_NUMBER('1,500', '999,999')
FROM DUAL
-- -200
~~~



#### * TO_DATE

#####  문자 데이터를 날짜 데이터로 변환하는 

~~~sql
TO_DATE('문자열 데이터', '인식될 날짜 형태')

SELECT TO_DATE('1991-03-24', 'YYYY-MM-DD')
--1991/03/24
SELECT TO_DATE('19910324', 'YYYY-MM-DD')
--1991/03/24
~~~



##### 여러가지 형식으로 날짜 데잍터 출력하기

~~~SQL
SELECT TO_DATE('97/03/21', 'YY/MM/DD')
-- 1997/03/21
SELECT TO_DATE('97/03/21', 'RR/MM/DD')
-- 1997/03/21
~~~



📌주의!!!

날짜 데이터 형식을 지정할때 YYYY, RRRR, YY RR을 사용할 수 있는데

네 자리로 표현하는 연도는 상관 없지만

두자리 연도로 표현할 때는 YY, RR는 주의를 기울여야한다.