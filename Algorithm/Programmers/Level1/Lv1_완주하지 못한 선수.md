# 완주하지 못한 선수

#### Question

- [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576)

해시로 풀라고 되어있던 문제 !! O(n2)이라서 성능 테스트 실패

해시로 풀면 O(n)으로 해결할 수 있음.

#### O(n2)

```
class Solution {

    public String On2(String[] participant, String[] completion) {
        String answer = "";
        boolean flag = true;
        for(String data : participant) {
            flag = true;
            for(int i = 0; i < completion.length; i++) {
                if(completion[i] != null) {
                    if(data.equals(completion[i])) {
                        completion[i] = null;
                        flag = false;
                        break;
                    }
                }
            }
            if(flag) {
                answer += data;
            }
        }
        return answer;
    }
        
    public String solution(String[] participant, String[] completion) {
        return On2(participant, completion);
    }
}
```

#### 해시_O(n)

```java
import java.util.*; 
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = ""; 
        int val =0;Map <string, Integer> hm = new HashMap<>();
        for(String part : participant) { 
            if(hm.get(part) == null)
                hm.put(part,1); 
            else{val = hm.get(part) + 1;
                 hm.put(part,val);
                }
        } 
        for(String comp : completion) {
            val = hm.get(comp) - 1
                ;hm.put(comp,val);
        } 
        for(String key : hm.keySet()) {
            if(hm.get(key) == 1) 
                answer = key;
        } return answer;
    }                           
}
```

#### 정렬 방법!!!

- participant 길이와 completion 길이의 차이는 1차이가 나니까 비교만 하면 간단하게 해결가능!!

```java
import java.util.*; class Solution { 
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i; 
        for ( i=0; i < completion.length; i++){ 
            if (!participant[i].equals(completion[i])){ 
                return participant[i];
            }
        } 
        return participant[i];
    } 
} 
```

