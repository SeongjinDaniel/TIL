# Spring Day5



Component의 자손 

- @Repository
- @Controller
- @Service

Controller -> Service -> DAO

Autowired를 통해서 객체를 넘겨줌?

##### bean에 추가

```xml
	<context:component-scan base-package="service" /> <!-- 내가 넣어준것임 -->
	<context:component-scan base-package="dao" /> <!-- 내가 넣어준것임 -->
	<beans:bean id="multipartResolver"
		class="org.springframework.web.multipart.commons.CommonsMultipartResolver" />
```

##### web.xml에 추가

```xml
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-databind</artifactId> <!-- 응답을 xml로 하겠어, json으로 하겠어 응답을 도와주는 라이브러리 -->
			<version>2.9.9</version>
		</dependency>
		
		<dependency>
			<groupId>commons-fileupload</groupId>
			<artifactId>commons-fileupload</artifactId>
			<version>1.3.1</version>
		</dependency>       
```



#### 실습 product

```java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.bind.support.SessionStatus;

import vo.ProductVO;

@Controller
@SessionAttributes("cnt")
public class ProductController {
	@ModelAttribute("cnt")
	public ProductVO createModel1() { // session객체에 저장!!
		return new ProductVO();	
	}
	// client가 전송한 쿼리문자와 setter명과 같으면 null인 애들은 호출 x null이 아니면 호출
	// dispatcherServlet이 알아서 setter를 호출해서 사용한다.
	@RequestMapping("product")
	public String proc(@ModelAttribute("cnt")ProductVO vo) {
	    return "productView";
	}
	
	@RequestMapping("productdel")
	public String remove(SessionStatus s) {
		s.setComplete();
		return "delProduct";
	}
}
```

```java
package vo;

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
	<a href="/springedu/product?appleCnt=1"><img
		src="/springedu/resources/images/apple.gif" /></a>
	<a href="/springedu/product?bananaCnt=1"><img
		src="/springedu/resources/images/banana.jpg" /></a>
	<a href="/springedu/product?halabongCnt=1"><img
		src="/springedu/resources/images/halabong.jpg" /></a>
		
	<br>
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
	    	request.open('GET', '/springedu/productdel', true);
	    	request.send(); // GET방식은 send 메서드에 아규먼트가 잇으면 안된다.
		}

		domButton.addEventListener("click", cleanCart);
	</script>
</body>
</html>
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="vo.ProductVO" %>
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
<jsp:useBean id="cnt" class="vo.ProductVO" scope="session"/>
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
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	span{
		color : magenta;
	}
</style>
</head>
<body>
	<h1>요청을 처리하는 동안 에러가 발생했어요(스크립트 태그)</h1>
	<h3>오류의 원인 : <span><%= request.getAttribute("msg") %></span></h3>
	<br/>
	<br/>
	<h1>요청을 처리하는 동안 에러가 발생했어요(EL)</h1>
	<h3>오류의 원인 : <span>${ requestScope.msg }</span></h3>
	<br/>
	<br/>
	<a href="${ header.referer }">입력 화면으로</a>
</body>
</html>
```

#### 실습 LottoController2

**LottoController2  sol1**

```java
package vo;
public class LottoVO {
	private int lottoNum;
	private String result;
	private int applyCnt;

	public LottoVO()  {
		System.out.println("LottoVO Create object");
	}
	public int getApplyCnt() {
		return applyCnt;
	}
	public void setApplyCnt(int applyCnt) {
		if(applyCnt == 0) this.applyCnt = applyCnt;
		else this.applyCnt += applyCnt; 
		System.out.println(this.applyCnt);
	}
	public int getLottoNum() {
		return lottoNum;
	}
	public void setLottoNum(int lottoNum) {
		this.lottoNum = lottoNum;
	}
	public String getResult() {
		return result;
	}
	public void setResult(String result) {
		this.result = result;
	}	
}
```

```java
package service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import dao.LottoDAO;
@Service // 얘는 Service 객체야 라는 뜻 Controller와 같지만 나누는것 뿐이다.
public class LottoService {
	public LottoService()  {
		System.out.println("LottoService 객체생성");
	}
	@Autowired
	LottoDAO lottoDAO = null;
	public boolean getLottoProcess(int lottoNum) {
		boolean result = false;		
		int randomNumber = lottoDAO.getLottoNumber();
		System.out.println("--- 난수: " + randomNumber);
		System.out.println("--- 입력한 수: " + lottoNum);
		if(randomNumber == lottoNum) 
			result = true;
		return result;
	}
}
```

```java
package my.spring.springedu;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;

import service.LottoService;
import vo.LottoVO;
@Controller
@SessionAttributes("counter")
public class LottoController2 {
	@Autowired
	private LottoService lottoService;	
	
	@ModelAttribute("counter")
	public int[] createCounter() {
		System.out.println("create counter");
		return new int[1];
	}
	
	@RequestMapping("/lotto2")
	public String lottoProcess(LottoVO vo, @ModelAttribute("counter") int[] count) {
		count[0] += 1;
		System.out.println("--- 응모 횟수 : " + count[0]);

		if(count[0] > 3) vo.setResult("응모 횟수를 초과했습니다. 브라우저를 재기동해 주세요.");
		else if (lottoService.getLottoProcess(vo.getLottoNum())) {
			vo.setResult("추카추카!!");
			count[0] = 4;
		} else {
			vo.setResult("아쉽네요 .. 다음 기회를!!");
		}
		return "lottoView2";
	}
}

```

**LottoController2  sol2**

```java
package my.spring.springedu;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;

import service.LottoService;
import vo.LottoVO;
@Controller

public class LottoController2 {
	
	@Autowired
	private LottoService lottoService;
	@RequestMapping("/lotto2")
	public String lottoProcess(LottoVO vo, HttpServletRequest request) {	//lottoVO를 리퀘스트에 저장하고 소문자 lottoVO라는 이름으로 보관.
		// 리퀘스트 스코프 영역에 보관.. lottoVO라는 이름으로...
		// 디스패쳐 서블릿이 알아서 만든다..
		// 소문자 
		// LottoService lottoService = new LottoService(); 
		// 오토와이어드로 주입받기로 해놓고 여기서 또 해버리면 널포인트 익셉션 뜸.
		HttpSession session = request.getSession();
		if(session.getAttribute("cnt")==null)
			session.setAttribute("cnt",new int[1]);
		int[] lottoCnt = (int[])session.getAttribute("cnt");
		
		if(lottoCnt[0]>2) {
			vo.setResult("더 이상 응모할 수 없습니다. 브라우저를 재 기동 하세요");
			return "lottoView2";
		}else {
		if (lottoService.getLottoProcess(vo.getLottoNum())) {
			vo.setResult("추카추카!!");
			lottoCnt[0]+=1;
		} else {
			vo.setResult("아쉽네요 .. 다음 기회를!!");
			lottoCnt[0]+=1;
		}
		System.out.println(lottoCnt[0]);
		return "lottoView2";
	}
	}
}
//lotto 서비스 객체가 생성이 되어야 된다는 것을 뜻함.
// 로또 서비스를 어디서 찾냐?
// 컴포넌트 스캔을 통해 dao나 서비스 패키지도 스캔함.
// 서비스 패키지에 로또서비스 클래스가 있음.
// 로또 vo안에 컨트롤러와 
// 로또 컨트롤러 1이 로또컨트롤 메서드가 호출될 때 그안에 로또 넘이 들어와 있을 것,, 그것을 서비스 객체에 전달함.
```

**LottoController2  sol3**

```java
package my.spring.springedu;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import service.LottoService;
import vo.LottoVO;
@Controller
public class LottoController2 {
	@Autowired
	//Autowired 라고 되어있는 부분은 LottoController가 호출되면 객체 생성된다.
	//즉, LottoController 객체 생성하려면 먼저 LottoService가 호출되어야하므로
	//LottoService 객체에 의존적이다.
	private LottoService lottoService;	
	@RequestMapping("/lotto2")
	public String lottoProcess(LottoVO vo,HttpSession s) {
		
		if(s.getAttribute("lottocnt")==null) {
			s.setAttribute("lottocnt", new int[1]);
		}
		int lottocnt[] = (int [])s.getAttribute("lottocnt");
		lottocnt[0]++;
		System.out.println(lottocnt[0]);
		if (lottoService.getLottoProcess(vo.getLottoNum())) {
			lottocnt[0]=3;
			vo.setResult("추카추카!!");
		} else {
			vo.setResult("아쉽네요 .. 다음 기회를!!");
		}
		if(lottocnt[0]>=4) {
			//System.out.println("HERE");
			vo.setResult("더 이상 응모할 수 없습니다. 브라우저를 재기동해주세요.");
		}
		s.setAttribute("lottocnt", lottocnt);
		return "lottoView2";
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="vo.LottoVO"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>로또 결과</h1>
<hr>
<h2>${ lottoVO.result }</h2>
<%
	vo.LottoVO vo = (vo.LottoVO)request.getAttribute("lottoVO");
%>
<h2><%= vo.getResult() %></h2>
<hr>
<a href="/springedu/resources/lottoForm2.html">재시도.....</a>
</body>
</html>
```





**요청방식**

http://localhost:8000/springedu/body/text/unico

http://localhost:8000/springedu/body/htmltext/unico

http://localhost:8000/springedu/body/json/unico

http://localhost:8000/springedu/body/json1/unico

http://localhost:8000/springedu/body/xml1/unico

http://localhost:8000/springedu/body/json2/unico

```java
package my.spring.springedu;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import vo.MyGroupModel;
import vo.MyMainModel;
import vo.MyModel;
import vo.XmlVO;

@Controller
public class ResponseBodyController {
	// id는 동적으로 설정! 
	@RequestMapping(value = "/body/text/{id}", produces = "text/plain; charset=utf-8")
	@ResponseBody // 최근 추가된 annotation view를 안거치고 controller가 직접 응답 body를 구성하겠다.(원래는 view가 직접 응답한다.)
	public String getByIdInTEXT(@PathVariable String id) { // 이거 주지 않으면 쿼리 문자열에서 id를 추출한다.
		return "<h1>It returns the string directly from the controller : " + id + "</h1>";
	}

	@RequestMapping(value = "/body/htmltext/{id}", produces = "text/html; charset=utf-8")
	@ResponseBody
	public String getByIdInHTMLTEXT(@PathVariable String id) {
		return "<h1>It returns the HTML directly from the controller : " + id + "</h1>";
	}
	
	@RequestMapping(value = "/body/json/{id}", produces = "application/json; charset=utf-8")
	@ResponseBody
	public String getByIdInJSON(@PathVariable String id) {
		String s = "{ \"name\" : \"ROSE\", \"num\":5, \"id\" : \""+id+"\"}";
		return s;
	}
	
	@RequestMapping(value = "/body/json1/{id}", produces = "application/json; charset=utf-8")
	@ResponseBody
	public MyModel getByIdInJSON1(@PathVariable String id) {
		MyModel my = new MyModel();
		my.setFlowerName("ROSE");
		my.setNum(5);
		my.setId(id);		
		return my;
	}	
	
	@RequestMapping(value = "/body/json2/{id}", produces = "application/json; charset=utf-8")
	@ResponseBody
	public List<MyModel> getByIdInJSON2(@PathVariable String id) {
		List<MyModel> list = new ArrayList<MyModel>();
		MyModel my = new MyModel();
		my.setFlowerName("ROSE");
		my.setNum(5);
		my.setId(id);
		list.add(my);
		my = new MyModel();
		my.setFlowerName("LILY");
		my.setNum(5);
		my.setId(id);
		list.add(my);
		return list;
	}

	
	@RequestMapping(value = "/body/json3/{id}", produces = "application/json; charset=utf-8")
	@ResponseBody
	public List<MyMainModel> getByIdInJSON3(@PathVariable String id) {
		ArrayList<MyMainModel> list = new ArrayList<>();
		ArrayList<MyGroupModel> list2 = new ArrayList<>();
		ArrayList<MyGroupModel> list2_1 = new ArrayList<>();
		ArrayList<MyModel> list3 = new ArrayList<>();
		ArrayList<MyModel> list3_1 = new ArrayList<>();
		MyModel my1 = new MyModel();
		my1.setFlowerName("AAA");
		my1.setNum(5);
		my1.setId(id);
		MyModel my2 = new MyModel();
		my2.setFlowerName("BBB");
		my2.setNum(5);
		my2.setId(id);
		MyModel my3 = new MyModel();
		my3.setFlowerName("BBB");
		my3.setNum(5);
		my3.setId(id);
		MyModel my4 = new MyModel();
		my4.setFlowerName("CCC");
		my4.setNum(5);
		my4.setId(id);
		MyModel my5 = new MyModel();
		my5.setFlowerName("DDD");
		my5.setNum(5);
		my5.setId(id);
		list3.add(my1);
		list3.add(my2);
		list3_1.add(my3);
		list3_1.add(my4);
		list3_1.add(my5);
		MyGroupModel mgm1 = new MyGroupModel();
		mgm1.setCategory("요가");
		mgm1.setMyModellist(list3);
		MyGroupModel mgm2 = new MyGroupModel();
		mgm2.setCategory("수영");
		mgm2.setMyModellist(list3_1);
		list2.add(mgm1);
		list2_1.add(mgm2);
		MyMainModel mmm1 = new MyMainModel();
		mmm1.setYear("2019");
		mmm1.setGrouplist(list2);
		MyMainModel mmm2 = new MyMainModel();
		mmm2.setYear("2018");
		mmm2.setGrouplist(list2_1);
		list.add(mmm1);
		list.add(mmm2);
		System.out.println(list);
		return list;
	}
	
	@RequestMapping(value = "/body/json4/{id}", produces = "application/json; charset=utf-8")
	@ResponseBody
	public List<HashMap<String, String>> getByIdInJSON4(@PathVariable String id) {
		List<HashMap<String, String>> list = new ArrayList<>();
		HashMap<String, String> map1 = new HashMap<>();
		map1.put("aa", "10");
		map1.put("bb", "20");
		HashMap<String, String> map2 = new HashMap<>();
		map2.put("cc", "30");
		map2.put("dd", "40");
		list.add(map1);
		list.add(map2);
		return list;
	}

	@RequestMapping(value = "/body/xml1/{id}", produces = "application/xml; charset=utf-8")
	@ResponseBody
	public MyModel getByIdInXML1(@PathVariable String id) {
		MyModel my = new MyModel();
		my.setFlowerName("ROSE");
		my.setNum(5);
		my.setId(id);
		return my;
	}

	
	@RequestMapping(value = "/body/xml2/{id}", produces = "application/xml; charset=utf-8")
	@ResponseBody
	public XmlVO getByIdInXML4(@PathVariable String id) {
		XmlVO vo = new XmlVO();
		ArrayList<MyModel> list = new ArrayList<MyModel>();
		MyModel my = new MyModel();
		my.setFlowerName("ROSE");
		my.setNum(5);
		my.setId(id);
		list.add(my);
		my = new MyModel();
		my.setFlowerName("LILY");
		my.setNum(5);
		my.setId(id);
		list.add(my);
		vo.setList(list);
		return vo;
	}	
	@RequestMapping(value = "/getJSON1", 
			      produces = "application/json; charset=utf-8")
	@ResponseBody
	public String test1(String id) {		
		String s = "{ \"result\" : \"ㅋㅋ1"+id+"\"}";
		return s;
	}
	@RequestMapping(value = "/getJSON2", 
		      produces = "application/json; charset=utf-8")
	@ResponseBody
	public HashMap<String, String> test2(String id) {		
		HashMap<String, String> map = new HashMap<String, String>();
		map.put("result", "ㅋㅋ2"+id);
		return map;
	}
}
```



