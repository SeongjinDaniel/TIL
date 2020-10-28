## 불변 *@ConfigurationProperties* 바인딩



Spring Boot 2.2 ***부터는 @ConstructorBinding\*** **주석을** **사용하여 구성 속성을 바인딩 할 수 있습니다** .

이것은 본질적으로 *@ConfigurationProperties* 주석이 달린 클래스가 이제 [변경](https://www.baeldung.com/java-immutable-object) 불가능할 수 있음을 의미합니다 .

```java
@ConfigurationProperties(prefix = "mail.credentials")
@ConstructorBinding
public class ImmutableCredentials {
 
    private final String authMethod;
    private final String username;
    private final String password;
 
    public ImmutableCredentials(String authMethod, String username, String password) {
        this.authMethod = authMethod;
        this.username = username;
        this.password = password;
    }
 
    public String getAuthMethod() {
        return authMethod;
    }
 
    public String getUsername() {
        return username;
    }
 
    public String getPassword() {
        return password;
    }
}
```

보시다시피 *@ConstructorBinding을* 사용할 때 바인딩하려는 모든 매개 변수를 생성자에 제공해야합니다.

*ImmutableCredentials의* 모든 필드  는 최종적입니다. 또한 setter 메서드가 없습니다.

또한 **생성자 바인딩을 사용하려면 *@EnableConfigurationProperties* 또는 *@ConfigurationPropertiesScan*****을 사용하여 구성 클래스를 명시 적으로 활성화해야** 한다는 점을 강조하는 것이 중요합니다 *.*

#### 참조

- https://www.baeldung.com/configuration-properties-in-spring-boot