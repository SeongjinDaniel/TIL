# Component&Autowired

스프링부트의 경우 @Component, @Service, @Controller, @Repository, @Bean, @Configuration 등으로 필요한 빈들을 등록하고 필요한 곳에서 @Autowired를 통해 주입받아 사용하는 것이 일반적이다.

 

다음 그림과 같이 @Service, @Controller, @Repository는 모두 @Component를 상속받고 있으며 해당 어노테이션으로 등록된 클래스들은 스프링 컨테이너에 의해 자동으로 생성되어 스프링 빈으로 등록된다.



@Controller @Service @Repository은 @Component를 상속받고 있다. 결국 이 어노테이션들도 스프링에 빈을 등록하기 위해 사용되는 어노테이션이다. 



@Component 어노테이션과 차이점은 특정한 사용용도를 가진다는 것이다.

@Controller : Spring MVC에서 사용하기 위함. @RequestMapping과 함께 사용할 수 있음

@Service : service layer

@Repository : persistence layer



**[ @Component & @Autowired ]**

스프링부트에서 사용자 클래스를 스프링 빈으로 등록하는 가장 쉬운 방법은 클래스 선언부 위에 Component Annotation을 사용하는 것이다. @Component가 붙은 클래스는 스프링 빈 객체로 등록이 되어 객체 생성/삭제를 스프링에서 관리할 수 있다.



#### 참고

- https://cbw1030.tistory.com/54