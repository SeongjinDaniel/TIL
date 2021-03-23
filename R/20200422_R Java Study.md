# 20200423 R & Java Study

web.xml에 추가

```
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
```

---------

servlet-context.xml

task 추가 할 떄 버전 정보가 4.3이게 지웠다가 다시 적용 안되면 그냥 수기로 적용해도된다.

```
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns="http://www.springframework.org/schema/mvc"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:task="http://www.springframework.org/schema/task"
	xsi:schemaLocation="http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd
		http://www.springframework.org/schema/task http://www.springframework.org/schema/task/spring-task-4.3.xsd
		http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

	<!-- DispatcherServlet Context: defines this servlet's request-processing infrastructure -->
	
	<!-- Enables the Spring MVC @Controller programming model -->
	<annotation-driven />
	<!-- 추가 -->
	<task:annotation-driven />
	<!-- Handles HTTP GET requests for /resources/** by efficiently serving up static resources in the ${webappRoot}/resources directory -->
	<resources mapping="/resources/**" location="/resources/" />

	<!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
	<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<beans:property name="prefix" value="/WEB-INF/views/" />
		<beans:property name="suffix" value=".jsp" />
	</beans:bean>
	
	<context:component-scan base-package="edu.spring.redu" />
	<!-- 추가 -->
	<context:component-scan base-package="rtest" />
	<context:component-scan base-package="service" />
	
</beans:beans>
```

--------

#### 실습

다음에 제시된 웹 페이지는 다음뉴스의 랭킹페이지이다.

(https://media.daum.net/ranking/popular/)

이 페이지에서 각 뉴스의 제목과 이 뉴스를 올린 신문사명칭을 스크래핑하여

뉴스제목(newstitle), 신문사명(newspapername) 형식의 데이터프레임을 만들고 CSV 파일로 저장하려고 한다. 

이 페이지를 요청하고 앞에서부터 5개의 데이터만 데이터프레임으로 생성하여 리턴하는 것은 R 로 구현하고 R이 생성한 데이터 프레임을 받아와서 파일(daumnews_schedule.csv)에 저장하는 것은 Java API를 이용하여 Java 로 구현한다. 5개 행의 출력 형식은 다음과 같다

 

newstitel,newspapername,datetime

뉴스제목,신문사명, YYYY-MM-dd



또한 가장 중요한 것은 위의 기능을 10분에 한 번씩 수행하도록 스프링의 스케쥴링 컨포넌트와 연계시켜본다. csv 파일에 저장하는 것은 append 모드로 처리해서 이전에 저장된 내용에 추가되게 한다. 즉, SpringSchedulerTest 와 비슷한 역할의 클래스(ScrapingScheduler)를 하나 만들고 10분에 한번씩 수행하도록 설정한다. 