# 대소문자 변환

### 문제

------

문자열이 주어질 때, 대문자는 소문자로, 소문자는 대문자로 바꾸는 프로그램을 작성하시오. 알파벳이 아닌 문자는 그대로 유지한다. 

### 입력

------

첫 번째 줄에 문자열이 주어진다. ( 1 ≤ 문자열의 길이 ≤ 1,000 ) 

### 출력

------

문자열 내의 대문자는 소문자로, 소문자는 대문자로 바꾼 결과를 출력한다.

 

### 예제 입력

```
hELLO wORLD!
```

### 예제 출력

```
Hello World!
```

 ```c++
#include <stdio.h>
#include <string.h>

const int MAX = 1005;
int main() {
  char ss[MAX];
  fgets(ss, MAX, stdin);
  int len = strlen(ss);

  for(int i = 0; i < len; i++){
    if(ss[i] >= 'a' && ss[i] <= 'z'){
      printf("%c", ss[i] - 32);
    }
    else if(ss[i] >= 'A' && ss[i] <= 'Z'){
      printf("%c", ss[i] + 32);
    }
    else{
      printf("%c", ss[i]);
    }
   
  }

  return 0;
}
 ```