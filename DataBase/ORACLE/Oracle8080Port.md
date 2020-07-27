# Oracle 8080 port

오라클 10g express 버전을 인스톨하면 자동으로 8080 포트를 데이터베이스 htmldb 웹 페이지를 위한 포트로 할당 된다.

인지하다 시피 8080 포트가 디폴트 웹서버 포트이다.이것을 아래와 같이 수정한다.

sqlplus 에 system 유저로 로그인해서,



`SQL> exec dbms_xdb.sethttpport(9090)`

```
PL/SQL procedure successfully completed.
```



**결론 : Oracle XML DB 에서 해당 포트를 점유하고 있었다.**



확인하는 법은 다음과 같다.

해당 서비스를 종료시키지 않은 상태에서 웹브라우져에서 http://localhost:8080/ 를 치고 들어간다.

그러면 로그인창이 뜨는데 자신의 db 계정을 치면 된다. 그러면 로그인이 된다.



#### 참조

- [오라클 10g xe, 9i 8080 포트 변경하기](http://blog.naver.com/tyboss/70020789950)