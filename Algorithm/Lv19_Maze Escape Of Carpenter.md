# 목수의 미로 탈출

### 문제

------

아래와 같이 이동할 수 있는 길, 그리고 이동할 수 없는 벽으로 이루어진 크기 N x M 의 지도가 주어진다. 이 때, (N-1, 0) 에서 출발하여 (0, M-1) 까지 도착하는 최단거리를 찾으려 한다. 그런데 목수는 도끼 하나를 갖고 있으며, 이 도끼를 이용하여 벽을 깨부술 수 있다. 하지만 이 도끼는 내구성이 그렇게 좋지 않기 때문에, 벽을 최대 1개밖에 깰 수 없다. 목수가 출발점에서 도착점까지 이동하기 위한 최단거리를 출력하는 프로그램을 작성하시오. 물론, 벽은 최대 1개까지 깰 수 있다. 아래 예제의 경우 ‘X’ 로 표시된 벽을 깰 경우 거리 18만에 출발점에서 도착점으로 이동할 수 있다.

![ec-20](https://s3.ap-northeast-2.amazonaws.com/alms-problem/ec-20.PNG)

 

### 입력

------

첫째 줄에 지도의 세로 길이 N과 지도의 가로 길이 M이 주어진다. ( 1 ≤ N, M ≤ 1,000 ) 둘째 줄부터 지도의 정보가 주어진다. 0은 이동할 수 있는 부분, 1은 이동할 수 없는 부분을 나타낸다.

 

### 출력

------

목수가 (N-1, 0) 에서 출발하여 (0, M-1) 까지 이동하는 데 필요한 최단거리를 출력한다. 목수는 미로를 항상 탈출할 수 있다고 가정한다.

 

### 예제 입력

```
10 10 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 0 1 0 1 0  0 1 1 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0  0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0
```

### 예제 출력

```
18
```

 

### 예제 입력

```
10 10 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 1 0 0
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
	int y, x;
};

int n, m;
bool checkS[MAX][MAX], checkE[MAX][MAX];
int dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int map[MAX][MAX], mapS[MAX][MAX], mapE[MAX][MAX];
int shortest[MAX][MAX];

bool isInside(int y, int x) {
	return ((y >= 0 && y < n) && (x >= 0 && x < m));
}

void bfsS(int yy, int xx) {
	queue <position> q;
	position pos;
	pos.y = yy;
	pos.x = xx;
	q.push(pos);
	mapS[yy][xx] = 0;
	checkS[yy][xx] = true;

	while (!q.empty()) {
		int curY = q.front().y;
		int curX = q.front().x;
		q.pop();

		for (int i = 0; i < 4; i++) {
			position np;
			np.y = curY + dir[i][0];
			np.x = curX + dir[i][1];

			if (isInside(np.y, np.x) && !checkS[np.y][np.x]) {
				checkS[np.y][np.x] = true;
				mapS[np.y][np.x] = mapS[curY][curX] + 1;
				if (map[np.y][np.x] == 0) {
					q.push(np);
				}
			}
		}
	}

}

void bfsE(int yy, int xx) {
	queue <position> q;
	position pos;
	pos.y = yy;
	pos.x = xx;
	q.push(pos);
	mapE[yy][xx] = 0;
	checkE[yy][xx] = true;

	while (!q.empty()) {
		int curY = q.front().y;
		int curX = q.front().x;
		q.pop();

		for (int i = 0; i < 4; i++) {
			position np;
			np.y = curY + dir[i][0];
			np.x = curX + dir[i][1];

			if (isInside(np.y, np.x) && !checkE[np.y][np.x]) {
				checkE[np.y][np.x] = true;
				mapE[np.y][np.x] = mapE[curY][curX] + 1;
				if (map[np.y][np.x] == 0) {
					q.push(np);
				}
			}
		}
	}

}
int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			mapS[i][j] = 987987987;
			mapE[i][j] = 987987987;
		}
	}

	bfsS(n - 1, 0);
	bfsE(0, m - 1);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			printf("%d ", mapS[i][j]);
		}
		printf("\n");
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			printf("%d ", mapE[i][j]);
		}
		printf("\n");
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			shortest[i][j] = mapS[i][j] + mapE[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			printf("%d ", shortest[i][j]);
		}
		printf("\n");
	}

	int min = 987987987;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (shortest[i][j] == 0) continue;
			if (min > shortest[i][j]) {
				min = shortest[i][j];
			}
		}
	}
	printf("%d\n", min);

	return 0;
}
```

