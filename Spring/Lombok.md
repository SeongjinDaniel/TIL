# Lombok

## [공식문서](https://projectlombok.org/features/Builder)

프로젝트를 진행하면서 DB와 데이터를 주고받기 위해  **DTO, VO** Class들을 작성하여 데이터를 손쉽게 다루게 된다. 그런데 항상 반복되는 코드들이 있다. 물론 근래의 IDE들은 이러한 코드들을 자동으로 완성시켜주는 기능들을 가지고 있다. 그럼 `왜? 쓸까?` 먼저 `Lombok`을 이용해 위의 코드를 작성한다.



#### Lombok을 사용한 후

```java
@ToString
@EqualsAndHashCode
@Getter @Setter
public class Student {
    
    private String id;
    private String name;

    public Student(){}

    public Student(String id, String name) {
        this.id = id;
        this.name = name;
    }
}

```

**코드들이 획기적으로 줄어든 것**을 볼 수 있다. 무엇보다도 이 **DTO를 보다 더 명시적으로 볼 수 있다**는 것이다. 또한 기존 각각의 **변수명을 바꾸어 줄경우, 앞서 작성했던 대량의 코드들을 각각 수정을 해주어야 했지**만 지금은 그럴 필요가 없게 되었다. 

#### 장점

위의 장점을 간추려보면 다음과 같다.

**1. 코드작성이 쉽고 필요한 코드가 적다.**

**2. 코드가 명시적이다.**

**3. 수정이 간편하다.**



#### Lombok은 무엇인가?

`Lombok`은 `DTO, VO`등에서 반복적으로 사용되는 코드를 `@`을 통해 작성이 쉽고, 수정이 간편하게 도와주는 라이브러리이다.



#### Lombok의 Annotation(@)

##### @Getter, @Setter

![image](https://user-images.githubusercontent.com/55625864/84736930-da1c1f80-afe1-11ea-910a-f7760a84d8cd.png)

 getter, setter 메소드를 자동으로 생성해준다.

\- AccessLevel이라는 값을 가지고 있어, 이것을 통해 접근제한자를 설정해줄 수 있다. 기본값은 PUBLIC 이다.



**클래스에 @Getter,@Setter**을 줄 경우에는 모든 필드에 대해 생성이 된다. 하지만 **필드에** 부여되는 경우에는 그 필드에 대해서만 getter, setter 생성이 된다. 



##### @ToString

![image](https://user-images.githubusercontent.com/55625864/84737044-0f287200-afe2-11ea-8dd1-af97b4b89838.png)

\- toString() 메소드를 자동으로 생성해준다.

\- exclude라는 값을 가지고 있어, 제외할 필드를 지정할 수 있다.



##### @EqualsAndHashCode

 equals() 와hashCode()를 자동으로 생성해준다.

##### @AllArgsConstructor

![image](https://user-images.githubusercontent.com/55625864/84737154-4434c480-afe2-11ea-8d3e-4978665dd15c.png)

모든 인스턴스 변수를 포함하는 생성자를 생성해준다.

\- 마찬가지로 AccessLevel이란 것을 포함하고 있어 접근제한자를 지정해줄수 있다.



#### [Lombok 사용시 주의할 점](https://kwonnam.pe.kr/wiki/java/lombok/pitfall)

Lombok이 편리하기도 하지만, 완벽한것은 아니기에 개발자가 주의하여 사용해야 합니다. 아래는 그런 문제들을 잘 정리해놓은 블로그입니다. 꼭 참고하시길 바라겠습니다.



출처: https://galid1.tistory.com/531 [배움이 즐거운 개발자]



----



## 생성자 자동 생성

Lombok을 사용하면 생성자도 자동으로 생성할 수 있습니다. `@NoArgsConstructor` 어노테이션은 파라미터가 없는 기본 생성자를 생성해주고, `@AllArgsConstructor` 어노테이션은 모든 필드 값을 파라미터로 받는 생성자를 만들어줍니다. 마지막으로 `@RequiredArgsConstructor` 어노테이션은 `final`이나 `@NonNull`인 필드 값만 파라미터로 받는 생성자를 만들어줍니다.

```java
@NoArgsConstructor
@RequiredArgsConstructor
@AllArgsConstructor
public class User {
  private Long id;
  @NonNull
  private String username;
  @NonNull
  private String password;
  private int[] scores;
}
```

```java
User user1 = new User();
User user2 = new User("dale", "1234");
User user3 = new User(1L, "dale", "1234", null);
```

---



#### @AllArgsConstructor

[@AllArgsConstructor, @RequiredArgsConstructor](https://projectlombok.org/features/constructor) 는 매우 편리하게 생성자를 만들어주지만 개발자의 별 생각없는 꼼꼼함이 치명적 버그가 되게 만들 수 있다. 

위 클래스에 대해 자동으로 `cancelPrice, orderPrice` 순서로 인자를 받는 생성자가 만들어진다. 그런데 개발자가 보기에 `Order` 클래스인데 `cancelPrice`가 `orderPrice`보다 위에 있는것이 마음에 안들어서 순서를 다음과 같이 바꾼다고 해보자. 

이 경우, IDE가 제공해주는 **리팩토링은 전혀 작동하지 않고, lombok이 개발자도 인식하지 못하는 사이에 생성자의 파라미터 순서를 필드 선언 순서에 맞춰 `orderPrice,cancelPrice`로 바꿔버린다.** 게다가 이 두 필드는 **동일한 Type 이라서 기존 생성자호출 코드에서는 인자 순서 변경이 없음에도 어떠한 오류도 발생하지 않는다.** 

이에 의해, 위의 생성자를 호출하는 코드는 아무런 에러없이 잘 작동하는 듯 보이지만 실제로 입력된 값은 바뀌어 들어가게 된다. 

이 문제는 `@AllArgsConstructor`와 `@RequiredArgsConstructor`에 둘 다 존재하며, 이에 따라 이 두 lombok 애노테이션은 사용을 금지하는 것이 좋다. 

대신, 생성자를 (IDE 자동생성등으로) 직접 만들고 필요할 경우에는 직접 만든 생성자에 [@Builder](https://projectlombok.org/features/Builder) 애노테이션을 붙이는 것을 권장한다. 파라미터 순서가 아닌 이름으로 값을 설정하기 때문에 리팩토링에 유연하게 대응할 수 있다. 

---



#### @Builder

Lombok에는 @Builder Annotation도 있다. 이는 모델 객체를 생성할 때 Builder를 자동으로 추가해 주는 Annotation이다. 이를 이용하면 Builder Pattern을 아주 손쉽게 적용할 수 있다.

```java
@Data
@Builder
public class User {
  private String name;
  private int age;
}
```

```java
public class UserBuilderTest {
  @Test  public void builderTest() {
    User user = User.builder()
                  .name("홍길동")
                  .age(19)
                  .build();
    System.out.println(user);
  }
}
```

**@Builder 사용시 특정 속성에 기본값을 설정하려면???**

```java
@Data@Builderpublic class User {
  private String name;
  @Builder.Default  private int age = 19;
}
```

```java
public class UserBuilderTest {
  @Test  public void builderTest() {
    User user = User.builder()
                  .name("홍길동")
                  .build();
    System.out.println(user);
  }
}
```



##### @Builder.Default

If a certain field/parameter is never set during a build session, then **it always gets 0 /** **null** **/ false**. If you've put @Builder on a class (and not a method or constructor) you can instead specify the default directly on the field, and annotate the field with @Builder.Default:

@Builder.Default private final long created = System.currentTimeMillis();



즉, @Builder를 사용한 경우 build()시 설정하지 않으면 0 / null / false가 된다고 언급하고 있다.

위 테스트 코드에서 getAge() 했을 때, 0이 나온 이유이다.



출처: https://tomining.tistory.com/180 [마이너의 일상]



---





