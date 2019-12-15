# 두 수 교환하기

## 출력

첫째 줄에 바뀐 두 수를 출력한다.

-----------------

## 예제 입력

10 5

## 예제 출력

5 10

------------------

## 예제 입력

45 55

## 예제 출력

55 45

```C++
#include <stdio.h>

int main() {
  int a, b, temp;
  scanf("%d %d", &a, &b);
  
  temp = a;
  a = b;
  b = temp;
  
  printf("%d %d", a, b);
  return 0;
}
```



