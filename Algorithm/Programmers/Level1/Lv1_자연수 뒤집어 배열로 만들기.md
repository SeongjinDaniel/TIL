# Lv1_자연수 뒤집어 배열로 만들기



####  Question

- [Lv1_자연수 뒤집어 배열로 만들기](https://programmers.co.kr/learn/courses/30/lessons/12932)



#### Mine

```java
class Solution { 
    public int[] solution(long n) {
        String str = "" + n; // 스트링 + int 할 경우 스트링으로 인식 
        int number = str.length(); 
        int[] answer = new int[number];
        for(int i = 0; i < number; i++) {
            answer[i] = (int)(n % 10);
            n/=10;
        } 
        return answer;
    } 
}
```



#### Others

```java
class Solution {
  public int[] solution(long n) {
      String s = String.valueOf(n);
      StringBuilder sb = new StringBuilder(s);
      sb = sb.reverse();
      String[] ss = sb.toString().split("");

      int[] answer = new int[ss.length];
      for (int i=0; i<ss.length; i++) {
          answer[i] = Integer.parseInt(ss[i]);
      }
      return answer;
  }
}
```

