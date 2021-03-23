# wrapper클래스,박싱(boxing),언박싱(unboxing)



 박싱(boxing)이란 기본형을 참조형으로 변환하는 것이고 언박싱(unboxing)이란 반대로 참조형을 기본형으로 바꾸는 것이다. 그리고 JDK 1.5부터는 이것을 자동으로 해주는 기능이 추가되었다.



```java
public class Tut02 {
    public static void main(String[] args) {
        Integer iA = new Integer(123);
        Integer iB = new Integer(123);
        
        int ia = (int)iA; //(1) 언박싱(unboxing)
        int ib = iB; //(2) 오토언박싱(auto unboxing)
        Integer iC = (Integer)456; //(3)박싱(boxing)
        Integer iD = ia; //(4)오토 박싱(auto boxing)
    }
}


출처: https://studymake.tistory.com/420 [스터디메이크]

출처: https://studymake.tistory.com/420 [스터디메이크]

출처: https://studymake.tistory.com/420 [스터디메이크]
```





#### 참조

- https://studymake.tistory.com/420 [스터디메이크]

