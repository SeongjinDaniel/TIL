# 인텔리제이에서 Jar파일 export(내보내기) 생성하기



**방법1**과 **방법2**를 나누어서 설명합니다. 먼저 결론을 말씀드리면 방법1로  jar파일로 만들면 모든 의존성들이 jar파일에 모두 들어있기 때문에 방법1을 사용할 것을 권장합니다.

## **방법 1**

인텔리제이 오른쪽 상단에 Maven을 클릭하고 Lifecycle에서 clean을 더블 클릭하여 target 디렉토리 모두를 clean시킵니다.

![image](https://user-images.githubusercontent.com/83576599/128986778-f96c1473-6248-4684-b8e6-234d92438d40.png)

clean을 실행 한 후 package를 더블 클릭하여 target 디렉토리 안에 jar 파일을 생성합니다.

![image](https://user-images.githubusercontent.com/83576599/128986802-b57ddb4a-42c7-4078-b9de-0f2a3ea1de66.png)

아래 jar 파일로 애플리케이션을 실행시킬 수 있습니다.

**실행 명령어**

- `java -jar [jar파일이름.jar]`

![image](https://user-images.githubusercontent.com/83576599/128986817-6d405a3b-af14-40da-a5b7-93e5e2744b54.png)

스프링부트는 내장 JAR로, 만들어진 JAR파일 안에 여러 JAR파일들을 묶어 놓고, 그 JAR파일들을 읽을 수 있는 파일들을 만들어 놓았습니다.



스프링부트는 was서버가 내장되어 배포시에 별도의 서버(톰캣 등)없이 바로 운영이 가능합니다. 물론 별도의 외장 was서버를 사용하는 것도 가능합니다. 여기서는 내장 was를 사용하기 위해서 인텔리제이에서 어떻게 jar파일을 생tjd하는지 알아보겠습니다.



### jar파일 export

<img src="https://user-images.githubusercontent.com/83576599/128816960-eccb3b7f-8532-4fe0-a909-75cf3d87338d.png" alt="image" style="zoom:80%;" />

jar파일을 생성하기 위해서 프로젝트를 실행하고 상단의 file 메뉴에서 Project Structure 메뉴를 선택합니다.

![image-20210810151602998](C:\Users\highbrow20210409\AppData\Roaming\Typora\typora-user-images\image-20210810151602998.png)

상단의 이미지처럼 + 버튼을 누르고 메뉴를 선택합니다.

![image](https://user-images.githubusercontent.com/83576599/128817488-a47d9e83-a177-41b5-919e-8cc83ea95d7c.png)

팝업창이 나오면 위와 동일하게 설정한 후 Main Class 설정하면 됩니다. 스프링부트의 경우 보통 `프로젝트 이름 + Application` 이름으로 클래스가 생성되고 해당 클래스를 지정하면 됩니다.

![image](https://user-images.githubusercontent.com/83576599/128817724-a7acdbe3-2b80-4526-a22a-27d4255db6d0.png)

![image](https://user-images.githubusercontent.com/83576599/128817819-76cbf991-713f-4db7-91fb-0b9f5091ae0c.png)

Output directory부분이 jar파일이 생성되는 경로입니다. 확인 후 OK 버튼을 누릅니다.

다음 차례로 설정하여 jar파일을 생성합니다.

![image](https://user-images.githubusercontent.com/83576599/128817899-4513631e-6478-453b-be16-2ba66272c0fd.png)

위처럼 클릭하면 아래 처럼 나오는데 Build를 선택합니다.

![image](https://user-images.githubusercontent.com/83576599/128818018-df6c6fd9-e18b-456f-9e5d-0fcb522094e8.png)

처음에 지정했던 경로에 가보면 jar파일이 생성된 것을 확인할 수 있습니다.