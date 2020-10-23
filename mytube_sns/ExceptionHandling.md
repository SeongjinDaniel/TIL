# 예외처리



![image](https://user-images.githubusercontent.com/55625864/90465292-08d18600-e14a-11ea-9da2-b314c79a43f1.png)



위 [그림1]은 예외클래스의 구조이다. 모든 예외클래스는 Throwable 클래스를 상속받고 있으며, Throwable은 최상위 클래스 Object의 자식 클래스이다.

Trowable을 상속받는 클래스는 Error와 Exception이 있다. Error는 시스템 레벨의 심각한 수준의 에러이기 때문에 시스템에 변화를 주어 문제를 처리해야 하는 경우가 일반적이다. 반면에 Exception은 개발자가 로직을 추가하여 처리할 수 있다.

Exception은 수많은 자식클래스를 가지고 있다. 그 중 RuntimeException을 주목해야 한다. RuntimeException은 CheckedException과 UncheckedException을 구분하는 기준이다. Exception의 자식 클래스 중 RuntimeException을 제외한 모든 클래스는 CheckedException이며, RuntimeException과 그의 자식 클래스들을 Unchecked Exception이라 부른다. CheckedException과 UncheckedException에 대해 더 자세히 살펴보자.

![image](https://user-images.githubusercontent.com/55625864/90465513-7978a280-e14a-11ea-8515-30e7c5354935.png)

Checked Exception과 Unchecked Exception의 가장 명확한 구분 기준은 ‘꼭 처리를 해야 하느냐’이다. Checked Exception이 발생할 가능성이 있는 메소드라면 반드시 로직을 try/catch로 감싸거나 throw로 던져서 처리해야 한다. 반면에 Unchecked Exception은 명시적인 예외처리를 하지 않아도 된다. 이 예외는 피할 수 있지만 개발자가 부주의해서 발생하는 경우가 대부분이고, 미리 예측하지 못했던 상황에서 발생하는 예외가 아니기 때문에 굳이 로직으로 처리를 할 필요가 없도록 만들어져 있다.



# Java 예외(Exception) 처리에 대한 작은 생각

 [Nextree](http://www.nextree.co.kr/author/nextree/) Dec 31, 2013 [10 Comments](http://www.nextree.co.kr/p3239/#disqus_thread)

일상생활에서도 기본적인 것은 고민하지 않고 습관처럼 사용하는 경우가 있다. 초급 개발자인 나에게 ‘예외(Exception)’이 바로 그런 것이었다.

처음 JAVA수업 때 강사님께 "왜 로직을 try문으로 감싸고, 또 catch(e)는 무엇인가요?"라는 질문을 한 적이 있다. 돌아온 대답은 "이렇게 안하면 에러가 나니까."였다. 나는 이것을 안 하면 어떤 일이 벌어지는지 언제 어떻게 사용해야 하는지도 모른 채 강사님의 코드를 따라 치기 바빴다. 입사 후 공부를 하면서도 Runtime Exception과 Checked Exception은 이론 그 이상으로 활용하지 못했었다.

하지만 최근 약 4개월 반 동안 진행했던 한 프로젝트에서 수석님들께 배우며 예외(Exception)에 대해 큰 깨달음을 얻었고, 꼭 이 깨달음을 글로 남기고 싶었다. 이 글을 통해 초급 개발자들이 예외처리를 할 때, 이해하고 생각하며 적용할 수 있기를 바란다.

## 1. 예외란? (Error vs Exception)

먼저 오류(Error)와 예외(Exception)의 개념을 정리하고 넘어가자.

오류(Error)는 시스템에 비정상적인 상황이 생겼을 때 발생한다. 이는 시스템 레벨에서 발생하기 때문에 심각한 수준의 오류이다. 따라서 개발자가 미리 예측하여 처리할 수 없기 때문에, 애플리케이션에서 오류에 대한 처리를 신경 쓰지 않아도 된다.

오류가 시스템 레벨에서 발생한다면, 예외(Exception)는 개발자가 구현한 로직에서 발생한다. 즉, 예외는 발생할 상황을 미리 예측하여 처리할 수 있다. 즉, 예외는 개발자가 처리할 수 있기 때문에 예외를 구분하고 그에 따른 처리 방법을 명확히 알고 적용하는 것이 중요하다.

## 2. 예외클래스

![img](http://www.nextree.co.kr/content/images/2016/09/Exception-Class.png)[그림1] 예외클래스의 구조

위 [그림1]은 예외클래스의 구조이다. 모든 예외클래스는 Throwable 클래스를 상속받고 있으며, Throwable은 최상위 클래스 Object의 자식 클래스이다.

Trowable을 상속받는 클래스는 Error와 Exception이 있다. Error는 시스템 레벨의 심각한 수준의 에러이기 때문에 시스템에 변화를 주어 문제를 처리해야 하는 경우가 일반적이다. 반면에 Exception은 개발자가 로직을 추가하여 처리할 수 있다.

Exception은 수많은 자식클래스를 가지고 있다. 그 중 RuntimeException을 주목해야 한다. RuntimeException은 CheckedException과 UncheckedException을 구분하는 기준이다. Exception의 자식 클래스 중 RuntimeException을 제외한 모든 클래스는 CheckedException이며, RuntimeException과 그의 자식 클래스들을 Unchecked Exception이라 부른다. CheckedException과 UncheckedException에 대해 더 자세히 살펴보자.

## 3. Checked Exception과 Unchecked(Runtime) Exception

![img](http://www.nextree.co.kr/content/images/2016/09/exception-table.png)[표1] Checked Exception과 Unchecked Exception

Checked Exception과 Unchecked Exception의 가장 명확한 구분 기준은 ‘꼭 처리를 해야 하느냐’이다. Checked Exception이 발생할 가능성이 있는 메소드라면 반드시 로직을 try/catch로 감싸거나 throw로 던져서 처리해야 한다. 반면에 Unchecked Exception은 명시적인 예외처리를 하지 않아도 된다. 이 예외는 피할 수 있지만 개발자가 부주의해서 발생하는 경우가 대부분이고, 미리 예측하지 못했던 상황에서 발생하는 예외가 아니기 때문에 굳이 로직으로 처리를 할 필요가 없도록 만들어져 있다.

또한 예외를 확인할 수 있는 시점에서도 구분할 수 있다. 일반적으로 컴파일 단계에서 명확하게 Exception 체크가 가능한 것을 Checked Exception이라 하며, 실행과정 중 어떠한 특정 논리에 의해 발견되는 Exception을 Unchecked Exception이라 한다. 따라서 컴파일 단계에서 확인할 수 없는 예외라 하여 Unchecked Exception이며, 실행과정 중 발견된다 하여서 Runtime Exception이라 하는 것이다.



그리고 한 가지 더 인지하고 있으면 좋은 것이 있다. 바로 예외발생시 트랜잭션의 roll-back 여부이다. 기본적으로 Checked Exception은 예외가 발생하면 트랜잭션을 roll-back하지 않고 예외를 던져준다. 하지만 Unchecked Exception은 예외 발생 시 트랜잭션을 roll-back한다는 점에서 차이가 있다. 트랜잭션의 전파방식 즉, 어떻게 묶어놓느냐에 따라서 Checked Exception이냐 Unchecked Exception이냐의 영향도가 크다. roll-back이 되는 범위가 달라지기 때문에 개발자가 이를 인지하지 못하면, 실행결과가 맞지 않거나 예상치 못한 예외가 발생할 수 있다. 그러므로 이를 인지하고 트랜잭션을 적용시킬 때 전파방식(propagation behavior)과 롤백규칙 등을 적절히 사용하면 더욱 효율적인 애플리케이션을 구현할 수 있을 것이다.

## 4. 예외 처리 방법

![image](https://user-images.githubusercontent.com/55625864/90470793-5accd880-e157-11ea-84f9-a918d488112f.png)

[그림2] 예외 처리 방법 위 [그림 2]는 예외를 처리하는 일반적인 방법 3가지이다. 예외 처리 방법에는 예외가 발생하면 다른 작업 흐름으로 유도하는 예외 복구와 처리를 하지 않고 호출한 쪽으로 던져버리는 예외처리 회피, 그리고 호출한 쪽으로 던질 때 명확한 의미를 전달하기 위해 다른 예외로 전환하여 던지는 예외 전환이 있다.

### 4.1. 예외 복구

```java
int maxretry = MAX_RETRY;  
while(maxretry -- > 0) {  
    try {
        // 예외가 발생할 가능성이 있는 시도
        return; // 작업성공시 리턴
    }
    catch (SomeException e) {
        // 로그 출력. 정해진 시간만큼 대기
    } 
    finally {
        // 리소스 반납 및 정리 작업
    }
}
throw new RetryFailedException(); // 최대 재시도 횟수를 넘기면 직접 예외 발생  
```

예외복구의 핵심은 예외가 발생하여도 애플리케이션은 정상적인 흐름으로 진행된다는 것이다. 위 [리스트 1]은 재시도를 통해 예외를 복구하는 코드이다. 이 예제는 네트워크가 환경이 좋지 않아서 서버에 접속이 안되는 상황의 시스템에 적용하면 효율 적이다. 예외가 발생하면 그 예외를 잡아서 일정 시간만큼 대기하고 다시 재시도를 반복한다. 그리고 최대 재시도 횟수를 넘기면 예외를 발생시킨다. 재시도를 통해 정상적인 흐름을 타게 한다거나, 예외가 발생하면 이를 미리 예측하여 다른 흐름으로 유도시키도록 구현하면 비록 예외가 발생하였어도 정상적으로 작업을 종료할 수 있을 것이다.

### 4.2. 예외처리 회피

```java
public void add() throws SQLException {  
    ... // 구현 로직
}
```

위 [리스트 2]는 간단해 보이지만 아주 신중해야하는 로직이다. 예외가 발생하면 throws를 통해 호출한쪽으로 예외를 던지고 그 처리를 회피하는 것이다. 하지만 무책임하게 던지는 것은 위험하다. 호출한 쪽에서 다시 예외를 받아 처리하도록 하거나, 해당 메소드에서 이 예외를 던지는 것이 최선의 방법이라는 확신이 있을 때만 사용해야 한다.

### 4.3. 예외 전환

```java
catch(SQLException e) {  
   ...
   throw DuplicateUserIdException();
}
```

예외 전환은 위 [리스트 3]에서 처럼 예외를 잡아서 다른 예외를 던지는 것이다. 호출한 쪽에서 예외를 받아서 처리할 때 좀 더 명확하게 인지할 수 있도록 돕기 위한 방법이다. 어떤 예외인지 분명해야 처리가 수월해지기 때문이다. 예를 들어 Checked Exception 중 복구가 불가능한 예외가 잡혔다면 이를 Unchecked Exception으로 전환하여서 다른 계층에서 일일이 예외를 선언할 필요가 없도록 할 수도 있다.



이상으로 예외를 처리하는 3가지 방법을 알아봤다. 하지만 예외를 처리하는 방법보다도 초급 개발자가 가장 잊지 말아야 할 것은 예외를 잡고 아무런 처리도 하지 않는 것은 정말 위험한 행위라는 것이다. try/catch문으로 예외를 잡아놓고 catch를 비워두면 물론 컴파일 오류는 나지 않겠지만, 예외가 발생했을 때 그 원인을 파악하기가 어려워 개발은 물론 유지보수에 아주 치명적인 민폐를 끼치는 일이라고 생각한다. 따라서 어떤 처리를 해야 하는지 모르더라도 무작정 catch하고 무시하거나, throw해버리는 행위를 할 때는 더욱 신중해야 할 것이다.



---

---

- 깨끗한 코드는 읽기도 좋아야 하지만 안정성도 높아야 한다. 이 두가지의 목표는 대립되는 목표가 아니다.
- 오류 처리를 프로그램 논리와 분리하면 독립적인 추록이 가능해지며 코드 유지보수성도 크게 높아진다.



-----

---

자바에서 예외(Exception)은 크게 checked 예외와 unchecked 예외로 나뉘어진다. **checked** 예외는 코드에서 명시적으로 try-catch-finally 예외 처리를 해야하는 것을 의미하며, **unchecked** 예외는 그럴 필요가 없는 것을 의미한다. checked 예외에서 try-catch로 예외를 처리하지 않는 경우에는 메소드에 throws 절을 추가해야 한다.



**자바에서 checked 예외는 java.lang.Exception 을 상속받는 형태이며,** unchecked 예외는 java.lang.RuntimeException을 상속받는 예외이다. checked 예외이든 unchecked 예외이든 두가지 모두 동일한 기능을 수행한다. 따라서, 어느 것이 더 낫다라고 말할 수는 없다. 하지만, 예외 발생시 어떠한 로직을 추가하느냐에 따라서 그 비용적인 측면은 다양할 수 있다.



**IllegalArgumentException**: 메소드의 전달인자 값이 부적절한 경우 발생.
-> Illegal(부적절한) Argument(아규먼트) Exception(예외)
참고 링크: http://bufferoverflow.tistory.com/entry/파라미터-parameter-아규먼트-argument

**IllegalStateException**: 객체의 상태가 메소드 호출에는 부적합한 경우 발생.
-> Illegal(부적절한) State(상태) Exception(예외상황)
ex> java.lang.IllegalStateException: getOutputStream() has already been called for this response
-> 해당 response는 getOutputStream() 메소드를 호출하기 위한 준비가 되어있지 않습니다.

**NullPointerException**: null 이 금지된 상황에서 전달인자 값이 null인 경우 발생한다.
-> Null(null) Pointer(포인터) Exception(예외상황)

**IndexOutOfBoundsException**: index 값이 범위를 벗어난 경우 발생한다.
-> Index(인덱스) OutOfBounds(범위이탈) Exception(예외상황)

**ConcurrentModificationException**: 금지된 곳에서 객체를 동시에 수정(concurrent modification)하는 것이 감지된 경우 발생한다.
-> Concurrent(동시) Modification(수정) Exception(예외상황)
참고 링크 : http://wonsama.tistory.com/194

**UnsupportedOperationException**: 객체가 메소드를 지원하지 않는 경우 발생한다.
-> Unsupported(지원하지 않는) Operation(객체) Exception(예외상황)
참고 링크: http://younghoe.info/482



#### 참고 

- https://meetup.toast.com/posts/47
- http://java-performance.info/throwing-an-exception-in-java-is-very-slow/
- https://groups.google.com/g/ksug/c/UbBu-5n79F4
- https://jobc.tistory.com/134
- **[Java 예외(Exception) 처리에 대한 작은 생각Java 예외(Exception) 처리에 대한 작은 생각](http://www.nextree.co.kr/p3239/)** 
- [Exception Handling in Spring MVC](https://baekjungho.github.io/spring-exceptionhandler/)
- [Exception 처리, 어떻게 하는게 좋을까?](https://umbum.dev/896)
- [Java에서 Checked Exception은 언제 써야 하는가?](https://blog.benelog.net/1901121)
- [자바의 런타임 계열 예외와 checked 예외](https://hamait.tistory.com/213)
- [Java Exception의 종류](https://codepedia.tistory.com/entry/JavaException)
- [[Java\] Error(에러)와 Exception(예외) 그리고 자주 보이는 Exception](https://java119.tistory.com/44)
