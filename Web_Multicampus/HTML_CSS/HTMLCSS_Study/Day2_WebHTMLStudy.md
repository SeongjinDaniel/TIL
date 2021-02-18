# Day2 Web(HTML)

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
<!-- Ordered List -->
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
<!--행(tr)을 먼저 만들고 그 안에 셀(td)을 만들어 주었습니다.
맨 위에 이름, 나이, 점수 부분과 같이 해당 테이블의 헤더 셀(제목 셀)은 th 요소를 사용합니다. -->
<h2>테이블 태그</h2>
<table border ="1">
	<tr><th>언어이름</th><th>설명</th></tr> <!-- 제목행 -->
	<tr><td>Java</td><td>범용으로 활용되는 OOP 언어</td></tr> <!-- 컨텐츠행 -->
	<tr><td>JavaScript</td><td>동적인 웹 페이지 개발에 사용하는 OOP 언어</td></tr>
	<tr><td>CSS</td><td>HTML의 스타일을 조정하는 언어</td></tr>
	<tr><td>R</td><td>통계분석과 데이터 마이닝에 사용되는 언어</td></tr>
</table>
<h2>입력 폼 태그</h2>
<form action = "..."method=""> <!-- JSP나 svlet 프로그램이 원래 온다. -->
	<!-- input tag는 type이 중요 -->
	<input type="text" placeholder="이름을 입력하세요..." required name= "gname"><br>
	<!-- number type이라서 숫자만 입력 가능 -->
	<input type="number" placeholder="나이를 입력하세요..." required name= "gage"><br>
	<input type="email" placeholder="메일 주소를 입력하세요..." required name= "gemail"><br>
	<input type="date" name= "gage"><label>원하는 날짜를 입력하세요...</label><br>
	성별을 선택하세요:<br>
	남성<input type ="radio" name="gender"> <!-- type 속성과 name 속성이 같아야 한 그룹이 된다. -->
	여성<input type ="radio" name="gender">
	<br>
	좋아하는 음식을 선택하세요:<br>
	떡볶이<input type ="checkbox" name="food" value = "떡볶이"> <!-- type 속성과 name 속성이 같아야 한 그룹이 된다. -->
	오뎅<input type ="checkbox" name="food" value ="오뎅">
	튀김<input type ="checkbox" name="food" value ="튀김">
	순대<input type ="checkbox" name="food" value ="순대">
	김밥<input type ="checkbox" name="food" value ="김밥">
	<br>
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

  -------

- 실습2 exam2

목록을 만드는 방법은 아래 세 가지가 있다.

```html
<ul>내용</ul>
<ol>내용</ol>
<dl>내용</dl>
```

**<ol>태그는** ordered list의 약자로, 숫자나 알파벳 등 순서가 있는 목록을 만드는 데 사용한다.

**<ul>태그는** unordered list의 약자로, 순서가 필요 없는 목록을 만든다.

**<dl>태그는** definition list의 약자로, 사전처럼 용어를 설명하는 목록을 만든다.

```html
<ol>과 <ul>의 각 항목들을 나열할 때는 ** 태그를** 사용하는데 list item의 약자입니다.
```

[목록을 만드는 ul, ol, li 태그](http://aboooks.tistory.com/210)

**<dl>태그는** definition list(정의 목록)의 약자로, 사전처럼 용어를 설명하는 목록을 만든다.

**<dt>**는 definition term(정의 용어)의 약자로, 정의되는 용어의 제목을 넣을 때 사용한다..

**<dd>**는 definition description(정의 설명)의 약자로, 용어를 설명하는 데 사용한다.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>리스트 출력 태그</h1>
<hr>
<h2>좋아하는 칼라</h2>
<ul>
	<li>녹색</li>
	<li>보라색</li>
	<li>주황색</li>
</ul>
<hr>
<h2>좋아하는 음식</h2>
<ol>
	<li>피자</li>
	<li>떡볶이</li>
	<li>짜장면</li>
</ol>
<hr>
<dl>
	<dt>자바</dt>
	<dd>플랫폼에 의존적이지 않은 OOP 언어</dd>
	<dt>HTML</dt>
	<dd>웹 페이지의 구조와 내용을 작성하는 마크업언어</dd>
	<dt>CSS</dt>
	<dd>HTML 엘리먼트들이 브라우저에 랜더링될 때 스타일을 조정하는 언어</dd>
</dl>
</body>
</html>
```

- 실습3 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>입력폼 학습</h1>
<hr>
<form>
이름 <input type="text" name="stname" required><br>
암호 <input type="password" name="stpwd"><br>
나이 <input type="number" name="stage"><br> <!-- HTML5 -->
좋아하는 칼라 <input type="color" name="stcolor"><br> <!-- HTML5 -->
좋아하는 음식 <br>
햄버거 <input type="checkbox"  name="stfood" value="f1">
비지찌게 <input type="checkbox"  name="stfood" value="f2">
회덮밥 <input type="checkbox"  name="stfood" value="f3">
돈까스 <input type="checkbox"  name="stfood" value="f4"><br>
성별 <br>
남성 <input type="radio"  name="gender" value="male">
여성 <input type="radio"  name="gender" value="female"><br>
<input type="submit" value="전송하기">
<input type="reset" value="초기상태로">
</form>
</body>
</html>
```

**실습 4 exam4**

#### form 요소

form 요소는 **폼(FORM)의 범위**를 표시한다. 폼은 사용자 입력을 위한 다양한 형식의 컨트롤(W3C는 입력필드, 버튼 등 폼을 구성하는 입력 요소를 컨트롤이라고 부름)로 구성되는 영역이며, 이 영역의 시작과 종료 지점은 form 요소에 의해 정의된다.

상호작용이 양방향으로 이루어지면서 사용자로부터 데이터를 수집해야 하는 상황이 자주 발생하였고, 이를 위해 고안된 것이 바로 컨트롤이다. 그리고 이 컨트롤들이 모여 있는 곳이 바로 폼이다.

```html
<form>
...
</form>
```

#### action 속성

action 속성은 **실행 애플리케이션**을 지정한다. 실행 애플리케이션은 입력된 데이터를 처리하는 서버 또는 프로그램이다. 이곳으로 데이터를 보내려면 브라우저가 전송 위치(URL)를 알아야 하며, 이를 위해 action 속성을 사용한다.

```html
<form action="http://www.example.com/addresscheck.html/"> </form>
```

#### accept-charset 속성

accept-charset 속성은 **승인된 문자 세트(accepted character set encoding)**을 지정한다. 일반적으로 HTML 문서에 적용된 문자 세트가 적용된다. 그런데 폼에 입력된 문자를 문서 전체에 적용된 문자 세트로 표현할 수 없는 경우도 있을 수 있다. 이럴 때 accept-charset 속성을 사용하여 적절한 문자 세트를 적용시킬 수 있다.

```html
<form accept-charset="utf-8"> </form>
```

- `enctype="application/x-www-form-urlencoded"` : 서버에 보내기전에 모든 문자를 인코딩하는 방식이며 폼에 텍스트 데이터를 포함했을 때 지정한다(기본값).
- `enctype="multipart/form-data"` : 파일 업로드 컨트롤처럼 문자가 아닌 파일을 전송할 때 사용된다.
- `enctype="text/plain"` : 일반 텍스트로 인코딩된다.

#### method 속성

method 속성은 **HTTP 메소드(HTTP method)**를 지정한다. HTTP 메소드는 클라이언트와 서버 간 데이터를 주고받기 위한 방식을 의미하는데 주로 사용되는 방식은 GET과 POST 방식이다.

```html
<form action="http://www.example.com/form.html/" method="post"> </form>
```

- GET 방식 : 입력된 데이터가 URL에 의해 전송되므로 암호화하지 않으면 URL만으로도 어떤 데이터를 입력했는지 알 수 있다. POST 방식보다 상대적으로 보안이 취약하고 전송할 수 있는 데이터도 제한적이다.

- POST 방식 : 입력된 데이터를 HTTP Body에 담아 전송하면서 서버측에서 데이터를 처리하는 방식이다. HTTP Body는 URL에 비해 더 많은 정보를 담을 수 있기 때문에 POST 방식은 GET 방식보다 더 많은 양의 데이터를 전송할 수 있으며 상대적으로 보안이 높은 편이다.

#### name 속성

name 속성은 **폼 이름**을 지정한다. 이 속성은 스크립트에서 폼을 참조할 때 필요하다.

```html
<form action="http://www.example.com/form.html/" method="post" name="profile_new"> </form>
```

### FIELDSET 요소

fieldset 요소는 관련 있는 **폼 필드 세트(form FIELD SET)**를 표시한다. 폼 필드 세트는 폼 내에서 관련 컨트롤을 하나의 그룹으로 묶은 것을 말한다.

```html
<form> <fieldset> ... </fieldset> </form>
```

- 폼을 효과적으로 계층화시킬 수 있다.
- legend 요소를 함께 사용해야 한다.

#### form 속성

form 속성은 해당 **fieldset 요소가 속해 있는 폼**을 지정한다. 이 속성을 지정하면 특정 form과 fieldset 요소의 관계를 명시적으로 연결할 수 있다. 이렇게 연결하면 브라우저는 두 요소 사이의 상호작용이 좀 더 쉽게 이루어질 수 있도록 도울 수 있으며 fieldset 요소가 form 요소 밖에 있더라도 둘 사이의 관계를 유지할 수 있다. 특히 하나의 fieldset 요소가 복수의 form 요소와 관계를 맺어야 할 때 효과적인 속성이다.

```html
<form id="user"> ... 
</form> 
<p>The fieldset below is outside the form element, but still part of the form</p> 
<fieldset form="user"> 
    <legend>법인등록</legend> 
    ... 
</fieldset>
```

### LEGEND 요소

legend 요소는 **fieldset 요소의 제목(LEGEND)**을 표시한다. fieldset 요소를 이용하여 여러 개의 컨트롤들을 묶었으면 이 묶음이 어떤 성격 또는 용도인지 알려줄 필요가 있으며, 이때 legend 요소를 사용한다.

```html
<form> 
    <fieldset> 
        <legend>개인정보:</legend> 
        <label>이름: <input type="text"></label><br> 
        <label>주소: <input type="text"></label><br> 
        <input type="submit"> 
    </fieldset> 
</form>
```

```html
<!-- 실습4 exam4 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<form action="...." method="get">
<fieldset>
	<legend>필수 항목</legend>
	<ul>
	<li>
		<label for=head_size>머리 둘레(cm)</label>
		<input id=head_size name=head_size type=number min=60 max=100 autofocus required>
	</li>
	<li>
		<label for=name>이름</label>
		<input id=name name=name type=text required maxlength=4>
	</li>
	<li>
		<label for=email>Email</label>
		<input id=email name=email type=email placeholder="example@xxx.yyy" required>
	</li>
	</ul>
</fieldset>
<fieldset>
	<legend>선택 항목</legend>
	<ul>
	<li>
		<label for=phone>연락처</label>
		<input id=phone name=phone type=tel 
		        placeholder="00*-000*-0000" 
		        pattern="[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}"> <!-- [0-9]{2,3} 0부터 9까지 숫자가 2개 아니면 3개 -->
	</li>
	<li>
		<label for=date_of_birth>생일</label>
		<!-- Date Type에도 min, max 사용가능 -->
		<input id=date_of_birth name=date_of_birth type=date min="1950-01-01" max="2000-01-01">
	</li>
	<li>
		<!--  url type은 유효성 검증은 하지 않음 -->
		<label for=homepage>홈페이지</label>
		<input id=homepage name=homepage type=url>
	</li>
	<li>
		<label for=favorite_color>좋아하는 색</label>
		<input id=favorite_color name=favorite_color type=color>
	</li>
	<li>
		<label for=gender>성별</label>
		<input id=gender name=gender type=text list=gender_list>
		<datalist id=gender_list>
			<option value=male label=남>
			<option value=female label=여>
		</datalist>
	</li>
	<li>
		<label for=favorite_star>좋아하는 연예인</label>
		<!-- 적어도 되지만 선택도가능 -->
		<input id=favorite_star name=favorite_star type=text list=favorite_star_list>
		<datalist id=favorite_star_list>
			<option value=윤아>
			<option value=태연>
			<option value=유리>
			<option value=제시카>			
		</datalist>
	</li>
	</ul>
</fieldset>
<!-- 비교!! button~~ -->
<button type="submit">Submit</button>
<button>Submit</button> <!--form 태그 안에서 사용하면 type속성 생략해도 버튼 태그는 submib 역할을 하게 된다.-->
<!-- 버튼 태그는 이미지도 사용가능 button 태그는 form 태그 밖에서도 사용가능하다 -->
<input type="submit"> <!-- value 속성을 생략했더니 제출이라고 사용됨 IE는 쿼리전송이라고 사용됨 -->
<!-- submit type은 폼 태그 안에서 사용해야한다. -->
<!-- button 보다 input 태그가 많이 사용됨 -->
<input type="reset">
</form>
</body>
</html>
```

[결과 화면]

![image-20200103204015912](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103204015912.png)

#### 실습5 exam5

줄바꾸기 기능을 하는 가장 일반적인 태그는 \<p>와 \<br>태그입니다.

**하나의 문단을 의미하는  태그**

p는 paragraph의 약자로 문단을 의미합니다.

```html
<p>태그와 </p>태그 사이에 위치하는 내용이 하나의 문단을 구성합니다.
<p>첫번째 문단(paragraph)</p>
<p>두번째 문단(paragraph)</p>
```

위와 같이 코딩하면 아래와 같이 첫번째 문단과 두번째 문단 사이에 공백라인이 들어갑니다.

```
첫번째 문단(paragraph)

두번째 문단(paragraph)
```

한글의 경우에는 문단의 첫글자를 들여쓰기 하지만 영문의 경우에는 문단과 문단 사이에는 한줄의 공백이 있습니다.

**강제 줄바꿈을 할때는 \<br> 태그**

br은 Line Break를 의미하며 우리말로 하면 강제 줄바꿈이라고 할 수 있습니다.

```html
<!--실습5-->
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>날짜와 시간 컨트롤 만들기</title>
</head>
<body>
	<form id="myForm"  method="get" action="not.jsp">
		<fieldset>
			<legend>날짜와 시간 컨트롤 만들기</legend>
			<p>
				<label>Date Picker 컨트롤에서 날짜를 선택하시오: <input type="date"  name="a"/>
				</label>
			</p>
			<p>
				<label>시간을 선택하시오: <input type="time"  name="b"/>
				</label>
			</p>
			<p>
				<label>날짜와 시간을 선택하시오(datetime-local): <input type="datetime-local"  name="c"/>
				</label>
			</p>
			<p>
				<label>월을 선택하시오: <input type="month"  name="d"/>
				</label>
			</p>
			<p>
				<label>주를 선택하시오: <input type="week"  name="e"/>
				</label>
			</p>
		</fieldset><br>
		<input type="submit" value="전달해보자">
	</form>
</body>
</html>
```

[결과 화면]

![image-20200103204600472](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103204600472.png)

#### 실습6 exam6

<input> 태그의 multiple 속성은 <input> 요소에 사용자가 둘 이상의 값을 입력할 수 있음을 명시합니다.

multiple 속성이 제대로 동작하는 <input> 요소의 type 속성값은 다음과 같습니다.

\- email, file

<input> 요소의 type 속성값이 “email”인 경우에는 이메일 사이에 콤마(,)를 추가하여 여러 이메일 주소를 동시에 입력할 수 있으며, type 속성값이 “file”인 경우에는 CTRL이나 SHIFT키를 사용하여 여러 파일을 동시에 선택할 수 있습니다.

multiple 속성은 불리언(boolean) 속성입니다.

불리언 속성은 해당 속성을 명시하지 않으면 속성값이 자동으로 false 값을 가지게 되며, 명시하면 자동으로 true 값을 가지게 됩니다.

```html
<!--실습6 exam6-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>&lt;select&gt; 태그, &lt;textarea&gt; 태그, file 타입의 &lt;input&gt; 태그</h2>
<form>
학년을 선택하세요 : 
<select name="grade">
	<option>1학년</option>
	<option>2학년</option>
	<option>3학년</option>
	<option>4학년</option>
</select><br>
<mark>댓글</mark>남기기 :<br>
<textarea name="memo" rows="10" cols="50"></textarea><br>
업로드할 파일을 선택하세요 :<br>
<input type="file" name="files" multiple>
</form>
</body>
</html>
```

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

#### 실습7 exam7

```html
<!--실습7 exam7-->
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

#### 실습 1 문제

![image-20200103172032110](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103172032110.png)

```html
<!--실습 1 문제-->
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
	<li>취미 : 향수 만들기</li>
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

#### 실습 2 문제

![image-20200103175457321](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103175457321.png)

```html
<!--실습2 문제-->
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

#### 실습 문제3

![image-20200103175546909](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103175546909.png)

```html
<!--실습 문제3-->
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

## colspan과 rowspan

표를 만들다 보면, 다음과 같이 셀을 병합하는 형태를 만들 필요가 있습니다.

| 참가자 | 점수 |      |
| :----: | :--: | ---- |
|  이름  | 나이 |      |
| 홍길동 | 19세 | 62점 |

colspan과 rowspan이 쓰인 예

여기서 보면, 두 번의 셀 병합이 있습니다. 하나는 '참가자' 셀이 가로로 두 칸을 차지하고, 다른 하나는 '점수' 셀이 세로로 두 칸을 차지하고 있습니다.

이럴 때 사용하는 것이 **colspan** 속성과 **rowspan** 속성입니다. 여기서 'colspan'은 가로로 합치는 것, 다시 말해 열(col)들을 병합(span: 걸치다)하는 속성이고, 'rowspan'은 세로로 합치는 것, 행(row)들을 병합하는 속성입니다. 이 속성은 th 또는 td에 사용할 수 있으며, 속성 값으로 병합할 셀의 숫자를 적습니다. 다음과 같이 사용합니다.

```html
<td colspan="2">참가자</td>
```

colspan에 속성 값을 2를 주어 두 개의 같은 행의 셀을 병합했습니다. 만약 다음과 같은 형태의 표를 만든다면 그 다음과 같이 작성합니다.	

![image-20200103194721713](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103194721713.png)

```html
<table>
  <tr>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
    <td colspan="2">c</td>
  </tr>
</table>
```

여기서 눈 여겨 봐야 할 것은 **병합된 셀의 수만큼 \**같은 행(tr) 안에 셀\**을 덜 적어 준 것**입니다.

그 다음은 rowspan 예시 입니다.

![image-20200103194821080](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200103194821080.png)

```html
<table>
  <tr>
    <td rowspan="3">a</td>
    <td>b</td>
  </tr>
  <tr>
    <td>c</td>
  </tr>
  <tr>
    <td>d</td>
  </tr>
</table>
```

여기서 참고 해야 할 부분은 **병합된 셀의 수 만큼 \**다음 행(tr)의 셀\** 개수가 하나씩 줄어들었다는 점** 입니다.

colspan과 rowspan은 표가 복잡해 질 수록, 조금 헷갈릴 수 있습니다. 하지만, 표를 몇 번 직접 작성 하다 보면, 금방 익숙해질 것 입니다.

- 테이블 요소들은 레이아웃이 아닌 도표의 의미가 필요할 때에만 사용.
- 테이블 요소들은 table 요소안에 포함.
- tr은 행, td는 셀.
- tr이 먼저 만들어지고, 그 안에 td가 들어가는 방식.
- 헤더, 제목이 되는 셀은 th 사용.
- colspan 속성은 열 병합, rowspan 속성은 행 병합.
- 셀 병합을 할 경우, 병합된 개수 만큼의 셀은 뺄 것.

참고 사이트: http://webberstudy.com/html-css/html-2/tables-and-layout/ 