





# Trouble Shooting

#### 1. output에서 한글 깨짐 현상

- [solution](https://freehoon.tistory.com/146) 이 블로그 참고!!

일단 intellij 의 화면에서 **Shift 키를 두번** 눌러주자
아래와 같은 화면이 열릴 것이다.
그리고 입력창에 'vm' 이라고 입력하자.

조회된 항목 중에서 맨 위에 있는 **'Edit Custom VM Options...'** 를 클릭하자.
그리고 열린 내용의 가장 아랫줄에 **-Dfile.encoding=UTF-8** 를 입력해 주자.

![image](https://user-images.githubusercontent.com/55625864/84768117-a4416000-b00e-11ea-9f2b-0e4b23c15967.png)

intellij를 닫고 새로 시작하자.
그리고 서버를 재시작 해보자.



#### 2. 톰캣 server port shutdown 에러

sevlet 테스트 및 공부를 하다가 서버를 종료하면 "destroy"를 오버라이드해서 "destroy"를 출력하려고 했는데 나오지 않았다 !!!

왜 안나오지? 찾아본 결과 

 원인은 바로 server.xml 설정 중 shutdown 포트가 -1로 잡혀 있었던 것이었다.	



이클립스에서 톰캣 서버를 사용할 때 그 톰캣의 원래 config(server.xml)을 사용하지 않고 Extra Config를 사용한다.

인텔리제이를 처음 사용하면서 이 또한 그럴것 같아 찾아봤으나 인텔리제이의 경우 {TOMCAT_HOME}의 설정값을 참조 하고 있다. 

그래서 Tomcat의 수정이 필요한 경우의 tomcat home에 위치해있는 conf/server.xml을 직접 수정해서 사용해야 톰캣 설정 변경이 가능하다.

**↓↓↓↓↓↓↓↓ 내부 tomcat 파일로 들어가서 수정!! 하니까 해결 ↓↓↓↓↓↓↓↓↓↓↓**

```xml
<Server port="8005" shutdown="SHUTDOWN">
```

**인텔리제이에서 톰캣 서버 종료할 때**

- **shutdown port 번호가 8005로 되어있는것 같다!!**



#### 3. Maven dependency가 pom.xml을 수정하면 변경 안됨

- Automatically download에서 source를 체크한다 -> **annotations 추가로 클릭해서 Test할것!(나중에 프로젝트 생성할 때)**

- Maven에 가서 refresh를 해볼것!!

  ![image](https://user-images.githubusercontent.com/55625864/84783667-76671600-b024-11ea-822f-40502f5fcde5.png)

  



에러 메시지
- Configuration Error: deployment source 'me.whiteship:war exploded' is not valid
  [2020-06-17 02:45:39,205] Artifact me.whiteship:war exploded: Error during artifact deployment. See server log for details.

결국 ---------> 새로운 프로젝트 만들어서 진행함!! --> 여기서 에러는 원래있던 프로젝트를 복붙해서 폴더를 런타임으로 돌릴 때 에러가 났음!!  artifact때문인지 무튼 에러남 그래서 프로젝트 새로 만들어서 그냥 진행 !! 추후에 다시 생각해볼것!! 



#### Whitelabel Error Page(404 Not Found)에러

webapp/WEB-INF/jsp/events/list.jsp의 루트를 직접 만들어서 생성하다가 에러가 났으며 

```properties
spring.mvc.view.prefix=/WEB-INF/jsp/
spring.mvc.view.suffix=.jsp
```

이것을 추가하면서 WEB-INF인데 폴더명이 WEB_INF로 오타가 있었다.ㅠㅠㅠㅠㅠㅠ 오타지옥!

인프런 강의에서는 /경로를 안 붙여줘서 에러페이지가 나오기도 했음!!





### ./mvnw package를 실행할 때 에러

- 현상
  - java를 11로 선택했는데 runtime path는 자바 8버전으로 설정되어있었음!
  
  
  
- Solution

  - 윈도우에서 java path를 11로 변경해서 해결함!!

#### 또다른 에러!! : `java -jar target/*.tar`

- ```
  Exception in thread "main" java.lang.UnsupportedClassVersionError: me/whiteship/demojsp/DemoJspApplication has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version
  
  of the Java Runtime only recognizes class file versions up to 52.0
  
          at java.lang.ClassLoader.defineClass1(Native Method)
  
          at java.lang.ClassLoader.defineClass(Unknown Source)
  
          at java.security.SecureClassLoader.defineClass(Unknown Source)
  
          at java.net.URLClassLoader.defineClass(Unknown Source)
  
          at java.net.URLClassLoader.access$100(Unknown Source)
  
          at java.net.URLClassLoader$1.run(Unknown Source)
  
          at java.net.URLClassLoader$1.run(Unknown Source)
  
          at java.security.AccessController.doPrivileged(Native Method)
  
          at java.net.URLClassLoader.findClass(Unknown Source)
  
          at java.lang.ClassLoader.loadClass(Unknown Source)
  
          at org.springframework.boot.loader.LaunchedURLClassLoader.loadClass(LaunchedURLClassLoader.java:151)
  
          at java.lang.ClassLoader.loadClass(Unknown Source)
  
          at java.lang.Class.forName0(Native Method)
  
          at java.lang.Class.forName(Unknown Source)
  
          at org.springframework.boot.loader.MainMethodRunner.run(MainMethodRunner.java:46)
  
          at org.springframework.boot.loader.Launcher.launch(Launcher.java:109)
  
          at org.springframework.boot.loader.Launcher.launch(Launcher.java:58)
  
          at org.springframework.boot.loader.WarLauncher.main(WarLauncher.java:59)
  ```

- Solution

  [java runtime 버전 변경](https://dogcowking.tistory.com/42)

  ![image](https://user-images.githubusercontent.com/55625864/85003803-aa137e80-b191-11ea-8878-258cad0d5169.png)










### JUnit4 -> [JUnit5](https://hychul.github.io/java/2019/01/18/junit5/)

JUnit 5에서 Java 8 또는 그 이상버전을 지원하기 시작하면서 Java 8의 람다와 같은 새로운 기능들에 대한 장점을 수용하려 노력했다.

- @BeforeClass -> @BeforeAll 
- @Before -> @BeforeEacch 

| JUnit 4      | JUnit 5      | Description                                               |
| :----------- | :----------- | :-------------------------------------------------------- |
| @Before      | @BeforeEach  | 테스트 메서드가 시작전에 호출되는 메서드에 사용           |
| @After       | @AfterEach   | 테스트 메서드가 끝난 후에 호출되는 메서드에 사용          |
| @BeforeClass | @BeforeAll   | 모든 테스트 메서드가 호출되기 전에 호출되는 메서드에 사용 |
| @AfterClass  | @AfterAll    | 모든 메스트 메서드가 끝난 후에 호출되는 메서드에 사용     |
| @Ignore      | @Disable     | 테스트 클래스 또는 메서드를 실행하지 않을 때 사용         |
| @RunWith     | @ExtendWith  | Extension을 등록할 때 사용                                |
|              | @Nested      | Nested Test를 위해 이너 클래스에 사용                     |
|              | @Tag         | 테스트 필터링을 위해 클래스 또는 메서드에 사용            |
|              | @TestFactory | *dynamic tests*를 위한 테스트 팩토리 메서드에 사용        |
|              | @DisplayName | 테스트 클래스 또는 메서드에 커스텀 네임을 설정할 때 사용  |



| JUnit4                       | JUnit5                             |
| ---------------------------- | ---------------------------------- |
| @RunWith(SpringRunner.class) | @ExtendWith(SpringExtension.class) |
|                              |                                    |



---

DefaultHandlerExceptionResolver 계속 이렇게 나와서 다음 Test도 제대로 진행 안됩니다ㅠㅠ

도와주세요



Person

```
package me.whiteship.demobootweb;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Person {

    @Id @GeneratedValue
    private Long id;

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }
}
```

PersonRepository

```
package me.whiteship.demobootweb;

import org.springframework.data.jpa.repository.JpaRepository;

public interface PersonRepository extends JpaRepository<Person, Long> {
}
```

SampleController

```
package me.whiteship.demobootweb;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {

    @GetMapping("/hello")
    public String hello(@RequestParam("id") Person person){
        return "hello " + person.getName();
    }
}
```

WebConfig

```
package me.whiteship.demobootweb;

import org.springframework.context.annotation.Configuration;
import org.springframework.format.FormatterRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

}
```

SampleControllerTest

```
package me.whiteship.demobootweb;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.junit.Assert.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;

@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class SampleControllerTest {

    @Autowired
    MockMvc mockMvc;

    @Test
    public void hello() throws Exception {
        this.mockMvc.perform(get("/hello")
                    .param("id", "1"))
                .andDo(print())
                .andExpect(content().string("hello keesun"));
    }
}
```

pom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.1.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>me.whiteship</groupId>
    <artifactId>demo-boot-web</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>demo-boot-web</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>11</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
        </dependency>

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
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

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



코드는 이러합니다ㅠㅠ 감사합니다



에러내용:

"C:\Program Files\Java\jdk-11.0.7\bin\java.exe" -ea -Didea.test.cyclic.buffer.size=1048576 "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.1\lib\idea_rt.jar=49909:C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.1\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.1\lib\idea_rt.jar;C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.1\plugins\junit\lib\junit5-rt.jar;C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.1\plugins\junit\lib\junit-rt.jar;C:\Users\seouz\IdeaProjects\demo-boot-web\target\test-classes;C:\Users\seouz\IdeaProjects\demo-boot-web\target\classes;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-web\2.3.1.RELEASE\spring-boot-starter-web-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter\2.3.1.RELEASE\spring-boot-starter-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot\2.3.1.RELEASE\spring-boot-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-autoconfigure\2.3.1.RELEASE\spring-boot-autoconfigure-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-logging\2.3.1.RELEASE\spring-boot-starter-logging-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\ch\qos\logback\logback-classic\1.2.3\logback-classic-1.2.3.jar;C:\Users\seouz\.m2\repository\ch\qos\logback\logback-core\1.2.3\logback-core-1.2.3.jar;C:\Users\seouz\.m2\repository\org\apache\logging\log4j\log4j-to-slf4j\2.13.3\log4j-to-slf4j-2.13.3.jar;C:\Users\seouz\.m2\repository\org\apache\logging\log4j\log4j-api\2.13.3\log4j-api-2.13.3.jar;C:\Users\seouz\.m2\repository\org\slf4j\jul-to-slf4j\1.7.30\jul-to-slf4j-1.7.30.jar;C:\Users\seouz\.m2\repository\jakarta\annotation\jakarta.annotation-api\1.3.5\jakarta.annotation-api-1.3.5.jar;C:\Users\seouz\.m2\repository\org\yaml\snakeyaml\1.26\snakeyaml-1.26.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-json\2.3.1.RELEASE\spring-boot-starter-json-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\core\jackson-databind\2.11.0\jackson-databind-2.11.0.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\core\jackson-annotations\2.11.0\jackson-annotations-2.11.0.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\core\jackson-core\2.11.0\jackson-core-2.11.0.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jdk8\2.11.0\jackson-datatype-jdk8-2.11.0.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jsr310\2.11.0\jackson-datatype-jsr310-2.11.0.jar;C:\Users\seouz\.m2\repository\com\fasterxml\jackson\module\jackson-module-parameter-names\2.11.0\jackson-module-parameter-names-2.11.0.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-tomcat\2.3.1.RELEASE\spring-boot-starter-tomcat-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\apache\tomcat\embed\tomcat-embed-core\9.0.36\tomcat-embed-core-9.0.36.jar;C:\Users\seouz\.m2\repository\org\glassfish\jakarta.el\3.0.3\jakarta.el-3.0.3.jar;C:\Users\seouz\.m2\repository\org\apache\tomcat\embed\tomcat-embed-websocket\9.0.36\tomcat-embed-websocket-9.0.36.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-web\5.2.7.RELEASE\spring-web-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-beans\5.2.7.RELEASE\spring-beans-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-webmvc\5.2.7.RELEASE\spring-webmvc-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-aop\5.2.7.RELEASE\spring-aop-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-context\5.2.7.RELEASE\spring-context-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-expression\5.2.7.RELEASE\spring-expression-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-data-jpa\2.3.1.RELEASE\spring-boot-starter-data-jpa-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-aop\2.3.1.RELEASE\spring-boot-starter-aop-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\aspectj\aspectjweaver\1.9.5\aspectjweaver-1.9.5.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-jdbc\2.3.1.RELEASE\spring-boot-starter-jdbc-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\com\zaxxer\HikariCP\3.4.5\HikariCP-3.4.5.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-jdbc\5.2.7.RELEASE\spring-jdbc-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\jakarta\transaction\jakarta.transaction-api\1.3.3\jakarta.transaction-api-1.3.3.jar;C:\Users\seouz\.m2\repository\jakarta\persistence\jakarta.persistence-api\2.2.3\jakarta.persistence-api-2.2.3.jar;C:\Users\seouz\.m2\repository\org\hibernate\hibernate-core\5.4.17.Final\hibernate-core-5.4.17.Final.jar;C:\Users\seouz\.m2\repository\org\jboss\logging\jboss-logging\3.4.1.Final\jboss-logging-3.4.1.Final.jar;C:\Users\seouz\.m2\repository\org\javassist\javassist\3.24.0-GA\javassist-3.24.0-GA.jar;C:\Users\seouz\.m2\repository\net\bytebuddy\byte-buddy\1.10.11\byte-buddy-1.10.11.jar;C:\Users\seouz\.m2\repository\antlr\antlr\2.7.7\antlr-2.7.7.jar;C:\Users\seouz\.m2\repository\org\jboss\jandex\2.1.3.Final\jandex-2.1.3.Final.jar;C:\Users\seouz\.m2\repository\com\fasterxml\classmate\1.5.1\classmate-1.5.1.jar;C:\Users\seouz\.m2\repository\org\dom4j\dom4j\2.1.3\dom4j-2.1.3.jar;C:\Users\seouz\.m2\repository\org\hibernate\common\hibernate-commons-annotations\5.1.0.Final\hibernate-commons-annotations-5.1.0.Final.jar;C:\Users\seouz\.m2\repository\org\glassfish\jaxb\jaxb-runtime\2.3.3\jaxb-runtime-2.3.3.jar;C:\Users\seouz\.m2\repository\org\glassfish\jaxb\txw2\2.3.3\txw2-2.3.3.jar;C:\Users\seouz\.m2\repository\com\sun\istack\istack-commons-runtime\3.0.11\istack-commons-runtime-3.0.11.jar;C:\Users\seouz\.m2\repository\com\sun\activation\jakarta.activation\1.2.2\jakarta.activation-1.2.2.jar;C:\Users\seouz\.m2\repository\org\springframework\data\spring-data-jpa\2.3.1.RELEASE\spring-data-jpa-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\data\spring-data-commons\2.3.1.RELEASE\spring-data-commons-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-orm\5.2.7.RELEASE\spring-orm-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-tx\5.2.7.RELEASE\spring-tx-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\slf4j\slf4j-api\1.7.30\slf4j-api-1.7.30.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-aspects\5.2.7.RELEASE\spring-aspects-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\com\h2database\h2\1.4.200\h2-1.4.200.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-starter-test\2.3.1.RELEASE\spring-boot-starter-test-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-test\2.3.1.RELEASE\spring-boot-test-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\boot\spring-boot-test-autoconfigure\2.3.1.RELEASE\spring-boot-test-autoconfigure-2.3.1.RELEASE.jar;C:\Users\seouz\.m2\repository\com\jayway\jsonpath\json-path\2.4.0\json-path-2.4.0.jar;C:\Users\seouz\.m2\repository\net\minidev\json-smart\2.3\json-smart-2.3.jar;C:\Users\seouz\.m2\repository\net\minidev\accessors-smart\1.2\accessors-smart-1.2.jar;C:\Users\seouz\.m2\repository\org\ow2\asm\asm\5.0.4\asm-5.0.4.jar;C:\Users\seouz\.m2\repository\jakarta\xml\bind\jakarta.xml.bind-api\2.3.3\jakarta.xml.bind-api-2.3.3.jar;C:\Users\seouz\.m2\repository\jakarta\activation\jakarta.activation-api\1.2.2\jakarta.activation-api-1.2.2.jar;C:\Users\seouz\.m2\repository\org\assertj\assertj-core\3.16.1\assertj-core-3.16.1.jar;C:\Users\seouz\.m2\repository\org\hamcrest\hamcrest\2.2\hamcrest-2.2.jar;C:\Users\seouz\.m2\repository\org\junit\jupiter\junit-jupiter\5.6.2\junit-jupiter-5.6.2.jar;C:\Users\seouz\.m2\repository\org\junit\jupiter\junit-jupiter-api\5.6.2\junit-jupiter-api-5.6.2.jar;C:\Users\seouz\.m2\repository\org\apiguardian\apiguardian-api\1.1.0\apiguardian-api-1.1.0.jar;C:\Users\seouz\.m2\repository\org\opentest4j\opentest4j\1.2.0\opentest4j-1.2.0.jar;C:\Users\seouz\.m2\repository\org\junit\platform\junit-platform-commons\1.6.2\junit-platform-commons-1.6.2.jar;C:\Users\seouz\.m2\repository\org\junit\jupiter\junit-jupiter-params\5.6.2\junit-jupiter-params-5.6.2.jar;C:\Users\seouz\.m2\repository\org\junit\jupiter\junit-jupiter-engine\5.6.2\junit-jupiter-engine-5.6.2.jar;C:\Users\seouz\.m2\repository\org\junit\platform\junit-platform-engine\1.6.2\junit-platform-engine-1.6.2.jar;C:\Users\seouz\.m2\repository\org\mockito\mockito-core\3.3.3\mockito-core-3.3.3.jar;C:\Users\seouz\.m2\repository\net\bytebuddy\byte-buddy-agent\1.10.11\byte-buddy-agent-1.10.11.jar;C:\Users\seouz\.m2\repository\org\objenesis\objenesis\2.6\objenesis-2.6.jar;C:\Users\seouz\.m2\repository\org\mockito\mockito-junit-jupiter\3.3.3\mockito-junit-jupiter-3.3.3.jar;C:\Users\seouz\.m2\repository\org\skyscreamer\jsonassert\1.5.0\jsonassert-1.5.0.jar;C:\Users\seouz\.m2\repository\com\vaadin\external\google\android-json\0.0.20131108.vaadin1\android-json-0.0.20131108.vaadin1.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-core\5.2.7.RELEASE\spring-core-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-jcl\5.2.7.RELEASE\spring-jcl-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\springframework\spring-test\5.2.7.RELEASE\spring-test-5.2.7.RELEASE.jar;C:\Users\seouz\.m2\repository\org\xmlunit\xmlunit-core\2.7.0\xmlunit-core-2.7.0.jar;C:\Users\seouz\.m2\repository\junit\junit\4.13\junit-4.13.jar;C:\Users\seouz\.m2\repository\org\hamcrest\hamcrest-core\2.2\hamcrest-core-2.2.jar" com.intellij.rt.junit.JUnitStarter -ideVersion5 -junit4 me.whiteship.demobootweb.SampleControllerTest,hello

15:12:57.894 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - SpringJUnit4ClassRunner constructor called with [class me.whiteship.demobootweb.SampleControllerTest]

15:12:57.914 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating CacheAwareContextLoaderDelegate from class [org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate]

15:12:57.941 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating BootstrapContext using constructor [public org.springframework.test.context.support.DefaultBootstrapContext(java.lang.Class,org.springframework.test.context.CacheAwareContextLoaderDelegate)]

15:12:58.115 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating TestContextBootstrapper for test class [me.whiteship.demobootweb.SampleControllerTest] from class [org.springframework.boot.test.context.SpringBootTestContextBootstrapper]

15:12:58.190 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Neither @ContextConfiguration nor @ContextHierarchy found for test class [me.whiteship.demobootweb.SampleControllerTest], using SpringBootContextLoader

15:12:58.220 [main] DEBUG org.springframework.test.context.support.AbstractContextLoader - Did not detect default resource location for test class [me.whiteship.demobootweb.SampleControllerTest]: class path resource [me/whiteship/demobootweb/SampleControllerTest-context.xml] does not exist

15:12:58.224 [main] DEBUG org.springframework.test.context.support.AbstractContextLoader - Did not detect default resource location for test class [me.whiteship.demobootweb.SampleControllerTest]: class path resource [me/whiteship/demobootweb/SampleControllerTestContext.groovy] does not exist

15:12:58.224 [main] INFO org.springframework.test.context.support.AbstractContextLoader - Could not detect default resource locations for test class [me.whiteship.demobootweb.SampleControllerTest]: no resource found for suffixes {-context.xml, Context.groovy}.

15:12:58.231 [main] INFO org.springframework.test.context.support.AnnotationConfigContextLoaderUtils - Could not detect default configuration classes for test class [me.whiteship.demobootweb.SampleControllerTest]: SampleControllerTest does not declare any static, non-private, non-final, nested classes annotated with @Configuration.

15:12:58.548 [main] DEBUG org.springframework.test.context.support.ActiveProfilesUtils - Could not find an 'annotation declaring class' for annotation type [org.springframework.test.context.ActiveProfiles] and class [me.whiteship.demobootweb.SampleControllerTest]

15:12:58.864 [main] DEBUG org.springframework.context.annotation.ClassPathScanningCandidateComponentProvider - Identified candidate component class: file [C:\Users\seouz\IdeaProjects\demo-boot-web\target\classes\me\whiteship\demobootweb\DemoBootWebApplication.class]

15:12:58.925 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Found @SpringBootConfiguration me.whiteship.demobootweb.DemoBootWebApplication for test class me.whiteship.demobootweb.SampleControllerTest

15:12:59.603 [main] DEBUG org.springframework.boot.test.context.SpringBootTestContextBootstrapper - @TestExecutionListeners is not present for class [me.whiteship.demobootweb.SampleControllerTest]: using defaults.

15:12:59.604 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Loaded default TestExecutionListener class names from location [META-INF/spring.factories]: [org.springframework.boot.test.mock.mockito.MockitoTestExecutionListener, org.springframework.boot.test.mock.mockito.ResetMocksTestExecutionListener, org.springframework.boot.test.autoconfigure.restdocs.RestDocsTestExecutionListener, org.springframework.boot.test.autoconfigure.web.client.MockRestServiceServerResetTestExecutionListener, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcPrintOnlyOnFailureTestExecutionListener, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverTestExecutionListener, org.springframework.boot.test.autoconfigure.webservices.client.MockWebServiceServerTestExecutionListener, org.springframework.test.context.web.ServletTestExecutionListener, org.springframework.test.context.support.DirtiesContextBeforeModesTestExecutionListener, org.springframework.test.context.support.DependencyInjectionTestExecutionListener, org.springframework.test.context.support.DirtiesContextTestExecutionListener, org.springframework.test.context.transaction.TransactionalTestExecutionListener, org.springframework.test.context.jdbc.SqlScriptsTestExecutionListener, org.springframework.test.context.event.EventPublishingTestExecutionListener]

15:12:59.674 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Using TestExecutionListeners: [org.springframework.test.context.web.ServletTestExecutionListener@418c5a9c, org.springframework.test.context.support.DirtiesContextBeforeModesTestExecutionListener@18e36d14, org.springframework.boot.test.mock.mockito.MockitoTestExecutionListener@5082d622, org.springframework.boot.test.autoconfigure.SpringBootDependencyInjectionTestExecutionListener@13d4992d, org.springframework.test.context.support.DirtiesContextTestExecutionListener@302f7971, org.springframework.test.context.transaction.TransactionalTestExecutionListener@332729ad, org.springframework.test.context.jdbc.SqlScriptsTestExecutionListener@75d2da2d, org.springframework.test.context.event.EventPublishingTestExecutionListener@4278284b, org.springframework.boot.test.mock.mockito.ResetMocksTestExecutionListener@9573584, org.springframework.boot.test.autoconfigure.restdocs.RestDocsTestExecutionListener@3370f42, org.springframework.boot.test.autoconfigure.web.client.MockRestServiceServerResetTestExecutionListener@6057aebb, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcPrintOnlyOnFailureTestExecutionListener@63eef88a, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverTestExecutionListener@53251a66, org.springframework.boot.test.autoconfigure.webservices.client.MockWebServiceServerTestExecutionListener@6853425f]

15:12:59.690 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.697 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.701 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.703 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.703 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.703 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.740 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.740 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.746 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.746 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.771 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.771 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.815 [main] DEBUG org.springframework.test.context.support.AbstractDirtiesContextTestExecutionListener - Before test class: context [DefaultTestContext@36a5cabc testClass = SampleControllerTest, testInstance = [null], testMethod = [null], testException = [null], mergedContextConfiguration = [WebMergedContextConfiguration@432038ec testClass = SampleControllerTest, locations = '{}', classes = '{class me.whiteship.demobootweb.DemoBootWebApplication}', contextInitializerClasses = '[]', activeProfiles = '{}', propertySourceLocations = '{}', propertySourceProperties = '{org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true}', contextCustomizers = set[[ImportsContextCustomizer@7daa0fbd key = [org.springframework.boot.test.autoconfigure.web.servlet.MockMvcAutoConfiguration, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcWebClientAutoConfiguration, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcWebDriverAutoConfiguration, org.springframework.boot.autoconfigure.security.oauth2.client.servlet.OAuth2ClientAutoConfiguration, org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration, org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration, org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration, org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcSecurityConfiguration]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@76ed1b7c, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@6236eb5f, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@ba54932, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@4b3fa0b3, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizerFactory$Customizer@7e9131d5, org.springframework.boot.test.context.SpringBootTestArgs@1], resourceBasePath = 'src/main/webapp', contextLoader = 'org.springframework.boot.test.context.SpringBootContextLoader', parent = [null]], attributes = map['org.springframework.test.context.web.ServletTestExecutionListener.activateListener' -> true]], class annotated with @DirtiesContext [false] with mode [null].

15:12:59.823 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved @ProfileValueSourceConfiguration [null] for test class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.823 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - Retrieved ProfileValueSource type [class org.springframework.test.annotation.SystemProfileValueSource] for class [me.whiteship.demobootweb.SampleControllerTest]

15:12:59.972 [main] DEBUG org.springframework.test.context.support.TestPropertySourceUtils - Adding inlined properties to environment: {spring.jmx.enabled=false, org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true}



 .  ____     _      __ _ _

 /\\ / ___'_ __ _ _(_)_ __ __ _ \ \ \ \

( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \

 \\/ ___)| |_)| | | | | || (_| | ) ) ) )

 ' |____| .__|_| |_|_| |_\__, | / / / /

 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::    (v2.3.1.RELEASE)



2020-06-20 15:13:02.875 INFO 13492 --- [      main] m.w.demobootweb.SampleControllerTest   : Starting SampleControllerTest on DESKTOP-M96FNV1 with PID 13492 (started by seouz in C:\Users\seouz\IdeaProjects\demo-boot-web)

2020-06-20 15:13:02.884 INFO 13492 --- [      main] m.w.demobootweb.SampleControllerTest   : No active profile set, falling back to default profiles: default

2020-06-20 15:13:04.725 INFO 13492 --- [      main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFERRED mode.

2020-06-20 15:13:04.887 INFO 13492 --- [      main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 137ms. Found 1 JPA repository interfaces.

2020-06-20 15:13:07.525 INFO 13492 --- [      main] o.s.s.concurrent.ThreadPoolTaskExecutor : Initializing ExecutorService 'applicationTaskExecutor'

2020-06-20 15:13:07.555 INFO 13492 --- [      main] com.zaxxer.hikari.HikariDataSource    : HikariPool-1 - Starting...

2020-06-20 15:13:08.022 INFO 13492 --- [      main] com.zaxxer.hikari.HikariDataSource    : HikariPool-1 - Start completed.

2020-06-20 15:13:08.212 INFO 13492 --- [     task-1] o.hibernate.jpa.internal.util.LogHelper : HHH000204: Processing PersistenceUnitInfo [name: default]

2020-06-20 15:13:08.436 INFO 13492 --- [     task-1] org.hibernate.Version          : HHH000412: Hibernate ORM core version 5.4.17.Final

2020-06-20 15:13:09.048 WARN 13492 --- [      main] JpaBaseConfiguration$JpaWebConfiguration : spring.jpa.open-in-view is enabled by default. Therefore, database queries may be performed during view rendering. Explicitly configure spring.jpa.open-in-view to disable this warning

2020-06-20 15:13:09.356 INFO 13492 --- [     task-1] o.hibernate.annotations.common.Version  : HCANN000001: Hibernate Commons Annotations {5.1.0.Final}

2020-06-20 15:13:10.381 INFO 13492 --- [     task-1] org.hibernate.dialect.Dialect      : HHH000400: Using dialect: org.hibernate.dialect.H2Dialect

2020-06-20 15:13:12.576 INFO 13492 --- [      main] o.s.b.t.m.w.SpringBootMockServletContext : Initializing Spring TestDispatcherServlet ''

2020-06-20 15:13:12.585 INFO 13492 --- [      main] o.s.t.web.servlet.TestDispatcherServlet : Initializing Servlet ''

2020-06-20 15:13:12.670 INFO 13492 --- [      main] o.s.t.web.servlet.TestDispatcherServlet : Completed initialization in 85 ms

2020-06-20 15:13:12.704 INFO 13492 --- [      main] DeferredRepositoryInitializationListener : Triggering deferred initialization of Spring Data repositories…

2020-06-20 15:13:14.772 INFO 13492 --- [     task-1] o.h.e.t.j.p.i.JtaPlatformInitiator    : HHH000490: Using JtaPlatform implementation: [org.hibernate.engine.transaction.jta.platform.internal.NoJtaPlatform]

2020-06-20 15:13:14.794 INFO 13492 --- [     task-1] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'

2020-06-20 15:13:15.281 INFO 13492 --- [      main] DeferredRepositoryInitializationListener : Spring Data repositories initialized!

2020-06-20 15:13:15.303 INFO 13492 --- [      main] m.w.demobootweb.SampleControllerTest   : Started SampleControllerTest in 15.176 seconds (JVM running for 20.434)

2020-06-20 15:13:15.877 WARN 13492 --- [      main] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.web.method.annotation.MethodArgumentConversionNotSupportedException: Failed to convert value of type 'java.lang.String' to required type 'me.whiteship.demobootweb.Person'; nested exception is java.lang.IllegalStateException: Cannot convert value of type 'java.lang.String' to required type 'me.whiteship.demobootweb.Person': no matching editors or conversion strategy found]



MockHttpServletRequest:

   HTTP Method = GET

   Request URI = /hello

​    Parameters = {id=[1]}

​     Headers = []

​       Body = null

  Session Attrs = {}



Handler:

​       Type = me.whiteship.demobootweb.SampleController

​      Method = me.whiteship.demobootweb.SampleController#hello(Person)



Async:

  Async started = false

   Async result = null



Resolved Exception:

​       Type = org.springframework.web.method.annotation.MethodArgumentConversionNotSupportedException



ModelAndView:

​    View name = null

​       View = null

​      Model = null



FlashMap:

​    Attributes = null



MockHttpServletResponse:

​      Status = 500

  Error message = null

​     Headers = []

   Content type = null

​       Body = 

  Forwarded URL = null

  Redirected URL = null

​     Cookies = []



MockHttpServletRequest:

   HTTP Method = GET

   Request URI = /hello

​    Parameters = {id=[1]}

​     Headers = []

​       Body = null

  Session Attrs = {}



Handler:

​       Type = me.whiteship.demobootweb.SampleController

​      Method = me.whiteship.demobootweb.SampleController#hello(Person)



Async:

  Async started = false

   Async result = null



Resolved Exception:

​       Type = org.springframework.web.method.annotation.MethodArgumentConversionNotSupportedException



ModelAndView:

​    View name = null

​       View = null

​      Model = null



FlashMap:

​    Attributes = null



MockHttpServletResponse:

​      Status = 500

  Error message = null

​     Headers = []

   Content type = null

​       Body = 

  Forwarded URL = null

  Redirected URL = null

​     Cookies = []



java.lang.AssertionError: Response content 

Expected :hello keesun

Actual  :

<Click to see difference>





 at org.springframework.test.util.AssertionErrors.fail(AssertionErrors.java:59)

 at org.springframework.test.util.AssertionErrors.assertEquals(AssertionErrors.java:122)

 at org.springframework.test.web.servlet.result.ContentResultMatchers.lambda$string$4(ContentResultMatchers.java:136)

 at org.springframework.test.web.servlet.MockMvc$1.andExpect(MockMvc.java:196)

 at me.whiteship.demobootweb.SampleControllerTest.hello(SampleControllerTest.java:30)

 at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)

 at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)

 at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)

 at java.base/java.lang.reflect.Method.invoke(Method.java:566)

 at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:59)

 at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)

 at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:56)

 at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)

 at org.springframework.test.context.junit4.statements.RunBeforeTestExecutionCallbacks.evaluate(RunBeforeTestExecutionCallbacks.java:74)

 at org.springframework.test.context.junit4.statements.RunAfterTestExecutionCallbacks.evaluate(RunAfterTestExecutionCallbacks.java:84)

 at org.springframework.test.context.junit4.statements.RunBeforeTestMethodCallbacks.evaluate(RunBeforeTestMethodCallbacks.java:75)

 at org.springframework.test.context.junit4.statements.RunAfterTestMethodCallbacks.evaluate(RunAfterTestMethodCallbacks.java:86)

 at org.springframework.test.context.junit4.statements.SpringRepeat.evaluate(SpringRepeat.java:84)

 at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:366)

 at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:251)

 at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:97)

 at org.junit.runners.ParentRunner$4.run(ParentRunner.java:331)

 at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:79)

 at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:329)

 at org.junit.runners.ParentRunner.access$100(ParentRunner.java:66)

 at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:293)

 at org.springframework.test.context.junit4.statements.RunBeforeTestClassCallbacks.evaluate(RunBeforeTestClassCallbacks.java:61)

 at org.springframework.test.context.junit4.statements.RunAfterTestClassCallbacks.evaluate(RunAfterTestClassCallbacks.java:70)

 at org.junit.runners.ParentRunner$3.evaluate(ParentRunner.java:306)

 at org.junit.runners.ParentRunner.run(ParentRunner.java:413)

 at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.run(SpringJUnit4ClassRunner.java:190)

 at org.junit.runner.JUnitCore.run(JUnitCore.java:137)

 at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:68)

 at com.intellij.rt.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:33)

 at com.intellij.rt.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:230)

 at com.intellij.rt.junit.JUnitStarter.main(JUnitStarter.java:58)



2020-06-20 15:13:16.190 INFO 13492 --- [extShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'

2020-06-20 15:13:16.192 INFO 13492 --- [extShutdownHook] .SchemaDropperImpl$DelayedDropActionImpl : HHH000477: Starting delayed evictData of schema as part of SessionFactory shut-down'

2020-06-20 15:13:16.218 INFO 13492 --- [extShutdownHook] o.s.s.concurrent.ThreadPoolTaskExecutor : Shutting down ExecutorService 'applicationTaskExecutor'

2020-06-20 15:13:16.220 INFO 13492 --- [extShutdownHook] com.zaxxer.hikari.HikariDataSource    : HikariPool-1 - Shutdown initiated...

2020-06-20 15:13:16.237 INFO 13492 --- [extShutdownHook] com.zaxxer.hikari.HikariDataSource    : HikariPool-1 - Shutdown completed.



Process finished with exit code -1



**Solution**

**스프링 부트 2.3.1 말고 2.3.0을 써보세요. 현재 2.3.1에는 이슈가 있습니다.**

**https://www.youtube.com/watch?v=-mFD1iX5MJo**





### JSR 303 애노테이션이 안나옵니다.

spring 2.3.0 부터는 validation이 빠져서 추가해야합니다. 프로젝트 만들때 validation을 사용할거면 추가하면 됩니다.

**Solution**

https://www.youtube.com/watch?v=cP8TwMV4LjE&feature=youtu.be



### Validation Starter no longer included in web starters

As of [#19550](https://github.com/spring-projects/spring-boot/issues/19550), Web and WebFlux starters do not depend on the validation starter by default anymore. If your application is using validation features, for example you find that `javax.validation.*` imports are not being resolved, you’ll need to add the starter yourself.

**추가하면 끝!!**

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```



