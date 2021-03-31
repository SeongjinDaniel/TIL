# Algorithm answer of Stream



#### Question

- [Lv1_문자열 내림차순으로 배치하기](https://programmers.co.kr/learn/courses/30/lessons/12917)

```java
import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.util.Comparator;

public class ReverseStr {
    public String reverseStr(String str){
        return Stream.of(str.split(""))
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.joining()); // collect(Collectors.joining(", ") 이렇게 하면 Z, b, c d, e, f, g 이런식으로 출력이 된다!
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
    }
}
```

