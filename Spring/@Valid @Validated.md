## @Valid @Validated



#### 스프링에서 사용하기

다양한 기능을 알아보기 전에 Spring에서 Bean Validation을 어떻게 쓰는지 알아보겠다. 의존성에 'spring-boot-starter-validation'을 추가했다면 바로 사용할 수 있다. Service나 Bean에서 사용하기 위해서는 '@Validated'와 '@Valid'를 추가해야 한다.

```java
@Validated // 여기에 추가
@Service
public class ContactService {
    public void createContact(@Valid CreateContact createContact) { // '@Valid'가 설정된 메서드가 호출될 때 유효성 검사를 진행한다.
        // Do Something
    }
}
```

Controller는 '@Validated'가 필요 없다. 검사를 진행할 곳에 '@Valid'를 추가하면 된다.

```java
  @PostMapping("/contacts")
    public Response createContact(@Valid CreateContact createContact) { // 메서드 호출 시 유효성 검사 진행
        return Response
            .builder()
            .header(Header
                .builder()
                .isSuccessful(true)
                .resultCode(0)
                .resultMessage("success")
                .build())
            .build();
    }
```

여기서 주의할 점은 데이터 유효성 검사를 진행할 때 검사가 중복으로 실행되지 않도록 해야 한다는 것이다. 같은 데이터 유효성 검사가 여러 번 실행될 경우 애플리케이션 성능에 영향을 미칠 수 있다는 점을 명심해야 한다.



#### 참조

- https://meetup.toast.com/posts/223
- [[Spring] @Valid, @Validated를 이용한 데이터 유효성 검증](https://velog.io/@damiano1027/Spring-Valid-Validated%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D)
- https://kapentaz.github.io/spring/Spring-Boo-Bean-Validation-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90/#