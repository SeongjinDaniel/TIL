# MongoDB and Morphia

### MongoDB

MongoDB는 JSON(JavaScript Object Notation) 스타일 문서를 저장하고 검색하기 위한 문서 지향 데이터베이스이다. 인덱싱, 복제 및 샤딩 기능으로 늘어난 MongoDB는 강력하고 확장 가능한 NoSQL 경쟁자로 부상했다. 공식 Java 드라이버는 MongoDB와 상호작용하기 위해 사용 가능하다. 드라이버는 데이터 저장소에서 문서를 표현하기 위해 Map 구현인 BasicDBObject를 제공한다. Map 표현이 편리하다고 하더라도, 특히 JSON에서 왔다갔다하며 일련화할 때 문서를 Java 클래스 계층으로 표현할 수 있는 것도 장점을 가진다. 예를 들어, Java 도메인 모델에서부터 왔다갔다하며 문서를 맵핑하면 MongoDB로 스키마 제거 개발의 혜택을 누리는 동시에 Java 계층에서 유형 안전을 강제 실행할 수 있다. 그리고 많은 Java 프레임워크는 POJO(Plain Old Java Objects)의 사용을 가정하거나, 이를 더 능히 처리할 수 있다.

개발자들이 MongoDB를 사용하는 이유는 직관적인 데이터 모델 때문일 것이다. MongoDB는 정보를 행(row) 대신에 도큐먼트(document)에 저장한다. 도큐먼트(document)의 데이터 구조는 한 개 이상의 key-value 쌍으로 되어 있다.

#### MongoDB의 구조 및 스키마 디자인

MongoDB는 하나의 서버에 Database를 여러개 가지고 있을 수 있고, 각 Database 는 여러개의 collection이 있으며, collection 내부에는 document들이 있다.

```
<SERVER>
│
├<Database>
│ ├──<collection>
│ │   ├── document
│ │   ├── document
│ │   ├── document
│ │   └── document
│ │
│ └──<collection>
│     ├── document
│     ├── document
│     └── document
```

##### Literal은 코드 상에서 데이터를 표기하는 방법

리터럴은 어떤 데이터를 표기하는 법 {} - 객체를 표현할 때 사용하는 표기법, 객체 리터럴 [] - 배열, 리스트, Document 를 표현하느 표기법, 배열 리터럴

##### collection

MongoDB도 create collection 이라는 명령으로 document를 담는 그릇을 미리 만들어 놓을 수도 있지만!! 대부분은 데이터를 넣을 때 생성이 되게 만든다..

##### 모든 문서는!!

모든 문서는!, 중첩된 문서는 제외!! 서브 다큐먼트는 문서가 없었다. 서브 문서에는 아이디가 없었다.

count()는 collection이 가지고 있는 문서의 수를 반환해주는 api 함수이다.

`pk`의 역할은 `_id`가 대신한다. `_id` 값을 따로 값을 설정하지 않으면 자동으로 생성된다.

##### MongoDB는 사전 정의가 없다.

document의 묶음을 collection 이라고 한다. MongoDB으 document는 스키마가 없다보니 제약이 없다. 가령, 서로 다른 구조의 키를 가지고 있어도 문제가 없다.

이러한 이점으로 인해 개발할 때 더 편하다. 이 때문에 상당히 빠르게 개발할 수 있다는 장점이 있다. 스키마가 없음으로 인해 너무 자유롭다.다만 통제가 잘 안된다.

##### 인덱스를 쓰는 이유

인덱스는 데이터가 많을 때 경제성이 뛰어나다. 인덱스의 구조는 B-트리이다.

###### MongoDB의 특성

Scale Up VS Scale Out

Scale Out을 했을 때는 Sharding 샤딩이 필요하다. Sharding(샤딩)은 분산데이터베이스를 구현할 때 사용하는 방법이며, Sharding을 통해서 옆으로 계속 확장할 수 있다.

Shard1, Shard2, Shard3

몽고디비는 Scale Out하기에 좋은 구조를 가지고 있다.

데이터의 구조가 내포형이라면,(카탈로그 형태라면) 문서형 데이터베이스를 쓰는 게 좋다.이 지점에서는 관계형 DB보다 훨씬 큰 이점을 지니고 있다.



### Morphia

  Morphia는 유형에 안전한 MongoDB를 위한 오브젝트 맵핑 라이브러리인 오픈 소스 문서 지향 데이터베이스입니다. 이 기사는 오브젝트로 맵핑 및 오브젝트에서 맵핑 문서의 이점을 설명하고, 이 용도를 위해 Morphia를 사용하는 방법을 보여줍니다. 그 다음에 MongoDB로 맵핑된 Java™ 도메인 모델을 지속하고 로드하고 삭제하며 쿼리하는 방법을 시연합니다.

Morphia는 MongoDB에서 문서로 저장된 POJO를 지속하고 검색하고 삭제하며 쿼리할 수 있는 Apache 라이센스 부여된 Google Code 프로젝트이다. Morphia는 Mongo Java 드라이버와 관련된 랩퍼와 어노테이션 세트를 제공하여 이를 완수한다. Morphia는 JPA(Java Persistence API) 또는 JDO(Java Data Objects) 구현과 같은 오브젝트 지향적 맵퍼와 개념적으로 유사하다. 이 기사에서 MongoDB로 맵핑된 Java 도메인 모델로 Morphia를 사용하는 방법을 보여줄 것이다. 



#### 참조

- [데이터 기술 자료](https://kdata.or.kr/info/info_04_view.html?field=&keyword=&type=techreport&page=82&dbnum=152747&mode=detail&type=techreport)

- [Database/Data | NoSQL - MongoDB 란 무엇인가?](https://mchaemil.github.io/2019/12/24/DB-nosql-what-is-the-nosql-and-mongodb.html)

