# `@Transactional` 애노테이션을 달아주면 스프링 내부적으로 어떻게 동작할까?

AOP 프록시를 통해 활성화 되고 내부에는 PlatformTransactionManager 구현과 TransactionInterceptor 를 이용하여 메서드 호출을 중심으로 AOP 프록시를 생성합니다. Transactional 어노테이션을 선언적 트랜잭션이라 합니다.

사용할 때 속성을 설정하지 않으면 기본으로 설정되어있는 속성들로 설정되어 생략이 가능합니다.

**트랜잭션의 동작방식에 영향을 줄수 있는 4가지 속성으로 TransactionAttributes 프로퍼티를 통해 전파(propagation), 격리수준(isolation level), 제한시간(time out), 읽기 전용(read only)을 설정할 수 있습니다.**

#### 참조

- https://docs.spring.io/spring-framework/docs/2.0.x/reference/transaction.html
- https://docs.spring.io/spring-framework/docs/2.0.x/reference/aop.html#aop-understanding-aop-proxies
- Toby Spring book
- https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth