# 상태 유지 기술 (Cookie & Session)

HTTP는 stateless한 프로토콜이다. 서버는 클라이언트의 요청에 대한 응답을 하고 나면 연결을 끊어버린다. 서버에서는 클라이언트가 이전에 무엇을 했는지, 클라이언트에 대한 상태 정보를 알 수 없다.



클라이언트에 대한 상태 정보 유지를 위해 탄생한 기술이 쿠키와 세션이다. 쿠키와 세션을 사용하면 클라이언트에 대한 상태를 저장하고 클라이언트가 누구인지 식별할 수 있다.



### **1) 쿠키 (Cookie)**

- 쿠키는 HTTP 헤더에 추가되어 key-value 쌍의 형태로 전달된다.

- 쿠키는 클라이언트(사용자)의 컴퓨터에 저장된다.

- 따라서 사용자가 쿠키의 내용을 볼 수 있고 맘대로 수정도 할 수 있다.

- 이때문에 보안성이 떨어지므로 중요한 정보는 쿠키에 저장하지 않는다.

- 브라우저별로 쿠키의 수와 용량에 제한이 있습니다. 생각보다 얼마 저장 못한다.

![image](https://user-images.githubusercontent.com/55625864/91639242-34107b00-ea50-11ea-907e-5a84112182c0.png)

### **2) 세션 (Session)**

- 세션은 서버에 저장된다.

- 클라이언트(사용자)는 세션 저장소의 내용을 볼 수 없고 수정도 할 수 없다.

- 클라이언트가 아는 것은 오직 세션키 뿐이다. (세션키는 쿠키를 통해 전달된다.)

- 따라서 보안성이 좋습니다. 하지만 세션은 쿠키와 다르게 서버에 저장되므로 세션 관리 비용이 발생한다.

![image](https://user-images.githubusercontent.com/55625864/91639293-76d25300-ea50-11ea-9bb2-22e16942e256.png)

\* 쿠키와 세션은 목적에 맞게 적절하게 선택해 사용.

\* 예시) 장바구니 기능 - 쿠키, 회원 인증 - 세션



### Cookie 사용법 (with Spring MVC)



#### **1) javax.servlet.http.Cookie (읽기 & 쓰기)**

Servlet API를 쓰는 방식이므로 Spring과 무관하며 Spring을 쓰지 않더라도 사용 가능하다.



**서버에서 쿠키 생성, HttpServletResponse에 쿠키 추가하기**

```java
Cookie cookie = new Cookie("key", "value");
cookie.setMaxAge(3600); // 쿠키 유효기간 설정 (초 단위)
response.addCookie(cookie);
```



**클라이언트가 보낸 쿠키 읽기 (HttpServletRequest에서 읽기)**

```java
Cookie[] cookies = request.getCookies(); // 쿠키가 없으면 null이 반환됨
```



**클라이언트에게 쿠키 삭제 요청**

- 따로 쿠키를 삭제하는 명령은 없고, 유효기간이 0인 같은 이름의 쿠키를 보내면 된다.

- 단, 쿠키는 클라이언트에서 마음대로 조작할 수 있으므로 쿠키가 실제로 삭제되는지 여부는 보장할 수 없다.

```java
Cookie cookie = new Cookie("key", null);
cookie.setMaxAge(0); // 쿠키 유효기간 설정 (초 단위)
response.addCookie(cookie);
```



#### **2) @CookieValue (읽기 전용)**

Spring MVC의 어노테이션을 사용하는 방식입니다. 당연히 Spring MVC를 설치해야 쓸 수 있다.

컨트롤러 메소드의 매개변수에 @CookieValue 어노테이션을 쓰면 클라이언트로부터 전달받은 쿠키 정보가 매핑된다.

단, @CookieValue는 읽기 전용입니다. 클라이언트가 서버에게 전송한 쿠키 정보를 받아오는 것만 할 수 있다.

**서버에서 쿠키를 생성하고 클라이언트에게 전송하기 위해서는 앞서 배운 서블릿 API를 써야한다.**

```java
@RequestMapping(path="/list", method=RequestMethod.GET)
public String list(@CookieValue(value="count", defaultValue="1", required=true) String value) {  // 생략 }
```





### Session 사용법 (with Spring MVC)



**1) javax.servlet.http.HttpSession**

Servlet API를 쓰는 방식이므로 Spring과 무관하며 Spring을 쓰지 않더라도 사용 가능합니다.



**세션 생성 및 얻기**

```java
// 서버에 생성된 세션이 있다면 세션을 반환하고 없다면 새롭게 세션을 생성하여 반환 
// 새롭게 생성된 세션인지는 HttpSession의 isNew() 메소드를 통해 알 수 있음 
HttpSession session = request.getSession(); 

// getSession()에 false를 전달하면, 이미 생성된 세션이 있다면 반환하고 없으면 null을 반환 
HttpSession session2 = request.getSession(false);
```



**세션에 값 저장**

```java
// setAttribute(String name, Object value) 
session.setAttribute("user", "njw1204");
```



**세션의 값 조회**

```java
// getAttribute의 리턴 타입은 Object이므로 형변환 필요 
String value = (String) session.getAttribute("user");
```



**세션의 값 삭제**

```java
// 해당 키에 대응되는 세션 값을 삭제
session.removeAttribute("user"); 

// 세션을 유효하지 않게 설정 (세션에 저장된 모든 값을 삭제) 
session.invalidate();
```



**2) @SessionAttributes**

Spring MVC의 어노테이션을 사용하는 방식입니다.



---



### 쿠키의 종류

쿠키는 크게 퍼스트 파티 (First-Party)와 서드 파티 (Third-Party)의 두종류로 나눌 수 있다.



#### 퍼스트 파티 (First-Party) 쿠키

퍼스트 파티 쿠키는 사용자가 방문한 웹사이트에서 직접 발행하는 쿠키 파일을 말한다. 예를 들어 사용자가 [naver.com](http://naver.com/)으로 접속했을 때 [naver.com](http://naver.com/)에서 로그인 기록에 관한 쿠키를 발행하는 건 퍼스트 파티 쿠키에 해당된다. 네이버에 "로그인 기억" 상태로 로그인하고, 창을 닫았다가 다시 네이버에 접속하면 로그인이 유지된 상태인 것을 알 수 있는데, 쿠키 정보를 이용한 것.

접속한 도메인과 쿠키를 발행한 도메인이 동일 할 경우가 퍼스트 파티 쿠키이다. 서브 도메인이 발행한 쿠키도 퍼스트 쿠키로 간주된다. [test.com](http://test.com/) 사이트에서 [sub1.test.com](http://sub1.test.com/)이 발행한 쿠키는 퍼스트 파티 쿠키로 간주된다.

#### 서드 파티 (Third-Party) 쿠키

서드 파티 쿠키는 사용자가 방문한 웹사이트가 아닌, 다른 웹사이트 (제 3자)에서 발행한 쿠키 파일을 말한다. 보통 광고 서버에서 발행하는 쿠키가 여기에 해당된다. 간단하게 요약하면 접속한 사이트 도메인에서 발행되지 않은 쿠키는 모두 서드 파티 쿠키이다. (서브 도메인은 예외)

예를 들어 [example.com](http://example.com/)이라는 사이트에 사용자가 접속을 했는데, 사이트 페이지 속에 [adserver.com](http://adserver.com/)의 스크립트가 심어져 있는 경우가 있다. 이 때 [adserver.com](http://adserver.com/)은 해당 사용자가 [example.com](http://example.com/)이라는 사이트를 방문했다는 정보를 담은 쿠키를 발행한다.



그리고 사용자가 [test.com](http://test.com/)이라는 사이트에 방문했을 때, 마찬가지로 사이트 페이지 속에 [adserver.com](http://adserver.com/)의 스크립트가 심어져 있는 경우, [adserver.com](http://adserver.com/)은 해당 사용자가 [example.com](http://example.com/)이라는 사이트의 사용 내역에 대한 정보를 쿠키로 부터 빼올 수 있기 때문에, 그 정보를 활용하여 광고를 보여줄 수 있다.

[adserver.com](http://adserver.com/)의 스크립트가 삽입 된 사이트가 많을 수록, [adserver.com](http://adserver.com/)은 각 개인의 온라인상의 행동을 추적하기가 쉬워지고, 그 행동 데이터를 분석하여 활용할 수 있는 영역이 넓어지게 된다.



요즘은 개인정보 보호를 이유로 이 서드 파티 쿠키를 사용하지 않거나 막아버리는 것이 주된 흐름이다. 브라우저 자체에서 트레킹을 막는 설정을 할 수 있다던지, 애드 블록 같은 애드온을 사용한다던지, 백신 프로그램으로 막아버린다던지, 쿠키파일을 지워버린다던지 하며 서드 파티 쿠키는 점점 외면 받고 있다.

일반 사용자 입장에서는 서드파티 쿠키는 지워버리거나 막아버려도 사실 불편한 것이 없다. 서드파티 쿠키는 대부분 온라인 광고에 이용되기 때문에, 오히려 사용자 입장에선 보기 싫은 광고를 막을 수 있어서 편의성이 좋아질 수가 있다.

반면 퍼스트 파티 쿠키는 막아버리면 각 사이트 측에서는 사용자를 식별하기가 매우 어려워지기 때문에, 그만큼 서비스를 제공하기가 힘들어지고, 사용자 자체도 매번 로그인을 해야하는 등 번거로움이 따르기 때문에, 퍼스트 쿠키를 막거나 삭제하는 경우는 드물다.

#### 참고

- [부스트코스\] 쿠키와 세션 / Spring MVC Cookie & Session 사용법](http://blog.naver.com/njw1204/221641159167)

- [[Spring Boot] Session과 Cache의 기본 저장소 !](https://sabarada.tistory.com/22)

- [Spring MVC / HttpSession, @SessionAttribute, @SessionAttributes](https://ecsimsw.tistory.com/entry/Spring-MVC-HttpSession-SessionAttribute-SessionAttributes)

- [쿠키(Cookie)에 대해 알아보자](https://sy34.net/what-is-cookie/)