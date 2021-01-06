# Logback



#### logback 예제

```java
package chapters.introduction;
 
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
 
public class HelloWorld1 {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld1");
 
    logger.trace("Hello world.");
    logger.debug("Hello world."); //debug level로 해당 메시지의 로그를 찍겠다.
    logger.info("Hello world.");
    logger.warn("Hello world.");
    logger.error("Hello world.");
  }
}
```



#### Logback 설정 파일 예시

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOGS_ABSOLUTE_PATH" value="./logs" />
 
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <layout class="ch.qos.logback.classic.PatternLayout">
            <Pattern>%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern>
        </layout>
    </appender>
    <appender name="SAMPLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>[%d{yyyy-MM-dd HH:mm:ss}:%-3relative][%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>
    <appender name="ROLLING" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOGS_ABSOLUTE_PATH}/logback.log</file>
        <encoder>
            <pattern>[%d{yyyy-MM-dd HH:mm:ss}:%-3relative][%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOGS_ABSOLUTE_PATH}/logback.%d{yyyy-MM-dd}.%i.log.gz</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <!-- or whenever the file size reaches 100MB -->
                <maxFileSize>5MB</maxFileSize>
                <!-- kb, mb, gb -->
            </timeBasedFileNamingAndTriggeringPolicy>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>
    
    <logger name="com.apress.spring" level="DEBUG">
        <appender-ref ref="SAMPLE" />
    </logger>
    <logger name="com.apress.spring.jeongpro" level="INFO">
        <appender-ref ref="ROLLING" />
    </logger>
    <root level="INFO">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```



#### Appender 종류

**ConsoleAppender**

- 콘솔에 로그를 찍는 방법

**FileAppender**

- 파일에 로그를 찍는 방법

**RollingFileAppender** 

- 여러개의 파일을 순회하면서 로그를 찍는 방법

**SMTPAppender** 

- 로그를 메일에 찍어 보내는 방법

**DBAppender**

- 데이터베이스에 로그를 찍는 방법

기타 SocketAppender, SSLSocketAppender등이 있다.

Console과 RollingFileAppender 가 가장 많이 사용됀다.



3.1 장점 (http://logback.qos.ch/reasonsToSwitch.html)

①log4j보다 약 10배 정도 빠르게 수행되도록 내부가 변경되었으며, 메모리 효율성도 좋아졌다.
②log4j때부터 광범위한 테스트를 진행한 경험을 가지고 있으며, logback은 더욱 높은 레벨의 테스트를 통해 검증되었다.
③문서화가 잘 되어 있다.
④설정 파일을 변경하였을 경우, 서버 재기동 없이 변경 내용이 자동으로 갱신된다.
⑤서버 중지 없이 I/O Faliure에 대한 복구를 지원한다.
⑥RollingFileAppender를 사용할 경우 자동적으로 오래된 로그를 지워주며 Rolling 백업을 처리한다.



#### 참조

- [Logging 서비스](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte:fdl:logging)
- [강력한 자바 오픈소스 로깅 프레임워크, logback 사용법 with example(스프링 부트에서 logback 가이드, logback-spring.xml 설정하기)](https://jeong-pro.tistory.com/154)
- [[LOG\] Log4j, LogBack 정리](https://goddaehee.tistory.com/45)