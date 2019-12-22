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
// [solution]
#include <cstdio>
using namespace std;

int main(){
  int n;
  int arr[20];
  int inx = 1;
  
  scanf("%d", &n);
  
  while(1){
    if(n == 1) break;
    arr[inx++] = n % 2;
    n = n / 2;
  }
  
  printf("1");
  for(int i = inx - 1; i >= 1; i--){
    printf("%d", arr[i]);
  }
  printf("\n");
  
  return 0;
}
 ```

