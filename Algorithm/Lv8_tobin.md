# tobin

### 문제

------

두 정수 n, k를 입력받아 k개의 1을 가진 n자리 이진 패턴을 출력하는 프로그램을 작성하세요.

### 입력

------

두 정수 n, k가 입력으로 주어진다. ( 0 < n <= 30, 0 <= k < 8 , n >= k )

### 출력

------

결과를 내림차순으로 출력한다.



### 예제 입력

```
2 1
```

### 예제 출력

```
10 01
```

 

### 예제 입력

```
2 0
```

### 예제 출력

```
00
```

 

### 예제 입력

```
4 2
```

### 예제 출력

```
1100 1010 1001 0110 0101 0011
```

 

### 출처

------

uwaterloo junior contest 

------

```c++
//[solution]
#include <stdio.h>

const int MAX = 35;

int n, k;
bool check[MAX];
int data[MAX];

void tobin(int x, int start){
  if(x >= k){
    for(int i = 0; i < n; i++){
      printf("%d", data[i]);
    }
    printf("\n");
  }
  else{
    for(int i = start; i < n; i++){
      if(!check[i]){
        check[i] = true;
        data[i] = 1;
        tobin(x + 1, i);
        check[i] = false;
        data[i] = 0;
      }
    }
  }
}

int main() {
  scanf("%d %d", &n, &k);
  tobin(0, 0);
  
  return 0;
}
```

