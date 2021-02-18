# Mybatis Day3

## news 게시판 실습

File -> new -> other -> Spring -> Spring Legacy Project -> springnews -> Spring MVC Project 선택 -> next -> springnews -> my.spring.springnews(맨 마지막은 contextPath)

springnews-> 오른쪽 클릭 -> properties -> UTF-8 변경

##### pom.xml 변경

```xml
<properties>
    <java-version>1.8</java-version>
    <org.springframework-version>5.0.2.RELEASE</org.springframework-version>
    <org.aspectj-version>1.6.10</org.aspectj-version>
    <org.slf4j-version>1.6.6</org.slf4j-version>
</properties>
```

##### pom.xml 추가

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId> <!-- 응답을 xml로 하겠어, json으로 하겠어 응답을 도와주는 라이브러리 -->
    <version>2.9.9</version>
</dependency>

<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId> <!-- fileupload 라이브러리 지원 -->
    <version>1.3.1</version>
</dependency>  

<dependency>
    <groupId>com.jslsolucoes</groupId>
    <artifactId>ojdbc6</artifactId>
    <version>11.2.0.1.0</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.0.2.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.4.1</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.3.2</version>
</dependency>
```

##### web.xml 추가 

```xml
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

##### sevlet-context.html 추가

```xml
	<context:component-scan base-package="vo" /> <!-- 내가 넣어준것임 -->
	<context:component-scan base-package="dao" /> <!-- 내가 넣어준것임 -->
	
	<beans:bean id="multipartResolver"
		class="org.springframework.web.multipart.commons.CommonsMultipartResolver" />
		
```

##### sevlet-context.html 추가 (news 실습 2단계에서부터)

```xml

<beans:bean id="dataSource" 
		class="org.springframework.jdbc.datasource.DriverManagerDataSource">
	<beans:property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"/>
			<beans:property name="url" value="jdbc:oracle:thin:@localhost:1521:XE" />
			<beans:property name="username" value="jdbctest" />
			<beans:property name="password" value="jdbctest" />		
	</beans:bean>
		
	<beans:bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">	
			<beans:property name="dataSource" ref="dataSource"/>
			<beans:property name="configLocation" 
				value="classpath:/resource/mybatis-config.xml"/>
			<beans:property name="mapperLocations" 
				value="classpath:/resource/*Mapper.xml"/> 	classpath -> source 폴더에 : src/main/java, *Mapper.xml : Mapper라고 쓰여지모든것을 읽음
	</beans:bean> 
	
	<beans:bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate"  
	destroy-method="clearCache">
			<beans:constructor-arg index="0"  ref="sqlSessionFactory" />
	</beans:bean>
```

