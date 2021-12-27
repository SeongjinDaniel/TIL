# Lv2_전화번호 목록



[전화번호 목록(Hash 문제)](https://programmers.co.kr/learn/courses/30/lessons/42577?language=java)



아래 코드는 Hash를 무시하고 풀었을 때 정답을 나오나 효율성 테스트 FAIL

```java
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        for (String number : phone_book) {
            for (String number2 : phone_book) {
                if (number == number2)
                    continue;
                // 접두어만이 같아야한다.(number: 접두어)
                if (number.length() <= number2.length()) {
                    char[] chars = number.toCharArray();
                    int idx = 0;
                    int count = 0;
                    for (char cha : chars) {
                        if (cha == number2.charAt(idx++)) {
                            count++;
                        }
                    }
                    if (number.length() == count) {
                        answer = false;
                        break;
                    }
                }
            }
            if (!answer)
                break;
        }
        return answer;
    }
}
```



아래 방법도 시간초과

```java
import java.util.*;
class Solution {
    public boolean solution(String[] phoneBook) {
            for(int i=0; i<phoneBook.length-1; i++) {
            for(int j=i+1; j<phoneBook.length; j++) {
                if(phoneBook[i].startsWith(phoneBook[j])) {return false;}
                if(phoneBook[j].startsWith(phoneBook[i])) {return false;}
            }
        }
        return true;
    }
}
```



아래 방법으로 해결!!

```java
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, String> map = new HashMap<>();
        for(String temp : phone_book){
            map.put(temp, temp);
        }
        for(String str : phone_book){
            for(int index = 0; index < str.length(); index++){
                String temp = str.substring(0, index);                
                if( map.containsKey( temp ) ){
                    return false;
                }
            }
        }
        return true;
    }
}
```



