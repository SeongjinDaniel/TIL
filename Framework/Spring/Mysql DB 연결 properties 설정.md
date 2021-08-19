# [스프링부트] Mysql DB 연결 properties 설정



### DB 하나 사용

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://[host]:[port]/[schemaname]?autoReconnect=true&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Seoul
spring.datasource.username=[******]
spring.datasource.password=[******]
mybatis.mapper-locations=classpath:mapper/*.xml # 각자 mapper 경로에 맞게 설정
```

대괄호로 묶은 것들은 각자의 DB 설정에 맞게 사용



#### DB 다중 사용

```properties
# 첫번째 DB 설정
spring.datasource.homepage.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.homepage.jdbc-url=jdbc:mysql:[host]:[port]/[schemaname]?autoReconnect=true&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Seoul&useSSL=false
spring.datasource.homepage.username=[******]
spring.datasource.homepage.password=[******]
spring.datasource.homepage.generate-dll=false
spring.datasource.homepage.mapper-locations=classpath:mapper/homepage/*.xml # 각자 mapper 경로에 맞게 설정

# 두번째 DB 설정
spring.datasource.sdk.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.sdk.jdbc-url=jdbc:mysql://[host]:[port]/[schema]?autoReconnect=true&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Seoul&useSSL=false
spring.datasource.sdk.username=[******]
spring.datasource.sdk.password=[******]
spring.datasource.sdk.generate-dll=false
spring.datasource.sdk.mapper-locations=classpath:mapper/sdk/*.xml # 각자 mapper 경로에 맞게 설정
```

