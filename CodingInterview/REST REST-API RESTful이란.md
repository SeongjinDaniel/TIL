# REST

### REST란?

- REST 정의
  - "Representational State Transfer"의 약자
    - *자원(Resource)을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든것을 의미한다.*
      - 자원(resource)의 표현(representation)
        - 자원: 해당 소프트웨어가 관리하는 모든 것
          -> Ex) 문서, 그림, 데이터, 해당 소프트웨어 자체 등
        - 자원의 표현: 그 자원을 표현하기 위한 이름
          -> Ex) DB의 학생 정보가 자원일 때, ‘students’를 자원의 표현으로 정한다.
  - *월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식*
    - REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.
    - REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.
- REST의 구체적인 개념
  - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
  - 즉, REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.
  - 웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.
  - CRUD Operation
    - Create : 생성(POST)
    - Read : 조회(GET)
    - Update : 수정(PUT)
    - Delete : 삭제(DELETE)

#### REST 장단점

- **장점**
  - HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구출할 필요가 없다.
  - HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해준다.
  - HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
  - Hypermedia API의 기본을 충실히 지키면서 범용성을 보장한다.
  - REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
  - 여러가지 서비스 디자인에서 생길 수 있는 문제를 최소화한다.
  - 서버와 클라이언트의 역할을 명확하게 분리한다.
  - **구성 요소 상호작용의 규모 확장성(scalability of component interactions)**
  - **인터페이스의 범용성 (Generality of interfaces)**
  - **구성 요소의 독립적인 배포(Independent deployment of components)**
  - **중간적 구성요소를 이용해 응답 지연 감소, 보안을 강화, 레거시 시스템을 인캡슐레이션 (Intermediary components to reduce latency, enforce security and encapsulate legacy systems)**\

- **단점**
  - 표준이 존재하지 않는다.
  - 사용할 수 있는 메소드가 4가지 밖에 없다.
    - HTTP Method 형태가 제한적이다.
  - 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 값이 왠지 더 어렵게 느껴진다.
  - 구형 브라우저가 아직 제대로 지원해주지 못하는 부분이 존재한다.
    - PUT, DELETE를 사용하지 못하는 점
    - pushState를 지원하지 않는 점

#### REST가 필요한 이유

- ‘애플리케이션 분리 및 통합’
- ‘다양한 클라이언트의 등장’
- 최근의 서버 프로그램은 다양한 브라우저와 안드로이폰, 아이폰과 같은 모바일 디바이스에서도 통신을 할 수 있어야 한다.
- 이러한 멀티 플랫폼에 대한 지원을 위해 서비스 자원에 대한 아키텍처를 세우고 이용하는 방법을 모색한 결과, REST에 관심을 가지게 되었다.



일반적으로 **REST**라고 하면 좁은 의미로 **HTTP**를 통해 **CRUD**를 실행하는 **API**를 뜻합니다





### REST API란?

아래 url 참고

### RESTful이란?

아래 url 참고





자세한 내용은 아래 url을 참고

#### 참고

- https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html
- https://ko.wikipedia.org/wiki/REST