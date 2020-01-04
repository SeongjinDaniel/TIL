# array3

### 문제

------

N이 주어질 때, 다음과 같은 프로그램을 작성해보자. 

### 입력

------

첫째 줄에 자연수 N이 주어진다.(1<=N<=100)

 

### 출력

------

예시를 참고하여 작성하자.

### 예제 입력

```
3 
```

### 예제 출력

```
1 2 4 3 5 6 
```

 

### 예제 입력

```
5
```

### 예제 출력

```
1 2 4 7 11 3 5 8 12  6 9 13  10 14 15 
```

```c++
//[solution]
//array3
#include <stdio.h>

int main() {
  int n;
  int arr[110][110] = {0};
  int r = 1, c = 1;
  int k = 1;
  scanf("%d", &n);
  
  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= i; j++){
      if(i == 1 && j == 1){
        arr[r][c] = k;
        k++;
        c++;
      }
      else{
        arr[r][c] = k;
        k++;
        if(i == j){
          c = i + 1;
          r = 1;
        }
        else{
          c--;
          r++;
        }
        
      }
    }
    
  }
  
  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= n - i + 1; j++){
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }

  return 0;
}
```

