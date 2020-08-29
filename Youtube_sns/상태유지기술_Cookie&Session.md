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





#### 참고

- [부스트코스\] 쿠키와 세션 / Spring MVC Cookie & Session 사용법](http://blog.naver.com/njw1204/221641159167)

- [[Spring Boot] Session과 Cache의 기본 저장소 !](https://sabarada.tistory.com/22)