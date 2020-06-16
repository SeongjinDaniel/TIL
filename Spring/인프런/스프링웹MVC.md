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