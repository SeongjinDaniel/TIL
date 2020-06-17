# "용어사전"&"What is it"

## 1. [서블릿2.3의 새로운 특징, 라이프 사이클과 속성 이벤트!](https://javacan.tistory.com/entry/69)

서블릿 2.3에서 추가됨

- ServletContextEvent
- HttpSessionEvent
- **ServletContextEvent와 ServletContextListener**

![image](https://user-images.githubusercontent.com/55625864/84773453-6432ab00-b017-11ea-877a-cbe81c61381c.png)



콘텍스트의 초기화는 사용자들이 웹브라우저를 사용하여 웹어플리케이션을 실행하는 시점보다 이전에 발생하기 때문에, 웹 어플리케이션에서 사용하는 데이터베이스 커넥션이나 객체의 풀 또는 각종 설정 정보등을 초기화하기에 가장 알맞은 시점이다. 또한, 콘텍스트의 종료는 서블릿 엔진을 종료하기 이전에 수행되기 때문에 어플리케이션에서 사용하고 있는 자원을 반납하기에 가장 알맞은 시점이 된다.



## [Spring] @PostConstruct , @PreDestroy



@postConstruct

\- 객체의 초기화 부분
\- 객체가 생성된 후 별도의 초기화 작업을 위해 실행하는 메소드를 선언한다.
\- @PostConstruct 어노테이션을 설정해놓은 init 메소드는 WAS가 띄워질 때 실행된다.


 @PreDestory

\- 마지막 소멸 단계
\- 스프링 컨테이너에서 객체(빈)를 제거하기 전에 해야할 작업이 있다면 메소드위에 사용하는 어노테이션.
\- close() 하기 직전에 실행 -> ((AbstractApplicationContext) context).close()


 

< 예제 >
//초기화 메소드
@PostConstruct
public void init(){
  System.out.println("초기화 메소드!!");
}
//소멸 메소드
@PreDestroy
public void destory(){
  System.out.println("종료 직전!!");    
}


(!) xml에서 어노테이션을 사용 안하고 bean에 지정 하는 방법
 \- init-method 와 destroy-method를 사용

// 초기화 메소드
public void init() {
System.out.println("초기화 메소드!!");
}

// 소멸 메소드
public void destory() {
  System.out.println("종료 직전!!"); 
}

xml
<bean id="지정 아이디" class="패키지.클래스명" init-method="init" destroy-method="destory"></bean>

java의 implements InitializingBean, DisposableBean도 같은 기능을 한다.



출처: https://goddaehee.tistory.com/46 [갓대희의 작은공간]





## [[Spring\] @Controller와 @RestController 차이](https://mangkyu.tistory.com/49)



- 블로그 글이 좋아서!! Controller와 RestController의 차이 확인!