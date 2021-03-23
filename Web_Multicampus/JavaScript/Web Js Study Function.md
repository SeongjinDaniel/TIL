# 함수

## 값으로서의 함수

```javascript
function a(){}
```

위의 예제에서 함수 a는 변수 a에 담겨진 값이다. 또한 함수는 객체의 값으로 포함될 수 있다. 이렇게 객체의 속성 값으로 담겨진 함수를 메소드(method)라고 부른다.

```javascript
a = {
    b:function(){
    }
};
```

함수는 값이기 때문에 다른 함수의 인자로 전달 될수도 있다. 아래 예제를 보자.

```javascript
function cal(func, num){
    return func(num)
}
function increase(num){
    return num+1
}
function decrease(num){
    return num-1
}
alert(cal(increase, 1));
alert(cal(decrease, 1));
```

10행을 실행하면 함수 increase와 값 1이 함수 cal의 인자로 전달된다. 함수 cal은 첫번째 인자로 전달된 increase를 실행하는데 이 때 두번째 인자의 값이 1을 인자로 전달한다. 함수 increase은 계산된 결과를 리턴하고 cal은 다시 그 값을 리턴한다.



-------



함수는 함수의 리턴 값으로도 사용할 수 있다.

```javascript
function cal(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}
alert(cal('plus')(2,1));
alert(cal('minus')(2,1));   
```

당연히 배열의 값으로도 사용할 수 있다.

```javascript
var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];
var input = 1;
for(var i = 0; i < process.length; i++){
    input = process[i](input);
}
alert(input);
```



----

## 콜백

### 처리의 위임

값으로 사용될 수 있는 특성을 이용하면 함수의 인자로 함수로 전달할 수 있다. 값으로 전달된 함수는 호출될 수 있기 때문에 이를 이용하면 함수의 동작을 완전히 바꿀 수 있다. 인자로 전달된 함수 sortNumber의 구현에 따라서 sort의 동작방법이 완전히 바뀌게 된다.

```javascript 
function sortNumber(a,b){
    // 위의 예제와 비교해서 a와 b의 순서를 바꾸면 정렬순서가 반대가 된다.
    return b-a;
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]
```



---------------

## 클로저

클로저(closure)는 내부함수가 외부함수의 맥락(context)에 접근할 수 있는 것을 가르킨다. 클로저는 자바스크립트를 이용한 고난이도의 테크닉을 구사하는데 필수적인 개념으로 활용된다.  

## 내부함수

자바스크립트는 함수 안에서 또 다른 함수를 선언할 수 있다. 아래의 예제를 보자. 결과는 경고창에 coding everybody가 출력될 것이다.

```javascript
function outter(){
    function inner(){
        var title = 'coding everybody'; 
        alert(title);
    }
    inner();
}
outter();
```

위의 예제에서 함수 outter의 내부에는 함수 inner가 정의 되어 있다. 함수 inner를 내부 함수라고 한다.

내부함수는 외부함수의 지역변수에 접근할 수 있다. 아래의 예제를 보자. 결과는 coding everybody이다.

```javascript
function outter(){
    var title = 'coding everybody';  
    function inner(){        
        alert(title);
    }
    inner();
}
outter();
```

위의 예제는 내부함수 inner에서 title을 호출(4행)했을 때 외부함수인 outter의 지역변수에 접근할 수 있음을 보여준다.

---

클로저(closure)는 내부함수와 밀접한 관계를 가지고 있는 주제다. 내부함수는 외부함수의 지역변수에 접근 할 수 있는데 외부함수의 실행이 끝나서 외부함수가 소멸된 이후에도 내부함수가 외부함수의 변수에 접근 할 수 있다. 이러한 메커니즘을 클로저라고 한다. 아래 예제는 이전의 예제를 조금 변형한 것이다. 결과는 경고창으로 coding everybody를 출력할 것이다.

```javascript
function outter(){
    var title = 'coding everybody';  
    return function(){        
        alert(title);
    }
}
inner = outter();
inner();
```

예제의 실행순서를 주의깊게 살펴보자. 7행에서 함수 outter를 호출하고 있다. 그 결과가 변수 inner에 담긴다. 그 결과는 이름이 없는 함수다. 실행이 8행으로 넘어오면 outter 함수는 실행이 끝났기 때문에 이 함수의 지역변수는 소멸되는 것이 자연스럽다. 하지만 8행에서 함수 inner를 실행했을 때 coding everybody가 출력된 것은 외부함수의 지역변수 title이 소멸되지 않았다는 것을 의미한다. 클로저란 내부함수가 외부함수의 지역변수에 접근 할 수 있고, 외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않는 특성을 의미한다.

---

조금 더 복잡한 아래 예제를 살펴보자. 아래 예제는 클로저를 이용해서 영화의 제목을 저장하고 있는 객체를 정의하고 있다. 실행결과는 Ghost in the shell -> Matrix -> 공각기동대 -> Matrix 이다.

```javascript
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
alert(ghost.get_title());
alert(matrix.get_title());
 
ghost.set_title('공각기동대');
 
alert(ghost.get_title());
alert(matrix.get_title());
```

위의 예제를 통해서 알 수 있는 것들을 정리해보면 아래와 같다.

1. 클로저는 객체의 메소드에서도 사용할 수 있다. 위의 예제는 함수의 리턴값으로 객체를 반환하고 있다. 이 객체는 메소드 get_title과 set_title을 가지고 있다. 이 메소드들은 외부함수인 factory_movie의 인자값으로 전달된 지역변수 title을 사용하고 있다.

2. 동일한 외부함수 안에서 만들어진 내부함수나 메소드는 외부함수의 지역변수를 공유한다. 17행에서 실행된 set_title은 외부함수 factory_movie의 지역변수 title의 값을 '공각기동대'로 변경했다. 19행에서 ghost.get_title();의 값이 '공각기동대'인 것은 set_title와 get_title 함수가 title의 값을 공유하고 있다는 의미다.

3. 그런데 똑같은 외부함수 factory_movie를 공유하고 있는 ghost와 matrix의 get_title의 결과는 서로 각각 다르다. 그것은 외부함수가 실행될 때마다 새로운 지역변수를 포함하는 클로저가 생성되기 때문에 ghost와 matrix는 서로 완전히 독립된 객체가 된다.

4. factory_movie의 지역변수 title은 2행에서 정의된 객체의 메소드에서만 접근 할 수 있는 값이다. 이 말은 title의 값을 읽고 수정 할 수 있는 것은 factory_movie 메소드를 통해서 만들어진 객체 뿐이라는 의미다. JavaScript는 기본적으로 Private한 속성을 지원하지 않는데, 클로저의 이러한 특성을 이용해서 Private한 속성을 사용할 수 있게된다.

참고 Private 속성은 객체의 외부에서는 접근 할 수 없는 외부에 감춰진 속성이나 메소드를 의미한다. 이를 통해서 객체의 내부에서만 사용해야 하는 값이 노출됨으로서 생길 수 있는 오류를 줄일 수 있다. 자바와 같은 언어에서는 이러한 특성을 언어 문법 차원에서 지원하고 있다.

아래의 예제는 클로저와 관련해서 자주 언급되는 예제다. 



-------

```javascript
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(){
        return i;
    }
}
for(var index in arr) {
    console.log(arr[index]());
}
```

함수가 함수 외부의 컨텍스트에 접근할 수 있을 것으로 기대하겠지만 위의 결과는 아래와 같다.

```javascript
5
5
5
5
5
```

위의 코드는 아래와 같이 변경해야 한다.

```javascript
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id) {
        return function(){
            return id;
        }
    }(i);
}
for(var index in arr) {
    console.log(arr[index]());
}
```

결과는 아래와 같다.

```javascript
0
1
2
3
4
```

- https://developer.mozilla.org/ko/docs/JavaScript/Guide/Closures
- http://ejohn.org/apps/learn/#48
- http://blog.javarouka.me/2012/01/javascripts-closure.html



----------

## arguments

함수에는 arguments라는 변수에 담긴 숨겨진 유사 배열이 있다. 이 배열에는 함수를 호출할 때 입력한 인자가 담겨있다. 아래 예제를 보자. 결과는 10이다.

```javascript
function sum(){
    var i, _sum = 0;    
    for(i = 0; i < arguments.length; i++){
        document.write(i+' : '+arguments[i]+'<br />');
        _sum += arguments[i];
    }   
    return _sum;
}
document.write('result : ' + sum(1,2,3,4));
```

함수 sum은 인자로 전달된 값을 모두 더해서 리턴하는 함수다. 그런데 1행처럼 함수 sum은 인자에 대한 정의하가 없다. 하지만 마지막 라인에서는 4개의 인자를 함수 sum으로 전달하고 있다. 함수의 정의부분에서 인자에 대한 구현이 없음에도 인자를 전달 할 수 있는 것은 왜 그럴까? 그것은 arguments라는 특수한 배열이 있기 때문이다.

arguments는 함수안에서 사용할 수 있도록 그 이름이나 특성이 약속되어 있는 일종의 배열이다. arguments[0]은 함수로 전달된 첫번째 인자를 알아낼 수 있다. 또 arguments.length를 이용해서 함수로 전달된 인자의 개수를 알아낼 수도 있다. 이러한 특성에 반복문을 결합하면 함수로 전달된 인자의 값을 순차적으로 가져올 수 있다. 그 값을 더해서 리턴하면 인자로 전달된 값에 대한 총합을 구하는 함수를 만들 수 있다.

arguments는 사실 배열은 아니다. 실제로는 arguments 객체의 인스턴스다.

----

매개변수와 관련된 두가지 수가 있다. 하나는 함수.length, 다른 하나는 arguments.length이다. arguments.length는 함수로 전달된 실제 인자의 수를 의미하고, 함수.length는 함수에 정의된 인자의 수를 의미한다. 아래의 코드를 보자.

```javascript
function zero(){
    console.log(
        'zero.length', zero.length,
        'arguments', arguments.length
    );
}
function one(arg1){
    console.log(
        'one.length', one.length,
        'arguments', arguments.length
    );
}
function two(arg1, arg2){
    console.log(
        'two.length', two.length,
        'arguments', arguments.length
    );
}
zero(); // zero.length 0 arguments 0 
one('val1', 'val2');  // one.length 1 arguments 2 
two('val1');  // two.length 2 arguments 1
```



----------

## 함수의 호출

함수에 대한 기본 수업에서 함수를 호출하는 방법을 알아봤다. 아래는 함수를 호출하는 가장 기본적인 방법이다.

```javascript
function func(){
}
func();
```

JavaScript는 함수를 호출하는 특별한 방법을 제공한다. 본 토픽의 시작에서 함수를 객체라고 했다. 위의 예제에서 함수 func는 Function이라는 객체의 인스턴스다. 따라서 func는 객체 Function이 가지고 있는 메소드들을 상속하고 있다. 지금 이야기하려는 메소드는 Function.apply과 Function.call이다. 이 메소드들을 이용해서 함수를 호출해보자. 결과는 3이다.

```javascript
function sum(arg1, arg2){
    return arg1+arg2;
}
alert(sum.apply(null, [1,2]))
```

함수 sum은 Function 객체의 인스턴스다. 그렇기 때문에 객체 Function 의 메소드 apply를 호출 할 수 있다. apply 메소드는 두개의 인자를 가질 수 있는데, 첫번째 인자는 함수(sum)가 실행될 맥락이다. 맥락의 의미는 다음 예제를 통해서 살펴보자. 두번째 인자는 배열인데, 이 배열의 담겨있는 원소가 함수(sum)의 인자로 순차적으로 대입된다. Function.call은 사용법이 거의 비슷하다 여기서는 언급하지 않는다.

좀 더 흥미로운 예제를 살펴보자. 결과는 6과 185이다.

```javascript
o1 = {val1:1, val2:2, val3:3}
o2 = {v1:10, v2:50, v3:100, v4:25}
function sum(){
    var _sum = 0;
    for(name in this){
        _sum += this[name];
    }
    return _sum;
}
alert(sum.apply(o1)) // 6
alert(sum.apply(o2)) // 185
```

예제가 복잡해보이지만 한나씩 분해해서 생각해보면 어렵지 않다.

우선 두개의 객체를 만들었다. o1는 3개의 속성을 가지고 있다. 각각의 이름은 val1, val2,val3이다. o2는 4개의 속성을 가지고 있고 o1과는 다른 속성 이름을 가지고 있고 속성의 수도 다르다.

그 다음엔 함수 sum을 만들었다. 이 함수는 객체의 속성을 열거할 때 사용하는 for in 문을 이용해서 객체 자신(this)의 값을 열거한 후에 각 속성의 값을 지역변수 _sum에 저장한 후에 이를 리턴하고 있다.

객체 Function의 메소드 apply의 첫번째 인자는 함수가 실행될 맥락이다. 이렇게 생각하자. sum.apply(o1)은 함수 sum을 객체 o1의 메소드로 만들고 sum을 호출한 후에 sum을 삭제한다. 아래와 비슷하다. (실행결과가 조금 다를 것이다. 그것은 함수 for in문으로 객체 o1의 값을 열거할 때 함수 sum도 포함되기 때문이다.)

```javascript
o1.sum = sum;
alert(o1.sum());
delete o1.sum();
```

