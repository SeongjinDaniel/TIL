# 18_set



- 두 select 문을 통해 얻어온 결과를 집합 연산을 통해 하나의 결과로 만드는 것을 set이라고 부른다.
- 합집합, 교집합, 차집합 등 집합 연산을 할 수 있다.
- 집합 연산을 하기 위해서는 두 select문을 통해 가져오는 컬럼이 같아야 한다.



#### 합집합

- 두 select문의 결과를 모두 포함하는 최종 결과를 반환한다.
- UNION : 중복되는 데이터를 하나만 가져온다.
- UNION ALL : 중복되는 데이터도 모두 가져온다.



#### 교집합

- 두 select문의 결과 중 중복되는 부분만 가져온다.
- 교집합은 join 문을 사용한다.



#### 차집합

- 두 select 문에서 중복되는 부분을 제거하고 첫번 째 select 문 결과만 가져온다.
- 차집합은 서브쿼리를 이용한다.



```mysql
select emp_no from titles where title = 'Senior Staff';
select emp_no from titles where title = 'Staff';

-- 중복되는 데이터를 하나만 가져온다.
select emp_no from titles where title = 'Senior Staff'
union
select emp_no from titles where title = 'Staff';

-- 중복되는 데이터도 모두 가져온다.
select emp_no from titles where title = 'Senior Staff'
union all
select emp_no from titles where title = 'Staff';

select a1.emp_no
from titles a1, titles a2
where a1.emp_no = a2.emp_no and a1.title = 'Senior Staff' and
	  a2.title='Staff';

select emp_no
from titles
where title='Staff' and 
	  emp_no not in(slect emp_no from titles where title='Senior Staff');
```



#### 학습정리

- 집합연산을 하면 합집합, 차집합, 교집합 연산을 할 수 있다.