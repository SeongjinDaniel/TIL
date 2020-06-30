# Maven

[공식문서](http://maven.apache.org/)

### [spring-boot-maven-plugin](https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/maven-plugin/reference/html/)

#### 메이븐이란?

주로 java 진영에서 프로젝트 빌드, 관리에 사용되는 도구이다. 개발자들이 전체 개발과정을 한 눈에 알아볼 수 있다. 아파치 프로젝트이다.

##### maven의 특징

- 빌드 절차 간소화
- 동일한 빌드 시스템 제공
- 프로젝트 정보 제공

##### 구조

![image](https://user-images.githubusercontent.com/55625864/86114046-fdc48700-bb04-11ea-8590-6b3b00c84dfd.png)



##### ant와의 차이점

1. Ant가 비교적 자유도가 높다. 전처리, 컴파일, 패키징, 테스팅, 배포 가능
2. **Maven은 정해진 라이프사이클에 의하여 작업 수행**하며, 전반적인 프로젝트 관리 기능까지 포함하고 있음. (**Build Tool + Project Management**)

##### gradle과의 차이점

1. XML 대신 groovy 스크립트를 사용하여 **동적인 빌드 가능**.
2. maven은 멀티프로젝트에서 상속구조인데, gradle은 주입 방식이다. 멀티프로젝트에서 gradle이 더 적합하다.

#### 플러그인

- 메이븐은 플러그인을 구동해주는 프레임워크(plugin execution framework)이다. 모든 작업은 플러그인에서 수행한다.
- 플러그인은 다른 산출물(artifacts)와 같이 저장소에서 관리된다.
- 메이븐은 여러 플러그인으로 구성되어 있으며, 각각의 플러그인은 하나 이상의 goal(명령, 작업)을 포함하고있다. Goal은 Maven의 실행단위이다.

![image](https://user-images.githubusercontent.com/55625864/86117079-6281e080-bb09-11ea-860c-13586143e159.png)

- 플러그인과 골의 조합으로 실행한다. ex. `mvn :` = `mvn archetype:generate`
- 메이븐은 여러 goal을 묶어서 lifecycle phases 로 만들고 실행한다. ex. `mvn ` = `mvn install`

#### 라이프사이클

메이븐은 프로젝트 생성에 필요한 단계(phases)들을 Build Lifecycle이라 정의하고 default, clean, site 세가지로 표준 정의한다. Lifecycle은 Build Phase 들로 구성되며 일련의 순서를 갖는다. phase 는 실행단위로서 goal과 바인딩된다.

아래 사진은 Build default 라이프사이클의 주요 phase이고 그 밑에는 전체이다.

![image](https://user-images.githubusercontent.com/55625864/86117468-0f5c5d80-bb0a-11ea-87d5-b3b957e59537.png)



clean : 빌드 시 생성되었던 산출물을 삭제

1. pre-clean : clean 작업 전에 사전작업
2. clean : 이전 빌드에서 생성된 모든 파일 삭제
3. post-clean : 사후작업

default : 프로젝트 배포절차, 패키지 타입별로 다르게 정의됌

1. validate : 프로젝트 상태 점검, 빌드에 필요한 정보 존재유무 체크
2. initialize : 빌드 상태를 초기화, 속성 설정, 작업 디렉터리 생성
3. generate-sources : 컴파일에 필요한 소스 생성
4. process-sources : 소스코드를 처리
5. generate-resources : 패키지에 포함될 자원 생성
6. compile : 프로젝트의 소스코드를 컴파일
7. process-classes : 컴파일 후 후처리
8. generate-test-source : 테스트를 위한 소스 코드를 생성
9. process-test-source : 테스트 소스코드를 처리
10. generate-test-resources : 테스팅을 위한 자원 생성
11. process-test-resources : 테스트 대상 디렉터리에 자원을 복사하고 가공
12. test-compile : 테스트 코드를 컴파일
13. process-test-classes : 컴파일 후 후처리
14. test : 단위 테스트 프레임워크를 이용해 테스트 수행
15. prepare-package : 패키지 생성 전 사전작업
16. package : 개발자가 선택한 war, jar 등의 패키징 수행
17. pre-integration-test : 통합테스팅 전 사전작업
18. integration-test : 통합테스트
19. post-integration : 통합테스팅 후 사후작업
20. verify : 패키지가 품질 기준에 적합한지 검사
21. install : 패키지를 로컬 저장소에 설치
22. deploy : 패키지를 원격 저장소에 배포

site : 프로젝트 문서화 절차

1. pre-site : 사전작업
2. site : 사이트문서 생성
3. post-site : 사후작업 및 배포 전 사전작업
4. site-deploy : 생성된 문서를 웹 서버에 배포



출처: https://sjh836.tistory.com/131 [빨간색코딩]