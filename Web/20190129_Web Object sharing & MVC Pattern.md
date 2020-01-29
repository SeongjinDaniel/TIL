# 객체공유 & MVC 패턴

## 객체공유

객체의 스코프란 객체가 생성되어 유지되는 기간을 의미하며 **Page Scope, Request Scope, Session Scope 그리고 Application Scope** 로 구성된다 .

```
Page Scope : Servlet 또는 JSP가 수행되는 동안만 유효한 객체가 된다.
Request Scope : Web 클라이언트로 부터의 요청이 끝날 때까지 유효한 객체가 된다.
Session Scope : 요청을 보내온 Web 클라이언트가 기동되어 있는 동안 유효한 객체가 된다.
Application Scope : 서버가 기동되어 있는 동안 유효한 객체가 된다.
```

```
Request Scope -> HttpServletRequest 객체에 객체를 보관한다.
Session Scope -> HttpSession 객체에 객체를 보관한다.
Application Scope -> ServletContext 객체에 객체를 보관한다.
```

HttpServletRequest, HttpSession 그리고 ServletContext 는 모두 객체를 저장하는 방으로 사용하는 것이 가능하며 다음과 같은 객체의 저장 , 추출 , 삭제 기능의 메서드들을 지원한다

```
public void setAttribute(String key, Object value)
public Object getAttribute(String key)
public void removeAttribute(String key)
```

공통점 : 객체를 보관할 수 있는 방으로 사용할 수 있다. -> 이것을 컨테이너라고도함

#### [ Servlet과 JSP 에서 사용되는 Java 객체의 scope ]

1. 요청 동안의 객체 공유

   A와 B가 forward 또는 include 관계에 있는 경우 A 가 생성하는 객체를 HttpServletRequest 객체에 보관하면 B 에서 추출할 수 있다. 요청이 끝나면 사라진다.

2. 세션이 유지되는 동안 각 클라이언트별 객체 공유

   각 클라이언트별로 서버에 하나씩 만들어지는 HttpSession 객체에 객체를 보관하면 세션이 유지되는 한 계속해서 클라이언트별로 이 객체를 꺼내서 사용할 수 있다.

3. 서버가 기동되어 있는 동안 모든 클라이언트에 의한 객체 공유

   서버에 등록되는 Web Application 당 하나씩 만들어지는 ServletContext 객체에 객체를 보관하면 서버 종료시까지 이 객체를 꺼내서 사용할 수 있다. 이 객체는 모든 클라이언트에 의해 공유된다.



## MVC

**xxxVO - Value Object - 값을 보관하는 용도의 객체**

**xxxDAO - Data Access Object - DB 연동기능(JDBC)을 지원하는 객체**

**Service(xxxBiz) - Service Object - 이런 저런 서비스 로직을 지원하는 객체**

1.  mvc 라는 새로운 Dynamic Web Project 생성
2.  이 프로젝트에서 생성되는 소스(텍스트)들의 인코딩 정보를 utf-8로 설정
3. mvc 프로젝트를 톰갯 서버에 컨텍스트로 등록
4. src 폴더에 controller, model 패키지 생성
5. WebContent 폴더에 images, jsexam 폴더 생성
6. 강사컴퓨터 교육자로 폴더에서 htmlexam 폴더를 복사하여 WebContent에 붙인다.

- lottoForm.html -> htmlexam, LottoServlet2.java -> controller를 복사하여

#### 실습

```

```

