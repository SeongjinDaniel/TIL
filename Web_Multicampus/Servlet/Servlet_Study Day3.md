# Day3 Servlet

- 요청 재지정

  요청재지정이란 클라이언트에서 요청한 페이지 대신 다른 페이지를 클라이언트가 보게 되는 기능
  으로서 redirect 방법과 forward 방법으로 나뉜다 .

  클라이언트는 노란애를 요청했지만 빨간애를 가져간다.
  노란애랑 빨간애는 같은 웹프로젝트 안에 있어야 한다.
  MVC 패턴이다.(유지보수성 확장성이 좋다) 같은 프로젝트 안에 있어야 사용가능

  - redirect : HttpServletResponse 의 sendRedirect() 메서드를 사용한다
  - forward : RequestDispatcher 의 forward() 메서드를 사용한다

#### 실습 요청 재지정 first

```java
package core;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/forward")
public class ForwardServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("ForwardServlet 수행 시작");
		// RequestDispatcher 이것은 URI형식으로 주어야한다.
		RequestDispatcher rd = request.getRequestDispatcher("/first.html"); // 컨택스트패스 이후 부분을 줘야(sedu이후)
		rd.forward(request, response);
		System.out.println("FowardServlet 수행 종료");
		
	}
}
```

#### 

```
edu
sedu
이것들을↑↑↑↑↑↑↑↑↑
OS - 폴더
Eclipse - Web Project
Tomcat - Context(Context Path : /edu, /sedu) // /ContextName
Developer - Web Application
```

#### 실습 요청 재지정 문제

다음 기능의 서블릿클래스를 생성한다.

(1) 클래스명 : core.MoveServlet
(2) 매핑명 : /move
(3) GET 방식지원 서블릿
(4) 기능 : action이라는 이름으로 전달되는 Query 문자열을 추출하고

              추출된 값이
              naver 이면 네이버 페이지로
              daum 이면 다음 페이지로
              google 이면 구글 페이지로
              추출되지 않으면 직접 다음 내용을 응답한다.
    
              <h2>전달된 쿼리 문자열이 없어서 MoveServlet이 직접 응답합니당..</h2>  
    
    http://localhost:8000/edu/move?action=naver
    http://localhost:8000/edu/move?action=daum
    http://localhost:8000/edu/move?action=google
             http://localhost:8000/edu/move

(5) 제출 : MoveServlet.java

```java
//[solution]
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/move")
public class MoveServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		String action = null;
		String str = null;
		action = request.getParameter("action"); // getParameter는 객체 가 생성된다.
		
		// null을 먼저 확인하지 않으면 nullPointException 에러가 난다. 
		// 이유는 action객체가 널이기때문에 action.equals를 비교하지 못한다.
		if(action == null){ 
			out.print("<h2>전달된 쿼리 문자열이 없어서 MoveServlet이 직접 응답합니당..</h2>");
		}
		else if(action.equals("naver")) str = "http://www.naver.com/";
		else if(action.equals("daum")) str = "http://www.daum.net/";
		else if(action.equals("google")) str = "http://www.google.com/";
		
		response.sendRedirect(str);
		out.close();
	}

}
```

#### 실습 Ajax and Servlet

```java
//[servlet]
package core;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/basket1")
public class BasketServlet1 extends HttpServlet {
	private static final long serialVersionUID = 1L;

	void Writes(String pid){
		Date today = new Date();
		SimpleDateFormat dateformat = new SimpleDateFormat("yyyyMMddHHmm");
		
		String newToday = dateformat.format(today);
		
        String path = "C:/logtest/";
        File isDir = new File(path);
        if (!isDir.exists()) {
        	isDir.mkdirs();
        }
        try (FileWriter  writer = new FileWriter(path + "mylog.txt", true);){
        	writer.append(newToday + " " + pid +"\r\n");
        } catch (IOException ioe) {
            System.out.println("파일로 출력할 수 없습니다.");
        }
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		
		String pid = request.getParameter("pid");
		Writes(pid);
		
		out.print(String.format("{\"pid\":\"%s\"}", pid));
		out.close();
	}

}
```

```html
<!--[html] -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	img{
		width : 160px;
		height : 160px;
		border : 1px ;
		border-radius : 10px;
		border : 1px solid #cc33ff;
		box-shadow: 5px 5px 5px #cc33ff;
		margin : 5px 5px;
		margin-top: 10px;
	}
	img:hover{
		transform : rotate(10deg); /*3도 만큼 회전시켜라*/
		transition : transform 1s; /*transform을 2초동안 움직여라*/
	}

	section{
		text-align : center;
	}
</style>
</head>

<body>
<!-- <form method="GET" action="http://localhost:8000/sedu/basket"> -->
	<h2 style="text-align:center">원하는 상품을 클릭해 주세요!! 마구마구^^</h2>
	<hr>	
	<section>
		<img src="/sedu/images/1.jpg" data-pid = p001> <!-- id 말고 data-int="1"를 주어도 된다. 더 잘한것임 -->
		<img src="/sedu/images/2.jpg" data-pid = p002>
		<img src="/sedu/images/3.jpg" data-pid = p003>
		<img src="/sedu/images/4.jpg" data-pid = p004>
		<img src="/sedu/images/5.jpg" data-pid = p005><br>
		<img src="/sedu/images/6.jpg" data-pid = p006>
		<img src="/sedu/images/7.jpg" data-pid = p007>
		<img src="/sedu/images/8.jpg" data-pid = p008>
		<img src="/sedu/images/9.jpg" data-pid = p009>
		<img src="/sedu/images/10.jpg" data-pid = p010>
		<div id="output" style="width:350px; margin : 10px auto"></div>
	</section>
<!-- </form> -->

     <script>	
     var button, clicks;

	    function getQueryString(){ //http://localhost:8000
		      return '../../sedu/basket1';
		}
	    
		function buttonPressed(){
			//console.log(this.getAttribute("data-pid"));
			var str = getQueryString() + "?pid=" + this.getAttribute("data-pid");
			console.log(str);

			var request = new XMLHttpRequest();
			request.onload = function() {
			 		if (request.status == 200) { // 이것은 확인해야한다.
			 			console.log(request.responseText);
			 			console.log("success");
			 			console.log(request.responseText);
			 			
			 			var jsObj = JSON.parse(request.responseText);
			 			console.log(jsObj);
			 			var target = document.getElementById('output');
			 			console.log(jsObj.pid);
			 			target.textContent = "선택된 상품 : " + jsObj.pid;
			 		}
			 };
			 request.open('GET', str, true);
			 request.send(); // GET방식은 send 메서드에 아규먼트가 잇으면 안된다.
		}      

		var getAddress = function(){
			var inputAdd = document.getElementById("address").value;
			return inputAdd;
		}
	 	
	     window.onload = function() {
	         clicks = document.getElementsByTagName("img");

	         for(var i = 0; i < clicks.length; i++){
	        	 clicks[i].onclick = buttonPressed;	        	 
	         }
	     };
 	
		
     </script>
</body>
</html>
```





- 상태정보 유지 기술
  웹 브라우저에서 웹 서버에 정보를 요청할 때 이전 접속시의 결과 물 상태정보 를 일정시간 동안
  유지하는 것을 상태정보 유지라고 한다 . 상태정보 유지 방법은 여러 가지가 있으며
  1. Cookie 를 이용한 방법 (cookie: 웹 서버가 필요에 의해서)
  2. HttpSession 객체를 이용한 방법
  3. URL 문자열 뒤에 추가하는 방법
  4. **\<form\> 태그의 hidden 타입을 사용하는 방법**(게시판 할 때 사용할 것임.)




### 넷스케이프 쿠키

1996 년 12 월 12 일부터 사양
쿠키는 cookies.txt파일 에있는 클라이언트 시스템에 저장된 작은 정보입니다 . 이 부록에서는 Navigator 클라이언트에서의 쿠키 구현에 대해 설명합니다. 공식적인 사양이나 표준이 아닙니다.

쿠키를 조작 할 수 있습니다

명시 적으로 CGI 프로그램과 함께.
프로그래밍 방식으로 문서 개체 의 쿠키 속성을 사용하는 클라이언트 측 JavaScript
클라이언트 쿠키 유지 관리를 사용할 때 LiveWire를 통해 클라이언트 개체를 투명하게 볼 수 있습니다.
LiveWire에서 쿠키를 사용하는 방법에 대한 자세한 내용은 LiveWire 개발자 안내서를 참조하십시오 .

이 부록에서는 HTTP 헤더의 쿠키 정보 형식에 대해 설명하고 CGI 프로그램 및 JavaScript를 사용하여 쿠키를 조작하는 방법에 대해 설명합니다.

통사론
CGI 프로그램은 다음 구문을 사용하여 쿠키 정보를 HTTP 헤더에 추가합니다.

쿠키 설정 : 
   이름 = 값
    [; EXPIRES = dateValue ] 
   [; DOMAIN = domainName ] 
   [; PATH = pathName ] 
   [; SECURE]
매개 변수
name = value 는 세미콜론, 쉼표 및 공백을 제외한 일련의 문자입니다. name 또는 value 에 제한된 문자를 배치하려면 URL 스타일 % XX 인코딩과 같은 인코딩 방법을 사용하십시오.

EXPIRES = dateValue 는 해당 쿠키의 유효 수명을 정의하는 날짜 문자열을 지정합니다. 만료 날짜에 도달하면 쿠키가 더 이상 저장되거나 제공되지 않습니다. dateValue를 지정하지 않으면 사용자 세션이 종료 될 때 쿠키가 만료됩니다.

날짜 문자열의 형식은 다음과 같습니다.

Wdy, DD-Mon-YY HH : MM : SS GMT
여기서 Wdy는 요일입니다 (예 : Mon 또는 Tues). DD는 월의 두 자리 숫자 표현입니다. Mon은 해당 월의 3 자 약어입니다 (예 : Jan 또는 Feb). YY는 연도의 마지막 두 자리입니다. HH : MM : SS는 각각 시간, 분 및 초입니다.

DOMAIN = domainName 은 유효한 쿠키의 도메인 속성을 지정합니다. "유효한 쿠키 결정"을 참조하십시오 . domainName 값을 지정하지 않으면 Navigator는 쿠키 응답을 생성 한 서버의 호스트 이름을 사용합니다.

PATH = pathName 은 유효한 쿠키의 경로 속성을 지정합니다. "유효한 쿠키 결정"을 참조하십시오 . pathName 값을 지정하지 않으면 Navigator는 쿠키 속성을 생성 한 문서의 경로 (또는 CGI 프로그래밍을 위해 HTTP 헤더에 의해 설명 된 문서의 경로)를 사용합니다.

SECURE는 호스트와의 통신 채널이 보안 인 경우에만 쿠키가 전송되도록 지정합니다. HTTPS (HTTP over SSL) 서버 만 현재 안전합니다. SECURE를 지정하지 않으면 쿠키는 모든 채널을 통해 전송 된 것으로 간주됩니다.

**기술**
**서버는 요청에 응답 할 때 쿠키 정보를 HTTP 헤더의 클라이언트에게 보냅니다. 해당 정보에는 유효한 URL 범위에 대한 설명이 포함되어 있습니다. 해당 범위에 해당하는 클라이언트의 향후 HTTP 요청에는 클라이언트에서 서버로 상태 객체의 현재 값 전송이 포함됩니다.**

**많은 다른 응용 프로그램 유형이 쿠키를 활용할 수 있습니다. 예를 들어, 쇼핑 응용 프로그램은 현재 세션 또는 향후 세션에서 사용하기 위해 현재 선택된 항목에 대한 정보를 저장할 수 있으며 다른 응용 프로그램은 클라이언트 컴퓨터에 개별 사용자 기본 설정을 저장할 수 있습니다.**

유효한 쿠키 결정
유효한 쿠키에 대한 쿠키 목록을 검색 할 때 쿠키의 도메인 속성을 URL을 검색하는 호스트의 도메인 이름과 비교합니다.

도메인 속성이 호스트의 정규화 된 도메인 이름의 끝과 일치하면 쿠키 일치 여부를 결정하기 위해 경로 일치가 수행됩니다. 예를 들어 "acme.com"의 도메인 속성은 "shipping.crate.acme.com"뿐만 아니라 호스트 이름 "anvil.acme.com"과 일치합니다.

지정된 도메인 내의 호스트 만 도메인의 쿠키를 설정할 수 있습니다. 또한 도메인 이름은 적어도 두 개 또는 마침표를 사용해야합니다. "COM", "EDU", "NET", "ORG", "GOV", "MIL"및 "INT"범주의 도메인은 두 개의 기간 만 필요합니다. 다른 모든 도메인에는 최소 3 개의 기간이 필요합니다.

PATH = pathName 은 쿠키가 유효한 도메인의 URL을 지정합니다. 쿠키가 이미 도메인 일치를 통과 한 경우 URL의 경로 이름 구성 요소가 경로 속성과 비교되고 일치하는 경우 쿠키가 유효한 것으로 간주되어 URL 요청과 함께 전송됩니다. 예를 들어, PATH = / foo는 "/ foobar"및 "/foo/bar.html"과 일치합니다. "/"경로가 가장 일반적인 경로입니다.

쿠키 HTTP 요청 헤더의 구문
HTTP 서버에서 URL을 요청하면 브라우저는 기존의 모든 쿠키와 URL을 일치시킵니다. 쿠키가 URL 요청과 일치하면 일치하는 모든 쿠키의 이름 / 값 쌍을 포함하는 행이 HTTP 요청에 다음 형식으로 포함됩니다.

쿠키 : NAME1 = OPAQUE_STRING1; NAME2 = OPAQUE_STRING2 ...
**쿠키 저장**
**단일 서버 응답으로 여러 Set-Cookie 헤더를 발급 할 수 있습니다. 기존 쿠키와 동일한 PATH 및 NAME 값을 사용하여 쿠키를 저장하면 기존 쿠키를 덮어 씁니다. PATH 값은 동일하지만 NAME 값은 다른 쿠키를 저장하면 추가 쿠키가 추가됩니다.**

EXPIRES 값은 매핑을 제거 할시기를 나타냅니다. 또한 Navigator는 쿠키 수가 내부 제한을 초과하는 경우 만료 날짜에 도달하기 전에 쿠키를 삭제합니다.

높은 수준의 PATH 값을 가진 쿠키는보다 구체적인 PATH 값을 무시하지 않습니다. 별도의 경로로 여러 개의 일치 항목이있는 경우 아래 예와 같이 일치하는 모든 쿠키가 전송됩니다.

CGI 스크립트는 동일한 PATH 및 NAME 값과 과거의 EXPIRES 값을 가진 쿠키를 반환하여 쿠키를 삭제할 수 있습니다. PATH와 NAME이 정확히 일치해야하므로 쿠키 작성자 이외의 스크립트가 쿠키를 삭제하기가 어렵습니다.

클라이언트 사양
쿠키를 서버로 보낼 때보다 구체적인 경로 매핑을 가진 모든 쿠키는 덜 구체적인 경로 매핑을 가진 쿠키보다 먼저 전송됩니다. 예를 들어, 경로 매핑이 "/"인 쿠키 "name1 = foo"는 경로 매핑이 "/ bar"인 쿠키 "name1 = foo2"다음에 둘 다 보내야합니다.

네비게이터는 다음을 수신하고 저장할 수 있습니다.

총 쿠키 300 개
쿠키 당 4 킬로바이트. 여기서 이름과 OPAQUE_STRING은 4 킬로바이트 제한을 구성합니다.
서버 또는 도메인 당 쿠키 20 개 완전히 지정된 호스트와 도메인은 별도의 엔티티로 간주되며 각각 20 개의 쿠키 제한이 있습니다.
300 쿠키 제한 또는 서버 당 20 쿠키 제한을 초과하면 Navigator는 가장 최근에 사용한 쿠키를 삭제합니다. 4 킬로바이트보다 큰 쿠키가 발견되면 쿠키를 맞추기 위해 잘라 내야하지만 이름이 4 킬로바이트보다 작 으면 그대로 유지해야합니다.

예
다음 예는 일반적인 CGI 프로그램의 트랜잭션 순서를 보여줍니다. JavaScript와 함께 쿠키를 사용하는 예는 "cookie"를 참조하십시오 .

실시 예 1
클라이언트는 문서를 요청하고 응답으로 수신합니다.

쿠키 설정 : CUSTOMER = WILE_E_COYOTE; 경로 = /; 만기일 = 수요일, 
   09-11 월 -99 23:12:40 GMT
클라이언트가이 서버에서 "/"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : CUSTOMER = WILE_E_COYOTE
클라이언트는 문서를 요청하고 응답으로 수신합니다.

쿠키 설정 : PART_NUMBER = ROCKET_LAUNCHER_0001; 경로 = /
클라이언트가이 서버에서 "/"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : CUSTOMER = WILE_E_COYOTE; PART_NUMBER = ROCKET_LAUNCHER_0001
고객은 다음을받습니다.

쿠키 설정 : SHIPPING = FEDEX; 경로 = / foo
클라이언트가이 서버에서 "/"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : CUSTOMER = WILE_E_COYOTE; PART_NUMBER = ROCKET_LAUNCHER_0001
클라이언트가이 서버에서 "/ foo"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : CUSTOMER = WILE_E_COYOTE; PART_NUMBER = ROCKET_LAUNCHER_0001; 
   해운 = 페덱스
실시 예 2
이 예에서는 예 1의 모든 맵핑이 지워 졌다고 가정합니다.

고객은 다음을받습니다.

쿠키 설정 : PART_NUMBER = ROCKET_LAUNCHER_0001; 경로 = /
클라이언트가이 서버에서 "/"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : PART_NUMBER = ROCKET_LAUNCHER_0001
고객은 다음을받습니다.

쿠키 설정 : PART_NUMBER = RIDING_ROCKET_0023; 경로 = / 탄약
클라이언트가이 서버에서 "/ ammo"경로의 URL을 요청하면 다음을 전송합니다.

쿠키 : PART_NUMBER = RIDING_ROCKET_0023; 
   PART_NUMBER = ROCKET_LAUNCHER_0001
"/ ammo"매핑 외에 "/"매핑의 상속으로 인해 "PART_NUMBER"라는 이름 / 값 쌍이 두 개 있습니다.