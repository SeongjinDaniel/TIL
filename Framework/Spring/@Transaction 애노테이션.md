# @Transaction 애노테이션



스프링에서 트랜잭션 애노테이션을 사용했는데 롤백이 제대로 되지 않는 현상으로 인하여 조금 더 트랜잭션의 개념을 알아보고 이유를 찾아보고자 한다.

@Transactional 만 붙이면 롤백이 안되고, @Transactional(rollbackFor = Exception.class)를 사용해야 롤백이 된다.



#### 트랜잭션이란?

트랜잭션의 4가지 성질은 ACID이다.  

**원자성(Atomic)**

- 한 트랜잭션 내에서 실행한 작업을 하나의 단위로 처리한다. 즉, 모두 성공 또는 실패.

**일관성(Consistency)**

- 트랜잭션은 일관성 있는 데이터베이스 상태를 유지한다.

**격리성(Isolation)**

- 동시에 실행되는 트랜잭션들이 서로 영향을 미치지 않도록 격리한다.

**영속성(Durability)**

- 트랜잭션을 성공적으로 마치면 결과가 항상 저장되어야 한다.



#### 트랜잭션 옵션

**1. isolation**

- 트랜잭션에서 일관성없는 데이터 허용 수준을 설정한다

**2. propagation**

- 트랜잭션 동작 도중 다른 트랜잭션을 호출할 때, 어떻게 할 것인지 지정하는 옵션이다

**3. noRollbackFor**

- 특정 예외 발생 시 rollback하지 않는다.

**4. rollbackFor**

- 특정 예외 발생 시 rollback한다.

**5. timeout**

- 지정한 시간 내에 메소드 수행이 완료되지 않으면 rollback 한다. (-1일 경우 timeout을 사용하지 않는다)

**6. readOnly**

- 트랜잭션을 읽기 전용으로 설정한다.



#### 참조

- https://velog.io/@kdhyo/JavaTransactional-Annotation-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90-26her30h