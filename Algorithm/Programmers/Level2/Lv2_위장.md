# Lv2_위장



#### Question

- [위장](https://programmers.co.kr/learn/courses/30/lessons/42578)



#### Mine

```java
import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        // 종류 : 개수
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0) + 1);
        }
        // 경우의 수 = (옷 가지 수 + 안 입을 경우)
        for (int count : map.values()) {
            answer *= (count + 1);
        }
        return answer - 1;
    }
}
```

