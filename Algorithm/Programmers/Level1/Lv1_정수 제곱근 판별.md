# Lv1_정수 제곱근 판별



#### Question

- [Lv1_정수 제곱근 판별](https://programmers.co.kr/learn/courses/30/lessons/12934)

#### Mine

```java
class Solution {
    public long solution(long n) {
        long answer = 0;
        if(Math.sqrt(n) - (int)Math.sqrt(n) == 0) {
            double sqrts = Math.sqrt(n);
            answer = (long)((sqrts + 1) * (sqrts + 1));
        } else {
            answer = -1;
        }
        
        return answer;
    }
}
```



#### Others

```java
class Solution {
  public long solution(long n) {
      if (Math.pow((int)Math.sqrt(n), 2) == n) {
            return (long) Math.pow(Math.sqrt(n) + 1, 2);
        }

        return -1;
  }
}
```

