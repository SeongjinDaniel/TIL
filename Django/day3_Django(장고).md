# day3 Django



ascii artii --- 구글 검색

ascii artii api --- 구글 검색

---

python split --- 구글 검색

[python split](https://docs.python.org/ko/3.7/library/stdtypes.html) 



- 두번째 app이 생성..
- 하나의 urls.py에서 모든 path를 관리하기가 어려워짐.

1. URL 로직 분리
   - 기존 url이 바뀌어 버려서 지금까지 작성한 모든 url을 다시 손봐줘야 됨.ex) artilces/lotto_catch
   - 그건 어려우니 그냥 url에 이름을 만들자.
2. URL NAME
   - 그런데 두개의 앱의 url 이름이 같다면,,,?
   - 어떤 앱의 url 이름인지 app_name을 설정하자.
3. URL Namespace

----

- 분명히 두번째 app의 index 주소로 요청을 보냈는데, 템플릿은 계속 첫번째 app의 index.html을 보여준다.

1. Django Namespace
   - app_name/templates 이후에 app_name 폴더를 하나 더 둠으로써 이름 공간을 생성한다.

---

- 여러 페이지에 동일한 구조를 적용 시키고 싶다.
- 템플릿의 재사용성에 초점.

1. Template Inheritance
2. static

django는 기본적으로 templates를

app_name/templates에서 찾는다.



django는 기본적으로 static도 app_name/static에서 찾는다.



firstapp/templates/까지도 찾을 수 있게 되었다.



**static**

- 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어, 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주는 파일.(정적 파일)
- 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 응답해주면 되는 것.



### `url`[¶](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#url)

```
{% url 'some-url-name' v1 v2 %}
```

```
{% url 'some-url-name' arg1=v1 arg2=v2 %}
```

```
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```
path('clients/', include('project_name.app_name.urls'))
```

```
{% url 'app-views-client' client.id %}
```

```
{% url 'some-url-name' arg arg2 as the_url %}

<a href="{{ the_url }}">I'm linking to {{ the_url }}</a>
```

```
{% url 'some-url-name' as the_url %}
{% if the_url %}
  <a href="{{ the_url }}">Link to optional stuff</a>
{% endif %}
```

```
{% url 'myapp:view-name' %}
```



## 폴더 구조 변경

app_name/

​	static/

​		app_name/    <-- namespace 분리 역할

​			stylesheets/

​				...,css

​			images/

​				sool.png

---

### 상속

구글에 **django template inheritance** 검색

https://docs.djangoproject.com/en/3.0/ref/templates/language/#template-inheritance

 