# 15_groubby&having



#### group by

- 앞서 살펴본 그룹 함수를 사용하면 로우의 수, 총합, 평균, 최대, 최저 값을 가져올 수 있다.
- 앞서 살펴본 예제들은 select 문을 통해 가져온 모든 로우를 하나의 그룹으로 묶고 그 안에서 로우의 수, 총합, 평균, 최대, 최저 값을 구하게 된다.
- Group by 절은 select문을 통해 가져온 모든 로우를 개발자가 정한 기준에 따라 그룹으로 나눌 수 있다.
- Group by 절을 이용해 그룹으로 나눈 후 그룹 함수를 사용하면 각 그룹내에서 로우의 수, 총합, 최대, 최저 값을 구할 수 있다.

#### having

- Group by 절을 이용하여 개발자가 정한 기준으로 그룹을 나눈 후 having 절로 만든 조건에 맞는 그룹의 데이터만 가져올 수 있다.



```mysql
-- 사원의 수를 성별로 구분하여 가져온다.
select gender, count(*) from employees
group by gender;

-- 각 부서에 근무하고 있는 사원들의 수를 가져온다.
select count(*)
from dept_emp
where to_date = '9999-01-01'
group by dept_no;

-- 각 부서별 과거의 매니저의 수를 가져온다.
select dept_no, count(*)
from dept_manager
where to_date <> '9999-01-01'
group by dept_no;

-- 급여 수령 시작일별 급여 총합을 가져온다.
select from_date, sum(salary)
from salaries
group by from_date;

-- 급여 수령 시작일별 급여 평균을 가져온다.
select from_date, avg(salary)
from salaries
group by from_date;

-- 급여 수령 시작일별 급여 최고액을 가져온다.
select from_date, max(salary)
from salaries
group by from_date;

-- 급여 수령 시작일별 급여 최저액을 가져온다.
select from_date, min(salary)
from salaries
group by from_date;

-- having
-- 10만명 이상이 사용하고 있는 직함의 이름과 직원의 수를 가지고 온다.
select title, count(*)
from titles
group by title
having count(*) >= 100000;

-- 5만명 이상 근무하고 있는 부서의 부서 번호와 부서 소속 사원의 수를 가져온다.
select dept_no, count(*)
from dept_emp
group by dept_no
having count(*) >= 50000;

```



#### 학습 정리

- Group by 절을 이용하면 데이터를 그룹별로 나눠 가져올 수 있다.
- Having 절을 이용하면 원하는 그룹의 데이터만 가져올 수 있다.