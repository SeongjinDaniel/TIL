# OAuth

사용자가 가입된 서비스의 API에 접근하기 위해서는 사용자로부터 권한을 위임 받아야 합니다. 이 때 사용자의 패스워드 없이도 권한을 위임 받을 수 있는 방법이 필요합니다. 이를 위해서 고안된 기술이 OAuth입니다. 오늘날 많은 API들이 OAuth를 통해서 상호 연동을 지원하고 있습니다. 



OAuth는 third party에서 accessToken이라는 비밀번호를 발급하고 우리의 서비스는 OAuth를 통해 accessToken을 획득한 다음에 우리가 필요로 하는 그들의 서비스를 사용하는 것이다.

![image](https://user-images.githubusercontent.com/55625864/101973687-31dbd080-3c7d-11eb-83e8-d3d7c1d04eee.png)

---

![image](https://user-images.githubusercontent.com/55625864/101973710-50da6280-3c7d-11eb-8adb-cffc30764e42.png)





### OAuth를 등록하는 절차

![image](https://user-images.githubusercontent.com/55625864/101974889-b3cbf980-3c7d-11eb-86cf-4aeec7934bf3.png)

![image](https://user-images.githubusercontent.com/55625864/101975181-e0801100-3c7d-11eb-8d0f-86cb945cacaf.png)

oauth2 *클라이언트*가 *레지스터 서버*에 등록하기 위한 필수요소: **클라이언트 ID, 클라이언트 Secret, Authorized redirect URL**

- 클라이언트 Secret을 노출하면 엄청난 보안사고가 일어날 수 있다.

- Resource Server가 권한을 부여하는 과정에서 Client한테 Authorized code라는 값을 전달해 줄 것이다.
  그 때의 Resource Server가 이 주소로 전달해 주세요라고 알려준것임. Resource Server는 저 주소 말고 다른 서버로 요청을 하면 무시하게 될것이다.



### Resource Owner의 승인

예를들어, Third party의 기능인 구글 캘린더를 사용해서 글을 쓴다던지, 페이스북에 글을 쓴다는 행동을 하기위해서는 인증을 받아야하므로 그 Third party의 로그인을 통해 인증을 받아야한다. 뭐가 됐건간에 사용자가 동의를 해야 받아들일 수 있을것이다.



Resource owner와 Resource Server의 승인 단계 -> Resour Server가 어디까지 승인해 줄것인지 물어보고 Resource owner가 승인을 하는 과정.

![image](https://user-images.githubusercontent.com/55625864/101975456-12927280-3c80-11eb-80b6-6fa03e643b8a.png)

### Resource Server의 승인

Resource Server는 Client가 등록된 Client가 맞는지 확인하기 위해서 Resource Owner을 통해서 Client에게 Authorization code를 전달합니다. 이 값을 받은 Client는 이 값과 Client secret의 값을 Resource Server로 전송해서 Client의 신원을 Resource Owner에게 증명합니다.



그 다음 단계는 accessToken을 발급 받게 된다.



### Access token

**OAuth의 목적은 AccessToken을 발급 받는 것이다.**

![image](https://user-images.githubusercontent.com/55625864/101975678-94cf6680-3c81-11eb-9c64-1d12bbd678de.png)

Resource Server는 User id가 1이고, acessToken이 4인것을 가진 클라이언트에게 scope b, c를 허용해서 동작하게 해야겠다해서 동작이 되는것이다.



### Refresh token

Access token은 수명이 있습니다. Access token의 수명이 다했을 때 새로운 access token을 발급 받는 방법이 refresh token입니다.

이 때마다 Access token을 사용자에게 발급받게 하면 힘들기 때문에 쉽게 token을 발급받게 하기 위해서 refresh token이 사용된다. 

refresh token을 통해 Access token을 다시 발급 받게 된다. refresh token도 새로 발급 될수도 있고 Access token만 새로 발급 받게 되는 경우도 있다.

![image](https://user-images.githubusercontent.com/55625864/101975836-12e03d00-3c83-11eb-906b-0741b31591c4.png)



#### 참조

- [생활코딩](https://opentutorials.org/course/3405) 