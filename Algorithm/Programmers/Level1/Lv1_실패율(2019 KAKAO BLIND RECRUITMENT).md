# Lv1_실패율(2019 KAKAO BLIND RECRUITMENT)



#### Question

- [Lv1_실패율(2019 KAKAO BLIND RECRUITMENT)](https://programmers.co.kr/learn/courses/30/lessons/42889#)



#### Mine

```java
import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int stageLen = stages.length;
        int[] answer = new int[N];
        int[] cnt = new int[N + 2]; // stage는 1번부터니까 1~N+1으로 인덱스를 사용
        double[] score = new double[N + 2]; // 1~N+1
        List<Integer> flagList = new ArrayList<Integer>();
        
        Arrays.sort(stages);
        for(int i = 0; i < stageLen; i++) {
            cnt[stages[i]]++;
        }
        
        int div = stageLen;
        for(int i = 1; i <= N; i++) {
            //System.out.println("cnt: "+cnt[i]);
            //System.out.println("div: "+div);
            if(div == 0) continue;
            score[i] = (double)cnt[i] / (double)div;
            div = div - cnt[i];
            //System.out.println(score[i]);
        }
        
        boolean[] flag = new boolean[N+2];
        Arrays.fill(flag, false);
        double max = -987987987;
        int idx = 0;
        for(int i = 1; i <= N; i++) {
            max = -987987987;
            for(int j = 1; j <= N; j++) {
                if(flag[j] == false) {
                    flag[j] = true;
                    if(max < score[j]) {
                        max = score[j];
                        idx = j;
                    }
                }
            }

            answer[i - 1] = idx;
            flagList.add(idx);
            Arrays.fill(flag, false);
            for(int j = 0; j < flagList.size(); j++) {
                flag[flagList.get(j)] = true;
            }
        }
        
        
        return answer;
    }
}
```

- 회고 : HashMap을 사용해보자!!



#### Others

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int N, int[] lastStages) {
        int nPlayers = lastStages.length;
        int[] nStagePlayers = new int[N + 2];
        for (int stage : lastStages) {
            nStagePlayers[stage] += 1;
        }

        int remainingPlayers = nPlayers;
        List<Stage> stages = new ArrayList<>();
        for (int id = 1 ; id <= N; id++) {
            double failure = (double) nStagePlayers[id] / remainingPlayers;
            remainingPlayers -= nStagePlayers[id];

            Stage s = new Stage(id, failure);
            stages.add(s);
        }
        Collections.sort(stages, Collections.reverseOrder());

        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = stages.get(i).id;
        }
        return answer;
    }

    class Stage implements Comparable<Stage> {
        public int id;
        public double failure;

        public Stage(int id_, double failure_) {
            id = id_;
            failure = failure_;
        }

        @Override
        public int compareTo(Stage o) {
            if (failure < o.failure ) {
                return -1;
            }
            if (failure > o.failure ) {
                return 1;
            }
            return 0;
        }
    }
}
```





#### Others

```java
import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        Map<Integer,Integer> map = new HashMap<>();
        Map<Integer,Double> ans = new HashMap<>();

        for (int stage : stages) {
            int count = map.containsKey(stage) ? map.get(stage) + 1 : 1;
            map.put(stage,count);
        }

        int total = stages.length;
        for (int i = 1; i <= N; i++) {
            if (map.containsKey(i)) {
                int cnt = map.get(i);
                ans.put(i,  (double) cnt / total);
                total -= cnt;
            } else {
                ans.put(i, 0.0);
            }
        }

        List<Integer> list = sortByValue(ans);
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }

    public static List<Integer> sortByValue(final Map<Integer,Double> map) {
        List<Integer> list = new ArrayList();
        list.addAll(map.keySet());
        Collections.sort(list, (Comparator) (o1, o2) -> {
            Object v1 = map.get(o1);
            Object v2 = map.get(o2);
            return ((Comparable) v2).compareTo(v1);
        });
        return list;
    }
}
```





HashMap에 containsKey 메소드에 키값을 넘겨주면 해당 키값이 HashMap에 있을경우 true를 없을 경우 false를 넘겨 준다.

HashMap에 containsValue 메소드에 값을 넘겨주면 해당 값이 HashMap에 있을경우 true를 없을 경우 false를 넘겨 준다.

아래는 키가 있는지 값이 있는지 출력해본 코드 이다.

```java
public static void main(String[] args) {
   Map<String, String> map = new HashMap<String, String>();
   map.put("A", "aaa");
   map.put("B", "bbb");
   map.put("C", "ccc");
   
   System.out.println(map.containsKey("A"));
   System.out.println(map.containsKey("a"));
   System.out.println(map.containsValue("aaa"));
   System.out.println(map.containsValue("AAA"));
}
```

출력 결과는 아래와 같다.

```
true
false
true
false
```



#### 참고

- [[Java] HashMap에 키가 있는지 값이 있는지 체크 하기](https://rainny.tistory.com/120)

  