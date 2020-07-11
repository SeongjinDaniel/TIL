# CI CD

#### 목차

- DevOps란?
- CI/CD 개념
- SourceCommit 소개 및 시나리오





## DevOps란?

- Development와 Operation의 합성어
- SW 개발자들과 IT 종사자들 사이의 의사소통, 협업, 융합을 강조한 개발방법론
- 개발/운영/품질관리 부서 간 통합, 커뮤니케이션 협업을 위한 일련의 방식
- 지속적 환경(지속적 평가, 지속적 delivery와 배포, 지속적 운영, 지속적 통합 및 테스트)이 유지되는 cycle

##### DevOps 구현은?

- 프로세스 자동화
  - 잦은 릴리즈, 잦은 배포
  - 테스트 자동화
  - 지속적 통합
  - 지속적 출시 파이프 라인 마련
- DevOps 도구
  - 지속적 통합 도구: 코드 변경시 마다 통합 & 빌드되고 컴파일 과정에서 자동 테스트 실행, 결과는 Noti
  - 릴리즈 자동화 도구: 클릭한번으로 전체 과정이 수분내 Deploy 릴리즈 실패, 취소도 쉽게 제어
  - 프로비져닝: 서버자원, OS, 스토리지, 계정 프로비져닝 자동화





### CI / CD

##### CI ( continuous Integration )

- 여러 명으로 구성된 팀이 개발(수정)한 소프트웨어를 지속적으로 통합하고 QC(품질통제)하는 애자일 기법
- 자동화된 빌드와 테스트를 통하여 통합 에러 조기 검증으로 단위코드의 품질을 향상("integration hell"방지)
- Build , Test를 실시하는 프로세스를 말하며 이러한 통합 프로세스를 상시로 실시해 주는것을 CI라고 합니다.

![image](https://user-images.githubusercontent.com/55625864/87226658-30f1fa80-c3d0-11ea-9a0b-ea2adbf057a0.png)



##### CD ( continuous Delivery or continuous Deploy)

- 변경된 요구사항에 대한 개발/통합/배포/테스트/릴리즈를 자동화하여 SW개발과 운영을 통합하는 DevOps를 지원하는 SW 연속적인배포 출시
- 짧은 주기로 소프트웨어를 개발하는 소프트웨어 공학적 접근의 하나로, 소프트웨어가 언제든지 신뢰 가능한 수준으로 출시될 수 있도록 보증하기 위한 것. 소프트웨어를 더 빠르게, 더 주기적으로 빌드하고 테스트하고 출시하는 것을 목표로 한다. 이러한 접근은 더 많은 증분 업데이트를 업무 애플리케이션에 적용할 수 있게 함으로써 변경사항의 배포에 대한 비용, 시간, 위험을 줄일 수 있게 함.
- **짧은 주기로 개발중인 소프트웨어를 배포하고 그 과정을 자동화 하겠다는 뜻이다.**

![image](https://user-images.githubusercontent.com/55625864/87226756-e2912b80-c3d0-11ea-962c-dbdd50ed523e.png)

##### Naver Cloud Platform 에서의 CI & CD

![image](https://user-images.githubusercontent.com/55625864/87226854-8d094e80-c3d1-11ea-84f4-ec6397e654e1.png)