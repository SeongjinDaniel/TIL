# combinationpascal

### 문제

------

n명의 사람중 m명을 순서에 상관없이 뽑는 경우의 수를 조합이라고 하며 nCm으로 나타낸다.

이 조합은 파스칼의 삼각형과 아주 밀접한 관련이 있다고 한다.

n과 m이 주어졌을때 nCm의 값을 출력하는 프로그램을 작성하시오. 

### 입력

------

첫째 줄에 정수 n, m(0 ≤ m ≤ n ≤ 30)이 들어온다.

### 출력

------

첫째 줄에 nCm의 값을 출력한다.

### 예제 입력

```
5 2
```

### 예제 출력

```
10
```

 ```c++
//[solution]
#include <stdio.h>
const int MAX = 35;
int main() {
  int n, m;
  int result[MAX][MAX] = {0};
  scanf("%d %d", &n, &m);
  
  for(int i = 0; i <= 30; i++){
    for(int j = 0; j <= i+1; j++){
      if(i == 1 || j == i){
        result[i][j] = 1;
      }
      else{
        result[i][j] = result[i-1][j-1] + result[i-1][j];
      }
    }
  }
  
  printf("%d", result[n][m]);
  return 0;
}
 ```



