# 웹서버 vs WAS



**1. 웹 서버와** **WAS( Web Application Server )**

- **웹 서버**는 **정적**인 컨텐츠( html, css, js )를 제공하는 서버입니다.

- - Apache, Nginx 
  - WEB Server로 가장 많이 쓰는 프로그램으로는 Apache재단의 Apache가 있고, Microsoft사의 IIS, nginx등이 있습니다.

- **WAS**는 DB 조회나, 어떤 로직을 처리해야 하는 **동적**인 컨텐츠를 제공하는 서버입니다.
- JSP, ASP, PHP 등 사용자의 입력을 받아 서버에서 무언가를 처리하고 그 결과를 보여주는 동적인 데이터를 처리하는 웹서버 입니다.
  
- - Tomcat, Jeus
  - WAS로 가장 많이 쓰는 프로그램으로는 BEA사의 Web Logic, IBM사의 Web Sphere, T-max사의 Jeus, Tomcat, Redhot사의 JBoss 등이 있습니다.

WAS는 정적,동적 처리 둘다 가능하지만 정적처리를 WAS가 하게되면 부하가 많이 걸려서 좋지 않음



#### 참고

- [WEB 서버와 WAS 서버의 차이](https://sungks.tistory.com/195)

- [apache와 apache tomcat의 차이점](https://ithub.tistory.com/101)