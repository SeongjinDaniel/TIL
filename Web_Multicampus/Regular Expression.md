# 정규표현식(Regular expression)

```javascript
// 정규표현식 생성
// 정규 표현식 리터럴
var pattern = /a/; // /찾고자 하는것/ 
var patern = new RegExp('a'); // '찾고자하는것'

```

정규표현식을 컴파일해서 객체를 만들었다면 이제 문자열에서 원하는 문자를 찾아내야 한다. 

추출, tes, 치환 -> 정규표현식을 통해 하는 주요한 작업들

### 정규표현식 리터럴

```javascript
var pattern = /a/
```

### 정규표현식 객체 생성자

```javascript
var pattern = new RegExp('a';
```

두가지 모두 같은 결과를 만들지만 각자가 장단점이 있다. 

## 정규표현식 메소드 실행

### RegExp.exec()

```javascript
console.log(pattern.exec('abcdef'); // ["a"]
```

실행결과는 문자열 a를 값으로 하는 배열을 리턴한다.

```javascript
var pattern = /a./; // . 은 하나의 문자라는 뜻이다.
pattern.exec('abcde');
```

실행결과는 문자열 ab를 값으로 하는 배열을 리턴한다.

```javascript
console.log(pattern.exec('bcdefg')); // null
```

인자 'bcdef'에는 a가 없기 때문에 null을 리턴한다.

### RegExp.test()

test는 인자 안에 패턴에 해당되는 문자열이 있으면 true, 없으면 false를 리턴한다.

```javascript
console.log(pattern.test('abcdef')); // true 
cnosole.log(pattern.test('bcdefg'); // false
```

```
pattern.extec :  추출
pattern.test : 있는지 없는지 유무
```



-------------

## 문자열 메소드 실행

문자열 객체의 몇몇 메소드는 정규표현식을 사용할 수 있다. 

### String.match()

RegExp.exec()와 비슷하다.

```javascript
var pattern = /a/;
var str = 'abcdef';
str.match(pattern); // ["a"]
console.log('abcdef'.match(pattern)); // ["a"]
console.log('bcdefg'.match(pattern)); // null
```

### String.replace()

문자열에서 패턴을 검색해서 이를 변경한 후에 변경된 값을 리턴한다.

```javascript
console.log('abcdef'.replace(pattern, 'A'));  // Abcdef
```



---------

## 옵션

 정규표현식 패턴을 만들 때 옵션을 설정할 수 있다. 옵션에 따라서 검출되는 데이터가 달라진다.

### i

i를 붙이면 대소문자를 구분하지 않는다.

```javascript
var xi = /a/; 
console.log("Abcde".match(xi)); // null
var oi = /a/i; 
console.log("Abcde".match(oi)); // ["A"];
```

### g

g를 붙이면 검색된 모든 결과를 리턴한다.

```javascript
var xg = /a/;
console.log("abcdea".match(xg)); // ["a"]
var og = /a/g;
console.log("abcdea".match(og)); // ["a", "a"]
```



```javascript
var ig = /a/ig;
"AabcAa".match(ig); // ["A", "a", "A", "a"]
```



--------

### 캡처

괄호안의 패턴은 마치 변수처럼 재사용할 수 있다. 이 때 기호 $를 사용하는데 아래 코드는 coding과 everybody의 순서를 역전시킨다.

```javascript
var pattern = /(\w+)\s(\w+)/;
var str = "coding everybody";
var result = str.replace(pattern, "$2, $1");
console.log(result); // everybody, coding
```

\w : A~Z, a ~ z, 0 ~ 9

\+ : 하나 이상

\s : space 공백

(\w+)\s : A띄어쓰기 까지 가능

### 치환

아래 코드는 본문 중의 URL을 링크 html 태그로 교체한다. 

```javascript
var urlPattern = /\b(?:https?):\/\/[a-z0-9-+&@``#\/%?=~_|!:,.;]*/gim;
var content = '생활코딩 : http://opentutorials.org/course/1 입니다. 네이버 : http://naver.com 입니다. ';
var result = content.replace(urlPattern, function(url){    
    return'+url+'">'+url+'';
});
console.log(result);
```



by 생활코딩