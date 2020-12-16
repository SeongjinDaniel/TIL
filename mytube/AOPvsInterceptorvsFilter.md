# AOP vs Interceptor vs Filter



- Interceptor와 Filter는 Servlet 단위에서 실행된다. <> 반면 AOP는 메소드 앞에 Proxy패턴의 형태로 실행된다.

- 실행순서를 보면 Filter가 가장 밖에 있고 그안에 Interceptor, 그안에 AOP가 있는 형태이다.



#### 참고

- https://goddaehee.tistory.com/154

- [인터셉터(Interceptor)란? + 인터셉터를 이용한 로그인 처리](https://rongscodinghistory.tistory.com/2)