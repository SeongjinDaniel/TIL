# aws Code Commit & Code Deploy & Code Pipeline Summary



## CI / CD



- CI : Continuous Integration (지속적인 통합)

- CD : Continuous Deployment (지속적인 배포)



## CI / CD의 장점

- 자동화 시스템 (Automation) - 테스트
- Incremental Change
  - 프로그램을 점차 점차 수정하는 것



## CI / CD - 중앙 리포지토리(Repository)

- **Github**
  - Local & Master branch



## CI / CD - 배포 준비 및 배포

- 배포 준비
- 배포



## Code Commit

- 파일들을 보관하는 저장 장소 (Repository) - Github과 매우 유사
  - 코드, 사진, 라이브러리, 등등...
- 동시에 많은 사람들이 저장 장소 접근 및 업데이트 가능
- 버전 컨트롤 기능 제공
  - 예) **언제 어떻게 누가** 저장 장소 내용을 변경하였는지

<img src="https://user-images.githubusercontent.com/76925694/109409591-62f3b380-79d7-11eb-9461-e1dbccd7308f.png" alt="image" style="zoom:80%;" />

<img src="https://user-images.githubusercontent.com/76925694/109409601-7868dd80-79d7-11eb-92f6-563b26f74f79.png" alt="image" style="zoom:80%;" />

<img src="https://user-images.githubusercontent.com/76925694/109409606-84549f80-79d7-11eb-9c3e-6f668e402848.png" alt="image" style="zoom:80%;" />





## Code Deploy - 자동 배포(Automated Deployment)



#### Code Deploy 장점

- 새로운 기능들의 빠른 배포
- 소프트웨어 & 서버 다운타임 X
- Manual 에러 X



#### Code Deploy 방식

- Rolling 배포 : 점층적 배포
  <img src="https://user-images.githubusercontent.com/76925694/109409876-90416100-79d9-11eb-8007-bbbec78b025e.png" alt="image" style="zoom: 50%;" />

<img src="https://user-images.githubusercontent.com/76925694/109409881-9fc0aa00-79d9-11eb-84e5-793f7327a145.png" alt="image" style="zoom:50%;" /><img src="https://user-images.githubusercontent.com/76925694/109409891-b5ce6a80-79d9-11eb-9976-13d98f1392ae.png" alt="image" style="zoom:50%;" />

<img src="https://user-images.githubusercontent.com/76925694/109409895-bebf3c00-79d9-11eb-8678-8c8575511d69.png" alt="image" style="zoom:50%;"/>

문제가 생겨서 이전으로 돌아가는것은 힘들다

맨 처음 배포할 때 사용한다. 그이유는 Blue/Green 배포 이것은 비용이 발생하기 때문이다

- Blue/Green 배포
  - Blue: 기존 production
  - Blue: 새로 배포할 production
  - 두개의 서버가 필요하기 때문에 추가적인 비용이 발생함

<img src="https://user-images.githubusercontent.com/76925694/109409926-fa5a0600-79d9-11eb-8ec4-b6a950b367d4.png" alt="image" style="zoom: 80%;" />![image-20210228153126077](C:\Users\oliver\AppData\Roaming\Typora\typora-user-images\image-20210228153126077.png)![image](https://user-images.githubusercontent.com/76925694/109409936-0e9e0300-79da-11eb-8566-0723d9e034bb.png)

<img src="https://user-images.githubusercontent.com/76925694/109409936-0e9e0300-79da-11eb-8566-0723d9e034bb.png" alt="image" style="zoom:80%;" />





#### 코드 배포 명령어

ec2를 실행한 후 아래 명령어 실행

```
sudo yum update
sudo yum install ruby
sudo yum install wget
wget https://aws-codedeploy-ap-northeast-2.s3.amazonaws.com/latest/install
chmod +x install
sudo ./install auto
sudo service codedeploy-agent status
```



```
aws deploy create-application --application-name mywebapp
aws deploy push --application-name mywebapp --s3-location s3://aws-learner-code-deploy-bucket/webapp.zip --ignore-hidden-files
```



### Code Pipeline



#### CI/CD의 끝판왕

#### Code Pipeline이 하는 일은?

- 빌드, 테스트, 배포 과정을 관리
  - 코드 변경시 Code Pipeline은 이를 감지할 수 있음
- 소프트웨어 및 어플리케이션 출시 자동화 가능
  - 빠르고 쉬운 디버깅을 가능케 해줌
    - 배포(Deployment) VS 출시(Release)



<img src="https://user-images.githubusercontent.com/76925694/109411419-4a8a9580-79e5-11eb-8c43-bf0107a96776.png" alt="image" style="zoom:80%;" />



