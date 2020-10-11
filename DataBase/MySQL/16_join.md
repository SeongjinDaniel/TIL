# 16_join



#### 데이터 중복의 최소화

- 데이터 베이스에서 가장 중요한 부분은 데이터를 가져오는데 걸리는 시간의 최소화이다.
- 데이터 베이스는 저장된 데이터의 총량이 크면 클 수록 데이터를 가져오는데 시간이 오래 걸리게 된다.
- 이 때문에 데이터의 중복을 최소화 하여 데이터를 빠르게 가져올 수 있도록 테이블을 구성하게 된다.
- 이 과정에서 테이블을 두 개 이상으로 분리될 수 밖에 없다.



- 예를 들어 고객의 구매 정보를 저장하는 테이블이 있고 이 테이블은 고객이름, 고객 전화번호, 상품 이름, 상품 가격으로  구성되어 있다고 가정한다.
- 고객 한명이 여러 상품을 구매할 수 도 있고 같은 상품을 여러 사람이 구매할 수도 있기 때문에 데이터를 상당히 중복 될 수 밖에 없다.

![image](https://user-images.githubusercontent.com/55625864/95670631-e2b7e780-0bc8-11eb-950d-5c86712af76f.png)



- 앞서 살펴본 테이블을 다음과 같이 나누면 데이터의 중복을 최소화 할 수 있다.

![image](https://user-images.githubusercontent.com/55625864/95670654-0da23b80-0bc9-11eb-998d-f2e8d73fd6dd.png)



- 위와 같이 데이터의 중복을 최소화 하기 위해 테이블을 분리 시킨 후 데이터를 가져올 때 여러 테이블을 하나의 결과로 가져와야 하는데 이럴 때 Join문을 사용한다.
- Join문을 사용하면 여러 테이블의 데이터를 한번에 가져올 수 있다.



- 여러 테이블을 join할 때는 테이블의 이름을‘,’ 로 구분하여 작성하여 주고 각 테이블의 컬럼명을 기술하여 주면 원하는 데이터를 가져올 수 있다.
- Select 컬럼명1, 컬럼명2, 컬럼명3
  from 테이블1, 테이블2



- Join문을 사용하게 되면 다 대 다의 관계를 가져온게 된다. 이 때문에 잘못된 데이터가 구성될 수 있는데 이를 위해 join 조건문을 작성해야 한다.
- join문을 사용하면 공통으로 사용하는 값을 묶어 줘야한다.

```mysql
-- 각 사원들의 사원번호, 근무 부서 번호, 근무 부서 이름을 가져온다.
-- 사원번호를 기준으로 오름 차순 정렬한다.
select dept_emp.emp_no, dept_emp.dept_no, departments.dept_name
from departments, dept_emp

select a2.emp_no, a2.dept_no, a1.dept_no, a1.dept_name
from departments a1, dept_emp a2
where a1.dept_no = a2.dept_no
order by a2.emp_no;

-- 각 사원들의 사원번호, first_name, 근무 부서 번호를 가져온다.
select a1.emp_no, a1.first_name, a2.dept_no
from employees a1, dept_emp a2
where a1.emp_no = a2.emp_no

-- 각 사원들의 사원번호, first_name, 현재 받고 있는 급여액을 가져온다.
select a1.emp_no, a1.first_name, a2.salary
from employees a1, salaries a2
where a1.emp_no = a2.emp_no
	  and a2.to_date='9999-01-01';

-- 각 사원들의 사원번호, first_name, 근무 부서 이름를 가져온다.
select a1.emp_no, a1.first_name, a3.dept_name
from employees a1, dept_emp a2, departments a3
where a1.emp_no = a2.emp_no and a2.dept_no = a3.dept_no;

```



#### 학습 정리

- 여러 테이블에서 데이터를 동시에 가져올 때 join 문을 사용한다.
- Join 문은 다 대 다의 관계로 가져오기 때문에 잘못된 데이터를 포함한다. 이를 제거하기 위해 조건문을 설정해야 한다.