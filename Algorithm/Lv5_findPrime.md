# findprime

--------

## 문제

주어진 숫자들 중 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오. 

## 입력

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 줄에 걸쳐 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

## 출력

주어진 수들 중 소수의 개수를 출력한다.

---------

## 예제 입력

4
1
3
5
7

## 예제 출력

3

```c++
#include <stdio.h>

int main() {
  int n;
  int cntTemp = 0;
  int ret = 0;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    int num;
    scanf("%d", &num);
    if(num == 1) continue;
    cntTemp = 0;
    for(int i = 2; i < num; i++){
      if(num % i == 0) cntTemp++;
    }
    if(cntTemp == 0) ret++;
  }
  printf("%d\n", ret);

  return 0;
}
```

