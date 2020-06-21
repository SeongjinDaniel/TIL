# 스프링 웹 MVC

이 강좌는 자바 서블릿(Servlet) 기반의 MVC 프레임워크인 스프링 웹 MVC(이하 스프링 MVC)에 대해
학습합니다.
자바 엔터프라이즈 에디션(Jave EE)은 웹 애플리케이션을 개발할 수 있는 HTTP Servlet(이하
서블릿)이라는 스팩과 API를 제공합니다. 스프링 MVC는 서블릿 API 기반 애플리케이션을 개발할 때 보다
쉽고 빠르게 개발할 수 있는 프레임워크를 제공하여 개발자가 서블릿 API 보다는 애플리케이션 로직에 집중할
수 있도록 도와줍니다. 현재 많은 회사에서 스프링 MVC 기반으로 엔터프라이즈 애플리케이션을 개발하고
배포하며 운영하고 있습니다.
이 강좌는 스프링 MVC 동작 원리와 설정 방법 그리고 애노테이션 기반 MVC 활용 방법에 대해 다루고
있으며 다음과 같은 특징이 있습니다

1. 아쉽지만 Webflux는 다루지 않습니다.
스프링 프레임워크 5 버전부터 리액티브 스택 기반으로 웹 애플리케이션을 개발할 때 사용할 수 있는 스프링
Webflux를 제공하지만 이번 강좌에서 다루는 기술 스택과 차이가 크기 때문에 이번 강좌에서 다루지
않습니다.
2. 서블릿에 대해 학습합니다.
이번 강좌에서는 스프링 MVC 동작 원리를 이해하는데 필요한 서블릿 기능에 대해 학습합니다. 따라서 서블릿
기반 웹 애플리케이션 개발이 처음이거나 스프링 MVC 동작 원리가 궁금했던 학생 또는 개발자에게 유용할
것입니다.
3. 타임리프를 주로 사용합니다.
스프링 MVC 기능 학습에 필요한 뷰를 만들 때 타임리프(Thymeleaf)를 사용합니다. 하지만 타임리프와
JSP(Java Server Pages) 또는 기타 다른 뷰 템플릿 엔진에 대해서 자세히 학습하지는 않습니다. 이번
강좌는 스프링 MVC에 집중하겠습니다.
4. 스프링 부트
이번 강좌도 스프링 부트를 사용하여 예제 프로젝트를 만들고 코딩하지만, 스프링 부트 없이 설정하는 방법도
학습합니다. 그러면 스프링 부트가 제공하는 자동 설정을 보다 잘 이해할 수 있을 뿐 아니라 스프링 MVC
설정을 원하는 대로 고쳐 사용할 수 있을 것입니다.
5. 테스트 친화적 개발
뷰를 만들고 요청을 보내는 방법으로 스프링 MVC 기능을 확인하고 학습할 수도 있지만 테스트 코드를
작성하여 확인하는 방법을 익히는 것 또한 효율적이며 중요합니다. 따라서 이번 강좌에서는 모든 스프링 MVC
기능을 코드로 테스트 하는 방법도 소개합니다.
원활한 학습을 위해 이번 강좌를 수강하기 전에 다음 강좌 수강을 고려해 주시기 바랍니다.



- 스프링 프레임워크 핵심 기술 (필수)
- 스프링 부트 개념과 활용 (선택)

학습 목표

- 애노테이션 기반 스프링 MVC의 동작 원리를 이해합니다.
- 스프링 MVC가 제공하는 다양한 기능을 이해합니다.
- 사용하는 스프링 MVC 기능에 대한 테스트 코드를 작성할 수 있습니다.
- 스프링 부트 없이도 스프링 MVC 애플리케이션을 개발할 수 있습니다.
- 스프링 부트가 제공하는 스프링 MVC 설정을 고쳐 사용할 수 있습니다.

예제 코드 저장소

- 1부 스프링 MVC 핵심 원리: https://github.com/keesun/javaservletdemo
- 2부 스프링 MVC 설정: https://github.com/keesun/demo-boot-web
- 3부 스프링 MVC 활용: https://github.com/keesun/demo-web-mvc



## 1.강좌 소개
첫 페이지 참고

## 2. 강사 소개

백기선

- 현재 마이크로소프트 미국 본사에 근무 중. (그전에는 네이버와 아마존에서 일을 했습니다.)
- 2007년부터 개발자로 일했으며 이제 막 경력 10년이 조금 넘었네요.
- 자바, 스프링 프레임워크, JPA, 하이버네이트를 주로 공부하고 공유해 왔습니다.
- Youtube/백기선 채널에서 코딩 관련 정보를 영상으로 공유하고 있습니다.
- (예전에는 Whiteship.me 라는 블로그에 글도 많이 올렸지만 요즘은 잘 안써요.)
- (예전에는 책도 쓰고 번역도 하고 발표도 종종 했었지만 역시나.. 요즘은 거의 안합니다.)





# 1부. 스프링 MVC 동작 원리

## 3. **스프링 MVC 소개**

스프링 MVC로 웹 애플리케이션 개발하기 소개

M: 모델
V: 뷰
C: 컨트롤러

모델: 평범한 자바 객체 POJO
뷰: HTML. JSP, [타임리프](https://www.thymeleaf.org/doc/tutorials/2.1/usingthymeleaf.html) , ...
컨트롤러: 스프링 @MVC

모델: 도메인 객체 또는 DTO로 화면에 전달할 또는 화면에서 전달 받은 데이터를 담고 있는 객체.
뷰: 데이터를 보여주는 역할. 다양한 형태로 보여줄 수 있다. HTML, JSON, XML, ...
컨트롤러: 사용자 입력을 받아 모델 객체의 데이터를 변경하거나, 모델 객체를 뷰에 전달하는 역할.

- 입력값 검증
- 입력 받은 데이터로 모델 객체 변경
- 변경된 모델 객체를 뷰에 전달

MVC 패턴의 장점

- 동시 다발적(Simultaneous) 개발 - 백엔드 개발자와 프론트엔드 개발자가 독립적으로 개발을 진행할 수 있다.
- 높은 결합도 - 논리적으로 관련있는 기능을 하나의 컨트롤러로 묶거나, 특정 모델과 관련있는 뷰를
  그룹화 할 수 있다.
- 낮은 의존도 - 뷰, 모델, 컨트롤러는 각각 독립적이다.(loosly coupled)
- 개발 용이성 - 책임이 구분되어 있어 코드 수정하는 것이 편하다.
- 한 모델에 대한 여러 형태의 뷰를 가질 수 있다.

MVC 패턴의 단점

- 코드 네비게이션 복잡함
- 코드 일관성 유지에 노력이 필요함
- 높은 학습 곡선

참고

- https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
- https://www.thymeleaf.org/doc/tutorials/2.1/usingthymeleaf.html



## 4. **서블릿 소개**

가장 기본적인 서블릿 애플리케이션 만들기

서블릿 (Servlet)

- 자바 엔터프라이즈 에디션은 웹 애플리케이션 개발용 스팩과 API 제공.
- 요청 당 쓰레드 (만들거나, **풀에서 가져다가** ) 사용
- 그 중에 가장 중요한 클래스중 하나가 HttpServlet.

서블릿 등장 이전에 사용하던 기술인 CGI (Common Gateway Interface)

- 요청 당 프로세스를 만들어 사용

서블릿의 장점 (CGI에 비해)

- 빠르다.
- 플랫폼 독립적
- 보안
- 이식성

서블릿 엔진 또는 서블릿 컨테이너 (톰캣, 제티, 언더토, ...)

- 세션 관리
- 네트워크 서비스
- MIME 기반 메시지 인코딩 디코딩
- 서블릿 생명주기 관리
- ...

서블릿 생명주기

- 서블릿 컨테이너가 서블릿 인스턴스의 init() 메소드를 호출하여 초기화 한다.
  - 최초 요청을 받았을 때 한번 초기화 하고 나면 그 다음 요청부터는 이 과정을 생략한다.
- 서블릿이 초기화 된 다음부터 클라이언트의 요청을 처리할 수 있다. 각 요청은 별도의 쓰레드로
  처리하고 이때 서블릿 인스턴스의 service() 메소드를 호출한다.
  - 이 안에서 HTTP 요청을 받고 클라이언트로 보낼 HTTP 응답을 만든다.
  - service()는 보통 HTTP Method에 따라 doGet(), doPost() 등으로 처리를 위임한다.
  - 따라서 보통 doGet() 또는 doPost()를 구현한다.
- 서블릿 컨테이너 판단에 따라 해당 서블릿을 메모리에서 내려야 할 시점에 destroy()를 호출한다.





### 5. 서블릿 애플리케이션 개발

준비물: 메이븐, 톰캣

서블릿 구현

```java
public class HelloServlet extends HttpServlet {
    
    @Override
    public void init() throws ServletException {
    	System. out .println( "init" );
    }
    
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws
        ServletException, IOException {
        System. out .println( "doGet" );
        resp.getWriter().write( "Hello Servlet" );
    }
    
    @Override
    public void destroy() {
    	System. out .println( "destroy" );
    }
}
```

서블릿 등록

```xml
<!DOCTYPE web-app PUBLIC
"-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
"http://java.sun.com/dtd/web-app_2_3.dtd" >
< web-app >
	< display-name > Archetype Created Web Application </ display-name >

    < servlet >
        < servlet-name > hello </ servlet-name >
        < servlet-class > me.whiteship.HelloServlet </ servlet-class >
    </ servlet >

    < servlet-mapping >
        < servlet-name > hello </ servlet-name >
        < url-pattern > /hello </ url-pattern >
    </ servlet-mapping >
</ web-app >
```



#### Maven Project 파일 생성

![image-20200616163053663](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200616163053663.png)

![image-20200616163137698](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200616163137698.png)

![image-20200616163206546](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200616163206546.png)

---



구글 검색 : maven repository

-> 들어가서 java servlet으로 검색하면 servlet API([javax.servlet-api](https://mvnrepository.com/artifact/javax.servlet/javax.servlet-api)) 클릭
-> 이 API에 최신버전 4.0.1을 복사해서 pom.xml에 추가

![image-20200616164434742](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200616164434742.png)

↑↑↑↑↑↑↑ main에 java 폴더를 만든후 진행 ↑↑↑↑↑↑↑ 이렇게 설정하면 이제 source 디렉토리가 된다.





### 6. 서블릿 리스너와 필터
서블릿 리스너

- 웹 애플리케이션에서 발생하는 주요 이벤트를 감지하고 각 이벤트에 특별한 작업이 필요한 경우에
  사용할 수 있다.

  - 서블릿 컨텍스트 수준의 이벤트
    - 컨텍스트 라이프사이클 이벤트
    - 컨텍스트 애트리뷰트 변경 이벤트
  - 세션 수준의 이벤트
    - 세션 라이프사이클 이벤트
    - 세션 애트리뷰트 변경 이벤트
  - 서블릿 필터
    - 들어온 요청을 서블릿으로 보내고, 또 서블릿이 작성한 응답을 클라이언트로 보내기 전에 특별한
      처리가 필요한 경우에 사용할 수 있다.
    - 체인 형태의 구조

  ![image](https://user-images.githubusercontent.com/55625864/84770413-7bbb6500-b012-11ea-8ada-b4996045d12f.png)

참고
● https://docs.oracle.com/cd/B14099_19/web.1012/b14017/filters.htm#i1000654





### 7. 스프링 IoC 컨테이너 연동

![image](https://user-images.githubusercontent.com/55625864/84770771-20d63d80-b013-11ea-98a0-5610fc3e7224.png)

(출처: https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html#mvc )

서블릿 애플리케이션에 스프링 연동하기

- 서블릿에서 스프링이 제공하는 IoC 컨테이너 활용하는 방법
- 스프링이 제공하는 서블릿 구현체 DispatcherServlet 사용하기

ContextLoaderListener

- 서블릿 리스너 구현체
- ApplicationContext를 만들어 준다.
- ApplicationContext를 서블릿 컨텍스트 라이프사이클에 따라 등록하고 소멸시켜준다.
- 서블릿에서 IoC 컨테이너를 ServletContext를 통해 꺼내 사용할 수 있다.





### 8. 스프링 MVC 연동

![image](https://user-images.githubusercontent.com/55625864/84781872-55052a80-b022-11ea-8621-2e45da79db22.png)

(출처: https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html#mvc )

서블릿 애플리케이션에 스프링 연동하기

- 서블릿에서 스프링이 제공하는 IoC 컨테이너 활용하는 방법
- 스프링이 제공하는 서블릿 구현체 DispatcherServlet 사용하기

DispatcherServlet

- 스프링 MVC의 핵심.
- Front Controller 역할을 한다.

참고

- http://www.corej2eepatterns.com/FrontController.htm
- https://www.oracle.com/technetwork/java/frontcontroller-135648.html
- https://martinfowler.com/eaaCatalog/frontController.html





### 9. DispatcherServlet 동작 원리 1부
DispatcherServlet 초기화

- 다음의 특별한 타입의 빈들을 찾거나, 기본 전략에 해당하는 빈들을 등록한다.
- HandlerMapping: 핸들러를 찾아주는 인터페이스
- HandlerAdapter: 핸들러를 실행하는 인터페이스
- HandlerExceptionResolver
- ViewResolver
- ...

DispatcherServlet 동작 순서

1. 청을 분석한다. (로케일, 테마, 멀티파트 등)
2. (핸들러 맵핑에게 위임하여) 요청을 처리할 핸들러를 찾는다.
3. (등록되어 있는 핸들러 어댑터 중에) 해당 핸들러를 실행할 수 있는 “핸들러 어댑터”를 찾는다.
4. 찾아낸 “핸들러 어댑터”를 사용해서 핸들러의 응답을 처리한다.
   - 핸들러의 리턴값을 보고 어떻게 처리할지 판단한다.
     - 뷰 이름에 해당하는 뷰를 찾아서 모델 데이터를 랜더링한다.
     - @ResponseEntity가 있다면 Converter를 사용해서 응답 본문을 만들고.
5. (부가적으로) 예외가 발생했다면, 예외 처리 핸들러에 요청 처리를 위임한다.
6. 최종적으로 응답을 보낸다.

HandlerMapping

- RequestMappingHandlerMapping

HandlerAdapter

- RequestMappingHandlerAdapter





### 10. DispatcherServlet 동작 원리 2부: SimpleController
HandlerMapping

- BeanNameUrlHandlerMapping

HandlerAdapter

- SimpleControllerHandlerAdapter

```java
@org.springframework.stereotype.Controller ( "/simple" )
public class SimpleController implements Controller {
    @Override
    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse
    response) throws Exception {
    	return new ModelAndView( "/WEB-INF/simple.jsp" );
    }
}
```



### 11. DispatcherServlet 동작 원리 3부: 커스텀 ViewResolver
ViewResolver

- InternalResourceViewResolver

InternalResourceViewResolver

- Prefix
- Suffix

```java
@Configuration
@ComponentScan
public class WebConfig {
    
	@Bean
	public InternalResourceViewResolver viewResolver() {
        InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
        viewResolver.setPrefix( "/WEB-INF/" );
        viewResolver.setSuffix( ".jsp" );
        return viewResolver;
    }
}
```

```java
@org.springframework.stereotype.Controller ( "/simple" )
public class SimpleController implements Controller {
    @Override
    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse
    response) throws Exception {
    	return new ModelAndView( " /WEB-INF/ simple .jsp " );
    }
}
```

**Basic code completion (the name of any class, method or variable)**





# 12. 스프링 MVC 구성 요소

![image](https://user-images.githubusercontent.com/55625864/84899954-58f98100-b0e4-11ea-94b8-fbd5e4ad69e6.png)



DispatcherSerlvet의 기본 전략

- DispatcherServlet.properties

MultipartResolver

- 파일 업로드 요청 처리에 필요한 인터페이스
- HttpServletRequest를 MultipartHttpServletRequest로 변환해주어 요청이 담고 있는 File을
  꺼낼 수 있는 API 제공.

LocaleResolver

- 클라이언트의 위치(Locale) 정보를 파악하는 인터페이스
- 기본 전략은 요청의 accept-language를 보고 판단.

ThemeResolver

- 애플리케이션에 설정된 테마를 파악하고 변경할 수 있는 인터페이스
- 참고: https://memorynotfound.com/spring-mvc-theme-switcher-example/

HandlerMapping

- 
  요청을 처리할 핸들러를 찾는 인터페이스

HandlerAdapter

- HandlerMapping이 찾아낸 “핸들러”를 처리하는 인터페이스
- 스프링 MVC **확장력** 의 핵심

HandlerExceptionResolver

- 요청 처리 중에 발생한 에러 처리하는 인터페이스

RequestToViewNameTranslator

- 핸들러에서 뷰 이름을 명시적으로 리턴하지 않은 경우, 요청을 기반으로 뷰 이름을 판단하는
  인터페이스

ViewResolver

- 뷰 이름(string)에 해당하는 뷰를 찾아내는 인터페이스

FlashMapManager

- FlashMap 인스턴스를 가져오고 저장하는 인터페이스
- FlashMap은 주로 리다이렉션을 사용할 때 요청 매개변수를 사용하지 않고 데이터를 전달하고
  정리할 때 사용한다.
- redirect:/events

---

-------> redirect: 어떤 데이터를 요청해서 받아서 저장을 하고  보통 redirect를 한다. 왜 redirect를 하느냐? 화면에서 refesh를 할 때 그 데이터가 또 넘어오죠? form submission이 또 발생한다. 화면에서 refresh 했을 때 같은 데이터를 또 보내오지 않도록 방지하기 위한 일종의 패턴이다. POST요청을 받은 후 redirection을 하고 get 요청으로 redirect를 하는것이다. 그래서 get해서 view를 보여준다. 이 상황에서는 브라우저를 refresh해도 form submission이 일어나는것이 아니라 get 요청이 다시 한번 가게 되는 것이다. 이런식으로 중복 form submission을 조금이라도 방지하기 위한 일종의 요청 처리 패턴이다. form 데이터에 요청을 처리하고 나서 redirect를 하는데 이 get 화면에서 보여줄 때 어떤 데이터를 post요청 처리한 후 전달해야할 때가 있다.  이런 경우에 get 요청 redirect를 하는 경우는 pull url을 준다. url에다가 필요한 데이터를 url에 다 적어주거나 url path에다가 적어주거나 한다. 

---





# 13. 스프링 MVC 동작원리 정리
결국엔 (굉장히 복잡한) 서블릿.

= DispatcherServlet

**DispatcherServlet 초기화**

1. 특정 타입에 해당하는 빈을 찾는다.
2. 없으면 기본 전략을 사용한다. (DispatcherServlet.properties)

**스프링 부트 사용하지 않는 스프링 MVC**

- 서블릿 컨네이너(ex, 톰캣)에 등록한 웹 애플리케이션(WAR)에 DispatcherServlet을 등록한다.
  - web.xml에 서블릿 등록
  - 또는 WebApplicationInitializer에 자바 코드로 서블릿 등록 (스프링 3.1+, 서블릿 3.0+)
- 세부 구성 요소는 빈 설정하기 나름.

**스프링 부트를 사용하는 스프링 MVC**

- 자바 애플리케이션에 내장 톰캣을 만들고 그 안에 DispatcherServlet을 등록한다.
  - 스프링 부트 자동 설정이 자동으로 해줌.
- 스프링 부트의 주관에 따라 여러 인터페이스 구현체를 빈으로 등록한다.



---



## 2부. 스프링 MVC 설정

###  14. 스프링 MVC 구성 요소 직접 빈으로 등록하기

@Configuration을 사용한 자바 설정 파일에 직접 @Bean을 사용해서 등록하기





### 15. @EnableWebMvc

애노테이션 기반 스프링 MVC를 사용할 때 편리한 웹 MVC 기본 설정

```java
@Configuration
@EnableWebMvc
public class WebConfig {
}
```





### 16. WebMvcConfigurer 인터페이스

@EnableWebMvc가 제공하는 빈을 커스터마이징할 수 있는 기능을 제공하는 인터페이스

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void configureViewResolvers(ViewResolverRegistry registry) {
        registry.jsp( "/WEB-INF/" , ".jsp" );
    }
}
```





### 17. 스프링 부트의 스프링 MVC 설정

![image-20200618132915579](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200618132915579.png)

스프링 부트의 “주관”이 적용된 자동 설정이 동작한다.

- JSP 보다 Thymeleaf 선호
- JSON 지원
- 정적 리소스 지원 (+ 웰컴 페이지, 파비콘 등 지원)

스프링 MVC 커스터마이징

- application.properties
- **@Configuration + Implements WebMvcConfigurer: 스프링 부트의 스프링 MVC 자동설정**
  **\+ 추가 설정**
- @Configuration + @EnableWebMvc + Imlements WebMvcConfigurer: 스프링 부트의
  스프링 MVC 자동설정 사용하지 않음.



#### 프로젝트 생성!!

![image-20200618140834744](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200618140834744.png)





### 18. 스프링 부트에서 JSP 사용하기
**“ If possible, JSPs should be avoided. There are several known limitations when using**
**them with embedded servlet containers.”**

- https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-feature
s-spring-mvc-template-engines

**제약 사항**

- JAR 프로젝트로 만들 수 없음, WAR 프로젝트로 만들어야 함
- Java -JAR로 실행할 수는 있지만 “실행가능한 JAR 파일”은 지원하지 않음
- 언더토우(JBoss에서 만든 서블릿 컨테이너)는 JSP를 지원하지 않음
- Whitelabel 에러 페이지를 error.jsp로 오버라이딩 할 수 없음.

**참고**

- https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-features-jsp-li
mitations
- https://github.com/spring-projects/spring-boot/tree/v2.1.1.RELEASE/spring-boot-samples
/spring-boot-sample-web-jsp (샘플 프로젝트)

**의존성 추가**

```xml
< dependency >
    < groupId > javax.servlet </ groupId >
    < artifactId > jstl </ artifactId >
</ dependency >
< dependency >
    < groupId > org.apache.tomcat.embed </ groupId >
    < artifactId > tomcat-embed-jasper </ artifactId >
    < scope > provided </ scope >
</ dependency >
```

**태그선언**

```jsp
<%@ taglib prefix =" c " uri =" http://java.sun.com/jsp/jstl/core "%>
```

**application.properties**

```properties
spring.mvc.view.prefix = /WEB-INF/jsp
spring.mvc.view.suffix = .jsp=
```

---

**war 파일 패키지하고 컴파일 하기** 

1. `./mvnw package`
2. `java -jar target/*.war`

---





### 19. WAR 파일 배포하기
java -jar를 사용해서 실행하기

![image](https://user-images.githubusercontent.com/55625864/85004792-f0b5a880-b192-11ea-8de5-52ed9f55b005.png)



- SpringApplication.run 사용하기



서블릿 컨테이너에 배포하기

![image](https://user-images.githubusercontent.com/55625864/85004952-20fd4700-b193-11ea-9edd-b6d999d2d8f7.png)

- SpringBootServletInitializer (WebApplicationInitializer) 사용하기





### 20. 포매터 추가하기

https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html#addFormatters-org.springframework.format.FormatterRegistry-

### Formatter

- Printer: 해당 객체를 (Locale 정보를 참고하여) **문자열** 로 어떻게 출력할 것인가
- Parser: 어떤 **문자열**을 (Locale 정보를 참고하여) 객체로 어떻게 변환할 것인가

https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/format/Formatter.html

포매터 추가하는 방법 1

- WebMvcConfigurer의 addFormatters(FormatterRegistry) 메소드 정의

포매터 추가하는 방법 2 (스프링 부트 사용시에만 가능 함)

- 해당 포매터를 빈으로 등록





### 21. 도메인 클래스 컨버터 자동 등록
스프링 데이터 JPA는 스프링 MVC용 도메인 클래스 컨버터를 제공합니다.

도메인 클래스 컨버터

- 스프링 데이터 JPA가 제공하는 Repository를 사용해서 ID에 해당하는 엔티티를 읽어옵니다.



의존성 설정

```xml
<dependency>	
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
</dependency>
```

엔티티 맵핑

```java
@Entity
public class Person {
    @Id @GeneratedValue
    private Integer id ;
...
```

리파지토리 추가

```java
public interface PersonRepository extends JpaRepository<Person, Integer> {
}
```

테스트 코드 수정

- 테스트용 이벤트 객체 생성
- 이벤트 리파지토리에 저장
- 저장한 이벤트의 ID로 조회 시도





### 22. 핸들러 인터셉터 1부: 개념
https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html#addInterceptors-org.springframework.web.servlet.config.annotation.InterceptorRegistry-

HandlerInterceptor

- 핸들러 맵핑에 설정할 수 있는 인터셉터

- 핸들러를 실행하기 전, 후(아직 랜더링 전) 그리고 완료(랜더링까지 끝난 이후) 시점에 부가 작업을
  하고 싶은 경우에 사용할 수 있다.

- 여러 핸들러에서 반복적으로 사용하는 코드를 줄이고 싶을 때 사용할 수 있다.

  - 로깅, 인증 체크, Locale 변경 등...

  

boolean preHandle(request, response, **handler** )

- 핸들러 실행하기 전에 호출 됨
- “핸들러"에 대한 정보를 사용할 수 있기 때문에 서블릿 필터에 비해 보다 세밀한 로직을 구현할 수
  있다.
- 리턴값으로 계속 다음 인터셉터 또는 핸들러로 요청,응답을 전달할지(true) 응답 처리가 이곳에서
  끝났는지(false) 알린다.

void postHandle(request, response, **modelAndView** )

- 핸들러 실행이 끝나고 아직 뷰를 랜더링 하기 이전에 호출 됨
- “뷰"에 전달할 추가적이거나 여러 핸들러에 공통적인 모델 정보를 담는데 사용할 수도 있다.
- 이 메소드는 인터셉터 역순으로 호출된다.
- 비동기적인 요청 처리 시에는 호출되지 않는다.

void afterCompletion(request, response, handler, ex)

- 요청 처리가 완전히 끝난 뒤(뷰 랜더링 끝난 뒤)에 호출 됨
- preHandler에서 true를 리턴한 경우에만 호출 됨
- 이 메소드는 인터셉터 역순으로 호출된다.
- 비동기적인 요청 처리 시에는 호출되지 않는다.

vs 서블릿 필터

- 서블릿 보다 구체적인 처리가 가능하다.
- 서블릿은 보다 일반적인 용도의 기능을 구현하는데 사용하는게 좋다.

참고:

- https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/HandlerInterceptor.html
- https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/AsyncHandlerInterceptor.html
- ● http://forum.spring.io/forum/spring-projects/web/20146-what-is-the-difference-between-using-a-filter-and-interceptor (스프링 개발자 Mark Fisher의 서블릿 필터와의 차이점에 대한 답변 참고)





### 23. 핸들러 인터셉터 2부: 만들고 등록하기

핸들러 인터셉터 구현하기

```java
public class GreetingInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
    Object handler) throws Exception {
        System. out .println( "preHandle 1" );
        return true ;
    }
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response,
    Object handler, ModelAndView modelAndView) throws Exception {
    	System. out .println( "postHandle 1" );
    }
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response,
    Object handler, Exception ex) throws Exception {
    	System. out .println( "afterCompletion 1" );
    }
}
```

핸들러 인터셉터 등록하기

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor( new GreetingInterceptor()).order( 0 );
        registry.addInterceptor( new AnotherInterceptor())
        .addPathPatterns( "/keeun" )
        .order(- 1 );
    }
}
```

- 특정 패턴에 해당하는 요청에만 적용할 수도 있다.
- 순서를 지정할 수 있다.





### 24. 리소스 핸들러
https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html#addResourceHandlers-org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry-

이미지, 자바스크립트, CSS 그리고 HTML 파일과 같은 정적인 리소스를 처리하는 핸들러 등록하는 방법

디폴트(Default) 서블릿

- 서블릿 컨테이너가 기본으로 제공하는 서블릿으로 정적인 리소스를 처리할 때 사용한다.
- https://tomcat.apache.org/tomcat-9.0-doc/default-servlet.html

스프링 MVC 리소스 핸들러 맵핑 등록

- 가장 낮은 우선 순위로 등록.
  - 다른 핸들러 맵핑이 “/” 이하 요청을 처리하도록 허용하고
  - 최종적으로 리소스 핸들러가 처리하도록.
- [DefaultServletHandlerConfigurer](https://github.com/spring-projects/spring-framework/blob/master/spring-webmvc/src/main/java/org/springframework/web/servlet/config/annotation/DefaultServletHandlerConfigurer.java)

리소스 핸들러 설정

- 어떤 요청 패턴을 지원할 것인가
- 어디서 리소스를 찾을 것인가
- 캐싱
- ResourceResolver: 요청에 해당하는 리소스를 찾는 전략
  - 캐싱, 인코딩(gzip, brotli), WebJar, ...
- ResourceTransformer: 응답으로 보낼 리소스를 수정하는 전략
  - 캐싱, CSS 링크, HTML5 AppCache, ...

스프링 부트

- 기본 정적 리소스 핸들러와 캐싱 제공

참고

- https://www.slideshare.net/rstoya05/resource-handling-spring-framework-41





### 25. HTTP 메시지 컨버터 1부: 개요

https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html#configureMessageConverters-java.util.Listhttps://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html#extendMessageConverters-java.util.List-

HTTP 메시지 컨버터

- 요청 본문에서 메시지를 읽어들이거나(@RequestBody), 응답 본문에 메시지를 작성할 때(@ResponseBody) 사용한다.

기본 HTTP 메시지 컨버터

- 바이트 배열 컨버터
- 문자열 컨버터
- Resource 컨버터
- Form 컨버터 (폼 데이터 to/from MultiValueMap<String, String>)
- (JAXB2 컨버터)
- (Jackson2 컨버터)
- (Jackson 컨버터)
- (Gson 컨버터)
- (Atom 컨버터)
- (RSS 컨버터)
- ...

설정 방법

- 기본으로 등록해주는 컨버터에 새로운 컨버터 추가하기: extendMessageConverters
- 기본으로 등록해주는 컨버터는 다 무시하고 새로 컨버터 설정하기: configureMessageConverters
- **의존성 추가로 컨버터 등록하기 (추천)**
  - **메이븐 또는 그래들 설정에 의존성을 추가하면 그에 따른 컨버터가 자동으로 등록 된다.**
  - **WebMvcConfigurationSupport**
  - (이 기능 자체는 스프링 프레임워크의 기능임, 스프링 부트 아님.)

참고

- https://www.baeldung.com/spring-httpmessageconverter-rest



---

**postman**

- rest api

- http api

  를 테스트할 때 매우 편리한 클라이언트 에플리케이션!!

---





### 26. HTTP 메시지 컨버터 2부: JSON
스프링 부트를 사용하지 않는 경우

- 사용하고 싶은 JSON 라이브러리를 의존성으로 추가
- GSON
- JacksonJSON
- JacksonJSON 2

스프링 부트를 사용하는 경우

- 기본적으로 JacksonJSON 2가 의존성에 들어있다.
- 즉, **JSON용 HTTP 메시지 컨버터가 기본으로 등록되어 있다.**

참고

- JSON path 문법
- https://github.com/json-path/JsonPath
- http://jsonpath.com/





### 27. HTTP 메시지 컨버터 3부: XML
OXM(Object-XML Mapper) 라이브러리 중에 스프링이 지원하는 의존성 추가

- JacksonXML
- JAXB

스프링 부트를 사용하는 경우

- **기본으로 XML 의존성 추가해주지 않음.**

JAXB 의존성 추가

```xml
<!-- jaxb interface -->
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
</dependency>
<!-- 구현체 -->
<dependency>
    <groupId>org.glassfish.jaxb</groupId>
    <artifactId>jaxb-runtime</artifactId>
</dependency>
<!-- xml -> 객체, 객체 -> xml(마샬링, 언마샬링) -->
<!-- 추상화해놓은것을 spring이 제공해준다. -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-oxm</artifactId>
    <version>${spring-framework.version}</version>
</dependency>
```

Marshaller 등록

```java
@Bean
public Jaxb2Marshaller marshaller() {
    Jaxb2Marshaller jaxb2Marshaller = new Jaxb2Marshaller();
    jaxb2Marshaller.setPackagesToScan(Event. class .getPackageName());
    return jaxb2Marshaller;
}
```

도메인 클래스에 @XmlRootElement 애노테이션 추가

참고

- Xpath 문법
- https://www.w3schools.com/xml/xpath_syntax.asp
- https://www.freeformatter.com/xpath-tester.html





### 28. 그밖에 WebMvcConfigurer 설정
https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/servlet/config/annotation/WebMvcConfigurer.html

CORS 설정

- Cross Origin 요청 처리 설정
- 같은 도메인에서 온 요청이 아니더라도 처리를 허용하고 싶다면 설정한다.

리턴 값 핸들러 설정

- 스프링 MVC가 제공하는 기본 리턴 값 핸들러 이외에 리턴 핸들러를 추가하고 싶을 때 설정한다.

아큐먼트 리졸버 설정

- 스프링 MVC가 제공하는 기본 아규먼트 리졸버 이외에 커스텀한 아규먼트 리졸버를 추가하고 싶을때 설정한다.

뷰 컨트롤러

- 단순하게 요청 URL을 특정 뷰로 연결하고 싶을 때 사용할 수 있다.

비동기 설정

- 비동기 요청 처리에 사용할 타임아웃이나 TaskExecutor를 설정할 수 있다.

뷰 리졸버 설정

- 핸들러에서 리턴하는 뷰 이름에 해당하는 문자열을 View 인스턴스로 바꿔줄 뷰 리졸버를 설정한다.

Content Negotiation 설정

- 요청 본문 또는 응답 본문을 어떤 (MIME) 타입으로 보내야 하는지 결정하는 전략을 설정한다.





### 29. 스프링 MVC 설정 마무리
스프링 MVC 설정은 즉 DispatcherServlet이 사용할 여러 빈 설정.

HandlerMapper

HandlerAdapter

ViewResolver

ExceptionResolver

LocaleResolver

...
일일히 등록하려니 너무 많고, 해당 빈들이 참조하는 또 다른 객체들까지 설정하려면... 설정할게 너무 많다.

@EnableWebMvc

- 애노테이션 기반의 스프링 MVC 설정 간편화
- WebMvcConfigurer가 제공하는 메소드를 구현하여 커스터마이징할 수 있다.

스프링 부트

- **스프링 부트 자동 설정을 통해 다양한 스프링 MVC 기능을 아무런 설정 파일을 만들지 않아도**
**제공한다.**
- WebMvcConfigurer가 제공하는 메소드를 구현하여 커스터마이징할 수 있다.
- @EnableWebMvc를 사용하면 스프링 부트 자동 설정을 사용하지 못한다.

스프링 MVC 설정 방법

- 스프링 부트를 사용하는 경우에는 application.properties 부터 시작.
- WebMvcConfigurer로 시작
- @Bean으로 MVC 구성 요소 직접 등록





## 3부. 스프링 MVC 활용
### 30. 스프링 MVC 핵심 기술 소개

애노테이션 기반의 스프링 MVC

- 요청 맵핑하기
- 핸들러 메소드
- 모델과 뷰
- 데이터 바인더
- 예외 처리
- 글로벌 컨트롤러

사용할 기술

- 스프링 부트
- 스프링 프레임워크 웹 MVC
- 타임리프

학습 할 애노테이션

- @RequestMapping
  - @GetMapping, @PostMapping, @PutMapping, ...
- @ModelAttribute
- @RequestParam, @RequestHeader
- @PathVariable, @MatrixVariable
- @SessionAttribute, @RequestAttribute, @CookieValue
- @Valid
- @RequestBody, @ResponseBody
- @ExceptionHandler
- @ControllerAdvice

참고:

● https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html#mvc-controller





### 31. HTTP 요청 맵핑하기 1부: 요청 메소드
HTTP Method

- GET, POST, PUT, PATCH, DELETE, ...

GET 요청

- 클라이언트가 서버의 리소스를 요청할 때 사용한다.
- 캐싱 할 수 있다. (조건적인 GET으로 바뀔 수 있다.) -> 응답 바디(본문)을 보내지 않아도 클라이언트 쪽에서 캐싱하던 정보 그대로 클라이언트가 바로 보여주기 때문에 요청 처리가 굉장히 빠르다.  서버쪽 리소스도 아낄수있음.
- 브라우저 기록에 남는다.
- 북마크 할 수 있다.
- 민감한 데이터를 보낼 때 사용하지 말 것. (URL에 다 보이니까)
- idempotent

POST 요청

- 클라이언트가 서버의 리소스를 수정하거나 새로 만들 때 사용한다.
- 서버에 보내는 데이터를 POST 요청 본문에 담는다.
- 캐시할 수 없다.
- 브라우저 기록에 남지 않는다.
- 북마크 할 수 없다.
- 데이터 길이 제한이 없다.

PUT 요청

- URI에 해당하는 데이터를 새로 만들거나 수정할 때 사용한다.
- POST와 다른 점은 “URI”에 대한 의미가 다르다.
  - POST의 URI는 보내는 데이터를 처리할 리소스를 지칭하며
  - PUT의 URI는 보내는 데이터에 해당하는 리소스를 지칭한다.
- 
- ● Idempotent

PATCH 요청

- PUT과 비슷하지만, 기존 엔티티와 새 데이터의 차이점만 보낸다는 차이가 있다.
- Idempotent

DELETE 요청

- URI에 해당하는 리소스를 삭제할 때 사용한다.
- Idempotent

스프링 웹 MVC에서 HTTP method 맵핑하기

- @RequestMapping(method=RequestMethod.GET)
- @RequestMapping(method={RequestMethod.GET, RequestMethod.POST})
- @GetMapping, @PostMapping, ...



참고

- https://www.w3schools.com/tags/ref_httpmethods.asp
- https://tools.ietf.org/html/rfc2616#section-9.3
- https://tools.ietf.org/html/rfc2068





### 32. HTTP 요청 맵핑하기 2부: URI 패턴 맵핑
URI, URL, URN 헷갈린다

- https://stackoverflow.com/questions/176264/what-is-the-difference-between-a-uri-a-url-and-a-urn

요청 식별자로 맵핑하기

- @RequestMapping은 다음의 패턴을 지원합니다.
- ?: 한 글자 (“/author/???” => “/author/123”)
- \* *: 여러 글자 (“/author/*” => “/author/keesun”)
- \** **: 여러 패스 (“/author/** => “/author/keesun/book”)

클래스에 선언한 @RequestMapping과 조합

- 클래스에 선언한 URI 패턴뒤에 이어 붙여서 맵핑합니다.

정규 표현식으로 맵핑할 수도 있습니다.

- /{name:정규식}

패턴이 중복되는 경우에는?

- 가장 구체적으로 맵핑되는 핸들러를 선택합니다.

URI 확장자 맵핑 지원 

- 이 기능은 권장하지 않습니다. (스프링 부트에서는 기본으로 이 기능을 사용하지 않도록 설정 해 줌)

  - 보안 이슈 (RFD Attack)
  - URI 변수, Path 매개변수, URI 인코딩을 사용할 때 할 때 불명확 함.

  spring mvc는 controller에 mapping 명을 사용하면 암묵적으로 \*\*\*\*\*.xml, \*\*\*\*\*.json \*\*\*\*\*.*등을 등록을 해준다. spring boot는 이기능을 사용하지 않도록 설정을 해놓았다.

  

RFD Attack

- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/reflected-file-download-a-new-web-attack-vector/
- https://www.owasp.org/index.php/Reflected_File_Download
- https://pivotal.io/security/cve-2015-5211





### 33. HTTP 요청 맵핑하기 3부: 미디어 타입 맵핑
특정한 타입의 데이터를 담고 있는 요청만 처리하는 핸들러

- @RequestMapping(**consumes** =MediaType.APPLICATION_JSON_UTF8_VALUE)
- Content-Type 헤더로 필터링
- 매치 되는 않는 경우에 415 Unsupported Media Type 응답

특정한 타입의 응답을 만드는 핸들러

- @RequestMapping(**produces** =”application/json”)
- Accept 헤더로 필터링 (하지만 살짝... 오묘함)
- 매치 되지 않는 경우에 406 Not Acceptable 응답

문자열을 입력하는 대신 MediaType을 사용하면 상수를 (IDE에서) 자동 완성으로 사용할 수 있다.

클래스에 선언한 @RequestMapping에 사용한 것과 조합이 되지 않고 메소드에 사용한 @RequestMapping의 설정으로 덮어쓴다.

Not (!)을 사용해서 특정 미디어 타입이 아닌 경우로 맵핑 할 수도 있다.





### 34. HTTP 요청 맵핑하기 4부: 헤더와 매개변수

특정한 헤더가 있는 요청을 처리하고 싶은 경우

- @RequestMapping(**headers** = “key”)

특정한 헤더가 없는 요청을 처리하고 싶은 경우

- @RequestMapping(**headers** = “ **!**key”)

특정한 헤더 키/값이 있는 요청을 처리하고 싶은 경우

- @RequestMapping(**headers** = “key=value”)

특정한 요청 매개변수 키를 가지고 있는 요청을 처리하고 싶은 경우

- @RequestMapping(**params** = “a”)

특정한 요청 매개변수가 없는 요청을 처리하고 싶은 경우

- @RequestMapping(**params** = “ **!**a”)

특정한 요청 매개변수 키/값을 가지고 있는 요청을 처리하고 싶은 경우

- @RequestMapping(**params** = “a=b”)





### 35. HTTP 요청 맵핑하기 5부: HEAD와 OPTIONS 요청 처리
우리가 구현하지 않아도 스프링 웹 MVC에서 자동으로 처리하는 HTTP Method

- HEAD
- OPTIONS

HEAD

- GET 요청과 동일하지만 **응답 본문을 받아오지 않고 응답 헤더**만 받아온다.

OPTIONS

- 사용할 수 있는 HTTP Method 제공
- 서버 또는 특정 리소스가 제공하는 기능을 확인할 수 있다.
- 서버는 Allow 응답 헤더에 사용할 수 있는 HTTP Method 목록을 제공해야 한다.

참고

- https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html
  https://github.com/spring-projects/spring-framework/blob/master/spring-test/src/test/java/org/springframework/test/web/servlet/samples/standalone/resultmatchers/HeaderAssertionTests.java





### 36. HTTP 요청 맵핑하기 6부: 커스텀 애노테이션
@RequestMapping 애노테이션을 메타 애노테이션으로 사용하기

- @GetMapping 같은 커스텀한 애노테이션을 만들 수 있다.

메타(Meta) 애노테이션

- 애노테이션에 사용할 수 있는 애노테이션
- 스프링이 제공하는 대부분의 애노테이션은 메타 애노테이션으로 사용할 수 있다.

조합(Composed) 애노테이션

- 한개 혹은 여러 메타 애노테이션을 조합해서 만든 애노테이션
- 코드를 간결하게 줄일 수 있다.
- 보다 구체적인 의미를 부여할 수 있다.

@Retention

- 해당 애노테이션 정보를 언제까지 유지할 것인가.
- Source: 소스 코드까지만 유지. 즉, 컴파일 하면 해당 애노테이션 정보는 사라진다는 이야기.
- Class: 컴파인 한 .class 파일에도 유지. 즉 런타임 시, 클래스를 메모리로 읽어오면 해당 정보는 사라진다.
- Runtime: 클래스를 메모리에 읽어왔을 때까지 유지! 코드에서 이 정보를 바탕으로 특정 로직을 실행할 수 있다.

@Target

- 해당 애노테이션을 어디에 사용할 수 있는지 결정한다.

@Documented

- 해당 애노테이션을 사용한 코드의 문서에 그 애노테이션에 대한 정보를 표기할지 결정한다.

메타 애노테이션

- https://docs.spring.io/spring/docs/current/spring-framework-reference/core.html#beansmeta-annotations
- https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/core/annotation/AliasFor.html