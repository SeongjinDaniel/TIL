# Day4 JavaScript

이벤트 : 웹 페이지상에서 마우스, 키보드 등을 통해 발생하는 액션

​			  웹 브라우저에서 자동으로 발생하는 액션

이벤트 핸들러(리스너) : 이벤트가 발생했을 때 수행되는 기능을 구현한 함수

이벤트 타겟 : 이벤트가 발생한 대상 DOM 객체

​					  ((1)this, (2) 핸들러에 매개변수(e)를 하나 정의한 후 : e.target)

#### 실습 exam1

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

#### 실습 exam2

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

#### 실습 exam3

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
// setInterval 은 매초마다 주기적으로 사용할 때 사용
window.setTimeout(function() {
	dom.innerHTML = "오늘은 불금";
	dom.style.color ="red";
	dom.style.backgroundColor ="lime"; // 원래는 background-color 이지만 자바스크립트는 -기호 인정 X
}, 5000);
</script>
</body>
</html>
```

#### 실습 exam4

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

#### 실습 exam4_1

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

#### 실습 exam4_2

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

#### 실습 exam5

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

#### 실습 exam5_1

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

#### 실습 exam6

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>고전 이벤트 모델과 표준 이벤트 모델의 차이</h1>
<hr>
<button>고전 이벤트 모델</button>
<button>표준 이벤트 모델</button>
<script>
	var doms = document.querySelectorAll("button");
	var dom1 = doms[0];
	var dom2 = doms[1];
	
	// 고전은 똑같은 이벤트핸들러에 두개를 등록할수 없다.
	dom1.onclick = function () {
		alert("첫 번째 핸들러 수행(고전)");
	};
	dom1.onclick = function () {					
		alert("두 번째 핸들러 수행(고전)");
	};
	// 똑같은 이벤트 핸들러를 여러개 등록할수 있다.							  
	dom2.addEventListener("click", 
			                 function () { alert("첫 번째 핸들러 수행(표준)");});
	dom2.addEventListener("click", 
            function () { alert("두 번째 핸들러 수행(표준)");});

</script>
</body>
</html>
```

#### 실습 exam7

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 이벤트 모델</h1>
<hr>
<!-- 마우스 올릴때마다 경고창 뜬다. -->
<button onmouseover="test1();">인라인이벤트모델</button>
<!-- 한버만 수행 -->
<button id="b1">고전이벤트모델</button>
<button id="b2">표준이벤트모델</button>
<script>

function test1() {
	alert("인라인이벤트모델 버튼 클릭");
}
function test2() {
	alert("고전이벤트모델 버튼 클릭");
	btn1.onmouseover = null;
}
function test3() {
	alert("표준이벤트모델 버튼 클릭");
	btn2.removeEventListener("mouseover", test3);
}
var btn1 = document.querySelector("#b1");
var btn2 = document.getElementById("b2");
btn1.onmouseover = test2;  // 고전
btn2.addEventListener("mouseover", test3);
</script>
</body>
</html>
```

#### 실습 exam8

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>디폴트 이벤트 핸들러</h1>
<hr>
<!-- 인라인 이벤트 는 return false;를 사용하면 이벤트 핸들러 제외 -->
<!-- 고전 이벤트 는 return false;를 사용하면 이벤트 핸들러 제외 -->
<!-- 표준 이벤트 는 return false;를 사용하면 이벤트 핸들러 제외 --> 
<a href="http://www.w3schools.com/" onclick="test1(); return false;">HTML5 학습하기(인라인)</a><hr>
<a id="t1" href="http://www.w3schools.com/">HTML5 학습하기(고전)</a><hr>
<a id="t2" href="http://www.w3schools.com/">HTML5 학습하기(표준)</a>
<script>
function test1() {
	alert("인라인이벤트모델 버튼 클릭");
	//여기서 return false해도 소용없다
}
function test2() {
	alert("고전이벤트모델 버튼 클릭");	
	return false;
}
function test3(e) {
	e.preventDefault();
	alert("표준이벤트모델 버튼 클릭");	
}
var link1 = document.querySelector("#t1");
var link2 = document.getElementById("t2");
link1.onclick = test2;  // 고전
link2.addEventListener("click", test3);

</script>
</body>
</html>
```

#### 실습 exam9

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	section {
		border : 1px solid lime;	
		padding :10%;
		margin : 0px auto;	
	}
	div {
		border : 1px solid blue;	
		width : 80%;
		padding :10%;
		margin : 0px auto;	
	}
	h1 {
		border : 1px solid red;	
		width : 80%;
		padding :10%;
		margin : 0px auto;		
	}
</style>

</head>
<body>
  <section>
	<div>
		<h1>테스트</h1> <!-- h1 입장에서 div section body 모두 조상이다 -->
	</div>
  </section>
<script>
function clickHandler() {
	var dom1 = document.getElementsByTagName("h1")[0];
	var dom2 = document.getElementsByTagName("div")[0];
	var dom3 = document.getElementsByTagName("section")[0];
	var dom4 = document.getElementsByTagName("body")[0];
	dom1.addEventListener("click", displayAlert);
	dom2.addEventListener("click", displayAlert);	
	dom3.addEventListener("click", displayAlert);	
	dom4.addEventListener("click", displayAlert);	
}
function displayAlert(e) {
	window.alert(e.target+"\n"+e.currentTarget+"\n"+this);
	e.stopPropagation(); // 조상들한테 올리지마!
}
window.addEventListener("load", clickHandler);
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