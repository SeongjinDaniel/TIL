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

![image](https://user-images.githubusercontent.com/55625864/87226658-30f1fa80-c3d0-11ea-9a0b-ea2adbf057a0.png)



##### CD ( continuous Delivery)

- 변경된 요구사항에 대한 개발/통합/배포/테스트/릴리즈를 자동화하여 SW개발과 운영을 통합하는 DevOps를 지원하는 SW 연속적인배포 출시

![image](https://user-images.githubusercontent.com/55625864/87226756-e2912b80-c3d0-11ea-962c-dbdd50ed523e.png)

##### Naver Cloud Platform 에서의 CI & CD

![image](https://user-images.githubusercontent.com/55625864/87226854-8d094e80-c3d1-11ea-84f4-ec6397e654e1.png)