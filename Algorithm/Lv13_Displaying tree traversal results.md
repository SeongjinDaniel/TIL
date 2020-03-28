# 트리 순회 결과 출력하기

### 문제

------

루트가 0인 이진트리가 주어질 때, 이를 전위순회, 중위순회, 후위순회한 결과를 각각 출력하는 프로그램을 작성하시오.

 

### 입력

------

첫 번째 줄에 트리의 노드 개수 n이 주어진다. ( 1 ≤ n ≤ 100 ) 두 번째 줄부터 트리의 정보가 주어진다. 각 줄은 3개의 숫자 a, b, c로 이루어지며, 그 의미는 노드 a의 왼쪽 자식노드가 b, 오른쪽 자식노드가 c라는 뜻이다. 자식노드가 존재하지 않을 경우에는 -1이 주어진다.

 

### 출력

------

첫 번째 줄에 전위순회, 두 번째 줄에 중위순회, 세 번째 줄에 후위순회를 한 결과를 출력한다.

 

### 예제 입력

```
6
0 1 2
1 3 4
2 -1 5
3 -1 -1
4 -1 -1
5 -1 -1
```

### 예제 출력

```
0 1 3 4 2 5
3 1 4 0 2 5
3 4 1 5 2 0
```

 #### solve

```c++
#include <stdio.h>

const int MAX = 100;

struct Tree{
  int left;
  int right;
};

Tree tree[MAX];

void preOrder(int x){
  if(tree[x].left == -1 && tree[x].right == -1){
    printf("%d ", x);
  }
  else{
    printf("%d ", x);
    if(tree[x].left != -1)
      preOrder(tree[x].left);
    
    if(tree[x].right != -1)
      preOrder(tree[x].right);
  }
}

void inOrder(int x){
  if(tree[x].left == -1 && tree[x].right == -1){
    printf("%d ", x);
  }
  else{
    if(tree[x].left != -1)
      inOrder(tree[x].left);
      
    printf("%d ", x);
    
    if(tree[x].right != -1)
      inOrder(tree[x].right);
  }
}

void postOrder(int x){
  if(tree[x].left == -1 && tree[x].right == -1){
    printf("%d ", x);
  }
  else{
    if(tree[x].left != -1)
      postOrder(tree[x].left);

    if(tree[x].right != -1)
      postOrder(tree[x].right);
      
    printf("%d ", x);
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    tree[a].left = b;
    tree[a].right = c;
  }
  
  preOrder(0);
  printf("\n");
  inOrder(0);
  printf("\n");
  postOrder(0);
  printf("\n");
  

  return 0;
}
```

