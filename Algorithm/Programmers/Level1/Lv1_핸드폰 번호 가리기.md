# Lv1_핸드폰 번호 가리기



#### Question

- Lv1_핸드폰 번호 가리기



#### Mine

```java
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int len = phone_number.length();
        char[] partials = new char[len];
        
        for(int i = 0; i < len; i++) {
            if(len - 4 <= i && len - 1 >= i) {
                partials[i] = phone_number.charAt(i);
            } else {
                partials[i] = '*';
            }
        }
        
        for(int i = 0; i < len; i++) {
            answer += partials[i];
        }
                
        return answer;
    }
}
```



#### Others

```java
class Solution {
  public String solution(String phone_number) {
     char[] ch = phone_number.toCharArray();
     for(int i = 0; i < ch.length - 4; i ++){
         ch[i] = '*';
     }
     return String.valueOf(ch);
  }
}
```

String.toCharArray();

String.valueOf(ch); -> 다시 String으로 변경해서 return.



#### Others

```java
class Solution {
  public String solution(String phone_number) {
    return phone_number.replaceAll(".(?=.{4})", "*");
  }
}
```

