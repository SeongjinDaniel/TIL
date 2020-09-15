# HttpSession

**JAVA HttpSession (javax.Servlet.Http)**

 



JAVA HttpSession은 복수 Page에 걸쳐 Request에 의해 Web 사이트에 접속한 User를 식별해, 그 User에 대한 정보를 제어할 수 있는 법을 제공한다.

Servlet Container는 HttpSession Interface를 사용하여 Http Client와 Http Server간에 Session을 작성한다. 

Session은 User로부터의 복수 접속, 즉 Page Request에 걸쳐 일정기간 지속한다. 

통상 1개의 Session은 사이트에 접속하는 1명의 User에게 대응하며, Server는 Cookie의 사용이나 URL의 갱신 등 다양한 방법으로 Session을 유지할 수 있다.

 

 

HttpSession Interface에 의해 Servlet은 다음과 같은 일을 수행한다.

\- Session 식별자, 생성 시간, 최종 액세스 시간 등의 Session에 대한 정보를 참조하고 제어한다.

\- User 정보가 여러 차례 접속에 걸쳐서 유지되도록 Object를 Session에 bind한다.

 

 

Application이 Session 내에 Object를 포함하거나 Session으로부터 Object를 삭제하거나 할 때에 Session은 Object가 HttpSessionBindingListener를 구현하고 있는지의 여부를 체크한다. 

HttpSessionBindingListener를 구현하고 있는 경우에는 Session에 Object가 bind 된 것이다.

Session 정보의 유효 범위는 현재의 Web Application (ServletContext)이므로, 1개의 문맥 내에 포함된 정보를 다른 문맥내에서 직접 볼 수 없다.

 

 

**HttpSession을 이용한 Session 관리 장점**

\- 관리할 수 있는 상태값(Client Data)의 종류나 크기, 개수의 제한이 없다.

\- Server에 저장되므로 Cookie에 비해 보안상 유리하다.

 

**HttpSession을 이용한 Session 관리 단점**

\- Server에 부담을 준다.

 

 

**HttpSession 객체 생성방법**

\- HttpServletRequest객체.getSession() : // 기존 Session이 있으면 기존 Session 객체를, 없으면 새로 생성하여 반환한다.

\- HttpServletRequest객체.getSession(false) // 기존 Session이 있으면 기존 Session 객체를, 없으면 null을 반환한다.

 

**HttpSession METHOD**

\- setAttribute(String, Object)

\- getAttribute(): Object

\- getCreationTime(): long

\- getLastAccessedTime(): long

\- setMaxInactiveInterval(int second) // Client가 이 시간동안 request가 없으면 Session 만료.

\- getMaxInactiveInterval(): int

\- invalidate() : // Session 종료. Session에 속한 속성들도 같이 제거.

\- getId() : String // jSessionId값 return

 

 

Session 종료

Session이 종료되는 경우는 3가지 (개발자는 1, 2번의 경우만 조정할 수 있다.)

1. 시간이 다 되어서(타임아웃).

2. 개발자가 Session 객체의 invalidate() 를 호출.

3. 애플리케이션이 다운되는 경우.

 

 

Session의 timeout은 DD(Deployment Descriptor : web.xml)에서 설정하며, 단위는 분이다.

```
<wep-app....>

 <Servlet>

  ...

 </Servlet>

 <Session-config>

  <Session-timeout>15</Session-timeout> 

 </Session-config>

</wep-app>
```



위 설정은 모든 Session Object 에 setMaxInactiveInterval()를 호출 하는 것과 같다.

#### 참고

- [JAVA HttpSession (javax.Servlet.Http)](https://m.blog.naver.com/PostView.nhn?blogId=rex4314&logNo=206376623&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [세션(Session) 이용하는 방법](https://enai.tistory.com/29)
- 