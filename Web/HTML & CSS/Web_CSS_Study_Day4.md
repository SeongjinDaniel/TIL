# Day4 CSS

```html
Img[src]
Img[src=duke.png]
Img[src$=png]
```

![image-20200106094432024](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106094432024.png)

![image-20200106094700447](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106094700447.png)

![image-20200106103415230](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106103415230.png)

![image-20200106103428434](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106103428434.png)

#### 실습1 exam8

```html
<!-- 실습1 exam8 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
</head>
<body>
	<h1>레이아웃 나누기</h1>
	<!-- em 기울임 -->
	<em>오늘은 즐거운 월요일</em><br>
	<!-- strong 굵은 글씨 -->
	<strong>고르세용</strong><br>
	<!-- mark highlight -->
	<mark>먹고싶은거</mark>
	<ul>
		<li>메뉴1</li>
		<li>메뉴2</li>
		<li>메뉴3</li>
		<li>메뉴4</li>
	</ul>
	<h2>제목1</h2>
	<p>내용1</p>
	<h2>제목2</h2>
	<p>내용2</p>
	<h3>홈페이지 정보(바닥 글)</h3>	
</body>
</html>
```

**다음 트로이**를 검색해서 들어가면 핸드폰 Layout에서 확인이 가능하다!!

#### 실습2 exam8_1

```html
<!-- 실습2 exam8_1 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
<style>
	header {
		border : 1px dotted red;
	}
	footer {
		border : 1px dotted yellow;
	}
	section {
		border : 1px dotted blue;		
	}
	article {
		border : 1px dotted green;
	}
	nav {
		border : 1px dotted magenta;
	}
	aside {
		border : 1px dotted orange;
	}
</style>
</head>
<body>
	<header>
		<h1>레이아웃 나누기</h1>
		<em>오늘은 즐거운 월요일</em>
	</header>
	<nav>
		<strong>고르세용</strong><br>
		<mark>먹고싶은거</mark>
		<ul>
			<li>메뉴1</li>
			<li>메뉴2</li>
			<li>메뉴3</li>
			<li>메뉴4</li>
		</ul>
	</nav>
	<section>
		<article>
			<h2>제목1</h2>
			<p>내용1</p>
		</article>
		<article>
			<h2>제목2</h2>
			<p>내용2</p>
		</article>
	</section>
	<footer>
		<h3>홈페이지 정보(바닥 글)</h3>
	</footer>
</body>
</html>
```

#### 실습3 exam8_2

```html
<!-- 실습3 exam8_2 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
<style>
	header {
		width : 100%;
		height : 100px;
		background-color : lime;
	}
	nav {
		width : 30%;
		height : 500px;
		float : left;
		background-color : pink;
	}
	section {
		width : 70%;
		height : 500px;
		float : right;
		background-color : skyblue;
	}
	article {
		width : 80%;
		height : 200px;
		background-color : magenta;
		margin-left : auto;
		margin-right : auto;	
	}
	footer {
		width : 100%;
		height : 50px;
		/*안쓰면 section , nav에 가려진다 *//* clear both를 주어야 footer가 제대로 나타남 -> 나는 왼쪽 오른쪽에도 쓰지 않을거야 라는 의미 */		
		clear : both;
		background-color : lightgray;
	}

</style>
</head>
<body>
	<header>
		<h1>레이아웃 나누기</h1>
		<em>오늘은 즐거운 월요일</em>
	</header>
	<nav>
		<strong>고르세용</strong><br>
		<mark>먹고싶은거</mark>
		<ul>
			<li>메뉴1</li>
			<li>메뉴2</li>
			<li>메뉴3</li>
			<li>메뉴4</li>
		</ul>	
	</nav>
	<section>
		<article>
			<h2>제목1</h2>
			<p>내용1</p>
		</article>
		<article>
			<h2>제목2</h2>
			<p>내용2</p>
		</article>
	</section>
	<footer>
		<h3>홈페이지 정보(바닥 글)</h3>
	</footer>
</body>
</html>
```

#### 실습4 exam8_3

```html
<!-- 실습4 exam8_3 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 학습</title>
<style>
	* {
		margin : 0;
	} /*태그 마다 default로 정해저 있는 마진이 있으니까 모든 기본 태그의 마진을 0으로 설정*/
	header {
		width : 100%;
		height : 100px;
		background-color : lime;
	}
	nav {
		width : 30%;
		height : 500px;
		float : left;
		background-color : pink;
	}
	section {
		width : 70%;
		height : 500px;
		float : right;
		background-color : skyblue;
	}
	article {
		width : 80%;
		height : 200px;
		background-color : magenta;
		margin : 10px auto;		
	}
	footer {
		width : 100%;
		height : 50px;		
		clear : both;
		background-color : lightgray;
	}

</style>
</head>
<body>
	<header>
		<h1>레이아웃 나누기</h1>
	</header>
	<nav>
		<strong>고르세용</strong><br>
		<mark>먹고싶은거</mark>
		<ul>
			<li>메뉴1</li>
			<li>메뉴2</li>
			<li>메뉴3</li>
			<li>메뉴4</li>
		</ul>
	</nav>
	<section>
		<article>
			<h2>제목1</h2>
			<p>내용1</p>
		</article>
		<article>
			<h2>제목2</h2>
			<p>내용2</p>
		</article>
	</section>
	<footer>
		<h3>홈페이지 정보(바닥 글)</h3>
	</footer>
</body>
</html>
```

#### 실습5 exam8_4

```html
<!-- 실습5 exam8_4 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet"  href="mystyle.css">
</head>
<body>
	<header>
		<h1>레이아웃 나누기(외부 CSS)</h1>
	</header>
	<nav>
		<strong>고르세용</strong><br>
		<mark>먹고싶은거</mark>
		<ul>
			<li>메뉴1</li>
			<li>메뉴2</li>
			<li>메뉴3</li>
			<li>메뉴4</li>
		</ul>
	</nav>
	<section>
		<article>
			<h2>제목1</h2>
			<p>내용1</p>
		</article>
		<article>
			<h2>제목2</h2>
			<p>내용2</p>
		</article>
	</section>
	<footer>
		<h3>홈페이지 정보(바닥 글)</h3>
	</footer>
</body>
</html>
```

```css
/*mystyle.css*/
@charset "UTF-8";

* {
	margin: 0;
}

header {
	width: 100%;
	height: 100px;
	background-color: lime;
}

nav {
	width: 30%;
	height: 500px;
	float: left;
	background-color: pink;
}

section {
	width: 70%;
	height: 500px;
	float: right;
	background-color: skyblue;
}

article {
	width: 80%;
	height: 200px;
	background-color: magenta;
	margin: 10px auto;
}

footer {
	width: 100%;
	height: 50px;
	clear: both;
	background-color: lightgray;
}
```



display : none, block, inline, inline-block

#### 실습6 문제 csslab1 

![image-20200106200947430](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106200947430.png)

![image-20200106201009273](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201009273.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 실습</title>
<style>
	h1{
		color : blue;
		text-align : center;
		margin : 10px auto; /*값을 두개 주면 상하는 10px 좌우는 auto*/
		padding : 30px;
		border-radius : 10px;
		width : 250px;
		height : 40px;
		background-image : linear-gradient(to right, red, orange, yellow, green, blue, navy, purple);
	}
	img{
		border : 1px solid red;
		box-shadow: 6px 6px 6px gray;
		/*opacity : 0.3;/*0.0(완전투명) ~ 1.0(완전불투명)*/
		margin-right : 20px;
		margin-top : 5px;
	}
	div{
		text-align : center;
	}
	.cl:hover{
		opacity : 0.3;
	}
</style>
</head>
<body>
<h1 id=section>날씨<span style="color:white">의 종류</span></h1>
<hr>
<div>
<img src="../images/sun.png" width="200" height="200" class="cl">
<img src="../images/rain.png" width="200" height="200" class="cl">
<img src="../images/cloud.png" width="200" height="200" class="cl">
</div>
<br>
<div>
<img src="../images/cloud_sun.png" width="200" height="200" class="cl">
<img src="../images/snow.png" width="200" height="200" class="cl">
<img src="../images/etc.png" width="200" height="200" class="cl">
</div>
</body>
</html>
```

#### 실습7 문제 csslab2

![image-20200106201125625](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201125625.png)

![image-20200106201137835](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201137835.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>CSS 실습</title>
<style>
	h1{
		width : 350px;
		height : 50px;
		color : Fuchsia;
		text-align : center;
		margin : 10px auto; /*값을 두개 주면 상하는 10px 좌우는 auto*/
		padding : 30px;
		border-radius : 10px;
		background-image : linear-gradient(to right, yellow, green);
	}
	hr{
		height : 2px;
		background-image : linear-gradient(to right, yellow, orange, red, green);
	}
	img{
		border : 1px solid green;
		box-shadow: 10px 10px 10px lime;
		border-radius : 10px;
		margin-right : 20px;
		margin-top : 5px;
	}
	div{
		text-align : center;
	}
	.cl:hover{
		transform : rotate(10deg); /*3도 만큼 회전시켜라*/
		transition : transform 1s; /*transform을 2초동안 움직여라*/
	}
	.cll:hover{
		transform : rotate(-10deg); /*3도 만큼 회전시켜라*/
		transition : transform 0.5s; /*transform을 2초동안 움직여라*/
	}
</style>
</head>
<body>
<h1>과일<span style="color:white">의</span><span style="color:#ff9900"> 종류</span></h1>
<hr>
<div>
<img src="../images/r1.gif" width="200" height="200" class="cl">
<img src="../images/r2.gif" width="200" height="200" class="cl">
<img src="../images/r3.jpg" width="200" height="200" class="cl">
<img src="../images/r4.gif" width="200" height="200" class="cl">
</div>
<br>
<div>
<img src="../images/r5.png" width="200" height="200" class="cll">
<img src="../images/r6.png" width="200" height="200" class="cll">
<img src="../images/r7.png" width="200" height="200" class="cll">
<img src="../images/r8.jpg" width="200" height="200" class="cll">
</div>
</body>
</html>
```

#### 실습8 문제 homework2

![image-20200106201525914](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201525914.png)

![image-20200106201534566](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201534566.png)

![image-20200106201553171](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201553171.png)

![image-20200106201602260](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200106201602260.png)

```html
<!--실습8 문제 homework2-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	* {
		margin : 0;
		
	} /*태그 마다 default로 정해저 있는 마진이 있으니까 모든 기본 태그의 마진을 0으로 설정*/
	header {
		text-align : center;
		color : blue;
		background-image : linear-gradient(to right bottom, yellow, skyblue);
	}
	h1, h2, h3{
		color : blue;
		text-shadow:3px 3px 5px ;
	}
	a{
		/* font-weight : bold; */
		margin : 0px 30px;
		text-decoration : none;
	}
	nav {
		margin : 10px 0px;
	}
	.urlss:hover{
		font-weight : bolder;
	}
	
 	section {
		/*text-align : center;*/
		font-weight : bold;	
		margin-left : 150px;
		width : 80%;
		
	}
	article {
		margin : 20px 0px;
		border : 2px solid #990000;	
		border-radius : 10px;
	}
	table{
		text-align : center;
		padding : 10px;
		border-collapse : collapse;
	}
	th{
		color : white;
		background-color : #99ccff;
		font-weight : bold;
	}
	th, tr, td{
		margin : 0px 5px;
		padding : 5px 20px;
	}
	aside {
		text-align : center;
		margin : 20px 0px;
		border : 2px solid #990000;	
		border-radius : 10px;
		width : 80%;
		margin-left : 150px;
	}
	figcaption{
		text-align : center;	
	}
	footer {
		border : 1px dotted yellow;
		background-color : gray;
	}
	#imagess{
		text-align : center;
	}
	img:hover{
		opacity : 0.3;
	}
	div{
		margin : 10px 10px;
	}
</style>
</head>
<body>
<header>
<h1>HTML5 학습</h1>

<nav>
	<a href="http://www.w3.org/" class="urlss">W3C</a>
	<a href="http://www.w3schools.com/" class="urlss">W3SCHOOLS</a>
	<a href="http://www.jquery.com/" class="urlss">jQuery</a>
</nav>

</header>

<br>
<!-- ----------------------------------------------------------------- -->
<section>
	<article>

	 <div>
	 	<h2>나의 소개</h2> <!-- 	<h2 style="text-align:center">나의 소개</h2> -->
	 	<div class = "uis">
		 	<ul>
				<li>이름 : 유성진</li>
				<li>별명 : oliver</li>
				<li>관심기술 : Web Server</li>
				<li>취미 : 향수만들기</li>
			</ul>
		</div>
	 </div>
	</article>

	<article>
		<div>
			<h2>올해 재미있게 읽은 책</h2>
			<div class = "uis">
				<table border ="2">
					<tr><th >제목</th><th>장르</th></tr>
					<tr><td>아가씨와 밤</td><td>소설</td></tr>
					<tr><td>27년동안 영어 공부에 실패 했던 39세 김과장은 어떻게 3개월 만에 영어 천재가 됐을까</td><td>자기계발</td></tr>
					<tr><td>Gigged 직장이 없는 시대가 온다</td><td>경제경영</td></tr>
				</table>
			</div>
		</div>
	</article>
	
	<article>
		<div>
			<h2>자랑하고 싶은 <span style="color:#009933">우리동네의 유적지</span></h2>
			<h3>서울에서 가장 오래된 마을, 서울 암사동 유적입니다.</h3>
			<div>
				우리나라 선사시대를 대표하는 서울 암사동 유적은 한강유역
				최대의 집단 취락지로 그 가치가 매우 높은 곳입니다.
				여러 차례 발굴조사 결과 40기 이상의 집자리터가 발견되었으며,
				한강을 중심으로 어로와 채집 생활을 하며 살았던 신석기시대 사람들 삶의 흔적이 고스란히 남아있습니다.
				신석기시대 사람들은 암사동에서 마을이라는 공동체 사회를 이루며 인류 역사상 가장 혁신적이고 예술적인 빗살무늬토기 문화를 꽃피웠습니다.
			</div>

			<figure>
				<div id ="imagess">
				 	 <img src="../images/amsa.png" alt="Trulli" style="width:80%">
				 </div>
			  <figcaption>Fig.1 - 암사 선사 유적지</figcaption>
			</figure>
		</div>
	</article>
</section>

<!-- ----------------------------------------------------------------- -->

<aside id="player">
  <video id="media" width="720" height="400" controls>
  	<!-- <img src="/edu/images/duke_luau.png"> 상대 URL --> 
    <source src="/edu/htmlexam/amsa.mp4">
    <source src="/edu/htmlexam/amsa.ogg">
  </video> 
  <br>
  
    <footer>
        <em>이 문서는 유튜브에 의해 다운로드를 받아 온 파일 이며 절대 이 동영상 활용하여 사용하면 안됩니다.</em><br>
    </footer>
</aside>

</body>
</html>
```

#### 실습9 exam

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>뷰포트를 조정하지 않은 페이지</h1>
<hr>
<h1>ㅋㅋㅋㅋㅋㅋㅋㅋ</h1>
<h2>ㅋㅋㅋㅋㅋㅋㅋㅋ</h2>
<h3>ㅋㅋㅋㅋㅋㅋㅋㅋ</h3>
<h4>ㅋㅋㅋㅋㅋㅋㅋㅋ</h4>
<p>
paragraph paragraph paragraph paragraph paragraph paragraph
</p>
<p>
PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH 
</p>
<ol>
<li>HTML5
<li>JavaScript
<li>jQuery
</ol>

</body>
</html>
```



### CSS 코드 내부에서 분기하는 방법

CSS 코드 내부에서 사용하는 미디어 쿼리의 기본적인 문법 예는 다음과 같다. 일반적으로 권장하고 널리 쓰이는 방식이다.

```css
@media only all and (조건문) {실행문}
```

- **@media**: 미디어 쿼리가 시작됨을 선언한다. `@media`, `only`, `all`, `and`, `(조건문)` 사이에 포함되어 있는 공백은 필수적이다.
- **only**: `only` 키워드는 미디어 쿼리를 지원하는 사용자 에이전트만 미디어 쿼리 구문을 해석하라는 명령이며 생략 가능하다. 생략했을 때 기본 값은 `only`로 처리 된다. 생략해도 무방하므로 이 키워드는 일반적으로 작성하지 않는다. 이 자리에는 `not` 키워드를 사용할 수 있는데 뒤에 오는 모든 조건을 부정하는 연산을 한다.
- **all**: `all` 키워드는 미디어 쿼리를 해석해야 할 대상 미디어를 선언한 것이다. `all` 이면 모든 미디어가 이 구문을 해석해야 한다. `all` 키워드 대신 `screen` 또는 `print`와 같은 특정 미디어를 구체적으로 언급할 수도 있다. `all` 키워드는 생략 가능하고 생략했을 때 기본 값은 `all` 으로 처리된다. 이 밖에도 다양한 미디어 타입(`all`, `aural`, `braille`, `embossed`, `handheld`, `print`, `projection`, `screen`, `speech`, `tty`, `tv`)이 있다. `all`, `screen`, `print`를 가장 널리 쓴다.
- **and**: `and` 키워드는 논리적으로 ‘AND’ 연산을 수행하여 앞과 뒤의 조건을 모두 만족해야 한다는 것을 의미한다. 조건이 유일하거나 또는 `only`, `all`과 같은 선행 키워드가 생략되면 `and` 키워드는 사용하지 말아야 한다. `and` 대신 콤마 `,` 기호를 사용하면 ‘OR’ 연산을 수행한다. ‘OR’ 연산은 나열된 조건 중에서 하나만 참이어도 `{실행문}`을 해석한다.
- **(조건문)**: 브라우저는 조건문이 참일때`{실행문}`을 처리하고 거짓일 때 무시한다. 조건문은 두 가지 이상 등장할 수 있다. 둘 이상의 조건문은 `and` 키워드 또는 콤마 `,` 기호로 연결해야 한다.
- **{실행문}**: 일반적인 CSS 코드를 이 괄호 안에 작성한다. 브라우저는 `(조건문)`이 참일때 실행문 안쪽에 있는 CSS 코드를 해석한다.

### 미디어 쿼리 코드 템플릿

아래 코드는 모든 해상도를 커버하기 위한 미디어 쿼리 코드 템플릿이다. All, Mobile, Tablet, Desktop 으로 기기별 대응 코드를 분류 했지만 Liquid 레이아웃 기법을 사용하면 사실상 모든 해상도를 커버할 수 있다.

```css
@charset "utf-8";

/* All Device */
모든 해상도를 위한 공통 코드를 작성한다. 모든 해상도에서 이 코드가 실행됨.

/* Mobile Device */
768px 미만 해상도의 모바일 기기를 위한 코드를 작성한다. 모든 해상도에서 이 코드가 실행됨. 미디어 쿼리를 지원하지 않는 모바일 기기를 위해 미디어 쿼리 구문을 사용하지 않는다.

/* Tablet &amp; Desktop Device */
@media all and (min-width:768px) {
    사용자 해상도가 768px 이상일 때 이 코드가 실행됨. 테블릿과 데스크톱의 공통 코드를 작성한다.
}

/* Tablet Device */
@media all and (min-width:768px) and (max-width:1024px) {
    사용자 해상도가 768px 이상이고 1024px 이하일 때 이 코드가 실행됨. 아이패드 또는 비교적 작은 해상도의 랩탑이나 데스크톱에 대응하는 코드를 작성한다.
}

/* Desktop Device */
@media all and (min-width:1025px) {
    사용자 해상도가 1025px 이상일 때 이 코드가 실행됨. 1025px 이상의 랩탑 또는 데스크톱에 대응하는 코드를 작성한다.
}
```

### 조건문이 될 수 있는 특징들

#### width / height

뷰포트의 너비와 높이. 뷰포트의 크기는 HTML body 콘텐츠를 표시하는 영역으로 실제 스크린의 크기와는 다르다. 반응형 웹 구현시 가장 일반적으로 사용하는 조건이 된다.

```css
@media all and (min-width:768px) and (max-width:1024px) { … } // 뷰포트 너비가 768px 이상 '그리고' 1024px 이하이면 실행
@media all and (width:768px), (width:1024px) { … } // 뷰포트 너비가 768px 이거나 '또는' 1024px 이면 실행
@media not all and (min-width:768px) and (max-width:1024px) { … } // 뷰포트 너비가 768px 이상 '그리고' 1024px 이하가 '아니면' 실행
```

#### device-width / device-height

스크린의 너비와 높이. 스크린은 출력 장치가 픽셀을 표시할 수 있는 모든 영역으로 일반적으로 HTML `body` 콘텐츠를 표시하는 뷰포트 보다 크다.

```css
@media all and (device-width:320px) and (device-height:480px) { … } // 스크린 너비가 320px '그리고' 높이가 480px 이면 실행
@media all and (min-device-width:320px) and (min-device-height:480px) { … } // 스크린 너비가 최소 320px 이상 '그리고' 높이가 최소 480px 이상이면 실행
```

#### orientation

뷰포트의 너비와 높이 비율을 이용하여 세로 모드인지 가로 모드인지를 판단한다.

```css
@media all and (orientation:portrait) { … } // 세로 모드. 뷰포트의 높이가 너비에 비해 상대적으로 크면 실행
@media all and (orientation:landscape) { … } // 가로 모드. 뷰포트의 너비가 높이에 비해 상대적으로 크면 실행
```

#### aspect-ratio

뷰포트의 너비와 높이에 대한 비율. ‘너비/높이’ 순으로 조건을 작성한다. `min/max` 접두사를 사용하면 너비 값의 최소/최대 비율을 정할 수 있다.

```css
@media all and (aspect-ratio:5/4) { … } // 뷰포트 너비가 5, 높이가 4 비율이면 실행
@media all and (min-aspect-ratio:5/4) { … } // 뷰포트 너비가 5/4 비율 이상이면 실행
@media all and (max-aspect-ratio:5/4) { … } // 뷰포트 너비가 5/4 비율 이하면 실행
```

#### device-aspect-ratio

스크린의 너비와 높이에 대한 비율. ‘너비/높이’ 순으로 조건을 작성한다. `min/max` 접두사를 사용하면 너비 값의 최소/대최 비율을 정할 수 있다.

```css
@media all and (device-aspect-ratio:5/4) { … } // 스크린 너비가 5, 높이가 4 비율이면 실행
@media all and (min-device-aspect-ratio:5/4) { … } // 스크린 너비가 5/4 비율 이상이면 실행
@media all and (max-device-aspect-ratio:5/4) { … } // 스크린 너비가 5/4 비율 이하면 실행
```

#### color

출력 장치의 색상에 대한 비트 수. 출력 장치가 컬러가 아닌 경우 `0`의 값에 대응한다.

```css
@media all and (color) { … } // 출력 장치가 컬러를 지원하면 실행
@media all and (color:0) { … } // 출력 장치가 컬러가 아니면 실행
@media all and (color:8) { … } // 출력 장치가 8비트 색상이면 실행
@media all and (min-color:8) { … } // 출력 장치가 8비트 이상 색상이면 실행
@media all and (max-color:8) { … } // 출력 장치가 8비트 이하 색상이면 실행
```

#### color-index

출력 장치가 색상 색인 테이블을 사용하는 경우 표현할 수 있는 색의 수. 출력 장치가 색상 색인 테이블을 사용하지 않으면 `0`의 값에 대응한다. 현재 제대로 지원하는 브라우저가 없다.

```css
@media all and (color-index) { … } // 출력 장치가 색상 색인 테이블을 사용하면 실행
@media all and (color-index:0) { … } // 출력 장치가 색상 색인 테이블을 사용하지 않으면 실행
@media all and (color-index:256) { … } // 출력 장치가 256 색을 지원하면 실행
@media all and (min-color-index:256) { … } // 출력 장치가 256 이상 색을 지원하면 실행
@media all and (max-color-index:256) { … } // 출력 장치가 256 이하 색을 지원하면 실행
```

#### monochrome

출력 장치가 흑백인 경우 픽셀당 비트 수. 출력 장치가 흑백이 아니라면 `0`의 값에 대응한다.

```css
@media all and (monochrome) { … } // 출력 장치가 흑백이면 실행
@media all and (monochrome:0) { … } // 출력 장치가 흑백이 아니면 실행
@media all and (min-monochrome:2) { … } // 출력 장치가 흑백이고 2비트 이상이면 실행
@media all and (max-monochrome:2) { … } // 출력 장치가 흑백이고 2비트 이하이면 실행
```

#### resolution

출력 장치의 해상력에 대응한다. `min/max` 접두사는 사각형 아닌 픽셀(인쇄 장치)에도 대응하지만 접두사 없는 `resolution` 조건은 사각형 픽셀에만 대응한다. 조건의 값으로 dpi와 dpcm 단위를 사용할 수 있다.

```css
@media all and (resolution:96dpi) { … } // 1인치당 96개의 사각형 화소를 제공하면 실행
@media all and (min-resolution:96dpi) { … } // 1인치당 96개 이상의 화소를 제공하면 실행
@media all and (max-resolution:96dpi) { … } // 1인치당 96개 이하의 화소를 제공하면 실행
```

#### scan

TV의 스캔 방식에 따라 대응한다. `progressive` 값은 초당 60회 수준의 고화질 스캔에 대응하고 `interlace` 값은 초당 30회 수준의 일반 스캔에 대응한다. 대부분의 HDTV는 `progressive`와 `interlace` 방식을 모두 지원하고 있다.

```css
@media tv and (scan:progressive) { … } // 초당 60회 수준의 고화질 스캔 방식 TV에 대응한다
@media tv and (scan:interlace) { … } // 초당 30회 수준의 일반 스캔 방식 TV에 대응한다
```

#### grid

출력 장치가 그리드 방식이면 대응한다. 그리드 방식은 타자기와 같이 고정된 글꼴만 사용하는 장치이다. 통상 출력 장치는 비트맵이 아니면 그리드 방식이다. 값은 정수 `0`과 `1` 뿐이고 `0`의 값은 비트맵 방식에 대응한다.

```css
@media all and (grid) { … } // 출력 장치가 그리드 방식이면 실행
@media all and (grid:0) { … } // 출력 장치가 그리드 방식이 아니면 실행
@media all and (grid:1) { … } // 출력 장치가 그리드 방식이면 실행
```

#### 실습10 exam

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- viewport는 cell phone에서만 적용 된다 웹에서는 x -->
<meta name="viewport" content="width=device-width">
<title>Insert title here</title>
</head>
<body>
<h1>뷰포트를 지정한 페이지</h1>
<hr>
<h1>ㅋㅋㅋㅋㅋㅋㅋㅋ</h1>
<h2>ㅋㅋㅋㅋㅋㅋㅋㅋ</h2>
<h3>ㅋㅋㅋㅋㅋㅋㅋㅋ</h3>
<h4>ㅋㅋㅋㅋㅋㅋㅋㅋ</h4>
<p>
paragraph paragraph paragraph paragraph paragraph paragraph
</p>
<p>
PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH PARAGRAPH 
</p>
<ol>
<li>HTML5
<li>JavaScript
<li>jQuery
</ol>

</body>
</html>
```

#### 실습11 exam

```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>미디어쿼리</title>
<style>
body {
	background-color: gray;
}

#logo img {
	width: 100%;
	margin-top: 150px;
}

@media screen and (max-width: 960px) {
	body {
		background-color: green;
	}
}

@media screen and (max-width:500px) {
	body {
		background-color: yellow;
	}
}

@media screen and (max-width:320px) {
	body {
		background-color: orange;
	}
}
</style>
</head>
<body>
	<div id="logo">
		<img src="logo.png">
	</div>
</body>
</html>
```

#### 실습12 exam

```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>미디어쿼리</title>
  <style>
  body{
		background-color:gray;
	}
	#logo img{
		width:100%;
		margin-top:50px;
	}
	
	@media screen and (orientation:landscape) {
		body {background-color:orange;}
	}
	
	@media screen and (orientation:portrait) {
		body {background-color:yellow;}
	}
	
  </style>
</head>
<body>
  <div id="logo">
		<img src="logo.png">
	</div>
</body>
</html>
```

#### 실습13 exam

| pseudo-element | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| ::first-letter | 콘텐츠의 첫글자를 선택한다.                                  |
| ::first-line   | 콘텐츠의 첫줄을 선택한다. 블록 요소에만 적용할 수 있다.      |
| ::after        | 콘텐츠의 뒤에 위치하는 공간을 선택한다. 일반적으로 content 어트리뷰트와 함께 사용된다. |
| ::before       | 콘텐츠의 앞에 위치하는 공간을 선택한다. 일반적으로 content 어트리뷰트와 함께 사용된다. |
| ::selection    | 드래그한 콘텐츠를 선택한다. iOS Safari 등 일부 브라우저에서 동작 않는다. |

```html
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8"/>
    <title>반응형 웹디자인(RWD)</title>
    <!-- 모바일 스크린에 맞춰 너비와 스케일을 설정함.(iOS전용, Android 알아서 적절히 렌더링함.) -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no"/>
    <style type="text/css">
        body {
            background: black;
            color: #333;
            font-family: NanumGothic, 나 눔 고 딕, "Malgun Gothic", "맑은 고딕", sans-serif;
        }
        h1:after {
            color: black;
            display: block;
        }
        @media all and (max-width: 320px) {
            body {
                background-color: red;
            }
            h1 {
                color: white;
            }
            h1:after {
                content: "max-width: 320px";
            }
        }

        @media all and (min-width: 321px) and (max-width: 768px) {
            body {
                background-color: blue;
            }
            h1 {
                color: white;
            }
            h1:after {
                content: "min-width: 321px max-width: 768px";
            }
        }

        @media all and (min-width: 769px) {
            body {
                background-color: orange;
            }
            h1 {
                color: white;
            }
            h1:after {
                content: "min-width: 769px";
            }
        }
    </style>
</head>
<body>
<h1>반응형 웹디자인</h1>
</body>
</html>
```

#### 실습14 exam

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>반응형 웹디자인(RWD)</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no"/>
    <link href="stylesheet1.css" rel="stylesheet"/>
    <link href="stylesheet2.css" media="screen and (min-width: 600px)" rel="stylesheet"/>
</head>
<body>
<p>왜 반응형 웹 디자인인가</p>
<p>반응형 웹 디자인과 개발 원리 덕분에 화면 크기에 상관 없이 모든 기기에서 웹 사이트를 확인할 수 있게 됐으며 사용 경험도 한층 개선됐다.</p>
<p id="attribute-test">화면 해상도가 600px 이하일 때<br/>박스가 사라진다.</p>
</body>
</html>
```

```css
/*stylesheet1*/
body {
    background: black;
    color: #333;
    font-family: NanumGothic, �굹�닎怨좊뵓, "Malgun Gothic", "留묒� 怨좊뵓", sans-serif;
}

p {
    width: 60%;
    min-width: 18.75em; /* 300px : 1em=16px, 0.75em=12px */
    max-width: 43.75em; /* 700px */
    margin: 2em auto;
    background: #fff;
    padding: 20px;
}

a {
    color: #333;
}

#attribute-test {
    display: none;
}

@media only screen and (min-width: 18.75em) /* 300px */ {
    body {
        background: yellow;
    }
}

@media only screen and (min-width: 30em) /* 480px */ and (max-width: 38.75em) /* 620px */ {
    body {
        background: green;
    }
}

@media screen and (min-width: 38.75em) /* 620px */ {
    body {
        background: red;
    }
}

@media screen and (min-width: 50em) /* 800px */ {
    body {
        background: blue;
    }
}

@media screen and (min-width: 68.75em) /* 1100px */ {
    body {
        background: orange;
    }
}

@media screen and (min-width: 75em) /* 1200px */ {
    body {
        background: navy;
    }
}

@media screen and (min-width: 78.152em) /* 1250px */ {
    body {
        background-color: pink;
    }
}
```

```css
/*stylesheet2*/
#attribute-test {
    display: block;
    color: #fff;
    background: black;
    text-align: center;
}
```

