# SpringBoot Junit5에서 Junit4로 변경



pom.xml에서 이부분 삭제 하면 junit 4 사용가능 !!!!

```xml
<exclusions>
    <exclusion>
        <groupId>org.junit.vintage</groupId>
        <artifactId>junit-vintage-engine</artifactId>
    </exclusion>
</exclusions>
```

