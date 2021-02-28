# aws API Gateway



## API와 RESTful API의 이해



#### API는 무엇인가요?

- **A**pplication **P**rogramming **I**nterface



#### RESTful API?

- API종류들 중 하나

- REpresentational State Transfer

- CREATE(post), READ(get), UPDATE(put), DELETE

- JSON형태로 요청을 받고 해결함

- ex) {customer_id": "helo_01,

  ​        "category": "car"}



#### 생각해봅시다

- 대부분의 어플리케이션은 RESTful API 기반으로 운용됨
- 매우 힘든 RESTful API 관리
  - Authentication & Authorization
  - API 요청을 모니터링 해야함
  - 더나은 성능을 위해 API요청 캐시 시스템 필요



#### API Gateway란?

- 뛰어난 확장성 제공 및 API를 만들고 운영하고 모니터링 가능
- Back-end 서비스(웹 어플리케이션, EC2)에 들어있는 데이터 접근 허용
- Pay As You Go

<img src="https://user-images.githubusercontent.com/76925694/109408510-c678e380-79cd-11eb-9240-f18b405f3304.png" alt="image" style="zoom:80%;" />



