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

-----------

#### 실습 lottoForm.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
h2{
	color:red;
	padding : 5px 5px;
}
</style>
</head>
<body>

<form method="get"action="/mvc/lotto2">
	<h2>로또 번호를 맞춰 보세요!!!</h2>
	1부터 6까지의 숫자를 입력 하세요 : <input type="number" name="lottoNum" min=1 max=6>
	   <input type="image" src="http://localhost:8000/sedu/jspexam/click_image.png" alt="Submit" style="width:50px;height:15px">
	   
</form>

</body>
</html>
```

#### 실습 LottoServlet2.java

```java
package controller;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import model.vo.LottoVO;

@WebServlet("/lotto2")
public class LottoServlet2 extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String sendnum = request.getParameter("lottoNum");
		HttpSession session = request.getSession();
		if(session.getAttribute("cnt") == null) {
			session.setAttribute("cnt", new int [1]);
		}
		int [] session_v = (int[])session.getAttribute("cnt");
		session_v[0]+=1;
		int picknum = Integer.parseInt(sendnum);
		int rannum = (int)(Math.random()*6)+1;
		System.out.println("입력한 숫자 : "+picknum + "\n"+ "랜덤 숫자 : "+rannum);
		
		LottoVO vo = new LottoVO();
		LocalDateTime ctime = LocalDateTime.now();
		DateTimeFormatter formatter = 
				                  DateTimeFormatter.ofPattern("hh시 mm분");	
		if(session_v[0]>=4) {
			vo.setMsg("더 이상 응모할 수 없어요...ㅠㅠ 브라우저를 재기동한 후에 응모하세요");
			vo.setImgUrl("/images/sad.png" );
		} else {	
			if(picknum==rannum) {
				vo.setMsg(ctime.format(formatter) + "에 당첨!! 추카추카~");
				vo.setImgUrl("/images/congraturation.png" );				
				session_v[0]=10;
			} else {
				vo.setMsg(ctime.format(formatter) + "에 당첨 실패!! 아쉽아쉽~");
				vo.setImgUrl("/images/sorry.png" );
				vo.setLinkDisplay(true);				
			}
		}
		request.setAttribute("lotto", vo);
		RequestDispatcher impossible = request.getRequestDispatcher("/jspexam/lottoView.jsp");
		impossible.forward(request, response);
	}
}
```

#### 실습 lottoView.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="model.vo.LottoVO"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	// request, session 객체를 꺼낼 때는 obj라 형변환 해주어야한다.
	LottoVO vo = (LottoVO)request.getAttribute("lotto");
%>
<h1><%= vo.getMsg() %></h1>
<%
	if(vo.getImgUrl() != null){	
%>
		<img src="<%= vo.getImgUrl() %>" width = "100"><br><br>
<%
	}
%>

<%
	if(vo.isLinkDisplay() == true){	
%>
		<a href ="<%= request.getHeader("referer") %>">로또응모</a>  <%-- 접속 경로 --%>
<%
	}
%>
</body>
</html>
```

----------

#### 실습 eduForm.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	h2{
		padding-top : 30px;
		padding-left : 10px;
	}
	section{
		margin-left : auto;
		margin-right : auto;
		width : 500px;
		height : 300px;
		background: radial-gradient(#ff5050, #99ccff, #0066ff, #ff9933);
		padding-left : 20px;
	}
</style>
</head>
<body>
<form method="post" action ="/mvc/eduservlet">
	<section>
		<h2>성적을 입력하시오.</h2>
		<hr>
		이름: <input type="text" name = "gname" value=""><br>
		평균점수: <input type="number" name = "gavg" value="" style="margin-top : 5px;"><br>
		<input type="submit" value ="전송" style="margin-top : 5px;">
		<input type="reset" value="재작성" style="margin-top : 5px;">
	</section>
</form>
</body>
</html>
```

실습 EduServlet.java

```java
package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/eduservlet")
public class EduServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		String gname = request.getParameter("gname");
		int gavg = Integer.parseInt(request.getParameter("gavg"));
		
		String url = "";
		if(gavg >= 90) {
			url = "jspexam/gradeA.jsp";
		}
		else if(gavg >= 80 && gavg < 90) {
			url = "/jspexam/gradeB.jsp";
		}
		else if(gavg >= 70 && gavg < 80) {
			url = "/jspexam/gradeC.jsp";
		}
		else {
			url = "/jspexam/gradeD.jsp";
		}
		request.setAttribute("gname", gname);
		RequestDispatcher sendFoward = request.getRequestDispatcher(url);
		sendFoward.forward(request, response);
	}

}
```

#### 실습 gradeA, B, C, D.jsp

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
<%-- <%
	String gname = request.getAttribute("gname").toString();
%> --%>
<h2>${param.gname}님은 A등급입니다. 우수한 성적이네요</h2>
<%-- <a href="/mvc/htmlexam/eduForm.html">성적 화면 입력으로</a> --%>
<a href ="<%= request.getHeader("referer") %>">성적 화면 입력으로</a>
</body>
</html>
```

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
<%
	String gname = request.getAttribute("gname").toString();
%>
<h2><%= gname+"님은 B등급입니다. 우수한 성적이네요"%></h2>
<a href ="<%= request.getHeader("referer") %>">성적 화면 입력으로</a>
</body>
</html>
```

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
<%
	String gname = request.getAttribute("gname").toString();
%>
<h2><%= gname+"님은 C등급입니다. 우수한 성적이네요"%></h2>
<a href ="<%= request.getHeader("referer") %>">성적 화면 입력으로</a>
</body>
</html>
```

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
<%
	String gname = request.getAttribute("gname").toString();
%>
<h2><%= gname+"님은 D등급입니다. 우수한 성적이네요"%></h2>
<a href ="<%= request.getHeader("referer") %>">성적 화면 입력으로</a>
</body>
</html>
```

----------

#### 실습 xxxVO

#### 실습 memberForm.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	h1{
		text-shadow : 10px 10px 5px lightgray;
	}
	form{
		margin-left : 10px;
	}
	p > input{
		text-radius : 10px;
		border-radius: 30px;
		width : 300px;
		height : 25px;
	}
</style>
</head>
<body>
<form method="post" action="/mvc/memberservlet">
	<h1>회원 정보를 입력하십시오.</h1>
	<hr>
	<p><input type="text" name="gname" placeholder="이름을 입력하세요"></p>
	<p><input type="tel" name="gphone" placeholder="전화번호를 입력하세요" pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}"></p>
	<p><input type="text" name="gmyid" placeholder="계정을 입력하세요"></p>
	<p><input type="password" name="gmypwd" placeholder="패스워드를 입력하세요"></p>
	<input type="submit" style="border-radius: 10px; width : 60px; height : 30px; font-weight:bold" value="등록">
	<input type="reset" style="border-radius: 10px; width : 60px; height : 30px; font-weight:bold" value="재작성">
</form>

</body>
</html>
```

```java
package model.vo;

public class MemberVO {
	private String mName;
	private String mPhoneNumber;
	private String id;
	private String pwd;
	
	public String getmName() {
		return mName;
	}
	public void setmName(String mName) {
		this.mName = mName;
	}
	public String getmPhoneNumber() {
		return mPhoneNumber;
	}
	public void setmPhoneNumber(String mPhoneNumber) {
		this.mPhoneNumber = mPhoneNumber;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPwd() {
		return pwd;
	}
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}
	
}
```

```java
package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.vo.MemberVO;

@WebServlet("/memberservlet")
public class MemberServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		MemberVO vo = new MemberVO();
		
		String gname = request.getParameter("gname");
		String gphone = request.getParameter("gphone").replaceAll("[^0-9]","");
		String gmyid = request.getParameter("gmyid");
		String gmypwd = request.getParameter("gmypwd");
		
		//method로 만들면 good
		if(gname.equals("")) vo.setmName("없음");
		else vo.setmName(gname);
		
		if(gphone.equals("")) vo.setmPhoneNumber("없음");
		else vo.setmPhoneNumber(gphone);
		
		if(gmyid.equals("")) vo.setId("없음");
		else vo.setId(gmyid);
		
		if(gmypwd.equals("")) vo.setPwd("없음");
		else vo.setPwd(gmypwd);
		
		request.setAttribute("member", vo);
		RequestDispatcher sendFoward = request.getRequestDispatcher("/jspexam/memberView.jsp");
		sendFoward.forward(request, response);

	}
}
```

```jsp
<%@page import="model.vo.MemberVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>스크립트 태그</h1>
<!-- 객체 꺼낼때 형변환은 필수이다. -->
<% MemberVO vo = (MemberVO)request.getAttribute("member"); %> <!-- getAttribute는 가져올때 사용 client가 아닐때 client로 부터 가져오는 것은 getParameter를 사용한다. -->
<h1>회원  정보</h1>
<hr>
<ul>
 <li>회원 이름 : <%= vo.getmName() %></li>
 <li>회원 계정 : <%= vo.getId() %></li>
 <li>회원 암호 : <%= vo.getPwd() %></li>
 <li>회원 전화번호 : <%= vo.getmPhoneNumber() %></li>
</ul>
<hr>

<h1>액션 태그</h1>
<%-- request 속성에서 찾을거니까 scope에 쓴다. --%>
<%-- useBean은 객체가 없으면 생성하는 역할까지 할 수 있다. --%>
<jsp:useBean id= "member" class="model.vo.MemberVO" scope="request"/>
<h1>회원  정보</h1>
<hr>
<ul>
<%-- property는 get 빼고 바로 첫 문자가 대문자이면 소문자로 변경 --%>
 <li>회원 이름 : <jsp:getProperty name="member" property="mName"/></li>
 <li>회원 계정 : <jsp:getProperty name="member" property="id"/></li>
 <li>회원 암호 : <jsp:getProperty name="member" property="pwd"/></li>
 <li>회원 전화번호 : <jsp:getProperty name="member" property="mPhoneNumber"/></li>
</ul>
<hr>

<h1>표현 언어(EL)</h1>

<h1>회원  정보</h1>
<hr>
<ul>
 <li>회원 이름 : ${requestScope.member.mName}</li>
 <li>회원 계정 : ${requestScope.member.id}</li>
 <li>회원 암호 : ${requestScope.member.pwd}</li>
 <li>회원 전화번호 : ${requestScope.member.mPhoneNumber}</li>
</ul>
<hr>

</body>
</html>
```

-------

#### 실습 product.html (plus EL & AJAX)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
img {
	width: 300px;
	height: 300px;
}

button {
	width: 150px;
	height: 40px;
	font-weight: bolder;
	border-radius: 10px;
	border: 2px solid black;
}
</style>
</head>
<body>
	<h1>구매하고자 하는 상품을 선택하십시오.</h1>
	<hr>
	<a href="/mvc/productservlet?pid=p001"><img
		src="/mvc/images/apple.gif" /></a>
	<a href="/mvc/productservlet?pid=p002"><img
		src="/mvc/images/banana.jpg" /></a>
	<a href="/mvc/productservlet?pid=p003"><img
		src="/mvc/images/halabong.jpg" /></a>
	<button>장바구니 비우기</button>
	<h2 id="output"></h2>
	<script>
		var domButton = document.getElementsByTagName("button")[0];

		function cleanCart() {
			request = new XMLHttpRequest();
			request.onload = function() {
				if (request.status == 200) {
					//console.log(request.responseText);
					console.log("success");

					var jsObj = JSON.parse(request.responseText);
					//console.log(jsObj +" -> jsobj");
					var target = document.getElementById('output');
					//console.log(jsObj.pid);

					if (jsObj.msg) {
						target.innerHTML = "장바구니가 비어졌어요!";
					}

				}
			};
	    	request.open('GET', '/mvc/productservlet' + "?pid=" + "del", true);
	    	request.send(); // GET방식은 send 메서드에 아규먼트가 있으면 안된다.
		}

		domButton.addEventListener("click", cleanCart);
	</script>
</body>
</html>
```

```java
package model.vo;

public class ProductVO {
	private int halabongCnt;
	private int bananaCnt;
	private int appleCnt;
	
	public int getHalabongCnt() {
		return halabongCnt;
	}
	public void setHalabongCnt(int halabongCnt) {
		this.halabongCnt += halabongCnt;
	}
	public int getBananaCnt() {
		return bananaCnt;
	}
	public void setBananaCnt(int bananaCnt) {
		this.bananaCnt += bananaCnt;
	}
	public int getAppleCnt() {
		return appleCnt;
	}
	public void setAppleCnt(int appleCnt) {
		this.appleCnt += appleCnt;
	}	
}
```

```java
package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import model.vo.ProductVO;

@WebServlet("/productservlet")
public class ProductServlet extends HttpServlet {
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");

	    String pid = request.getParameter("pid");
	    int num = 0;
	    
	    if(pid != null)
	    	if(!pid.equals("del")) {
	    		num = Integer.parseInt(pid.replaceAll("[^0-9]", ""));
	    	}

		HttpSession session = request.getSession();
		if(session.getAttribute("cnt") == null) {
			session.setAttribute("cnt", new ProductVO());
		}
		ProductVO vo = (ProductVO)session.getAttribute("cnt");
		//System.out.println(session.getAttribute("cnt"));
		String url;
	    if(num == 1) {
	    	vo.setAppleCnt(1);
	    	url = "/jspexam/productView.jsp";
	    }else if(num == 2) {
	    	vo.setBananaCnt(1);
	    	url = "/jspexam/productView.jsp";
	    }else if(num == 3){
	    	vo.setHalabongCnt(1);
	    	url = "/jspexam/productView.jsp";
	    }
	    else {
	    	session = request.getSession(false);
	    	if(session != null)
	    		session.invalidate();
	    	url = "/jspexam/delProduct.jsp";
	    	System.out.println("del");
	    }
	    
		request.setAttribute("product", vo);
		RequestDispatcher sendFoward = request.getRequestDispatcher(url);
		sendFoward.forward(request, response);
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="model.vo.ProductVO" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	a{
		background : linear-gradient(to left, green, #ff66cc, yellow);
		font-size : 1.2em;
	}
</style>
</head>
<body>
<% ProductVO vo = (ProductVO)session.getAttribute("cnt"); %>
<h1>선택된 상품 정보는 다음과 같습니다.(스크립트 태그)</h1>
<hr>
<h2>선택된 사과의 개수: <%= vo.getAppleCnt() %></h2>
<h2>선택된 바나나의 개수: <%= vo.getBananaCnt() %></h2>
<h2>선택된 한라봉의 개수: <%= vo.getHalabongCnt() %></h2>

<h1>선택된 상품 정보는 다음과 같습니다.(액션 태그)</h1>
<hr>
<jsp:useBean id="cnt" class="model.vo.ProductVO" scope="session"/>
<h2>선택된 사과의 개수: <jsp:getProperty name="cnt" property="appleCnt"/></h2>
<h2>선택된 바나나의 개수: <jsp:getProperty name="cnt" property="bananaCnt"/></h2>
<h2>선택된 한라봉의 개수: <jsp:getProperty name="cnt" property="halabongCnt"/></h2>


<h1>선택된 상품 정보는 다음과 같습니다.(표현 언어)</h1>
<hr>
<h2>선택된 사과의 개수: ${sessionScope.cnt.appleCnt}</h2>
<h2>선택된 바나나의 개수: ${sessionScope.cnt.bananaCnt}</h2>
<h2>선택된 한라봉의 개수: ${sessionScope.cnt.halabongCnt}</h2>
<%-- <a href="/mvc/htmlexam/product.html">상품 선택화면</a> --%>
<%-- <% System.out.println(request.getHeader("referer")); %> --%>
<%-- <a href ="<%= request.getHeader("referer") %>">상품 선택화면</a> --%>
<a href ="${header.referer}">상품 선택화면</a>

</body>
</html>
```

```jsp
<%@ page contentType="text/json; charset=utf-8"%>
{
	"msg" : "장바구니가 비어졌어요!"
}
```

------------------------



