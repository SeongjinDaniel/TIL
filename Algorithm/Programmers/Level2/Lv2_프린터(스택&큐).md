# Lv2_프린터



#### Question

- Lv2_프린터(스택/큐)



#### Mine

```java
import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        PriorityQueue priority = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int prior : priorities) {
            priority.add(prior);
        }
        
        while(!priority.isEmpty()) {
            for(int i = 0; i < priorities.length; i++) {
                if(priorities[i] == (int)priority.peek()) {
                    if(i == location) {
                        return answer;
                    }
                    answer++;
                    priority.poll();
                }
            }
        }
        
        return answer;
    }
}
```



#### Others

```java
import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int l = location;

        Queue<Integer> que = new LinkedList<Integer>();
        for(int i : priorities){
            que.add(i);
        }

        Arrays.sort(priorities);
        int size = priorities.length-1;

        while(!que.isEmpty()){
            Integer i = que.poll();
            if(i == priorities[size - answer]){
                answer++;
                l--;
                if(l < 0)
                    break;
            }else{
                que.add(i);
                l--;
                if(l < 0)
                    l = que.size()-1;
            }
        }

        return answer;
    }
}
```

