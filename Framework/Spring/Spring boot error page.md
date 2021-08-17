# Spring boot error page



Custom Error 페이지 만들어서 사용하는 건 간단합니다. 아래 폴더중에 한 곳에 `error/{응답코드}.<확장명>` 형식으로 파일을 생성하면, 스프링 부트에서 Http 상태 값에 다라서 해당 파일을 로딩해줍니다.

- 폴더
  - `/templates/error`
  - `/static/error`
- 파일
  - `4xx.<확장명>`
  - 400번 대의 모드 상태 코드 발생시 이 파일로 로딩이 된다
  - `404.<확장명>`
  - Http 상태 코드가 404인 경우에 이 파일이 로딩이 된다



#### 참조

- https://blog.advenoh.pe.kr/spring/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-%EA%B8%B0%EB%B3%B8-%EC%98%A4%EB%A5%98-%ED%8E%98%EC%9D%B4%EC%A7%80-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0/