# combinationzero

### 문제

------

n명의 사람중 m명을 순서에 상관없이 뽑는 경우의 수를 조합이라고 하며 nCm으로 나타낸다.

nCm은 수식으로 n!/m!(n-m)! 으로 구할 수 있다. (5! = 1 * 2 * 3 * 4 * 5)

n과 m이 주어졌을때 nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오. 

### 입력

------

첫째 줄에 정수 n, m(0≤m≤n≤1,000,000)이 들어온다.

### 출력

------

첫째 줄에 0의 개수를 출력한다.

### 예제 입력

```
25 12
```

### 예제 출력

```
2
```

 ```c++
//[solution]
#include <stdio.h>

int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  int aT = 0, bT = 0, cT = 0;
  int aF = 0, bF = 0, cF = 0;
  int ret;
  int tempF = 5;
  int tempT = 2;

  while(n / tempF >= 1){
    aF += n / tempF;
    tempF *= 5;
  }
  while(n / tempT >= 1){
    aT += n / tempT;
    tempT *= 2;
  }
  
  tempF = 5;
  while((n-m) / tempF >= 1){
    bF += (n - m) / tempF;
    tempF *= 5;
  }
  tempT = 2;
  while((n-m) / tempT >= 1){
    bT += (n-m) / tempT;
    tempT *= 2;
  }

  tempF = 5;
  while(m / tempF >= 1){
    cF += m / tempF;
    tempF *= 5;
  }
  tempT = 2;
  while(m / tempT >= 1){
    cT += m / tempT;
    tempT *= 2;
  }
  
  // int subT = aT - bT + cT;
  // int subF = aF - bF + cF;
  // aT = subT;
  // aF = subF;
  // int motherT = bF + cF - subF;
  // int motherF = bF + cF - subF;
  // printf("%d %d\n", aT, aF);
  // printf("%d %d\n", motherT, motherF);
  
  

  while(1){
    if(aT >= 1 && bT + cT >= 1){
      aT--;
      if(bT != 0) bT--;
      else cT--;
    }
    else break;
  }
  while(1){
    if(aF >= 1 && bF + cF >= 1){
      aF--;
      if(bF != 0) bF--;
      else cF--;
    }
    else break;
  }
  
  // aT = aT - bT + cT;
  // aF = aF - bF + cF;
  
  
  int sonTen = 0, motherTen = 0;
  while(1){
    if(aT == 0 || aF == 0) break;
    else{
      sonTen++;
      aT--;
      aF--;
    }
  }
  
  while(1){
    if(bT + cT == 0 || bF + cF == 0) break;
    else{
      motherTen++;
      // printf("%d %d %d %d\n", bT, cT, bF, cF);
      if(bT != 0) bT--;
      else cT--;

      if(bF != 0) bF--;
      else cF--;
    }
  }
  // printf("\n");
  // printf("%d\n", sonTen);
  // printf("%d\n", motherTen);

  ret = sonTen - motherTen;

  printf("%d\n", ret);
  
  return 0;
}
 ```

