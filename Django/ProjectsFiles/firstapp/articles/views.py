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
    reverse = text[::-1] # 역순으로 !! 회문에서 사용!
    if text == reverse: 
        result = True
    else:
        result = False
    context = {
        'text': text,
        'result': result,
    }
    
    return render(request, 'palindrome.html', context)


