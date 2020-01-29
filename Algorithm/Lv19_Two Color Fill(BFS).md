# 2색칠하기

### 문제

------

2색 칠하기란, 다음 두 조건을 만족하면서 그래프의 정점을 모두 색칠할 수 있는지 묻는 문제이다. 2개의 색이 존재한다. 인접한 두 정점은 색깔이 다르다. 그래프가 주어질 때, 2색 칠하기가 가능한지 출력하는 프로그램을 작성하시오. 예를 들어, 아래의 그래프는 2색 칠하기가 가능한 그래프이며, 정점을 색칠한 결과는 다음과 같다.

![ec-13](https://s3.ap-northeast-2.amazonaws.com/alms-problem/ec-13.PNG)

 

### 입력

------

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. ( 1 ≤ N ≤ 10,000, 1 ≤ M ≤ 100,000 ) 둘째 줄부터 간선의 정보가 주어진다. 각 줄은 두 개의 숫자 a, b로 이루어져 있으며, 이는 정점 a와 정점 b가 연결되어 있다는 의미이다.(0 ≤ a, b ≤ N-1)

 

### 출력

------

주어진 그래프에 대하여 2색 칠하기를 할 수 있으면 YES, 할 수 없으면 NO를 출력한다.

 

### 예제 입력

```
9 10 0 1 0 2 0 3 1 5 2 5 3 4 5 6 5 8 6 7 7 8
```

### 예제 출력

```
YES
```

 

### 예제 입력

```
9 11 0 1 0 2 0 3 1 5 2 5 3 4 4 5 5 6 5 8 6 7 7 8
```

### 예제 출력

```
NO
```

```c++
//[solution]
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

const int MAX = 100005;

int n, m;
vector <int> v[MAX];
bool check[MAX];
int color[MAX];
bool flag;

void bfs(){
  queue <int> q;
  q.push(0);
  color[0] = 1;
  
  while(!q.empty()){
    int cur = q.front();
    int nodeColor = color[cur];
    q.pop();
    
    for(int i = 0; i < v[cur].size(); i++){
      int next = v[cur][i];
      if(nodeColor == color[next]){
        flag = true;
        return;
      }
      
      if(!check[next]){
        check[next] = true;
        q.push(next);
        color[next] = nodeColor * -1;
      }
      
    }
    
  }
  
}


int main() {
  scanf("%d %d", &n, &m);
  for(int i  = 0; i < n; i++){
    int a, b;
    scanf("%d %d", &a, &b);
    
    v[a].push_back(b);
    v[b].push_back(a);
  }
  
  bfs();
  if(flag) printf("NO\n");
  else printf("YES\n");

  return 0;
}
```

