# aws ELB summary



#### ELB (Elastic Load Balancer)

- 수 많은 서버의 흐름을 균형있게 흘려보내는데 중추적인 역할을 함
- 하나의 서버로 traffic이 몰리는 병목현상(bottleneck) 방지
- Traffic의 흐름을 Unhealthy instance -> healthy instance로



1. Application Load Balancer : OSI Layer7에서 작동됨
   - HTTP, HTTPS와 같은 traffic의 load balancing에 가장 적합함
   - 고급 request 라우팅 설정을 통하여 특정 서버로 request를 보낼 수 있음
2. Network Load Balancer : OSI Layer4에서 작동됨, 매우 빠른 속도를 자랑하며 Production 환경에서 종종 쓰임
   - 극도의 performance가 요구되는 TCP traffic에서 적합함
   - 초당 수백만개의 request를 아주 미세한 delay로 처리 가능
3. Classic Load Balancer : 현재 Legacy로 간주됨, 따라서 거의 쓰이지 않음.
   - Layer7의 HTTP/HTTPS 라우팅 기능 지원
   - Layer4의 TCP traffic 라우팅 기능도 지원



- Load Balancer Error : 504 ERROR

<img src="https://user-images.githubusercontent.com/76925694/109016510-985b8100-76f9-11eb-89a3-01e3c1bd3239.png" alt="image" style="zoom: 67%;" />



- X-Forwarded-For 헤더
  - EC2는 Private IP address밖에 볼 수가 없음!!
  - X-Forwarded-For 헤더를 통해 public IP address를 받을 수 있음

<img src="https://user-images.githubusercontent.com/76925694/109016831-e8d2de80-76f9-11eb-8115-aa5b0f5fe033.png" alt="image" style="zoom:67%;" />

