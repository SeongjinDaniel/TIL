# Spring Day3

필드에 설정된 @Autowired  - Spring FW 전용
(1) 타입으로 찾아서 1개이면 해당 객체 주입
(2) 타입으로 찾아서 2개 이상이면 변수명과 동일한 id(id를 따로 주지 않으면 객체의 맨앞 소문자 이름) 값을 갖는 객체 주입
(3) 없으면 NoSuchBeanDefinitionException 발생
     (required = false 속성을 사용하여 없으면 null 이 되게 지정 가능)x
(4) @Qualifier(value="xxx")를 추가로 사용해서 변수명이 아닌 다른 이름 지정 가능

필드에 설정된 @Resource  - Java
(1) 변수명과 동일한 id 값을 갖는 빈을 찾아서 해당 객체 주입
(2) 타입으로 찾아서 1개이면 객체 주입
(3) 타입으로 찾아서 2개이상 이면 NoUniqueBeanDefinitionException 발생
(4) 없으면 NoSuchBeanDefinitionException 발생

#### 실습 sampleanno03

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<context:component-scan base-package="sampleanno03"/> <!-- 스프링 컨테이너에게 프로젝트에 있는 component annotation을 찾는다. -->
<bean id="favoriteFood" class="sampleanno03.Food" 
				p:foodName="Noodle" p:foodPrice="2500"/>
<bean id="unFavoriteFood" class="sampleanno03.Food" 
				p:foodName="Bread" p:foodPrice="1500"/>
</beans>
```

```java
package sampleanno03;

public class Food {
	private String foodName;
	private int foodPrice;
	
	public void setFoodName(String foodName) {
		this.foodName = foodName;
	}
	public void setFoodPrice(int foodPrice) {
		this.foodPrice = foodPrice;
	}
	@Override
	public String toString() {
		return "Food [foodName=" + foodName + ", foodPrice=" + foodPrice + "]";
	}
}
```

```java
package sampleanno03;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component("myFood")  //default : myFoodMgr(이름을 설정하지 않으면 Class 이름의 맨 앞글자를 소문자로 쓴다.) // @Component를 써놓으면 bean 태그를 대신한다.
public class MyFoodMgr{
	@Autowired
	//@Qualifier(value="unFavoriteFood")
	// Food 객체가 여러개 있으면 favoriteFood 이름으로 찾는다. 없으면 에러
	private Food favoriteFood;     // setter - Can be omitted

	@Autowired
	private Food unFavoriteFood;
	                 
	@Override
	public String toString() {
		return "[Food1=" + favoriteFood + ", Food2=" + unFavoriteFood + "]";
	}
}
```

```java
package sampleanno03;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class FoodTest {
	public static void main(String[] args) {
		ApplicationContext factory = new ClassPathXmlApplicationContext("sampleanno03/bean1.xml");

		MyFoodMgr ob=factory.getBean("myFood", MyFoodMgr.class);
		System.out.println(ob.toString());

		((ClassPathXmlApplicationContext) factory).close();
	}
}

```

---------

#### sampleanno04

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:c="http://www.springframework.org/schema/c"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<context:component-scan base-package="sampleanno04"/>
<bean id="emp1" class="sampleanno04.Emp" 
				p:name="Dooly" p:age="25" p:score="75.4" />
<bean id="emp" class="sampleanno04.Emp"
				p:name="Duke" p:age="30" p:score="90.5" />
<bean id="dept" class="java.lang.String"  c:_0="development"/>
<!-- <bean id="engineer" class="sampleanno04.Engineer"  /> -->

</beans>
```

````

```

```

```

```

```



## Spring MVC Project : springedu

 패키지명 : my.spring.springedu

http://localhost:8000/springedu
톰캣재기동 한후에
http://localhost:8000/springedu/hello

### 환경 설정

File -> New -> other -> Spring Legacy ~ ->  springedu -> Spring MVC Project 선택 -> Next -> my.spring.springedu   (마지막 springedu는 project 이름이랑 같지 않으면 안된다.)

pom.xml이 있다는 것은 maven이 관리 할수 있게 도와주는 프로젝트라는것을 알수있다.

springedu 프로젝트 톰캣에 저장!! 

http://localhost:8000/springedu/ -> 확인

#### html 위치

springedu -> src -> main -> webapp -> resources -> html

springedu -> src -> main -> webapp -> resources -> html

springedu 프로젝트 -> UTF-8로 변경

filter 적용!!

src 밑에 -> web.xml 에 필터적용

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee https://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

	<!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/spring/root-context.xml</param-value>
	</context-param>
	
	<!-- Creates the Spring Container shared by all Servlets and Filters -->
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>

	<!-- Processes application requests -->
	<servlet>
		<servlet-name>appServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
		</init-param>
		<load-on-startup>1</load-on-startup>
	</servlet>
		
	<servlet-mapping>
		<servlet-name>appServlet</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>
	
	<filter>
    <filter-name>encodingFilter</filter-name>
    <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
    <init-param>
      <param-name>encoding</param-name>
      <param-value>UTF-8</param-value>
    </init-param>
  	</filter>
	  <filter-mapping>
	    <filter-name>encodingFilter</filter-name>
	    <url-pattern>/*</url-pattern>
	  </filter-mapping>

</web-app>
```

pom.xml 에서 소스 수정

```xml
		<java-version>1.8</java-version>
		<org.springframework-version>5.0.2.RELEASE</org.springframework-version>
```

이부분 수정했음

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>my.spring</groupId>
	<artifactId>springedu</artifactId>
	<name>springedu</name>
	<packaging>war</packaging>
	<version>1.0.0-BUILD-SNAPSHOT</version>
	<properties>
		<java-version>1.8</java-version>
		<org.springframework-version>5.0.2.RELEASE</org.springframework-version>
		<org.aspectj-version>1.6.10</org.aspectj-version>
		<org.slf4j-version>1.6.6</org.slf4j-version>
	</properties>
	<dependencies>
		<!-- Spring -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>${org.springframework-version}</version>
			<exclusions>
				<!-- Exclude Commons Logging in favor of SLF4j -->
				<exclusion>
					<groupId>commons-logging</groupId>
					<artifactId>commons-logging</artifactId>
				 </exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>
				
		<!-- AspectJ -->
		<dependency>
			<groupId>org.aspectj</groupId>
			<artifactId>aspectjrt</artifactId>
			<version>${org.aspectj-version}</version>
		</dependency>	
		
		<!-- Logging -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>${org.slf4j-version}</version>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>jcl-over-slf4j</artifactId>
			<version>${org.slf4j-version}</version>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-log4j12</artifactId>
			<version>${org.slf4j-version}</version>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>log4j</groupId>
			<artifactId>log4j</artifactId>
			<version>1.2.15</version>
			<exclusions>
				<exclusion>
					<groupId>javax.mail</groupId>
					<artifactId>mail</artifactId>
				</exclusion>
				<exclusion>
					<groupId>javax.jms</groupId>
					<artifactId>jms</artifactId>
				</exclusion>
				<exclusion>
					<groupId>com.sun.jdmk</groupId>
					<artifactId>jmxtools</artifactId>
				</exclusion>
				<exclusion>
					<groupId>com.sun.jmx</groupId>
					<artifactId>jmxri</artifactId>
				</exclusion>
			</exclusions>
			<scope>runtime</scope>
		</dependency>

		<!-- @Inject -->
		<dependency>
			<groupId>javax.inject</groupId>
			<artifactId>javax.inject</artifactId>
			<version>1</version>
		</dependency>
				
		<!-- Servlet -->
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>servlet-api</artifactId>
			<version>2.5</version>
			<scope>provided</scope>
		</dependency>
		<dependency>
			<groupId>javax.servlet.jsp</groupId>
			<artifactId>jsp-api</artifactId>
			<version>2.1</version>
			<scope>provided</scope>
		</dependency>
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>jstl</artifactId>
			<version>1.2</version>
		</dependency>
	
		<!-- Test -->
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.7</version>
			<scope>test</scope>
		</dependency>        
	</dependencies>
    <build>
        <plugins>
            <plugin>
                <artifactId>maven-eclipse-plugin</artifactId>
                <version>2.9</version>
                <configuration>
                    <additionalProjectnatures>
                        <projectnature>org.springframework.ide.eclipse.core.springnature</projectnature>
                    </additionalProjectnatures>
                    <additionalBuildcommands>
                        <buildcommand>org.springframework.ide.eclipse.core.springbuilder</buildcommand>
                    </additionalBuildcommands>
                    <downloadSources>true</downloadSources>
                    <downloadJavadocs>true</downloadJavadocs>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>2.5.1</version>
                <configuration>
                    <source>1.6</source>
                    <target>1.6</target>
                    <compilerArgument>-Xlint:all</compilerArgument>
                    <showWarnings>true</showWarnings>
                    <showDeprecation>true</showDeprecation>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>1.2.1</version>
                <configuration>
                    <mainClass>org.test.int1.Main</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>

```

----------

#### Spring MVC 실습

HelloController.java

```java
package my.spring.springedu;
import java.util.Calendar;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
@Controller
public class HelloController {
	public HelloController() {
		System.out.println("HelloController Create object");
	}
	@RequestMapping("/hello") // controller 메서드, 핸들러 메서드 // client 로 부터 요청된 url이 hello로 끝나면 요청해줘!!
	public ModelAndView xxx(){		
		ModelAndView mav = new ModelAndView(); //ModelAndView : 뷰 객체와 모델 객체를 하나의 객체로 담음.
		mav.setViewName("helloView"); // views에 .jsp 파일 이름을 명칭해서 보내고 servlet처럼 forward 방식으로 보내지 않음 알아서 views파일에 가서 보낸다.
		mav.addObject("msg", getMessage()); // addObject는 setAttribute와 같다.
		return mav;
	}
	private String getMessage(){
		int hour = Calendar.getInstance()
				.get(Calendar.HOUR_OF_DAY);		
		if(hour >= 6 && hour <= 10){
			return "Good Morning!!";
		}else if(hour >= 12 && hour <= 15){
			return "Good Afternoon";
		}else if(hour >= 18 && hour <= 22){
			return "Good Evening!!";
		}else{ 
			return "Hello!!";
		}
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" 
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<h1>Result of processing the view</h1>
<hr>
<%
String result = (String)request.getAttribute("msg");
%>
expression tag : <%= result %>
<hr>
EL : ${ msg }
</body>
</html>
```

POJO - Plain Old Java Object (순수한 자바 객체다) -> 아무상속같은것을 할수있다.



src-> WEB-INF -> spring -> appServlet -> servlet-context.xml이 bean 파일이다. Dispatcher Servlet이 알아서 넣어준다.



http://localhost:8000/springedu      ->>> 웹앱까지 찾아감

http://localhost:8000/springedu/resources/multi.html

#### 실습 

```java
package my.spring.springedu;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
@Controller
public class MultiController {	
	@RequestMapping(value="/select")
	public String select() {
		System.out.println("select ............");
		return  "viewTest";
	}
	@RequestMapping(value="/search")
	public String search() {
		System.out.println("search ............");
		return "viewTest";
	}
	@RequestMapping(value="/insert")
	public String insert(int pageno) {
		System.out.println("insert ............"+pageno);
		return  "viewTest";
	}
}
```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	a, form, button {
		margin : 10px;
	}

</style>
</head>
<body>
<h1>MultiController Request</h1>
<hr>
<a href="/springedu/select?pageno=100" style="text-decoration:none">SELECT Request</a><br>
<hr>
<button onclick="location.href='/springedu/search?pageno=1000'">SEARCH Request</button>
<hr>
<form method="get" action="/springedu/insert">
<input type="hidden" name="pageno" value="10">
<input type="submit" value="GET Request">
</form>
<hr>
<form method="post" action="/springedu/insert">
<input type="hidden" name="pageno" value="10">
<input type="submit" value="POST Request">
</form>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2><%= request.getAttribute(
		"javax.servlet.forward.request_uri") %> Request successful!!!</h2>
<hr>
<h2>Request Method : ${ pageContext.request.method }</h2>
<hr>
<h2>Query Value : ${ param.pageno }</h2>
<hr>
<a href='${ header.referer }'>To Form Page....</a>
</body>
</html>
```

----------

#### 실습 

```java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class RequestMethodController {

	public RequestMethodController() {
		System.out.println("RequestMethodController 객체생성");
	}

	@RequestMapping(value = "/requestmethod", method = RequestMethod.GET)
	public String myGet1() {
		System.out.println("GET ............");
		return "getResult";
	}

	@RequestMapping(value = "/requestmethod", method = RequestMethod.POST)
	public String myPost() {
		System.out.println("POST ............");
		return "postResult";
	}
}
```

```html
<!--  requestmethodtest.html -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>requestmethod.html</title>
</head>
<body>
<form method="get" action="/springedu/requestmethod">
<input type="submit" value="GET-request">
</form>
<br><a href="/springedu/requestmethod">GET request</a><br><br>
<form method="post" action="/springedu/requestmethod">
<input type="submit" value="POST-request">
</form>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
   h1 {
   	color : lime;
   }

</style>
</head>
<body>
<h1>response VIEW : <%= request.getRequestURI() %></h1>
<h2><%= request.getMethod() %></h2>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
   h1 {
   	color : pink;
   }

</style>
</head>
<body>
<h1>response VIEW : <%= request.getRequestURI() %></h1>
<h2><%= request.getMethod() %></h2>
</body>
</html>
```

-----

#### 실습

