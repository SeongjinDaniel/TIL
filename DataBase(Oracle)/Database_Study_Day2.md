# Day2

**[ SELECT 명령어 ]**

```sql
select 추출하려는 컬럼명리스트 또는 *
from 테이블이름
[where 행의조건식]
[order by 컬럼명(별칭, 식) desc|asc] 
```

```sql
SELECT [조회할 열1 이름], [열2 이름], ... [열N 이름]
FROM [조회할 테이블 이름]
WHERE [조회할 행을 선별하기 위한 조건식];
```

```sql
where num = 10
where name = '김정현' -- 문자 데이터는 단일 인용 부호 ''
				    -- 별칭은 더블 인용 부호 ""
where hiredate = '1997/10/21'
where name = 'KIM'
where name = 'kim'	-- 문자 데이터는 대소문자 구분됨
where name = '김'
-- where 문이나 num, name 등등은 대소문자 구분 안해도된다.
where name like '김%'	-- 0개 이상의 모든 데이터 - meta character
where addr like '%강남구%'	-- 0개 이상의 모든 데이터 - meta character
						-- 앞에 있던 뒤에있던 상관없이 강남구만 있으면 조회
where addr like '강남구%'  -- 앞에 강남구가 있으면 조회
where addr like '%강남구'  -- 뒤에 강남구가 있으면 조회
where name like '김__'	 -- 임의의 문자 1개
						-- 성은 김이고 이름은 두글자인 이름을 조회
where ssn like '______-1______' -- 주민등록번호 조회
```

```sql
-- 모든 행 출력
select * from tab; -- 오라클은 tab은 dictionary라고 함
				  -- 오라클 테이블 정보를 가지고 있다.
-- 하나의 컬럼으로 출력하기 위해서는
|| 연산자를 사용한다.
select 컬럼1 || 컬럼2 "별칭"
select concat(컬럼1, 컬럼2) "별칭"
select 컬럼1 || ',' || 컬럼2 "별칭"
```

```sql
-- rr/mm/dd - 기본설정 날짜 포맷
-- yy/mm/dd
```



