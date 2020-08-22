# Lv1_다른 사람의 풀이



#### 문제

- [Lv1_다른 사람의 풀이](https://programmers.co.kr/learn/courses/30/lessons/12916)



#### Solution

```java
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCnt = 0;
        int yCnt = 0;
        
        for(int i = 0 ; i < s.length(); i++) {
            if(s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                pCnt++;
            } else if(s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
                yCnt++;
            }
        }
        
        if(pCnt != yCnt) answer = false;

        return answer;
    }
}
```



#### Other Solution

```java
class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();

        return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
    }
}
```



람다 and s.toUpperCase() 사용!!