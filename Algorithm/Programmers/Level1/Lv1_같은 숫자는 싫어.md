# Lv1_같은 숫자는 싫어



#### 문제

- [Lv1_같은 숫자는 싫어](https://programmers.co.kr/learn/courses/30/lessons/12906)



#### Solution

```java
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        int idx = 0;
        int oldNum = 0;
        List<Integer> list = new ArrayList<Integer>();
        
        oldNum = 10;
        for(int i = 0; i < arr.length; i++) {
            if(oldNum != arr[i]) {
                list.add(arr[i]);
                oldNum = arr[i];
            }
        }
        int size = list.size();
        answer = new int[size];
        for(int i = 0; i < size; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
```

