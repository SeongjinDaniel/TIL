# Lv1_체육복

#### Question

- [Lv1_체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)



#### Mine

```java
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        answer = n - lost.length;
        
        for(int i = 0; i < lost.length; i++) {
            for(int j = 0; j < reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    answer++;
                    lost[i] = -10;
                    reserve[j] = -20;
                    break;
                }
            }
        }
        for(int i = 0; i < lost.length; i++) {
            boolean rent = false;
            int out = 0;
            for(int j = 0; j < reserve.length; j++) {
                if(out == reserve.length) break;
                if(reserve[j] - lost[i] == -1 || reserve[j] - lost[i] == 1 || reserve[j] == lost[i]) {
                    reserve[j] = -1;
                    answer++;
                    rent = true;
                    break;
                }
            }
            
        }
        return answer;
    }
}
```



#### Second Mine

```java
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        // 배열에 순서대로 체육복의 개수를 정리.
        int[] clothesCnt = new int[n];
        for(int i =0 ; i < n; i++) {
            clothesCnt[i] = 1;
        }
        for(int i = 0; i < lost.length; i++) {
            clothesCnt[lost[i] - 1]--;
        }
        for (int i = 0; i < reserve.length; i++) {
            clothesCnt[reserve[i] - 1]++;
        }
        // 1 ~ n까지 확인하면서
        // 만약 체육복을 확인하는 번호에 체육복이 
        // 0개 이면 앞뒤에 체육복이 2개 이상인지 확인하여
        // 체육복을 빌려준다.
        for (int i = 0; i < n; i++) {
            if(clothesCnt[i] == 0) {
                if(i >= 1 && i <= n - 2) {
                    if(clothesCnt[i - 1] == 2) {
                        clothesCnt[i]++;
                        clothesCnt[i - 1]--;
                    }
                    if(clothesCnt[i + 1] == 2) {
                        clothesCnt[i]++;
                        clothesCnt[i + 1]--;
                    }
                } else if(i == 0){
                    if(clothesCnt[i + 1] == 2) {
                        clothesCnt[i]++;
                        clothesCnt[i + 1]--;
                    }
                } else if(i == n - 1) {
                    if(clothesCnt[i - 1] == 2) {
                        clothesCnt[i]++;
                        clothesCnt[i - 1]--;
                    }
                }
            }
        }
        
        for(int data : clothesCnt) {
            if(data >= 1) {
                answer++;
            }
        }
        // (1, 1), (2, 0), (3, 1), (4, 2), (5, 1)
        return answer;
    }
}
```



- forEach문을 잘 활용해야 겠다. 코드를 읽기에는 forEach문이 더 가독성이 좋은것 같다.



#### Others

```java
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] people = new int[n];
        int answer = n;

        for (int l : lost) 
            people[l-1]--;
        for (int r : reserve) 
            people[r-1]++;

        for (int i = 0; i < people.length; i++) {
            if(people[i] == -1) {
                if(i-1>=0 && people[i-1] == 1) {
                    people[i]++;
                    people[i-1]--;
                }else if(i+1< people.length && people[i+1] == 1) {
                    people[i]++;
                    people[i+1]--;
                }else 
                    answer--;
            }
        }
        return answer;
    }
}
```

- 배열 크기를 n+2로 선언하면 추가 조건 비교를 하지 않아도 된다.