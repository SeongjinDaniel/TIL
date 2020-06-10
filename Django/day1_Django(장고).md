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





