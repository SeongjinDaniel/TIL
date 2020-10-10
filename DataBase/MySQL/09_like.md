# 09_like



- 조건식을 만들어 줄 때 문자열과 비교 시 사용한다.
- 문자열 값을 비교할 때 = 을 이용하면 지정된 문자열이 저장되어 있는 로우를 가져 올 수 있다.

- Like는 이를 보다 확장해서 조건을 만들어 줄 때 사용한다.
- Like는 와일드 카드라는 개념을 사용하는데 와일드 카드는 모든 글자를 의미하는 특수 기호이다.
- _ : 글자 하나를 의미한다.
- % : 글자 수와 상관 없이 모든 글자를 의미한다.



```mysql
-- 이름이 Tommaso 사원의 사원번호, 이름을 가져온다.
select emp_no, firstname
from employees
where first_name = 'Tomaso';

-- 이름이 A로 시작하는 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name like 'A%';

-- 이름의 마지막 글자가 s로 끝나는 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name like '%s';

-- 이름의 두 번째 글자가 i인 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name like '_i%';

-- 이름에 o가 포함되어 있는 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where forst_name like '%o%';

-- 이름에 o가 포하되어 있는 사원의 사원번호, 이름을 가져온다.
-- 단 마지막 글자가 o가 아닌 사원만 가져온다.
select emp_no, first_name
from employees
where first_name like '%o%' and not first_name like '%o';

-- 이름이 5글자인 사원의 사우너 번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name like '_____'; -- _ 5개

```

Like 연산자를 사용하면 다양한 문자열 조건식을 만들 수 있다.