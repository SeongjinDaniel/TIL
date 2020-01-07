# 팩토리얼

### 문제

------

N 팩토리얼 (N!)은 1부터 N까지의 곱으로 정의된다.

예를 들어

- 3! = 1 x 2 x 3 = 6
- 4! = 1 x 2 x 3 x 4 = 24 이다.

N이 주어질 때, N!을 계산하는 프로그램을 작성하시오. 

### 입력

------

첫 번째 줄에 숫자 N이 주어진다. ( 1 ≤ N ≤ 10 ) 

### 출력

------

첫째 줄에 N!을 출력한다.

 

### 예제 입력

```
4
```

### 예제 출력

```
24
```

```c++
#include <stdio.h>
const int MAX = 15;

int n;
int result=1;
int factorial(int num){
  if(num == 0) return 1;
  else return factorial(num-1) * num;
}

int main() {
  scanf("%d", &n);
  
  printf("%d\n", factorial(n));

  return 0;
}
```