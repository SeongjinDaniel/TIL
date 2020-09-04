# RequestContextHolder



`RequestContextHolder` 는 Spring에서 전역으로 Request에 대한 정보를 가져오고자 할 때 사용하는 유틸성 클래스이다.



주로, Controller가 아닌 Business Layer 등에서 Request 객체를 참고하려 할 때 사용한다.
Request Param이라던지.. UserAgent 라던지.. 매번 method의 call param으로 넘기기가 애매할 때 주로 쓰인다.
아래처럼 호출하면 같은 `Request Thread` 범위에 있는 경우 요청정보를 얻어낼 수 있다.



```java
RequestContextHolder.getRequestAttributes()
```



다만, 위에처럼 사용하면 Attribute만 얻어올 수 있으므로 아래와 같이 Wrapping해서 사용한다.

```java
HttpServletRequest servletRequest = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
```

이렇게 되면 익히 알고 있는 Cookie, Header ... 등의 정보를 얻을 수 있다.

![image](https://user-images.githubusercontent.com/55625864/92240804-28153500-eef8-11ea-80c4-de172b5b2b7d.png)



## 생성

`RequestContextHolder`는 언제 생성되는지, 그리고 어디서 호출하던 관계없이 Request 정보를 얻을 수 있는지에 대해 알아보자.

일단 이 클래스가 초기화되는건 `Servlet` 이 생성될 때 이다.



즉, Http Request가 오는 시점에 생성 및 초기화가 되어지고 Business Layer를 거친 뒤 Servlet 이 destroy될 때 clean되고 있다.





#### 참고

- https://gompangs.tistory.com/entry/Spring-RequestContextHolder
- http://dveamer.github.io/backend/SpringRequestContextHolder.html
- https://offbyone.tistory.com/144