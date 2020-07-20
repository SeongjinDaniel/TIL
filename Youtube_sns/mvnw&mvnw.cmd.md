# mvnw, mvnw.cmd

maven이 설치되어 있지 않은 환경에서도 maven을 사용할 수 있도록 해줍니다.

**mvnw = maven wrraper**



단순 maven을 이용하여 빌드하고 배포할 수 있지만, 좋은 환경을 구성하기 위해 wrapper는 필수입니다.

**mvnw** 과 **mvnw.cmd** 은 Maven Wrapper 를 실행시키기 위한 script 파일입니다.



- Maven Wrapper란 무엇인가?

  **Maven wrapper** 란 개발자들이 Maven 을 별도의 환경에서 개발할 때 local machine 에 **따로 설치를 원하지 않거나 Maven 의 특정 버전을 빌드하길 원할 때** 사용될 수 있습니다.

  다시말해, **Maven wrapper** 을 사용하면 빌드 시 **버전**이나 **개발 환경**에 더이상 의존하지 않아도 되며 **독립적**이게 됩니다.

  Maven wrapper 만 가지고 있으면 별도로 설치하지 않아도 되며, classpath 별다른 Maven version 을 지정할 필요도 없습니다 .



- *mvnw* : 완전히 설치된 Maven 대신 사용되는 실행 가능한 Unix 쉘 스크립트입니다.
- *mvnw.cmd* : 위 스크립트의 배치 버전입니다.





#### 참고

- https://sanghye.tistory.com/34
- https://www.baeldung.com/maven-wrapper