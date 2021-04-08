# Lv1_정수 내림차순으로 배치하기



#### Question

```java
import java.util.*;
class Solution {
    public long solution(long n) {
        int len = Long.toString(n).split("").length;
        String[] array = new String[len];
        array = Long.toString(n).split("");
        Arrays.sort(array);
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < len; i++) {
            sb.append(array[i]);
        }
        sb = sb.reverse();
        String[] ss = sb.toString().split("");
        long answer = 0;
        
        answer = Long.valueOf(sb.toString().trim());

        return answer;
    }
}
```



#### Second Mine

```java
import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String s = String.valueOf(n);
        List<String> list = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            list.add(Character.toString(s.charAt(i)));
        }
        Collections.sort(list, Collections.reverseOrder());
        String ss = "";
        for(int i = 0; i < list.size(); i++) {
            ss += list.get(i);
        }
        answer = Long.parseLong(ss);
        return answer;
    }
}
```



#### Others

```java
import java.util.Arrays;

public class ReverseInt {
    public int reverseInt(int n){

        String str = Integer.toString(n);
        char[] c = str.toCharArray();
        Arrays.sort(c);
        StringBuilder sb = new StringBuilder(new String(c,0,c.length));  
        return Integer.parseInt(((sb.reverse()).toString()));
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        ReverseInt ri = new ReverseInt();
        System.out.println(ri.reverseInt(118372));
    }
}
```



```java
// 배열의 offset 인덱스 위치부터 length만큼 String 객체로 생성
// String str2 = new String(byte[] bytes, int offset, int length);
String str2 = new String(bytes, 6, 4);
System.out.println(str2);
```

```JAVA
// 배열 전체를 String 객체로 생성
// String str = new String(byte[] bytes);
byte[] bytes = { 72, 101, 108, 108, 111, 32, 74, 97, 118, 97 };
String str = new String(bytes);
System.out.println(str);
```



#### Others

```java
public class ReverseInt {
    String res = "";
    public int reverseInt(int n){
        res = "";
        Integer.toString(n).chars().sorted().forEach(c -> res = Character.valueOf((char)c) + res);
        return Integer.parseInt(res);
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        ReverseInt ri = new ReverseInt();
        System.out.println(ri.reverseInt(118372));
    }
}
```

안 동작 하지만 이렇게도 가능하다는것을 알아두자