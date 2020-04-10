

이 글은 Google의 oAtuh2를 이용하는 방법에 대한 글입니다.



최근 로그인 인증 기능에 대해서 대형 포털 혹은 소셜 등에서 많이 제공하고 있습니다. 간단하게 우리가 뉴스 기사 등에 댓글을 달아도 굳이 그 사이트에 로그인이 아닌 Naver나 Daum, 페이스북, 구글 로그인 만으로 댓글을 달 수 있습니다.

그 기능에 oAuth2를 통한 로그인 기능입니다.



저는 구글의 oAuth2를 하는 방법에 대해 소개를 하지만 oAuth2는 거의 표준이기 때문에 다른 포털에서도 90% 비슷하게 사용할 수 있습니다.



oAuth2를 이용하기 위해서는 먼저 Google console에 접속하셔서 어플리케이션 등록을 해야합니다.

google console - [https://console.developers.google.com](https://console.developers.google.com/)

출처: https://nowonbun.tistory.com/479 [명월 일지]

![image-20200222162852559](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222162852559.png)

![image-20200222162907435](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222162907435.png)

접속을 하시면 위 이미지처럼 API 및 서비스가 나오는 데 사용자 인증 정보에서 사용자 인증 정보 만들기를 클릭합니다.

여기서 여러가지 기능이 있습니다만, 일단 로그인 기능만 사용할 생각이기 때문에 OAuth 클라이언트 ID를 클릭합니다.

![image-20200222162940943](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222162940943.png)

![image-20200222163032931](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222163032931.png)

여기서 저는 웹 어플리케이션에서 로그인 정보를 사용할 생각이기 때문에 웹 어플리케이션을 선택하고 제한사항으로는 일단 로컬에서 테스트하기 때문에 「http://localhost」 혹은 「http://localhost:8000」를 넣습니다.

먼저 apache에서 html로 테스트를 한 후에 자바 서블릿으로도 테스트를 할 생각이기 때문에 기본 포트인 8000도 등록했습니다. C#이나 php의 경우는 로컬에서 기동되는 포트 번호를 넣으면 되겠네요.



그리고 승인된 리디렉션 URI는 로그인이 완료되면 token을 보내는 URI입니다.

기본적으로 OAuth의 흐름은 아래와 같습니다.

![image-20200222163211100](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222163211100.png)

출처 - https://developers.google.com/identity/protocols/OAuth2

생성을 하면 클라이언트 ID와 보안 키가 발급됩니다.

![image-20200222163240678](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222163240678.png)

이제 apache에서 html과 javascript로 인증을 해보겠습니다. (참고로 file을 브라우져에서 띄울 경우는 리디렉션 주소 설정이 어렵기 때문에 apache로 테스트하는게 좋을 듯싶습니다.)

인증하는 방법에는 redirect로 하는 방법과 google 라이브러리를 이용하는 방법이 있습니다.

먼저 redirect로 하는 방법을 알아보겠습니다.

#### index.html

```html
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
</head>
<body>
<input type="button" id="loginBtn" value="login">
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script>
$("#loginBtn").click(function(){
location.href="https://accounts.google.com/o/oauth2/auth?client_id="+
"클라이언트 ID를 여기에 넣습니다."+
"&redirect_uri="+
"http://localhost/redirect.html" +
"&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email&approval_prompt=force&access_type=offline";
});
</script>
</body>
</html>
```

발급받은 인증 코드로 token으로 변환한다.

#### redirect.html

```html
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
</head>
<body>
<form method="POST" action="https://accounts.google.com/o/oauth2/token">
<!-- 로그인으로 얻은 code를 여기에 넣는다. -->
<input type="text" name="code"> <br />
<!-- 클라이언트 ID를 넣는다. -->
<input type="text" name="client_id" value="클라이언트 ID"> <br />
<!-- 클라이언트 보안 키를 넣는다. -->
<input type="text" name="client_secret" value="클라이언트 보안 key"> <br />
<!-- 등록한 리디렉트 주소를 여기에 넣는다. -->
<input type="text" name="redirect_uri" value="http://localhost/redirect.html"> <br />
<!-- 고정값 -->
<input type="text" name="grant_type" value="authorization_code"> <br />
<input type="submit">
</form>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script>
// 주소 창에 있는 parameter를 취득한다.
function getParameter(name){
var list = location.search.substring(1).split('&');
for(var i=0;i<list.length;i++){
var data = list[i].split('=');
if(data.length === 2){
if(data[0] === name){
return data[1];
}
}
}
return null;
}
// 파라미터 code를 취득하고 URL 디코딩해서 input code에 넣는다.
$("input[name=code]").val(decodeURIComponent(getParameter('code')));
</script>
</body>
</html>
```

#### userinfo.html

```html
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
</head>
<body>
<form method="GET" action="https://www.googleapis.com/oauth2/v1/userinfo">
<!-- 받은 인증 코드로 id 정보를 얻는다.. -->
<input type="text" name="access_token">
<input type="submit">
</form>
</body>
</html>
```

여기까지 html를 작성하고 apache로 실행해 보겠습니다.

![image-20200222190113865](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190113865.png)

여기서 login버튼을 누른다.

![image-20200222190213524](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190213524.png)

계정을 선택해서 로그인을 합니다.

![image-20200222190240705](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190240705.png)

그럼 인증 코드가 발급되서 가장 위 Textbox에 입력된다. 여기서 다시 제출 버튼을 누른다.

![image-20200222190331988](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190331988.png)

그럼 토큰이 발급된 것을 확인할 수 있습니다. 여기서 가장 위 access_token을 가지고 id정보를 가져옵니다.

userinfo.html로 가서 access_token을 넣고 제출 버튼을 누릅니다.

![image-20200222190348190](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190348190.png)

그럼 id와 email주소 사진정보를 얻을 수 있습니다.

![image-20200222190420370](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222190420370.png)

이번에는 구글 라이브러리를 이용해서 얻는 방법을 소개하겠습니다.

```html
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
<meta name="google-signin-client_id" content="클라이언트 ID">
</head>
<body>
<input type="button" id="loginBtn" value="login">
<div id="googleSigninButton" style="display:none;"></div>
<br />
<br />
<br />
<span id="result"></span>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script type="text/javascript" src="https://apis.google.com/js/platform.js?onload=onLoad" async defer></script>
<script>
$("#loginBtn").on("click", function(){
$(".abcRioButtonContents").trigger("click");
});
function onSignIn(googleUser) {
// 프로필 가져오기
var profile = googleUser.getBasicProfile();
// 로그인 정보 출력하기
$("span#result").html("id : "+profile.getId()+"<br />"+"email : "+profile.getEmail()+"<br />"+"name : "+profile.getName());
}
function onLoad() {
gapi.load('auth2,signin2', function() {
var auth2 = gapi.auth2.init();
auth2.then(function() {
// 로그인 객체 가져오기
var isSignedIn = auth2.isSignedIn.get();
// 접속되어 있는 유저
var currentUser = auth2.currentUser.get();
gapi.signin2.render('googleSigninButton', {
'onsuccess' : 'onSignIn', // 로그인이 되면 onSignIn 함수를 호출한다.
'longtitle' : true,
'theme' : 'dark',
'width' : '0'
});
});
});
}
</script>
</body>
</html>
```

![image-20200222193424520](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222193424520.png)

라이브러리를 이용한 방법은 redirect 방법과는 다르게 브라우져에서 Google이 로그인되어 있는 쿠키가 있을 경우 자동으로 로그인이 되어 있어서 정보를 가져올 수 있습니다.

[![img](https://t1.daumcdn.net/tistory_admin/assets/blog/4a71a8a93ca305dfb888d8c19c29f19fef98b7cd/blogs/image/extension/zip.gif?_version_=4a71a8a93ca305dfb888d8c19c29f19fef98b7cd) Library OAuth.zip](https://nowonbun.tistory.com/attachment/cfile10.uf@99558B385D07BD89368BB4.zip)

여기까지 html과 자바 스크립트로 구글 OAuth를 이용하는 방법을 알아보았습니다. 그럼 실제 Java servlet에서는 HttpConnection을 이용해서 사용하는데 구현해 보겠습니다.

구현은 redirect 형식의 html과 비슷한데 redirect 부분과 유저 정보를 취득하는 부분을 좀 더 안전하게 서블릿에서 HttpConnection를 이용하는 것 뿐입니다.

#### index.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF8" pageEncoding="UTF8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF8">
<title>Insert title here</title>
</head>
<body>
<input type="button" id="loginBtn" value="login">
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script>
$("#loginBtn").click(function(){
location.href="https://accounts.google.com/o/oauth2/auth?client_id="+
"220458850151-3varsnqai8qutmf3k4c77mmnq4bk9dls.apps.googleusercontent.com"+
"&redirect_uri="+
"http://localhost:8080/WebExample/redirect" +
"&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email&approval_prompt=force&access_type=offline";
});
</script>
</body>
</html>
```

#### Token.java

```java
class Token {
private String access_token;
private int expires_in;
private String refresh_token;
private String scope;
private String token_type;
private String id_token;
public String getAccess_token() {
return access_token;
}
public void setAccess_token(String access_token) {
this.access_token = access_token;
}
public int getExpires_in() {
return expires_in;
}
public void setExpires_in(int expires_in) {
this.expires_in = expires_in;
}
public String getRefresh_token() {
return refresh_token;
}
public void setRefresh_token(String refresh_token) {
this.refresh_token = refresh_token;
}
public String getScope() {
return scope;
}
public void setScope(String scope) {
this.scope = scope;
}
public String getToken_type() {
return token_type;
}
public void setToken_type(String token_type) {
this.token_type = token_type;
}
public String getId_token() {
return id_token;
}
public void setId_token(String id_token) {
this.id_token = id_token;
}
}
```

#### redirect.java

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.google.gson.Gson;
import javax.net.ssl.HttpsURLConnection;
@WebServlet("/redirect")
public class Redirect extends HttpServlet {
private static final long serialVersionUID = 1L;
public Redirect() {
super();
}
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
String code = request.getParameter("code");
String query = "code=" + code;
query += "&client_id=" + "클라이언트 ID";
query += "&client_secret=" + "클라이언트 보안 키";
query += "&redirect_uri=" + "등록한 리디렉트 주소";
query += "&grant_type=authorization_code";
String tokenJson = getHttpConnection("https://accounts.google.com/o/oauth2/token", query);
System.out.println(tokenJson.toString());
Gson gson = new Gson();
Token token = gson.fromJson(tokenJson, Token.class);
String ret = getHttpConnection("https://www.googleapis.com/oauth2/v1/userinfo?access_token=" + token.getAccess_token());
System.out.println(ret);
}
private String getHttpConnection(String uri) throws ServletException, IOException {
URL url = new URL(uri);
HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
conn.setRequestMethod("GET");
int responseCode = conn.getResponseCode();
System.out.println(responseCode);
String line;
StringBuffer buffer = new StringBuffer();
try (InputStream stream = conn.getInputStream()) {
try (BufferedReader rd = new BufferedReader(new InputStreamReader(stream))) {
while ((line = rd.readLine()) != null) {
buffer.append(line);
buffer.append('\r');
}
}
} catch (Throwable e) {
e.printStackTrace();
}
return buffer.toString();
}
private String getHttpConnection(String uri, String param) throws ServletException, IOException {
URL url = new URL(uri);
HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
conn.setRequestMethod("POST");
conn.setDoOutput(true);
try (OutputStream stream = conn.getOutputStream()) {
try (BufferedWriter wd = new BufferedWriter(new OutputStreamWriter(stream))) {
wd.write(param);
}
}
int responseCode = conn.getResponseCode();
System.out.println(responseCode);
String line;
StringBuffer buffer = new StringBuffer();
try (InputStream stream = conn.getInputStream()) {
try (BufferedReader rd = new BufferedReader(new InputStreamReader(stream))) {
while ((line = rd.readLine()) != null) {
buffer.append(line);
buffer.append('\r');
}
}
} catch (Throwable e) {
e.printStackTrace();
}
return buffer.toString();
}
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
doGet(request, response);
}
}

```

![image-20200222193836684](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200222193836684.png)

다른 포털 사이트의 OAuth 형식도 구글의 형식과 많이 비슷합니다. 다만 라이브러리를 지원하는 데가 있고 지원하지 않는 곳이 있는데 Redirect 방식의 95%비슷하니 참고해서 사용하면 되겠습니다.

[![img](https://t1.daumcdn.net/tistory_admin/assets/blog/4a71a8a93ca305dfb888d8c19c29f19fef98b7cd/blogs/image/extension/zip.gif?_version_=4a71a8a93ca305dfb888d8c19c29f19fef98b7cd) WebExample.zip](https://nowonbun.tistory.com/attachment/cfile3.uf@993EFF485D07BD8907B3C6.zip)

여기까지 Google OAuth 사용법에 대한 글이었습니다.

궁금한 점이나 잘못된 점이 있으면 댓글 부탁드립니다.

출처: https://nowonbun.tistory.com/479 [명월 일지]

-----------

1. 문제 상황

   다음 코드에서 오류 발생

   ```java
   import com.google.gson.Gson;
   ... (생략)
   new Gson();
   ```

2. 조치

   pom.xml의 dependencies 내부에 아래 내용 추가

   ```xml
   <dependency>
       <groupId>com.google.code.gson</groupId>
       <artifactId>gson</artifactId>
   </dependency>
   ```

   ------------>  **jre 1.8 이상으로 변경!!**



---------

https://minwan1.github.io/2018/02/24/2018-02-24-OAuth/

OAuth 개념정리 사이트

---------------------------------

### 생활코딩

https://developers.google.com/identity/sign-in/web/sign-in

#### Load the Google Platform Library

에서 

```html
<script src="https://apis.google.com/js/platform.js" async defer></script>
```

복붙

#### Specify your app's client ID

```html
<meta name="google-signin-client_id" content="YOUR_CLIENT_ID.apps.googleusercontent.com">
```

복붙

#### Add a Google Sign-In button

에서 

```html
<div class="g-signin2" data-onsuccess="onSignIn"></div>
```

복붙

#### Get profile information

에서

```javascript
function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}
```

**총 내용 index.html**

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Index</title>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="905573480053-nj2mct13m72s933mfpvqb65du0hlu51u.apps.googleusercontent.com">
<script>
	function onSignIn(googleUser) {
	  var profile = googleUser.getBasicProfile();
	  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	  console.log('Name: ' + profile.getName());
	  console.log('Image URL: ' + profile.getImageUrl());
	  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
	}

</script>
</head>
<body>
	<div class="g-signin2" data-onsuccess="onSignIn"></div><!-- 로그인이 끝났을 때 onSignIn 함수를 호출할 것이다. -->
	
</body>
</html>
```

여기까지 첫번째 방법!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

----------

Google에 Google Sign-In JavaScript client reference를 검색한다.

-> 없어서 Building a custom Google Sign-In button 검색해서 https://developers.google.com/identity/sign-in/web/build-button이곳으로 들어간다.

#### Auth Setup

에서 

```html
<script src="https://apis.google.com/js/platform.js?onload=init" async defer></script>
```

복붙(body 맨 밑에다가)

```javascript
<script>
	function init(){
		console.log('init');
		gapi.load('auth2', function() {
		/* Ready. Make a call to gapi.auth2.init or some other API */
			console.log('auth2');
			gapi.auth2.init({
				
			})
		});
	}
</script>
```

-----------

#### gapi.auth2.init(params)

에서

```javascript
gapi.auth2.init({
				{
					  client_id: '905573480053-nj2mct13m72s933mfpvqb65du0hlu51u.apps.googleusercontent.com'
				}
})
```

추가

그럼 meta 태그 지움

so, 

```javascript
<script>
	function init(){
		console.log('init');
		gapi.load('auth2', function() {
		/* Ready. Make a call to gapi.auth2.init or some other API */
			console.log('auth2');
			var gauth = gapi.auth2.init({
				{
					  client_id: '905573480053-nj2mct13m72s933mfpvqb65du0hlu51u.apps.googleusercontent.com'
				}
			})
		});
	}
</script>
```

gapi.auth2.init이것이 리턴 값이 있으니까 변수에 저장

### GoogleAuth.then(onInit, onError) 

첫번째 인자는 성공을 의미하고 두번째 인자는 에러를 의미한다.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Index</title>

<script>
	function init(){
		console.log('init');
		gapi.load('auth2', function() {
		/* Ready. Make a call to gapi.auth2.init or some other API */
			console.log('auth2');
			var gauth = gapi.auth2.init({
				client_id: '905573480053-nj2mct13m72s933mfpvqb65du0hlu51u.apps.googleusercontent.com'
			})
			gauth.then(function(){
				console.log('googleAuth success');
			}, function(){
				console.log('googleAuth fail');
			});
		});
	}
</script>

</head>
<body>
	
<script src="https://apis.google.com/js/platform.js?onload=init" async defer></script> <!-- 다른 예제들을 보니까 맨 밑에 있어서 맨 밑으로 뺌 -->
</body>
</html>
```

여기까지 Initialize 코드 완료!!!!!!!!!!!!!!!!

-------

### GoogleAuth.isSignedIn.get()

에서 보면 로그인이 되어 있으면 true, 아니면 false를 리턴한다.

### GoogleAuth.signIn(), GoogleAuth.signOut()

에서 보면 로그인과 로그아웃을

--------------

### GoogleAuth.currentUser.get()

에서 보면 현재 Google 유저를 리턴한다.

### GoogleUser.getBasicProfile()

| Returns                   |      |
| :------------------------ | ---- |
| `gapi.auth2.BasicProfile` |      |

You can retrieve the properties of `gapi.auth2.BasicProfile` with the following methods:

- BasicProfile.getId()
- BasicProfile.getName()
- BasicProfile.getGivenName()
- BasicProfile.getFamilyName()
- BasicProfile.getImageUrl()
- BasicProfile.getEmail()

- 사용법

  GoogleAuth.currentUser.get().getBasicProfile();

------------

google calendar api scope를 검색하면 Authorizing Requests ~어쩌구 에서 어떤 Scope를 써라라고 나와있다.

​	