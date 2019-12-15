# A+B

----------------------------------

## 문제

두 수 A,B를 입력받고, A + B를 출력하는 프로그램을 작성해보자.

## 입력

첫째 줄에 정수 A,B가 주어진다. ( A,B는 100 이하의 정수 )

## 출력

첫째 줄에 A + B를 출력한다.

## 예제 입력

5 6

## 예제 출력

11

```java
#include <cstdio>
using namespace std;

int main() {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d\n", a + b);
  return 0;
}
```