# DB를 여러개 사용하는 방법



**DB 하나 설정**

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://[DB주소]:[port번호]/[DBTable이름]?autoReconnect=true&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Seoul
spring.datasource.username=[DB이름]
spring.datasource.password=[DB비밀번호]
spring.datasource.[해당DB이름].mapper-locations=classpath:lasspath:mapper/**/*.xml
```

**DB 멀티 설정**

```properties
spring.datasource.[해당DB이름].driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.[해당DB이름].jdbc-url=jdbc:mysql://[DB주소]:[port번호]/[DBTable이름]?autoReconnect=true&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Seoul
spring.datasource.username=[DB이름]
spring.datasource.password=[DB비밀번호]
spring.datasource.[해당DB이름].mapper-locations=classpath:mapper/[해당DB이름]/*.xml
```

