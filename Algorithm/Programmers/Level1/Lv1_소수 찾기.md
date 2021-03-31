# Lv1_소수 찾기



#### Question

- [Lv1_소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/12921)



#### 시간초과!!

```java
class Solution {
    public int solution(int n) {
        int answer = 1; // 2는 포함
        int cnt = 0;
        for(int i = 3; i <= n; i++) {
            cnt = 0;
            for(int j = 2; j < i; j++) {
                if(i % j == 0) {
                    cnt++;
                    break;
                }
                
                if (j == i - 1) {
                    if (cnt == 0) answer++;
                }
            }
        }
        
        return answer;
    }
}
```



#### Mine

```java
class Solution {
    public int solution(int n) {
        //final int MAX = 1000000;
        int answer = 0;
        int[] arr = new int[n+1];
        
        for(int i = 0; i <= n; i++) {
            arr[i] = 1;
        }
        
        arr[0] = arr[1] = 0; // 0, 1은 소수가 아님으로 제거
        for(int i = 2; i <= n; i++) {
            for(int j = i + i; j <= n; j += i) {
                if(arr[j] != 0) {
                    arr[j] = 0;
                }
            }
        }
        
        for(int i = 0; i <= n; i++) {
            if(arr[i] != 0) {
                answer++;
            }
        }
        
        return answer;
    }
}
```



```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n + 1];
        arr[0] = 0;
        arr[1] = 0;
        for(int i = 2; i <= n; i++) {
            arr[i] = i;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = i + i; j <= n; j = j + i) {
                arr[j] = 0;
            }
        }
        for(int i = 2; i <= n; i++) {
            if(arr[i] != 0) answer++;
        }
        return answer;
    }
}
```



에라토스테네스의 체 이용!