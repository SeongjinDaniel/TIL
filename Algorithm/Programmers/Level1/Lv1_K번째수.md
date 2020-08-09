# Lv1_K번째수

### 문제 [K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748)



#### Solution

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

