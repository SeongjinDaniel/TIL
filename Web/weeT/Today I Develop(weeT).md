# 개발 일지

#### JPA설정 방법

- pom.xml

```xml
<!-- https://mvnrepository.com/artifact/org.eclipse.persistence/org.eclipse.persistence.jpa -->
<dependency>
<groupId>org.eclipse.persistence</groupId>
<artifactId>org.eclipse.persistence.jpa</artifactId>
<version>2.5.2</version>
</dependency>
```

@Entity 어노테이션을 사용할 수 있게 해준다.

- @NotEmpty

```xml
<dependency>
<groupId>javax.validation</groupId>
<artifactId>validation-api</artifactId>
<version>1.1.0.Final</version>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-validator</artifactId>
<version>5.1.3.Final</version>
</dependency>
```
- @CookieValue Annotation을 이용하면 쿠키 값을 파라미터로 전달받을 수 있다.

  

  @CookieValue Annotation은 해당 쿠키가 존재하지 않으면 기본적으로 500 에러를 발생시킨다. 따라서, 쿠키가 필수가 아닌 경우에는 required 속성의 값을 false로 지정해 주어야 한다. required 속성의 기본 값은 true이다.

  required 속성의 값을 false로 지정할 경우, 해당 쿠키가 존재하지 않으면 null을 값으로 전달받게 된다.