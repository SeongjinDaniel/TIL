# Lv1_다른 사람의 풀이



#### Question

- [Lv1_다른 사람의 풀이](https://programmers.co.kr/learn/courses/30/lessons/12918)



#### Mine

```java
class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        char temp;
        
        if(s.length() != 4 && s.length() != 6) {
            return false;
        }
        for(int i = 0; i < s.length(); i ++) {
            temp = s.charAt(i);
            if(!(temp >= '0' && temp <= '9')) {
                answer = false;
                break;
            }
        }
        
        return answer;
    }
}
```



#### others

```java
import java.util.*;
 
class Solution {
  public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6) return s.matches("(^[0-9]*$)");
        return false;
  }
}
```



#### others

```java
class Solution {
  public boolean solution(String s) {
    return (s.length() != 4 && s.length() != 6) || (s.split("[0-9]").length > 0) ? false:true;
  }
}
```



#### others

```java
class Solution {
  public boolean solution(String s) {
      boolean answer = false;
      if(s.length() == 4 || s.length() == 6 ){
        int i;       
        for(i=0;i<s.length();i++){
           if(!Character.isDigit(s.charAt(i))){
               break;
           }
         }
        if(i==s.length()){
            answer =true;
        }
      }
      return answer;
  }
}

```



#### 참고

- [정규표현식](https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D)