# 트랜젝션

- **데이터 베이스에서 데이터 처리의 한 단위**를 트랜젝션이라고 부른다.
- 대부분의 데이터베이스는 데이터를 저장하고 수정하고 삭제하는 작업을 바로 물리적인 하드디스크에 저장된 데이터에 반영하지 않는다.
- 이는 개발자의 실수로 잘못된 명령문을 입력하였을 경우 다시 원래 상태로 되돌리기 위한 안전 장치이다.
- 따라서 개발자가 **커밋**이라는 작업을 하기 전까지 입력한 명령문은 메모리에서만 동작하고 물리적인 하드디스크에 반영하지 않으며 **커밋** 작업이 발생하면 그때 하드디스크에 반영하게 된다.

- **개발자가 데이터에 대한 작업을 하기 위해 입력하는 명령문들의 시작부터 커밋까지를 하나의 트랜젝션**이라고 부른다.



#### RollBack

- 데이터의 저장, 삭제, 수정 등의 작업을 하고 난 후 원래의 형태로 되돌리는 작업을 의미한다.
- 커밋이라는 작업을 하고 난 이후에는 RollBack 작업을 해도 원래의 형태로 되돌릴수 없다.
- workbench등의 프로그램에서는 자동으로 커밋 작업이 발생하므로 RollBack을 해도 원래의 형태로 되돌릴수가 없다.

![image](https://user-images.githubusercontent.com/55625864/87310641-33339080-c559-11ea-9f00-f0dbe444fbf0.png)

그리고 종료했다가 재접속!!



#### Commit

- 하나의 트랜젝션을 물리적인 데이터베이스에 적용하는 작업이다.
- 이 작업을 하게 되면 RollBack을 해도 되돌릴 수 없다.   ----> commit을 하면 새로운 트랜젝션이 생성되기때문에 RollBack을 해도 새로운 트랜젝션 처음으로 RollBack된다.
- 일반적으로 개발자가 만드는 프로그램들은 자동으로 커밋이 발생한다.



#### SavePoint

- save point를 지정하면 rollback시 지정된 위치로 복원할 수 있다.
- savepoint 명령어로 지점을 지정하고 rollback 명령어로 복원한다.
- 여기서 `rollback to savepot지정명`으로 rollback 가능하다.



#### truncate

- truncate를 사용하면 지정된 테이블의 모든 로우를 삭제한다.
- delete문과 다른점은 delete문은 데이터베이스에 바로 반영하지 않으므로 rollback이 가능하지만 **truncate는 바로 데이터베이스에 반영하므로 rollback이 불가능하다.**



```mysql
delete from test_table2;
select * from test_table2;

rollback;
select * from test_table2; -- 복원된거 확인 가능

delete from test_table2;
select * from test_table2;
rollback;
select * from test_table2;

delete from test_table2;
commit;
select * from test_table2;
rollback;
select * from test_table2; -- 복원 안됨 커밋 했기 때문에
-- -------------------------------------------------------------

insert into test_table2 (data1, data2, data3) values (100, '문자열1', 11.11);
insert into test_table2 (data1, data2, data3) values (200, '문자열2', 22.22);
insert into test_table2 (data1, data2, data3) values (300, '문자열3', 33.33);

-- ------------------------------------------------------------
-- 이렇게 하면 rollback시 commit 바로 이후의 데이터가 저장된다.
commit;
select * from test_table2;

update test_table2 set data2='새로운문자열', data3=44.44 where data1=100;
select * from test_table2;
delete from test_table2 where dat1=100;
select * from test_table2;
rollback;
select * from test_table2;

-- savepoint 까지 롤백 됌
commit;
select * from test_table2;

update test_table2 set data2='새로운문자열', data3=44.44 where data1=100;
savepoint aa;
select * from test_table2;
delete from test_table2 where data1=100;
select * from test_table2;
rollback to aa;
select * from test_table2;

-- 
commit;

select * from test_table2;

delete from test_table2;
select * from test_table2;
rollback;
select * from test_table2;

truncate test_table2;
rollback;
select * from test_table2; -- rollback 불가능

```



#### 학습정리

- rollback 명령문을 사용하면 데ㅣ터를 복원할 수 있다.
- commit을 하게 되면 데이터 베이스에 반영한다.
- savepoint를 이용하면 복원 지점을 설정할 수 있다.
- truncate를 사용하면 테이블의 모든 로우를 삭제할 수 있으며 복원은 불가능하다.