# Lv1_이상한 문자 만들기



#### Question

- [Lv1_이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)



#### Mine

```java
class Solution {
    public String solution(String s) {
        String answer = "";
        int len = s.length();
        int idx = 0;
        for(int i = 0; i < len; i++) {
            char temp = s.charAt(i);
            if(temp == ' ') {
                idx = 0;
                answer += ' ';
                continue;
            }
            if(idx++ % 2 == 0) {
                answer += Character.toUpperCase(temp);
            }else answer += Character.toLowerCase(temp);
        }
        
        return answer;
    }
}
```



#### Others

```java
	class Solution {
  public String solution(String s) {

        String answer = "";
        int cnt = 0;
        String[] array = s.split("");

        for(String ss : array) {
            cnt = ss.contains(" ") ? 0 : cnt + 1;
            answer += cnt%2 == 0 ? ss.toLowerCase() : ss.toUpperCase(); 
        }
      return answer;
  }
}
```

- contains : 자바 스트링 contains () 메소드는 스트링에서 특성의 순서를 검색합니다. 만약 char 값의 시퀀스가 찾아진다면 True를, 반대라면 False를 반환합니다.



#### Others

```java
class Solution {
  public String solution(String s) {
        char[] chars = s.toCharArray();
        int idx = 0;

        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ')
                idx = 0;
            else
                chars[i] = (idx++ % 2 == 0 ? Character.toUpperCase(chars[i]) : Character.toLowerCase(chars[i]));
        }

        return String.valueOf(chars);
  }
}
```

- String.valueOf(chars) -> char변수를 String으로 변환, 만약 int값이면 String으로 변경.
- toCharArray()