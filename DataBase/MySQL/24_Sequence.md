# 24_Sequence



- 로우를 추가할 때 자동으로 증가하는 값이 저장되는 것을 시퀀스라고 부른다.
- 시퀀스는 데이터베이스 마다 사용하는 방법이 다르므로 반드시 파악해야 한다.
- mysql은 auto_increment 키워드를 설정해주면 된다.
- 데이터를 insert 할 때 auto_increment를 설정한 컬럼은 제외한다.



#### limit

- select 해서 가져온 로우에서 원하는 범위의 로우만 가지고 올 때 사용한다.
- 게시판 등에서 사용하는 페이징 기법을 구현할 때 사용한다.
- 데이터 베이스마다 구현하는 방법이 다르므로 반드시 파악해야 한다.
- select 문 limit 시작인덱스, 개수



```mysql
create table test_table100(
    data1 int auto_increment,
    data2 int not null,
    data3 int not null,
    constraint pk1 primary key(data1)
);

-- data1의 값은 자동으로 증가해서 들어가기 때문에 null이 아니라서 오류 안남!
insert into test_table100 (data2, data3) values (100, 200);
insert into test_table100 (data2, data3) values (101, 201);
insert into test_table100 (data2, data3) values (102, 202);
select * from test_table100;

use employees;

select * from employees order by emp_no;
-- 처음부터 10개를 가져온다.
select * from employees order by emp_no limit 0, 10;
-- 11번 부터 10개를 가져온다.
select * from employees order by emp_no limit 10, 10;

```



#### 학습 정리

- 시퀀스를 사용하면 자동으로 증가되어 저장되는 컬럼을 만들 수 있다.
- limit를 사용하면 정해진 범위에 해당하는 로우를 가져올 수 있다.