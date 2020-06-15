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





-----

새로운 프로젝트 생성 !!!

`jango-admin startproject crud`

`cd crud`

`python manage.py startapp articles`

settings.py에서 추가!!!!!!

INSTALLED_APPS = [

  'articles',

---

| id   | title | content | created_at | updated_at |
| ---- | ----- | ------- | ---------- | ---------- |
| 1    |       |         |            |            |
| 2    |       |         |            |            |
| 3    |       |         |            |            |
| 4    |       |         |            |            |
| 5    |       |         |            |            |

---

#### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length는 필수 인자
- 텍스트 양이 많을 경우 -> TextField()를 사용



### models.DateTimeField

#### auto_now_add

- 최초 생성 일자	
- django ORM이 최초 INSERT시에만 현재날짜와 시간으로 갱신

#### auto_now

- 최종 수정 일자
- django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

---

#### Model 작성 3단계

1. **models.py 작성**
2. **makemigrations(설계도 작성)**
3. **migrate(db 작성, 구축)**

`python manage.py makemigrations` --> migrations파일안에 0001_initial.py가 생성된다.

---> 설계도를 만들어서 SQL로 해석 해준다.

`python manage.py sqlmigrate articles 0001` --> migrations가 여기서 출력되는 것으로 해석이 되어서 내보내줄것이다.

- `python manage.py sqlmigrate 앱네임 마이그레이션_number`'
- 해당 migarations가 어떻게 SQL문으로 해석되어 동작할지 미리 확인 할 수 있다.

`python manage.py migrate` --> 최종적으로 데이터베이스를 구축하는 명령어

![image](https://user-images.githubusercontent.com/55625864/84612917-f98d4c80-aefc-11ea-8d15-0e8ad2715efe.png)



---

visual studio code 에서 SQLite 설치

-> ctrl + shift + p
-> SQLite:Open database

->db.sqlite3까지 하면!!!!!!

SQLITE EXPLORER이 생성되고 그 안에 테이블이 생성된다.



## 파이썬 Shell programming

### -----순서대로 보면 됩니다 CRUD 나오기 전까지 CRUD 설명이랑 같이 보면 Good-----

#### cmd 창에서 python prompt 사용하기

`python -i`

 

#### ipython 설치하기

`pip install ipython`

#### ipython 확장 설치

`pip install django-extensions`

[INSTALLED_APPS 에 등록](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)

#### 장고 확장 설치 한 다음에 사용!!

`python manage.py shell_plus` : 모든 import해야할 것들을 다 import 해주고있음!!

`Article.objects.all()`

![image](https://user-images.githubusercontent.com/55625864/84618375-fc903900-af0c-11ea-87bf-a875cba8c2e2.png)

- objects가 ORM에 관련된 메서드를 제공해줌.
- `dir(Article.objects)` : 모든 메서드들을 확인할 수 있음

![image](https://user-images.githubusercontent.com/55625864/84618946-a3290980-af0e-11ea-9df0-8d608f1b1d8f.png)

-------------------> 클래스 인스턴스를 만들어서 테이블에 저장!!

`Article.objects.all()` 하면 이제 object가 들어가있음

![image-20200615135001854](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200615135001854.png)

![image](https://user-images.githubusercontent.com/55625864/84619289-9f49b700-af0f-11ea-88f8-f1670cd45256.png)

우선 tzinfo는 모든 전세계를 기준으로 하기 때문에 UTC로 되어있지만 우리가  TIME_ZONE = 'Asia/Seoul'이라고 했으니 실제 해석을 내가 한걸로 변경해서 해준다.

![image](https://user-images.githubusercontent.com/55625864/84620265-7ecf2c00-af12-11ea-8875-e5761df56991.png)

이렇게 하면 바로 Table에 적용된다.

![image](https://user-images.githubusercontent.com/55625864/84620621-73c8cb80-af13-11ea-883d-546bd648eb06.png)

조회할 때는 pk를 이용해서 한다.

![image](https://user-images.githubusercontent.com/55625864/84620899-2b5ddd80-af14-11ea-8045-48a90a51ebb0.png)

filter의 특성은 없으면 에러가 나진 않지만 빈 QuerySet이 나온다.

![image-20200615142739457](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200615142739457.png)

title이 같으면 이렇게 여러개가 나올수 있으면 무조건 filter는 QuerySet이 나오게 된다.

- 역순 출력

  ![image](https://user-images.githubusercontent.com/55625864/84621063-960f1900-af14-11ea-9712-7418254fd517.png)



__는 ............



![image](https://user-images.githubusercontent.com/55625864/84621175-d8385a80-af14-11ea-8439-47c80dd5d155.png)

fi가 있는 것들을 찾음

![image](https://user-images.githubusercontent.com/55625864/84621208-f30acf00-af14-11ea-932d-27824fd01b8e.png)

첫번째가 fi로 시작하는 것들을 찾음

![image-20200615143254561](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200615143254561.png)

content에서 !로 끝나는 것들을 찾음

구글에서 django orm을 검색해서 -->https://docs.djangoproject.com/en/3.0/ref/models/querysets/#contains

이곳으로 찾아서 orm 문서를 확인 할 수 있다.



![image](https://user-images.githubusercontent.com/55625864/84621952-d40d3c80-af16-11ea-818d-0d7381a672c1.png)

↑↑↑↑↑↑이렇게 **수정**할 수 있음!!↑↑↑↑↑↑

![image](https://user-images.githubusercontent.com/55625864/84621919-be981280-af16-11ea-9ad1-1dd1ac5bd01e.png)

↑↑↑↑↑↑이렇게 **삭제**할 수 있음!!↑↑↑↑↑↑



새로 Table을 만들면 pk=1은 다시는 살아오지 못한다.

![image-20200615144708856](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200615144708856.png)

맨 뒤로 생성된다.



#### CRUD

#### CREATE

```python
# 1
article = Article()
article.title = 'first'
article.content = 'content'
article.save() # save를 호출해야 DB에 저장된다.

# 2
article = Article(title='second', content='django!!')
article.save() # save를 호출해야 DB에 저장된다.

# 3
Ariticle.objects.create(title='third', content='django!!')
```

SQL문을 ORM으로 대체하는것임.

#### READ

```python
# 모든 객체 조회
Articles.objects.all()

# 특정 객체 조회
Articles.objects.get(pk=1)

# 특정 조건 객체 가져오기
Article.objects.filter(title='first')
Article.objects.filter(title='first', content='django!')

# 내림차순
Article.objects.order_by('-pk') # pk아니고 다른 column써도 된다.

# LIKE
Article.objects.filter(title__contain='fi') # title중에 fi가 포함된것 검색
Article.objects.filter(title__startswith='fi') # fi로 시작하는 것 검색
Article.objects.filter(content__endswith='!') # content에서 !로 끝나는 것 검색

```

- .get()을 사용할 때 해당 객체가 없으면 DoesNotExist 에러가 발생.
- 여러개일 경우에 MultipleObjectReturned 에러가 발생.
- 이와 같은 특징 때문에 unique한 속성을 가지고 있는 데이터에 사용해야 한다.

#### UPDATE

```python
article = Article.objects.get(pk=1)
article.title = 'edit title'
article.save()
```

#### DELETE

```python
article = Article.objects.get(pk=1)
article.delete()
```



#### objects

- models.py에 작성한 클래스를 불러와서 사용할 때 DB와의 인터페이스 역할을 하는 manager
- Python class(python) --------- objects --------- DB(SQL)

---

#### QuerySet

- objects 매니저를 사용하여 복수의 데이터를 가져오는 함수를 사용할 때 반환되는객체 타입
- 단일 객체는 Query(class의 인스턴스로 반환)
- query(질문)를 DB에게 보내서 글을 조회하거나 생성, 수정, 삭제
- query를 보내는 언어를 활용해서 DB에게 데이터에 대한 조작 실행



#### Admin 계정

`python manage.py createsuperuser`

![image](https://user-images.githubusercontent.com/55625864/84623659-b346e600-af1a-11ea-813f-f7c2c66b7ad4.png)

![image](https://user-images.githubusercontent.com/55625864/84623735-db364980-af1a-11ea-824e-1bc24de0a096.png)

비밀번호는 SHA 알고리즘을 사용해서 저장한다. 장고가 자동으로

`python manage.py runserver` 를 시작하고 admin 페이지로 이동한다.

![image](https://user-images.githubusercontent.com/55625864/84623929-50098380-af1b-11ea-904f-c2bc9f3acbb6.png)

admin만 사용자가 등록되어 있는것을 호가인할 수 있다.



#### admin.py에 추가

```
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
# admin site에 등록(register) 하겠다.
```

- **계정 또한 데이터이기 때문에 반드시 migrate 작업 후에 관리자 계정을 생성해야한다.(실수 많이 함) 반드시 테이블을 만들고 해야한다.**

#### admin 작성 순서

1. python manage.py createsuperuser
2. admin.py 작성



**django는 기본적으로 app_name/templates만 알고 있다.**

​    								  **app_name/static**만 알고있다.



