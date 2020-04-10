# Day1, Day2 JSP

## JSP : JavaServer Pages	

```
CGI		 -->	   ASP, PHP
Servlet	  -->	   JSP ----> 실행시 Servlet으로 변경됨(최초한번만)
(1998)			  (1999)
자바+HTML	          HTML+JSP태그+약간의Java코드
----------------------------------------------------> MVC 개발패턴
												 Servlet + JSP
												 요청      응답
```

1. 내장 객체 (JSP는 HttpSession request.getSession();가져다 사용할 필요없고 내장 되어 있다.)

   9개가 있다.

   - request, response, session, out, application, config, exception, page, pageContext
     - page : this와 같다.
     - exception : 아무곳에서 사용할 수 없다. 나머지는 필요할 때 언제든지 사용가능

2. JSP 태그

   ​        <%@   %>,   <%! %>,     	 	 <%= %>,                      <% %>,             <%-- --%>

   ​	    지시자태그   선언문태그   		 표현식태그                수행문태그          주석태그

   ​                           멤버변수를 선언   (out.print와 같다.)    (if문 for문 같은것들)

   ​                           ------------------------------------------------------------------------스크립트 태그(자바 언어 사용가능)

   - <%@   %>  - **(page 지시자태그)**

     - Converter라는것이 jsp소스를 servlet으로 변경해준다.

     - <%-- errorPage는 실행하다가 에러가 생겼을때 발생 가능 이 구문이 에러면 해당 안된다. --%>

     - (<%@ page 속성명 ="속성값", ....   %>)

       속성명 : import, language, contentType, pageEncoding, errorPage, isErrorPage, session, buffer, isELIgored ...

   - <%@ incude file="포함하려는대상파일의로컬URL"   %> -** (include 지시자태그)**

     포함하는 위치 : 이 지시자태그가 사용된 위치

     포함하는 시기 : JSP를 Servlet으로 변환하기 전

     포함하는 대상 : html, jsp, jspf(f: fragment조각):또다른 jsp

     Servlet으로 변환하기전에 포함시켜서 함수마냥 사용할수있다.

3. **액션태그**(자바 코드를 대신할 때 사용)

   <jsp:include />, <jsp:forward />, <jsp:param   />...

   ​                          -------------------.

   ​                          servlet의 RequestDispatcher

4. 커스텀 태그 - 스크립트 코드와 EL을 혼합해서 사용하는 대신 또 다른태그를 만들어서 사용할 수 있도록 지원한다.

```
include action 태그로 : 2개의 서블릿 : 동적 포함, 다른 servlet이나 프로그램이어도 된다.
include 지시자 태그로 : 1개의 서블릿 : 정적 포함
```

**html 주석으로 막혀있으면 jsp문을 무조건 실행된다.**

Servers  -> Tomcat v9.0 Servet at localhost -> server.xml 내부에 reloadable = true이면 계속 리로드한다 개발이 끝나면 이것을 false로 변경한다.

Servlet 단점: 출력하는것이 제일 불편하다.



#### [변경된 servlet 파일을 찾아볼수 있다.]

C:\Oliver_C\eclipse-workspace\.metadata\.plugins\org.eclipse.wst.server.core\tmp0\work\Catalina\localhost\sedu\org\apache\jsp\jspexam



##### JSP는 기본은 Get, Post를 한번에 사용할 수 있는 Service이다.

##### 각각의 태그에 맞춰서 같은 형식으로 Servlet으로 변경된다.

##### request.getHeader("referer")    :    실행한 url을 알수있다.

#####  import 문 처리 여러개 가능 한개씩 가능 <%@ page import ="java.time.LocalDateTime, java.time.format.DateTimeFormatter" %>

#### 실습 exam1

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
<h1>JSP 맛보기</h1>
<hr>
<h3>현재 시간 정보 : <%= java.time.LocalDateTime.now() %></h3>
</body>
</html>
```

#### 실습 exam2

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
<%! int member_v = 0; %> <%-- 전역변수 --%>
<%-- 지역변수 --%>
<% 
	int local_v = 0;  // 지역변수
	member_v += 10;
	local_v +=10;
%>  
<ul>
	<li>멤버 변수<%= member_v %></li> <!-- 식만 올수있다. 대입연산자에 오른쪽에 있는것만 -->
	<li>로컬 변수<%= local_v %></li>

</ul>
</body>
</html>
```

#### 실습 exam3

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
<h1>표현식 태그 테스트</h1>
<hr>
<% int num = 10; %>
<ul>
	<li><%= 100 %></li>
	<li><%= num %></li>
	<li><%= ++num %></li>
	<li><%= num*2 %></li>
	<li><%= "가나다".length() %></li>
	<li><%= num % 2 == 0 %></li>
	<li><%= request.getParameter("stname") %></li> <!-- JSP에서는 HttpRequest를 바로 사용가능 -->
	<li><%= new java.util.Date(session.getCreationTime()) %></li>
	<li><%= application.getServerInfo() %></li>

</ul>
</body>
</html>
```

#### 실습 exam4

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
<h1>Query Character Input(GET&amp;POST)</h1>
<hr>
<%
   if (request.getMethod().equals("Post")){
      request.setCharacterEncoding("utf-8");
   }
%>

<h2> 당신의 이름은 <%= request.getParameter("name") %></h2>
<a href="<%= request.getHeader("referer") %>"> 입력 화면으로</a>

</body>
</html>
```

#### 실습 exam5

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>선언문 태그</title>
</head>
<body>
<h1>Query 문자열 추출(GET&amp;POST)</h1>
<hr>
<%!
	int multiply(int n1, int n2){
		return n1 * n2;
	}
%>
<%
	int result = 0;
	if(request.getMethod().equals("GET")){
		request.setCharacterEncoding("utf-8");
	
%>
		<h3>숫자 2개를 입력하세요</h3>
		<form method ="post" action="/sedu/sjexam/exam5.jsp">
			숫자 1 <input type="number" name="su1"><br>
			숫자 2 <input type="number" name="su2"><br>
			<input type="submit">
		</form>
<%
	} else{
		int su1 = Integer.parseInt(request.getParameter("su1"));
		int su2 = Integer.parseInt(request.getParameter("su2"));
		result = multiply(su1, su2);
	
%>
		<h2>수행 결과: <%= result %></h2>
		<%-- <%= request.getHeader("referer") %>는 그 html파일의 주소로 돌아간다. --%>
		<a href="<%= request.getHeader("referer") %>"> 입력 화면으로 </a>
<%
	}
%>
</body>
</html>
```



**xxxVO - Value Object - 값을 보관하는 용도의 객체**

**xxxDAO - Data Access Object - DB 연동기능(JDBC)을 지원하는 객체**

**Service(xxxBiz) - Service Object - 이런 저런 서비스 로직을 지원하는 객체**



