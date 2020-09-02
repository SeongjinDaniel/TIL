# Lv1_Summer/Winter Coding(~2018)



#### Question

- [Lv1_Summer/Winter Coding(~2018)](Lv1_Summber/Winter Coding(~2018))



#### Mine

```java
import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        
        for(int i = 0; i < d.length; i++) {
            if(budget >= d[i]) {
                budget -= d[i];
                answer++;
            }
        }

        return answer;
    }
}
```

작은것부터 비교해서  최대한 많은 부서의 물품을 구매해 줄 수 있도록 알고리즘을 구성.

#### Others

```java
import java.util.*;

class Solution {
  public int solution(int[] d, int budget) {
      int answer = 0;

        Arrays.sort(d);

        for (int i = 0; i < d.length; i++) {
            budget -= d[i];

            if (budget < 0) break;

            answer++;
        }

        return answer;
  }
}
```



#### Others

```java
import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int[] dept = Arrays.copyOf(d, d.length);
        Arrays.sort(dept);
        int sum = 0;
        for (int inx=0; inx<dept.length; inx++) {
            sum += dept[inx];
            if (sum<=budget) {
                answer++;
            }
        }
        return answer;
    }
}
```

