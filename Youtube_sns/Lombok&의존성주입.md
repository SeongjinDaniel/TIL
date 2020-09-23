# Lombok을 이용해서 의존성 주입



### @AllArgsConstructor

@AllArgsConstructor 어노테이션을 통해 생성자를 만들어 주면 자동으로 의존성 주입을 해주게된다.

하지만, 필드에 선언하는 Class 객체는 선언을 해야한다.



```java
@AllArgsConstructor
@Service
public class UserLoginServiceImpl implements UserLoginService {

  private final UserService userService;
  private final LoginService loginService;
}
```

이렇게 사용하면 생성자를 생성하고 의존성 주입도 자동으로 된다.

클래스를 de-lombok하면 다음과 같이 된다.

```java
@Service
public class UserLoginServiceImpl implements UserLoginService {

  private final UserService userService;
  private final LoginService loginService;
    
  public UserLoginServiceImpl(UserService userService, LoginService loginService) {
      
      this.userService = userService;
      this.loginService = loginService;
  }
}
```





### @AllArgsConstructor vs @RequiredArgsConstructor



**@AllArgsConstructor**

 모든 필드에 대한 생성자 생성한다.

**@RequiredArgsConstructor**

 초기화 되지 않은 final 필드와 @NonNull 어노테이션이 붙은 필드에 대한 생성자 생성한다.

```java
@RequiredArgsConstructor
public class Employee {

    private final String name;
    private int salary;
}
```



```java
public class Employee {

    private final String name;
    private int salary;

    public Employee(String name) {
        this.name = name;
    }
}
```



#### 참고

- [Lombok @AllArgsConstructor, @NoArgsConstructor and @RequiredArgsConstructor](http://www.javabyexamples.com/delombok-allargsconstructor-noargsconstructor-and-requiredargsconstructor)



#### 