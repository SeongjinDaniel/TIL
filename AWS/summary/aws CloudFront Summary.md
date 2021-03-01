# aws CloudFront Summary



## CloudFront



- 정적, 동적 실시간 웹사이트 컨튼츠를 유저들에게 전달
- Edge Location을 사용
- 컨텐트 딜리버리 네트워크 Content Delivery Network(**CDN**)
- 분산 네트워크 (Distributed Network)



#### Edge Location이 없을 때

<img src="https://user-images.githubusercontent.com/76925694/109384603-5026a380-7931-11eb-8152-ba7a188fe6e5.png" alt="image" style="zoom:67%;" />

#### Edge Location이 있을 때

<img src="https://user-images.githubusercontent.com/76925694/109384627-895f1380-7931-11eb-931e-04b01173fa5a.png" alt="image" style="zoom:67%;" />

- 가까운 서버가 근처에 하나더 가지고 있어 캐싱기능을 사용한다고 생각하면 된다



#### CloudFront 용어 정리

- Edge Location (엣지 지역) : 컨텐츠들이 캐시(Cache)에 보관되어지는 장소
- Origin(오리진) : 원래 컨텐츠들이 들어있는 곳, 웹서버 호스팅이 되어지는 곳. S3, EC2 인스턴스가 오리진이 될 수 있음
- Distribution(분산) : CDN에서 사용되어지며 Edge Location들을 묶고 있다는 개념





