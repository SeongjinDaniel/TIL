# Lv1_문자열을 정수로 바꾸기



#### Question

- [Lv1_문자열을 정수로 바꾸기](https://programmers.co.kr/learn/courses/30/lessons/12925)



#### Mine

```java
class Solution {
    public int solution(String s) {
        int answer = 0;

        if(s.charAt(0) == '-') {
            answer += -Integer.pacrseInt(s.substring(1));
        }else answer = Integer.parseInt(s);
        
        return answer;
    }
}
```



#### Second Mine

```java
class Solution {
    public int solution(String s) {
        int answer = Integer.parseInt(s);
        return answer;
    }
}
```



#### Others

```java
public class StrToInt {
    public int getStrToInt(String str) {
            boolean Sign = true;
            int result = 0;

      for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                if (ch == '-')
                    Sign = false;
                else if(ch !='+')
                    result = result * 10 + (ch - '0');
            }
            return Sign?1:-1 * result;
    }
    //아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String args[]) {
        StrToInt strToInt = new StrToInt();
        System.out.println(strToInt.getStrToInt("-1234"));
    }
}
```

