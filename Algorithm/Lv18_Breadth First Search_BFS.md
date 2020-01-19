# 그래프 순회

## 너비우선탐색(Breadth First Search) : BFS

- 큐를 이용하여 그래프를 순회하는 방법

```c++
// 너비우선탐색(BFS)

// 1 ----- 2 ------ 6
//  \     / \      /
//   \   /   4 ---5
//    \ /   / \
//     3 - 7 - 8 - 9
// DFS: 1 -> 2-> 3 -> 7 -> 4 -> 5 -> 6 -> 8 -> 9
// BFS: 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 5 -> 8 -> 9 
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
const int MAX = 100;

int n, m;
vector <int> myGraph[MAX];  

void BFS(){
  // 1. 지작점을 큐에다가 삽입한다.
  // 2. 시작점을 색칠한다.
  
  // BFS 시작!
  
  // 3. 큐에서 하나를 뺀다. 얘가 우리의 현재 위치이다.
  // 4. 인접한 모든 정점에게 방문했는지 물어보고
  //    방문을 하지 않았다면, 색칠하고 큐에 삽입한다.
  // 5. 모두 완료 했다면 3. 으로 돌아간다.
  queue <int> Queue;
  bool check[MAX] = {0}; // check[x] = true면 x가 색칠이 됨.
  
  // Queue.push(x); // x를 큐에 삽입
  // Queue.pop(); // 큐의 맨앞에 있는 원소를 제거
  // Queue.front(); // 맨 앞에 있는 원소를 반환
  // Queue.empty(); //  비었으면 true를 반환
  
  Queue.push(1);
  check[1] = true;
  
  while(!Queue.empty()){
    int current = Queue.front();
    Queue.pop();
    printf("%d ", current);
  
    for(int i = 0; i < myGraph[current].size();i++){
      int next = myGraph[current][i];
      // current -- next
      
      if(check[next] == false){
        check[next] = true;
        Queue.push(next);
        
      }
    }
    
  }
}

int main() {
  scanf("%d %d", &n, &m);
  
  for(int i = 0; i< m; i++){
    int a, b;
    
    scanf("%d %d", &a, &b); // a --- b
    
    myGraph[a].push_back(b);
    myGraph[b].push_back(a);
  }
  
  BFS();

  return 0;
}
```

