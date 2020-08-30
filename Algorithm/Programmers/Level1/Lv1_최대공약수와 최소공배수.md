# Lv1_최대공약수와 최소공배수



#### Question

- [Lv1_최대공약수와 최소공배수](https://programmers.co.kr/learn/courses/30/lessons/12940)



#### Mine

```java
class Solution {
    private int gcd(int a, int b) {

        if(b == 0) return a;
        else return gcd(b, a % b);
    }
    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        int gcdNum = gcd(n, m);
        answer[0] = gcdNum;
        answer[1] = n * m / gcdNum;
        System.out.println(answer[0]);
        System.out.println(answer[1]);
        return answer;
    }
}
```



#### Others

```java
import java.util.Arrays;

class TryHelloWorld {
    public int[] gcdlcm(int a, int b) {
        int[] answer = new int[2];
      int temp=1;
      int gcd=a*b;
      while(temp!=0){
      	temp=b%a;
        b=a;
        a=temp;
      }
      answer[0]=b;
      answer[1]=gcd/b;
        return answer;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        TryHelloWorld c = new TryHelloWorld();
        System.out.println(Arrays.toString(c.gcdlcm(3, 12)));
    }
}
```

