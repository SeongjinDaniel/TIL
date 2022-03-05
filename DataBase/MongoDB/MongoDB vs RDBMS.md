# MongoDB vs RDBMS

| 특징            | SQL                | NoSQL      |
| ------------- |:------------------:|:----------:|
| 스키마           | 정적 스키마             | 동적 스키마     |
| 데이터 모델        | Entity Relation 모델 | document모델 |
| Object Mapper | 필수                 | 옵셔널, 거의 안씀 |
| 데이터베이스 구성     | static             | dynamic    |

SQL에 비해서 NoSQL 이 가지는 가장 큰 특징은 NoSQL은 **문서가 생성이 되면 저장 공간을 할당한다.** 즉, insert 전까지 콜렉션이 생성되지 않는다!!

관계형 데이터베이스는 N:N이 안되지만, NoSQL은 N:N이 된다. 관계형 데이터베이스에서 N:N 을 사용하기 위해서는 테이블을 연결하는 테이블인, 관계 엔티티(Associative Entity) 가운데 있어야 한다.

#### 참조

- [**Database/Data | NoSQL - MongoDB 란 무엇인가?**](https://mchaemil.github.io/2019/12/24/DB-nosql-what-is-the-nosql-and-mongodb.html)