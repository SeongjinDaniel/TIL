# Web2 - OAuth 2.0

나의 서비스가 있고(opentutorals.org), 

사용자, 

나의 서비스가 연동하려고 하는 그들의 서비스(Google, Facebook, Twitter ...) 



나의 서비스가 사용자를 대시해서 Google과 같은 calendar에서 저장 한다던지 Facebook 에서 글을 공유 하고 싶다던지를 하고 싶다면,,,, 나의 서비스가 그들의 서비스에게 허가를 받아야한다.

우리가 사용자의 ID와 패스워드를 기억하고 있다가 그들의 서비스에 모든 기능을 다 사용할 수 있기 때문에 아주 강력한 방법이다. 하지만 이것은 아주 위험하고 걱정되는 방법이다. 사용자 입장에서 처음보는 서비스를 신뢰할 수 가 없기 때문에 또한 보안 사고들이 일어 날 수 있기 때문에 ,,,, 유출 될 수 있는 고초들,,, Google, Facebook 입장에서도 다른 누군가가 가지고 있다는 것은 불만족 스러운 것이다.

그래서 oAuth를 통해서 우리가 만든 서비스와 그들이 만든 서비스를 안전하게 연결 시켜준다.

-> 예전에는 나의 서비스에서 그들의 서비스의 ID, Password를 가지고 있었지만 이것에는 비밀 번호 대신에 accessToken을 발급한다.

장점 

1. 그들의 ID, Password가 아니다.
2. 그들의 서비스가 꼭 필요한 필수적인 기능만 부분적으로 허용하는 비밀번호이다. 그래서 accessToken을 획득하고 이것을 통해서 그들의 데이터를 생성 삭제등을 할 수 있게 된다.

federated identity: 
Digital identity platforms that allow users to log onto third-party websites, applications, mobile devices and gaming systems with their existing identity, i.e. enable social login,

federated identity:  회원을 식별할 수 있는 기능을 구현할 수 있다. 

--------------

## 역할

OAuth에 등장하는 3자에 대한 역할과 용어.

위에 서 말했던 그들(Resource Server : 데이터를 가지고 있는 서버)

그들(Authorization Server : 인증과 관련되 처리를 전담하는 서버)

User = Resource Owner

나의 서비스 = Client

---------

## 등록

OAuth를 이용해서 Resource Server에 접속하기 위해서는 우선 Resource Server에 등록하는 과정이 필요(Client --resgister---> Resource Server)

![image-20200223175333600](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200223175333600.png)

- Create app

  - Clent ID : 1          --> ID라고 할 수 있고

  - Client Secret : 2  --> Password(외부에 절대 노출 되면 안된다. 엄청난 보안 사고가 일어남)

  - Authorized redirect URIs    :  https://client/callback

    Resource Server 권한을 부여하는 과정에서 Authorized Code값을 전달 받게 되는데 그때의 이 주소로 전달해 주세요 라고 알려주는것임.

구글, 페이스북에서 등록하는 방법 소개도 함(https://opentutorials.org/module/3668/22005)

-----------

## Resource Owner의 승인

OAuth의 첫번째 절차는 Resource Owner가 Resource Server에게 Client의 접근을 승인.



Resource Owner(User)는 우리의 Application에 접속할 거고, 그리고 접속을 하는 과정에서 Resource Server에 Facebook에서 글을 기재 한다던지, Google 캘린더를 사용한다던지 하는 상황들이 있을 수 있을 것이다.

Faceboo, Twitter, Google 등의 버튼 등은 href 태그를 이용해서 주소를 적어주면 된다.

https://resource.server/?client_id=1&scope=B(사용할 서비스),C(사용할 서비스)&redirect_uri=https://client/callback

B : example) https://www.googleapis.com/auth/plus.login  

C : example) https://www.googleapis.com/auth/userinfo.email

Resource Owner가 로그인을 하고 있지 않다면 Resource Server가 로그인을 하라는 창을 보여준다. Resource Owner가 로그인을 해서 성공하면 Resource Server는 여기에 있는 Client가 가지고 있는 Client_id 값과 비교하고 Resource Server는 자신이 가지고 있는 Client id를 확인하여 redirect URL: https://~~~ 값과 Clinet에서의 redirect_uri값을 비교해ㅓ 다르면 작업을 끝내 버린다. 만약 같다면 Resource Owner에게 Client에게 scope에 해당하는 것들을 부여할 것인지 확인하는 메세지를 Resource Owner에게 전송하게 된다. 허용하면 Resource Server는 user_id : ~는 scope : b, c에 대한 작업을 허용하는 것에 동의 하였다 라는것을 저장한다.

여기까지는 Client가 Resuorce Owner에게 동의를 구하는 과정이다.

-------

## Resource Server의 승인

Resource Server는 Client가 등록된 Client가 맞는지 확인하기 위해서 Resource Owner을 통해서 Client에게 Authorization code를 전달합니다. 이 값을 받은 Client는 이 값과 Client secret의 값을 Resource Server로 전송해서 Client의 신원을 Resource Owner에게 증명.

Resource Server는 임시 비밀 번호(authorization code : 3)를 Resource Owner한테 전송한다. Location:https://client/callback?code=3 (Location : https한테 https://client/callback?code=3이 주소로 이동하세요 라고 명령한 것이다.)

Location 헤더 값에 의해서 Resource Owner의 사용자 사람이 인식하지도 못하게 은밀하게 https://client/callback?code=3이 주소로 이동을 하게 된다.(Resource Owner -> Client) 그러면 code=3에 의해서 Client는 authorization code : 3을 갖게 된다.

Client가 Resource Server에게 access token을 발급받기 전 단계까지 온상태이다.

Client는 Resource Server에게 https://resource.server/token?grant_type=authorization_code&code3&redirect_uri=https://client/callback&client_id=1&client_secret=2 전송을 한다.

![image-20200223184838972](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200223184838972.png)

authorization_code 외에도 4가지 형태의 방법이 더있다.

이 때 Resource Server는 authorization_code를 자신의 것과 Client에서 전송한 것과 맞는지 확인한다. 또한 client_id, client_secret, redirect_uri가 완전히 맞는지 확인한다. 모두 일치 한다면 그 때 다음 단계로 진행하게 된다.

Acess Token

-------------

## Access token

OAuth의 핵심인 access token의 값을 발급 받는 과정.

Resource Source는 authorization_code 를 인증을 했기 때문에 이제 삭제한다.

![image-20200223185958707](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200223185958707.png)

그리고 나서 accessToken:4를 생성하고 AccessToken=4를 Client에게 전송한다. Client는 AccessToken=4라는 것을 내부적으로 저장한다. DataBase나 파일이나 이런 곳에.

AccessToken으로 Client가 Resource Server에 접근을 하게 되면 AccessToken=4를 보고 Client_id : 1번 사용자의 b, c에 권한이 있는 유효한 key이니까 사용자의 정보에 대해서 AccessToken=4를 가진 Client에게 허용을 해야겠다 라고 생각하고 동작하게 된다.

-----

## API 호출

API가 무엇인지, Access token을 이용해서 API를 호출하는 방법.

이제는 Resource server를 handling 해야한다.

Resource Server를 사용할 때는 API를 사용해야한다.

https://developers.google.com/calendar/v3/reference 사이트에서 많은 API를 볼수있다.

https://www.googleapis.com/calendar/v3/calendars/calendarId를 접속하면 아직 token을 받지 않았으니까 제대로 된 내용이 나오지 않는다.

https://developers.google.com/identity/protocols/OAuth2WebServer 여기서 Calling Google APIs ->http/rest 에 정확히 읽어보면 방식을 권하고 있다.

더 좋은 방식은 이것이다.

```
GET https://www.googleapis.com/drive/v2/files?access_token=access_token
```

https://www.googleapis.com/calendar/v3/calendars/calendarId?access_token=access_token(실제 값을 넣어야한다.) 

이렇게 요청 하면 이 내용을 볼수 있다.

```
curl -H "Authorization: Bearer access_token(실제값을 넣어야한다.)" https://www.googleapis.com/drive/v2/files
```

하지만 이렇게 적용해야 보안을 더 높일 수 있다.

```
curl -H "Authorization: Bearer access_token(실제값을 넣어야한다.)" https://www.googleapis.com/calendar/v3/calendars/calendarId
```

curl이라는 프로그램을 이용해서 페이지를 요청 하면 웹페이지를 다운 받을 수있다.

curl -H "Authorization: Bearer access_token(실제값을 넣어야한다.)" https://www.googleapis.com/calendar/v3/calendars/calendarId

이명령을 붙여 넣으면 그 안에 값들을 가져올수 있다. 이것을 사용하면 더 안전하게 서버와 통신을 할 수 있다.

--------

## Refresh token

Access token은 수명이 있습니다(1시간 2시간 길게는 60일 90일). Access token의 수명이 다했을 때 새로운 access token을 발급 받는 방법이 refresh token.

구글에서 oauth 2.0 rfc 검색한후 [RFC 6749 - The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749) 여기에 들어가보면 **The OAuth 2.0 Authorization Framework**  의 표준 문서가 있다.

여기서 목차에 Refresh Token 으로 가면 설명이 있고 그림을 잘 그려놨다. 참고!!

현재 우리는 Resource Server와 Authorization Server를 퉁 쳤는데 여기서는 구분하고 있다.

Authorization Grant : 권한을 허가 한다.

보통 Access Token을 발급 받을 때 Refresh Token을 같이 주는 경우가 있다. 하지만 Refresh Token을 안주는 경우가 있다.

Access Token을 잘 쓰고 있따가 Invalid Token Error이 뜨면 Access Token의 수명이 끝난것이다. 그럼 우리의 Client는 보관하고 있던 Refresh Token을 Authorization Server에게 전달하면서 Acess Token을 다시 발급 받는다.

(H)를 보면은 경우에 따라서는 refresh token을 새로 발급 되는 경우가 있고 access token만 갱신 되는 경우도 있다고 한다.

**구글 Identity Platform**

https://developers.google.com/identity/protocols/OAuth2WebServer 여기에서 Refreshing an access token (offline access)이 곳에 가보면은 매뉴얼을 제공한다.

```
POST /token HTTP/1.1
Host: oauth2.googleapis.com
Content-Type: application/x-www-form-urlencoded

client_id=your_client_id&
client_secret=your_client_secret&
refresh_token=refresh_token&
grant_type=refresh_token
```

client_id, client_secret, refresh_token, grant_type 이값들을 전송하면 구글에서는

```json
{
  "access_token": "1/fFAGRNJru1FTz70BzhT3Zg",
  "expires_in": 3920,
  "scope": "https://www.googleapis.com/auth/drive.metadata.readonly",
  "token_type": "Bearer"
}
```

이렇게 json 포맷으로 return해준다. 새로 만들어진 access_token과 이것이 얼마동안 유효한지 보내준다.라는 뜻이다.

-------

