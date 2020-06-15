# day4_Django(장고)

#### SQLite

- MySQL 보다 가벼움
- 일반적으로 쓰기에도 충분한 관계형 데이터 베이스



#### 용어 정리

- scheme

  - 데이터베이스에서 자료의 구조, 표현방법, 관계등을을 정의한 구조

  - | column | dataType |
    | ------ | -------- |
    | id     | INT      |
    | age    | INT      |
    | phone  | TEXT     |

- table

  - 열(Column), 컬럼
  - 행(row), 레코드
  - PK (기본키)



#### SQL Keywords

- INSERT
- DELETE
- UPDATE
- SELECT
  - SELECT * FROM table
  - 테이블 조회



#### ORM

- OOP 프로그래밍(객체 지향 프로그래밍)에서  RDBMS를 연동할 때, 데이터 베이스와  OOP 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

#### 장점

- SQL문을 몰라도 DB 연동이 가능하다.
- SQL의 절차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 증가한다.



#### 단점

- ORM 만으로 완전한 서비스를 구현하는데에는 어렵다.



##### python 자습서 구글 검색

- https://docs.python.org/ko/3/tutorial/index.html  

- -> [목차에서 클래스 클릭](https://docs.python.org/ko/3/tutorial/classes.html)

- 파이썬에서는 생성자와 동일한 초기화 함수를 구현한다.(파이썬에서는 생성자라는 단어가 없음)

  ```python
  class Complex:
       def __init__(self, realpart, imagpart):
           self.r = realpart
           self.i = imagpart
  
  >>> x = Complex(3.0, -4.5)
  >>> x.r, x.i
  >>> (3.0, -4.5)
  ```



#### 클래스

- 객체를 표현하기 위한 문법
- 같은 종류의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 OOP 프로그램의 기본적인 데이터 타입

#### 인스턴스

- 클래스의 인스턴스/객체 (실제로 메모리상에 할당된 것)
- 인스턴스는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.
- 인스턴스의 행위는 클래스에 정의된 행위에 대한 메서드를 공유함으로써 메모리를 경제적으로 사용할 수 있다.

#### 속성(attribute)

- 클래스/인스턴스가 가지고 있는 속성(값)

#### 메서드(method)

- 클래스/인스턴스가 할 수 있는 행위(함수)



```python
# MyDogList (파스칼 케이스, upper 카멜 케이스)
# myDogList (카멜 케이스, lower 카멜 케이스
```



#### self

- 인스턴스 자기자신









