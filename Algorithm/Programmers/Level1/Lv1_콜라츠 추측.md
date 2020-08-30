# Lv1_콜라츠 추측



#### Question

- [Lv1_콜라츠 추측](https://programmers.co.kr/learn/courses/30/lessons/12943)



#### Mine

```java
class Solution {
    public int solution(long num) {
        int answer = 0;
        int cnt = 0;
        
        if(num == 1) return answer;
        else {
            while(num != 1) {
                if(num % 2 == 0) {
                    num /= 2;
                } else {
                    num = (num * 3) + 1;
                }
                cnt++;
                if(cnt == 500) {
                    cnt = -1;
                    break;
                }
            }
            answer = cnt;
        }
        
        return answer;
    }
}
```



#### Others

```java
class Collatz {
    public int collatz(int num) {
    long n = (long)num;
    for(int i =0; i<500; i++){      
      if(n==1) return i;
      n = (n%2==0) ? n/2 : n*3+1;            
    }
    return -1;
  }
    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        Collatz c = new Collatz();
        int ex = 6;
        System.out.println(c.collatz(ex));
    }
}
```

