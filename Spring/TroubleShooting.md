# Trouble Shooting

#### 1. output에서 한글 깨짐 현상

- [solution](https://freehoon.tistory.com/146) 이 블로그 참고!!

일단 intellij 의 화면에서 **Shift 키를 두번** 눌러주자
아래와 같은 화면이 열릴 것이다.
그리고 입력창에 'vm' 이라고 입력하자.

조회된 항목 중에서 맨 위에 있는 **'Edit Custom VM Options...'** 를 클릭하자.
그리고 열린 내용의 가장 아랫줄에 **-Dfile.encoding=UTF-8** 를 입력해 주자.

![image](https://user-images.githubusercontent.com/55625864/84768117-a4416000-b00e-11ea-9f2b-0e4b23c15967.png)

intellij를 닫고 새로 시작하자.
그리고 서버를 재시작 해보자.



#### 2. 톰캣 server port shutdown 에러

sevlet 테스트 및 공부를 하다가 서버를 종료하면 "destroy"를 오버라이드해서 "destroy"를 출력하려고 했는데 나오지 않았다 !!!

왜 안나오지? 찾아본 결과 

 원인은 바로 server.xml 설정 중 shutdown 포트가 -1로 잡혀 있었던 것이었다.	



이클립스에서 톰캣 서버를 사용할 때 그 톰캣의 원래 config(server.xml)을 사용하지 않고 Extra Config를 사용한다.

인텔리제이를 처음 사용하면서 이 또한 그럴것 같아 찾아봤으나 인텔리제이의 경우 {TOMCAT_HOME}의 설정값을 참조 하고 있다. 

그래서 Tomcat의 수정이 필요한 경우의 tomcat home에 위치해있는 conf/server.xml을 직접 수정해서 사용해야 톰캣 설정 변경이 가능하다.

**↓↓↓↓↓↓↓↓ 내부 tomcat 파일로 들어가서 수정!! 하니까 해결 ↓↓↓↓↓↓↓↓↓↓↓**

```xml
<Server port="8005" shutdown="SHUTDOWN">
```

**인텔리제이에서 톰캣 서버 종료할 때**

- **shutdown port 번호가 8005로 되어있는것 같다!!**



