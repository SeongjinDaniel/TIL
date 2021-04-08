# Index



(검색을 위해) 임의의 규칙대로 부여된, 임의의 대상을 가리키는 무언가.

 

#### Cluster : 군집

#### Clustered : 군집화

#### Clusted Index : 군집화된 인덱스



#### Advanced

1. Explain aka 실행계획
2. B - Tree, Page(Block) in InnoDB
3. Cardinality
4. Composite key
5. innodb_buffer_pool_size
6. log_throttle_queries_not_using_indexes



#### 인덱스가 왜 필요할까?

**Full Table Scan** : 대용량 데이터에 비효율적이므로, 인덱스를 메모리에 저장한다.



#### 인덱스의 구조와 원리

**이진트리**

<img src="C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20210407193636585.png" alt="image-20210407193636585" style="zoom:70%;" />

**B-Tree**

이진 트리가 자식 노드가 최대 2개인 노드를 말하는 것이라면 B-Tree는 자식 노드의 개수가 2개 이상인 트리를 말한다.

<img src="C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20210407194438739.png" alt="image-20210407194438739" style="zoom:70%;" />

**Range Scan <-> Full Table Scan**

**참조**

- https://hyungjoon6876.github.io/jlog/2018/07/20/btree.html



#### 인덱스를 언제 쓰는게 좋을까?

**SELECT**를 사용할 때는 좋으나 나머지 insert, update, delete에서는 오히려 성능을 저하 시킬수 있다.

**INSERT는 왜 성능을 저하시킬까?**

- 인덱스는 정렬이 된 상태로 저장이 되어야 하기 때문이다. 만약 예를 들어, 어떤 데이터 중간에 Index를 정렬해야 한다면 원래 있던 데이터들을 뒤로 쭉쭉 변경하여 정렬해야하기 때문에 성능에 저하가 있다. 또한, Index는 테이블과 별도의 객체라서 테이블에도 삽입하고 Index에도 삽입해주어야한다.

**DELETE는 왜 성능을 저하시킬까?**

- 실제로 데이터를 지우는게 아니라 Index안에는 사용안함이라는 것으로 표시해 주기 때문에 공간 낭비가 있다. 

**UPDATE는 왜 성능을 저하시킬까?**

- Index에는 update라는 개념이 없다. 그래서 Index에서는 DELETE를 하고 INSERT로 작업을 해주기 때문에 부하가 크게 걸린다.



#### 인덱스 Column 설정 기준

- Cardinality(기수성)가 높은 것으로 인덱스 Column 설정 기준으로 할 수 있다.
  - Cardinality : 농도, the number of elements in a set or group
  - 성별, 팀이름, 닉네임, 주민번호가 있으면 주민번호는 모두 다르기 때문에 Cardinality가 가장 높다고 표현할 수 있다.
  - 종류의 수가 가장 많은 것?
  - 여러 컬럼으로 인덱스를 잡는다면 **카디널리티가 높은순에서 낮은순으로 (`group_no, from_date, is_bonus`) 구성하는게 더 성능이 뛰어**나다.



#### 참조

- https://jojoldu.tistory.com/243

