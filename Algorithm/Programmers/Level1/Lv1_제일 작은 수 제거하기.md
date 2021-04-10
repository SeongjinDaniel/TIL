# Lv1_제일 작은 수 제거하기



#### Question

- [Lv1_제일 작은 수 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12935)



#### Mine

```java
class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int len = arr.length;
        
        if(len <= 1) {
            answer = new int[1];
            answer[0] = -1;
        } else {
            int min = 987987987;
            for(int i = 0; i < len; i++) {
                if(min > arr[i]) {
                    min = arr[i];
                }
            }
            
            answer = new int[len - 1];
            int idx = 0;
            for(int i = 0; i < len; i++) {
                if(min == arr[i]) continue;
                else {
                    answer[idx++] = arr[i];
                }
            }
        }
        
        return answer;
    }
}
```



#### Second Mine

```java
import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int len = arr.length;
        if(len <= 1) return new int[]{-1};
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            list.add(arr[i]);
        }
        Collections.sort(list, Comparator.reverseOrder());
        int temp = list.remove(len - 1);
        int[] answer = new int[len - 1];
        int idx = 0;
        for (int i = 0; i < len; i++) {
            if(arr[i] == temp) continue;
            answer[idx++] = arr[i];
        }
        return answer;
    }
}
```





#### Others

```java
import java.util.Arrays;
import java.util.stream.Stream;
import java.util.List;
import java.util.ArrayList;

class Solution {
  public int[] solution(int[] arr) {
      if (arr.length <= 1) return new int[]{ -1 };
      int min = Arrays.stream(arr).min().getAsInt();
      return Arrays.stream(arr).filter(i -> i != min).toArray();
  }
}
```

