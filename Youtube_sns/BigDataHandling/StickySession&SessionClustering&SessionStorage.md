scale out을 할 때 서버가 최소 2대 이상이면 Session id를 공유 할 수 없는 문제가 발생 할 수 있다고 했습니다. 다시한번 더 말씀드리면 클라이언트가 한 대의 서버에 로그인 요청을 한 후 다시 로드 밸런서에 의해 다른 서버에 새로운 요청을 했을 때 Session id를 가지고 있지 않아 다시 로그인하라는 페이지로 리다이렉트 될 수 있습니다. 이러한 문제를 해결할 수 있는 **Sticky Session**을 알아 보도록 하겠습니다.



# Sticky Session



sticky session은 클라이언트가 요청 했을 때 한 대의 서버와 쿠키 또는 세션을 사용하여 고정된 서버를 사용하여 통신하는 방식을 말합니다.

![image](https://user-images.githubusercontent.com/55625864/95205950-096ccb80-0821-11eb-9451-59eb4c1d801f.png)



ClientA는 Load balacer로 인하여 ServerA와만 통신을 하고 ClientB도 ServerB와만 통신을 하게 하는 방식을 sticky session이라고 합니다. 

sticky session은 계속해서 session을 만들지 않고 고정된 session을 사용하기 때문에 session을 생성하는 과정이 제거되고 조금 더 빠른 성능을 가져올 수 있는 장점이 있습니다.



하지만 당연하게도 하나의 고정된 서버를 사용하면 단점이 존재합니다. 하나의 서버가 고장나게 되면 그 안에 있는 내부 session 정보들을 다 날려버릴 수도 있고 그 서버를 사용하고 있던 모든 Client는 session이 끊기는 상황이 발생됩니다.

![image-20201006222848878](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20201006222848878.png)

이러한 정합성 문제점을 해결하기 위해서 session 정보를 다른 서버에도 저장해서 사용하는 session clustering 방식을 사용하게 됩니다.



# Session clustering





#### 참고

- [What is load balancing?](https://www.citrix.com/ko-kr/glossary/load-balancing.html)
- [sticky session](https://www.imperva.com/learn/availability/sticky-session-persistence-and-cookies/)

- https://www.ramkitech.com/2012/10/tomcat-clustering-series-simple-load.html
- https://www.javacodegeeks.com/2012/11/tomcat-clustering-series-part-2-session-affinity-load-balancer.html
- https://www.ramkitech.com/2012/11/tomcat-clustering-series-part-3-session.html
- https://www.ramkitech.com/2012/12/tomcat-clustering-series-part-4-session.html
- https://www.ramkitech.com/2013/01/tomcat-clustering-series-part-5-nginx.html