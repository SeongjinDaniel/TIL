# aws DynamoDB Summary



## DynamoDB란 (1)



- NoSQL(Not Only SQL) 데이터베이스
  - Not only A, but also B
- **매우 빠른 쿼리 속도**
- **Auto-Scaling** 기능 탑재
- **Key-Value** 데이터 모델 지원
- **테이블 생성시 스키마 생성 필요 없음**
- 모바일, 웹, IoT 데이터 사용시 추천됨
- SSD 스토리지 사용



## DynamoDB란 (2)



- 테이블 (Table)
- 아이템 (Items) - 행(row)과 개념이 비슷함
- 특징 (Attributes) - 열(column)과 개념이 비슷함
- Key-Value (Key : 데이터의 이름, Value : 데이터 자신)
- 예시) JSON, XML



## DynamoDB - Primary Keys (PK)



- PK를 사용하여 데이터 쿼리
- DynamoDB에는 두가지의 PK 유형이 있음
  - **파티션키 (Partition Key)**
    - 고유 특징 (Unique Attribute)
    - 실제 데이터가 들어가는 위치를 결정해줌
    - 파티션키 사용시 동일한 두개의 데이터가 같은 위치에 저장될 수 없음!
  - **복합키**
    - 파티션키(Partition Key) + 정렬키(Sort Key)
    - 예시 : 똑같은 고객이 다른 날짜에 다른 물건을 구매
    - 파티션키: 고객 아이디, 정렬키 : 날짜 (Timestamp)
    - 같은 파티션키의 데이터들은 같은 장소에 보관, 그 다음 정렬키에 의해 데이터가 정렬됨



## DynamoDB 데이터 접근 관리



- AWS IAM으로 관리할 수 있음
  - 테이블 생성과 접근 궈너한을 부여할 수 있음
  - 특정 테이블만, 특정 데이터만 접근 가능케 해주는 특별한 IAM 역할 존재

<img src="C:\Users\oliver\AppData\Roaming\Typora\typora-user-images\image-20210227220242878.png" alt="image-20210227220242878" style="zoom:67%;" />



## Index

- 특정 컬럼만을 사용하여 쿼리 
- 테이블 전체가 아닌 기준점(pivot)을 사용해 쿼리가 이루어짐
- 매우 큰 쿼리 성능 효과
- 두가지의 Index 유형 존재
  - **Local Secondary Index**
  - **Global Secondary Index**



#### Local Secondary Index

- 테이블 생성시에만 정의해줄 수 있음
- 따라서 테이블 생성 후 변경, 삭제가 불가능
- 똑같은 파티션키 사용, 그러나 다른 정렬키 사용

<img src="https://user-images.githubusercontent.com/76925694/109388174-ca165700-7948-11eb-8f58-1d86e71ffc65.png" alt="image" style="zoom:50%;" />



#### Global Secondary Index

- 테이블 생성후에도 추가, 변경, 삭제 가능
- 다른 파티션키, 정렬키 사용

<img src="C:\Users\oliver\AppData\Roaming\Typora\typora-user-images\image-20210227221217636.png" alt="image-20210227221217636" style="zoom:60%;" />







## Query VS Scan



#### Query

- Primary Key를 사용하여 데이터 검색
- Query 사용시 모든 데이터(컬럼) 반환
- ProjectionExpression 파라미터 -> 이용하여 원하는 컬럼만 볼 수 있음

<img src="https://user-images.githubusercontent.com/76925694/109388238-46109f00-7949-11eb-97ea-da0512a33a81.png" alt="image" style="zoom:67%;" />



#### Scan

- 모든 데이터를 불러옴 (primary key 사용 X)
- ProjectionExpression 파라미터



#### Query VS Scan

- Query 가 Scan보다 훨씬 효율적임
- 따라서 Query 사용 추천

- Scan

<img src="https://user-images.githubusercontent.com/76925694/109388336-c20ae700-7949-11eb-9d8f-51f0ff1bd013.png" alt="image" style="zoom:80%;" />

<img src="https://user-images.githubusercontent.com/76925694/109388343-c9ca8b80-7949-11eb-8c86-27f6a8227ae5.png" alt="image" style="zoom:80%;" />





## DAX(DynamoDB Accelerator)



#### DAX란?

- 클러스터 In-memory 캐시
- 10배 이상의 속도 향상
- 읽기 요청만 해당사항 (X 쓰기요청)
- Ex) Black Fiday날 쇼핑 웹사이트 운영 (수많은 읽기 요청 예상)



#### DAX 원리

- DAX 캐싱 시스템
  - 테이블에 데이터 삽입 & 업데이트시 DAX에도 반영
- 읽기 요청에 맞는 데이터가 DAX에 들어있을시 DAX에서 데이터 즉시 반환 (**Cache Hit**) <-> (Cache Miss)



#### DAX 단점

- 쓰기 요청이 많은 어플리케이션에서는 부적절함
- 읽기 요청이 많지 않은 어플리케이션에서 부적절함
- 아직 모든 지역에서 제공하지 않음



현재 DAX는 서울에서 지원하지 않는다.



## DynamoDB Streams



- DynamoDB 테이블에서 일어나는 일들(삽입, 수정, 삭제 등)이 일어날 시 시간적 순서에 맞게 Streams에 기록
- Log는 즉각 암호화가 일어나면 24시간동안 보관됨
- 주로 이벤트를 기록하고 이벤트 발생을 외부로 알리는 용도 (예시 : Lambda Function)
- 이벤트 전&후에 대한 상황 보관

<img src="https://user-images.githubusercontent.com/76925694/109408267-1c985780-79cb-11eb-9f33-7d27b6a7cc5c.png" alt="image" style="zoom:80%;" />

<img src="https://user-images.githubusercontent.com/76925694/109408276-2cb03700-79cb-11eb-8235-72cc0b065a1d.png" alt="image" style="zoom:80%;" />



