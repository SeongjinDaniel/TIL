# Day3 JavaScript

#### 실습1  exam23

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaScript학습</title>
</head>
<body>
<h1>자바스크립트의 객체 생성과 사용(객체리터럴)</h1>
<hr>
<script src ="util.js"></script>
<script>
	var student1 = {
		name:'둘리',
		kor:90,
		eng:80,
		math:95,
		getSum: function(){
			return this.kor + this.eng + this.math;
		},
		getAvg: function(){
			return this.getSum() / 3;
		},
		toString: function(){
			return this.name+"학생의 총점은 " + this.getSum() + '입니다.';
		},
	}
	var student2 = {
		name:'도우너',
		kor:100,
		eng:80,
		math:55,
		getSum: function(){
			return this.kor + this.eng + this.math;
		},
		getAvg: function(){
			return this.getSum() / 3;
		},
		toString: function(){
			return this.name+"학생의 총점은 " + this.getSum() + '입니다.';
		},
	}
	var student3 = {
		name:'또치',
		kor:20,
		eng:90,
		math:95,
		getSum: function(){
			return this.kor + this.eng + this.math;
		},
		getAvg: function(){
			return this.getSum() / 3;
		},
		toString: function(){
			return this.name+"학생의 총점은 " + this.getSum() + '입니다.';
		},
	}
	writeColor("학생1 : "+student1, "h3", "blue");
	writeColor("학생2 : "+student2, "h3", "red");
	writeColor("학생3 : "+student3, "h3", "green");
</script>
</body>
</html>
```

#### 실습2 exam24

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaScript학습</title>
</head>
<body>
<h1>자바스크립트의 객체 생성과 사용(생성자 함수)</h1>
<hr>
<script src ="util.js"></script>
<script>
	function Student(p1, p2, p3, p4){ //첫 글자를 대문자로 쓰는 관례적인 규칙이 있음 - 일반 함수와 구분하기 위해
		this.name = p1;
		this.eng = p2;
		this.kor = p3;
		this.math = p4;

		this.getSum = function(){
			return this.eng + this.math + this.kor;
		}

		this.getAvg = function(){
			return this.getSum() / 3;
		}

		this.toString = function(){
			return this.name+"학생의 총점은 " + this.getSum() + '입니다.';
		}
	}

	var s1 = new Student('둘리', 90, 80, 95);
	var s2 = new Student('또치', 90, 100, 95);
	var s3 = new Student('도우너', 90, 50, 95);

	writeColor("학생1 : "+s1, "h3", "blue");
	writeColor("학생2 : "+s2, "h3", "red");
	writeColor("학생3 : "+s3, "h3", "green");
</script>
</body>
</html>
```

#### 실습3 exam25

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaScript학습</title>
</head>
<body>
<h1>자바스크립트의 객체 생성과 사용(생성자 함수)</h1>
<hr>
<script src ="util.js"></script>
<script>
	function Student(p1, p2, p3, p4){ //첫 글자를 대문자로 쓰는 관례적인 규칙이 있음 - 일반 함수와 구분하기 위해
		this.name = p1;
		this.eng = p2;
		this.kor = p3;
		this.math = p4;

	}

	Student.prototype.getSum = function(){
		return this.eng + this.math + this.kor;
	}

	Student.prototype.getAvg = function(){
		return this.getSum() / 3;
	}

	Student.prototype.toString = function(){
		return this.name+"학생의 총점은 " + this.getSum() + '입니다.';
	}
	var s1 = new Student('둘리', 90, 80, 95);
	var s2 = new Student('또치', 90, 100, 95);
	var s3 = new Student('도우너', 90, 50, 95);

	writeColor("학생1 : "+s1, "h3", "blue");
	writeColor("학생2 : "+s2, "h3", "red");
	writeColor("학생3 : "+s3, "h3", "green");
</script>
</body>
</html>
```



### JavaScript의 객체 정의와 활용

```javascript
//JavaScript의 객체 의 다양한 활용
var person1 = new Object();
person1.firstName = "duke";
alert( person1.firstName );
alert( person1["firstName"] );

var person2 = {
firstName: "duke",
lastName: "java"
};
alert( person2.firstName + " " + person2.lastName );

var people = { };
people[ "person3" ] = person1;
people.persion4 = persion2;
alert( people[ "person3" ].firstName );
alert( people.person3.firstName );
alert( people[ "person4" ].firstName );
alert( people.person4.firstName );

// 함수네임이 대문자(관례)이니까!! 객체
function Car (make, model, color) { 
    this.make = make; 
    this.model = model; 
    this.color = color; 
    this.displayCar = displayCar; 
}
function displayCar() { 
    document.writeln("Make = " + this.make) 
}
var myCar = new Car ("Ford", "Focus", "Red"); 
myCar.displayCar(); 
myCar.make = "BMW"; 
myCar.displayCar();
```



### BOM(Browser Object Model)

- window, document, location(3초뒤에 넘어갑니다 등등), history(앞, 뒤로 가기 방문 페이지 가기 등), navigator, screen

  location.href : 페이지 이동을 구현하고자 할 때

  location.reload() : 현재 페이지를 재요청

  navigator.userAgent : 이 페이지를 랜더링하고 있는 클라이언트 머신과 브라우저 정보를 하나의 문자열로 추출

  #### 실습4 exam1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<form name="fm">
	<select id="choice" onchange="go();"> <!-- change이벤트 발생하면 go라는 함수 실행 -->
		<option value="">---관심있는 기술을 선택해 주세요---</option>
		<option value="http://www.w3schools.com/js/default.asp">Learn JavaScript</option>
		<option value="http://www.w3schools.com/js/js_htmldom.asp">Learn HTML DOM</option>
		<option value="http://www.w3schools.com/jquery/default.asp">Learn jQuery</option>
		<option value="http://www.w3schools.com/xml/ajax_intro.asp">Learn AJAX</option>
		<option value="http://www.w3schools.com/js/js_json_intro.asp">Learn JSON</option>
	</select>
</form>
<script>
window.alert(location.href);
function go(){	
	location.href = document.getElementById("choice").value;
	//location.href = document.querySelector("#choice").value; // # : id 선택자
	//location.href = "http://www.naver.com/";
}
</script>
</body>
</html>
```

#### 실습5 exam2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insert title here</title>
<script src="../util.js"></script>
<!-- <script src="/edu/jsexam/util.js"></script> -->
<!-- <script src="http://localhost:8000/edu/jsexam/util.js"></script> -->
</head>
<body>
<h1>navigator 내장객체</h1>
<hr>
<script>
write(navigator.platform, "h3"); //
write(navigator.userAgent, "h3"); // 브라우저 정보
var str = navigator.userAgent; // 현재 브라우저가 모바일인지 아닌지를 확인 가능
if (str.match(/(ipad)|(iphone)|(ipod)|(android)|(webos)/i)) // ipad, iphone...가 있으면, 대소문자 구분x
      write("모바일 디바이스 이군요", "h2");
else
      write("모바일 디바이스가 아니군요", "h2");
</script>
</head>
<body>
```

#### 실습6 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
//변수를 선언합니다.
var child = window.open('/edu/first.html', '', 'width=300, height=200');
var width = screen.width;
var height = screen.height;
child.moveTo(0, 0);
child.resizeTo(width, height); // width, height만큼 변경해라   
window.setInterval(function () {
    child.resizeBy(-20, -20); // 현재 크기에서 줄여라
    child.moveBy(10, 10); // 현재 위치에서 10px 만큼씩 이동
}, 2000);  //2s에 한번
</script>
</head>
<body>
</body>
</html>
```

```
[결과]
navigator 내장객체
---------------------------------------------------------------------------
Win32
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
모바일 디바이스가 아니군요
```

#### 실습7 exam4

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
	var child = window.open('', '', 'width=300, height=200');
	child.moveTo(0, 0);

	//setInterval은 윈도우 객체 이기 때문에 window 생략 가능!
	//window.setInterval(function() {
	setInterval(function() {
		child.moveBy(10, 10);
		child.document.write(new Date());
	}, 1000); // 1s에 한번
</script>
</head>
<body>
</body>
</html>
```



### DOM(Document Object Model)

- 브라우저의 HTML 파서가 서버로 부터 전달받은 HTML 문서의 내용을 파싱하고 랜더링할 때 인식된 HTML 태그, 속성, 그리고 텍스트로 구성된 컨텐츠를 하나하나 JavaScript 객체로 생성한다. 이 때, 만들어지는 DOM 객체들(Element 객체, Text 객체) 부모 자식 관계를 유지해서 트리 구조를 형성한다.

  --> JavaScript 코드로 HTML 태그나 속성 컨텐츠를 읽거나 변경할 수 있게 지원해서 동적인 웹페이지를 생성

- 파싱 : HTML 태그 내용을 읽는 것

- 랜더링 : 화면에 출력 되는것!

1. 필요한 태그를 찾는 방법

   - document : 대부분의 dom 객체는 document 의 자손이다.

     ```javascript
     document.getElementsByTagName("태그명"); // 복수형(0개이상 찾음) NodeList
     document.getElementById("태그의id속성값"); // 단수형(1개만 찾음) Node
     document.getElementsByClassName("태그의class속성값"); // 복수형 NodeList
     // 주로 이 것들을 많이 사용하고 추가된 것들이 있음↓
     // CSS선택자를 사용해서 태그를 찾을수 있음
     document.querySelector("CSS선택자"); // 단수형 Node
     document.querySelectorAll("CSS선택자"); // 복수형 NodeList
     // NodeList 배열이라고 생각하고 꺼내서 사용 가능
     ```

2. 태그의 내용이나 속성을 읽고 변경하는 방법, 삭제하는 방법

   ```javascript
   찾은Element객체.innerHTML
   찾은Element객체.textContent
   // 이둘을 사용하면 왠만한 편집작업은 쉽게 할 수 있다.
   // 현재는 표준이 되었다.
   //↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
   
   찾은Element객체.getAttribute("속성명")
   찾은Element객체.setAttribute("속성명", 속성값)
   찾은Element객체.removeAttribute("속성명")
   찾은Element객체.속성명
   찾은Element객체.속성명 = 속성값
   ```

   

3. 태그에서 발생하는 이벤트 또는 브라우저 객체에서 발생하는 이벤트(window)에 대한 이벤트 핸들러 구현 방법

   - 인라인 이벤트 모델

     ```html
     <button onclick="코드">1</button>
     ```

   - 전역적 이벤트 모델(고전 이벤트 모델)

     ```html
     <button>2</button>
     ```

     ```javascript
     var dom = document.getElementsTagName("button")[0]; // 첫번째 버튼 Tag
     dom.onclick = function() { 코드 };
     ```

     

   - 표준 이벤트 모델

     ```html
     <button>3</button>
     ```

     ```javascript
     var dom = document.getElementsTagName("button")[0]; // 첫번째 버튼 Tag
     dom.addEventListener("click", function() { 코드 });
     ```

#### 실습8 exam1

```html
	<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>컨텐트1</h1>
<h1>컨텐트2</h1>
<h1>컨텐트3</h1>
<h1>컨텐트4</h1>
<h1>컨텐트5</h1>
<h2>컨텐트5</h2>
<script src="../util.js"></script>
<script>
var h1dom=document.getElementsByTagName("h1");
write(h1dom.length, "h3");
for(var i=0;i<h1dom.length;i++)
   writeColor(h1dom[i].textContent,"h4", "red");
   
var h2dom = document.getElementsByTagName("h2");
writeColor(h2dom[0].textContent, "h2", "green");
writeColor(h1dom[0], "h2", "blue");
writeColor(h2dom[0], "h2", "blue");

var h5dom = document.getElementsByTagName("h5");
writeColor(h5dom.length, "h5", "magenta");
</script>
</body>	
</html>
```

```
[결과]
컨텐트1
컨텐트2
컨텐트3
컨텐트4
컨텐트5
컨텐트5
5
컨텐트1 -> (red)
컨텐트2 -> (red)
컨텐트3 -> (red)
컨텐트4 -> (red)
컨텐트5 -> (red)
컨텐트5 -> (green)
[object HTMLHeadingElement] -> (blue)
[object HTMLHeadingElement] -> (blue)
0  -> (magenta)
```

#### 실습8 exam2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<script src = "../util.js"></script>
<script>
		// 이벤트 핸들러로써의 기능을 하기 떄문에 그때 그때 사용!
		window.onload = function() {
		var dom1 = document.getElementById("t1");
		console.log(dom1);
		console.log(dom1.textContent);
		var dom2 = document.getElementById("t3");
		console.log(dom2);
		var dom3 = document.getElementById("t4");
		console.log(dom3);
		var dom4 = document.getElementById("t5");
		console.log(dom4);
		console.log(dom4.getAttribute("src")); // src에 작성한 대로 추출
		console.log(dom4.src); // 절대 URL로 추출 
		var dom5 = document.getElementById("p");
		// textContent는 HTML 태그를 사용할 수 없다.
		// 사용하려면 innerHTML을 사용해야한다.
		//dom5.textContent = "<h2>" + new Date().toLocaleString() + "</h2>";
		
		dom5.innerHTML = "<h2>" + new Date().toLocaleString() + "</h2>";
	}
</script>
<h1 id = "t1">컨텐트1</h1>
<h2 id = "t2">컨텐트5</h2>
<p id = "t3">컨텐트2</p>
<div id = "t4">컨텐트2</div>
<img id = "t5" src="../../images/totoro.png" width="100">
<hr>
<output id = "p"></output> <!-- javaScript의 수행능력을 표현하는 용도 ?-->
<hr>

</body>
</html>
```

#### 실습9 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="../util.js"></script>
</head>
<body>
<h1 id="test">DOM객체를 찾자</h1>
<h1>ㅋㅋㅋㅋㅋㅋㅋ</h1>
<hr>
<script>
var dom = document.getElementsByTagName("h1");
write(dom, "h2");
write(dom[1], "h2");
write(dom[1].textContent, "h2"); // innerText
write(dom[1].innerHTML, "h2");
hr();
dom = document.getElementById("test");
write(dom, "h2");
write(dom.textContent, "h2");
window.setTimeout(function() {
	dom.innerHTML = "오늘은 월요일";
	dom.style.color ="red";
	dom.style.backgroundColor ="lime";
}, 5000);
</script>
</body>
</html>
```

#### 실습10  exam4

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>exercise8</h1>
<hr>
<script src ="util.js"></script>
<script>
	function Objj(p1, p2, p3){
		this.tag = p1;
		this.color = p2;
		this.msg = p3;
	}
	
	Objj.prototype.toString = function(){
		return "tag : " + this.tag + " color : " + this.color + " msg : " + this.msg;
	}

	function printObject(p){
		if(typeof p == 'object'){
			writeColor(p, "h3", p.color);
		}
		else return;
	}
	
	var s1 = new Objj('둘리', "blue", '둘리입니다.');
	var s2 = new Objj('또치', "red", '또치입니다.');
	var s3 = new Objj('도우너', "green", '도우너입니다.');

	printObject(s1);
	printObject(s2);
	printObject(s3);

</script>
		
</body>
</html>
```

#### 실습11  exam5

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>exercise9</h1>
<hr>
<script src ="util.js"></script>
<script>
	function DayInfo(_name, _year, _month, _day){
		this.name = _name;
		this.year = _year;
		this.month = _month;
		this.day = _day;
	}
	
	DayInfo.prototype.getTotalDays = function(){
		//var curDate = new Date();
		//var ourDate = new Date(this.year, this.month-1, this.day);
		var dday = new Date() - new Date(this.year, this.month-1, this.day);
		//var dday = curDate.getTime() - ourDate.getTime();
		var toCur = Math.floor(dday / (24 * 60 * 60 * 1000)); // 시 * 분 * 초 * 밀리세컨
		return this.name + "님은 태어난지 " + toCur + "일 되었어요.";
	}
    
	DayInfo.prototype.getKorDay = function(){
    	var dday = new Date(this.year, this.month-1, this.day);
    	var week = new Array('일', '월', '화', '수', '목', '금', '토');
    	var day = week[dday.getDay()];
    	return this.name + "님은 " + day + "요일에 태어났어요.";
	}
	
	var s1 = new DayInfo("me", 1991, 03, 24);
	var s2 = new DayInfo("you", 1997, 03, 21);
	var s3 = new DayInfo("other", 2020, 01, 08);
	
	writeColor(s1.getTotalDays(), "h3", "red");
	writeColor(s2.getTotalDays(), "h3", "blue");
	writeColor(s3.getTotalDays(), "h3", "green");
	
	writeColor(s1.getKorDay(), "h3", "red");
	writeColor(s2.getKorDay(), "h3", "blue");
	writeColor(s3.getKorDay(), "h3", "green");

</script>
</body>
</html>
```

#### 실습12  exam6

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<script>
		//document.write(Math.random()*3 + 1);
		var check = window.confirm("page 이동할까요?");
		if(!check){
	 		var child = window.open('/edu/first.html', '', 'width=300, height=200');
			var width = screen.width;
			var height = screen.height;
			child.resizeTo(width, height);  
		}
		else{
			switch(Math.floor(Math.random()*3 + 1)){
			case 1:
				location.href = "http://www.daum.net/"
				break;
			case 2:
				location.href = "http://www.naver.com/"
				break;
			case 3:
				location.href = "http://www.google.com/"
			}
		}
	</script>
</body>
</html>
```

