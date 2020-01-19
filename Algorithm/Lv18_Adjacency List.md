# 인접 리스트 구현

```c++
//인접 리스트을 이용한 그래프의 구현
// 5 6  (정점의 갯수, 간선의 갯수)
// 1 --- 2
// | \  /
// |  \/
// 3   4 ----- 5
// ㄴ---------/

// myGraph[1] : 2 3 4
// myGraph[2] : 1 4
// myGraph[3] : 1 5
// myGraph[4] : 1 2 5
// myGraph[5] : 3 4 

// 5 6
// 1 2
// 1 3
// 1 4
// 2 4
// 3 5
// 4 5
#include <cstdio>
#include <vector>
using namespace std;

const int MAX = 100;
int main() {
  vector <int> myGraph[MAX];
  // vector <int> 가 MAX게 생김
  // myGraph[0] --> vector
  // myGraph[1] --> vector
  // ...
  // myGraph[99] --> vector
  
  // myGraph[X] =--> X와 인접해 있는 모든 
  int n, m;
  
  scanf("%d %d", &n, &m);
  
  for(int i = 0;i < m; i++){
    int a, b;
    
    scanf("%d %d", &a, &b); // a와 b가 연결돼있음.
    
    myGraph[a].push_back(b);
    myGraph[b].push_back(a);
  
  }
  
  for(int i = 1; i <= n; i++){
    printf("%d : ", i);
    
    // myGraph[i]
    for(int j = 0; j < myGraph[i].size(); j++){
      printf("%d ", myGraph[i][j]);
    }
    printf("\n");
  }
    
  return 0;
}
```

