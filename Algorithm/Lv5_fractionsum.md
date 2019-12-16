# fractionsum

--------

## 문제

분자 분모가 모두 자연수인 두 분수의 합 또한 분자 분모가 자연수인 분수로 표현할 수 있다.

두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오.

기약분수란 더 이상 약분되지 않는 분수를 의미한다. 

## 입력

첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 입력되는 네 자연수는 모두 30,000 이하이다.

## 출력

첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 공백으로 구분하여 순서대로 출력한다.

---------

## 예제 입력

2 7
3 5

## 예제 출력

31 35

```c++
#include <stdio.h>

int son, mother;
int son2, mother2;
int resultSon, resultMother;

void getFaction(int son_, int mother_){
  int inxSon = 0;
  int inxMother = 0;
  for(int i = 2; i <= son_; i++){
    if(son_ % i == 0){

      if(mother_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  
  for(int i = 2; i <= mother_; i++){
    if(mother_ % i == 0){

      if(son_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  son = son_;
  mother = mother_;
}

void getFaction2(int son_, int mother_){
  int inxSon = 0;
  int inxMother = 0;
  for(int i = 2; i <= son_; i++){
    if(son_ % i == 0){
        
      if(mother_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  
  for(int i = 2; i <= mother_; i++){
    if(mother_ % i == 0){
      if(son_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  son2 = son_;
  mother2 = mother_;
}

void getFaction3(int son_, int mother_){
  int inxSon = 0;
  int inxMother = 0;
  for(int i = 2; i <= son_; i++){
    if(son_ % i == 0){
      if(mother_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  
  for(int i = 2; i <= mother_; i++){
    if(mother_ % i == 0){
      if(son_ % i == 0){
        son_ /= i;
        mother_ /= i;
      }
    }
  }
  resultSon = son_;
  resultMother = mother_;
}

int main() {
  int result = 0;
  scanf("%d %d", &son, &mother);
  scanf("%d %d", &son2, &mother2);
  
  // 두수의 약수를 찾아서 공통 약수가 있으면
  // 두수 모두 나누어 기약분수를 만든다.
  // 1제외
  getFaction(son, mother);
  
  getFaction2(son2, mother2);
  
  resultSon = son*mother2 + son2*mother;
  resultMother = mother * mother2;
  
  getFaction3(resultSon, resultMother);
  printf("%d %d\n", resultSon, resultMother);

  return 0;
}
```

