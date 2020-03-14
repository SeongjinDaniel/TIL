## ES6 문법 정리

https://jsdev.kr/t/es6/2944

## 반응형 웹디자인

웹사이트의 레이아웃을 만들 때 방문자가 사용하는 모니터의 화면 해상도를 고려해야 합니다. 너무 크게 가로폭을 만들면 작은 해상도의 모니터로 접속했을 때 가로 스크롤이 생겨 컨텐츠를 보는 게 불편하기 때문입니다.

특히 스마트폰이나 태블릿 등 모바일 기기는 화면이 작기 때문에 가독성에 더욱 신경써야 합니다.

이러한 문제를 해결하는 방법 중의 하나가 반응형 웹디자인입니다. 해상도에 따라 가로폭이나 배치를 변경하여 가독성을 높이는 것입니다.

### @media

이러한 작업을 할 수 있게 해주는 것이 @media입니다. 예를 들어

```css
@media ( max-width: 768px ) {
  body { color: red; }
}
```

와 같이 하면, 웹브라우저의 가로 해상도가 768px 이하일 때 글자색을 빨간색으로 바꿉니다. 즉, 모바일 기기의 해상도를 고려하여 적절히 CSS를 수정하거나 추가하는 것이 가능합니다.

주의할 점은 가로폭 조정을 위해서 HTML 문서의 <head>와 </head> 사이에 다음의 코드를 넣어야 한다는 것입니다.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### 모바일 우선(Mobile First) VS 데스크톱 우선(Desktop First)

작은 가로폭부터 큰 가로폭 순서로 만드는 것을 모바일 우선(Mobile First), 큰 가로폭부터 작은 가로폭 순서로 만드는 것을 데스크톱 우선(Desktop First)이라고 합니다.

#### 모바일 우선(Mobile First)

작은 가로폭부터 큰 가로폭 순서로 만들고, min-width를 이용합니다.

```css
A
@media ( min-width: 768px ) {
  B
}
@media ( min-width: 1024px ) {
  C
}
```

기본 모양은 A, 768px 이상일 때는 B, 1024px 이상일 때는 C가 적용됩니다.

Bootstrap 등 대부분의 프레임워크는 모바일 우선으로 만들어져 있습니다.

#### 데스크톱 우선(Desktop First)

큰 가로폭부터 작은 가로폭 순서로 만들고, max-width를 이용합니다.

```css
A
@media ( max-width: 1023px ) {
  B
}
@media ( max-width: 767px ) {
  C
}
```

기본 모양은 A, 1023px 이하일 때는 B, 767px 이하일 때는 C가 적용됩니다.

### 예제 1

데스크톱 우선으로 만든 간단한 반응형 레이아웃 예제입니다.

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>CSS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      #jb-container {
        width: 940px;
        margin: 10px auto;
        padding: 20px;
        border: 1px solid #bcbcbc;
      }
      #jb-header {
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #bcbcbc;
      }
      #jb-content {
        width: 580px;
        padding: 20px;
        margin-bottom: 20px;
        float: left;
        border: 1px solid #bcbcbc;
      }
      #jb-sidebar {
        width: 260px;
        padding: 20px;
        margin-bottom: 20px;
        float: right;
        border: 1px solid #bcbcbc;
      }
      #jb-footer {
        clear: both;
        padding: 20px;
        border: 1px solid #bcbcbc;
      }
      @media ( max-width: 480px ) {
        #jb-container {
          width: auto;
        }
        #jb-content {
          float: none;
          width: auto;
        }
        #jb-sidebar {
          float: none;
          width: auto;
        }
      }
    </style>
  </head>
  <body>
    <div id="jb-container">
      <div id="jb-header">
        <h1>Responsive Layout</h1>
      </div>
      <div id="jb-content">
        <h2>Content</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec mollis nulla. Phasellus lacinia tempus mauris eu laoreet. Proin gravida velit dictum dui consequat malesuada. Aenean et nibh eu purus scelerisque aliquet nec non justo. Aliquam vitae aliquet ipsum. Etiam condimentum varius purus ut ultricies. Mauris id odio pretium, sollicitudin sapien eget, adipiscing risus.</p>
      </div>
      <div id="jb-sidebar">
        <h2>Sidebar</h2>
        <ul>
          <li>Lorem</li>
          <li>Ipsum</li>
          <li>Dolor</li>
        </ul>
      </div>
      <div id="jb-footer">
        <p>Copyright</p>
      </div>
    </div>
  </body>
</html>
```

기본 모양은 다음과 같습니다.

![image-20200314142403624](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200314142403624.png)

가로 해상도가 480px 이하면 가로폭이 줄어들고 사이드바가 밑으로 내려갑니다.

![image-20200314142420716](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200314142420716.png)

### 예제 2

위의 예제를 모바일 우선으로 만들려면 <style>의 내용을 다음과 같이 바꾸면 됩니다.

```css
<style>
  #jb-container {
    margin: 10px auto;
    padding: 20px;
    border: 1px solid #bcbcbc;
  }
  #jb-header {
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #bcbcbc;
  }
  #jb-content {
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #bcbcbc;
  }
  #jb-sidebar {
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #bcbcbc;
  }
  #jb-footer {
    padding: 20px;
    border: 1px solid #bcbcbc;
  }
  @media ( min-width: 481px ) {
    #jb-container {
      width: 940px;
    }
    #jb-content {
      width: 580px;
      float: left;
    }
    #jb-sidebar {
      width: 260px;
      float: right;
    }
    #jb-footer {
      clear: both;
    }
  }
</style>
```

---------

javascript에서 변수를 선언하고자 할 때 기본적으로 'var 변수명' 의 형태를 많이 사용한다.

뭐 그마저도 귀찮다면 var 도 생략하고 변수명에 값을 할당하는 방식을 쓰기도 하는데, 종종 보이는 '$변수명' 의 형태로 정의한 내용에 대해 차이점을 알아보고자 한다.



#### [javascript] 변수 선언 방식의 차이 : var name / $name

다들 아시다시피 변수 선언 시 사용되는 예약어인 var는 variable의 약자로 선언하는 위치에 따라 global scope, function scope로 사용된다. 간단하게 변수 범위에 대해서 짚고 넘어가자.

 

function 내부에서 선언한 변수는 **지역 변수(function scope)**로 해당 함수 내에서만 접근 및 호출가능하다.

정의한 함수 밖에서 호출하려고 하는 경우, 정의되지 않은 변수를 참조하려고 하여 Reference Error가 발생한다.

function 밖에서 선언한 변수는 모두 **전역 변수(global scope)**로 사용되며, 해당 페이지 내의 어떤 함수에서든 접근 및 호출할 수 있다.

또한 function 내부에서 선언하는 변수인 경우라도, 선언 명령어 var를 생략하고 변수를 선언하는 경우, 전역 변수로 사용되어 진다. 그렇기 때문에 지역 변수를 선언하는 경우는 반드시 변수를 선언하는 명령어를 써서 전역 변수와 구분해 주는 것이 좋다.

물론 전역 변수와 다른 이름을 쓰는 것이 가장 좋지만, function 내부에서만 사용하는 지역 변수라는 것을 나타낼 수 있으므로 명령어를 항상 표기하는 게 좋다고 생각된다.

 

오늘 내용에서 조금 벗어났지만, 변수 선언에 따른 범위에 대해 알아봤고

이제 본론으로 들어가서 변수명에 '$' 를 붙여주는 것과 붙이지 않는 것의 차이를 알아보자.

우리가 알고있는 일반적인 형태로 var name = "ojava"; 와 같이 선언한 변수는 일반 변수다.

그렇다면 var $jqvar의 형태로 선언한 값은 어떨까?

 

해당 변수도 일반 변수처럼 문자열이나 숫자를 담아서 사용할 수도 있겠지만, $가 일반적으로 jquery를 대표하는 문자로 사용된다는 것을 생각해보면 해당 변수에는 jquery object를 담는 변수임을 유추해 볼 수 있다. 

 

아래와 같이 아주 간단한 형태의 HTML과 script를 구현해보자.

물론 jsfiddle도 제공하니 코딩할 필요는 없다. https://jsfiddle.net/ojava/dsm0cb3q/1/

```html
<div id="blog">
	<p>ojava</p>
	<div class="info">
			ojava.tistory.com
		</div> 
	</div> 
	
<div id="print">
	<p>1111</p>
	<p class="result">2222</p>
</div>
```

```javascript
var $jqvar = $("#blog"); 
// var $jqvar가 가진 값 확인 
$("#print p:first").text($jqvar); 

// var $jqvar에서 jquery 기능 사용 
$("#print p.result").text(($jqvar.find("div.info").text()));

```

jquery 변수가 참조할 수 있는 blog라는 아이디값을 가지는 간단한 div 영역을 구성했고,

결과값을 보여줄 print라는 이름의 영역도 생성하였다.

jquery selector를 통해 $("#blog") 영역을 설정해두고 해당 변수가 어떤 값을 가지는 지 뿌려보았다.

[object Object]

javascript에서 jquery object를 뿌려주려고 하면 나오는 object Object가 띄워지는 것을 알 수 있다.

일단 일반 변수가 아닌 객체를 담을 수 있는 것은 확인하였고, 해당 객체에서 jquery 함수를 이용하여 객체에 접근하여 데이터 조회 등이 가능한지도 확인해보자.

$("#blog") 객체 하위의 info라는 class값을 가진 div의 text 값을 읽어오려고 한다.

해당 데이터는 $("#print p.result")에 입력되며, 코드를 실행하면 아래와 같은 값을 반환한다.

ojava.tistory.com

jquery selector 혹은 새롭게 선언한 객체를 담아두고 변수를 통해 참조해야 하는 경우,

변수명 앞에 $를 붙여서 jquery 변수로 사용하면 보다 쉽게 객체 사용이 가능하다는 점!

출처: https://ojava.tistory.com/143 [O! JAVA]

#### 변수 선언할때 var, $의 차이

var temp = '';
$temp = '';

```javascript
변수 var a 와 var $a 의 차이점.

1. var a;
자바스크립트 변수. 흔히 아는 방식으로 스크립트만 사용 가능하다.

2. var $a;
jQuery 변수. jQuery에서 사용하는 내장 함수들을 모두 사용할 수 있음.
ex) var a 는 a.css('backgroundcolor', 'blue') 라는 메소드가 안 먹음.
.css 메소드는 jQeury에서만 사용하는 것이므로.
var $a 는 jQuery 변수이므로 모든 스크립트 사용이 가능함.
.css(), .hide(), .show() 등등
```

```javascript
javaScript에서 $로 쓴다고해서 jQuery가 되는건 아닙니다.

jQuery가 지원하는 규칙에 주로 $가 절대 다수일 뿐이지요.


한국 사람이 쌀을 먹는다고 해서 

쌀을 먹는 사람이 한국 사람은 아니듯이.


pure js에서 다음 코드를 실행해보면 바로 확인되지요.

var a = 10;
alert(a);
var $a = 20;
alert($a);


그리고 일반 자바스크립트 객체는 그냥 쓰고

첫글자에 $를 써서 그것이 jQuery 확장 객체임을 

쉽게 구별하려는 의도일 뿐일 겁니다.
```

```
헝가리안 표기법으로 변수명 앞에 접두사를 붙여서 해당 변수가 참조하는 데이터의 타입을 명시해주려는 의도로 사용합니다. JavaScript가 동적 타입 언어라서 그래요. 아래 링크 참조 
https://jikime.tistory.com/305
```

---------

## JavaScript / 요소 추가하기 - .createElement(), .createTextNode(), .appendChild()

자바스크립트를 이용하여 문서에 HTML 요소를 추가할 수 있습니다. 이 때 필요한 자바스크립트 속성은 다음과 같습니다.

- .createElement()
- .createTextNode()
- .appendChild()

.createElement()는 요소를 만듭니다. 예를 들어

```javascript
.createElement( 'h1' )
```

은 다음과 같은 코드를 생성합니다.

```
<h1></h1>
```

.createTextNode()는 선택한 요소에 텍스트를 추가합니다. 예를 들어

```javascript
.createTextNode( 'My Text' )
```

는 My Text라는 문자열을 만듭니다.

.appendChild()는 선택한 요소 안에 자식 요소를 추가합니다.

다음은 Click이라는 텍스트를 가진 button 요소를 추가하는 예제입니다.

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>JavaScript</title>
  </head>
  <body>
    <script>
      var jbBtn = document.createElement( 'button' );
      var jbBtnText = document.createTextNode( 'Click' );
      jbBtn.appendChild( jbBtnText );
      document.body.appendChild( jbBtn );
    </script>
  </body>
</html>
```

```javascript
//각 줄의 의미는 다음과 같습니다.

var jbBtn = document.createElement( 'button' );
//button 요소를 만들고 jbBtn에 저장합니다.

var jbBtnText = document.createTextNode( 'Click' );
//Click이라는 텍스트를 만들고 jbBtnText에 저장합니다.

jbBtn.appendChild( jbBtnText );
//jbBtn에 jbBtnText를 넣습니다.

document.body.appendChild( jbBtn );
//jbBtn을 body의 자식 요소로 넣습니다.
```

------

