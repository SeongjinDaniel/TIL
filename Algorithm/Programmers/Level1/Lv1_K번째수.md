# Lv1_K번째수



### Question

- ### [K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748)

  

#### Mine

```java
def solution(array, commands):
#     answer = []
#     newList = []
#     for i in range(len(commands)):
#         start = commands[i][0]
#         end = commands[i][1]
#         pick = commands[i][2]
#         newList.clear()
#         for idx in range(start, end + 1):
#             newList.append(array[idx-1])
        
#         list.sort(newList)
#         # newList = sorted(newList)
#         # for index in range(len(newList)):
#         #     print(newList[index], end = ' ')
        
#         answer.append(newList[pick-1])
#     return answer
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
```



#### Second Mine

```java
import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int cmdLen = commands.length;
        int[] answer = new int[cmdLen];
        // commands length for문 안에
        // j - i 의 차이 만큼 list에 넣고 정렬
        // 정렬 후 k번째 수를 찾아 answer 배열에 저장.
        for (int i = 0; i < cmdLen; i++) {
            List<Integer> list = new ArrayList<>();
            for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
                list.add(array[j]);
            }
            Collections.sort(list);
            int order = commands[i][2] - 1;
            answer[i] = list.get(order);
        }
        return answer;
    }
}
```



#### Others

```java
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
```

