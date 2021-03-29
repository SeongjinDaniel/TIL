# Lv1_폰켓몬



#### Question

[Lv1_폰켓몬](https://programmers.co.kr/learn/courses/30/lessons/1845)



#### Mine

```java
import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> hs = new HashSet<>();
        int max = nums.length / 2;
        for(int data : nums) {
            hs.add(data);
        }
        
        if(hs.size() > max) {
            answer = max;
        } else {
            answer = hs.size();
        }
        return answer;
    }
}
```

