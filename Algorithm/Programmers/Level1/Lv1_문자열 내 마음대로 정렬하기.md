# Lv1_문자열 내 마음대로 정렬하기 



#### 문제

- [Lv1_문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)



#### Solution

```java
import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        
        for(int i = 0; i < strings.length; i++) {
            strings[i] = strings[i].charAt(n) + strings[i];
        }
        
        Arrays.sort(strings);
        answer = new String[strings.length];
        for(int i = 0; i < strings.length; i++) {
            answer[i] = strings[i].substring(1);
        }

        return answer;
    }
}
```

