# Lv1_내적



**Question**

[Lv1_내적](https://programmers.co.kr/learn/courses/30/lessons/70128)



#### Mine

```java
class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for(int i = 0; i < a.length; i++) {
            answer += a[i] * b[i];
        }
        return answer;
    }
}
```

