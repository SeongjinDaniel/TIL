# IOC(Inversion Of Control)

"제어의 역전" 이라는 의미는 말 그대로 메소드나 객체의 호출작업을 개발자가 결정하는 것이 아니라, **외부에서 결정되는 것**을 의미한다.



- Inversion Of Contorl, 제어의 역행이라는 뜻으로, **인스턴스의 생성 및 소멸을 개발자 대신 스프링 컨테이너가 한다.**
- 그외 제어권을 프레임워크에서 가져간다는 말로도 쓰인다.



**설명**

- 역제어라는 뜻으로 제어권의 반환을 뜻한다. 
  기존의 개발자들이 New 연산자, 인터페이스 호출, 팩토리 호출방식으로 객체의 인스턴스를 생성함으로 인스턴스 생성 방법에 대한 제어권을 개발자들이 가지고 있었다.
  **IOC 란 인스턴스 생성의 제어를 개발자 본인이 아닌 다른 누군가에게 반환 준다는 개념이다.**
  여기서 말하는 다른 누군가란 EJB, Servlet 등 bean을 관리해 주는 컨테이너이다.
  **즉 IOC 란 인스턴스의 생성부터 소멸까지의 인스턴스의 생명주기 관리를 내가 아닌 컨테이너가 대신 해준다는 뜻이다.**

  



# DI(Dependency Injection)

**"의존성 주입"은 제어의 역행이 일어날 때 스프링이 내부에 있는 객체들간의 관계를 관리할 때 사용하는 기법이다.**



의존성 주입은 말 그대로 **의존적인 객체를 직접 생성하거나 제어하는 것이 아니라, 특정 객체에 필요한 객체를 외부에서 결정해서 연결**시키는 것을 의미한다.
즉, 우리는 클래스의 기능을 추상적으로 묶어둔 인터페이스를 갖다 쓰면 되는 것이다.
따라서 이러한 의존성 주입으로 인해 모듈 간의 결합도가 낮아지고 유연성이 높아진다.



- Dependency Injection, 의존성 주입이라는 뜻으로, IOC를 실제로 구현하는 방법이다.
- 의존성이 있는 컴포넌트를 개발자가 코드로 명시하는 것이 아니라 Spring이 런타임에서 연결해 처리한다. 
  런타임 시에 사용 의존관계를 맺을 오브젝트를 주입해준다.
- XML파일을 통해 설정한대로, Bean객체 생성 시 의존성 주입을 수행한다.



**설명**

- DI(의존성 삽입) 은 Spring 컨테이너가 IOC 를 지원하는 새로운 형태다.
  **DI는 클래스 사이의 의존관계를 빈 설정정보를 바탕으로 컨테이너가 자동적으로 연결해 주는 것을 의미한다.** Spring 컨테이너가 지원하는 DI 는 두가지 유형이 있다.
- Setter Injection
  Setter Method를 명시하여 자동적으로 의존성 삽입이 이루어 지는 유형
- Constructor Injection
  인자를 가지고 있는 생성자를 호출 할때 의존성 삽입이 이루어 지는 유형



**의존 관계 주입 세가지 조건 충족 (by spring of toby)**

- 클래스 모델이나 코드에는 런타임 시점의 의존관계가 드러나지 않는다. 그러기 위해서는 인터페이스에만 의존하고 있어야 한다.
- 런타임 시점의 의존관계는 컨테이너나 팩토리 같은 제3의 존재가 결정한다.
- 의존관계는 사용할 오브젝트에 대한 레퍼런스를 외부에서 제공(주입)해줌으로써 만들어진다.



- **Dependency**: An object usually requires objects of other classes to perform its operations. We call these objects dependencies.
- **Injection**: The process of providing the required dependencies to an object.

Thus dependency injection helps in implementing inversion of control (IoC). This means that the responsibility of object creation and injecting the dependencies is given to the framework (i.e. Spring) instead of the class creating the dependency objects by itself.



```java
@Component
class Cake {

  private Flavor flavor;

  Cake(Flavor flavor) {
    Objects.requireNonNull(flavor);
    this.flavor = flavor;
  }

  Flavor getFlavor() {
    return flavor;
  }
  ...
}
```

Spring 4.3 이전 `@Autowired`에는 생성자에 주석을 추가해야했다 . 최신 버전에서는 클래스에 생성자가 하나만있는 경우 선택 사항ㅇ다.

위의 `Cake`클래스 에서는 생성자가 하나뿐이므로 `@Autowired`주석 을 지정할 필요가 없다 . 두 개의 생성자가있는 아래 예제를 고려해라.

```java
@Component
class Sandwich {

  private Topping toppings;
  private Bread breadType;

  Sandwich(Topping toppings) {
    this.toppings = toppings;
  }

  @Autowired
  Sandwich(Topping toppings, Bread breadType) {
    this.toppings = toppings;
    this.breadType = breadType;
  }
  ...
}
```

생성자가 여러 개인 클래스가있는 경우 생성자 `@Autowired`중 하나에 주석을 명시 적으로 추가하여 Spring이 종속성을 주입하는 데 사용할 생성자를 알 수 있도록해야한다.



## 생성자 주입을 사용해야하는 이유는 무엇입니까?

이제 다양한 유형의 주입을 보았으므로 생성자 주입을 사용하는 몇 가지 장점.

### 모든 필수 종속성은 초기화시 사용할 수 있습니다.

생성자를 호출하여 객체를 만듭니다. 생성자가 모든 필수 종속성을 매개 변수로 예상하면 종속성이 주입되지 않으면 클래스가 인스턴스화되지 않을 것이라고 100 % 확신 할 수 있다.

**IoC 컨테이너는 생성자에 전달하기 전에 생성자에 제공된 모든 인수를 사용할 수 있는지 확인합니다** . 이것은 악명 높은 `NullPointerException`.

생성자 삽입은 필요한 모든 종속성이로드되었는지 확인하기 위해 모든 곳에서 별도의 비즈니스 로직을 작성할 필요가 없으므로 매우 유용합니다. 따라서 코드 복잡성이 단순화된다.

#### 선택적 종속성은 어떻습니까?

setter 주입을 통해 Spring은 `@Autowired(required = false)`setter 메소드 에 추가 하여 선택적 종속성을 지정할 수 있습니다 . **모든** 생성자 인수에 `required=false`적용 되므로 생성자 주입에서는 불가능하다 .

Java의 `Optional`유형을 사용하여 생성자 주입과 함께 선택적 종속성을 제공 할 수 있다 .

### 코드 냄새 식별

생성자 주입은 빈이 너무 많은 다른 객체에 의존하는지 식별하는 데 도움이된다. 생성자가 많은 수의 인수를 가지고 있다면 이것은 우리 클래스에 너무 많은 [책임](https://reflectoring.io/single-responsibility-principle) 이 있다는 신호일 수 있다 . 문제의 적절한 분리를 더 잘 해결하기 위해 코드를 리팩토링하는 것에 대해 생각할 수 있다.

### 테스트에서 오류 방지

생성자 주입은 단위 테스트 작성을 단순화합니다. 생성자는 모든 종속성에 대해 유효한 개체를 제공하도록합니다. Mockito와 같은 모의 라이브러리를 사용하여 생성자에 전달할 수있는 모의 객체를 만들 수 있다.

물론 setter를 통해 모의를 전달할 수도 있지만 클래스에 새 종속성을 추가하면 테스트에서 setter를 호출하는 것을 잊고 잠재적으로 테스트에서 오류가 발생할 수 `NullPointerException`있다.

생성자 주입은 모든 종속성을 사용할 수있을 때만 테스트 케이스가 실행되도록다. 단위 테스트 (또는 그 문제에 대해 다른 곳)에서 절반의 개체를 생성하는 것은 불가능하다.

### 불변성

생성자의 서명이 개체를 만드는 유일한 방법이기 때문에 생성자 주입은 [변경 불가능한 개체](https://reflectoring.io/java-immutables) 를 만드는 데 도움이 된다. 빈을 생성하면 더 이상 종속성을 변경할 수 없다. setter 주입을 사용하면 생성 후 종속성을 주입 할 수 있으므로, 무엇보다도 다중 스레드 환경에서 스레드로부터 안전하지 않을 수 있고 변경 가능성으로 인해 디버그하기 어려운 가변 개체로 이어질 수 있다.

## 결론

생성자 주입은 코드를 더욱 강력하게 만듭니다. 불변의 객체를 생성하여 `NullPointerException`s 및 기타 오류를 방지 할 수 있다.



### 참조

- https://jobc.tistory.com/30
- https://blog.naver.com/jiruchi
- https://reflectoring.io/constructor-injection/