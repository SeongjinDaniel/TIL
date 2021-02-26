# aws ElasticCache Summary



- 클라우드 내에서 In-memory 캐시를 만들어줌
- 데이터베이스에서 데이터를 읽어오는 것이 아니라 캐시에서 빠른 속도로 데이터를 읽어옴
- **Read-Heavy 어플리케이션에서 상당한 Latency 감소 효과 누림**



## ElastiCache



#### Memcahced

- Object 캐시 시스템으로 잘알려져 있음
- ElastiCache는 Memcached의 프로토콜을 디폴트로 따름
- EC2 Auto Scaling처럼 크기가 커졌다 작아졌다 가능함
- 오픈소스

##### 언제 사용하는가?

1. 가장 단순한 캐싱 모델이 필요한가요?
2. Object caching이 주된 목적인가요?
3. 캐시 크기를 마음대로 scaling하기를 원하나요?



#### Redis

- Key-Value, Set List와 같은 형태의 데이터를 In-Memory에 저장 가능함
- 오픈 소스
- **Muli-AZ 지원**

##### 언제 사용하는가?

1. List, Set과 같은 데이터셋을 사용하나요?
2. 리더보드처럼 데이터셋의 랭킹을 정렬하는 용도가 필요한가요?
3. Multi AZ기능이 사용되어져야 하나요?



 