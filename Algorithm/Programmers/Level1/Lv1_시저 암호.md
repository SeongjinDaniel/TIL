# Lv1_시저 암호



#### Question

- 시저 암호



#### Mine

```java
class Solution {
    public String solution(String s, int n) {
        String answer = "";
        int len = s.length();
        String temp = "";
        
        System.out.println(n);
        for(int i = 0; i < n; i++) {
            temp = "";
            for(int j = 0; j < len; j++) {
                char one = s.charAt(j);
                
                if(one == 'z') temp += 'a';
                else if (one == 'Z') temp += 'A';
                else if (one == ' ') temp += ' ';
                else temp += (char)(one + 1);
            }
            s = temp;
        }
        
        answer = s;
        
        return answer;
    }
}
```

--> for 문 n번을 빼고 문자에 + n을 해주면 더 좋은 코드가 될수 있음.

#### Others

```java
class Caesar {
    String caesar(String s, int n) {
        String result = "";
    n = n % 26;
    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      if (Character.isLowerCase(ch)) {
        ch = (char) ((ch - 'a' + n) % 26 + 'a');
      } else if (Character.isUpperCase(ch)) {
        ch = (char) ((ch - 'A' + n) % 26 + 'A');
      }
      result += ch;
    }
        return result;
    }

    public static void main(String[] args) {
        Caesar c = new Caesar();
        System.out.println("s는 'a B z', n은 4인 경우: " + c.caesar("a B z", 4));
    }
}
```

