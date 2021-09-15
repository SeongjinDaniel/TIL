# Spring Redis Session 저장 값



## 저장된 세션값의 의미

| 저장 형식                                    | 자료형 | 역할                                                         |
| -------------------------------------------- | ------ | ------------------------------------------------------------ |
| spring:session:sessions:expires:(session id) | string | 해당 세션의 만료 키로 사용                                   |
| spring:session:expirations:(expire time)     | set    | expire time에 삭제될 세션 정보들을 담고 있음. 해당 time이 되면 저장된 데이터를 조회하여 해당 세션을 모두 삭제 |
| spring:session:sessions:(session id)         | hash   | 세션의 생성 시간, 마지막 세션 조회 시간, 최대 타임아웃 허용 시간과 해당 세션에 저장한 데이터를 저장 |





#### 참조

- https://velog.io/@now_iz/Redis-%EB%A5%BC-spring-%EC%97%90%EC%84%9C-%EC%84%B8%EC%85%98-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80%EB%A1%9C-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0

- https://velog.io/@albaneo0724/Spring-Redis%EB%A5%BC-session-storage%EB%A1%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0