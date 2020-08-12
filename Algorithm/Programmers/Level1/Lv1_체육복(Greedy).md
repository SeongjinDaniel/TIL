# Lv1_체육복

[문제 Lv1_체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)



#### Solution

```java
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        answer = n - lost.length;
        
        for(int i = 0; i < lost.length; i++) {
            for(int j = 0; j < reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    answer++;
                    lost[i] = -10;
                    reserve[j] = -20;
                    break;
                }
            }
        }
        for(int i = 0; i < lost.length; i++) {
            boolean rent = false;
            int out = 0;
            for(int j = 0; j < reserve.length; j++) {
                if(out == reserve.length) break;
                if(reserve[j] - lost[i] == -1 || reserve[j] - lost[i] == 1 || reserve[j] == lost[i]) {
                    reserve[j] = -1;
                    answer++;
                    rent = true;
                    break;
                }
            }
            
        }
        return answer;
    }
}
```

