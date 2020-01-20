# Spring

- Web Client : HTML5, CSS3, JavaScript ---> edu

- Web Server : Servlet, JSP, (JDBC), Spring FW, MyBatis FW

  ​					  (Junit FW, Log4J) - Java  ---> sedu

#### 환경구축

1. edu -> 우클릭-> new -> New Dynamic Web Project -> 생성
2. tomcat 연동
3. sedu -> Java Resources -> new -> servelet -> ->

![image-20200116113006456](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200116113006456.png)

Servlet은 Tomcat이 기동할때 읽는다.

## Servlet

- 1998년 가을에 발표된 기술

  CGI(Common Gateway Interface) - 웹의 표준 구현언어 투명성

  ---> Fast CGI

  ---> Servlet

- Server Side Applet(Applet : 웹 브라우저에서 실행되는 Java 프로그램)

- 구현상의 특징 

  1. HttpServlet을 상속해야 한다.

  2. main() 구현하지 않는다. (main() 메서드를 담고 있는 메인 클래스는 Tomcat이 내장)

  3. 수행하는 동안 호출되는 메서드가 정해져 있는데 이 때 호출되는 메서드는 init(), service(), destroy(), doGet(), doPost() 등이다. 하여 이 메서드들을 선택적으로 오버라이딩해서 구현한다.

     doGet() -> 은 url을 사용해야한다.

     doPost() -> 은 url을 사용하면 안된다.(HTTP 상태 405 메세지 나온다.)

  4. 서블릿에서 수행 결과를 출력 할 때

     - 요청해온 브라우저로의 출력(응답) 
       - HttpServletResponse의 getWriter()를 호출해서 클라이언트로의 출력 스트림 객체 생성해서 출력
     - 표준 출력 : System.out.println()

  5. 서블릿이 수행하는데 필요한 데이터를 요청 보내오는 클라이언트로 부터 전달받을 수 있다. 이 때 전달받는 데이터를 쿼리 문자열이라 한다.

     HttpServletRequest 의 getPrameter(): String

     또는 getParameterValue():String[]를 사용한다. 전자 단수 후자 복수

- 수행상의 특징

  1. 서블릿을 요청할 때는 "/컨택스트루트명/서블릿의매핑명" 형식의 URI를 사용한다.

  2. 서블릿의 요청은

     - 서블릿을 요청하는 URL 문자열을 브라우저의 주소 필드에 입력해서 직접 요청
     - \<a> 태그로 요청 : GET
     - \<form> 태그를 통해서 요청:GET/POST

  3. 서블릿 객체는 한 번 생성되는 서버가 종료되거나 컨택스트가 리로드 될 때까지 객체 상태를 유지한다.(한번 객체 생성하면 계속 그 객체를 사용하고 두개 세개 객체 생성하지 않는다.)

  4. 여러 클라이언트가 동일한 서블릿을 동시 요청하면 하나의 서블릿 객체를 공유해서 수행한다.

  5. 최초 요청시의 수행 흐름

     init(),  servlet() -> doGet(), destroy()

     ​	  				  -> doPost()

core 패키지 : FlowServlet(/flow)

​					 MemberLocalServlet

​					QueryServlet(/query) - GET

Web Server : Web 통신에서 서버역할을 수행하는 프로그램(Http Server)

Web Server(html 수행) + Application Server(Servlet, JSP를 수행) = Web Application Server = WAS

TOMCAT(대표적인 free WAS) = WAS = 코요테(웹서버) + 카탈리나(어플리케이션서버)



**console에 lifeCycle 에러가 나면 매핑명이 같은것이다.**

## URI ( Uniform Resource Identifier)

- 통합 자원 식별자
- 인터넷에 있는 자원을 나타내는 유일한 주소이다.
- URI의 존재는 인터넷에서 요구되는 기본조건으로서, 인터넷 프로토콜에 항상 붙어다님
  - ex) [http://www.naver.com](http://www.naver.com/) (http프로토콜임을 명시하고 있음)
- URI의 하위개념에 URL,URN이 포함되어 있다.
- URI의 보편적인 형태가 URL인데, URI의 부분집합으로 볼 수 있다.
  - 자원에 접근하기 위해 사용되는 절차
  - 어떤 자원을 가지고 있는 특정한 컴퓨터
  - 컴퓨터 상의 유니크한 자원의 이름(파일명)
- http://test.com/test.pdf?docid=111 이라는 주소는 URI이지만 URL은 아니다.
  - http://test.com/test.pdf 까지만 URL임(주소의 위치)
  - docid=111이라는 쿼리스트링의 값에 따라 결과가 달라지게됨, 따라서 식별자 역할을 하고 있음
- http://test.com/test.pdf?docid=111 ,http://test.com/test.pdf?docid=112는 같은 URL을 가지고 다른 URI를 가짐

## URN (Uniform Resource Name)

- 위치와 상관없이 리소스의 이름값을 이용해서 접근하는 방식
- 노출된 URL은 http://blog.com/syun/222 인데, http://blog.com/syun/list/323으로 요청을 보내면 404 response를 받는다. 이를 보완하기 위해서 위치 정보와는 무관하게 리소스를 찾을 수 있게 해주는 방식임
- 해당 리소스의 위치정보가 아닌 실제 리소소의 이름으로 사용하는 방식

## 정리

- URI에는 URL,URN이 포함되어 있다. URL은 URI이지만, URI는 URL이 아니다.
- URL은 인터넷 상의 자원 위치를 나타냄
- URI는 인터넷 상의 자원을 식별하기 위한 문자열의 구성

#### 실습 Servlet FlowServlet

```java
package core;

import java.io.IOException;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/flow")
public class FlowServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public void init(ServletConfig config) throws ServletException {
		System.out.println("init() 호출");
	}

	public void destroy() {
		System.out.println("destroy() 호출");
	}

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("service() 호출");
	}

}

```

#### 실습 Servlet MemberLocalServlet

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/query")
public class MemberLocalServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	int member_v = 0;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int local_v = 0;
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out = response.getWriter();
		String p1 = request.getParameter("p1");
		int p2 = Integer.parseInt(request.getParameter("p2"));
		String p3[] = request.getParameterValues("p3");
		out.print("<ul>");
		out.print("<li>p1 : " + p1 + "</il>");
		out.print("<li>p2 : " + p2 + "</il>");
		for(int i = 0; i < p3.length; i++)
			out.print("<li>p3[" + i + "] : " + p3[i] + "</li>");
		out.print("</ul>");
		out.close();
	}
}
//http://localhost:8000/sedu/query?p1=듀크&p2=24&p3=또치p3=희동&p3=도우너
```

#### 실습 Servlet QueryServlet

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/memberlocal")
public class QueryServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	int member_v = 0;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int local_v = 0;
		
		// ContentType을 먼저 작성해야 한다 반드시!!
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out = response.getWriter();
		member_v+= 10;
		local_v+= 10;
		out.print("<ul>");
		out.print("<li>멤버변수 " + member_v + "</il>");
		out.print("<li>지역변수 " + local_v + "</il>");
		out.print("</ul>");
		out.close();
	}

}
```

#### 실습 Servlet MyFirstServlet

- **문제**

  다음 기능의 서블릿클래스를 생성한다.

  (1) 클래스명 : core.MyFirstServlet
  (2) 매핑명 : /myfirst
  (3) GET 방식지원 서블릿
  (4) 기능 : name이라는 이름으로 전달되는 Query 문자열을 추출하고

                <h2> xxx 님 반가워요.. 오늘은 x요일입니다!! </h2>
      
                를 브라우저로 응답한다.
      
      name이라는 이름으로 Query 문자열이 전달되지 않은 경우에는
               GUEST 를 대신 출력한다.
      
      요일 출력하는 기능 구현시 Date 나 GregorianCalendar 말고
      LocalDate 를 사용한다.


  (5) 제출 : MyFirstServlet.java

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDate;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/myfirst")
public class MyFirstServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out = response.getWriter();
		
		String name = request.getParameter("name");
		if(name == null) name = "guest";
		
		LocalDate localDate = LocalDate.now();

		String weeks[] = {"", "월", "화", "수", "목", "금", "토", "일"};
		//무슨 요일인지?(월-1 ~일-7)
		int ansWeek = localDate.getDayOfWeek().getValue();
		
		out.print("<h2>" + name + "님 반가워요.. 오늘은 " + weeks[ansWeek] +"요일입니다!!" + "</h2>");
	}

}
```

#### 실습 Servlet GetPostServlet(with getpost.html)

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/getpost")
public class GetPostServlet extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		out.print("<h2>요청 방식 : "+request.getMethod()+"</h2>");
		out.print("<h2>Query 문자열 : "+
		                  request.getParameter("name")+"</h2>");
		out.close();
		System.out.println("GET 방식 수행");
	}
	// Post 방식은 쿼리에 노출이 되지 않는다. login 방식은 Post로 한다.
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		request.setCharacterEncoding("UTF-8");
		out.print("<h2>요청 방식 : "+request.getMethod()+"</h2>");
		out.print("<h2>Query 문자열 : "+request.getParameter("name")+"</h2>");
		out.close();
		System.out.println("POST 방식 수행");
	}
}
```

#### 실습 html getpost

- form method를 이용해서 get방식 post방식을 구분할수 있다.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>서블릿을 요청하는 다양한 방법</h1>
<hr>
<a href="/sedu/getpost?name=듀크">하이퍼링크로 요청</a>
<hr>
<form method="get" action="/sedu/getpost"> <!-- get방식으로 요청 -->
<input type="text" placeholder="이름을입력하세요" name="name" >
<input type="submit"  value="GET방식요청">
</form>
<hr>
<form method="post" action="/sedu/getpost"> <!-- post방식으로 요청 , post는 form 태그에서만 가능 그 외에는 get방식-->
<input type="text" placeholder="이름을입력하세요" name="name" >
<input type="submit"  value="POST방식요청">
</form>
</body>
</html>
```

#### 실습 Servlet QueryTestServlet

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/querytest")
public class QueryTestServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String name = request.getParameter("stname");
		String pwd = request.getParameter("pwd");
		int age = Integer.parseInt(request.getParameter("age"));
		
		String gender = request.getParameter("gender");
		
		String[] hobby = request.getParameterValues("hobby");
		String[] food = request.getParameterValues("food");
		
		String color = request.getParameter("color");
		String op = request.getParameter("op");
		
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out = response.getWriter();
		
		out.print("<h2> 전달된 내용 </h2>"); out.print("<hr>");
		
		out.print("<ul>");
		out.print("<li> 이름 : " +name+ "</li>");
		out.print("<li> 암호 : " +pwd+ "</li>");
		out.print("<li> 나이 : " +age+ "</li>");
		
		out.print("<li> 성별 : ");
			if (gender == null) {
				out.print("선택 제대로 하세요 -ㅅ-");	
			}
			else {
				out.print(gender);
			}
		out.print("</li>");
		
		out.print("<li> 취미 : ");
			if (hobby == null) {
				out.print("선택 제대로 하세요 -ㅅ-");	
			}
			else {
				for (int i=0 ; i<hobby.length ; ++i) {
					if (i == hobby.length -1) {
						out.print(hobby[i]);
						break;
					}
					out.print(hobby[i] +",");
				}
			}
		out.print("</li>");
		
		out.print("<li> 좋아하는 색 :" +(color == ""?"없음":color) +"</li>");
		out.print("<li> 좋아하는 음식 : ");
		if (food == null) {
			out.print("선택 제대로 하세요 -ㅅ-");	
		}
		else {
			for (int i = 0; i < food.length; ++i) {
				if (i == food.length - 1) {
					out.print(food[i]);
					break;
				}
				out.print(food[i] +",");
			}
		}
		out.print("</li>");
		
		
		out.print("<li> 의견 : " + op + "</li>");
		out.print("<li> 비밀1 : " + request.getParameter("h_1") + "</li>");
		out.print("<li> 비밀2 : " + request.getParameter("h_2") + "</li>");
		
		
		out.print("</ul>"); out.print("<hr>");
		out.print("<a href='http://70.12.113.164:8000/sedu/queryForm.html'>"
				+ "입력화면으로</a>");
		
		out.close();
	}

}
```

#### 실습 html querytest

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
		<!-- method를 샹략하면 GET 가독성을 위해 쓰는게 좋음 -->
	    <form method="GET" 
	    action="http://localhost:8000/sedu/querytest">
		이름 : <input name="stname" value="듀크" required><br>
		암호 : <input type="password" name="pwd"><br>
		나이 : <input type="number" name="age"><br>
		성별 : <input type="radio" name="gender" value="남자">남자
		<input type="radio" name="gender" value="여자">여자
		<br>
		
		취미 : 
		피아노 <input type="checkbox" name="hobby" value="피아노">
		수영 <input type="checkbox" name="hobby" value="수영">
		독서 <input type="checkbox" name="hobby" value="독서">
		게임 <input type="checkbox" name="hobby" value="게임">
		<br>
	
		좋아하는 색 : 
		<select name="color">
		    <option value=""></option>
			<option value="빨강색">RED</option>
			<option value="파랑색">BLUE</option>
			<option value="노랑색">YELLOW</option>
		</select>
		<br>
		
		좋아하는 음식 :
		<br> 
		<select name="food" size="4" multiple>
			<option value="라면">라면</option>
			<option value="냉면">냉면</option>
			<option value="짜장면">짜장면</option>
			<option value="햄버거">햄버거</option>
			<option value="닭강정">닭강정</option>
			<option value="육회">육회</option>
		</select>
		<br>
		
		의견 : 
		<br>
		<textarea name="op" rows="10" cols="50"></textarea><br>
		
		<!-- 사용자는 모르게 서버한테 보낸다. -->
		<input type="hidden" name="h_1" value="-ㅅ-">
		<input type="hidden" name="h_2" value="=ㅅ="> 
		
		<input type="submit" value="보내기">
		<input type="reset" value="다시작성하기">
	</form>
</body>
</html>
```

----------

querytestURI

\[http://localhost:8000/sedu/querytest?stname=%EB%A5%98%ED%81%AC&

pwd=1234&

age=5&

gender=%EC%97%AC%EC%9E%90&

hobby=%EB%8F%85%EC%84%9C&

color=%ED%8C%8C%EB%9E%91%EC%83%89&

food=%EB%9D%BC%EB%A9%B4&

food=%EB%83%89%EB%A9%B4&

food=%EC%A7%9C%EC%9E%A5%EB%A9%B4&

food=%ED%96%84%EB%B2%84%EA%B1%B0&

food=%EB%8B%AD%EA%B0%95%EC%A0%95&

food=%EC%9C%A1%ED%9A%8C&

op=%EC%A7%91%EC%97%90%EA%B0%80%EC%9E%90&

h_1=-%E3%85%85-&

h_2=%3D%E3%85%85%3D]

(http://localhost:8000/sedu/querytest?stname=류크&pwd=1234&age=5&gender=여자&hobby=독서&color=파랑색&food=라면&food=냉면&food=짜장면&food=햄버거&food=닭강정&food=육회&op=집에가자&h_1=-ㅅ-&h_2=%3Dㅅ%3D)

--------



