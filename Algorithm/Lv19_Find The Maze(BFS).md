# 미로 찾기

### 문제

------

아래와 같이 이동할 수 있는 길, 그리고 이동할 수 없는 벽으로 이루어진 크기 N x M 의 지도가 주어진다. 이 때, (N-1, 0) 에서 출발하여 (0, M-1) 까지 도착하는 최단거리를 출력하는 프로그램을 작성하시오. 아래 그림에 대하여 S에서 E까지 가는 최단거리는 22이다.

![ec-16](https://s3.ap-northeast-2.amazonaws.com/alms-problem/ec-16.PNG)

 

### 입력

------

첫째 줄에 지도의 세로 길이 N과 지도의 가로 길이 M이 주어진다. ( 1 ≤ N, M ≤ 1,000 ) 둘째 줄부터 지도의 정보가 주어진다. 0은 이동할 수 있는 부분, 1은 이동할 수 없는 부분을 나타낸다.

 

### 출력

------

(N-1, 0) 에서 출발하여 (0, M-1) 까지 이동하는 데 필요한 최단거리를 출력한다.

 

### 예제 입력

```
10 10
0 0 0 0 0 0 1 1 0 0
0 1 1 1 0 0 1 0 1 0
0 1 1 1 0 0 1 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 1 1 1 1 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 1 1 1 0 1 1 0 0
0 0 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0
0 0 0 0 0 0 0 1 0 0
```

### 예제 출력

```
22
```

```c++
//[solution]
#include <cstdio>
#include <queue>
using namespace std;
const int MAX = 1005;

struct position{
  int y;
  int x;
};

int n, m;
int map[MAX][MAX];
position dir[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool isInside(int y, int x){
  return ((y >= 0 && y < n) && (x >= 0 && x < m));
}

void bfs(){
  queue <position> q;
  position pos;
  pos.y = n-1; pos.x = 0;
  q.push(pos);
  map[pos.y][pos.x] = 1;
  
  while(!q.empty()){
    int curY = q.front().y;
    int curX = q.front().x;
    q.pop();
    
    for(int i = 0; i < 4; i++){
      position npos;
      npos.y = curY + dir[i].y;
      npos.x = curX + dir[i].x;
      
      if(isInside(npos.y, npos.x) && !map[npos.y][npos.x]){
          map[npos.y][npos.x] = map[curY][curX] + 1;
          q.push(npos);
      }
    }
  }
}

int main() {
  scanf("%d %d", &n, &m);
  for(int i = 0;i < n; i++){
    for(int j = 0; j < m; j++){
      scanf("%d", &map[i][j]);
    }
  }

  bfs();

  printf("%d\n", map[0][m-1]-1);

  return 0;
}
```

