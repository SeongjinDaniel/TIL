# Facebook Login

google에서 facebook for developer 를 검색 해서 들어간다.

로그인을 눌러서 로그인한다.

그리고 나서 마이앱을 생성하고 url을 http://locahost:8000 ~~~ 어쩌구로 정확히 사이트 url을 기입한다.

그후 끝까지 다음을 누른다.

APP ID: ~~~   -> 클라이언트 아이디와 APP Secret가 생성된다.

Seetings -> Basic에 들어가 보면 App Secret를 볼수있다. 여기서는 사용하지 않는다.

문서 카테고리에서 -> facebook login 클릭

- SDK(Software Devloper Kit)

#### 해야 할 일

1. SDK 환경 설정
2. SDK init(Client id)
3. Login
4. Logout
5. isLogined
6. Facebook API를 이용해서 backend를 개입 하지 않는다.

전체 문서에서 하나씩 적용하면 된다.

현 코드는 적용 순서대로 써놓은 것이다.

```javascript
//Load the SDK asynchronously
function(d, s, id) {                      
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk');
```

```javascript
window.fbAsyncInit = function() {
    FB.init({
        appId      : '188350789064888',
        cookie     : true,                     // Enable cookies to allow the server to access the session.
        xfbml      : true,                     // Parse social plugins on this webpage.
        version    : '{api-version}'           // Use this Graph API version for this call.
    });


    FB.getLoginStatus(function(response) {   // Called after the JS SDK has been initialized.
        statusChangeCallback(response);        // Returns the login status.
    });
};
```

facebook api change 라고 서칭 하면 페이스북 최근버전을 알수있다.

그리고 아이디를 찾아서 기입한다.

---------------

https만 가능 -> 추후 설정

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```





