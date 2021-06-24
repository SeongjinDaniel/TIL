# index 조회, 추가, 삭제

1. 테이블의 **인덱스 조회**
   - `SHOW INDEX FROM tablename;`
2. 테이블의 **인덱스 추가**
   - 테이블의 인덱스 추가 : 컬럼은 1개도 가능, 2개 이상도 가능
     - `ALTER TABLE tablename ADD INDEX indexname (column1, column2);`
   - 테이블의 유니크 인덱스 추가 : 컬럼은 1개도 가능, 2개 이상도 가능
     - `ALTER TABLE tablename ADD UNIQUE INDEX indexname (column1, column2);`

3. 테이블의 **인덱스 삭제**
   - `ALTER TABLE tablename DROP INDEX indexname;`

