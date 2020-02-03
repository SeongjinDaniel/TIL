# JSP

JSP, ASP, PHP : 공통점 HTML파일 안에 동적으로 수행한 결과를 포함하고 싶은데 동적 수행이 브라우저를 포함이라면 자바스크립트 서버면 다른 프로그래밍 언어로 해야한다.

JSP -> 실행될때 servlet으로 변경된다.

- Custom Tag : 필요한 기능의 태그를 직접 만들 수 있는 기능
  - Apache Open Group : JSTL(만들어진 태그들의 표준)
    - core library ,xml library, sql library
- Action Tag : JSP가 제공하는 태그로 기능, 구현 방법이 정해져 있는 태그들..

ASP, PHP -> CGI

- JSP ---> 웹 페이지 ---> HTML + JSP태그 + Java

    			규격화된 문서 ---> XML + JSP태그 + Java

  ​			  							  JSON + JSP 태그 + Java

```
<h1>
<form>
<br>
<%=   %>
<%    %>
<jsp:forward	/>    jsp: prefix(접두어) forward: jsp의 액션태그로 지정됨
<jsp:useBean	/>
<c:if />

for(변수선언 : 컬렉션객체){

}
```



