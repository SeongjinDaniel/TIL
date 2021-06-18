

redis나 memcached같은 캐시 엔진들도 있지만, 저 2개의 캐시 엔진과는 달리 ehcache는 데몬을 가지지 않고 Spring 내부적으로 동작하여 캐싱 처리를 한다.



따라서 redis같이 별도의 서버를 사용하여 생길 수 있는 네트워크 지연 혹은 단절같은 이슈에서 자유롭고 같은 로컬 환경 일지라도 별도로 구동하는 memcached와는 다르게 ehcache는 서버 어플리케이션과 라이프사이클을 같이 하므로 사용하기 더욱 간편하다.



ehcache는 2.x 버전과 3 버전의 차이가 크다.

3 버전 부터는 [javax.cache API (JSR-107)](https://www.jcp.org/en/jsr/detail?id=107)와의 호환성을 제공한다. 따라서 표준을 기반으로 만들어졌다고 볼 수 있다.

또한 기존 2.x 버전과는 달리 3 버전에서는 offheap 이라는 저장 공간을 제공한다. offheap이란 말 그대로 힙 메모리를 벗어난 메모리로 Java GC에 의해 데이터가 정리되지 않는 공간이다.



#### 데이터베이스 캐싱

데이터베이스 쿼리는 데이터베이스 서버에서 수행되기 때문에 속도가 느려지고 부하가 몰릴 수 있다. **결과값을 데이터베이스에 캐싱함으로써 응답 시간을 향상**시킬 수 있다. 대다수의 머신이 동일한 데이터베이스에 동일한 쿼리를 사용하는 경우에 유용하다. 대다수의 데이터베이스 서버는 최적화된 캐싱을 위한 기능을 기본적으로 지원하며, 요구사항에 맞게 수정할 수 있는 파라미터들이 존재한다.



# Spring Cache

Spring Caching Abstraction는 다른 캐시 솔루션을 Spring CacheManager를 통해서 쉽게 사용할 수 있도록 해준다. Spring Caching Abstraction는 **자바 메소드에 캐싱을 적용**하며, 메소드가 실행될 때 넘어온 **파라미터 값에 따라서 캐시**를 적용한다.

## 사용방법

- `pom.xml`



```
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
```

`pom.xml`에 다음과 같이 라이브러리를 추가한 후 `@EnableCaching` 어노테이션을 선언하게 되면 Spring Container에 빈이 등록된다. 기본적으로는 `ConcurrentMapCacheManager` 가 등록되며, 상황에 맞게 다른 캐시 구현체를 등록할 수 있다.

만약 EHCache, Redis 등 서드파티 모듈을 추가하게 되면, `EHCacheManager`, `RedisCacheManager` 를 Bean으로 등록해 사용할 수 있다.

적용하고 싶은 메소드에 `@Cacheable` 어노테이션을 붙이면 적용된다.



**Ehcache와 Redis 비교**

|                    | Ehcache                                                      | Redis                                                        |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 액세스 속도        | JVM 가상 머신에서 직접 Ehcache 캐시, 빠르고 효율적           | Redis는 소켓을 통해 캐시 서비스에 액세스하므로 ecache보다 덜 효율적입니다. |
| 클러스터링 및 분산 | Ehcache에는 캐시 공유 체계가 있지만 RMI 또는 Jgroup 멀티 캐스트를 통한 브로드 캐스트 캐시 알림 업데이트, 캐시 공유가 복잡하고 유지 관리가 불편합니다. 단순 공유는 가능하지만 캐시 복구가 필요하므로 빅 데이터 캐시는 적절하지 않습니다. | Redis는 입증 된 분산 솔루션을 보유하고 있습니다. 대규모 분산 클러스터 배포에 적합합니다. |
| 운영의 복잡성      | Ehcache에서 제공하는 인터페이스는 간단하고 간단하며 Ehcache에서 빌드하여 사용하는 데 몇 분 밖에 걸리지 않습니다. 사실 많은 개발자들이 Ehcache를 사용한다는 사실을 모르고 있으며, ehcache는 다른 오픈 소스 프로젝트에서 널리 사용됩니다. 예 : 최대 절전 모드 | 최소한 사용할 서버와 클라이언트를 설치해야합니다. 작업은 ehcache보다 약간 더 복잡합니다. |



**캐시는 언제 써야할까?**

\* 반복적으로 동일한 결과를 리턴해야하는 작업

\* 서버 자원을 많이 사용하는 작업 또는 시간이 오래걸리는 작업 (API호출, 데이터베이스 조회 쿼리, ...)

-> 데이터가 자주 변경되어 결과도 자주 변경되거나 애초에 소요되는 시간이 짧은 작업들은 굳이 할 필요가 없거나 오히려 역효과가 날 수 있다.



**- 캐시의 필요성**

캐시는 성능과 관련해서 가장 큰 영향력을 갖는다.

-> 데이터베이스 캐시

같은 쿼리를 10000번 날릴 때 같은 응답을 주는 상황에서 쿼리를 10000번 수행할 필요가 없다.

1번 수행하고 9999번은 이미 얻어낸 값을 캐시로 저장해두었다가 리턴해준다면 훨씬 효율적일 것이다.

데이터베이스에서는 쿼리를 최적화하고 DBMS 성능 튜닝 작업을 통해서 캐시 적중률을 높이는 방법으로 오래걸리는 작업을 최소화 시킨다. 아주 근본적인 해결책으로 애초에 실행을 적게할 수 있게 하는 방법으로 꼭 필요하다.

-> 브라우저 캐시

이미지 같은 리소스를 계속 클라이언트로 보내면 통신비용이 어마어마하게 들 것이다.

이런 경우 조금 다른데 서버가 아닌 브라우저가 캐시로 가지고 있어서 동일한 리소스는 다시 받아오지 않는 방법이다.

웹개발에서 이미지파일 이름은 그대로인 대신 다른 이미지로 교체하고 다시 로드하면 교체되지 않는 것을 보았을 것이다.

캐시를 지우고 다시 로드하면 교체한 이미지가 나왔을 것이다.

이런 작업 역시 브라우저가 해주지만 캐시는 꼭 필요하다.

-> 메서드 캐시

 앞서 설명한 이 글의 주제와 같다.

데이터베이스를 통해 가져오라는 명령자체를 타지않게 즉, 메서드 호출이 되지않고 결과를 리턴할 수 있기 때문에 적절하게 사용하면 아주 좋은 효과를 얻을 수 있다.

그리고 굳이 데이터베이스 조회 쿼리같은 것이 아니어도 데이터를 반복적으로 가공한다든지 수행시간이 긴 메서드를 호출한다든지 하는 작업이 있을 때는 서버(Business Layer)에서 캐시를 써야할 필요가 있다.



출처: https://jeong-pro.tistory.com/170 [기본기를 쌓는 정아마추어 코딩블로그]



#### 참조

- https://jaehun2841.github.io/2018/11/07/2018-10-03-spring-ehcache/#ehcache
- [Spring 로컬 캐시 라이브러리 ehcache](https://medium.com/finda-tech/spring-%EB%A1%9C%EC%BB%AC-%EC%BA%90%EC%8B%9C-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-ehcache-4b5cba8697e0)
- [EhCache와 RedisCache 둘다 사용하기](https://velog.io/@bonjugi/Cacheable-EhCache%EC%99%80-RedisCache-%EB%91%98%EB%8B%A4-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-CacheManager)
- [대용량 트래픽 환경에서 게시글 검색시 캐싱 적용하기](https://junshock5.tistory.com/m/105?category=875035)
- [Cache](https://dahye-jeong.gitbook.io/spring/spring/2020-04-09-cache)
- [캐시 추상화](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/cache.html)
- [Jedis 보다 Lettuce 를 쓰자](https://jojoldu.tistory.com/418)
- [SpringBoot + Ehcache 기본 예제 및 소개](https://jojoldu.tistory.com/57)
- [3가지만 기억하자. 스프링 부트 초간단 캐시 @EnableCaching, @Cacheable, @CacheEvict (spring boot cache example)](https://jeong-pro.tistory.com/170)
- [System Properties Comparison Ehcache vs. Memcached vs. Redis](https://db-engines.com/en/system/Ehcache%3bMemcached%3bRedis)
- [[DB/Redis]Redis에 대해서 공부하기, Redis vs Ehcache vs Memcached 비교하며 파악하기](https://postitforhooney.tistory.com/entry/DBRedisRedis%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0-Redis-vs-Ehcache-vs-Memcached-%EB%B9%84%EA%B5%90%ED%95%98%EB%A9%B0-%ED%8C%8C%EC%95%85%ED%95%98%EA%B8%B0)
- [Cache에 대하여.. (Spring+EHCache)](https://jaehun2841.github.io/2018/11/07/2018-10-03-spring-ehcache/#cache%EB%9E%80)
- [Redis or Ehcache?](https://stackoverflow.com/questions/33123633/redis-or-ehcache)
- [Comparison of Ehcache and Redis](https://topic.alibabacloud.com/a/comparison-of-ehcache-and-redis_1_47_10272750.html)
- [Cacheable, EhCache와 RedisCache 둘다 사용하기 (CacheManager)](https://velog.io/@bonjugi/Cacheable-EhCache%EC%99%80-RedisCache-%EB%91%98%EB%8B%A4-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-CacheManager)
- [SpringBoot기반 Redis Cache 활용법](https://yonguri.tistory.com/82)
- [Spring Data Redis - 공식문서](https://docs.spring.io/spring-data/data-redis/docs/current/reference/html/#reference)
- [Spring boot에서 Redis Cache 사용하기](https://deveric.tistory.com/98)
- https://github.com/lettuce-io/lettuce-core
- https://github.com/redis/jedis
- https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-caching-provider-redis
- [Ehcache memcache Redis Three cache tenor](https://topic.alibabacloud.com/a/ehcache-memcache-redis-three-cache-tenor_1_47_30187628.html)
- https://goldfishhead.tistory.com/29
- https://goddaehee.tistory.com/171
- [캐싱 전략](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Strategies.html)
- [강대명님 우아한레디스 강의](https://www.youtube.com/watch?v=mPB2CZiAkKM&t=2302s)



Look aside cache

- cache에 없으면 DB에서 읽어와서 cache에 채운다.