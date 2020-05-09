# jQuery (by 생활코딩)

#### jQuery

```
$(제어대상).method1().method2();
    주어          서술어
```

-----

#### JavaScript

```html
<html>
    <head>
        <script type="text/javascript">
            function addEvent(target, eventType,eventHandler, useCapture) {
                if (target.addEventListener) { // W3C DOM
                    target.addEventListener(eventType,eventHandler,useCapture?useCapture:false);
                } else if (target.attachEvent) {  // IE DOM
                    var r = target.attachEvent("on"+eventType, eventHandler);
                }
            }
 
     
            function clickHandler(event) {
                var nav = document.getElementById('navigation');
                for(var i = 0; i < nav.childNodes.length; i++) {
                    var child = nav.childNodes[i];
                    if(child.nodeType==3)
                        continue;
                    child.className = '';
                }
                event.target.className = 'selected';
            }
  
            addEvent(window, 'load', function(eventObj) {
                var nav = document.getElementById('navigation');
                for(var i = 0; i < nav.childNodes.length; i++) {
                    var child = nav.childNodes[i];
                    if(child.nodeType==3)
                        continue;
                    addEvent(child, 'click', clickHandler);
                }
            })
        </script>
        <style type="text/css">
            #navigation li {
                list-style:none;
                float:left;
                padding:5px;
            }
            #navigation {
                cursor:pointer;
            }
            #navigation .selected {
                background-color:red;
                color:white;
            }
        </style>
    </head>
    <body>
        <ul id="navigation">
            <li>HTML</li>
            <li>CSS</li>
            <li>javascript</li>
            <li class="selected">jQuery</li>
            <li>PHP</li>
            <li>mysql</li>
        </ul>
    </body>
</html>
```

#### JQuery

```html
<html>
    <head>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            $('#navigation li').on('click', function() {
                $('#navigation li').removeClass('selected');
                $(this).addClass('selected');
            })
        </script>
        <style type="text/css">
            #navigation li {
                list-style:none;
                float:left;
                padding:5px;
            }
            #navigation {
                cursor:pointer;
            }
            #navigation .selected {
                background-color:red;
                color:white;
            }
        </style>
    </head>
    <body>
        <ul id="navigation">
            <li>HTML</li>
            <li>CSS</li>
            <li>javascript</li>
            <li class="selected">jQuery</li>
            <li>PHP</li>
            <li>mysql</li>
        </ul>
    </body>
</html>
```

jQuery 1.7에 와서, .live() 함수는 사용이 중지되고, on() 함수로 대체되었습니다. (이벤트연결 기능)중요한 사항이니 꼭 참고!!

----------------

#### 레퍼(wrapper)란?

**jQuery(엘리먼트 오브젝트 | 'CSS스타일 선택자')**

붉은색으로 표시한 부분이 레퍼, 인자로 전달된 요소들에 jQuery의 기능성을 부가해서 반환

####  레퍼의 안전한 사용

$(엘리먼트) 와 jQuery(엘리먼트)는 같은 의미이지만 $를 사용하는 다른 라이브러리들과의 충돌 때문에 다음과 같은 방법을 사용한다.

```html
<script type="text/javascript">
//$ 대신 jQuery를 사용
jQuery('body').html('hello world');
</script>
```

```html
<script type="text/javascript">
//$를 함수의 지역변수로 선언해서 외부에 있을지 모르는 타 라이브러리의 $와의 충돌을 예방
(function($){
    $('body').html('hello world');
})(jQuery)
</script>
```

#### 제어 대상을 지정하는 방법

- jQuery( selector, [context] )  // selector : "문자열", 두번째 인자는 대괄호로 되어 있기 때문에 옵션이라는 뜻이다.생략가능
- jQuery( element )

**예제 1.** jQuery( selector, [context] )

```html
<html>
    <body>
        <ul>
            <li>test2</li>
        </ul>
        <ul class="foo">
            <li>test</li>
        </ul>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            (function($){            
                $('ul.foo').click( function() {
                    $('li', this).css('background-color','red');
                });
            })(jQuery)
        </script>
    </body>
</html>
```

**예제 2.** jQuery( element )

```html
<html>
    <body>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            jQuery(document.body).css( "background-color", "black" );
        </script>
    </body>
</html>
```

-----------

## 선택자란?

jQuery wrapper에는 CSS 선택자가 위치할 수 있는데, 이를 통해서 제어하려는 엘리먼트를 빠르고 정확하게 지정할 수 있다.

## 선택자 탐색기

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            body{
                font-size:12px;
            }
            .selected,.selected_parent {
                background-color: red !important;
                color:white;
                border:2px solid red !important;
            }
            input.btn {
                width:130px;
            }
            ul, .on{
                float:left;
                width:150px;
                padding-left:20px;
                margin:0;
            }
            textarea{
                float:left;
                width: 400px;
                height:150px;
                font-size:11px;
                margin-left:20px;
            }
            .clear{
                clear: both;
            }
            .sample{
                margin-bottom: 20px;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <fieldset>
            <legend> 기본 </legend>
            <div class="sample">
                <ul id="tutorials">
                    <li class="tutorial" id="HTML"> HTML </li>
                    <li class="tutorial" id="CSS"> CSS </li>
                    <li class="tutorial" id="javascript"> javascript </li>
                    <li class="tutorial" id="jquery"> jQuery </li>
                    <li class="tutorial" id="PHP"> PHP </li>
                    <li class="tutorial" id="MYSQL"> MYSQL </li>
                </ul>
<textarea>
<ul id="tutorials">
    <li class="tutorial" id="HTML"> HTML </li>
    <li class="tutorial" id="CSS"> CSS </li>
    <li class="tutorial" id="javascript"> javascript </li>
    <li class="tutorial" id="jquery"> jQuery </li>
    <li jclass="tutorial" id="PHP"> PHP </li>
    <li class="tutorial" id="MYSQL"> MYSQL </li>
</ul>
</textarea>
            <div class="clear"></div>
                </div>
            <input class="btn" type="button" id="#jquerybtn" value="#jquery" /> - id 선택자 <br />
            <input class="btn" type="button" id=".tutorial" value=".tutorial" /> - class 선택자 <br />
            <input class="btn" type="button" value="li" /> - 엘리먼트 선택자 <br />
            <input class="btn" type="button" value="#jquery, #MYSQL" /> - 다중 선택자 <br />
        </fieldset>
        
        
        <fieldset>
            <legend> filter </legend>
            <div class="sample">
                <ul id="list">
                    <li> HTML </li>
                    <li> CSS </li>
                    <li> javascript </li>
                    <li> PHP </li>
                    <li> MYSQL </li>
                </ul>
<textarea>
<ul id="list">
    <li> HTML </li>
    <li> CSS </li>
    <li> javascript </li>
    <li> PHP </li>
    <li> MYSQL </li>
</ul>    
</textarea>
                <div class="clear"></div>
            </div>
            <input class="btn" type="button" value="#list li:eq(2)" /> - 인자와 인덱스가 동일한 엘리먼트를 찾아내는 선택자 <br />
            <input class="btn" type="button" value="#list li:gt(1)" /> - 인자 보다 인덱스가 큰 엘리먼트를 찾아내는 선택자 <br />
            <input class="btn" type="button" value="#list li:lt(2)" /> - 인자 보다 인덱스가 작은 엘리먼트를 찾아내는 선택자 <br />
            <input class="btn" type="button" value="#list li:even" /> - 첫번째, 세번째... 홀 수의 인덱스 값을 가진 엘리먼트에 대한 선택자 <br />
            <input class="btn" type="button" value="#list li:odd" /> - 두번째, 네번째.... 짝 수의 인덱스 값을 가진 엘리먼트에 대한 선택자 <br />
            <input class="btn" type="button" value="#list li:first" /> - 첫번재 인덱스 엘리먼트에 대한 선택자 <br />
            <input class="btn" type="button" value="#list li:last" /> - 마지막 인덱스 엘리먼트에 대한 선택자 <br />
        </fieldset>
        
        
        <fieldset>
            <legend> 속성 </legend>
            <div class="sample">
                <ul id="attribute">
                    <li target="ABCD">ABCD</li>
                    <li target="BCDE">BCDE</li>
                    <li target="CDEF">CDEF</li>
                    <li target="DEFG">DEFG</li>
                    <li target="EFGH">EFGH</li>
                    <li id="FGHI" target="FGHI">FGHI</li>
                </ul>
<textarea>
<ul id="attribute">
    <li target="ABCD">ABCD</li>
    <li target="BCDE">BCDE</li>
    <li target="CDEF">CDEF</li>
    <li target="DEFG">DEFG</li>
    <li target="EFGH">EFGH</li>
    <li id="FGHI" target="FGHI">FGHI</li>
</ul>    
</textarea>
                <div class="clear"></div>
            </div>
            <input class="btn" type="button" value="[target*=&quot;BC&quot;]" /> - 속성의 값에 주어진 문자열이 포함되는 엘리먼트를 찾아내는 선택자 <br />
            <input class="btn" type="button" value="[target=&quot;DEFG&quot;]" /> - 속성의 값과 주어진 문자열이 일치하는 엘리먼트를 찾아내는 선택자 <br />
            <input class="btn" type="button" value="[target!=&quot;DEFG&quot;]" /> - 속성의 값과 주어진 문자열이 일치하지 않는 엘리먼트를 찾아내는 선택자 <br />
<input class="btn" type="button" value="[target^=&quot;B&quot;]" /> - 속성의 값으로 주어진 문자열이 처음 등장하는 엘리먼트를 찾아내는 선택자 <br />
<input class="btn" type="button" value="[target$=&quot;H&quot;]" /> - 속성의 값으로 주어진 문자열이 마지막으로 등장하는 엘리먼트를 찾아내는 선택자 <br />
<input class="btn" type="button" value="[target]" /> - 속성이 존재하는 엘리먼트를 찾아내는 선택자 <br />
<input class="btn" type="button" value="[target][id]" /> - 속성들이 존재하는 엘리먼트를 찾아내는 선택자
        </fieldset>
        <fieldset>
            <legend>Form</legend>
                <div class="on">
                    <div>
                        <input type="text" disabled="disabled" value="disabled" />
                        <input type="text" value="enabled"/>
                    </div>
                    <div><input type="checkbox" checked="checked" /></div>
                    <div><input type="checkbox" /></div>
                </div>
<textarea class="sample">
<div>
    <input type="text" disabled="disabled" value="disabled" />
    <input type="text" value="enabled"/>
</div>
<div><input type="checkbox" checked="checked" /></div>
<div><input type="checkbox" /></div>
</textarea>
            <div class="clear"></div>
            <input class="btn" type="button" value="[type=&quot;text&quot;]" /> - 폼 엘리먼트를 선택할 때는 속성 셀렉터를 사용한다. <br />
            <input class="btn" type="button" value="[type=&quot;text&quot;]:disabled" /> - disabled 속성의 값이 disabled인 엘리먼트를 찾아내는 선택자<br />
            <input class="btn" type="button" value="[type=&quot;text&quot;]:enabled" /> - disabled 속성의 값이 enabled인 엘리먼트를 찾아내는 선택자<br />
            <input class="btn" type="button" value="input:checked" /> - 체크박스 중 체크가 된 엘리먼트를 찾아내는 선택자 <br />
        </fieldset>
        <script>
            $('input').on('click', function() {
                $this = $(this);
                $('*').removeClass('selected');
                switch($this.attr('value')) {
                    case '#jquery':
                        $('#jquery').addClass('selected');
                        break;
                    case '.tutorial':
                        $('.tutorial').addClass('selected');
                        break;
                    case 'li':
                        $('li').addClass('selected');
                        break;
                    case '#jquery, #MYSQL':
                        $('#jquery, #MYSQL').addClass('selected');    
                        break;
                    case '#list li:eq(2)':
                        $('#list li:eq(2)').addClass('selected');
                        break;
                    case '#list li:gt(1)':
                        $('#list li:gt(1)').addClass('selected');
                        break;
                    case '#list li:lt(2)':
                        $('#list li:lt(2)').addClass('selected');
                        break;
                    case '#list li:even':
                        $('#list li:even').addClass('selected');
                        break;
                    case '#list li:odd':
                        $('#list li:odd').addClass('selected');
                        break;
                    case '#list li:first':
                        $('#list li:first').addClass('selected');
                        break;
                    case '#list li:last':
                        $('#list li:last').addClass('selected');
                        break;
                    case '[target*="BC"]':
                        $('li[target*="BC"]').addClass('selected');
                        break;
                    case '[target="DEFG"]':
                        $('li[target="DEFG"]').addClass('selected');
                        break;
                    case '[target!="DEFG"]':
                        $('li[target!="DEFG"]').addClass('selected');
                        break;
                    case '[target^="B"]':
                        $('li[target^="B"]').addClass('selected');
                        break;
                    case '[target$="H"]':
                        $('li[target$="H"]').addClass('selected');
                        break;
                    case '[target]':
                        $('li[target]').addClass('selected');
                        break;
                    case '[target][id]':
                        $('li[target][id]').addClass('selected');
                        break;
                    case '[type="text"]':
                        $('[type="text"]').addClass('selected');                    
                        break;
                    case '[type="text"]:disabled':
                        $('[type="text"]:disabled').addClass('selected');
                        break;
                    case '[type="text"]:enabled':
                        $('[type="text"]:enabled').addClass('selected');
                        break;
                    case 'input:checked':
                        $('input:checked').parent().addClass('selected');;
                        break;
                    
                }
            })
        </script>
    </body>
</html> 
```

html 소스를 실행해 각각의 것들을 확인할 수 있다.

각각의 API는 https://api.jquery.com/ 이 사이트 안에 설명되어있다.

-------

## Chain이란?

jQuery의 메소드들은 반환값으로 자기 자신을 반환해야 한다는 규칙을 가지고 있다.
이를 이용하면 한번 선택한 대상에 대해서 연속적인 제어를 할 수 있다.

**예제1.** jQuery를 이용해서 코딩하는 경우

```html
<html>
    <body>
        <a id="tutorial" href="http://jquery.com" target="_self">jQuery</a>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            jQuery('#tutorial').attr('href', 'http://jquery.org').attr('target', '_blank').css('color', 'red');
        </script>
    </body>
</html>
```

**예제2.** javascript의 DOM을 이용해서 코딩하는 경우

```html
<html>
     <body>
         <a id="tutorial" href="http://jquery.com" target="_self">jQuery</a>
         <script type="text/javascript">
             var tutorial = document.getElementById('tutorial');
             tutorial.setAttribute('href', 'http://jquery.org');
             tutorial.setAttribute('target', '_blank');
             tutorial.style.color = 'red';
         </script>
     </body>
 </html>
```

## chain의 장점

- 코드가 간결해진다.
- 인간의 언어와 유사해서 사고의 자연스러운 과정과 일치함.

## 탐색(traversing)

- chain의 대상을 바꿔서 체인을 계속 연장시킬 수 있는 방법
- http://api.jquery.com/category/traversing/
- [taeyo.net jQuery traverse 강좌](http://www.taeyo.pe.kr/Columns/View.aspx?SEQ=375&PSEQ=29)
- 너무 복잡한 chain은 코드의 가독성을 떨어 뜨릴 수 있다.

**예제3.** traversing을 이용해서 chain안에서 대상을 움직일 수 있다.

```html
<html>
    <body>
        <ul class="first">
            <li class="foo"> list item 1 </li>
            <li> list item 2 </li>
            <li class="bar"> list item 3 </li>
        </ul>
        <ul class="second">
            <li class="foo"> list item 1 </li>
            <li> list item 2 </li>
            <li class="bar"> list item 3 </li>
        </ul>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">$('ul.first').find('.foo').css('background-color', 'red').end().find('.bar').css('background-color', 'green');</script>
    </body>
</html>
```

-------

## 이벤트란?

- 시스템에서 일어나는 사건을 의미
- javascript나 jQuery에게 이벤트란 브라우져에서 일어나는 사건을 의미한다. (클릭, 마우스 이동, 타이핑, 페이지 로딩등)
- 이벤트가 발생했을 때 작동할 로직을 시스템에게 알려두면 이벤트가 발생했을 때 시스템이 그 로직을 호출한다.
- 이벤트에 대한 기본적인 내용은 자바스크립트 이벤트 편 참고[ ](http://http//opentutorials.org/course/49)[http://opentutorials.org/course/49](http://http//opentutorials.org/course/49)

## jQuery의 이벤트

- 크로스브라우징의 문제를 해결해줌
- bind로 이벤트 핸들러를 설치하고, unbind로 제거 (예제1)
- trigger로 이벤트 핸들러를 강제로 실행 (예제2)
- click, ready와 같이 다양한 이벤트 헬퍼(helper)를 제공함 (직관적으로)
- on를 이용하면 현재 존재 하지 않는 엘리먼트에 이벤트 핸들러를 설치할 수 있음

찾아보니 3.xx부터는 bind() 기능을 제공하지 않는다고 함.
(1.0 ~ 1.7 이하 버전 : bind() /1.7 ~ 3.0 미만 버전 : bind(), on() 모두 사용 가능
이상 최신 버전 : on() )

**예제1.** bind, unbind, trigger를 이용한 이벤트의 설치, 제거, 호출

```html
<html>
    <head>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            function clickHandler(e){
                alert('thank you');
            }
            $(document).bind('ready', function(){
                 $('#click_me').on('click', clickHandler);
                 $('#remove_event').on('click', function(e){
                     $('#click_me').off('click', clickHandler);
                 });
                 $('#trigger_event').bind('click', function(e){
                     $('#click_me').trigger('click');
                 });
             })
        </script>
    </head>
    <body>
        <input id="click_me" type="button" value="click me" />
        <input id="remove_event" type="button" value="unbind" />
        <input id="trigger_event" type="button" value="trigger" />
    </body>
</html>
```

**예제2**. 이벤트 헬퍼 -> 더 많이 사용하는 방법이다.

```html
<html>
    <head>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            function clickHandler(e){
                alert('thank you');
            }
            $(document).ready(function(){
                 $('#click_me').click(clickHandler);
                 $('#remove_event').click(function(e){
                     $('#click_me').unbind('click', clickHandler);
                 });
                 $('#trigger_event').click(function(e){
                     $('#click_me').trigger('click');
                 });
             })
        </script>
    </head>
    <body>
        <input id="click_me" type="button" value="click me" />
        <input id="remove_event" type="button" value="unbind" />
        <input id="trigger_event" type="button" value="trigger" />
    </body>
</html>
```

**예제3**. on을 이용하면 존재하지 않는 엘리먼트에 대해서 이벤트를 설치할 수 있다. die는 off와 같은 메서드 기능을 가지고 있다.

```html
<html>
    <head>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            function clickHandler(e) {
                alert('thank you');
            }
            $('#click_me').live('click', clickHandler);
            $('#remove_event').live('click', function(e) {
                $('#click_me').die('click', clickHandler);
            });
            $('#trigger_event').live('click', function(e) {
                $('#click_me').trigger('click');
            });
        </script>
    </head>
    <body>
        <input id="click_me" type="button" value="click me" />
    <input id="remove_event" type="button" value="unbind" />
    <input id="trigger_event" type="button" value="trigger" />
    </body>
</html>
```

----------

## 엘리먼트 제어

- jQuery는 엘리먼트를 제어하는 일관되고 풍부한 기능들을 제공한다.
- http://api.jquery.com/category/manipulation/

### 자식으로 삽입 (.append(), .appendTo(), .html(), .prepend(), .prependTo(), .text())

```html
<!-- http://api.jquery.com/append/ -->
<!DOCTYPE html>
<html>
    <head>
        <style>
            p {
                background:yellow;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p>
            I would like to say:
        </p>
        <script>$("p").append("<strong>Hello</strong>");</script>
    </body>
</html>
```

### 형제로 삽입 (.after(), .before(), .insertAfter(), .insertBefore())

```html
<!-- http://api.jquery.com/after/ -->
<!DOCTYPE html>
<html>
    <head>
        <style>
            p {
                background:yellow;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p>
            I would like to say:
        </p>
        <script>$("p").after("<b>Hello</b>");</script>
    </body>
</html>
```

### 부모로 감싸기 (.unwrap(), .wrap(), .wrapAll(), .wrapInner())

```html
<!-- http://api.jquery.com/wrap/ -->
<!DOCTYPE html>
<html>
    <head>
        <style>
            div {
                border:2px blue solid;
                margin:2px;
                padding:2px;
            }
            p {
                background:yellow;
                margin:2px;
                padding:2px;
            }
            strong {
                color:red;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <span>Span Text</span>
        <strong>What about me?</strong>
        <span>Another One</span>
        <script>$("span").wrap("<div><div><p><em><b></b></em></p></div></div>");</script>
    </body>
</html>
```

### 삭제 (.detach(), .empty(), .remove(), .unwrap())

```html
<!-- http://api.jquery.com/remove/ -->
<!DOCTYPE html>
<html>
    <head>
        <style>
            p {
                background:yellow;
                margin:6px 0;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p>
            Hello
        </p>
        how are
        <p>
            you?
        </p>
        <button>
            Call remove() on paragraphs
        </button>
        <script>
            $("button").click( function () {
                $("p").remove();
            });
        </script>
    </body>
</html>
```

### 치환 (.replaceAll(), .replaceWith())

```html
<!-- http://api.jquery.com/replaceAll/ -->
<!DOCTYPE html>
<html>
    <head>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p> Hello </p>
        <p> cruel </p>
        <p> World </p>
        <script>$("<b>Paragraph. </b>").replaceAll("p"); // check replaceWith() examples        </script>
    </body>
</html>
```

### 클래스 (.addClass(), .hasClass(), .removeClass(), .toggleClass())

addClass() : Class를 추가.

hasClass() : 어떤 엘리먼트의 클래스를 가지고 있는지 없는지 확인.

remveClass() : 클래스를 삭제.

toggleClass() : 클래스가 엔리먼트를 가지고 있으면 삭제하고 가지고 있지 않다면 추가 해줌.

```html
<!-- http://api.jquery.com/toggleClass/ -->
<!DOCTYPE html>
<html>
    <head>
        <style>p {
                margin: 4px;
                font-size:16px;
                font-weight:bolder;
                cursor:pointer;
            }
            .blue {
                color:blue;
            }
            .highlight {
                background:yellow;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p class="blue"> Click to toggle </p>
        <p class="blue highlight"> highlight </p>
        <p class="blue"> on these </p>
        <p class="blue"> paragraphs </p>
        <script>
             $("p").click( function () {
                 $(this).toggleClass("highlight");
             });
         </script>
    </body>
</html>
```

### 속성제어 (.attr(), .prop(), .removeAttr(), .removeProp(), .val())

val() : 

```html
<!DOCTYPE html>
<html>
    <head>
        <style>p {
                color:blue;
                margin:8px;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <input type="text" value="some text"/>
        <p>
        </p>
        <script>$("input").keyup( function () { //사용자가 키보드를 누르고 땠을 때 발생하는 이벤트
                var value = $(this).val();//그 엘리먼트가 가지고 있는 value값을 알아냄.
                $("p").text(value); 
            }).keyup();</script> <!-- trigger와 같다. 초기같을 셋팅 할 때 주로 trigger를 사용한다.  p태그 안에 초기화 시켜 주기 위한 트리거 -->
    </body>
</html>
```

---------

## 폼

- 서버로 데이터를 전송하기 위한 수단
- [생활코딩 HTML 튜토리얼 폼 편 참고](http://opentutorials.org/course/11/14)
- Query는 폼을 제어하는데 필요한 이벤트와 메소드를 제공한다.
- jQuery 폼 API 문서 : http://api.jquery.com/category/forms/
-  

**예제1**. (.focus(), .blur(), .change(), .select())

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            span {
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p>
            <input type="text" />
            <span></span>
        </p>
        <script>
            $("input").focus( function () {
                $(this).next("span").html('focus');
            }).blur( function() {
                $(this).next("span").html('blur');
            }).change(function(e){
                alert('change!! '+$(e.target).val());
            }).select(function(){
                $(this).next('span').html('select');
            });
        </script>
    </body>
</html>
```

**예제2**. (.submit(), .val())

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            p {
                margin:0;
                color:blue;
            }
            div, p {
                margin-left:10px;
            }
            span {
                color:red;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <p>
            Type 'correct' to validate.
        </p>
        <form action="javascript:alert('success!');">
            <div>
                <input type="text" />
 
                <input type="submit" />
            </div>
        </form>
        <span></span>
        <script>
            $("form").submit( function() {
                if ($("input:first").val() == "correct") {
                    $("span").text("Validated...").show();
                    return true;
                }
                $("span").text("Not valid!").show().fadeOut(1000);
                return false;
            });
        </script>
    </body>
</html>
```

-------------

# 탐색

- 체인 컨텍스트를 유지하면서 제어의 대상이 되는 엘리먼트를 변경하는 기법
- [chain 챕터참고 ](http://opentutorials.org/jquery_tutorial/?id=77)
- http://api.jquery.com/category/traversing/

**예제**

```html
<!-- http://opentutorials.org/example/jquery/example.traversing.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style>
            body{
                font-size:11px;
                width:1000px;
            }
            #panel div,#panel li,#panel ul{
                border:2px solid black;
                margin:10px;
                padding:10px;
            }
            #panel ul{
                list-style: none;
            }
            #panel .s{
                border:2px solid red;
                background-color: #808080;
            }
            #panel #root{
                margin-top:0;
            }
            textarea{
                width:982px;
                height:100px;
                font-size:11px;
                overflow: visible;
            }        
            #help{
                float:left;
                width:500px;
                height:450px;
                overflow-y: scroll;
                overflow-x: hidden
            }
            #panel{
                float:left;
                width:500px;
            }
            #help table{
                border:1px solid gray;
                border-collapse: collapse;
                width:100%;
            }
            #help table td{
                border:1px solid gray;
                padding:5px;
            }
            #help .title{
                color:white;
                background-color:#555;
                padding:3px;
            }
            #help .title.checked{
                background-color:red;
            }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <div id="wrapper">
            <p>
                javascript을 입력 한 후에 엔터를 눌러주세요.
                <textarea id="code"></textarea></p>
            <div id="help">
                <table>
                    <tr id="add"><td><div class="title">.add(selector)</div>엘리먼트를 추가한다</td></tr>
                    <tr id="andSelf"><td><div class="title">.andSelf()</div>현재 엘리먼트 셋에 이전 엘리먼트 셋을 더 한다</td></tr>
                    <tr id="children"><td><div class="title">.children([selector])</div>자식 엘리먼트를 선택한다</td></tr>
                    <tr id="closet"><td><div class="title">.closest(selector)</div>가장 가까운 selector 조상 엘리먼트를 탐색한다</td></tr>
                    <tr id="each"><td><div class="title">.each(function(index,Element))</div>현재 엘리먼트 셋에 반복 작업을 실행한다</td></tr>
                    <tr id="end"><td><div class="title">.end()</div>이전 체인 컨텍스트로 돌아간다.</td></tr>
                    <tr id="eq"><td><div class="title">.eq(index)</div>현재 엘리먼트 셋에서 index에 해당하는 엘리먼트를 선택한다</td></tr>
                    <tr id="filter"><td><div class="title">.filter(selector)</div>현재 엘리먼트 셋에서 selector에 해당하는 엘리먼트를 선택한다</td></tr>
                    <tr id="find"><td><div class="title">.find(selector)</div>현재 엘리먼트 셋에서 selector에 해당하는 자손 엘리먼트를 선택한다</td></tr>
                    <tr id="first"><td><div class="title">.first()</div>현재 엘리먼트 셋 중 첫번째 엘리먼트를 선택한다</td></tr>
                    <tr id="last"><td><div class="title">.last()</div>현재 엘리먼트 셋 중 마지막 엘리먼트를 선택한다</td></tr>
                    <tr id="next"><td><div class="title">.next()</div>각각의 엘리먼트에 대한 다음 형재 엘리먼트를 선택한다</td></tr>
                    <tr id="nextAll"><td><div class="title">.nextAll()</div>각각의 엘리먼트에 대한 다음 형재 엘리먼트 전부를 선택한다</td></tr>
                    <tr id="prev"><td><div class="title">.prev()</div>각각의 엘리먼트에 대한 이전 형재 엘리먼트를 선택한다</td></tr>
                    <tr id="prevAll"><td><div class="title">.prevAll()</div>각각의 엘리먼트에 대한 이전 형재 엘리먼트 전부를 선택한다</td></tr>
                    <tr id="siblings"><td><div class="title">.siblings()</div>각각의 엘리먼트에 대한 형재 엘리먼트 전부를 선택한다</td></tr>
                    <tr id="slice"><td><div class="title">.slice(start, [end])</div>현제의 엘리먼트 셋 중 start에서 end까지의 엘리먼트를 선택한다</td></tr>
                </table>
            </div>
            <div id="panel">
                <div id="root">
                    div#root
                    <div>
                        div
                    </div>
                    <div>
                        div
                        <ul>
                            ul
                            <li>li</li>
                            <li>li</li>
                            <li>li</li>
                            <li>li</li>
                        </ul>
                    </div>
                    <div>
                        div
                    </div>
                </div>    
            </div>
        </div>
        <script>
            var $wrapper = $('#root').addClass('selected');
            $('#code').keydown(function(e){
                if(e.keyCode == 13){
                    eval($(this).val());
                    return false;
                }
            }).change(function(){
                    eval($(this).val());
            });
            $('tr').click(function(){
                $(this).find('.title').toggleClass('checked');
            })
        </script>
    </body>
</html>
```

```javascript

$('#root').addClass('s').removeClass('s') // id 값이 root인 태그에서 class명으로 s가 추가 된다. 확인후에는 반드시 removeClass를 해서 's' class명을 삭제해줘야한다. ~~~~ 다음은 
$('#root').addClass('s').removeClass('s').children().addClass('s').removeClass('s') // 현 재 elelment의 자식 element만 선택된다.
$('#root').addClass('s').removeClass('s').children().addClass('s').removeClass('s').first().addClass('s')  // 자식 element중에 첫번째 element만 선택된다.
$('#root').addClass('s').removeClass('s').children().addClass('s').removeClass('s').first().addClass('s').removeClass('s').next().addClass('s') // 현재 선택된 다음 element로 이동한다.
$('#root').addClass('s').removeClass('s').children().addClass('s').removeClass('s').first().addClass('s').removeClass('s').next().addClass('s').removeClass('s').next().addClass('s') // 다음 element로 이동
$('#root').addClass('s').removeClass('s').children().addClass('s').removeClass('s').first().addClass('s').removeClass('s').next().addClass('s').removeClass('s').next().addClass('s').prev().addClass('s').removeClass('s').parent().addClass('s') // 현재 상태에서 이전으로 간다.
~~~~~find('li').first().end().addClass('s') 첫번째 엘리먼트, 였지만 end()를 하게 되면 이전 상태로 되돌아간다.
~~~filter(':first').addClass('s') // 필터는 현재 엘리먼트 중에서 인자로 선택된 것 중에서 가져온다. find는 현재 선택된 엘리먼트 set들의 자식 엘리먼트 중에서 가져와서 더 범주가 크다.
~~~~~.siblings().addClass('s') 현재 선택된 엘리먼트의 형제 엘리먼트들을 리턴한다.
~~~~.nextAll() 형제 엘리먼트중에 다음에 있는 것들 중에 나머지 모두를 리턴한다.
~~~~.
~~~~~~~~~~~~~~ 생략
```

--------

## 에니메이션

## 효과란?

- 자바스크립트와 CSS를 이용해서 HTML엘리먼트에 동적인 효과를 줄 수 있다.
- jQuery의 효과 메소드를 호출하는 것만으로 간단히 효과를 줄 수 있다.

**예제1**.

```html
<!DOCTYPE html>
<html>
    <head>
        <style>        span {
                color:red;
                cursor:pointer;
            }
            div {
                margin:3px;
                width:80px;
                height:80px;
            }
            div {
                background:#f00;
            }
</style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <input type="button" id="fadeout" value="fade out" />
        <input type="button" id="fadein" value="fade in" />
        <input type="button" id="hide" value="hide" />
        <input type="button" id="show" value="show" />
        <input type="button" id="slidedown" value="slide down" />
        <input type="button" id="slideup" value="slide up" />
        <input type="button" id="mix" value="mix" />
        <div id="target">
            target
        </div>
        <script>$('input[type="button"]').click( function(e) {
                var $this = $(e.target);
                switch($this.attr('id')) {
                    case 'fadeout':
                        $('#target').fadeOut('slow');
                        break;
                    case 'fadein':
                        $('#target').fadeIn('slow');
                        break;
                    case 'hide':
                        $('#target').hide();
                        break;
                    case 'show':
                        $('#target').show();
                        break;
                    case 'slidedown':
                        $('#target').hide().slideDown('slow');
                        break;
                    case 'slideup':
                        $('#target').slideUp('slow');
                        break;
                    case 'mix':
                        $('#target').fadeOut('slow').fadeIn('slow').delay(1000).slideUp().slideDown('slow', function(){alert('end')});
                        break;
                }
            }) 
        </script>
    </body>
</html>
```

**예제2**.

```html
 <!DOCTYPE html>
<html>
    <head>
        <style>        
            div {
                background-color:#bca;
                width:100px;
                border:1px solid green;
            }
</style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <button id="go">
            &raquo; Run
        </button>
 
        <div id="block">
            Hello!
        </div>
        <script>/* Using multiple unit types within one animation. */
 
            $("#go").click( function() {
                $("#block").animate({
                    width: "300px",
                    opacity: 0.4,
                    marginLeft: "50px",
                    fontSize: "30px",
                    borderWidth: "10px"
                }, 3000);
            });</script>
    </body>
</html>
```

--------

## ajax란?

- **A**synchronous **J**avaScript **a**nd **X**ML 의 약자
- 자바스크립트를 이용해서 비동기식으로 서버와 통신하는 방식. 이 때 XML을 이용한다.
- 꼭 XML을 이용할 필요는 없고, 최근에는 json을 더 많이 이용한다.
- 비동기식이란 여러가지 일이 동시적으로 발생한다는 뜻으로, 서버와 통신하는 동안 다른 작업을 할 수 있다는 의미.

## 선행지식

- [폼](http://opentutorials.org/course/11/14)

## **$.ajax(settings)**

// settings : 객체

- jQuery를 이용한 ajax통신의 가장 기본적인 API
- 주요속성
  - data : 서버에 전송할 데이터, key/value 형식의 객체
  - dataType : 서버가 리턴하는 데이터 타입 (xml, json, script, html)
  - type : 서버로 전송하는 데이터의 타입 (POST, GET)
  - url : 데이터를 전송할 URL
  - success : ajax통신에 성공했을 때 호출될 이벤트 핸들러

**예제1-1.** 웹페이지

```html
<!DOCTYPE html>
<html>
    <head>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
    </head>
    <body>
        <div id="result"></div>
        <input type="text" id="msg" />
        <input type="button" value="get result" id="getResult" />
        <script>
            $('#getResult').click( function() {
                $('#result').html('');
                $.ajax({
                    url:'http://opentutorials.org/example/jquery/example.jquery.ajax.php',
                    dataType:'json',
                    type:'POST',
                    data:{'msg':$('#msg').val()}, // msg에 ''있어도 되고 없어도된다.
                    success:function(result){
                        if(result['result']==true){
                          $('#result').html(result['msg']);
                        }
                    }
                });
            })
        </script>
    </body>
</html>
```

**예제 1-2**. 서버 쪽 로직

```html
<?
echo json_encode(array('result'=>true, 'msg'=>$_REQUEST['msg']));
?>
```

