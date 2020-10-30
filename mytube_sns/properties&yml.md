# .properties vs .yml



스프링 부트는 설정파일을 밖으로 빼낼 수 있게 해져있다. properties, yml, Environment, command line 등을 사용하여 정의할 수 있다. 정의된 설정 값은 @Value로 주입받거나 스프링이 제공하는 Environment interface로 접근할 수 있다.



**스프링 부트는 내부적으로 YML 파일을 읽어서 Properties로 바꾸고 궁극적으로 이를 Environment 로 들어가게된다.**
**@Value 어노테이션은 그냥 Environment에 있는 값을 불러오는 것이다. YML 파일을 읽어들이는 것이 아니다.**

그리고 YML 파일을 읽어서 properties로 바꾸기 때문에 같은 이름의 yml 파일과 properties 파일이 동시에 있을 경우 yml이 우선순위가 좀더 높다.

spring.profiles를 쓰면 development, local 환경을 분리할 수 있다.



### .properties 

#### 장점

- escape문자열 필요 없다.
- 선언부가 필요 없다.
- 단순하다.

#### 단점

- 가독성이 떨어질 수 있다.
- 키-값 1:1 매칭



### .yml

#### 장점

- escape 문자열 필요 없다

- 1:N 형식 매핑이 가능하다

- 선언부가 필요 없다.

- profile과 관련해서 spring의 지원을 받을 수 있다.

- 리스트로 표현하고자 할 때는 "-" (대쉬) 하나로 사용할 수 있다.

- —(대쉬 3번)의 사용으로 다른 파일에서 불러온것처럼 사용할 수 있다.

  ```yml
  spring:
    profiles:
      active: local # 기본 환경 선택
   
  # local 환경
  ---
  spring:
    profiles: local
    datasource:
      data: classpath:data-h2.sql # 시작할때 실행시킬 script
    jpa:
      show-sql: true
      hibernate:
        ddl-auto: create-drop
    h2:
      console:
        enabled: true
   
  # 운영 환경
  ---
  spring:
    profiles: set1
  server:
    port: 8081
  ```

  위와 같이 spring.profiles.active: local로 하면 profiles가 :local인 설정이 적용되고 set1으로하면 set1인 설정이 적용된다. default 환경을 설정해둘 수 있고 active되는 것마다 바꾸면 되니 개발하고 배포할 때 아주 편리하게 할 수 있다.

#### 단점

- yaml 파일의 단점은 `@PropertySource` 어노테이션으로 불러 올 수 없다.
  해당 어노테이션을 사용 하려면 프로퍼티 파일을 사용해야된다.





#### 참조

- [Spring Property 관리](https://supawer0728.github.io/2018/03/11/Spring-Property/)

- Spring boot 설정 파일 yaml 사용법 (설정 파일을 읽어서 bean으로 필요할 때 사용하는 방법)

  