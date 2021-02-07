# 두 개 뽑아서 더하기



#### Solution

```
import java.util.*;

class Solution {
    public Integer[] solution(int[] numbers) {
        int len = numbers.length;
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                if(i == j) continue;
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        
        Integer[] answer = list.toArray(new Integer[list.size()]);
                
        return answer;
    }
}
```



#### 문제

- https://programmers.co.kr/learn/courses/30/lessons/68644?language=java