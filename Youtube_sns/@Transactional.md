# @Transactional



transaction `begin`, `commit`을 자동 수행해준다.

예외를 발생시키면, `rollback` 처리를 자동 수행해준다.



데이터 베이스로 하나의 테이블에 데이터를 넣고 빼고 수정하고 막하고 커밋(Commit)을 안하면 넣고 빼고 수정했던 모든짓들이 다 적용이 안되어있다. 이런것 처럼 하나의 업무로 함께 진행해야 하는것이다.



클래스, 메서드위에 **@Transactional** 이 추가되면, 이 클래스에 트랜잭션 기능이 적용된 프록시 객체가 생성된다.



스프링에서는 @Transactional을 사용한 Checked Exception은 롤백되지 않습니다. 이유는 스프링이 EJB에서의 관습을 따르기 때문이라고 합니다.
Unchecked Exception은 Rollback 됩니다. 그래서 결국 Exception을 Checked 또는 Unchecked를 구분하여 로직의 Rollback 여부를 판단하여, 구현할 수 있습니다.

하지만, 모든 exception에 대해 롤백하게할수도 있다.

```java
// Exception예외로 롤백을 하려면 다음과 같이 지정하면됩니다. checked, unchecked exception 모두 포함
@Transactional(rollbackFor = Exception.class)
// 여러개의 예외를 지정할 수도 있습니다. 
@Transactional(rollbackFro = {RuntimeException.class, Exception.class})
```

추가적으로 특정 예외가 발생하면 롤백이 되지 않도록 지정하는 방법입니다.

```java
@Transactional(noRollbackFor={IgnoreRollbackException.class})
```

![image](https://user-images.githubusercontent.com/55625864/92324192-63d80800-f07a-11ea-908b-2a758be4a2bc.png)



**@Transactional을 써주는 이유?**

 companyDAO.saveDivisionData 에서 처리한 쿼리문이 정상적으로 완료가 되고, companyDAO.saveextensionTarget 에서 처리 도중 에러가 났을 때

 companyDAO.saveDivisionData 에서 처리한 쿼리를 자동 rollback 해주기 위해 사용된다.



만약 저 어노테이션을 써주지 않는다면, 위에꺼는 정상적으로 완료가 되었기 때문에 직접 save한 division 데이터를 복구 시켜놔야함...





\- 인터페이스를 구현한 클래스로 선언된 빈은 인터페이스 메소드에 한해서 트랜잭션이 적용됨

\- 인터페이스에 붙은 @Transactional 선언은 인터페이스 내의 모든 메소드에 적용됨

\- 동시에 메소드 레벨에도 @Transactional을 지정할 수 있다. 메소드 선언 > 인터페이스 선언

\- 클래스의 @Transactional > 인터페이스의 @Transactional

\- @Transactional 적용 대상은 미리 결정하고 애플리케이션 안에서 통일하는게 좋음. 인터페이스와 클래스 양쪽에 불규칙하게 @Transactional이 혼용되는 건 바람직하지 못함



#### **트랜잭션의 성질**

**1. 일관성(Consistency)** - 트랜잭션은 언제나 일관성 있는 데이터 베이스 상태를 유지하는 것을 의미.

**2. 원자성(Atomicity)** - 하나의 트랜잭션의 속한 작업들이 모두 실패인지 성공인지 보장을 의미 즉 하나로 간주

**3. 고립성(lsolation)** - 트랜잭션을 수행 시 다른 트랜잭션의 작업이 끼어들어들지 못하게 보장하는 것을 의미

**4. 지속성(Durability)** - 트랜잭션을 성공적으로 마치면 결과가 영원히 반영 되어야 하는걸 의미



#### 참고

- [@Transactional 이란? 사용이유](https://crosstheline.tistory.com/96)
- [[ Spring \] @Transactional 에 대하여](https://itjava.tistory.com/118)
- [[Spring] Transactional 정리 및 예제](https://goddaehee.tistory.com/167)
- [[Spring] @Transactional 사용시 주의해야할 점](https://mommoo.tistory.com/92)
- [Spring Transaction Exception 상황에서 Rollback 처리하기](https://interconnection.tistory.com/122)
- [[Spring] @Transactional 롤백은 언제 되는 걸까? - 예외가 발생했는데도 DB 반영이 된다고?](https://pjh3749.tistory.com/269)
- [응? 이게 왜 롤백되는거지?](https://woowabros.github.io/experience/2019/01/29/exception-in-transaction.html)