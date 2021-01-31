# SASS



CSS를 프로그래밍언어스럽게 작성가능한 일종의 Preprocessor

css에서 변수, 연산자, 함수, extend, import 이런걸 사용가능



브라우저는 SASS 문법 모르니까 SASS로 작성한 파일을 다시 CSS로 컴파일해야함 -> node-sass 설치하며 알아서 해줌



#### Install

```
yarn add node-sass
or
npm install node-sass
```



#### Detail.js

```react
import './Detail.scss'


```



#### Detail.scss

```scss
@import "./_Reset.scss";

$메인컬러: #ff0000;

.red {
  color: $메인컬러;
}

@mixin 함수() {
  background: #eeeeee;
  padding: 15px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
  margin: auto;
}

.my-alert {
  @include 함수();
}

.my-alert2 {
  @extend .my-alert;
  background: #ffe591;
}

// div.container h4 {
//   color: blue;
// }
// div.container p {
//   color: green;
// }

// nesting 문법
//div.container {
//   h4 {
//     color: blue;
//   }
//   p {
//     color: green;
//   }
// }
```

sass 문법을 작성하면 알아서 css로 변경해서 적용시켜준다.



#### _Reset.scss

```scss
// 모든 페이지에 적용하기 위해서
body {
  margin: 0;
}

div {
  box-sizing: border-box;
}

```

관습적으로 컴파일 하지 않고 쓸데없는 파일은 _(언더바)를 사용해서 작명한다.