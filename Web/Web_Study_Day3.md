# Day3 Web(HTML & CSS)

```
HTML 1.0 -> HTML 2.0 -> HTML 3.2 -> HTML 4.0 -> HTML 4.01 -> HTML 5
											XHTML 1.0 -> HTML보다 조금 더 엄격함 
											e.g) 대소문자 구분, 닫는 꺽쇠괄호 앞에 꼭 꺽쇠괄호줘야함
```

#### 실습 1 exam8

```html
<!--실습1 exam8-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<!-- 꺽쇠<> 기호를 사용하고자 한다면 
	 &lt;&gt;-->
<h1>HTML에서의 공백과 &lt;개행&gt;</h1>
<hr>

<!-- &nbsp; blank(띄어쓰기)로 인식!! -->
오늘은 화&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;요일입니다.<br/><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;날씨가 맑습니다.
</body>
</html>	
```

## CSS(Cascading Style Sheets) 란?

구조적으로 짜여짂 문서(HTML,XML)에 Style(글자,여백,레이아웃)을 적용하기 위해 사용 하는 언어(Language)이다.

- CSS 스타일시트는 HTML 문서의 요소에 적용되는 CSS 스타일 정의를 포함하며 CSS
- 스타일은 요소 표시 방법 및 페이지에서의 요소 위치를 지정한다.
- W3C의 표준이며 HTML구조는 그대로 두고 CSS 파일만 변경해도 젂혀 다른 웹사이트처럼 꾸밀 수 있다.

#### CSS(Cascading Style Sheets) 사용한 웹 페이지 개발

- 웹 표준에 기반핚 웹 사이트를 개발할 수 있다. (페이지의 내용과 디자읶을 분리)
- 클라이언트 기기에 알맞는 반응형 웹 페이지를 개발 할 수 있다.
- 이미지의 사용을 최소화시켜 가벼운 웹 페이지 개발을 가능하게 한다.

#### CSS 사용의 이점

- 확장성 : 표현을 더욱 다양하게 확장하거나 표현 기능의 변경 가능
- 편의성 : 훨씬 간편하게 레이아웃 등의 스타일 구성
- 재사용성 : 독립된 스타일 모듈 작성, 여러 HTML 문서에 공통으로 홗용
- 생산성 : 역할 분담에 따른 전문화, 모듈 단위의 협업과 생산성의 향상

#### CSS 의 작성 방법

- 인라인 방법 - HTML 엘리먼트에 style 이라는 속성으로 정의하는 방법
  <tag style="property: value">

- 전역적 방법 - <style> 이라는 태그에 웹 페이지의 태그들에 대핚 스타읷을 정의하는 방법

  ```html
  <style type="text/css">
  selector {property: value;}
  </style>
  ```

- 외부 파일 연결 방법 - 독릱된 파읷(확장자 .css)을 릶들어서 HTML 문서에 연결하는 방법

  ```html
  <link rel="stylesheet" type="text/css" href="style.css" />
  ```

#### CSS 실습1 exam1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
</head>
<body>
<h1>CSS로 무엇을 할 수 있을까?</h1>
<hr>
<!--인라인 방법 -->
<h2 style="color:green">둘리</h2>
<h2>또치</h2>
<h2 style="color:#ff0000; background-color:yellow">도우너</h2>
<!-- red = #ff0000 = #f00(두개가 같으면 하나로 줄여서 사용가능) = rgb(255, 0, 0) -->
<h2>희동이</h2>
</body>
</html>
```

#### CSS 실습2 exam2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
</head>
<body>
<h1>CSS 선택자 학습</h1>
<hr>
<!-- url 쓸때 마지막에 /쓰면 속도가 더 빠르다 -->
<!-- style="text-decoration:none" 이걸 사용하면 화면에 보여줄때 underline이 없어진다. -->
<a href="http://www.w3schools.com/"style="text-decoration:none">W3Schools</a><br>
<a href="http://www.html5test.com/">HTML5테스트</a><br>
<a href="http://www.caniuse.com">HTML과 CSS의 지원여부 체크</a>ㅋㅋㅋ<br>
<img src="../images/totoro.png"width="200"> <!-- 상대 URL -->
<img src="/edu/images/totoro.png"width="200"> <!-- 상대 URL -->
<img src="http://localhost:8000/edu/images/totoro.png"width="200"> <!-- 절대 URL -->

</body>
</html>
```

#### CSS 실습3 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
<!--마지막에는 세미콜론을 생략할수 있다.-->
<!-- 전역처리 -->
<!--hover : 유사선택자 -->
<!-- #t1 : t1인 id선택자를 찾아서 -->
<style>
	a{
		text-decoration : none
	}
	#t1:hover{
		font-weight : bold;
		color : red;
	}
	.t2:hover{
		opacity : 0.3;/*0.0(완전투명) ~ 1.0(완전불투명)*/
	}
	h1,a{
		border : 1px solid blue;
	}
	span{
		color : #0066cc;
	}
</style>
</head>
<body>
<h1>CSS 선택자 <span>학습</span></h1>
<hr>
<!-- url 쓸때 마지막에 /쓰면 속도가 더 빠르다 -->
<!-- style="text-decoration:none" 이걸 사용하면 화면에 보여줄때 underline이 없어진다. -->
<a href="http://www.w3schools.com/">W3Schools</a><br>
<a href="http://www.html5test.com/">HTML5테스트</a><br>
<a href="http://www.caniuse.com">HTML과 CSS의 지원여부 체크</a>ㅋㅋㅋ<br>
<img src="../images/totoro.png"width="200" class="t2"> <!-- 상대 URL -->
<img src="/edu/images/totoro.png"width="200" class="t2"> <!-- 상대 URL -->
<img src="http://localhost:8000/edu/images/totoro.png"width="200"> <!-- 절대 URL -->

</body>
</html>
```

[전역적인 스타일 설정]

- \<head\> 태그안에 \<style> 태그를 사용한다.

- CSS 정의 방법

  ​	CSS선택자{

  ​		CSS속성명 : 속성값;

  ​		CSS속성명 : 속성값;

  ​		CSS속성명 : 속성값;

  ​		CSS속성명 : 속성값 <!-- 마지막에는 세미콜론을 안줘도 되지만 그냥 통일하는게 좋다! 실수를 줄일수 있다. --> 

  ​	}

[ CSS 선택자 ]

- 전체 선택자
- 태그 선택자
- class 선택자
- ID 선택자
- 자식 선택자
- 자손 선택자
- 첫번째 동생 선택자
- 동생들 선택자
- 속성 선택자

-> css-cheat-sheet에서 소개를 하고 있음.

![image-20200104111919032](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200104111919032.png)

![image-20200104112253673](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200104112253673.png)

text-decoration : none | underline | overline | line-through(취소선) | blink(지원하는 브라우저 없음)

class : 태그에 부여된 추가적인 sub이름, 여러태그에 공통으로 가져갈수 있다.

id : unique하게 이름을 부여할 때 사용, id가 중복되면 아무일도 일어나지 않는다.

![image-20200104112907980](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200104112907980.png)

- 

  CSS를 다르게 적용하려는 태그(들) 또는 태그의 컨텐트에 정의하는 용도의 태그들

  \<div\> : 여러 태그들을 묶거나 또는 태그에 대하여 CSS 속성을 적용할 때

  \<span\> : 컨텐트의 일부분에 대하여 CSS 속성을 적용할 때

#### CSS 실습3_0 exam3_0

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
<style>
	div{
		background-color : lime;
		margin : 5px;
	}
	span{
		background-color : pink;
		margin : 5px;
	}
</style>
</head>
<body>
<h1>블럭 스타일 태그와 인라인 스타일 태그</h1>
<hr>
<!-- html4.0까지만 해도 엄청나게 많이 사용되었다. page layout 나누는 작업을 할 때 필요했었다.지금은 사용 안함 -->
<!-- Layout을 같은 스타일로 묶을때는 여전히 사용 -->
<div>가나다라마바사아</div>
<div>01012345678</div>
<div>abcdefghij</div>
<hr>
<!-- html으로만 사용할 거면 sapn 태그는 사용할 필요가 없다. -->
<span>가나다라마바사아</span>
<span>01012345678</span>
<span>abcdefghij</span>
</body>
</html>
```



#### CSS 실습4 exam4

블럭 스타일 태그 : 처음 부터 끝까지 블럭이 적용됨

인라인 스타일 태그 : 해당 문자에만 블럭이 적용됨

```html
<!--실습4 exam4-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
</head>
<body>
<h1>블럭 스타일 태그와 인라인 스타일 태그</h1>
<hr>
<div>가나다라마바사아</div>
<div>01012345678</div>
<div>abcdefghij</div>
<hr>
<span>가나다라마바사아</span>
<span>01012345678</span>
<span>abcdefghij</span>
</body>
</html>
```

#### 실습5 exam5

