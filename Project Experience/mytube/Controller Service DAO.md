# Controller Service DAO

### Controller

**사용자(Client)의 요청(Request)을 어떻게 처리 할 지(Handling) 결정**

- 클라이언트에서 요청이 들어올 때, 해당 요청을 수행할 **비즈니스 로직(Business Logic)을 제어**하는 객체이다. 스프링에서는 컨트롤러에서 세부적으로 서비스 레이어(Service Layer)를 만들어 해당 요청사항을 객체 지향적인 방식으로 좀 더 세분화하여 관리한다.

### Service

**비즈니스 로직을 수행**

- 서비스 레이어(Service Layer)단에서 **세분화된 비즈니스 로직을 처리**하는 객체이다.
- Service의 역할은 Dao가 DB에서 받아온 데이터를 전달받아 가공하는 것이다.

- Controller에서 많은 비즈니스 로직들을 수행하게 되면 코드들이 길어질 것이고 가독성이 매우 떨어진다. 그래서 Service라는 속성을 통해 요청과 수행을 분리한다.

### DAO(Data Access Object)

**DB에 접근하는 객체를 말한다.**

DAO는 데이터 액세스 개체를 나타냅니다. 일반적으로 DAO 클래스는 두 가지 개념을 담당합니다. *지속성 계층의 세부 정보를 캡슐화*하고 *단일 엔터티에 대한 CRUD 인터페이스를 제공*합니다.

- DB를 사용해 데이터를 조회하거나 조작하는 기능을 전담하도록 만든 객체이다.
- DB에 접근하는 객체를 말한다.
- DB를 사용해 데이터를 조회하거나 조작하는 기능을 담당하는 것들을 DAO라고 한다.
- DAO의 사용 이유는 효율적인 커넥션 관리와 보안성 때문이다.
- Database의 data에 access하는 트랜잭션 객체이다.
- Domain Logic(도메인 로직: 비즈니스 로직이나 DB와 관련없는 코드들)을 persistence mechnism과 분리하기 위해 사용한다.



#### persistence layer

Database에 data를 CRUD(Create, Read, Update, Drop)하는 계층

#### 비즈니스 로직(Business Logic)

컴퓨터 프로그램에서 실세계의 규칙에 따라 데이터를 생성, 표시 , 저장, 변경하는 부분을 일컫는다. 사용자에게 보여지지 않는 부분에서 데이터를 처리하는 코드라고 보면 된다.



#### 참고

- https://m.blog.naver.com/jysaa5/221751719334