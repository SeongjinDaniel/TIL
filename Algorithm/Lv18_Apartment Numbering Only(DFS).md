# 단지 번호 붙이기

### 문제

------

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![ec-17](https://s3.ap-northeast-2.amazonaws.com/alms-problem/ec-17.PNG)

 

### 입력

------

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

 

### 출력

------

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

 

### 예제 입력

```
7 0110100 0110101 1110101 0000111 0100000 0111110 0111000
```

### 예제 출력

```
3 7 8 9
```

 

### 출처

------

KOI 1996 초등부 1번 

```c++
//[solution]
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 30;

struct position {
	int y;
	int x;
};

int n, group[MAX], groupInx = 1;
int map[MAX][MAX];
int chkGroup[MAX][MAX];
position dir[4] = { { -1, 0 },{ 1, 0 },{ 0, -1 },{ 0, 1 } };

void dfs(int y, int x) {
	map[y][x] = groupInx + 1;
	group[groupInx]++;

	for (int i = 0; i < 4; i++) {
		int ny = y + dir[i].y;
		int nx = x + dir[i].x;

		if ((ny >= 0 && ny < n) && (nx >= 0 && nx < n)) {
			if (map[ny][nx] == 1) {
				dfs(ny, nx);
			}

		}
	}
}

void getResult() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!chkGroup[i][j] && map[i][j] == 1) {
				chkGroup[i][j] = true;
				dfs(i, j);
				groupInx++;
			}
		}
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &map[i][j]);
		}
	}

	getResult();
	 sort(group, group + groupInx);
	 printf("%d\n", groupInx - 1);
	 for(int i = 1; i < groupInx; i ++){
	   printf("%d\n", group[i]);
	 }

	return 0;
}
```

