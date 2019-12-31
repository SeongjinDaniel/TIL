# Day5

```sql
SELECT * FROM EMP WHERE 1 <> 1 -- 비어있는 RESULTSET -> 빈테이블!!
-- table 의 culumn 정보는 필요한데 내용은 필요 없음

```

```sql
[ 오라클의 휴지통 기능 ]

휴지통에 들은 테이블을 조회.
SQL> show recyclebin;

휴지통의 모든 내용이 비워집니다.
SQL> purge recyclebin;

삭제된 테이블을 되살리고 싶다면
SQL> flashback table 테이블명 to before drop;

특정 테이블을 휴지통에 남기지 않고 모두 삭제하려면..
SQL> drop table 테이블명 purge;

purge문 없이 그냥 drop 한 후에는
SQL> purge table 테이블명;
```