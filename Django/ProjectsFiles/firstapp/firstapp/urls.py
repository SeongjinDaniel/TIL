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
