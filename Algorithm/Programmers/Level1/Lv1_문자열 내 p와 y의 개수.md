# Lv1_문자열 내 p와 y의 개수



#### Question

- [Lv1_문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916)



#### Mine

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



#### Second Mine

```java
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCount = 0, yCount = 0;
        s = s.toLowerCase();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p') pCount++;
            if (s.charAt(i) == 'y') yCount++;
        }
        if (pCount != yCount) {
           answer = false; 
        }
        return answer;
    }
}
```



#### etc

```java
class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();

        return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
    }
}
```



람다 and s.toUpperCase() 사용!!