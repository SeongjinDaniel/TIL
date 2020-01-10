# Day4 JavaScript

이벤트 : 웹 페이지상에서 마우스, 키보드 등을 통해 발생하는 액션

​			  웹 브라우저에서 자동으로 발생하는 액션

이벤트 핸들러(리스너) : 이벤트가 발생했을 때 수행되는 기능을 구현한 함수

이벤트 타겟 : 이벤트가 발생한 대상 DOM 객체

​					  ((1)this, (2) 핸들러에 매개변수(e)를 하나 정의한 후 : e.target)

#### 실습1 exam3

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

#### 실습2 exam4

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>시간정보 출력하기</h1>
<hr>
<button onclick="startTime()">시간을 알려주라옹...</button>
<button onclick="stopTime()">시간 출력을 종료하라옹...</button>
<output></output>
<script>
var target = document.getElementsByTagName("output")[0];
function startTime() {
	var d = new Date();
	target.innerHTML = "<h2>"+d.toLocaleString()+"</h2>";
}
function stopTime() {
	target.innerHTML = "";
}
</script>
</body>
</html>
```

#### 실습3 exam4_1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>시간정보 출력하기</h1>
<hr>
<button onclick="startTime()">시간을 알려주라옹...</button>
<button onclick="stopTime()">시간 출력을 종료하라옹...</button>
<output></output>
<script>
var target = document.getElementsByTagName("output")[0];
var setId;
function startTime() {
	var d = new Date();
	target.innerHTML = "<h2>"+d.toLocaleString()+"</h2>";
	// startTime을 다시 1초후에 호출, setId는 clearTimeout에서 사용됨
	setId = window.setTimeout(startTime, 1000);
}
function stopTime() {
	//target.innerHTML = "";
	window.clearTimeout(setId);
}
</script>
</body>
</html>
```

#### 실습4 exam4_2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>시간정보 출력하기</h1>
<hr>
<button onclick="startTime()">시간을 알려주라옹...</button>
<button onclick="stopTime()">시간 출력을 종료하라옹...</button>
<output></output>
<script>
// setInterval()을 사용하여 동일한 기능 구현
var target = document.getElementsByTagName("output")[0];
var setId;
function startTime() {
	setId = window.setInterval(function(){
		var d = new Date();
		target.innerHTML = "<h2>"+d.toLocaleString()+"</h2>";
	}, 1000);
}
function stopTime() {
	//target.innerHTML = "";
	window.clearInterval(setId);
}
</script>
</body>
</html>
```

#### 실습5 exam5

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>세 가지 이벤트 모델</h1>
<hr>
<h1 onclick="f1();">인라인 이벤트 모델</h1>
<hr>
<h1 id="t1">고전 이벤트 모델</h1>
<hr>
<h1 id="t2">표준 이벤트 모델</h1>
<hr>
<script>
	function f1() {
		alert(document.querySelectorAll('h1')[1].textContent); //querySelectorAll('h1')[1] 모든 h1을 찾아라 1index번째인 =
	}
	var dom2 = document.querySelector('#t1');
    var dom3 = document.querySelector('#t2');
	function f2() {
		alert(dom2.textContent);
	}
	function f3() {
		alert(dom3.textContent);
	}    
    dom2.onclick = f2;
    dom3.addEventListener("click", f3); // 함수 이름만 주어야한다.!!
</script>
</body>
</html>
```

#### 실습6 exam5_1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>세 가지 이벤트 모델</h1>
<hr>
<h1 onclick="f1();">인라인 이벤트 모델</h1>
<hr>
<h1 id="t1">고전 이벤트 모델</h1>
<hr>
<h1 id="t2">표준 이벤트 모델</h1>
<hr>
<script>
    console.log(this);
	function f1() {
		alert(document.querySelectorAll('h1')[1].textContent);
	}
	var dom2 = document.querySelector('#t1');
    var dom3 = document.querySelector('#t2');
	function f2() { //f2(e) {
		//alert(e.target.textContent);
		alert(this.textContent);
	} 
    dom2.onclick = f2;
    dom3.addEventListener("click", f2);
</script>
</body>
</html>
```

#### 실습7 exercise11_1

[문제]

파일명 : exercise11.html

제시된 exercise11.html 파일을 가져가서 
다음에 제시된 기능을 자바스크립트로 구현해 본다.

1) <body> 태그안의 <h2> 태그를 찾아서 
    "오늘은 XXXX년 X월 X일입니다." 를  출력하는 자바스크립트 코드를 작성한다.

2) 제시된 버튼이 클릭되면 
    위에 출력된 "오늘은 XXXX년 X월 X일입니다."의 칼라로
    변경하는 이벤트 핸들러 구현을 3가지 방법으로 구현한다.

    exercise11_1.html - inline 방식
    exercise11_2.html - 전역 방식
    exercise11_3.html - 표준 방식
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<script src="/edu/jsexam/util.js"></script>
	
	<h2>오늘은 XXXX년 X월 X일입니다.</h2>
	<button onclick="total('red');">빨강색</button>
	<button onclick="total('blue');">파랑색</button>
	<button onclick="total('yellow');">노랑색</button>
	
	<script>
	
	var dom = document.getElementsByTagName("h2")[0];
	var dateInfo = new Date();
	dom.textContent = "오늘은" + dateInfo.getFullYear() + "년"
						+(dateInfo.getMonth() + 1) + "월"
						+dateInfo.getDate() + "일"
	 
	var total = function(color) {		
			dom.style.color = color;
	}

	</script>
</body>
</html>
```

#### 실습8 exercise11_2

```html

```



**hml 태그 표준 속성이 아닐때 data-~~~~라고 쓰면 허용가능!**

data-xxx : 사용자가 필요에 의해 태그에 정의하는 속성

**[디폴트 이벤트 핸들러]**

HTML 태그에 디폴트로 등록되어 있는 이벤트 핸들러를 의미한다.

태그에 따라서는 눈에 띄는 디폴트 이벤트 핸들러를 가지고 있다.

```html
<a> : click 이벤트에 대한 핸들러를 내장하고 있다.
<form> :  submit 이벤트에 대한 핸들러를 내장하고 있다.

<a href = "http://java.sun.com/">...</a>
<a href = "test.html/">...</a>
<a href = "#memo/">...</a> <!--#뒤에 온것을 #앵커명-->
<a href = "test.html#subject/">...</a>
    
<!--웹페이지에 부분에 대하여 앵커명을 지정해서 사용하기도 함!!-->
<a name ="memo"></a>
```



-------

**[이벤트 버블링]**

특정 DOM 객체에서 이벤트가 발생하면 그 DOM 객체에 등록된 이벤트 핸들러만 수행되는 것이 아니라 조상 DOM 객체에 등록된 핸들러도 수행된다.

#### 실습? exam9