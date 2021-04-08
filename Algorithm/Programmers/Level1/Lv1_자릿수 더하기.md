# Lv1_자릿수 더하기



#### Question

[Lv1_자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)



#### Mine

```java
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = String.valueOf(n);

        for(int i = 0; i < s.length(); i++) {
            int temp = s.charAt(i) - '0';
            answer += temp;
        }

        return answer;
    }
}
```



**Character.getNumericValue(input.charAt(i))**



#### Second Mine

```java
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = String.valueOf(n);
        for(int i = 0; i < s.length(); i++) {
            answer += Integer.parseInt(String.valueOf(s.charAt(i)));
        }
        
        return answer;
    }
}
```



#### Others

```java
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        while(true){
            answer+=n%10;
            if(n<10)
                break;

            n=n/10;
        }

        return answer;
    }
}
```



#### Others

```java
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        while (n != 0) {
            answer += n % 10;
            n /= 10;
        }

        return answer;
    }
}
```

