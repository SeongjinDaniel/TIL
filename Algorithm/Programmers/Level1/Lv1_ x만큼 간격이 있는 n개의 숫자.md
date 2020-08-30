# Lv1_ x만큼 간격이 있는 n개의 숫자



#### Question

- [Lv1_ x만큼 간격이 있는 n개의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12954)



#### Mine

```java
class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        long sum = 0;
        for(int i = 0; i < n; i++) {
            sum += x;
            answer[i] = sum;
        }
        
        return answer;
    }
}
```



#### Others

```java
import java.util.*;
class Solution {
    public static long[] solution(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;

        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] + x;
        }

        return answer;

    }
}
```



#### Others

```java
class Solution {
  public long[] solution(long x, int n) {
      long[] answer = new long[n];
      for(int i = 0; i < n; i++){
          answer[i] = x * (i + 1);
      }
      return answer;
  }
}
```

