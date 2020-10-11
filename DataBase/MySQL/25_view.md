# 25_view



- 뷰는 가상의 테이블을 의미한다.
- 두 개 이상의 테이블을 조인하거나 서브쿼리를 사용하는 select 문은 쿼리문이 복잡해지게 되는데 이를 매번 사용하게 되면 개발자의 불편함이 따르게 된다.
- 이 때 조인이나 서브쿼리를 사용해 얻어진 결과를 뷰로 만들어 놓으면 개발자는 뷰를 통해 결과를 얻어 올 수 있다.
- 사실 뷰는 select문 통해 얻어진 결과를 가지고 있는 것이 아니라 select문 자체를 가지고 있어 뷰를 select 하면 이전에 사용한 쿼리문이 실행되어 결과를 가져오게 된다.



- `Create view 뷰이름 as select 쿼리문`
- `Drop view 뷰이름`



```mysql
create table test_table1000(
    data1 int,
    data2 int not null,
    constraint pk1 primary key (data1)
);

create table test_table2000(
    data1 int not null,
    data2 int not null,
    constraint fk1 foreign key (data1) references test_table1000(data1)
);

insert into test_tabl1000(data1, data2) values (1, 10);
insert into test_tabl1000(data1, data2) values (2, 20);
insert into test_tabl1000(data1, data2) values (3, 30);
select * from test_table1000;

insert into test_tabl2000(data1, data3) values (1, 100);
insert into test_tabl2000(data1, data3) values (2, 200);
insert into test_tabl2000(data1, data3) values (3, 300);
select * from test_table2000;

select a1.data1, a1.data2, d2.data3
from test_table1000 a1, test_table2000 a2
where a1.data1 = a2.data1;

-- view 생성!!
create view test_view1
as
select a1.data1, a1.data2, d2.data3
from test_table1000 a1, test_table2000 a2
where a1.data1 = a2.data1;

-- 위에 세팅된 쿼리문이 출력된다.
select * from test_view1;

insert into test_table100 (data1, data2) values(4, 40);
insert into test_table2000 (data1, data3) values(4, 400);

-- 추가된것 까지 확인이 가능하다
select * from test_view1;

drop view test_view1;
select * test_view1; -- 존재 하지 않아서 오류남!! 

```



#### 학습 정리

- 복잡한 select 쿼리문을 이용해 뷰를 만들면 이후 부터는 편하게 데이터를 조회할 수 있다.	