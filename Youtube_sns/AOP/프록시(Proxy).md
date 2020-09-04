# 프록시(Proxy)



마치 자신이 클라이언트가 사용하려고 하는 실제 대상인 것처럼 위장해서 클라이언트의 요청을 받아주는 것을 대리자, 대리인과 같은 역할을 한다고 하여 **프록시(Proxy)**라 부른다. 프록시를 통해 최종적으로 요청을 위임받아 처리하는 실제 오브젝트를 **타깃(tartget)** or **실체(real subject)**라 부른다.

- 프록시의 특징은 타깃과 같은 인터페이스를 구현했다는 것과 프록시가 타깃을 제어할 수 있는 것이다.

- 프록시는 사용 목적에 따라 두 가지로 구분할 수 있다.
  - 클라이언트가 타깃에 접근하는 방법을 제어하기 위해서다.
  - 타깃에 부가적인 기능을 부여해주기 위해서다.

![image](https://user-images.githubusercontent.com/55625864/91586891-fe588d00-e990-11ea-8db1-c75dda451e08.png)

### 데코레이션 패턴

- 데코레이션 패턴은 타깃에 **부가적인 기능을 런타임 시 다이내믹하게 부여해주기 위해 프록시를 사용하는 패턴**을 말한다.
- 데코레이터라 불리는 이유는 마치 케익을 여러 겹으로 포장하고 그 위에 장식을 붙이는 것처럼 실제 내용물은 동일 하지만 부가적인 효과를 줄 수 있기 때문이다.
- 그래서 프록시를 여러 개 쓸 수 있고 순서를 정해서 단계적으로 위임하면 된다.
- 데코레이터 패턴은 인터페이스를 통해 위임하는 방식이므로 어느 데코레이터에서 타깃으로 연결될지 코드 레벨에선 미리 알 수 없다.
- 데코레이터 패턴은 타깃의 코드에 손대지 않고, 클라이언트가 호출하는 방법도 변경하지 않은 채로 새로운 기능을 추가할 때 유용하다.
- 소스코드를 출력하는 기능을 핵심기능으로 가지고 여러 데코레이터를 부여한다면 다음과 같이 조합할 수 있다.

![image](https://user-images.githubusercontent.com/55625864/91587204-6909c880-e991-11ea-9801-59ccdaf7ac68.png)



### 프록시 패턴

- 일반적으로 말하는 프록시는 클라이언트와 사용 대상 사이의 대리 역할을 맡은 오브젝트를 두는 방법을 말한다.
- 프록시 패턴의 프록시는 프록시를 사용하는 방법 중에서 타깃에 대한 접근 방법을 제어하려는 목적을 가진 경우를 말한다.
- 프록시 패턴의 프록시는 타깃의 기능을 확장하거나 추가하지 않는다. 대신 클라이언트가 타깃에 접근하는 방식을 변경해준다.
- 타깃 오브젝트를 필요한 시점까지 생성하지 않고 있다가 타깃 오브젝트에 대한 레퍼런스가 필요하면 프록시 패턴을 적용하면 된다.(지연 생성)
- 클라이언트에게 타깃에 대한 레퍼런스를 넘겨야 하는데 실제 타깃 오브젝트 대신 프록시를 넘긴다.
- 그리고 해당 타깃을 사용하려 할 때 프록시가 타깃 오브젝트를 생성하고 요청을 위임해 주는 식이다.
- 또는 특별한 상황에서 타깃에 대한 접근권한을 제어하기 위해 사용할 수도 있다.
- 프록시를 만들어 읽기전용으로 강제하고 add, update 등의 메소드를 사용하면 예외를 발생시키면 된다.
- **구조적으로 보면 프록시와 데코레이터 패턴은 유사하지만 프록시는 코드에서 자신이 접근할 타깃 클래스 정보를 직접적으로 알야야 한다.**

![image](https://user-images.githubusercontent.com/55625864/91587240-73c45d80-e991-11ea-8f65-2e240e23629f.png)

앞으로는 타깃과 동일한 인터페이스를 구현하고 클라이언트와 타깃 사이에 존재하면서 기능의 부가 또는 접근 제어를 담당하는 오브젝트는 모두 프록시라 부르겠다.

### 다이내믹 프록시

프록시를 만드는 것은 상당히 번거롭다. 하지만 자바에는 `java.lang.reflect` 패키지 안에 프록시를 손쉽게 만들게 지원해주는 클래스들이 있다. 마치 목프레임워크와 비슷하다. 이를 통해 몇 가지 API를 이용해 프록시처럼 동작하는 오브젝트를 다이내믹하게 생성해 보자. 프록시는 다음의 두 가지 기능으로 구성된다.

- 타깃과 같은 메소드를 구현하고 있다가 메소드가 호출되면 타깃 오브젝트로 위임한다.
- 지정된 요청에 대해서는 부가기능을 수행한다.



```java
public class UserServiceTx implements UserService {
    UserService userService; //타깃 오브젝트
    ...
    
    public void add(User user) {
        this.userService.add(user); //메소드 구현과 위임
    }
    
    public void upgradeLevels() { //메소드 구현
    	//부가기능 수행
        TransactionStatus status = this.transactionManager.getTransaction(new DefaultTransactionDefinition());
        try {
            userService.upgradeLevels(); //위임
            this.transactionManager.commit(status);
        } catch (RuntimeException e) {
            this.transactionManager.rollback(status);
            throw e;
        }
    }
}
```

위의 코드에서 UserServiceTx 코드는 UserService 인터페이스를 구현하고 타깃으로 요청을 위임하는 트랜잭션 부가기능을 수행하는 코드로 구분할 수 있다. 이렇게 **프록시의 역할은 위임, 부가작업이라는 두 가지 기능으로 구분할 수 있다.** 프록시가 번거로운 이유는 다음과 같다.

- 첫째는 타깃의 인터페이스를 구현하고 위임하는 코드를 작성하기가 번거롭다. 일일이 코드를 만들어 주고 타깃 인터페이스의 메소드가 추가되거나 변경될 때마다 함께 수정해야 한다.
- 둘째는 부가기능 코드가 중복될 가능성이 많다.



#### 리플랙션

이러한 문제들을 해결하기 위해 유용한 것이 다이내믹 프록시이다. **다이내믹 프록시는 리플랙션 기능을 이용해서 프록시를 만들어준다.**

> 리플랙션(java.lang.reflect): 자바의 코드 자체를 추상화해서 접근하도록 만든 것

```java
String name = "Spring";
```

위의 코드에서 길이를 알고 싶으면 name.length()를 호출하면 된다. 자바의 모든 클래스는 그 클래스 자체의 구성정보를 담은 class 타입의 오브젝트를 하나씩 갖고 있다. **'클래스이름.class', getClass() 메소드를 호출하면 클래스 정보를 담은 Class 타입의 오브젝트를 가져올 수 있다.** **클래스 오브젝트를 이용하면 클래스 코드에 대한 메타정보를 가져오거나 오브젝트를 조작할 수 있다.**

- 클래스의 이름이 무엇이고, 어떤 클래스를 상속하고, 어떤 인터페이스를 구현했는지, 어떤 필드를 갖고 있는지, 각각의 타입이 무엇인지, 메소드가 어떤게 있는지 등
- 더 나아가 오브젝트 필드의 값을 읽고 수정할 수도 있고, 원하는 파라미터 값을 이용해 메소드를 호출할 수도 있다.

```java
Method langthMethod = String.class.getMethod("length"); //length 메소드를 가져와 invoke로 실행시키기
int length = lengthMethod.invoke(name) //int length = name.length();
```



#### 프록시 클래스 예제

간단한 프록시 클래스를 만드는 예제를 진행해 보겠다. 프록시는 데코레이터 패턴을 적용해서 타깃인 HelloTarget에 부가기능을 추가했다.

```java
interface Hello { 
    String sayHello(String name);
}
//구현한 타깃 클래스
public class HelloTarget implements Hello {
    public String sayHello(String name) {
        return "Hello " + name;
    }
}
//인터페이스를 구현한 프록시
public class HelloUppercase implements Hello {
    Hello hello; //위임할 타깃 오브젝트(다른 프록시 접근을 위해 인터페이스로 접근)
    
    public HelloUppercase(Hello hello) {
        this.hello = hello
    }
    
    public String sayHello(String name) {
        return hello.sayHello(name).toUpperCase(); //위임과 부가기능 적용
    }
}
@Test
public void simpleProxy() {
    Hello proxiedHello = new HelloUppercase(new HelloTarget());
    asserThat(proxiedHello.sayHello("Havi"), is("HELLO HAVI"));
}
```



#### 다이내믹 프록시 적용

![img](https://t1.daumcdn.net/cfile/tistory/99B197505C4266501F)

- **다이내믹 프록시**는 프록시 팩토리에 의해 런타임 시 다이내믹하게 만들어지는 오브젝트이다.
- 클라이언트는 다이내믹 프록시를 통해 타깃의 인터페이스를 사용할 수 있다.
- 부가기능은 따로 InvocationHandler를 구현한 오브젝트에 담으며 다음과 같이 하나의 메소드를 갖고 있다.

```java
public Object invoke(Object proxy, Method method, Object[] args)
```

- invoke()는 리플렉션의 Method 인터페이스, 메소드 호출에 필요한 파라미터값(args)를 파라미터로 받는다.
- Hello 인터페이스의 메소드가 아무리 많아도 invoke() 메소드 하나로 모두 처리 가능하다.

[![img](https://github.com/young891221/blog/raw/master/images/Tobi/6.14.png)](https://github.com/young891221/blog/blob/master/images/Tobi/6.14.png)

```java
public class UppercaseHandler implements InvocationHandler {
    Hello target;
    
    public UppercaseHandler(Hello target) {
        this.target = target;
    }
    
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        String ret = (String) method.invoke(target, args); //리플렉션 API를 이용해 타깃 호출
        return ret.toUpperCase(); //부가기능
    }
}
Hello proxiedHello = (Hello) Proxy.newProxyInstance(
        getClass().getClassLoader(), //동적으로 생성되는 다이내믹 프록시 클래스의 로딩에 사용할 클래스 로더
        new Class[] { Hello.class }, //구현할 인터페이스는 여러개일 수 있으니 배열로
        new UppercaseHandler(new HelloTarget())); //부가기능, 위임 기능을 담은 InvocationHandler
```

#### 확장된 UppercaseHandler

리턴타입이 String이 아닌 경우를 구분해서 InvocationHandler를 호출할 수 있도록 해주었다.

```
public class UppercaseHandler implements InvocationHandler {
    Object target;
    
    public UppercaseHandler(Object target) {
        this.target = target;
    }
    
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        Object ret = method.invoke(target, args);
        if(ret instanceof String) {
            return ((String)ret).toUpperCase();
        } else {
            return ret;
        }
    }
}
```

#### 트랜잭션을 포함시킨 InvocationHandler

```
public class TransactionHandler implements InvocationHandler {
    private Object target;
    private PlatformTransactionManager transactionManager;
    private String pattern; //트랜잭션을 적용할 메소드 이름 패턴
    
    public void setTarget(Object target) {
        this.target = target;
    }
    
    public void setTransactionManager(PlatormTransactionManager transactionManager) {
        this.transactionManager = transactionManager;
    }
    
    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        if(method.getName().startsWith(pattern)) {
            return invokeInTransaction(method, args);
        } else {
            return method.invoke(target, args);
        }
    }
    
    private Object invokeInTransaction(Method method, Object[] args) throws Throwable {
        TransactionStatus status = this.transactionManager.getTransaction(new DefaultTransactionDefinition());
        try {
            Object ret = method.invoke(target, args);
            this.transactionManager.commit(status); //타깃 호출후 예외가 발생하지 않으면 commit
            return ret;
        } catch (InvocationTargetException e) { //예외가 발생하면 트랜잭션 롤백
            this.transactionManager.rollback(status);
            return e.getTargetException();
        }
    }
}
```

- 트랜잭션을 적용하는 것은 UserServiceTx와 동일하지만 예외는 runtimeException이 아닌 InvocationTargetException을 사용해서 잡는다.
- 이제 UserServiceTx보다 복잡하지 않으면서 트랜잭션 적용도 간단한 트랜잭션 프록시 핸들러가 만들어졌다.

### 다이내믹 프록시를 위한 팩토리 빈

이전 방법의 문제는 DI의 대상이 되는 다이내믹 프록시 오브젝트는 일반적인 스프링의 빈으로는 등록할 방법이 없다는 것이다. 스프링은 내부적으로 리플렉션 API를 이용해서 빈 정의에 나오는 클래스 이름을 가지고 빈 오브젝트를 생성한다. 문제는 다이내믹 프록시 오브젝트는 이런 식으로 프록시 오브젝트가 생성되지 않는 점이다.

#### 팩토리 빈

스프링은 대신해서 오브젝트의 생성로직을 담당하도록 만들어진 특별한 빈을 말한다. 이를 가장 쉽게 구현하는 방법은 FactoryBean이라는 인터페이스를 구현하는 것이다.

```
public interface FactoryBean<T> {
    T getObject() throws Exception; //빈 오브젝트를 생성해서 돌려준다.
    Class<? extends T> getObjectType(); //생성되는 오브젝트 타입을 알려준다.
    boolean isSingleton(); //getObject가 돌려주는 오브젝트가 항상 같은 싱글톤 오브젝트인지 알려준다.
}
public class Message {
    String text;
    
    private Message(String text) { //외부 생성 불가
        this.text = text;
    }
    
    public String getText() {
        return text;
    }
    
    public static Message newMessage(String text) { //생성자 대신 사용할 수 있는 스태틱 팩토리 메소드
        return new Message(text);
    }
}
public class MessageFactoryBean implements FactoryBean<Message> {
    String text;
    
    public void setText(String text) {
        this.text = text;
    }
    
    /*
     * 복잡한 방식의 오브젝트 생성과 초기화 작업 가능
     * 실제 빈으로 사용될 오브젝트 직접 생성
     */
    public Message getObject() throws Exception {
        return Message.newMessage(this.next);
    }
    
    public Class<? extends Message> getObjectType() {
        return Message.class;
    }
   
    /*
     * 이 팩토리 빈은 매번 요청마다 새로운 오브젝트를 만들므로 false로 설정한다.
     * 이는 펙토리 빈의 동작방식 설정이고 싱글톤으로 스프링이 관리해 줄 수 있다.
     */
    public boolean isSingleton() {
        return false;
    }
}
```

- Message 클래스는 생성자를 private으로 선언하였기에 직접 스프링 빈으로 등록이 불가능하다.
- 이렇게 선언된 Message를 오브젝트를 강제로 생성하는 것은 권장되지 않으며, 바르게 동작하지 않을 수 있다.
- 팩토리 빈은 전형적인 팩토리 메소드를 가진 오브젝트이다.
- 스프링은 FactoryBean 인터페이스를 구현한 클래스가 빈의 클래스로 지정되면, getObject() 메소드를 이용해 오브젝트를 가져오고, 이를 빈 오브젝트로 이용한다.
- 빈의 클래스로 등록된 팩토리 빈은 빈 오브젝트 생성하는 과정에서만 이용된다.



#### 다이내믹 프록시를 만들어주는 팩토리 빈

Proxy의 newProxyInstance() 메소드는 팩토리 빈을 사용하면 다이내믹 프록시 오브젝트를 스프링의 빈으로 만들 수 있다. 팩토리 빈의 getObject() 메소드에 다이내믹 프록시 오브젝트를 만들어 주는 코드를 넣으면 되기 때문이다. 스프링 빈에는 팩토리 빈과 UserSerivceImpl만 빈으로 등록한다.

[![img](https://github.com/young891221/blog/raw/master/images/Tobi/6.15.png)](https://github.com/young891221/blog/blob/master/images/Tobi/6.15.png)

```
팩토리 빈을 이용한 트랜잭션 다이내믹 프록시 적용
public class TxProxyFactoryBean implements FactoryBean<Object> {
    Object target;
    PlatformTransactionManager transactionManager;
    String pattern;
    Class<?> serviceInterface;
    
    public void setTarget(Object targer) {
        this.target = targer;
    }
    
    public void setTransactionManager(PlatformTransactionManager transactionManager) {
        this.transactionManager = transactionManager;
    }
    
    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    
    public void setServiceInterface(Class<?> serviceInterface) {
        this.serviceInterface = serviceInterface;
    }
    
    //FactoryBean 인터페이스 구현 메소드
    public Object getObject() throws Exception {
        TransactionHandler txHandler = new TransactionHandler();
        txHandler.setTarget(targer);
        txHandler.setTransactionManager(transactionManager);
        txHandler.setPattern(pattern);
        return Proxy.newProxyInstance(
                getClass().getCalssLoader(), new Class[] { serviceInterface },
                txHandler);
    }
    
    /*
	 * DI 받은 인터페이스 타입에 따라 팩토리 빈이 생성하는 오브젝트 타입이 달라진다.
	 * 다양한 프록시 오브젝트 생성을 위한 재사용 코드
	 */
    public Class<?> getObjectType() {
        return serviceInterface;
    }
    
    /*
     * 싱글톤 빈이 아니라는 뜻이 아니라
     * getObject()가 매번 같은 오브젝트를 리턴하지 않는다는 의미
     */
    public boolean isSingleton() {
        return false;
    }
}
<bean id="userService" class="springbook.user.service.TxproxyFactoryBean">
	<pxroperty neme="taget" ref="userSerivceImpl" />
	<pxroperty neme="transactionManager" ref="transactionManager" />
	<pxroperty neme="pattern" ref="pattern" />
	<pxroperty neme="serviceInterface" ref="serviceInterface" />
</bean>
```





출처: https://haviyj.tistory.com/28 [What do you want?]



---

---

메서드에 동일한 기능을 하는 코드를 넣고 싶을 때, 각각 메서드에 넣어주는 것은 효율성이 떨어진다.
이럴 때 프록시패턴을 사용한다.

프록시 객체는 원래 객체와 같은 interface를 구현해줘야한다. 원래 객체를 주입받아서, interface의 메서드들을 위임받아 사용하고, 원하는 추가 코드를 넣어주면 된다.

---

---



#### *** 프록시의 단점.**

 

1. 매 번 새로운 클래스 정의 필요.

- 실제 프록시 클래스(Proxy Class)는 실제 구현 클래스와 동일한 형태를 가지고 있기 때문에 구현 클래스의 Interface를 모두 구현해야 함.

 

 2. 타깃의 인터페이스를 구현하고 위임하는 코드 작성의 번거로움.

- 부가기능이 필요없는 메소드도 구현해서 타깃으로 위임하는 코드를 일일이 만들어줘야 함.

- 복잡하진 않지만 인터페이스의 메소드가 많아지고 다양해지면 상당히 부담스러운 작업이 될 수 있음.

- 타깃 인터페이스의 메소드가 추가되거나 변경될 때마다 함께 수정해줘야 한다는 부담도 있음.

 

3. 부가기능 코드의 중복 가능성.

- 프록시를 활용할 만한 부가기능, 접근제어 기능 등은 일반적으로 자주 활용되는 것들이 많기 때문에 다양한 타깃 클래스와 메소드에 중복되어 나타날 가능성이 높음. (특히 트랜잭션(Transaction) 처리는 데이터베이스를 사용하는 대부분의 로직에서 적용되어야 할 필요가 있음.)

- 메서드가 많아지고 트랜잭션 적용의 비율이 높아지면 트랜잭션 기능을 제공하는 유사한 코드가 여러 메서드에 중복돼서 나타날 수 있음.

 

*** 해결책은?**

 \- 다이내믹 프록시(Dynamic Prox)를 이용하는 것! (JDK Dynamic Proxy)



#### 다이내믹 프록시란?**

- 런타임 시 동적으로 만들어지는 오브젝트
- 리플렉션 기능을 이용해서 프록시 생성 (java.lang.reflect)
- 타깃 인터페이스와 동일한 형태로 생성.
- 팩토리빈(FactoryBean)을 통해서 생성.



 @ 스프링의 빈은 기본적으로 클래스 이름(Class name)과 프로퍼티(Property)로 정의. 
 @ 스프링은 지정된 클래스 이름을 가지고 리플렉션을 이용해서 해당 클래스의 오브젝트를 생성.

 

참고로 스프링은 지정된 클래스 이름을 가지고 리플렉션을 이용하여 해당 클래스의 오브젝트를 생성함.

이 외에도 팩토리빈(FactoryBean)과 프록시 팩토리빈(Proxy FactoryBean)을 통해 오브젝트를 생성할 수 있음. 팩토리빈 이란 스프링을 대신해서 오브젝트의 생성 로직을 담당하도록 만들어진 특별한 빈을 뜻함.

 

[추가 정리]

데코레이터(Decorator) 또는 프록시 패턴(Proxy Pattern)을 적용하는 데에 따른 어려움은 부가기능을 구현할 클래스가 부가기능과 관계없는 메서드들도 인터페이스에 선언된 메서드라면 전부 구현해야 하는 번거로움과 부가기능과 관계된 메소드들에 구현되는 코드 중복을 들 수 있음.

 

 -> 이는 자바의 리플렉션(Reflection)에서 제공하는 다이내믹 프록시(Dynamic Proxy)를 활용하여 해결할 수 있음.

 

1. Proxy.newProxyInstance() 를 통한 프록시 생성.

2. Proxy.newProxyInstance() 를 호출할 때 전달하는 InvocationHandler 인터페이스의 단일 메소드인 invoke()에 부가 기능을 단 한번 만 구현함으로써 코드 중복 해결.



- 다이나믹 프록시 오브젝트는 클래스 파일 자체가 존재하지 않음.

- 빈 오브젝트로 등록 불가.

- 팩토리빈 인터페이스 활용. (팩토리빈 인터페이스를 구현한 클래스를 빈으로 등록)



#### 참고

- [[Spring] 프록시 패턴 & 스프링 AOP](https://velog.io/@max9106/Spring-%ED%94%84%EB%A1%9D%EC%8B%9C-AOP-xwk5zy57ee)
- [토비의 스프링 | 6장. AOP2 - 다이내믹 프록시](https://haviyj.tistory.com/28)
- [Dynamic Proxy (동적 프록시)](https://yang1650.tistory.com/146)
- [AOP Proxy](https://yang1650.tistory.com/145?category=616507)