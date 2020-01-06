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

