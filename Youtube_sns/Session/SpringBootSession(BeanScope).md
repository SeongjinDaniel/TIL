# Spring Boot Session 사용하기 (Bean Scope)



### **[ Spring Bean 구성 요소 ]**

- class: Bean으로 등록할 Java 클래스 
- id: Bean의 고유 식별자 
- scope: Bean을 생성하기 위한 방법(singleton, prototype 등) 
- constructor-arg: Bean 생성 시 생성자에 전달할 파라미터 
- property: Bean 생성 시 setter에 전달할 인수 

 

1. 스프링 Ioc 컨테이너에서는 모든 **빈**들을 **싱글톤 객체**로 생성합니다.(scope 옵션으로 해제 가능)

   (참고로, 객체를 매번 생성하는 타입을 **프로토타입**이라고 합니다.)

   

   자원을 많이 사용하는 db 접근 객체들은 싱글톤으로 사용하는 게 좋은데, 저 선언 하나만으로 싱글톤으로 객체를 관리한다고 합니다..



2. 의존성 주입



3. 라이프 사이클 관리가 용이

-  쉽게 여러 시점에 접근가능합니다.

  어떤 빈들이 만들어졌을 때 추가적인 작업을 할 수 있다. ex) @PostContruct.. (라이프사이클 인터페이스 사용가능)



#### 참고

- [Spring Boot Session 사용하기 (Bean Scope)](https://gofnrk.tistory.com/42)
- [[SpringBoot\] @Bean, @Configuration, @Component 어노테이션](https://mangkyu.tistory.com/75)
