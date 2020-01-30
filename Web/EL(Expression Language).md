# EL(Expression Language)

특정
스코프 영역에 보관되어 있는 객체를 추출하여 이 객체의 값 또는 속성 값을 추출하여 표현 하고 하는 경우 사용된다 . 적절한 Java 코드와 함께 표현식 태그를 사용해도 되지만 JSP 가 추가로 지원하는 Expression Language 라는 구문으로 좀 더 간단하게 구현하는 것이 가능하다
EL은 $ 와 블록 ({ 으로 구현하는 것으로 표현하는 것과 관련된 연산자 와 EL 만의 내장 객체를 사용할 수 있다 . Query 문자열을 추출하여 표현하는 경우도 다음과 같이 스크립 팅 태그를 사용하는 것보다 간단하게 구현 한다

```html
<% out.println(request.getParameter("q")); %>
<%= request.getParameter("q") %>
${param.q} 또는 ${param["q"]}
```

- EL(Expression Language) 의 내장 객체
  pageContext - PageContext 객체
  pageScope - page 스코프에 포함된 객체들
  requestScope - request 스코프에 포함된 객체들
  sessionScope - session 스코프에 포함된 객체들
  applicationScope - application 스코프에 포함된 객체들
  param - HTTP 의 파라메터들
  paramValues - 한 파라메터의 값들
  header - 헤더 정보들
  headerValues - 한 헤더의 값들
  cookie - 쿠키들
  initParam - 컨텍스트의 초기화 파라미터들

HttpSession 객체에 cart 라는 명칭으로 저장된 객체의 getApple() 을 호출하여 리턴된 결과를
표현하려면 다음과 같이 구현한다
${ sessionScope.cart.apple } 또는 ${ cart.apple}



- EL 에서의 . 연산자
  변수명 .xxx
  (1) 변수의 참조 대상이 일반 Java 객체이면 getXxx() 를 호출한 결과가 된다.
  (2) 변수의 참조 대상이 Map 객체이면 get(xxx) 을 호출한 결과가 된다.

#### elexam1

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>EL 테스트</title>
</head>
<body>
<h2>EL의 연산자들</h2>
<hr>
\${200+100} :  ${200+100} <br> 
\${200-100} :  ${200-100} <br>
\${200/100} :  ${200/100} <br>
\${200>100} :  ${200>100} <br>
\${200==100} :  ${200==100} <br>
\${200!=100} :  ${200!=100} <br>
<%--\${ '10' - 10 } : ${ '10' - 10 }<br> 
\${10 * "10" } : ${10 * "10" }<br>  
\${40 div 5 } : ${40 div 5 }<br>--%>
\${40 mod 5 } : ${40 mod 5 }<br> 
\${ 10 eq 10 } : ${ 10 eq 10 }<br> 
\${ 10 lt 10 } : ${ 10 lt 10 }<br> 
\${ 10 gt 10 } : ${ 10 gt 10 }<br>
\${ 10 le 10 } : ${ 10 le 10 }<br>
\${ 10 ge 10 } : ${ 10 ge 10 }<br>
\${10 > 5?'A':'B'} : ${10 > 5?'A':'B'}<br>
\${100 + 200 + 300 } : ${100 + 200 + 300 }<br> <!-- +는 무조건 덧셈 -->
\${100 += 200 += 300 } : ${100 += 200 += 300 }<br> <!-- += 문자열 결합 -->
\${"EL" += 12 += 34 += "-문자열 결합연산" } : ${"EL" += 12 += 34 += "-문자열 결합연산" }
</body>
</html>
```

#### elexam2

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>EL 테스트</title>
</head>
<body>
<h2>EL의 Query 문자열 추출</h2>
<hr>
전달된 메시지의 존재 여부 : ${ !empty param.message }<hr> <!-- empty : 비어있으면 -->
전달된 메시지의 내용은 ${param.message} 입니다.<br> <!-- EL은 null이면 아무것도 표현하지 않고 나온다. -->
전달된 메시지의 내용은 ${param["message"]} 입니다.<br>
</body>
</html>
```

#### elexam3

EL 변수는 특정 scope 안에 내제되있는 변수들이다.

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>EL 테스트</title>
</head>
<body>
<h2>EL 변수</h2>
<hr>
name 변수의 값 : ${name}<br>
<% String name="듀크"; %>
name 변수의 값(표현식 태그) : <%= name %><br>
name 변수의 값(EL) : ${name}<br> <!-- java 변수 접근 불가능 -->
<% pageContext.setAttribute("name", "자바");  %>
name 변수의 값 : ${name}<br> <!-- java 변수 접근 가능 (pageScope영역을 먼저 찾기 때문에)-->
pageScope.name 변수의 값 : ${pageScope.name}<br>
<hr>
<% pageContext.setAttribute("number", 100); %>
number 변수의 값 : ${number}<br>
pageScope.number 변수의 값 : ${pageScope.number}<br>
number 변수의 값에 23을 더한 값 : ${ number + 23 }
</body>
</html>
```

#### elexam4

```java
package jspbean;

public class LanguageInfoBean {
	public static String name = "자바";
	
	public static int getBirthYear() {
		return 1996;
	}
	public static String getKindInfo() {
		return name +"는 OOP 프로그래밍 언어입니다.";
	}
}
```

```java
package jspbean;

import java.time.LocalTime;

public class TestBean {
	private String name;
	private String time;
	public TestBean() {
		LocalTime lt = LocalTime.now();
		time = lt.getHour()+ "시 " +lt.getMinute() +"분 " +lt.getSecond() +"초";
		name="Guest";
	}
	public TestBean(String name) {
		LocalTime lt = LocalTime.now();
		time = lt.getHour()+ "시 " +lt.getMinute() +"분 " +lt.getSecond() +"초";
		this.name=name;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getTime() {
		return time;
	}
}
```

```java
package jspbean;
import java.time.LocalDate;

public class Today {
	private int year;
	private int month;
	private int date;
	public Today() {
		year = LocalDate.now().getYear();
		month = LocalDate.now().getMonthValue();
		date = LocalDate.now().getDayOfMonth();
	}
	public int getYear() {
		return year;
	}
	public int getMonth() {
		return month;
	}
	public int getDate() {
		return date;
	}	
}
```

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"  %>
<%@ page import="jspbean.*, java.util.ArrayList"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"> 
<title>EL 테스트</title> 
</head>
<body>
<h2>객체의 getter 메서드, 컬렉션 객체의 원소, 클래스의 정적 멤버 사용</h2> 
<hr>
<%
pageContext.setAttribute("today", new Today()); // EL 에서는 today를 변수로 취급
ArrayList<TestBean> mylist = new ArrayList<>();
mylist.add(new TestBean("둘리"));
mylist.add(new TestBean("또치"));
mylist.add(new TestBean("도우너"));
pageContext.setAttribute("list", mylist); // EL 에서는 list를 변수로 취급
%>
<h3>객체의 멤버 접근</h3>
${ today.year }년 ${ today.month }월 ${ today.date }일 <!-- today.getYear와 같다. -->
<h3>컬렉션의 객체 사용</h3>
${ list[0].name }-${ list[1].name }-${ list[2].name }<br> <!-- list[0].getName와 같다. -->
<h3>클래스의 정적 멤버 사용</h3>
${ LanguageInfoBean.name }<br> <!--  -->
${ LanguageInfoBean.getBirthYear() }<br>
${ LanguageInfoBean.getKindInfo() }<br> 
</body>
</html>
```

