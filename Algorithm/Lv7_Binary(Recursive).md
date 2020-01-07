# binary

### 문제

------

숫자를 입력 받아 이진수로 출력하는 프로그램을 작성하시오.

 

### 입력

------

첫 번째 줄에 숫자를 입력 받는다. 숫자의 크기는 1,000보다 작거나 같다.

 

### 출력

------

첫째 줄에 숫자를 이진수로 바꾸어 출력한다.

 

### 예제 입력

```
14
```

### 예제 출력

```
1110
```

 

### 예제 입력

```
31
```

### 예제 출력

```
11111
```

```c++
#include <stdio.h>

void printBinary(int x){
  // x를 이진수로 바꾸어 출력하는 함수
  
  if(x == 0) printf("0");
  else if(x == 1) printf("1");
  else{
    printBinary(x/2);
    printf("%d", x%2);
  }
}

int main() {
  int x;
  scanf("%d", &x);
  printBinary(x);
  return 0;
}
```

