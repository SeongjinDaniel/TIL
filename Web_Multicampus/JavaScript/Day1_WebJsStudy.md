# Day1 JavaScript

### JavaScript 구문

1. JavaScript 코드 작성 방법

2. 데이터타입과 변수선언

   숫자, 문자열타입, 논리타입, 객체타입(배열타입), undefined 타입

   var 변수명;

   var 변수명=초기값;

   e.g) var v1; -> v1은 undefined

   ​		v1 = 10; -> v1은 number

   ​		v1 = '10'; -> v1은 String

   ​		v1 = true; -> v1은 boolean

   ​		어떤 값을 가지고 있느냐에 따라 특성값이 달라진다.

   ---------------------------------------------------------------------------------> typeof 연산자가 필요

3. 연산자 (Java와 85% 비슷) ---> ==, === 등가 연산자가 3개짜리도 있다. !=, !==, && ||, delete, typeof .. 

4. 제어문 : for, foreach, while, do ~ while, break, continue

5. 함수의 정의와 활용

6. 객체의 생성과 활용(생성자 함수, 객체리터럴)

7. 예외처리

8. API

   표준API : 함수, 생성자 함수

   BOM(Browser Object Model) API : 브라우저가 자바스크립트에게 제공하는 것으로 내장 객체 형식

   DOM(Document Object Model) API

   HTML5 API - Canvas(움직이는 그림 같은거 그릴때 사용, 은근히 대기업들이 많이 사용), WebStorage, drag&drop, geolocation

### JavaScript의 정의방법

JavaScript 코드는 HTML 내의 어느 부분에 삽입해도 가능하나 주로 필요에 따라 <head> 태그나 <body> 태그에 삽입하게 되는데 헤더 부붂에 위치하게 JavaScript 코드는 컨텐트 (<body> 태그)내용의 랜더링 이에 브라우저
에 의해 먼저 해석되어 랜더링을 지연시키는 결과가 될 수도 있다.
이벤트 핸들러 기능의 JavaScript 코드는 가급적 <body 태그의 마지막 부분 즉, </body> 태그의 바로 위에 삽입한다.

### JavaScript의 데이터 타입

- JavaScript는 데이터 타입이 number, string, boolean, null 그리고 undefined 로 구붂되는 기본형 타입과 객체 타입으로 나뉜다.
- 숫자 타입 : 100, 3.14
- 문자열 타입 : "가나다", 'abc'
- 논리 타입 : true, false

### JavaScript의 주요 연산자

- 수치 연산자
  덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 나머지(%), 중가 연산자(++,--), 단항 연산자(-) 문자열 연산자 + : 문자열을 합하여 하나의 문자열 생성
  str = "ABCD" +"1234"; ==> "ABCD1234"
- 비교 연산자
  <,>,<=, <=, ==, ===, !=, !==
- 조건 연산자
  AND 연산자(&&), OR연산자(||), NOT 연산자(!), ? 연산자
- 대입 연산자
  =, += -=, *=, /=, %=
- 비트 연산자
  비트 AND(&), 비트 OR(|),비트 XOR(^), 비트 좌우 이동(<<,>>)
- 타입 점검 연산자
  typeof, instanceof
- 삭제 연산자
  delete

for(변수선언 : 컬렉션 또는 배열 객체)

for(변수선언 in 배열 객체 또는 일반 객체)

### JavaScript의 제어문

- 조건 제어문 if, 다중 분기문 switch
  switch 문에 사용되는 비교식에 데이터 타입의 제한이 없다.
- 반복 제어문 for, while, do-while
  for…in 반복문 사용이 가능하다(for-each 문이라고도 한다.)
  for…in 명령은 지정된 배열이나 객체 내의 요소/멤버에 대해 선두부터 마지막까지 순서대로
  반복 문장을 수행한다.
- 분기 제어문 break, continue
  중첩된 반복문에서 사용될 때 레이블을 사용하여 외부 반복문에 대한 제어가 가능하다.
- 예외처리 구문이 지원된다.
  try – catch – finally 구문을 사용하여 실행 오류 발생시의 대비 코드 구현이 가능하다.

#### 실습1 exam1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaScript학습</title>
</head>
<body>
<h1>자바스크립트 맛보기</h1>
<hr>
<!-- 자바스크립트는 script 태그 안에 써야한다! -->
<script>
	window.alert(1+2+3+4+5);
	console.log(1+2+3+4+5);
	document.write(1+2+3+4+5);
</script>
</body>
</html>
```

**[출력 화면]**

![image-20200107200151284](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107200151284.png)

![image-20200107195953002](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107195953002.png)

#### 실습2 exam2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>JavaScript 변수 선언과 활용</h1>
	<hr>
	<script>
		var v1;
		document.writeln(v1 + "<br>"); // 개행 문자는 blank로 인식
		v1 = 100;
		document.writeln(v1 + "<br>");
		v1 = '가나다';
		document.writeln(v1 + "<br>");
		var v1 = true;
		document.writeln(v1 + "<br>");
		v1 = 123;
		document.writeln(v1 + 45 + "<br>");
		v1 = '123';
		document.writeln(v1 + 45 + "<br>");
	</script>
	<h1>JavaScript 변수 선언과 활용</h1>	
</body>
</html>
```

**[출력 화면]**

![image-20200107200100430](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107200100430.png)

#### 실습3 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트와 데이터 타입 체크</h1>
<hr>
<script>
	document.write("<h2>" + typeof 100 + "</h2>");
	document.write("<h2>" + typeof 3.14 + "</h2>");
	document.write("<h2>" + typeof '가' + "</h2>");
	document.write("<h2>" + typeof "abc" + "</h2>");
	document.write("<h2>" + typeof '100' + "</h2>");
	document.write("<h2>" + typeof true + "</h2>");
	document.write("<h2>" + typeof undefined + "</h2>");
</script>
</body>
</html>
```

**[출력 화면]**

![image-20200107201658074](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107201658074.png)

#### 실습4 exam4

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 변수 선언과 활용(2)</h1>
<hr>
<script>
	document.write("<ul>");
	var v1;
	document.write("<li>"+ v1 +"</li>");
	document.write("<li>"+ typeof v1 +"</li>");
	document.write("<li>"+ (v1+10) +"</li>"); // NaN은 등가로 비교 불가 isNaN함수를 사용
	v1 = 100;
	document.write("<li>"+ v1 +"</li>");
	document.write("<li>"+ typeof v1 +"</li>");
	document.write("<li>"+ (v1+10) +"</li>");
	v1 = true;
	document.write("<li>"+ v1 +"</li>");
	document.write("<li>"+ typeof v1 +"</li>");
	document.write("<li>"+ (v1+10) +"</li>");
	v1 = "가나다";
	document.write("<li>"+ v1 +"</li>");	
	document.write("<li>"+ typeof v1 +"</li>");
	document.write("<li>"+ (v1+10) +"</li>");
	document.write("<ul>");
</script>
</body>
</html>
```

**[출력 화면]**

![image-20200107112143097](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107112143097.png)

#### 실습5 exam5

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 연산자(1)</h1>
<hr>
<pre>
<script>
	document.writeln(10>5);				// true
	document.writeln("abc">"ABC"); 		// true
	var str = "가나다";
	document.writeln(str == "가나다"); 	// true
	document.writeln(true == 1);		// true
	document.writeln("100" == 100);		// true type 확인 안하니까 true
	document.writeln(true === 1);		// flase
	document.writeln("100" === 100);	// false
	document.writeln(10/3);				// 3.3333333333333335
	document.writeln(10%3);				// 1
	var num=10;
	document.writeln(++num);			// 11
	document.writeln(--num);			// 10
</script>
</pre>
</body>
</html>
```

비교식1 && 비교식2 && 비교식3

비교식1 || 비교식2

----------------------------------------------------------------------> && 와 || 를 이용해서 if문을 대신하여 구현 가능

```java
// java
if(a>b)
    System.out.println(a);
```

```javascript
// javascript
if(a>b)
    window.alert(a);
//참이면
-----> a>b && window.alert(a); // if 문을 대신한다. 앞에것이 참이면 && 뒤에 것을 실행 왜 되냐? -> javascript는 if문 안에 boolean형이 아니어도 된다.
//거짓이면
-----> a<=b || window.alert(a);
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
<h1>자바스크립트의 연산자(2)</h1>
<hr>
<pre>
<script>
	var num=5;
	// num이 짝수이면 "xx는 짝수"
	// num이 홀수이면 "xx는 홀수"
	num % 2 == 0 && document.writeln(num+"는 짝수");
	num % 2 == 0 || document.writeln(num+"는 홀수");
</script>
</pre>
</body>
</html>
```

**[출력 화면]**

![image-20200107201848758](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107201848758.png)

```javascript
window.alert();		// 경고 메시지를 출력하는 서브창을 display -> 이게 떠있으면 다른것 안함(modal창)
window.prompt();	// 사용로 부터 데이터를 입력받는 서브창을 display
window.confirm();	// 확인받는 목적으로 사용되는 API로서 
				   // yes/no 형식의 데이터 입력받는 서브창을 display
```

#### 실습7 exam7

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	span { color : red; }
</style>
</head>
<body>
<h1>자바스크립트의 연산자(2)</h1>
<hr>
<pre> <!-- html에서는 개행 문자가 blank이다 하지만 행단위로 하려면 <br> 또는 <pre></pre>(free format) -->
<!-- 사용자가 원할 때까지 반복 -->
<script>
	//for(var su=1;su<4;su++){
	while(true){
		var num=window.prompt("체크하려는 숫자를 입력해 주세요.");
		//window.alert(num+":"+isNaN(num));	
		if(isNaN(num) || num == '' || num == null ) {
			document.writeln("<span>숫자</span>를 입력해 주세요!!!");
		} else {
			num % 2 == 0 && document.writeln(num+"는 짝수");
			num % 2 == 0 || document.writeln(num+"는 홀수");
		}
		var result = window.confirm("계속 수행할까요?");
		// 취소 버튼 누르면 break
		if(!result)
			break;
	}
</script>
</pre>
</body>
</html>
```

**[출력 화면]**

![image-20200107202015528](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202015528.png)

![image-20200107202025964](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202025964.png)

![image-20200107202041468](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202041468.png)

![image-20200107202052058](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202052058.png)

-> 취소 버튼 후 끝!!

![image-20200107202127420](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202127420.png)

#### 실습8 exam8

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>자바스크립트의 랜덤값 처리</h1>
<hr>
<script>
for(var i=0; i <10; i++){
	var rand = Math.random();// 0.0<= rand < 1.0
	console.log(rand);
	console.log(rand*3);
	console.log(Math.floor(rand*3));
	console.log("-----------------------");	
	document.write(Math.floor(rand*3) +"<br>");
}
</script>
</body>
</html>
```

**[출력화면]**

![image-20200107202226027](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107202226027.png)

------

### JavaScript의 배열 정의와  활용

- JavaScript 배열의 특징과 정의 방법
- JavaScript 배열의 특징

- 객체로 취급된다.

- 배열을 구성하는 각 데이터들을 요소라고 핚다.

- 배열의 요소 개수를 가변적으로 처리할 수 있다. 배열을 생성할 때 크기를 지정하더라도
  필요하다면 배열을 구성하는 요소의 개수를 늘리는 것이 가능하다.

- 배열에 저장할 수 있는 데이터의 타입에 제한이 없다.
  배열을 구성하는 각 요소릴다 다른 타입의 데이터를 저장하고 사용하는 것이 가능하다.

- length 라는 속성을 사용하여 배열을 구성하고 있는 요소의 개수를 추출할 수 있다.

- 배열을 생성하여 변수에 담아 사용한다.

- JavaScript의 배열 생성 방법은 2가지 방법이 지원된다.

- 배열 리터럴을 사용하는 방법(자동으로 배열 객체가 된다.)
  [ 1, 2, 3, 4, 5 ]

- Array() 라는 생성자 함수를 호출하여 배열 객체를 생성하는 방법
  new Array(10)

- **속성**

  1. 다양한 타입의 데이터를 하나의 배열에 구성 가능
  2. 배열 생성 후에도 크기 변경이 가능

- **생성**

  **배열 리터럴**

  ```javascript
  var a1 = [ ];
  var a2 = [ 10, 20, 30 ];             a2[10] = 100; //앞의 모든 방부터 11번째 방을 만들어서 넣는다.
  var a3 = [ true, '가나다', 100 ];
  
  a1.length
  
  a2.length
  
  a3.length
  
  a3[1] -> 가나다
  
  // 표준 API(Array라는 생성자 함수를 이용)
  
    var a4 = new Array();
    var a5 = new Array(10); // -> 10인 배열의 크기를 지정
    var a55 = new Array('abc');
    var a6 = new Array(10, 20);
    var a7 = new Array(true, 3, 5, 'aaa', 'aa');
  ```

  배열의 활용
  var array_example1 = new Array( "hello", "world" );
  var array_example2 = [ "hello", "world" ];
  var array_example3 = [];
  array_example3.push( "5" );
  array_example3.push( "7" );
  array_example3[ 2 ] = "2";
  array_example3[ 3 ] = "12";
  var array_example4 = [];
  array_example4.push( 0 ); // [ 0 ]
  array_example4.push( 2 ); // [ 0 , 2 ]
  array_example4.push( 7 ); // [ 0 , 2 , 7 ]
  array_example4.pop(); // [ 0 , 2 ]
  var array_example5 = [ "world" , "hello" ];
  // [ "hello", "world" ]
  array_example5.reverse();
  var array_example7 = [ 3, 4, 6, 1 ];
  array_example7.sort(); // 1, 3, 4, 6

  ```javascript
  var a = [10, 3, 7, 20, 6];
  a.sort(); //--> [ 10, 20, 3, 6, 7]
  		 //--> 문자열을 sort한다.
            //--> 문자열 sort를 하고 싶지 않다면 argument로 알맞는 함수를 준다.
            //--> a.sort([fnc]) 이렇게 함수를 줄수있다.
  		 // [fnc] -> function(a, b){return b-a} : desc
  		 // [fnc] -> function(a, b){return a-b} : asc
  ```

  #### 실습9 exam9

  ```javascript
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  <h1>배열 생성과 활용(1)</h1>
  <hr>
  <script>
  var a1 = [];
  document.write("<h3>"+ typeof a1 +"</h3>");
  document.write("<h3>"+ Array.isArray(a1) +"</h3>");
  document.write("<h3>"+ a1.length +"</h3>");
  document.write("<h3>"+ a1[0] +"</h3>");
  document.write("<hr>");
  a1[4] = 100;
  document.write("<h3>"+ a1.length +"</h3>");
  for(var i=0; i < a1.length; i++)
  	document.write("<h4>"+ a1[i] +"</h4>");
  document.write("<hr>");
  // java와 javascript의 foreach의 차이는 java는 값을 가져오지만 javascript는 index값을 이용한다.
  // foreach는 undefined가 아닌 값만 가지고 실행된다.
  for(var i in a1)  // for(int data : ary) // -> undefined를 제외시킴
  	document.write("<h4>"+ a1[i] +"</h4>");
  document.write("<hr>");
  var a2 = [10, '가나다', true, 3.5];
  for(var i in a2)  // for(int data : ary)
  	document.write("<h4>"+ typeof a2[i] + ":" + a2[i] +"</h4>");
  </script>
  </body>
  </html>
  ```

  #### 실습10 exam10

  ```javascript
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  <h1>배열 생성과 활용(2)</h1>
  <hr>
  <script>
  var a1 = new Array();  // [ ]
  var a2 = new Array(10); // 크기
  var a3 = new Array('가'); // 원소값
  var a4 = new Array(10, 20); // 원소값
  var a5 = new Array(1,2,3,4,5); // 원소값
  /* window.alert(a1.length);
  window.alert(a2.length);
  window.alert(a3.length);
  window.alert(a4.length);
  window.alert(a5.length); */
  document.write(a1.toString() + "<br>"); // a1만 써도 결과는 같다.
  document.write(a2.toString() + "<br>");
  document.write(a3.toString() + "<br>");
  document.write(a4.toString() + "<br>");
  document.write(a5.toString() + "<br>");
  var d = new Date();
  document.write(d.toString() + "<br>");
  document.write(d + "<br>");
  </script>
  </body>
  </html>
  ```

  **[출력결과]**

  ![image-20200107162250749](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200107162250749.png)

  #### 실습11 exam11

  ```javascript
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  <h1>배열 객체의 주요 메서드 활용</h1>
  <hr>
  <script>
  var ary = ['둘리', '또치', '도우너', '희동이', '고길동']
  document.write(ary + "<br>");
  var ary2 = ary.sort(); // sort를 호출하면 array 개체를 변경한다.
  document.write(ary + "<br>");
  document.write(ary2 + "<br>");
  document.write("<hr>");
  var ary3 = [30, 11, 5, 27, 9]
  document.write(ary3 + "<br>");
  var ary4 = ary3.sort(function(a, b){ return b-a;});
  document.write(ary3 + "<br>");
  document.write(ary4 + "<br>");
  document.write("<hr>");
  var ary5 = [ ];
  ary5.push(100);
  ary5.push(200);
  ary5.push(500);
  document.write(ary5 + "<br>");
  </script>
  </body>
  </html>
  ```

  #### 실습12 exercise3

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  <br>
  <!-- <pre> -->
  	<script>
  		var ary = [ 10, 5, 7, 21, 4, 8, 18 ];
  		var sum = 0;
  		for (var i = 0; i < ary.length; i++) {	
  			sum += ary[i];
  		}
  		document.writeln("모든 원소의 합 : " + sum +"<br>");
  		ary.sort(function(a, b) {
  			return a - b
  		});
  		document.write("");
  		document.writeln("<ul><li> 최댓값 : " + ary[ary.length - 1]+"</li>"+"<br>");
  		document.writeln("<li> 최솟값 : " + ary[0]+"</li>"+"<br></ul>");
  	</script>
  <!-- </pre> -->
  </body>
  </html>
  ```

  #### 실습13 exercise4

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  <script>
  	var ary = [];
  	for(var i = 0; i < 10; i++){
  		ary.push(Math.floor(Math.random()*50 + 1))
  	}
  	document.write("정렬 전 : " + ary + "<br>");
  	ary.sort(function(a, b){return a-b});
  	document.write("정렬 후 : " + ary + "<br>");
  </script>
  </body>
  </html>
  ```

  -----------------

  ### 함수

  - 수행 문장들을 담고 있는 호출 가능 모듈. 단독으로 호출 가능

  - JavaScript의 함수 정의 방법

  - 함수(function)란 하나의 로직을 재실행 핛 수 있도록 하는 것으로 코드의 재사용성을 높여준다.

  - **명시적(선언적) 방식 함수 정의**
    function myFunction([인자...[,인자]]) {
    /* do something */
    }

    function 함수이름([매개변수 선언...]){

    

    }

  - **리터럴(표현식, 익명) 방식 함수 정의**
    var myFunction = function([인자...[,인자]]) {
    /* do something */
    }

    function([매개변수 선언..]){

    

    }([아규먼트..]);

    함수(function([매개변수 선언..]){

    

    });

    var 함수명 = function([매개변수 선언..]){

    

    };

    --

    함수명([아규먼트..]);

    var 함수명2 = 함수명;

    -->  같은 함수를 함수명2로 사용 할 수 있다.

    ps)

    종종 매개변수(parameter)와 전달인자(argument)는 적당히 섞어서 쓰이기도 하는데, 이 경우 문맥에 따라 의미를 달리해서 해석되기도 한다. 하지만 엄밀히 말해서 매개변수는 함수의 정의부분에 나열되어 있는 변수들을 의미하며, 전달인자는 함수를 호출할때 전달되는 실제 값을 의미한다. 이같은 의미를 명확히 하기 위해 매개변수는 변수(variable)로, 전달인자는 값(value)으로 보는 것이 일반적이다.

  ### 메서드

  - 수행문장들을 담고 잇는 호출 가능 모듈. 객체를 통해서만 호출 가능

    객체의 멤버 정의되는 함수

  ### 전역코드

  - <script>수행문장들...</script>

  

  

### 웹페이지를 디자인 할 때

1. PC만

2. 모바일만

3. PC, 모바일 : 반응형 웹디자인 - www.w3schools.com

   ​					 PC 디자인, 모바일 디자인 분리 -  www.naver.com

   ​																			m.naver.com

   