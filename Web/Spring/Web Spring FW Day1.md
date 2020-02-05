# Spring Frame Work

- 2005년 정도 부터 FrameWork  기반의 개발이 주류를 이루게 된다.

  ​                      	 <---------------->

  ​						반제품 형태의 SW

  ​						개발 생산성과 유지보수성이 높다.

  ​						Structs, Spring, Mybatis(IBatis), Hibernate, ...

  ​												<------------------->

  ​														JDBC

  **Spring IOC-study**, Spring JDBC, **Spring MVC-study**, Spring Android, Spring Hadoop....

  - Spring IOC(Inversion Of Control)는 모든 Spring에서의 기초가 된다.
    - IoC란 간단하게 말하여 프로그램의 제어 흐름 구조가 바뀌는 것이다.
    - 필요한 객체를 Spring이 알아서 만들어준다.

  Mybatis를 사용하면 DB연동을  JDBC보다 더 간단하게 활용할수있다.

- 1998년 EJB라는 기술의 FrameWork의 시초

- 고급 API

--------

- Spring IOC 구현 방법

  - DL - 의존성 검색

    저장소에 저장되어 있는 빈(Bean)에 접근하기 위하여 개발자들이 컨테이너에서 제공하는 API를 이용하여 사용하고자 하는 빈(Bean)을 Lookup 하는것

  - DI - 의존성 주입

    각 계층 사이, 각 클래스 사이에 필요로 하는 의존 관계를 컨테이너가 자동으로 연결해주는 것

    각 클래스 사이의 의존 관계를 빈 설정(Bean Definition) 정보를 바탕으로 컨테이너가 자동으로 연결해 주는 것

    DL 사용시 컨테이너 종속성이 증가하여, 이를 줄이기 위하여 DI를 사용

    - Setter Injection
    - Constructor Injection

  - Spring DI 컨테이너 초기화

    ApplicationContext context = new ("빈(Bean) 설정 파일");

    - bean - 스프링에서 제어권을 가지고 직접 만들고 관계를 부여하는 오브젝트

      자바빈, EJB의 빈가 비슷한 오브젝트 단위의 애플리케이션 컴포넌트를 말한다. 하지만 스프링을 사용하느 애플리케이션에서 만들어지는 모든 오브젝트가 빈은 아니다. 스프링의 빈은 스프링 컨테이너가 생성과 관계설정, 사용등을 제어해주는 오브젝트를 가리킨다.

  - DL 의 예

    타입명 bean=(타입명)context.getBean("빈이름");

  - DI 의 예
    1. Construction Injection :생성자를 통해서 객체 바인딩 (의존관계를 연결)
    2. Setter Injection : setter 메서드를 이용 해서 객체 바인딩 (의존관계를 연결)

### 환경 설정

Eclipse EE = Eclipse for Java Developer + WTP(플러그인:plugin) + STS(Spring Tool Shoot) 추가 설치

help -> Eclipse Marketplace -> STS 검색 -> go클릭 -> Spring Tools 3 Add-On for Spring Tools 4 3.9.12.CI 설치 -> Confirm -> 설치 완료

- SpringIoc 

  File -> New -> Spring -> Spring Legacy Project -> P Name : springioc -> Templates : Simple Java 클릭 -> Finish -> 프로젝트 생성 완료

  프로젝트에서 우클릭 -> configure -> Convert to Maven Project -> Name : springioc -> Description : 스프링 IoC를 학습하기 위한 프로젝트

### 공부 순서

1. Spring IOC		--> Java Application      --> SpringIoC
2. Spring MVC      --> Web 기반     -->  springedu
3. Mybatis             --> Web 기반

### **아파치 메이븐**(Apache Maven)

[자바](https://ko.wikipedia.org/wiki/자바_(프로그래밍_언어))용 **프로젝트 관리 도구**이다. 추가로 설치해야하는 라이브러리를 관리해준다. 이 프로그램에서는 어떤 라이브러리를 설정하여 사용할수있다

<description 밑에 복붙!!

```html
<dependencies>
  <!-- https://mvnrepository.com/artifact/org.springframework/spring-context -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.0.2.RELEASE</version>
    </dependency>
</dependencies>
```

https://mvnrepository.com/   -> mybatis 검색하면  -> 해당 라이브러리 소스 코드를 확인해서 사용하면된다.

C:\Users\student\.m2\repository   -----> 메이븐 파일 확인 가능

#### 예제1

```java
package sample1;

public interface MessageBean {
	public void sayHello();
	public void sayHello(String a, int b);
}
```

```java
package sample1;

public class MessageBeanImpl implements MessageBean{
	private String fruit;
	private int cost;	
	public MessageBeanImpl() {
		super();
		System.out.println("MessageBeanImpl Default Constructor Call");
	}
	public MessageBeanImpl(String fruit) {
		super();
		this.fruit = fruit;
		System.out.println(fruit + " :  MessageBeanImpl Constructor Call");
	}

	public void setCost(int cost) {
		this.cost = cost;
		System.out.println("setCost() Call");
	}

	@Override
	public void sayHello() {      
		System.out.println(fruit + "   " + cost);
	}

	@Override                     
	public void sayHello(String fruit, int cost) {   
		System.out.println(fruit + "   " + cost);
	}
}
```

```java
package sample1;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class HelloSpringApp {
	public static void main(String[] args) {
		ApplicationContext factory
		    	= new ClassPathXmlApplicationContext("sample1/beans.xml");
		System.out.println("**** Container Initialization End ****");
		
		MessageBean bean=(MessageBean)factory.getBean("messageBean");
		bean.sayHello();                 
		bean.sayHello("banana", 1500);   
		System.out.println(bean);
		System.out.println(factory.getBean("messageBean"));
		System.out.println(factory.getBean("messageBean"));
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

-------------

### 예제2

```java
package sample2;

public interface InterFoo {

}
```

```java
package sample2;

public class Foo implements InterFoo{
	public Foo() {
		System.out.println("Foo - Create object");
	}
	public Foo(String str) {
		System.out.println(str);
		System.out.println("-----------------------");
	}
	public Foo(String str, int n) {
		System.out.println(str + "  " + n);
		System.out.println("-----------------------");
	}
	public Foo(String str, int n, boolean b) {
		System.out.println(str + "  " + n + "   " + b);
		System.out.println("-----------------------");
	}
	public Foo(Bar bar) {
		System.out.println("Create object example");
		System.out.println("----------------------- ");
	}
}
```

```java
package sample2;

public class Bar {
	public Bar() {
		System.out.println("Bar - Create object");
	}
}
```

```java
package sample2;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class FooTestApp {
	public static void main(String[] args) {
		ApplicationContext factory
    		= new ClassPathXmlApplicationContext("sample2/applicationContext.xml");
		System.out.println("**** Container Initialization End ****");
		
		System.out.println("\n\nScope(singleton/prototype)");
		InterFoo ob1=(InterFoo)factory.getBean("foo0");
		System.out.println(ob1);
		InterFoo ob2=(InterFoo)factory.getBean("foo0");
		System.out.println(ob2);
		InterFoo ob3=(InterFoo)factory.getBean("foo0");
		System.out.println(ob3);
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

```html
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!-- 아규먼트 x -->
<bean id="foo0" class="sample2.Foo" scope="singleton"/> <!-- prototype/sigleton(default) --> <!-- prototype은 getBin할 때마다 객체생성해서 사용한다. singleton은 한번만 생성해서 사용한다. -->
<!-- 아규먼트 O -->
<bean id="foo1" class="sample2.Foo">
	<constructor-arg value="XYZ"/>	
</bean>
<!-- 아규먼트 O -->
<bean id="foo2" class="sample2.Foo">
	<constructor-arg  value="ABC"/>
	<constructor-arg  value="100"/>
</bean>
<!-- 아규먼트 O -->
<bean id="foo3" class="sample2.Foo">
	<!-- index를 설정안하면 작성 순서에 따라서 순서대로 아규먼트 적용-->
	<constructor-arg index="1"  type="int"  value="50"/>
	<constructor-arg index="0"  type="java.lang.String" value="xyz"/>
	<constructor-arg index="2"  type="boolean" value="true"/>
</bean>
<!-- 아규먼트 bar 객체 -->
<bean id="foo4" class="sample2.Foo">
	<constructor-arg ref="bar" /> <!-- ref대신 value를 쓰면 String 문자열을 보낸다. -->
</bean>
<bean id="bar"  class="sample2.Bar" />
	
</beans>
```

-----

### 예제3

----------

### 예제4

---------------

### 예제5



-----------

### 예제6

-----------









DTD나 [XML Schema](https://ko.wikipedia.org/w/index.php?title=XML_Schema&action=edit&redlink=1)는 크게 다음과 같은 문서들을 일정한 규칙을 정하여 통합하고, 다양한 문서간의 표준을 제시하기 위해 쓰인다.

DTD는 정의된 것을 써야된다 라고하면 Schema는 정의된것을 String으로 int형으로 설정하면서 더 세세하게 사용할수있다.

-----

bean설정파일은 만드는 방법 

src-> new-> other->Spring->Spring Bean Configuration File -> File name 설정 Next-> 사용하고자하는 것을 선택하고 Finish

--> 하단에 Namespace로 추가 삭제도 가능하다.