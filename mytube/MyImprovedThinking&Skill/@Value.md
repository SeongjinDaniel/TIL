# @Value



@Value를 사용하기 위해서

```java
  @Value("${file.path}")
  private String filePath;
```



적용을 했더니 안되는것이 아닌가?

**에러내용**

```
Description:

Parameter 1 of constructor in me.dev.oliver.youtubesns.service.VideoServiceImpl required a bean of type 'java.lang.String' that could not be found.


Action:

Consider defining a bean of type 'java.lang.String' in your configuration.
```



왜 안되지 생각해 봤는데

```java
@AllArgsConstructor
```

를 사용해 생성자 의존성 주입을 하려고 하는 것이었다.



그래서 RequiredArgsConstructor 어노테이션을 통해 fianl 또는 NonNull 어노테이션에만 적용할 수 있게 수정하여 문제를 해결하였다

**solution**

```java
@RequiredArgsConstructor
```

