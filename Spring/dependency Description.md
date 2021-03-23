# Dependency(의존성) 관련

## spring-boot-starter-web

- Spring MVC를 사용하는 RESTful 애플리케이션을 포함하여 웹 애플리케이션을 빌드하는 데 사용됩니다.

- 기본 내장 컨테이너로 Tomcat을 사용합니다.

  (It is used for building the web application, including RESTful applications using Spring MVC. It uses Tomcat as the default embedded container.)

- spring-boot-starter-web이 Tomcat과 Spring MVC를 추가했기 때문에
  자동 구성에서는 웹 응용 프로그램을 개발한다고 가정하고 이에 따라 Spring을 설정합니다.

  (Since spring-boot-starter-web added Tomcat and Spring MVC, the auto-configuration assumes that you are developing a web application and sets up Spring accordingly.)

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.1.RELEASE</version>
    <relativePath/> <!-- lookup parent from repository -->
  </parent>
  <groupId>me.dev.oliver</groupId>
  <!-- 다른 프로젝트에서 참조하는 이름 -->
  <artifactId>youtube-sns</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <!-- 현재 프로젝트 이름 -->
  <name>youtube-sns</name>
  <description>Demo project for Spring Boot</description>

  <properties>
    <java.version>1.8</java.version>
  </properties>


  <dependencies>
    <!--
    Spring MVC를 사용하는 RESTful 애플리케이션을 포함하여 웹 애플리케이션을 빌드하는 데 사용됩니다.
    기본 내장 컨테이너로 Tomcat을 사용합니다.
    spring-boot-starter-web이 Tomcat과 Spring MVC를 추가했기 때문에
    자동 구성에서는 웹 응용 프로그램을 개발한다고 가정하고 이에 따라 Spring을 설정합니다.-->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Getter Setter등을 간편히 에노테이션으로 사용할 수 있는 의존성 주입 -->
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <!-- 프로젝트를 참조하고 있는 다른 프로젝트에 추이적으로 의존성이 주입되지 않음 -->
      <optional>true</optional>
    </dependency>

    <!-- @SpringBootTest 어노테이션을 통해 스프링부트 어플리케이션 테스트에 필요한 거의 모든 의존성을 주입 -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <groupId>org.junit.vintage</groupId>
          <artifactId>junit-vintage-engine</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
  </dependencies>

  <!-- maven 의존성을 주입(jar or war 패키징 할 수 있음, 빌드 정보 생성과 프로그램 시작) -->
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>

</project>
```



## Test Scope Dependencies

The `spring-boot-starter-test` “Starter” (in the `test` `scope`) contains the following provided libraries:

- [JUnit 5](https://junit.org/junit5/) (including the vintage engine for backward compatibility with JUnit 4): The de-facto standard for unit testing Java applications.
- [Spring Test](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/testing.html#integration-testing) & Spring Boot Test: Utilities and integration test support for Spring Boot applications.
- [AssertJ](https://assertj.github.io/doc/): A fluent assertion library.
- [Hamcrest](https://github.com/hamcrest/JavaHamcrest): A library of matcher objects (also known as constraints or predicates).
- [Mockito](https://site.mockito.org/): A Java mocking framework.
- [JSONassert](https://github.com/skyscreamer/JSONassert): An assertion library for JSON.
- [JsonPath](https://github.com/jayway/JsonPath): XPath for JSON.

We generally find these common libraries to be useful when writing tests. If these libraries do not suit your needs, you can add additional test dependencies of your own.