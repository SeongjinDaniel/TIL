# 의존성(Dependency)

- 코드에서 두 모듈 간의 연결.
- 객체지향언어에서는 두 클래스 간의 관계라고도 말함.
- 일반적으로 둘 중 하나가 다른 하나를 어떤 용도를 위해 사용함.

의존한다는게 무엇일까? ‘누구에게 의지한다’, ‘의지하고 싶다' > 의지라는 단어 자체가 일단 스스로 못함을 의미한다. 즉 의존성이 발생했다는 것은 지금의 주체(함수 또는 클래스)가 누군가를 필요로 함을 뜻한다

​	 dependency injection를 통해서 의존성을 줄일 수 있다.

## 의존성 주입(Dependency Injection)

클래스는 사용하는 다른 클래스에 종속됩니다. 한 객체가 new 키워드를 사용하여 다른 객체를 만들면 코드가 밀접하게 결합되어 테스트, 유지 관리 및 확장이 어렵습니다.

의존성 주입은 클래스에 필요한 객체가 클래스 안에 생성되지 않고 클래스에 '주입'되어야한다는 원칙입니다. 주입은 일반적으로 생성자를 통해 발생하며 클래스는 생성자 매개 변수로 필요한 모든 객체를받습니다.

DI는 느슨한 결합을 달성하는 수단입니다.



의존성 주입에는 세 가지 주요 스타일이 있습니다. 내가 사용하는 이름은 생성자 주입, 세터 주입 및 인터페이스 주입입니다.

![image](https://user-images.githubusercontent.com/55625864/85838909-3860b380-b7d5-11ea-9787-47a687990266.png)

#### 인터페이스 프로그래밍

느슨한 결합을 달성하는 데 사용되는 일련의 사례 중 하나입니다. 인터페이스는 외부 종속성의 작동 방식에 대한 의도와 계약을 정의하지만 실제로는이 동작을 구현하기 위해 구체적인 구현에 맡깁니다. 예를 들어 IRepository <T> 인터페이스가 있고 <T> Get (string id)라는 메소드가있는 경우 주어진 ID에 대해 T의 인스턴스를 리턴하지만 저장소의 구체적인 구현을 리턴하도록 계약을 작성합니다. , StoreRepositiory : IRepository <Store>는 실제로 구현을 제공합니다.

DI를 통해 클래스는 응용 프로그램 전체의 인터페이스를 통해 다른 클래스와 상호 작용할 수 있습니다.

**[참고](https://endjin.com/blog/2014/04/understanding-dependency-injection)**

 [Inversion of Control Containers 및 Dependency Injection 패턴](http://martinfowler.com/articles/injection.html)

[제어의 역전](https://develogs.tistory.com/19)

출처: https://tony-programming.tistory.com/entry/Dependency-의존성-이란 [Tony Programming]