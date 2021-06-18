# Hibernate-validator를 사용하는 이유

하이버네이트 Validator는 JSR-303(Bean Validation - 데이터 유효성 검사를 좀더 효율적으로 할 수 있는 자바의 표준 기술)이라는 자바 빈 검증용 표준의 구현체이다. Member라는 클래스의 String name; 코드를 보자. 



```java
@NotNull 
@Size(min = 1, message = "입력하세요.") 
String name; 
```



이렇게 @NotNull이나 @Size라는 애노테이션을 제공하는 것은 javax.validation 패키지이고, 이 패키지는 validation-api.jar에 들어있다. 이러한 애노테이션을 사용해서 실제로 검증을 수행하는 검증기 구현체를 hibernate-validator가 제공한다.



하이버네이트 밸리데이터는 이메일 주소 형식, 신용카드 형식, 안전한 HTML인지 등등 다양한 검증 기능을 제공한다.



참고) 

- [Bean Validation](https://www.youtube.com/watch?v=zvuhOz8VhhI&feature=youtu.be) - 24분27초 부터 보시면 됩니다

- [Validation 어디까지 해봤니?](https://meetup.toast.com/posts/223)

### 그럼 Hibernate란 무엇인가?

 Object Relation Mapping(ORM - 객체 관계 매핑) Framework 중 하나이다.
객제지향 프로그래밍과 관계형 데이터베이스의 차이로 인해 발생하는 제약사항을 해결하는 해결책으로 본다.
데이터베이스는 데이터들의 집합 개념을 기반으로 하기 때문에 객체지향 개발방식과 근본적으로 다른점이 있어
객체 간 관계를 데이터베이스에 그대로 저장하기 어려운 문제가 있는 제약 사항이 있다.



한국에서는 거의 MyBatis가 대세를 이루지만 해외의 경우 높은 생산성등을 이유로 Hibernate가 거의 대세를 이룬다.

그러나, 한국에서 안사용하는 이유 처럼, Hibernate는 자체적으로 쿼리를 생성하고, OR Mapper로써, 객체들을 DB에서 로딩할때, 레퍼런스된 객체등을 로딩하는등, 제대로 특성을 이해하고 사용하지 않으면 장애를 일으키는 경우가 많지 않기 때문에, 해외에 비해서 한국에서는 많이 사용되지 않는다. (SI에서 기피)

이글에서는 하이버네이트에 대한 간단한 사용법에 대해서 소개하고자 한다.

하이버네이트는 자바 기반의 ORM (Object Relationship Mapper)이다. 쉽게 이야기 해서, 자바 객체를 RDBMS의 하나의 ROW로 맵핑해준다.

이 ORM 개념은 상당히 오래전부터 나왔는데, 처음의 시초는 EJB Entity Beans라고 할 수 있는데, 이 EJB는 여러가지 강력한 기능을 가졌음에도 불구하고, 사용법이 너무 어려워서, 근래에는 거의 사용되지 않는다. 이렇게 사용법이 어려워서 이를 간편화 하여 사용법은 편하게 하면서도, 더 많은 기능을 지원하게 한것이 ORM인데, 그중에서 대표적인 것이 Hibernate이다.

Hibernate가 개발된후에, Java 스펙에도 ORM의 표준 스펙을 정의했는데 이것이 JPA (Java Persistence API)이다. JPA는 하나의 스펙으로 JPA에 대한 구현체가 필요하다. 실제 구현체는 TopLink, OpenJPA등 여러가지가 있는데, 이렇게 ORM API를 JPA를 통해서 추상화 시켜놓음으로써, 다른 ORM과 쉽게 교체가 가능하게 만든 개념이지만, 실제로 ORM은 거의 Hibernate만 사용되기 때문에, JPA를 사용하는 것은 큰 의미가 없다.

JPA는 기본적으로 JBoss나 Weblogic과 같은 JEE 컨테이너를 가정으로 개발되어서 JTS/JTA, EJB3등과 사용하기에는 좋지만, 컨테이너 없이 Tomcat과 같은 Servlet 컨테이너만 사용할 경우, 큰 이득을 보기 어렵다.



이글 일부는 아래 사이트에서 발췌했습니다.

출처: https://bcho.tistory.com/906 [조대협의 블로그]