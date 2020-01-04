# W3 CSS exercise 

###### 텍스트 색상을 설정하는 **color**

*color:{색상}*

~~~css
body{color : red;}
~~~

~~~css
a {color: royalblue;}
a.hover {color: red;}
~~~

*color* 속성 값으로는 Hex 코드 뿐만 아니라 RGB 코드를 입력할 수도 있습니다. 이름을 직접 입력하거나 ***#NNNNNN*** 으로 표현할 수 있다.



###### 텍스트의 두께를 설정하는 font-weight

~~~css
/* 굵게 (700) */
.bold { font-weight : bold;}

/* 기본 (400) */
.bold { font-weight : normal;}

/* 가장굵게 (900) */
.bold { font-weight : bolder;}

~~~

:hover에서 가장 많이 사용된다.



###### 텍스트의 꾸밈을 설정하는 text-decoration

~~~css
a{
  color: red;
  text-decoration: none;
}
~~~

~~~css
a{
  color: #;
  text-decoration : none;
}
a:hover{
  text-decoration: underline; /*밑줄*/
}
~~~

마우스 커서를 올려놓았을 때 링크 텍스트 색상까지 바꾸고 싶다면 *color* 속성을 추가하면 된다.



###### 텍스트의 기울임을 설정하는 font-style

* italic - 필기체
* oblique  - 텍스트만 기울여진

~~~css
.italic {font-style: italicl;} 
~~~



###### 글씨체를 설정하는 font-family

font-family 속성을 이용할 때 주의해야 하는 점은 띄어쓰기가 있는 폰트명을 입력할 때에는 큰 따옴표를 사용해야 한다는 점이다. 

~~~css
body {font-family: "Gothic";}
~~~





###### 텍스트 및 블록 외부의 선을 설정하는 border

* border-width
* border-style
* border-color
* border 테두리
  * border-top (지정된 위치에만 선을 만들어주는 속성)
  * border-right                           / /
  * border-bottom
  * Border-left

~~~css
border:{font-width}{font-style}{font-color}
~~~

* solid: 일반적인 선

- dashed: 일반적인 점선
- dotted: dashed 스타일보다 좁은 점선
- double: 두 줄로 구성된 선, 3px 이상의 굵기부터 표현됨
- groove: 그림자가 적용된 선 (움푹 파인 그림자)
- inset: 안쪽으로 들어간 느낌의 그림자가 적용된 선
- outset: 바깥으로 나온 느낌의 그림자가 적용된 선
- ridge: 튀어나온 느낌의 선, 2px 이상의 굵기부터 표현됨



~~~css
.comment {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f6f6f6;
    color: #666;
    font-size: 12px;
}
  
.comment.red {
    border-color: #eed3d7;
    color: #b94a48;
    background-color: #f2dede;
 
#footnote {
    border-top: 3px solid #ccc;
    padding-top: 10px;
    margin-top: 20px;
    font-size: 11px;
    color: #aaa
~~~

~~~css
a {
    color: #b94a48;
    text-decoration: none;
}
a:hover {
    border-bottom: 1px dashed #b94a48;
}
~~~



###### HTML 요소의 배경 스타일을 설정하는 background

- background-color: 배경색 지정
- background-image: 배경 이미지 지정
- background-position-x: 배경 이미지의 가로 위치 지정 (백분율, px 단위 사용)
- background-position-y: 배경 이미지의 세로 위치 지정 (백분율, px 단위 사용)
- background-repeat-x: 배경 이미지의 가로 반복 여부 지정
- background-repeat-y: 배경 이미지의 세로 반복 여부 지정

~~~css
.cash {
    background: url(./image/pooh.gif) no-repeat 50% 50%
}
  
.cahs {
    background-image: url(./pooh.gif);
    background-repeat: no-repeat;
    background-position: 50% 50%;
~~~



css속성은 정말 많다. 

To Be Continued