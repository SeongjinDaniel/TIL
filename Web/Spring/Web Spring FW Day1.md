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



<description 밑에 복붙!!(pom.xml)

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

#### exam1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="morning" class="exam1.MorningGreetingImpl" scope="prototype"/>
<bean id="afternoon" class="exam1.AfternoonGreetingImpl"/>
<bean id="evening" class="exam1.EveningGreetingImpl"/>
<bean id="night" class="exam1.NightGreetingImpl"/>

<bean id="time" class="java.time.LocalDateTime" factory-method="now" /> <!-- LocalDateTime 생성자가 숨어있다. Abstract 클래스도 생성자 호출이 안되서 factory-method를 사용한다.-->
         
</beans>
```

```java
package exam1;

public interface Greeting {
	public void greet();
}
```

```java
package exam1;

public class MorningGreetingImpl implements Greeting {
	@Override
	public void greet() {
		System.out.println("상쾌한 아침입니다.");
	}
}
```

```java
package exam1;

public class AfternoonGreetingImpl implements Greeting {
	@Override
	public void greet() {
		System.out.println("즐거운 오후되세요.");
	}
	
}
```

```java
package exam1;

public class EveningGreetingImpl implements Greeting {
	@Override
	public void greet() {
		System.out.println("편안한 저녁되세요.");
	}
}
```

```java
package exam1;

public class NightGreetingImpl implements Greeting {
	@Override
	public void greet() {
		System.out.println("안녕히 주무세요.");
	}
}
```

```java
package exam1;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class GreetingTest {
	
	public static void main(String[] args) {
		ApplicationContext factory = new ClassPathXmlApplicationContext("exam1/beans.xml");
		
		LocalDateTime current = (LocalDateTime)factory.getBean("time");
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH");
        int formatted = Integer.parseInt(current.format(formatter));
        Greeting bean;
        if(formatted >= 6 && formatted < 12) {
        	bean = (Greeting)factory.getBean("morning");
        }
        else if(formatted >= 12 && formatted < 17) {
        	bean = (Greeting)factory.getBean("afternoon");
        }
        else if(formatted >= 17 && formatted <= 22) {
        	bean = (Greeting)factory.getBean("evening");
        }
		else {
			bean = (Greeting)factory.getBean("night");
		}
        bean.greet();
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

--------------

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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="userService" class="sample3.UserServiceImpl" 
                                                    scope="prototype"/>
<bean id="obj1" class="sample3.UserVo">
	<constructor-arg value="Dooly"/>	
</bean>
<bean id="obj2" class="sample3.UserVo">
	<constructor-arg value="Duke"/>	
</bean>
</beans>
```

```java
package sample3;

public interface UserService {
	public void addUser(UserVo vo);
}
```

```java
package sample3;

public class UserVo {
	private String userName;

	public UserVo(String userName) {
		super();
		this.userName = userName;
		System.out.println("UserVO Constructor Call");
	}

	public String getUserName() {
		return userName;
	}
}
```

```java
package sample3;

public class UserServiceImpl implements UserService{
	public UserServiceImpl() {
		super();
		System.out.println("UserService Constructor Call");
	}

	@Override
	public void addUser(UserVo vo) {
		System.out.println("UserService : addUser() Method Call");
		System.out.println("NAME : " + vo.getUserName());
	}
}
```

```java
package sample3;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class UserServiceApp {
	public static void main(String[] args) {
		ApplicationContext factory
        		=new ClassPathXmlApplicationContext("sample3/applicationContext.xml");
		System.out.println("** Container Initialization End **");
		
		UserService u1=(UserService)factory.getBean("userService");
		UserVo vo = (UserVo)factory.getBean("obj1");
		u1.addUser(vo);
		System.out.println(u1);
		System.out.println("----------------------------------------------------");
		
		UserService u2=factory.getBean("userService", UserService.class);//UserService.class : 확장자 지정
		UserVo vo2 = (UserVo)factory.getBean("obj2");
		u2.addUser(vo2);
		System.out.println(u2);		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

----------

### 예제4

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="test" class="sample4.AbstractTest" 
                          factory-method="getInstance"/><!-- factory-method를 이용하여 객체생성을 미리 생성한다. 생성자로 객체생성x -->

</beans>
```

```java
package sample4;
import java.util.Calendar;
import java.util.GregorianCalendar;
public abstract class AbstractTest {
	public abstract String dayInfo();	
	public static AbstractTest getInstance(){ //리턴 값이 AbstractTest이니까 factory 메서드 객체 생성을한다.
		GregorianCalendar cal=new GregorianCalendar();
		int day=cal.get(Calendar.DAY_OF_WEEK);
		AbstractTest test = null;
		switch(day){
			case 1 : test = new Sunday(); break;
			case 2 : test = new Monday(); break;
			case 3 : test = new Tuesday(); break;
			case 4 : test = new Wednesday(); break;
			case 5 : test = new Thursday(); break;
			case 6 : test = new Friday(); break;
			case 7 : test = new Saturday(); break;
		}
		return test;
	}
}
```

```java
package sample4;

public class Monday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Monday";
	}
}
```

```java
package sample4;

public class Tuesday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Tuesday";
	}
}
```

```java
package sample4;

public class Wednesday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Wednesday";
	}
}
```

```java
package sample4;

public class Thursday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Thursday";
	}
}
```

```java
package sample4;

public class Friday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "금요일 입니다";
	}
}
```

```java
package sample4;

public class Saturday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Saturday";
	}
}
```

```java
package sample4;

public class Sunday extends AbstractTest{
	@Override
	public String dayInfo() {
		return "Sunday";
	}
}
```

```java
package sample4;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestApp {
	public static void main(String[] args) {
		ApplicationContext factory = new ClassPathXmlApplicationContext("sample4/app.xml");
		
		AbstractTest bean = (AbstractTest) factory.getBean("test");
		System.out.println("Today : " + bean.dayInfo() + ".");
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

---------------

### 예제5

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- 네임스페이스 선언!!!을 반드시 해주어야 한다.-> 이문서에서 사용되는것들이 어떤 룰을 통해서 선언하고 작성되어야한다. -->
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="hong" class="sample5.DateVo">
	<property name="name" value="Duke"/>
	<property name="birth" value="1990-01-01"/>
	<!-- constant-arg 없으니까 아규먼트 없는 생성자 호출 -->
</bean>

<bean id="lee" class="sample5.DateVo" 
	p:name="Dooly"  p:birth="2000-12-12"/>	<!-- p라는 prefix -> property를 대신한다.-->
</beans>
```

```java
package sample5;
public class DateVo {
	private String name;
	private String birth;
	
	public void setName(String name) {
		this.name = name;
	}
	public void setBirth(String birth) {
		this.birth = birth;
	}
	@Override
	public String toString() {
		return name + "'s birthday : " + birth;
	}
}
```

```java
package sample5;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BirthdayEx { 
	public static void main(String[] args) {
		ApplicationContext factory = 
			       new ClassPathXmlApplicationContext("sample5/date.xml");
		
		//DateVo ob1=(DateVo)factory.getBean("hong");
		DateVo ob1 = factory.getBean("hong", DateVo.class); // 확장자까지 주었음
		System.out.println(ob1.toString());
			
		DateVo ob2=factory.getBean("lee", DateVo.class);
		System.out.println(ob2.toString());
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

-----------

####  스키마(schema)

- XML은 다른 마크업 언어를 만드는데 사용되는 다목적 마크업 언어입니다.

- 이렇게 다른 언어를 정의하기 위해서는 먼저 해당 언어에 필요한 요소와 속성을 파악해야만 합니다.

- 이러한 정보들의 집합을 스키마(schema)라고 부릅니다.

- 스키마는 일관성 있는 XML 문서를 유지하는데 아주 중요한 역할을 합니다.

- XML에서 스키마를 작성할 때에는 다음과 같이 두 가지 방법을 사용할 수 있습니다.

1. DTD(Document Type Definition)

2. XML 스키마(XSD)

#### 문서 타입 정의(DTD)란?

- 문서 타입 정의(DTD)는 XML 문서의 구조 및 해당 문서에서 사용할 수 있는 적법한 요소와 속성을 정의합니다.
- DTD는 엔티티를 정의할 수 있으며, 빠른 개발을 위한 내부 DTD를 사용할 수 있습니다.

- DTD는 예전부터 사용해 온 구식 방법이지만, 특유의 장점을 바탕으로 아직도 널리 사용되고 있습니다.

- 이러한 DTD는 XML 문서 내부에 명시할 수도 있으며, 별도의 파일로 분리할 수도 있습니다.

#### DTD의 사용 목적

- DTD를 사용하여 새로운 XML 문서의 구조를 정의함으로써 새로운 문서 타입을 만들 수 있습니다.

  이렇게 생성된 DTD는 새로운 문서 타입을 이용한 데이터의 교환에서 표준으로써 활용됩니다.

  또한, 응용 프로그램은 DTD의 정의에 따라 XML 문서의 구문 및 구조에 대한 유효성을 검사할 수 있습니다.

#### DTD 문법

XML에서 DTD를 작성하는 문법은 다음과 같습니다.

##### 문법

```
<!DOCTYPE 루트요소 DTD식별자 [ 선언1 선언2 ... ]>
```

DTD는 <!DOCTYPE 으로 시작합니다.

루트(root) 요소는 XML 파서(parser)에 명시된 루트 요소부터 파싱(parsing)을 시작하라고 알려주는 역할을 합니다.

DTD 식별자는 프로그램 외부에 존재하는 DTD 파일을 위한 식별자입니다.

만약에 DTD 식별자가 외부 주소를 가리키고 있으면, 그것을 외부 서브셋(subset)이라고 합니다.

괄호([]) 안에는 내부 서브셋(subset)이라 불리는 추가로 선언한 엔티티(entity)의 리스트가 존재합니다.

#### DTD 내부 서브셋(subset)

DTD가 XML 파일 내부에서 선언되면, 그 선언은 반드시 <!DOCTYPE>안에 위치해야 합니다.

```xml
예제
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE food [
<!ELEMENT food (name,type,cost)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT type (#PCDATA)>
<!ELEMENT cost (#PCDATA)>
]>
<food>
    <name>상추</name>
    <type>야채</type>
    <cost>2000</cost>
</food>
```


위의 예제에서 !DOCTYPE food 는 이 문서의 루트(root) 요소가 <food>요소라는 사실을 명시합니다.

!ELEMENT food는 <food>요소가 <name>, <type>, <cost>의 세 요소를 반드시 포함해야 한다는 사실을 명시합니다.

!ELEMENT name은 <name>요소가 #PCDATA 타입의 요소라는 사실을 명시합니다.

!ELEMENT type은 <type>요소가 #PCDATA 타입의 요소라는 사실을 명시합니다.

!ELEMENT cost은 <cost>요소가 #PCDATA 타입의 요소라는 사실을 명시합니다.

#### DTD 외부 서브셋(subset)

DTD가 XML 파일 외부에서 선언되면, <!DOCTYPE>은 반드시 외부 DTD 파일의 주소 정보를 포함해야 합니다.

이러한 외부 DTD 파일은 .dtd 확장자를 사용하여 저장합니다.

#### data.xml

```xml

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE food SYSTEM "food.dtd">
<food>
    <name>상추</name>
    <type>야채</type>
    <cost>2000</cost>
</food>
```

#### food.dtd

```xml
<!ELEMENT food (name,type,cost)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT type (#PCDATA)>
<!ELEMENT cost (#PCDATA)>
```

DTD(Document Type Definition)나 [XML Schema](https://ko.wikipedia.org/w/index.php?title=XML_Schema&action=edit&redlink=1)는 크게 다음과 같은 문서들을 일정한 규칙을 정하여 통합하고, 다양한 문서간의 표준을 제시하기 위해 쓰인다.

DTD는 정의된 것을 써야된다 라고하면 Schema는 정의된것을 String으로 int형으로 설정하면서 더 세세하게 사용할수있다.

-----

**bean설정파일은 만드는 방법 **

src-> new-> other->Spring->Spring Bean Configuration File -> File name 설정 Next-> 사용하고자하는 것을 선택하고 Finish

--> 하단에 Namespace로 추가 삭제도 가능하다.