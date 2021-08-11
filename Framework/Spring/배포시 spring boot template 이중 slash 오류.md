# 배포시 spring boot template 이중 slash 오류



### 에러 내용

**Thymeleaf 사용시** 

`org.thymeleaf.exceptions.TemplateInputException: Error resolving template "/index", template might not exist or might not be accessible by any of the configured Template Resolvers`



> When you use one of these templating engines with the default configuration, your templates are picked up automatically from src/main/resources/templates.
>
> Depending on how you run your application, IntelliJ IDEA orders the [classpath] differently. Running your application in the IDE from its main method results in a different ordering than when you run your application by using Maven or Gradle or from its packaged jar. This can cause Spring Boot to fail to find the templates on the classpath. If you have this problem, you can reorder the [classpath] in the IDE to place the module’s classes and resources first.
>
> The resulting jar contains the classes produced by compiling the application and all of the application’s dependencies so that it can then be run by using java -jar. The jar file also contains entries from the application’s classpath. You can add and remove explicit paths to the jar by using --include and --exclude. Both are comma-separated, and both accept prefixes, in the form of “+” and “-”, to signify that they should be removed from the defaults. The default includes are as follows:
>
> public/**, resources/**, static/**, templates/**, META-INF/**, *
>
> *- SpringBoot 2.0.4 Reference -*



`//`에대한 처리는 IDE에서는 처리를 해 주고, jar 배포시에는 처리를 못한다. 이것에 대해 몇가지 테스트를 더 해보았습니다. 우선 코드를 다시 아래와 같이 수정했습니다.

> When you’re running in your IDE the resource is available straight off the filesystem and the double slash doesn’t cause a problem. When you’re running from a jar file the resource is nested within that jar and the double slash prevents it from being found.



#### 참조

https://myserena.tistory.com/155