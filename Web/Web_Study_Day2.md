# Day2 Web

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>Let's start 2020!!!!</h1>
</body>
</html>

http://localhost:8000/edu/imsi.html -> 확인가능!!
                    ----------------
                        URI
```

HTML을 읽어 들이는것을 파싱한다라고 한다.

edu라는 프로젝트에서 우클릭 후 UTF-8로 다 변경한다.

![image-20200103094522995](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103094522995.png)

http://localhost:8000/edu/htmlexam/exam1.html

```html
<!--실습 exam1-->
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>HTML 학습</title>

</head>

<body> <!-- 실제 웹페이지 내용이 들어감, 대소문자 구분 안함  --> 
<h1>자주 사용되는 HTML 태그 학습</h1>
<hr> <!-- 수평선을 그어줌  --> 
<h2>하이퍼링크 태그</h2>
<a href="http://www.w3.org/">W3 컨소시엄</a><br>
<a href="http://www.w3schools.com/">Web Client 기술 학습하기</a><br>
<a href="http://java.sun.com/"><img src = "../images/java_duke.gif"></a><br> <!-- <br> : 행바꿈  -->
<!-- 하이퍼링크 텍스트 및 이미지 확인 -->
<h2>이미지 출력 태그</h2>
<img src="../images/duke_luau.png"> <!-- 상대 URL -->
<img src="/edu/imaages/duke_luau.png"> <!-- 상대 URL -->
<img src="http://localhost:8000/edu/images/duke_luau.png"> <!-- 절대 URL -->
<h2>리스트 태그</h2>
<!-- unOrdered List -->
<ul>
	<!-- 항상 안에 있는 것들은 컨텐트이다.. -->
	<li>Java Programming</li>
	<li>SQL</li>
	<li>HTML5</li>
	<li>CSS3</li>
	<li>JavaScript</li>
	<li>Ajax</li>
	<li>Servlet</li>
	<li>JSP</li>
	<li>JDBC</li>
</ul>
<hr>
<!-- onOrdered List -->
<ol>
	<!-- 항상 안에 있는 것들은 컨텐트이다.. -->
	<li>Java Programming</li>
	<li>SQL</li>
	<li>HTML5</li>
	<li>CSS3</li>
	<li>JavaScript</li>
	<li>Ajax</li>
	<li>Servlet</li>
	<li>JSP</li>
	<li>JDBC</li>
</ol>
<h2>테이블 태그</h2>
<table border ="1">
	<tr><th>언어이름</th><th>설명</th></tr> <!-- 제목행 -->
	<tr><td>Java</td><td>범용으로 활용되는 OOP 언어</td></tr> <!-- 컨텐츠행 -->
	<tr><td>JavaScript</td><td>동적인 웹 페이지 개발에 사용하는 OOP 언어</td></tr>
	<tr><td>CSS</td><td>HTML의 스타일을 조정하는 언어</td></tr>
	<tr><td>R</td><td>통계분석과 데이터 마이닝에 사용되는 언어</td></tr>
</table>
<h2>입력 폼</h2>
<form action = "..."method=""> <!-- JSP나 svlet 프로그램이 원래 온다. -->
	<!-- input tag는 type이 중요 -->
	<input type="text" placeholder="이름을 입력하세요..." required name= "gname">
	<input type="submit" value="전송">

</form>
</body>

</html>
```

gif, jpg(jpeg), png -> gif와 jpg의 장점을 합한게 png이다.  jpg는 사이즈가 크면서 해상도가 좋고 gif는 사이즈가 작으면서 해상도가 좋지 않다. 

---------------

**[placeholder에 썼을때!!]**

- unico 영어 전송

  http://localhost:8000/edu/htmlexam/...?gname=unico

- 유니코 한글을 전송

  [http://localhost:8000/edu/htmlexam/...?gname=%EC%9C%A0%EB%8B%88%EC%BD%94](http://localhost:8000/edu/htmlexam/...?gname=유니코)

- 한글 + 숫자

  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=123](http://localhost:8000/edu/htmlexam/...?gname=가&gage=123)

- 한글 + 영어 + 숫자 (공백은 + 기호로 표시된다.)

  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80+ABC&gage=123](http://localhost:8000/edu/htmlexam/...?gname=가+ABC&gage=123)

- 한글 + 숫자 + 날짜

  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=10&gage=2020-04-05](http://localhost:8000/edu/htmlexam/...?gname=가&gage=10&gage=2020-04-05)

- 한글 + 숫자 + 날짜 + radiobutton + checkbox

  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=5&gage=2020-01-06&gender=on&food=on&food=on](http://localhost:8000/edu/htmlexam/...?gname=가&gage=5&gage=2020-01-06&gender=on&food=on&food=on)

  -> radio 또는 checkbox는 value속성을 쓰지 않으면 이렇게 on이라고 표시되니 필수이다!!

- 한글 + 숫자 + 날짜 + radiobutton + checkbox(value 속성 추가)

  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=10&gage=2020-01-07&gender=on&food=%EB%96%A1%EB%B3%B6%EC%9D%B4&food=%ED%8A%80%EA%B9%80&food=%EC%88%9C%EB%8C%80](http://localhost:8000/edu/htmlexam/...?gname=가&gage=10&gage=2020-01-07&gender=on&food=떡볶이&food=튀김&food=순대)

  ![image-20200103133320466](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103133320466.png)

  **radio와 checkbox는 value 속성이 필수다!!**

- Query String: Web Client가 Web Server에게 정보(페이지)를 요청할 때 함께 전달 가능한 name과 value 구성되는 문자열

  W3C가 정해놓기를

  1. name-value로 구성되어야 한다.
  2. 여러개의 name=value를 전달하는 경우에는 & 기호로 분리한다.
  3. 영문과 숫자 그리고 일부 특수문자를 제외하고는 %기호와 코드 값으로 전달된다.
  4. 공백 + 기호로 전달된다.

![image-20200103114143915](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103114143915.png)

-------

http://html5test.com/



http://localhost:8000/edu/htmlexam/exam1.html

**HTML5를 지원하는 정도는 브라우저마다 다르다.**

**웹에서 표현되는 color**



![image-20200103134855339](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103134855339.png)

```html
<!-- 교육에서 사용 할 수 있는 tag-->

<h1>This is heading 1가나다</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>

<p>Do not <mark>forget to buy 밀크우유</mark> today.</p>

<p>This is a paragraph.</p>
<p>This is a paragraph.</p>
<p>This is a paragraph.</p>

<hr>

This is a paragraph.<br>
This is a paragraph.<br>
This is a paragraph.<br>

<picture>
  <source media="(min-width: 650px)" srcset="img_pink_flowers.jpg">
  <source media="(min-width: 465px)" srcset="img_white_flower.jpg">
  <img src="img_orange_flowers.jpg" alt="Flowers" style="width:auto;">
</picture>

<figure>
  <img src="../html/pic_trulli.jpg" alt="Trulli" style="width:100%">
  <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
</figure>

<textarea rows="4" cols="50">
At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
</textarea>

<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
<!-- 콤보박스 비슷 한데 한번에 하나만 선택!! 
멀티 기능을 사용하면 라디오박스와 비슷한데 한번에 여러개 선택 가능!! -->


```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>테이블 출력하기</h1>
<hr>
<table border="1">
	<tr><th>이름</th><th>고향</th><th>나이</th></tr>  
	<tr><td>둘리</td><td>쌍문동</td><td>10</td></tr>  
	<tr><td>도우너</td><td>깐따비아</td><td>9</td></tr>  
	<tr><td>또치</td><td>아프리카</td><td>10</td></tr>  
</table>
<hr>
<table border="1">
	<tr><th colspan="3">이름,고향,나이</th></tr>  <!-- colspan="3" 3개의 열을 병합 -> th를 하나만 사용해서 !!-->
	<tr><td rowspan="2">ㅋㅋㅋㅋ</td><td>쌍문동</td><td>10</td></tr> <!-- rowspan="2" 2개의 행을 병합  td를 하나만 사용해서 -->  
	<tr><td>깐따비아</td><td>9</td></tr>  
	<tr><td>또치</td><td>아프리카</td><td>10</td></tr>  
</table>
</body>
</html>
```

- 실습 1 문제

![image-20200103172032110](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103172032110.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>HTML5 학습</h1>
<a href="http://www.w3.org/">W3C </a>
<a href="http://www.w3schools.com/">W3SCHOOLS</a>
<a href="http://java.sun.com/">jQuery</a>
<br>
<h2>나의 소개</h2>
<ul>
	<li>이름 : 유성진</li>
	<li>별명 : oliver</li>
	<li>관심기술 : Web Server</li>
	<li>취미 : 스티커모으기</li>
</ul>

<h2>올해 재미있게 읽은 책</h2>
<table border ="1">
	<tr><th>제목</th><th>장르</th></tr>
	<tr><td>아가씨와 밤</td><td>소설</td></tr>
	<tr><td>27년동안 영어 공부에 실패 했던 39세 김과장은 어떻게 3개월 만에 영어 천재가 됐을까</td><td>자기계발</td></tr>
	<tr><td>Gigged 직장이 없는 시대가 온다</td><td>경제경영</td></tr>
</table>

<h2>자랑하고 싶은 우리동네의 유적지</h2>
<h3>서울에서 가장 오래된 마을, 서울 암사동 유적입니다.</h3>
<textarea rows="6" cols="110">
우리나라 선사시대를 대표하는 서울 암사동 유적은 한강유역
최대의 집단 취락지로 그 가치가 매우 높은 곳입니다.
여러 차례 발굴조사 결과 40기 이상의 집자리터가 발견되었으며,
한강을 중심으로 어로와 채집 생활을 하며 살았던 신석기시대 사람들 삶의 흔적이 고스란히 남아있습니다.
신석기시대 사람들은 암사동에서 마을이라는 공동체 사회를 이루며 인류 역사상 가장 혁신적이고 예술적인 빗살무늬토기 문화를 꽃피웠습니다.
</textarea>

<figure>
  <img src="../images/amsa.png" alt="Trulli" style="width:80%	">
  <figcaption>Fig.1 - 암사 선사 유적지</figcaption>
</figure>

<section id="player">
  <video id="media" width="720" height="400" controls> 
    <source src="amsa.mp4">
    <source src="amsa.ogg">
  </video> 
</section>
<em>이 문서는 유튜브에 의해 다운로드를 받아 온 파일 이며 절대 이 동영상 활용하여 사용하면 안됩니다.</em><br>

</body>
</html>
```

- 실습 2 문제

![image-20200103175457321](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103175457321.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>글을 남겨주세요</h2>
<hr>
<form action = "..."method="">
	 
	이름:<input type="text" placeholder="이름을 입력하세요..." required name= "gname"><br>
	남기고자 하는 의견 :<br>
	<textarea rows="15" cols="30">
	</textarea><br>
	<input type="submit" value="등록"> <input type="reset" value="재작성">
</form>
</body>
</html>
```

- 실습 문제3

![image-20200103175546909](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103175546909.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>회원 정보를 입력하십시오.</h1>
<hr>
<form action = "..."method="">
	<input type="text" placeholder="이름을 입력하세요" required name= "gname"><br>
	<input type="text" placeholder="전화번호를 입력하세요" required name= "gphone"><br>
	<input type="text" placeholder="계정을 입력하세요" required name= "guser"><br>
	<input type="password" placeholder="패스워드를 입력하세요" required name= "gpassword"><br>
	<input type="submit" value="등록"> <input type="reset" value="재작성">
</body>
</html>
```

