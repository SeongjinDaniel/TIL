# Lv1_문자열 내림차순으로 배치하기



#### Question

- [Lv1_문자열 내림차순으로 배치하기](https://programmers.co.kr/learn/courses/30/lessons/12917)



#### mine

```java
import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        List<Character> list = new ArrayList<Character>();
        
        for(int i = 0; i < s.length(); i++) {
            list.add(s.charAt(i));
        }
        
        list.sort(Comparator.reverseOrder());
        for(Character data : list) {
            answer += data;
        }
        
        return answer;
    }
}
```



#### etc

```java
import java.util.Arrays;

public class ReverseStr {
    public String reverseStr(String str){
    char[] sol = str.toCharArray();
    Arrays.sort(sol);
    return new StringBuilder(new String(sol)).reverse().toString();
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
    }
}
```



string 객체에 .toCharArray() 함수를 통해 배열로 저장해서 StringBuilder 사용



#### etc

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

