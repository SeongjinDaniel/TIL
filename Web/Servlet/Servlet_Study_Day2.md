# # Day2 Servlet

name = duke&passwd=1234&age=&gender=female

​			request.getParameter("name") --> "duke"

​			request.getParameter("passwd") --> "1234"

​			request.getParameter("age") --> ""

​			request.getParameter("hobby") --> "null"

### HTTP 상태 500 – 내부 서버 오류

null을 가지고 숫자로 변환하려고 하니까  NumberFormatException 에러가 난다.

```
예외
java.lang.NumberFormatException: null
	java.lang.Integer.parseInt(Unknown Source)
	java.lang.Integer.parseInt(Unknown Source)
	core.QueryTestServlet2.doGet(QueryTestServlet2.java:16)  ---> 중요
	javax.servlet.http.HttpServlet.service(HttpServlet.java:634)
	javax.servlet.http.HttpServlet.service(HttpServlet.java:741)
	org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
```

response.setContentType("text/**plain**; charset=UTF-8");  -> plain이라고 하면 무조건 text로만 인식

#### 응답코드

| **200** | **OK**                    | **오류 없이 전송 성공.** |
| ------- | ------------------------- | ------------------------ |
| **500** | **Internal Server Error** | **서버 내부 오류**       |

| 404     | Not Found              | 문서를 찾을 수 없음. 서버가 요청한 파일이나 스크립트를 찾지 못함. |
| ------- | ---------------------- | ------------------------------------------------------------ |
| **405** | **Method not allowed** | **메서드 허용 안됨. 요청 내용에 명시된 메서드를 수행하기 위해 해당 자원의 이용이 허용되지 않음.[[20\]](https://ko.wikipedia.org/wiki/HTTP#cite_note-20)** |

405 error : 요청하는 방식하고 servlet이 지원하는 방식과 일치 하지 않을때.

500 error : 요청을 다 받았 servlet 에서 error가 있다.



get방식을 보완하기 위해서 post(쿼리문자의 길이 제한이 없다, 요청 방식이 없다.)를 만들었다.

모든 웹서버는 응답 상태 코드가 와야한다.

#### 실습 

```

```






## 웹 의 처리 구조

웹 통신에 사용되는 표준 통신 프로토콜은 HTTP( HyperText Transfer Protocol) 이다.



Java : Java SE(standrd Edition), Java EE(Enterprise Edition), Java ME(Micro Edition)

```
톰캣 : Web Server + Application Server : WAS

       ------------   --------------
	     코요테		  카탈리나
					   서블릿엔진
					   서블릿컨테이너
```



