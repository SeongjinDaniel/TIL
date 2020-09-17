# Sticky session



#### ELB(Elastic Load Balancer)란?

- Elastic Load Balancing의 약자로써, **부하분산(Traffic Load Balance, 대용량 트래픽을장애 없이 처리하기 위해 여러 대의 서버에 적절히 트래픽을 분배하는 것)과 고가용성(High Availability)**을 위한 서비스 이다.(AWS 프리티어 계정에서 무료로 사용 가능)
- ELB는 아마존에서 제공하는 일종의 L4와 같은 로드 밸런서이다. 내부적으로 VM위에서 동작하는 소프트웨어 로드밸런서이고, 아마존 환경에 맞춰서 최적화 되어 있다.



로드밸런싱이 필요한 대규모 트래픽이 발생하는 서비스에서는 세션 관리에 문제가 생길 수 있다. 여러 서버가 있을 때 한 서버에 JSESSIONID, VALUE를 저장 하고 있지만, 다른 서버에 로그인 요청을 했을 때 JSESSIONID, VALUE가 없기 때문에 로그인 오류를 나게 한다. 방금 로그인 했는데 바로 또 로그인을 하라고 하는 사태가 발생할 수 있다.



결국 이런 세션 관리의 문제를 해결하기 위한 방법 중 하나는 **Sticky Session** 을 사용하는 것이다.



#### Sticky session이란?

- ELB 옵션으로 사용된다.
- ELB는 기본적으로 라운드로빈 방식으로 트래픽을 분산 하는데, **이를 쿠키 또는 세션을 사용하여 트래픽을 분산하는 기능**이다.
- 즉, **특정 사용자가 접속을 시도 했을 때 처음 접속된 서버로 계속해서 접속되도록(특정 세션의 요청을 처음 처리한 서버로만 보내는 것)** 트래픽을 처리하는 방식이다.

이렇게 첫 요청 이후의 모든 요청을 특정 서버로 고정하는 방법으로 세션 관리를 한다. 



일반적으로 특정 서버로 요청 처리를 고정시키는 방법은 Cookie를 사용하거나 클라이언트의 IP tracking 하는 방식이 있다. 참고로 AWS ELB는 cookie를 사용하여 Http Response에 cookie를 이용해서 해당 클라이언트가 가야하는 EC2 instance의 정보를 저장해두고 그걸 활용하여 특정 EC2로 요청을 고정한다.

- [아마존 ELB와 Sticky session 예시](https://aws.amazon.com/ko/blogs/aws/new-elastic-load-balancing-feature-sticky-sessions/)

- **Sticky session 필요성**

  - 로그인 세션을 유지하기 위해서 사용한다.
  - 서버가 여러대 있을 때 어떤 서버로 session을 유지 할 때 어떤 서버에 session이 유지 되어 있는지 모를 수도 있지만 Sticky session을 사용하여 처음 접속된 서버로 계속해서 접속되도록 트래픽을 처리한다.

- **단점**

  - 로드밸런싱이 잘 동작하지 않을 수 있다
  - 특정 서버만 과부하가 올 수 있다.
  - 특정 서버 Fail시 해당 서버에 붙어 있는 세션들이 소실될 수 있다.

  이러한 단점들을 고려한 세션 관리 기법 중 **Session Clustering** 방식이 있다.

  



# Session Clustering

- 여러 WAS의 세션을 동일한 세션으로 관리하는 것이다.

- 각 WAS들은 세션을 각각 가지고 있지만, 이를 하나로 묶어 하나의 클러스터로 관리하는 것이다.
  이 상태에서 하나의 WAS가 fail 발생하면 해당 WAS가 들고 있던 세션은 다른 WAS로 이동되어 그 WAS가 해당 세션을 관리한다.

- 각 서버마다 세션 클러스터링 방식이 다르고, 지원하는 방식이 다르기 때문에 현재 사용하고 있는 WAS의 session clustering 부분을 보고 확인해야 한다.

  하지만 이 방식은 scale out 관점에서 새로운 서버가 하나 뜰 때마다 기존에 존재하던 WAS에 새로운 서버의 IP/Port를 입력해서 클러스터링 해줘야 하는 단점이 있다.

  새로운 서버를 띄우면 기존 서버에 수정이 발생하고, 휴먼 에러가 발생할 가능성도 충분히 있다. 그렇기 때문에 Session server를 따로 두고 관리하는 방식도 있다.

  ![image](https://user-images.githubusercontent.com/55625864/87243426-ed9b9880-c470-11ea-8b73-f666de7437e3.png)

  위와 같은 방식은 새로운 서버를 띄우더라도 해당 서버에만 세션 서버의 정보를 적어주고 연결 해주면 되기 때문에 scale out 할 때 기존 서버의 수정이 발생하지 않는다는 장점이 있다.

  대신 Redis Session 서버의 중요성이 올라가고, 해당 세션 서버가 죽는 순간 모든 세션이 사라지기 때문에 이 Redis 서버의 다중화도 고려해보아야 할 점이다. (사용해 본 적은 없지만 Redis가 Replication 설정이 쉽다고 한다.)

### 참고자료

- https://d2.naver.com/helloworld/284659
- https://www.citrix.co.kr/glossary/load-balancing.html
- https://bcho.tistory.com/794
- https://docs.spring.io/spring-session/docs/current/reference/html5/guides/boot-redis.html
- https://brunch.co.kr/@springboot/114
- http://tomcat.apache.org/tomcat-8.5-doc/cluster-howto.html
- https://smjeon.dev/web/sticky-session/

