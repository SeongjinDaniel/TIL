# Lv1_나누어 떨어지는 숫자 배열



#### Question

- [Lv1_나누어 떨어지는 숫자 배열](https://programmers.co.kr/learn/courses/30/lessons/12910)



#### Mine

```java
import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        List<Integer> list = new ArrayList<Integer>();
        
        for(int i = 0, size = arr.length; i < size; i++) {
            if(arr[i] % divisor == 0) {
                list.add(arr[i]);
            }
        }
        int size = list.size();
        if(size == 0) {
            answer = new int[1];
            answer[0] = -1;
        } else {
            answer = new int[size];
            for(int i = 0; i < size; i++) {
                answer[i] = list.get(i);
            }
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}
```



#### Second Mine

```java
// arr의 모든 수를 divisor로 나누어 보면서
// divisor로 나누어 떨어지는 수가 있다면 list에 담기
// list.size()가 0이라면 answer = -1
import java.util.*;
class Solution {
    public Integer[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        for (int data : arr) {
            if(data % divisor == 0) {
                list.add(data);
            }
        }
        
        Collections.sort(list);
        
        if(list.size() == 0) {
            Integer[] answer = {-1};
            return answer;
        } else {
            Integer[] answer = list.toArray(new Integer[0]);
            return answer;
        }
    }
}
```



#### Others

```java
public int[] divisible(int[] array, int divisor) {
    //ret에 array에 포함된 정수중, divisor로 나누어 떨어지는 숫자를 순서대로 넣으세요.
    return Arrays.stream(array).filter(factor -> factor % divisor == 0).toArray();
}
```





