# Lv1 두 정수 사이의 합



#### Question

- [Lv1 두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)



#### Mine

```java
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int min = 0;
        int max = 0;
        
        if(a > b) {
            min = b;
            max = a;
        }
        else {
            min = a;
            max = b;
        }
        
        if(min == max) {
            answer = min;
        } else {
            for(int i = min; i <= max; i++) {
                answer += i;
            }
        }
            
        return answer;
    }
}
```



#### etc

```java
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int min = 0;
        int max = 0;
        
        if(a > b) {
            min = b;
            max = a;
        }
        else {
            min = a;
            max = b;
        }
        
        for(int i = min; i <= max; i++) {
            answer += i;
        }
            
        return answer;
    }
}
```



#### etc

```java
class Solution {

    public long solution(int a, int b) {
        return sumAtoB(Math.min(a, b), Math.max(b, a));
    }

    private long sumAtoB(long a, long b) {
        return (b - a + 1) * (a + b) / 2; //등차 수열의 합 공식
    }
}
```

