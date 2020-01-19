# 그래프 순회

## 깊이우선탐색 (Depth First Search) : DFS

- 스택을 이용하여 그래프를 순회하는 방법

- 스택 = 선행 관계

- 나를 먼저 방문하고 그 다음으로 인접한 노드를 차례로 방문

  단, 방문했던 노드는 방문하지 않는다.

- 정점과 간선으로 이루어진 자료구조

### 깊이 우선 탐색의 과정

- DFS(v, visited) :           ---> v: 시작점, visited: 방문한 기록

  1. v를 방문했다고 처리한다
  2. v와 인접한 모든 w에 대하여 다음을 반복
  3. 만약 w를 아직 방문하지 않았다면, (= 이웃을 아직 방문하지 않았다면)
  4. DFS(w, visited)
  5. 방문순서 반환

  - 재귀함수 -> 스택 사용

```c++
// graph라는 그래프를 x부터 시작해서 DFS하라!
void DFS(Graph graph, int x, bool visieted[]){
	visited[x] = true; // = 방문했다 (false = 방문하지 않았다.)
	
	for(int i =0 ; i < graph[x].size(); i++){
		int y = graph[x][i];
        
        if(visited[y] == false){
            DFS(graph, y, visited); // graph라는 그래프를 y부터 시작해서 DFS하라!
        }
	}
}
```

```c++
// DFS
//  1 - 2 - 3 - 4 - 5
//   \
//    6 - 7 - 8 - 9
//     \
//      10 - 11 - 12 

//   1 ----- 2 -------- 6
//    \     / \       /
//     \   /   4 --- 5
//      \ /   / \ 
//       3 - 7 - 8 - 9

// 1 --> 2 --> 3 --> 7 --> 4 --> 5 --> 6 --> 8 --> 9

// 9 12 ( 정점 개수 ) ( 간선 개수 )
// 1 2
// 1 3
// 2 3
// 2 4
// 2 6
// 3 7
// 4 5
// 4 7
// 4 8
// 5 6
// 7 8
// 8 9

#include <cstdio>
#include <vector>
using namespace std;
const int MAX = 100;

int n, m;
vector <int> myGraph[MAX];
bool visited[MAX];

void DFS(int x) {
	// x부터 시작해서 DFS하여 그 순서를 출력하는 함수
	// 단, visited에 방문 기록이 있음.
	visited[x] = true;
	printf("%d ", x);

	for (int i = 0; i < myGraph[x].size(); i++) {
		int y = myGraph[x][i];
    // x와 y가 연결이 되어 있다.
		if (visited[y] == false) {
			DFS(y);
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int a, b;

		scanf("%d %d", &a, &b);

		myGraph[a].push_back(b);
		myGraph[b].push_back(a);
	}

	DFS(1);

	return 0;
}
```

- 정확성 증명 (DFS가 정말 순회를 하는가)
  1. 모든 정점을 방문한다.
  2. 하나의 정점을 두번 이상 방문하지 않는다.
  3. 순회를 한다 = 정점을 모두 방문했다.

[방문 순서]

1. 나 방문

2. 모든 이웃에게 물어봄

   |V| = 2 * |E| 

[시간 복잡도]

각 정점은 1번씩, 각 간선은 2번씩 방문함 = O(V+E)