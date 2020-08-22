# Lv1_가운데 글자 가져오기



#### Question

- [Lv1_가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)



#### Solution

```java
class Solution {
    public String solution(String s) {
        String answer = "";
        
        answer = s.substring((s.length() - 1) / 2, s.length() / 2 + 1);
        
        return answer;
    }
}
```

