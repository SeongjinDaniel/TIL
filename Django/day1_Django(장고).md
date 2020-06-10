# Django(장고)

##### 설치 방법

해당 리포지토리에서 git bash를 켠다.

그후 

`pip install django==2.1.15` 

`pip install django` --> 최신버전 설치됨

설치가 완료되면

`django-admin startproject firstapp`

`ls`

`cd firstapp`   `ls` --> manage.py가 생성된다.

 `python manage.py runserver` -- git bash에서 안되면 vs code 터미널에서 실행!!

http://127.0.0.1:8000/ -----> 위 명령어를 실행후 이것을 클릭하고 congratulations! 문구가 나오는 로켓이 나오면 Success!!!!!!



**프로젝트명 주의**

django, test, class -----> 이미 있을 법한 예약어로 프로젝트 이름을 만들면 안된다.

django-test 하이픈 섞어서도 사용하면 안된다.

djangoTest는 가능!!

-------

**\_\_init\_\_.py**

존재하는 디렉토리들을 패키지화한다.

```
from firstapp import urls
```

**settings.py**

모든 설정을 하는 곳이다!

![image](https://user-images.githubusercontent.com/55625864/84215891-b5680980-ab02-11ea-829c-32a648ad519d.png)

------



#### 어플리케이션 만드는 방법

`python manage.py startapp '어플리케이션이름(현재는 articles)'` 어플리케이션 이름은 복수형으로

- **처음에 프로젝트 만들때는 이 명령어를 사용해야한다.**

  `django-admin startproject firstapp` 

`python manage.py` 하나의 프로젝트는 여러 앱을 가지게 된다. 

django 프로젝트는 app들의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역할.

app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적.

작은 규모의 서비스에서는 세부적으로 나누지는 않는다.

app 이름은 복수형으로 하는 것이 권장된다. 

`python manage.py startapp articles`

**admin.py**

관리자용 페이지를 customizing하는 곳이다.

**apps.py**

앱의 정보가 들어있는 곳이고 **절대** 수정하지 않을 것이다.

**test.py**

test 코드를 사용하는 곳이다.

**views.py**

view들이 정의되는 곳이고 다양한 함수들을 사용할 예정이다.



1. django 프로젝트 생성

2. app 생성

3. 프로젝트 app 등록 (settings.py)

   **앞으로 코드작성 순서(== 요청의 흐름)**

4. urls.py 작성

5. views.py 작성

6. templates 작성

### setting.py

articles 추가!! 

```python
INSTALLED_APPS = [
    # 1. local apps
    'articles'
    # 2. 3rd party app
    # 3. django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- **trailing comma** 

  어차피 요소 뒤쪽에 추가할 예정이니까 써놓은 것이다!!

  일반적인 python에서는 안된다. django위에서는 가능!!

수정할것!! ↓↓↓↓↓↓↓↓↓↓↓↓

```
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```





#### urls.py

수정 및 추가↓↓↓↓↓↓↓↓↓

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views),
]

```

TypeError: view must be a callable or a list/tuple in the case of include(). --> 이런 에러가 뜰것이다 views.py에 어떠한 코드도 작성하지 않았기 때문이다.



**반드시 articles 안에 폴더를 만들때 `templates`로 만들어야한다.**

![image](https://user-images.githubusercontent.com/55625864/84217408-0679fc80-ab07-11ea-80a6-1faabd047390.png)





--------

**django --> Extension 설치!!**



\# django import style guide

\# 1. standard library

\# 2. 3rd party library

\# 3. django

\# 4. local django

```python
import random

from django.shortcuts import render
```



#### 어!! emmet이 안되네요!!!!!!!!! -- 해결법

**ctrl + shift + p**

json -> Open Settings (JSON)에 들어간다.

django extension에 써져 있는 것들을 추가해야한다.!

```
"files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
},
"emmet.includeLanguages": {"django-html": "html"},
```



#### Variable Routing

1. 자기소개 페이지 (이름, 나이)
2. 수 2개를 받아서 곱셈 결과를 보여주는 페이지



#### emmet cheat sheet

구글 검색 emmet cheat sheet !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





#### django built in tag를 구글에서 검색하면 다 서칭해서 볼수있다.

[django built in tag](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference)

**주석**

주석 쓸때 html dtl 따로 해야하지만 한번에 가능하다

#### `comment`[¶](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#comment)

Ignores everything between `{% comment %}` and `{% endcomment %}`. An optional note may be inserted in the first tag. For example, this is useful when commenting out code for documenting why the code was disabled.

Sample usage: --------전체 주석 태그하는법 ----

```html
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

`comment` tags cannot be nested.



#### DTL(*Django Template* Language)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>1. 반복문</h3>
    {# 사용자에게 보여주지 않는 로직은 {%%}를 사용한다. endfor를 반드시 해주어야한다.#}
    
    {% for food  in foods %}
        <p>{{ food }}</p>
    {% endfor %}

    {% for food in foods %}
        <p>{{ forloop.counter }} {{ food }}</p>
    {% endfor %}

    {% for element in empty_list %}
        <p>{{ element }}</p>
    {% empty %}
        <p>지금 아무것도 없네요...</p>
    {% endfor %}

    <h3>2. 조건문</h3>
    {% if '짜장면' in foods %}
        <p>짜장면 역시 또자강!!</p>
    {% endif %}

    
    {% for food in foods %}
        {% if forloop.first %}
            <p>짜장면엔 고추가루지!!</p>
        {% else %}
            <p>{{ food }}</p>
        {% endif %}
    {% endfor %}

    <h3>3. length filter</h3>
    {% for food in foods %}
        {% if food|length > 2 %}
            <p>메뉴 이름이 너무 길어요</p>
        {% else %}
            <p>{{ food }}, {{ food|length }}</p>
        {% endif %}

    {% endfor %}

    <h3>4. lorem ipsum</h3>
    <p>{% lorem %}</p> {# 이미 정의된 함수 호출이기 때문에 {%%}를 사용한다. #}
    <hr>
    {% lorem 3 w %}
    <hr>
    {% lorem 4 w random %}
    <hr>

    <h3>5. 글자수 제한 filter</h3>
    <p>{{ messages|truncatewords:3 }}</p> {# 끝을 워드 단위로 자른다.#}
    <p>{{ messages|truncatechars:3 }}</p>
    <p>{{ messages|truncatechars:10 }}</p> {#...이 무조건 나옴#}
</body>
</html>
```





##### django mathfilters

존재하지만 사용하지 않는다.

view에서 template으로 할일을 넘기면 안된다.



#### 실습 회문 판별

- variable routing
- 회문일때랑 아닐때 다르게 출력 되도록

##### urls.py

```python
"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # views.index -> views안에 index:  함수이름
    path('dinner/', views.dinner),
    path('pictures/', views.pictures),
    path('hello/<str:name>/', views.hello),
    # str 타입은 기본값이라서 생략 가능
    # path('hello/<name>/', views.hello)
    path('introduce/<name>/<int:age>/', views.introduce),
    path('multi/<int:num1>/<int:num2>/', views.multi),
    # url에서는 _안쓰는게 좋다 인식 못함!
    path('dtl-practice/', views.dtl_practice), # 혼합형 할 때 _쓰는것을 snake case라고 한다.
    path('palindrome/<text>/', views.palindrome),
]
```

##### views.py

```python
# django import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django

import random
from datetime import datetime # 공교롭게도 라이브러리 이름과 패키지 이름이 똑같다
from django.shortcuts import render


# Create your views here.

# 필수 인자로 request를 사용한다.
def index(request):
    # 2번째는 template 주소를 쓸것임 # 3번째인자부터는 선택인자다
    # django가 templates까지는 알고있음 - django는 app안에 templates가 있는지
    # 이미 알고 있으니까 templates를 안써도된다.
    # return render(request, './templates/index.html') 
    return render(request, 'index.html')


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    # 3번째 인자는 dictionary형식으로 보낸다.
    # 왼쪽 pick이 html에서 사용할 pick
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)
    
def pictures(request):
    image_url = 'https://picsum.photos/200/300.jpg'
    context = {
        'image_url' : image_url
    }
    return render(request, 'pitures.html', context)

def hello(request, name): # url 변수명을 인자로 사용하면 받을수있음
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'introduce.html', context)

def multi(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'multi.html', context)


def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, You need Python'
    datetime_now = datetime.now()
    context = {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'dtl_practice.html', context)


def palindrome(request, text):
    textTemp = text[::-1] # 역순으로 !! 회문에서 사용!
    if text == textTemp: 
        result = 'True'
    else:
        result = 'False'
    context = {
        'text': text,
        'result': result,
    }
    
    return render(request, 'palindrome.html', context)

```

##### palindrome.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회문 실습</title>
</head>
<body>
    {% if 'True' in result %}
        <h1>{{ text }}는 회문입니다. </h1>
    {% else %}
        <h1>{{ text }}는 회문이 아닙니다. </h1>
    {% endif %}
 
</body>
</html>
```

