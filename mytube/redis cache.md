# Redis caching



#### 주요 어노테이션

- **캐시등록**
  - `@Cacheble`: 캐시가 있으면 캐시의 정보를 가져오고, 없으면 등록한다.
  - `@CacehPut` : 무조건 캐시에 저장한다.
- 캐시삭제
  - `@CacheEvict`
- 

#### 참조

- [SpringBoot기반 Redis Cache 활용법](https://yonguri.tistory.com/82)

- [Spring boot에서 Redis Cache 사용하기](https://deveric.tistory.com/98)
- [SpringBoot기반 Redis Cache 활용법](https://medium.com/@yongkyu.jang/%EC%9A%B0%EB%A6%AC%EA%B0%80-%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC-%EA%B0%9C%EB%B0%9C%ED%95%A0-%EB%95%8C-%EB%B0%B1%EC%95%A4%EB%93%9C-%EC%98%81%EC%97%AD%EC%97%90%EC%84%9C-cache%EB%A5%BC-%EC%A0%81%EA%B7%B9%EC%A0%81%EC%9C%BC%EB%A1%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B2%8C-%EB%90%98%EB%A9%B4-%EC%83%9D%EA%B0%81%ED%96%88%EB%8D%98%EA%B2%83-%EB%B3%B4%EB%8B%A4-%EB%8D%94-%EB%93%9C%EB%9D%BC%EB%A7%88%ED%8B%B1%ED%95%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%84%B1%EB%8A%A5-%EA%B0%9C%EC%84%A0%EC%9D%84-%EA%B0%80%EC%A0%B8%EC%98%AC-%EC%88%98-%EC%9E%88%EB%8B%A4-%EA%B3%A0-%EC%83%9D%EA%B0%81%ED%95%9C%EB%8B%A4-98ab99adfd69)