# Lv2_기능개발(스택&큐)



#### Question

- [Lv2_기능개발(스택&큐)](https://programmers.co.kr/learn/courses/30/lessons/42586)



#### Mine

```java
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        int pgrLen = progresses.length;
        int[] result = new int[pgrLen];
        int count = 0;
        int idx = 0;
        boolean flag = false;
        int firstIdx = 0;
        int[] answer;
        
        for(int data : progresses) {
            q.add(data);
        }
        
        while(!q.isEmpty()) {
            
            for(int i = firstIdx; i < pgrLen; i++) {
                progresses[i] += speeds[i];
                if(progresses[firstIdx] >= 100) {
                    firstIdx++;
                    count++;
                    q.poll();
                    flag = true;
                }
            }
            if(flag) {
                result[idx++] = count;
                count = 0;
                flag = false;
            }   
        }
        
        answer = new int[idx];

        for(int i = 0; i < idx; i++) {
            if(result[i] == 0) break;
            answer[i] = result[i];
        }
        
        return answer;
    }
}
```



#### Mine2

```java
import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int firstIdx = 0;
        boolean flag = false;
        int count = 0;
        List<Integer> result = new ArrayList<>();
        
        // 1. PriorityQueue progresses 저장
        // 2. while(!PriorityQueue.isEmpty()) 나 제거 될 때 까지 speeds 더하기 
        // 3. 만약 순서대로 idx를 확인할 때 100 이상이면 poll하면서 count++해서 result에 저장하기
        PriorityQueue<Integer> prior = new PriorityQueue<>();
        for (int progress : progresses) {
            prior.add(progress);
        }
        
        while(!prior.isEmpty()) {
            for(int i = 0; i < progresses.length; i++) {
                progresses[i] += speeds[i];
                if (progresses[firstIdx] >= 100) {
                    firstIdx++;
                    prior.poll();
                    count++;
                    flag = true;
                }
            }
            if (flag) {
                result.add(count);
                flag = false;
                count = 0;
            }
        }
        
        // list to array
        answer = result.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}
```





#### Others

```java
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] dayOfend = new int[100];
        int day = -1;
        for(int i=0; i<progresses.length; i++) {
            while(progresses[i] + (day*speeds[i]) < 100) {
                day++;
            }
            dayOfend[day]++;
        }
        return Arrays.stream(dayOfend).filter(i -> i!=0).toArray();
    }
}
```

