





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



