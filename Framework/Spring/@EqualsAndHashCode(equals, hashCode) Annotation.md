# Spring Annotation



#### @EqualsAndHashCode

**@EqualsAndHashCode** 어노테이션은 **equals와 hashcode를 자동으로 생성해주는 어노테이션** 입니다. @ToString 어노테이션과 마찬가지로 **exclude** 파라미터로 필드를 제외하거나 **callSuper** 파라미터로 부모 객체를 생략하거나 포함할수있습니다.

equals : **두 객체의 내용이 같은지, 동등성(equality)를 비교**하는 연산자입니다.
hashcode : **두 객체가 같은 객체인지, 동일성(identity)를 비교**하는 연산자입니다.

@EqualsAndHashCode(of="id"): 연관 관계가 복잡해 질 때, @EqualsAndHashCode에서 서로 다른 연관 관계를 순환 참조하느라 무한 루프가 발생하고, 결국 stack overflow가 발생할 수 있기 때문에 id 값만 주로 사용합니다.

먼저 첫번째로, exclude 파라미터를 알아보겠습니다 exclude = "value1" 는 value1는 동등비교에 포함시키지 않겠다는 의미입니다.

두번째로는 of 파라미터를 알아보겠습니다.  @EqualsAndHashCode(of="id"): 연관 관계가 복잡해 질 때, @EqualsAndHashCode에서 서로 다른 연관 관계를 순환 참조하느라 무한 루프가 발생하고, 결국 stack overflow가 발생할 수 있기 때문에 id 값만 주로 사용합니다.



#### 참조

- [[JAVA] Lombok @Getter, @Setter, @EqualsAndHashCode, @Data 자주쓰이는 어노테이션들](https://donggu1105.tistory.com/99)

