# Spring

ERD 무료 툴 : https://aquerytool.com/

#### 실습 spring eduForm

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
<form method="post" action ="/springedu/springedu1">
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

```java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class EduController{
	@RequestMapping("/springedu1")
	public ModelAndView proc(@RequestParam(defaultValue="0")int gavg){ // 전달할 모델이 없으면 return형을 ModelAndView이게 아니라 String으로 변경해도된다.		
		ModelAndView mav = new ModelAndView(); //ModelAndView : 뷰 객체와 모델 객체를 하나의 객체로 담음.
		String view = "";
		if(gavg >= 90) {
			view = "gradeA";
		}
		else if(gavg >= 80 && gavg < 90) {
			view = "gradeB";
		}
		else if(gavg >= 70 && gavg < 80) {
			view = "gradeC";
		}
		else {
			view = "gradeD";
		}
		mav.setViewName(view);
		return mav;
	}
	
//	@RequestMapping("/springedu1")
//	public String proc(@RequestParam(defaultValue="0")int gavg){ // 전달할 모델이 없으면 return형을 ModelAndView이게 아니라 String으로 변경해도된다.		
//		ModelAndView mav = new ModelAndView(); //ModelAndView : 뷰 객체와 모델 객체를 하나의 객체로 담음.
//		String view = "";
//		if(gavg >= 90) {
//			view = "gradeA";
//		}
//		else if(gavg >= 80 && gavg < 90) {
//			view = "gradeB";
//		}
//		else if(gavg >= 70 && gavg < 80) {
//			view = "gradeC";
//		}
//		else {
//			view = "gradeD";
//		}
//		return view;
//	}


}
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

#### 실습 Spring Calc

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form method="get" action="/springedu/calc">
	<h1>연산할 두 개의 숫자를 입력하고 연산자를 선택하시오.</h1>
	<hr>
	<input type="number" name="num1" value="숫자를 입력하세요">
	<select name="op">
	    <option value="+">+</option>
	    <option value="-">-</option>
	    <option value="*">*</option>
	    <option value="/">/</option>
	</select>
	<input type="number" name="num2" value="숫자를 입력하세요">
	<button>계산하기</button>
</form>
</body>
</html>
```

```java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class CalcController{
	@RequestMapping("/calc")
	public ModelAndView proc(@RequestParam(defaultValue="0")int num1,
			@RequestParam(defaultValue="0")int num2,@RequestParam(defaultValue="") String op){ // 전달할 모델이 없으면 return형을 ModelAndView이게 아니라 String으로 변경해도된다.		
		ModelAndView mav = new ModelAndView(); //ModelAndView : 뷰 객체와 모델 객체를 하나의 객체로 담음.
		int result = 0;
		boolean errFlag = false;
		String view = "";
		String errorMsg = "";
		switch(op) {
			case "+":
				result = num1 + num2;
				view = "calcResult";
				break;
			case "-":
				result = num1 - num2;
				view = "calcResult";
				break;
			case "*":
				result = num1 * num2;
				view = "calcResult";
				break;
			case "/":
				if(num2 == 0) {
					errFlag = true;
					errorMsg = "나눗셈 연산시 두 번째 숫자는 0일 수 없습니다!!";
					view = "errorResult";
				}
				else{
					result = num1 / num2;
					view = "calcResult";
				}
				break;
		}
		if(errFlag) mav.addObject("msg", errorMsg);
		else mav.addObject("msg", result); 
		mav.setViewName(view);
		return mav;
	}
}
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
<h1>연산 요청 결과</h1>
<hr>
<%-- <% String msg = request.getAttribute("msg").toString(); %> --%>
<%-- 결과 :<output style="color:#ff0066"> <%= msg %></output><br><br> --%>
결과 :<output style="color:#ff0066"> ${requestScope.msg}</output><br><br>
<%-- <a href="<%= request.getHeader("referer") %>">입력화면</a> --%>
<a href=" ${header.referer}">입력화면</a>

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
<%-- <% String msg = request.getAttribute("msg").toString(); %> --%>
<h1>요청을 처리하는 동안 오류가 발생했어요..</h1>
<%-- <h2> 오류의 원인 : <span style="color:#ff0066"> <%= msg %> </span> </h2><br> --%>
<h2> 오류의 원인 : <span style="color:#ff0066"> ${requestScope.msg} </span> </h2><br>
<%-- <font size="+2" color="black" >오류의원인 : </font>
<font size="+2" color="#ff0066"> <%= msg %> </font><br><br> --%>
<%-- <a href="<%= request.getHeader("referer") %>">입력화면</a> --%>
<a href="${header.referer}">입력화면</a>
</body>
</html>
```

---------

**Compiler 1.6 -> 1.8 로 디버깅하기**

--->>>프로젝트에서 properties -> project facet -> java -> combo button -> 1.8 -> 적용

--------

```java
package vo;
public class QueryVO {
	private String testName;
	private int testAge;
	private String testAddr;
	public String getTestName() {
		return testName;
	}
	public void setTestName(String testName) {
		this.testName = testName;
	}
	public int getTestAge() {
		return testAge;
	}
	public void setTestAge(int testAge) {
		this.testAge = testAge;
	}
	public String getTestAddr() {
		return testAddr;
	}
	public void setTestAddr(String testAddr) {
		this.testAddr = testAddr;
	}	
}
```

```java
package my.spring.springedu;
import java.util.Locale;
import javax.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import vo.QueryVO;
@Controller
public class QueryStringController2 {	
	@RequestMapping("/querystring5")
	public ModelAndView proc(QueryVO vo) { // 같지 않은 쿼리 문자가 오면 0으로 셋팅한다.
		ModelAndView mav = new ModelAndView();
		String name = vo.getTestName();
		int age = vo.getTestAge();
		String addr = vo.getTestAddr();
		mav.addObject("spring", name + "-" + age + "-" + addr);
		mav.setViewName("queryView3");
		return mav;
	}	
	@RequestMapping(value = "/querystring6", 
			                      method = RequestMethod.POST)
	public ModelAndView procPost(QueryVO vo) {
		ModelAndView mav = new ModelAndView();
		String name = vo.getTestName();
		int age = vo.getTestAge();
		String addr = vo.getTestAddr();
		mav.addObject("spring", name + "@" + age + "@" + addr);
		mav.setViewName("queryView3");
		return mav;
	}
	@RequestMapping("/querystring7")
	public ModelAndView proc(HttpServletRequest request) { // 쿼리를 직접 추출할수있다.
		ModelAndView mav = new ModelAndView();
		String name =request.getParameter("testName");
		int age = Integer.parseInt(request.getParameter("testAge"));
		String addr = request.getParameter("testAddr");
		mav.addObject("spring", name + "#" + age + "#" + addr);
		mav.setViewName("queryView3");
		return mav;
	}
	@RequestMapping(value="/locale.do") // 어떤 나라에 언어를 사용하느냐
	public ModelAndView proc(Locale l) {
		ModelAndView mav = new ModelAndView();
		mav.addObject("spring", "Processing locale ............"+
		       l.getDisplayCountry()+"_"+l.getDisplayLanguage());
		mav.setViewName("queryView3");
		return mav;
	}
}
```

Controller에서 매개 변수가 여러가지여도 상관없다!!

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>Get the Query String as a Model object(VO)</h1>
<hr>
<a href="/springedu/querystring5?testName=aaa&testAge=10&testAddr=bbb">querystring5-Request(Include query)</a>
<hr>
<a href="/springedu/querystring5">querystring5-Request(Exclude query)</a>
<hr>
<form method="get"  action="/springedu/querystring5">
<input type="text" placeholder="Please enter your name" name="testName" required><br>
<input type="number" placeholder="Please enter your age" name="testAge" required><br>
<input type="text" placeholder="Please enter your address" name="testAddr" required><br>
<input type="submit" value="querystring5-Request">
</form>
<hr>
<form method="post"  action="/springedu/querystring6">
<input type="text" placeholder="Please enter your name" name="testName" required><br>
<input type="number" placeholder="Please enter your age" name="testAge" required><br>
<input type="text" placeholder="Please enter your address" name="testAddr" required><br>
<input type="submit" value="querystring6-Request">
</form>
<hr>
<form method="post"  action="/springedu/querystring7">
<input type="text" placeholder="Please enter your name" name="testName" required><br>
<input type="number" placeholder="Please enter your age" name="testAge" required><br>
<input type="text" placeholder="Please enter your address" name="testAddr" required><br>
<input type="submit" value="querystring7-Request">
</form>
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
<title>JSP for response</title>
</head>
<body>
<h2>From QueryStringController1
                Forward to queryView1.jsp</h2>
<hr>
<h3>Data passed as spring name(EL) : ${ spring }</h3>
<h3>Data passed as spring name(Expression Tag) : 
                        <%= request.getAttribute("spring") %></h3>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="vo.QueryVO"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>응답용JSP</title>
</head>
<body>
<h2>Forward from QueryStringController2 to queryView2.jsp</h2>
<hr>
<%
	QueryVO vo = (QueryVO) request.getAttribute("queryVO");
    if(vo != null) {
%>
		<ul>
			<li>${ queryVO.testName }</li>
			<li>${ queryVO.testAge }</li>
			<li>${ queryVO.testAddr }</li>
		</ul>
<%
    }
%>
<h3>Total Query String : ${ spring }</h3>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>응답용JSP</title>
</head>
<body>
<h2>Forward from QueryStringController2 to queryView3.jsp</h2>
<hr>
	<c:if test="${!empty queryVO}" >
		<ul>
			<li>${ queryVO.testName }</li>
			<li>${ queryVO.testAge }</li>
			<li>${ queryVO.testAddr }</li>
		</ul>
    </c:if>
<h3>Total Query String : ${ spring }</h3>
</body>
</html>
```

-----------

#### 실습 member

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
<form method="post" action="/springedu/member">
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
package vo;

public class MemberVO {
	private String gname;
	private String gphone;
	private String gmyid;
	private String gmypwd;

	public String getGname() {
		return gname;
	}
	public void setGname(String gname) {
		this.gname = gname;
	}
	public String getGphone() {
		return gphone;
	}
	public void setGphone(String gphone) {
		this.gphone = gphone;
	}
	public String getGmyid() {
		return gmyid;
	}
	public void setGmyid(String gmyid) {
		this.gmyid = gmyid;
	}
	public String getGmypwd() {
		return gmypwd;
	}
	public void setGmypwd(String gmypwd) {
		this.gmypwd = gmypwd;
	}

}

```

```java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import vo.MemberVO;

@Controller
public class MemberController {
	

	
	@RequestMapping("/member")
	public ModelAndView proc(MemberVO vo) {
		ModelAndView mav = new ModelAndView();
		String name = vo.getGname();
		String phoneNum = vo.getGphone();
		String id = vo.getGmyid();
		String pwd = vo.getGmypwd();
		
		if(name == null || name.equals("")) vo.setGname("없음");
		else vo.setGname(name);
		
		if(phoneNum == null || phoneNum.equals("")) vo.setGphone("없음");
		else vo.setGphone(phoneNum);
		
		if(id == null || id.equals("")) vo.setGmyid("없음");
		else vo.setGmyid(id);
		
		if(pwd == null || pwd.equals("")) vo.setGmypwd("없음");
		else vo.setGmypwd(pwd);
				
		mav.addObject("member", vo);
		mav.setViewName("memberView");
		return mav;
	}

}

```

```jsp
<%@page import="vo.MemberVO"%>
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
 <li>회원 이름 : <%= vo.getGname() %></li>
 <li>회원 계정 : <%= vo.getGmyid() %></li>
 <li>회원 암호 : <%= vo.getGmypwd() %></li>
 <li>회원 전화번호 : <%= vo.getGphone() %></li>
</ul>
<hr>

<h1>액션 태그</h1>
<%-- request 속성에서 찾을거니까 scope에 쓴다. --%>
<%-- useBean은 객체가 없으면 생성하는 역할까지 할 수 있다. --%>
<jsp:useBean id= "member" class="vo.MemberVO" scope="request"/>
<h1>회원  정보</h1>
<hr>
<ul>
<%-- property는 get 빼고 바로 첫 문자가 대문자이면 소문자로 변경 --%>
 <li>회원 이름 : <jsp:getProperty name="member" property="gname"/></li>
 <li>회원 계정 : <jsp:getProperty name="member" property="gmyid"/></li>
 <li>회원 암호 : <jsp:getProperty name="member" property="gmypwd"/></li>
 <li>회원 전화번호 : <jsp:getProperty name="member" property="gphone"/></li>
</ul>
<hr>

<h1>표현 언어(EL)</h1>

<h1>회원  정보</h1>
<hr>
<ul>
 <li>회원 이름 : ${requestScope.member.gname}</li> <!-- setter 첫글자 소문자 -->
 <li>회원 계정 : ${requestScope.member.gmyid}</li>
 <li>회원 암호 : ${requestScope.member.gmypwd}</li>
 <li>회원 전화번호 : ${requestScope.member.gphone}</li>
</ul>
<hr>

</body>
</html>
```

#실습