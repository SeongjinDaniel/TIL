# 인접행렬 구현

```c++
//인접행렬을 이용한 그래프의 구현
  // 5 6  (정점의 갯수, 간선의 갯수)
  // 1 2  1 --- 2
  // 1 3  | \  /
  // 1 4  |  \/
  // 2 4  3   4 ----- 5
  // 4 5  ㄴ---------/
  // 3 5 
  
// Q1. 정점 X와 Y가 연결이 되어 있는가? (YES/NO)
// Q2. 정점 X와 연결이 되어 있는 모든 정점을 출력하라.

#include <stdio.h>

const int MAX = 10;

bool isConnected(int myGraph[MAX][MAX], int x, int y){
  // myGraph에서 x와 y가 연결이 되어 있으면 true, 아니면 false를 반환
  
  return myGraph[x][y] == 1 ? true : false;
}

void getAdj(int myGraph[MAX][MAX],int n, int x) {
  // n개의 정점을 갖는 myGraph에서 x와 연결되어 있는 모든 정점을 출력하는 함수
  
  for(int i = 1; i <= n; i++){
    if(myGraph[x][i] == 1){
      printf("%d ", i);
    }
  }
  printf("\n");
  
}

int main() {
  int n, m; // n : 정점의 갯수, m : 간선의 갯수
  int myGraph[MAX][MAX] = {0};
  
  scanf("%d %d", &n, &m);
  
  for(int i = 0; i < m; i++){
    int a, b;
    
    scanf("%d %d", &a, &b); // a와 b가 연결이 되어 있따.
    
    myGraph[a][b] = 1;
    myGraph[b][a] = 1;
  }
  
  // for(int i = 1; i <= n; i++){
  //   for(int j = 1;j <= n; j++){
  //     printf("%d ", myGraph[i][j]);
  //   }
  //   printf("\n");
  // }
  
  // isConnected O(1)
  
  printf("%d\n", isConnected(myGraph, 1, 2)); // 1
  printf("%d\n", isConnected(myGraph, 1, 5)); // 0
  printf("%d\n", isConnected(myGraph, 3, 5)); // 1
  
  // getAdj O(n)
  
  getAdj(myGraph, n, 2); // 1 4
  getAdj(myGraph, n, 4); // 1 2 5
  
  
  return 0;
}
```

