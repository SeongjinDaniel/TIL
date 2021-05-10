# Intellij에서 sbt 빌드 툴 사용하여 디버깅



1. sbt shell을 설치하여 path 설정을 한다.

2. cmd 창에서 path를 쳤을 때 sbt 파일의 위치와 같은지 확인 한다.

3. 해당 프로젝트가 있는 파일에서 배치 파일을 생성한다.

   아래와 같이 파일 안에 글자를 적고 저장하고 run.bat 라는 파일을 생성한다.

   `sbt -Djava.net.preferIPv4Stack=true -jvm-debug 9999 run`

3. 인텔리제이에서
   ![image-20210510124530803](C:\Users\highbrow20210409\AppData\Roaming\Typora\typora-user-images\image-20210510124530803.png)

   Remote JVM Debug를 사용하여 Port 번호를 Debug할 Port로 변경한다.

4. cmd 창을 켜서 프로젝트 파일 있는 위치로 들어간다. 예) cd C: \Program\server-app
5. 여기서 run.bat를 해주면 `sbt -Djava.net.preferIPv4Stack=true -jvm-debug 9999 run` 이 해당 코드가 실행 되면 run을 할 수 있게 된다.
6. 그 후 인텔리제이에서 벌레 모양 디버그를 클릭하면 디버깅을 할 수 있다. ![image-20210510125100132](C:\Users\highbrow20210409\AppData\Roaming\Typora\typora-user-images\image-20210510125100132.png)

