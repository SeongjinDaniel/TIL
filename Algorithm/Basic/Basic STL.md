# Basic STL

## Container

- Vector
- Pair
- Stack
- Queue
- Set
- Map
- Priority Queue

↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑자료구조

--------------------------------------

## Algorithm

- sort
- lower_bound
- upper_bound
- unique

↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑연산을 하는 함수들

---

## Vector

### Initialize

vector \<int> myArray(10, 3); // 길이가 10인 배열에서 3으로 초기화

#### Vector method

1.  .push_back(x)

   ```c++
   vector <int> myArray();
   myArray.push_back(1);
   myArray.push_back(2);
   myArray.push_back(3);
   ```

2.  .pop_back()

3.  .resize(x)

   - 크기를 변경

      .resize(5, 3); 크기를 5로 변경하고 나머지를 3으로 채워라

     만약 여기서 길이를 줄이면 .resize(2); 길이 2 뒤에는(길이 3부터) 삭제됨

4.  size()

   - 사이즈 변환 됨

     myArray.size(); 

```c++
#include <cstdio>
#include <vector>
using namespace std;

int main() {
  vector <int> arr;
  
  arr.push_back(1);
  arr.push_back(2);
  arr.push_back(3); // 1 2 3
  
  printf("%d\n", arr[0]);
  printf("%d\n", arr[1]);
  printf("%d\n", arr[2]);
  
  arr.pop_back();
  
  printf("%d\n", arr.size()); // 2
  
  arr.resize(10, 5); // 1 2 5 5 5 5 5 5 5 5
  
  for(int i = 0;i < arr.size(); i++){
    printf("%d ", arr[i]);
  }
  
  arr.resize(5);
  
  printf("\n");
  
  for(int i =0 ;i < arr.size();i++){
    printf("%d ", arr[i]);
  }
  
  return 0;
}
```

