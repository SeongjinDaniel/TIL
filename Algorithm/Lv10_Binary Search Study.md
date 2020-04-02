# Binary Search

- **정렬 되어 있는 숫자들 중에서** 특정 숫자를 찾는다.

  - 2 3 4 5 7 8 9 11 14 23

  1. 중간값을 가리키고 찾고자하는 숫자와 비교한다.
  2. 만약 중간값이 7이고, 찾고자하는 값은 14이면
  3. 14는 7보다 큰 값인걸 알수 있다.
  4. 7을 포함해서 왼쪽에 있는 숫자들은 다 날려버리고 생각하지 않는다.
  5. 그리고 남아 있는 숫자들 중에서 중간 값을 찾고 내가 찾고자하는 숫자와 비교한다.
  6. 현재는 내가 찾고자하는 숫자가 오른쪽에 있으니까 왼쪽을 또 날려버린다.
  7. 또 남아있는 숫자중에 중간값을 찾고 그 숫자가 내가 찾는 값이면 끝낸다.

- Binary Search의 효유류성

  - 정렬해야 하면 O(log n)이 아니라 결국 O(n log n)아닌가요?

    yes

  - 이미 배열이 정렬되어 있다면 Binary Search가 효율적임

  - 숫자 찾기를 엄청 많이 해야하는 경우에는 오히려 정렬을 한 뒤에 Binary Search를 하는 것이 좋음

    ex) 배열에 숫자가 1,000개 인데 숫자 찾기를 100,000번 해야 한다면?

## Binary Search의 구현

#### [Recap] 재귀 함수 디자인의 과정

1. 작성하려는 함수의 역할을 말로 명확하게 정의한다.
2. 함수가 기저조건에서 제대로 동작하게 작성한다.
3. 함수가 제대로 동작한다고 가정하고 함수를 완성한다.
4. 함수를 완성한 후, 기저조건으로 수렴함을 보인다.

#### Binary Search의 구현 [재귀호출]

1. 작성하려는 함수의 역할을 말로 명확하게 정의한다.

   ```c++
   // rr의 s번째 값부터 e번째 값중 value를 찾는 함수
   // 찾으려는 해당 숫자가 있으면 index번호 return
   // 없으면 -1 return
   int binarySearch(int arr[], int s, int e, int value)
   ```

2. 함수가 기저조건에서 제대로 동작하게 작성한다. 

   ```c++
   int binarySearch(int arr[], int s, int e, int value)
       if(s > e) return  -1;
       else if(s == e){
           if(value == arr[s]) return s;
           else return -1;
       }
   ```

3. 함수가 제대로 동작한다고 가정하고 함수를 완성한다.

   ```c++
   int binarySearch(int arr[], int s, int e, int value)
       if(s > e) return  -1;
       else if(s == e){
           if(value == arr[s]) return s;
           else return -1;
       }	
       int mid = (s+e)/2;
        if(arr[mid] == value) return mid;
        else if(arr[mid]) > value) return binarySearch(arr, s, mid-1, value);
        else return binarySearch(arr, mid + 1, e, value);
   ```

   4. 함수를 완성한 후, 기저조건으로 수렴함을 보인다. -> YES

-------

#### binary search 구현 (재귀)

```c++
#include <stdio.h>

int binarySearch(int arr[], int start, int end, int value){
    // arr의 start부터 end까지 값들 중에서
    // value가 존재한다면 그 위치를 반환하고,
    // 그렇지 않다면 -1을 반환하는 함수
   
    if(start > end){// 숫자가 존재 x
        return -1;
    }else if(start == end){ // 숫자가 하나
        if(arr[start] == value) return start;
        else return -1;
    }else{ // 숫자가 여러개
        int mid = (start+end) / 2;
        if(arr[mid] == value) return mid;
        else if(arr[mid] > value) return binarySearch(arr, start, mid-1, value);
        else return binarySearch(arr, mid+1, end, value);
    }
}

int main(){
    int n, m;
    int arr[100];
    
    scanf("%d", &n);
    
    // arr은 정렬이 되어 있어야 함.
    for(int i = 0;i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    scanf("%d", &m);
    
    int inx = binarySearch(arr, 0, n-1, m);
    
    if(inx == -1){
        printf("수가 없습니다.\n");
    }else{
        printf("%d번째에 숫자가 있습니다.", inx);
    }
    
	return 0;
}
```







