# Lv1_같은 숫자는 싫어



#### Question

- [Lv1_같은 숫자는 싫어](https://programmers.co.kr/learn/courses/30/lessons/12906)



#### Mine

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



#### Second Mine

```java
import java.util.*;

// 앞의 index 배열과 같으면 list에 추가 하지 않고 같지 않으면 추가한다.
public class Solution {
    public Integer[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int oldNumber = arr[0];
        list.add(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if(oldNumber != arr[i]) {
                list.add(arr[i]);
                oldNumber = arr[i];
            }
        }
        Integer[] answer = list.toArray(new Integer[0]);
        return answer;
    }
}
```



#### Third Mine

```java
import java.util.*;

public class Solution {
    public Integer[] solution(int []arr) {
        LinkedList<Integer> list = new LinkedList<>();
        int len = arr.length;
        
        list.add(arr[0]);
        for(int i = 1; i < len; i++) {
            if(list.getLast() != arr[i]) {
                list.add(arr[i]);
            }
        }
        Integer[] answer = list.toArray(new Integer[0]);
        return answer;
    }
}
```





```java
import java.util.*;

// 앞의 index 배열과 같으면 list에 추가 하지 않고 같지 않으면 추가한다.
public class Solution {
    public Integer[] solution(int []arr) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if(list.getLast() != arr[i]) {
                list.add(arr[i]);
            }
        }
        Integer[] answer = list.toArray(new Integer[0]);
        return answer;
    }
}
```

