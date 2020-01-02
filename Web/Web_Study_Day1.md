# Day1 Web

[Web 프로그래밍 기술 학습]

- 프로그래밍이 실행하는 위치

  - Web 서버 프로그래밍 - Web 클라이언트(브라우저)가 요청했을 때 서버에서 실행
    - servlet, Spring, Mybstis
  - Web 클라이언트 프로그래밍 - Web 클라이언트가 요청했을 때 클라이언트에서 실행
    - HTML5, CSS3, JavaScript, jQuery, Ajax

- 테스트 환경

  Web 클라이언트 역할의 프로그램 : 브라우저(크롬)

  Web 서버 역할의 프로그램 : Servlet, JSP를 처리할 수 있는 서버(WAS : Web Application Server)

  ​                                             															-----> Tomcat 9.0(https://tomcat.apache.org/)

  ​																				Tomcat 설치시 오라클과 포트 번호가 겹치면 안되니까

  ​																				HTTP/1.1Connector Port 를 8000으로 변경

  - Eclipse - Web Project - edu

    -> Eclipse에서 Tomcat 9.0을 관리하게 할것이다.

    -> Eclipse -> file -> new -> other ->Server -> server -> Apache -> Apache Tomcat v9.0

    Tomcat installation directory: -> 브라우저 선택

    C:\Program Files\Apache Software Foundation\Tomcat 9.0

    [Web Project 생성]

    file -> new -> other -> Web -> Dynmic Web Project -> project name : edu -> next -> next

    -> check box check(Generate web ~~~ )

    edu 에서 -> WebContent

    http://localhost:8000/edu/imsi.html -> 확인가능!!