# Lv2_주식가격(스택&큐)



#### Question

- [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584?language=java)



#### Mine

```java
import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        final int priceLen = prices.length;
        int[] answer = new int[priceLen];
        boolean[] check = new boolean[priceLen];
        Arrays.fill(check, false);
        
        for(int i = 0; i < priceLen - 1; i++) {
            for(int j = i + 1; j < priceLen; j++) {
                if(!check[i] && prices[i] > prices[j]) {
                    check[i] = true;
                    answer[i]++;
                    break;
                } else {
                    answer[i]++;
                }
            }
        }
        answer[priceLen - 1] = 0;
        
        return answer;
    }
}
```



#### Others

```java
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for(int i = 0; i < prices.length; i++)
        {
            for(int j=i+1; j < prices.length; j++)
            {
                if(prices[i] > prices[j])
                {
                    answer[i] = j-i;
                    break;
                }
                else
                    answer[i] = j-i;
            }
        }

        //System.out.println(Arrays.toString(answer));

        return answer;
    }
}
```



#### Others

```java
import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        Stack<Integer> beginIdxs = new Stack<>();
        int i=0;
        int[] terms = new int[prices.length];

        beginIdxs.push(i);
        for (i=1; i<prices.length; i++) {
            while (!beginIdxs.empty() && prices[i] < prices[beginIdxs.peek()]) {
                int beginIdx = beginIdxs.pop();
                terms[beginIdx] = i - beginIdx;
            }
            beginIdxs.push(i);
        }
        while (!beginIdxs.empty()) {
            int beginIdx = beginIdxs.pop();
            terms[beginIdx] = i - beginIdx - 1;
        }

        return terms;
    }
}
```

