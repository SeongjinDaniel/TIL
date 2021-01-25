# PostgreSQL에서 자동 증가 기본 키를 정의하는 방법



**1 단계, 테이블 생성 :**

```
CREATE TABLE epictable
(
    mytable_key    serial primary key,
    moobars        VARCHAR(40) not null,
    foobars        DATE
);
```



**2 단계, 다음과 같이 테이블에 값을 삽입하고 mytable_key가 첫 번째 매개 변수 목록에 지정되지 않았 음을 확인합니다. 이로 인해 기본 시퀀스가 자동 증가합니다.**

```sql
insert into epictable(moobars,foobars) values('delicious moobars','2012-05-01')
insert into epictable(moobars,foobars) values('worldwide interblag','2012-05-02')
```



#### 참조

- https://stackoverflow.com/questions/7718585/how-to-set-auto-increment-primary-key-in-postgresql