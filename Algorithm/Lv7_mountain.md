# mountain

### 문제

------

봉우리가 여러개인 산 모양을 출력한다. 산 모양은 그림과 같고 좌우 대칭이다.

![mountain](http://cfile3.uf.tistory.com/image/210B1037586DA2B30D0903)

 

### 입력

------

첫 번째 줄에 숫자를 입력 받는다. 숫자의 크기는 20보다 작은 자연수이다.

 

### 출력

------

출력 예의 형식으로 출력한다.

 

### 예제 입력

```
3
```

### 예제 출력

```
1213121
```

 

### 예제 입력

```
5
```

### 예제 출력

```
1213121412131215121312141213121
```

```c++
//[solution]
#include <stdio.h>

void getResult(int x){
  if(x == 0){
    return;
  }
  else{
    getResult(x - 1);
    printf("%d", x);
    getResult(x -1);
  }
}

int main() {
  int n;
  scanf("%d", &n);
  
  getResult(n);
  
  return 0;
}
```

