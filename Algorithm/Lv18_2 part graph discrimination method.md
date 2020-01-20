# 이분 그래프 판별

### 문제

------

이분 그래프란, 아래 그림과 같이 정점을 크게 두 집합으로 나눌 수 있는 그래프를 말한다. 여기서 같은 집합에 속한 정점끼리는 간선이 존재해서는 안된다. 예를 들어, 아래 그래프의 경우 정점을 크게 {1, 4, 5}, {2, 3, 6} 의 두 개의 집합으로 나누게 되면, 같은 집합에 속한 정점 사이에는 간선이 존재하지 않으므로 이분 그래프라고 할 수 있다.

![ec-14](https://s3.ap-northeast-2.amazonaws.com/alms-problem/ec-14.PNG)그래프가 입력으로 주어질 때, 이 그래프가 이분그래프인지를 판별하는 프로그램을 작성하시오.

 

### 입력

------

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. ( 2 ≤ N ≤ 1,000, N-1 ≤ M ≤ 100,000 ) 둘째 줄부터 간선의 정보가 주어진다. 각 줄은 두 개의 숫자 a, b로 이루어져 있으며, 이는 정점 a와 정점 b가 연결되어 있다는 의미이다. (1 ≤ a, b ≤ N)

 

### 출력

------

주어진 그래프가 이분 그래프이면 Yes, 아니면 No를 출력한다.

 

### 예제 입력

```
6 5 1 2 2 4 3 4 3 5 4 6
```

### 예제 출력

```
Yes
```

 

### 예제 입력

```
4 5 1 2 1 3 1 4 2 4 3 4
```

### 예제 출력

```
No
```

```c++
//[solution]
#include <cstdio>
#include <vector>
using namespace std;

const int MAX = 100005;

int n, m;
vector <int> v[MAX];
int check[MAX];
bool flag;

void dfs(int x, int color){
  check[x] = color;
  
  for(int i = 0; i < v[x].size(); i++){
    int next = v[x][i];
    if(check[next] == color){
      flag = true;
      return;
    }
    if(check[next] == 0){
      dfs(next, color*-1);
    }
  }
}

int main() {
  scanf("%d %d", &n, &m);
  for(int i = 0; i < m; i++){
    int a, b;
    scanf("%d %d", &a, &b);
    
    v[a].push_back(b);
    v[b].push_back(a);
  }
  
  dfs(1, 1);
  if(flag) printf("No\n");
  else printf("Yes\n");
 
  return 0;
}
```

