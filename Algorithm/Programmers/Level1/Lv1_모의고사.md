# Lv1_모의고사

### 문제 [모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840#)



#### Solution

```java
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        // 1번 수포자 답안 반복
        int[] first = {1, 2, 3, 4, 5};
        // 2번 수포자 답안 반복
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        // 3번 수포자 답안 반복
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        // 정답 개수
        int firstCount = 0, secondCount = 0, thirdCount = 0;
        
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == first[i % first.length]) firstCount++;
            if(answers[i] == second[i % second.length]) secondCount++;
            if(answers[i] == third[i % third.length]) thirdCount++;
        }
        
        int max = Math.max(Math.max(firstCount, secondCount), thirdCount);
        List<Integer> list = new ArrayList<Integer>();
        if(max == firstCount) list.add(1);
        if(max == secondCount) list.add(2);
        if(max == thirdCount) list.add(3);
        
        answer = new int[list.size()];
        
        for(int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
```

