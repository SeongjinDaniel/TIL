# 파이썬

- 파이썬 사이트에서 다운로드!!

  - [Python 3.7.6 - Dec. 18, 2019](https://www.python.org/downloads/release/python-376/)

    Download [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe)



1. Add Python 3.7 to PATH 를 무조건 체크하고 install Now를 클릭해서 다운로드를 받는다.

2. Disable Path ~~~ 클릭!!ㄱㄱ

##### 00_data_type.py

```python
print('Hello, World')

number = 10
string = '문자열'
bools = True

print(number, string, bools)

# 주석

# 숫자형 (int, float, complex)
a = 3
print(type(a))

# bool
print(type(False))

# 0, 0.0, (), [], {}, '', None -> 얘네는 False

# 문자형
greeting = 'hi'
name = 'harry'
print(greeting, name)
print(type(name))

# 사용자의 입력을 받음
# age = input()
# 사용자의 모든 입력 값은 string이어서 정수형을 쓰려면 변경해서 사용해야한다.
# print(type(age))

print("""
개행 문자 없이
여러줄을
그대로 출력 가능합니다.
""")

print(3 * 'hey' + ' yo!')

# string interpoltion

name = 'kim'
# 1. %-formatting
print('Hello, %s' % name)
# 2. .format()
print('Hello, {}'.format(name))
# 3. f-string (Literal String Interpolation) / 3.6+
print(f'Hello, {name}') # 소문자로 사용!!

pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2:.4}')


```

##### 01_operation.py

```python
# 논리 연산자
print('--- and ---')
print(True and True)
print(True and False)
print(True and False)
print(False and False)

# ctrl + d 단축키 : 하단으로 같은 단어들을 동시에 선택 할 수 있다.
print('--- or ---')
print(True or True)
print(True or False)
print(True or False)
print(False or False)

print('--- not ---')
print(not True)
print(not 0)

# 단축평가
# 첫번째 값이 확실할 때, 두번째 값은 확인하지 않음
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
print('--- 단축평가 ---')
vowels = 'aeiou'
print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True
print('a' and 'b') # 'b' 뒤에꺼 까지 봐야한다. a가 True라고 해서 뒤에께 True라는 보장이 없으니까

# and는 둘 다 True 경우만 True이기 때문에
# 첫번째 값이 True라도 두번째 값을 확인해야 한다.
print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

# true는 첫번째 true이면 뒤에꺼를 볼필요가 없다.
print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0

# Containment Test
# in 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.

print('--- in ---')
print('a' in 'apple')
print(1 in [1, 2, 3]) # 파이썬은 Array를 List라고 부른다.

```



## 시퀀스

- 데이터가 순서대로 나열된 형식
- 데이터에 순서(번호)를 붙여 나열한 것
- (주의!) 순서대로 나열된 것이 `정렬되었다` 라는 뜻은 아니다.
- 가변 시퀀스 - list
- 불변 시퀀스 - tuple, str, range

##### 범위 예제

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```

##### 02_sequence_data_type.py

```python
# 1. 리스트 (list)
my_list1 = [10, '문자열', True]
print(my_list1)
print(type(my_list1))
print(my_list1[1])

# 2. 튜플 (tuple) 
# 튜플은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없다.
# 직접 사용하기 보다는 파이썬 내부에서 사용하고 있다.
# list와는 다르게 요소의 수정이 불가능!!
my_tuple1 = (1, 2)
print(my_tuple1)
print(type(my_tuple1))

# 어떻게 파이썬 내부에서 사용하고 있을까?
my_tuple2 = 1, 2
print(my_tuple2)
print(type(my_tuple2))

x, y = 1, 2
print(x)
print(y)

x, y = y, x
print(x)
print(y)

# 하나의 요소로 구성된 튜프르은 값 뒤에 쉼표를 분여서 만든다.
single_tuple = ('hello',)
(1,)
print(type(single_tuple))
print(type((1,)))

# 3. range()
# range는 숫자의 시퀀스를 나타내기 위해 사용
print(type(range(1)))
print(range(10))
print(list(range(10)))

# list 만드는 방법
a = []
b = list()
```

##### 03_slcing.py

```python
# 파이썬에서는 변수명이나 함수명을 snake case를 사용한다.
sample_list = list(range(0, 31))
print(sample_list)
print(sample_list[1:3]) # : 이 슬라이싱!! 공간으로 자른다!
print(sample_list[10:-1]) # 끝에것만 제거 ! <---- -2, -1, 0   <----
print(sample_list[0 : len(sample_list) : 3])
print(sample_list[0::3]) # 위와 같음!
print(sample_list[::3]) # 위와 같음!

print(sample_list[::-1]) # 역순으로 !! 회문에서 사용!
print(sample_list[1:1]) # 아무것도 없음!! slcing을 어떻게 짜른지 생각하면 알수 있음!!
```



##### range()

- 숫자들의 시퀀스로 반복 할 필요가 있으면 사용하는 함수
- list나 tuple에 비해 범위의 크기에 무관하게 항상 같은 양의 메모리를 사용한다.
- (주의!) range가 돌려준 객체(iterable(반복가능한 객체))는 리스트인 것 같지만, 리스트가 아니다. 반복할 때 우너하는 시퀀스 항목들을 순서대로 돌려주는 객체이지만, 실제로 리스트를 만들지 않아서 공간을 절약하는 원리이다.

##### set

- 순서가 없는 자료구조
- 집합의 요소는 unique하다. 중복을 허용하지 않는다.
- 순서가 없으므로 set는 요소의 위치나 삽입 순서를 기록하지 않는다.
- 따라서 set는 인덱싱, 슬라이싱 또는 기타 시퀀스와 유사한 동작을 지원하지 않는다.
- 수학에서의 집합과 동일하게 처리된다.



##### dictionary

- 딕셔너리는 key와 value가 쌍으로 이루어져 있으며, 궁극의 자료구조라고 한다.

- key 중복이 되어선 안되며 중복되면 나중에 작성된 key 값으로 설정된다.
- key는 불변(immutable)한 모든 것이 가능.(str, int, float, boolean, tuple, range)
- list는 가변이기 때문에 dictionary `key`로 들어갈수 없음!!
- value는 list, dict를 포함한 모든 것이 가능하다.

## 데이터 타입

1. **시퀀스(ordered)**

- string
- list (가변)
- tuple
- range()

list 제외하고 모두 불변

2. **Unordered**

- set (가변)
- dictionary (가변) # key만 봤을 때는 불변!



##### 04_set_and_dictionary.py

```python
# 1. set 집합!!!!  순서없음!!
set_a = {1, 2, 3}
set_b = {3, 6, 9}

print(set_a - set_b) # 차집합
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

set_c = set() # 빈 set를 만들 때 {}를 사용하면 dict이기때문에 클래스 객체를 사용한다.(어쩔수 없이...)

# 중복 허용 x
set_temp = {1, 1, 1} # => {1}
print(set_temp)

# 2. dictionary   --> 궁극의 자료구조!!
dict_a = {} # 괄호를 사용해서 호출하면 훨씬더 메모리를 줄여서 사용할 수 있다.
print(type(dict_a))
dict_b = dict()
print(type(dict_b))
# key:value
dict_a = {1: 1, 2: 2, 3: 3, 1: 4} # key가 중복됨
print(dict_a)

# json 구조와 같다!
phone_book = {
    '서울': '02',
    '경기': '031',
    '대전': '042'
}
print(phone_book['서울'])

print(dir(dict)) # dir을 사용하면 어떤 함수를 사용할 수 있는지 알 수 있다.

# phone_book. 이렇게 치면 나오는 함수들을 확인 할 수 있다.
print(phone_book.values()) # dict_values(['02', '031', '042']) ---> 딱 값들만 나옴! 대괄호로 감싸져 있으니 list네!!! wow!
# dictionary는 만들때 그순서는 보장해주지만 set은 보장 x
# print(help(dict)) 
```



##### 05_if_statements.py

```python
x = 100

# 4 spaces - 파이썬에서 하나의 Style Guide
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

```



##### 06_while_statements.py

```python
# while 문은 조건식이 True인 경우 반복적으로 코드를 실행
# 조건식이 False 일 때까지 실행
# 그래서 종료조건을 반드시 설정해주어야 한다.

n = 0

while n < 3 :
    print(n)
    n = n + 1

a = ''
while a != '안녕': # a가 '안녕'일때까지 반복
    print('안녕이라고 할 때까지 물어볼꺼야...')
    a = input('말해봐 : ')
    
    
```



`enumerate`(*iterable*, *start=0*)

열거 객체를 돌려줍니다. *iterable* 은 시퀀스, [이터레이터](https://docs.python.org/ko/3.7/glossary.html#term-iterator) 또는 이터레이션을 지원하는 다른 객체여야 합니다. [`enumerate()`](https://docs.python.org/ko/3.7/library/functions.html?highlight=enumerate#enumerate) 에 의해 반환된 이터레이터의 [`__next__()`](https://docs.python.org/ko/3.7/library/stdtypes.html#iterator.__next__) 메서드는 카운트 (기본값 0을 갖는 *start* 부터)와 *iterable* 을 이터레이션 해서 얻어지는 값을 포함하는 튜플을 돌려줍니다.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```



##### 07_for_statements.py

```python
# for문은 정해진 범위 내 시퀀스(문자열, 튜플 리스트 같은)나
# 다른 반복가능한 객체(iterable)의 요소들을 순차적으로 실행합니다.

# 0, 1, 2, 3, 4
for num in [0, 1, 2, 3, 4]:
    print(num)

# 0~99
for num in range(100):
    print(num)

# 1~30중에 짝수인 것들
result = []
for num in range(1, 31):
    if num % 2 == 0:
        result.append(num)
print(result)

lunch = ['짜장면', '초밥', '탕수육']
for index,  menu in enumerate(lunch):
    print(index, menu)

print(enumerate(lunch))
print(type(enumerate(lunch)))
print(list(enumerate(lunch))) # list 내부는 tuple!!
print(type(list(enumerate(lunch))[0]))
```



##### 08_for_with_dict.py

```python
classroom = {
    'teacher': 'kim',
    'student1': 'hong',
    'student2': 'choi'
}

for member in classroom:
    print(member) # key가 나옴!!

for member in classroom:
    print(classroom[member]) # value 나옴!!
# ---> 이렇게 뽑지 않음
# ------------- 위는 권장 안함!!! --------------

# dict.values --> list 형태였음.
print('더 명확함----------')
# 더명확함!! keys
print('keys!!')
for member in classroom.keys():
    print(member) # key 나옴!!
# 더명확함!! values
print('values!!')
for member in classroom.values():
    print(member) # value 나옴!!
    print(type(member))

print('----------key, value-------------')
for key, value in classroom.items():
    print(key)
    print(value)
    print(type(key))
    print(type(value))

```



##### 09_list_comprehension.py

```python
my_list = []

for x in range(10):
    my_list.append(x ** 2)
print(my_list)

# my_newlist = my_list.append(x**2) for x in range(10)
# 
my_newlist = [x**2 for x in range(10)]
my_newlist2 = list(x**2 for x in range(10))
print(my_newlist)
print(my_newlist2)

# list comprehension with if statements

numbers = list(range(10, 100, 10))
print(numbers)

print('---------------------')
my_numbers_1 = []
for number in numbers:
    if number % 4 == 0:
        my_numbers_1.append(number)

my_numbers_1 = [number for number in numbers if number % 4 == 0]
print(my_numbers_1)

print('---------------------')
my_numbers_2 = []
for number in numbers:
    if number >= 50:
        my_numbers_1.append(number + 7)
    else:
        my_numbers_1.append(number + 5)

my_numbers_2 = [number + 7 if number >= 50 else number + 5 for number in numbers]
print(my_numbers_2)
# 조건 표현식
# true_value <if> 조건식 <else> false_value

gugu = []
for a in range(2, 10):
    for b in range(1, 10):
        gugu.append(a * b)
print(gugu)

gugu_2 = [a * b for a in range(2, 10) for b in range(1, 10)]
print(gugu_2)
```



## 리스트 커프리헨션

- 반복을 통해 리스트에 어떠한 것을 담는 경우 한줄로 줄여 쓰는것
- 단순히 반복문을 한 줄로 작성하는 것이 아님
- 시퀀스의 요소들 전부 또는 일부를 처리하고, 그 결과를 리스트로 돌려주는 간결한 방법

1. 간결함
2. 성능(일반화의 위험성)
3. 표현력(Pythonic)

리스트 컴프리헨션을 남용하면 안된다.



## 모듈 / 함수 / 라이브러리 (공적마스크 api)

내일 공부해봅시다!!!!!!!!!!



--------

##### 개념적

- python 자습서

- 코딩도장 파이썬 



-> 문법 : 프로그래머스 문제 풀이(조건, 반복)

-> 함수, 클래스 : 프레임워크(장고)

