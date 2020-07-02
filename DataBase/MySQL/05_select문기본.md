# select문 기본

- select 구문은 저장되어 있는 데이터를 가져올 때 사용한다.
- select 컬럼명 from 테이블명

### 테이블의 모든 정보 가져오기

- select * from 테이블명
- 사원의 모든 정보를 가져올 경우 사원 정보는 employees 테이블에 있으므로 다음과 같이 작성한다.
- select * from employees

![image](https://user-images.githubusercontent.com/55625864/86307248-425d3900-bc51-11ea-8071-bd0d7003bf1e.png)



### 연습 문제

- 부서 정보를 모두 가져온다.
- 부서 관리자 정보를 모두 가져온다.
- 사원들 직함 정보를 모두 가져온다.

### 일부 컬럼만 가져오기

- select 컬럼명1, 컬럼명2, 컬럼명3 from 테이블명

- 사원의 정보 중 사원번호, 사원 이름을 가져올 경우 다음과 같이 작성한다.

- select emp_no, first_name, last_name from employees

  ![image](https://user-images.githubusercontent.com/55625864/86307689-57869780-bc52-11ea-8861-287c5faf4211.png)



### 연습문제

- 사원의 사원번호, 생년월일, 성별을 가져온다.
- 부서의 부서번호, 부서 이름을 가져온다.
- 각 사원의 사원번호, 급여액을 가져온다.
- 각 사원의 사원번호, 직함 이름을 가져온다.



### 학습정리

- select 문을 사용하면 데이터를 가져올 수 있다.
- select * from 테이블명;
- select 컬럼명1, 컬럼명2 from 테이블명;

