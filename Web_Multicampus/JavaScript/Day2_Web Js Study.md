# Day2 JavaScript

## 함수

#### 실습1 exam12

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>함수 정의와 활용(1)-선언적 함수 정의</h1>
<hr>
<script>
function f1(){
	document.write('f1() 호출<br>');
}
function f2(p1, p2){
	document.write('f2() 호출-' + (p1+p2) + '<br>');
}
f1();
f2(10, 20);
document.write('<hr>');
var result1 = f1();
var result2 = f2(100, 200);
document.write('result1 : ' + result1 + ' result2 :' + result2);
if(result1 == undefined){ // if(!result1)
	document.write('<br>리턴값이 없군요!!');
}
document.write('<hr>');
f1(100);
f2(100);
</script>
</body>
</html>
```

#### 실습2 exam13

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>함수 정의와 활용(2)-표현식 함수 정의</h1>
<hr>
<script>
var f1 = function() {
	document.write('f1() 호출<br>');
}
var f2 = function(p1, p2){
	document.write('f2() 호출-' + (p1+p2) + '<br>');
}
f1();
f2(10, 20);
document.write('<hr>');
var result1 = f1();
var result2 = f2(100, 200);
document.write('result1 : ' + result1 + ' result2 :' + result2);
if(result1 == undefined){ // if(!result1)
	document.write('<br>리턴값이 없군요!!');
}
document.write('<hr>');
f1(100);
f2(100);
document.write(typeof f1 + '<br>');
document.write(typeof f2 + '<br>');
</script>
</body>
</html>
```

#### 실습3 exam14

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>함수에서 데이터의 타입채크</h2>
<hr>
<!-- clickprocess는 이벤트 핸들러, 이벤트 핸들러를 사용하지 않으면 클릭해도 아무 액션을 하지 않는다. -->
<button onclick="clickProcess(100);">숫자</button>
<button onclick="clickProcess('100');">문자열</button>
<button onclick="clickProcess(true);">논리값</button>
<button onclick="clickProcess(function(){ });">함수</button>
<button onclick="clickProcess([ ]);">배열</button> <!-- 자바 스크림트 대괄호 -->
<button onclick="clickProcess({ });">객체</button> <!-- 중괄호 객체 = -->
<button onclick="clickProcess();">????</button>
<script>
function clickProcess(p) {
	if (typeof p == "number") {
		alert("숫자 전달!!");
	} else if (typeof p == "string") {
		alert("문자열 전달!!");
	} else if (typeof p == "boolean") {
		alert("논리값 전달!!");
	} else if (typeof p == "function") {
		alert("함수 전달!!");
	} else if (typeof p == "object") {
		if (Array.isArray(p))
			alert("배열객체 전달!!");
		else 
			alert("객체 전달!!");
	} else if (typeof p == "undefined") {  // p == undefined
		alert("전달된 아규먼트 없음!!");
	}	
}
</script>
</body>
</html>
```

#### 실습4 exam15

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>가변아규먼트 처리 함수 만들기</h1>
<hr>
<script>
function out(){
	document.write("아규먼트 갯수 : " + arguments.length + "<br>");
	for(var i = 0; i < arguments.length; i++)
		console.log(arguments[i]);
	console.log('-------------------');
}

out();
out(10); out(10, 20); out('a', 'b', 'c'); out(1, 2, 3, 4, 5, 6, 7, 8);
</script>
</body>
</html>
```

#### 실습5 exam16

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>함수의 아규먼트 처리</h1>
<hr>
<script>
function pr(p) {
	document.write(typeof p + " : " + p + "<br>");	
}
pr(100);
pr("100");
pr(true);
pr(3.5);
pr(new Array(1,2,3));
//prNum(10); // html 문서는 위에서부터 해석 되기때문에 error난다. 밑에 있는것은 읽을수 x
//document.write("ㅋㅋㅋㅋㅋㅋ");
</script>
<hr>
<script>
function prNum(p) {
	if(typeof p == "number")
		document.write("숫자 전달 : " + p + "<br>");
	else if (p == undefined)
		document.write("아규먼트를 전달하시오 : " + p + "<br>");
	else
		document.write(typeof p + " : " + p + "<br>");	
}
prNum(100);
prNum("100");
prNum(true);
prNum(3.5);
prNum(new Array(1,2,3));
prNum();
pr(100000); // 위에 script에 있는 함수도 호출 가능
</script>
<hr>
<script>
function prAll() {
	for(var i=0; i < arguments.length; i++)
		document.writeln(arguments[i]);
	document.write("<br>");
	return arguments.length;
}
var r1 = prAll(100);
var r2 = prAll(1,2,3,4,5);
var r3 = prAll('a', 'b', '가', true);
var r4 = prAll();
document.write(r1 + "<br>");
document.write(r2 + "<br>");
document.write(r3 + "<br>");
document.write(r4 + "<br>");
</script>
</body>
</html>
```

#### 실습6 exam17

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>아규먼트로 함수 전달하기(고차함수)</h1>
<hr>
<script>
	function output(p){
		if(typeof p == 'function'){
			p("ㅋㅋㅋ");
		} else{
			document.write("<h2> ㅋㅋㅋ : " + p + "</h2>")
		}
	}
	output("둘리");
	output(function(param){ console.log(param);})
	// function myAlert(param){
	var myAlert = function(param){
		window.alert(param);
	}
	output(myAlert);
	//output(myAlert()); 안됨!!
</script>
</body>
</html>
```

#### 실습7 exam18

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>고차함수 활용 예</h2>
<hr>
<p>5초후에 이 화면은 바뀝니다.</p>
<script>
	var displayDate = function(){
		var d = new Date();
		document.write(d.toLocaleString()+"<br>");
	};
	var time = 5000;
	window.setInterval(displayDate, time);
	// setInterval은 첫 아규먼트에 함수를 쓴다.

</script>
</body>
</html>
```

#### 실습8 exam19

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>자바스크립트 변수의 스코프(2)</h2>
<hr>
<script>
// 스코프는 언제 부터 언제까지 사용할 수 있냐이다!
var i = 100; // 전역 변수
//var i = 50; // 전역 변수 -> 가능!!
var sum = 0; // 전역 변수
document.write("i : " + i + "<br>");
for(var i=0; i < 10; i++) {
	sum += i;
}
document.write("i : " + i + "<br>");
document.write("sum : " + sum + "<br>");
</script>
</body>
</html>
```

#### 실습9 exam20

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>자바스크립트 변수의 스코프(2)</h2>
<hr>
<script src="util.js"></script>
<script>
var g_v = 100;
function scopeTest() {
	var l_v = 1000; // 지역변수
	writeNewLine("scopeTest() l_v : " + l_v);
	writeNewLine("scopeTest() g_v : " + g_v );
}
scopeTest();
try {
	// 이문장을 수행하다가 에러가 나면은 catch 블럭 수행해라
	writeNewLine("l_v : " + l_v  );
} catch(e) {
	writeNewLine(e);
}
writeNewLine("g_v : " + g_v );
</script>
</body>
</html>
```

#### 실습10 exercise5

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<script>
	function sum(p){
		var sum = 0;
		for(var i = 1; i <= p; i++)
			sum += i;
	
		return sum;
	}
	var rand = Math.random()*6;
	var result = 0;
	
	if(rand == 0) result = sum();
	else result = sum(rand);
	
	if(!result) document.writeln('결과값이 없어요!!<br>');  
	else document.writeln('호출 결과값 : ' + result); 
	
</script>
</body>
</html>
```

#### 실습11 exercise6

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- 같은 디렉토리에 있느면 그냥 사용 가능  반드시 사용전 보다 위에 있어야함-->
 	<script src="util.js"></script> 
	<script>
		function calc() {
			var sum = 0;
			if (arguments.length == 0)
				return 0;
			else {
				for (var i = 0; i < arguments.length; i++){
					if (isNaN(arguments[i]))
						return "숫자만 전달하세요";
					sum += arguments[i]*1;
				}
				return sum;
			}
		}
		
		write(calc(), "h3");
		write(calc(10, 20, '30'), "h3");
		write(calc(10, '가나다', 20), "h3");
		write(calc(1, 2, 3, 4, 5), "h3");
	</script>
</body>
</html>
```

#### 실습12 exercise7

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<script>
	function printH1(content){
		document.write("<h1>" + content + "</h1>");
	}
	function printH4(content){
		document.write("<h4>" + content + "</h4>");
	}
	function apply(ary , fnc){
		// instanceof 연산자로도 가능
		if(!Array.isArray(ary) || typeof fnc != 'function'){
			console.log('아규먼트 오류');
			return false;
		}
		else{
			for(var i = 0; i < ary.length; i++)
				fnc(ary[i]);
			return true;
		}
	}
	function success(suc){
		if(suc) window.alert("성공");
		else window.alert("실패");
	}
	
	var arr = [];
	var ret;
	while(1){
		var p=window.prompt("숫자나 문자열을 입력해 주세요.");
		if(!p) break;
		arr.push(p);
	}
	
	var d = new Date();
	var week = new Array('일', '월', '화', '수', '목', '금', '토');
	var day = week[d.getDay()];
	if(day == '월' || day == '수' || day == '금'){
		ret = apply(arr, printH1);
	}
	else if(day == '토'){
		ret = apply(arr);
	}
	else if(day == '일'){
		ret = apply('ㅋㅋㅋ', printH1);
	}
	else{// 화 목
		ret = apply(arr, printH4);
	}
	
	success(ret);

</script>
</body>
</html>
```

### JavaScript의 객체의 특징

- 객체란 이름과 값을 가진 data(Property) 의 집합 및 data 를 조작하기 위핚 Method 가
  하나로 묶인 것이다.
- JavaScript 에서 객체는 Property 의 집합과 하나의 prototype object 을 가지고 있다 .
- Method 는 함수가 값으로 저장된 객체의 Property 로서, 객체의 속성을 취득 및 변경 하기 위한 창구이다. 객체의 프로퍼티에 할당되어 객체를 통해서 호출되는 함수를 메서드라 부른다.
- 객체의 속성과 메서드는 동적으로 추가하거나 삭제하는 것이 가능하다.
- 상속구문도 적용되어 JavaScript 에서 생성되는 모든 객체들은 조상 객체로 Object 객체를 갖는다.
- JavaScript 의 함수는 실행 가능한 코드와 연결된 객체라 할 수 있다.

```javascript
obj.속성명(r-value, l-value), obj['속성명']   // -> 객체 내에서 변수에 한에서 문자열 형식으로 사용 가능하다.
obj.속성명()
```

#### 실습13 exam21

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 객체 생성과 사용(객체리터럴)</h1>
<hr>
<script src = "util.js"> </script>
<script>
	// 같은 객체를 또 다시 접근하려면 반드시 this를 사용해야한다.
	// this를 생략하면 window 객체에서 찾는다.
	var obj = {
			name : "듀크",
			eat : function(food) {
				writeColor(this.name + "가 " + food + "를 먹어요!!", "h3", "green");
			}
	}
	obj.eat("바나나");
	obj.eat("딸기");
	hr();
	writeColor(typeof obj, "h2", "red");
	// 자바는 객체를 만들면 객체 정보를 변경 할수 없지만 자바 스크립트는 변경 가능하다.(속성 추가 가능)
	obj.project = "자바스크립트";
	obj.study = function(){
		writeColor(this.name + "가 " + this.project + "를 공부해요!!", "h3", "magenta");
	}
	obj.study();
	hr();
	// 객체 일때는 index를 가져오는게 아니라 속성명을 가져온다.
	for(var key in obj)
		write(key + " : " + obj[key], "h4");
	
/* 	for(var key in obj)
		write(key + " : " + obj.key., "h4"); xxxxxxxxxxxx*/ 

	hr();
	write(obj.project, "h2");
	write(obj["project"], "h2");
	// 객체 속성 삭제
	delete obj.study;
	for(var key in obj)
		write(key + " : " + obj[key], "h4");
</script>
</body>
</html>
```

#### 실습14 exam22

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 객체 생성과 사용(객체리터럴)</h1>
<hr>
<script src = "util.js"> </script>
<script>
	var student = {
			name : "둘리",
			kor : 90,
			eng : 80,
			math : 95,
			getSum : function(){
				return this.kor + this.eng + this.math;
			},
			getAvg : function(){
				return this.getSum() / 3;
			},
			toString : function(){
				return this.name + "학생의 총점은 " + this.getSum() + "입니다.";
			}
	}
	write("총점 : " + student.getSum(), "h3");
	write("평균 : " + student.getAvg(), "h3");
	writeColor(student.toString(), "h3", "blue");
	writeColor(student, "h3", "blue");
/* 	for(var key in obj){
		write(key + " : " + obj[key], "h2");
	} */
</script>
</body>
</html>
```