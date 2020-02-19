# Leaflet SVG

[ SVG 학습시 ]

https://thenounproject.com/

폴더명 : svgexam

[베지에 곡선 및 svg 가이드]

https://a11y.gitbook.io/graphics-aria/

https://a11y.gitbook.io/graphics-aria/svg-graphics/svg-paths-shape

[ SVG 커브 학습 사이트 ]

https://a11y.gitbook.io/graphics-aria/svg-graphics/svg-paths-shape

[ SVG 튜토리얼 ]

https://developer.mozilla.org/ko/docs/Web/SVG/Tutorial

#### 실습 exam1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>SVG학습</title>
</head>
<body>
<h1>SVG파일도 이미지로 사용 가능</h1>
<hr>
<img src="../images/noun_Cactus_3122517.svg">
<img src="../images/noun_Cactus_3122517.png">
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
<h1>이미지로 만든 SVG 그래프</h1>
<hr>
<svg width="300px" height="200px" xmlns:xlink= "http://www.w3.org/1999/xlink">
  <image xlink:href="../images/duke.png" x="50" y="1" width="40" height="80" />
  <image xlink:href="../images/duke.png" x="70" y="1" width="40" height="80" />
  <image xlink:href="../images/duke.png" x="90" y="1" width="40" height="80" />
  <!-- html 표준태그가 아닌 태그는 warning이 난다. -->
</svg>
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
</head>
<body>
<h1>텍스트</h1>
<hr>
<svg width="300px" height="200px">
<text x="110" y="30">Simplest Text</text>
  <text x="110" y="70" stroke="black">Outlined/filled</text>
  <text x="110" y="110" stroke="black" stroke-width="0.5" fill="none">Outlined only</text>
</svg>
<hr>
<svg width="300px" height="210px">
  <text x="110" y="30" font-size="1.5em" stroke="red">stroke="red"</text>
  <text x="110" y="60" font-size="1.5em" stroke="orange">stroke="orange"</text>
  <text x="110" y="90" font-size="1.5em" stroke="yellow">stroke="yellow"</text>
  <text x="110" y="120" font-size="1.5em" stroke="green">stroke="green"</text>
  <text x="110" y="150" font-size="1.5em" stroke="blue">stroke="blue"</text>
  <text x="110" y="180" font-size="1.5em" stroke="darkblue">stroke="darkblue"</text>
  <text x="110" y="210" font-size="1.5em" stroke="violet">stroke="violet"</text>
</svg>
<hr>
<svg width="300px" height="210px">
  <text x="110" y="30" font-size="1.5em" fill="red">fill="red"</text>
  <text x="110" y="60" font-size="1.5em" fill="orange">fill="orange"</text>
  <text x="110" y="90" font-size="1.5em" fill="yellow">fill="yellow"</text>
  <text x="110" y="120" font-size="1.5em" fill="green">fill="green"</text>
  <text x="110" y="150" font-size="1.5em" fill="blue">fill="blue"</text>
  <text x="110" y="180" font-size="1.5em" fill="darkblue">fill="darkblue"</text>
  <text x="110" y="210" font-size="1.5em" fill="violet">fill="violet"</text>
</svg>
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
<h1>직선</h1>
<hr>
<svg width="300px" height="200px">
  <line x1="10" y1="30" x2="230" y2="110" stroke="green" stroke-width="5" />
</svg>
<svg width="300px" height="200px">
  <line x1="20" y1="180" x2="250" y2="10" stroke="red" stroke-width="1" />
</svg>
<svg width="300px" height="200px">
  <line x1="150" y1="20" x2="150" y2="180" stroke="blue" stroke-width="10" />
</svg>
<svg width="300px" height="200px">
  <line x1="20" y1="100" x2="280" y2="100" stroke="orange" stroke-width="2" />
</svg>
<hr>
<svg width="300px" height="200px">
  <line x1="40" y1="10" x2="10" y2="190" stroke="midnightblue" />
  <line x1="70" y1="10" x2="40" y2="190" stroke="midnightblue" stroke-width="0" />
  <line x1="100" y1="10" x2="70" y2="190" stroke="midnightblue" stroke-width="1" />
  <line x1="130" y1="10" x2="100" y2="190" stroke="midnightblue" stroke-width="2" />
  <line x1="160" y1="10" x2="130" y2="190" stroke="midnightblue" stroke-width="4" />
  <line x1="190" y1="10" x2="160" y2="190" stroke="midnightblue" stroke-width="6" />
  <line x1="220" y1="10" x2="190" y2="190" stroke="midnightblue" stroke-width="10" />
  <line x1="250" y1="10" x2="220" y2="190" stroke="midnightblue" stroke-width="12" />
  <line x1="280" y1="10" x2="250" y2="190" stroke="midnightblue" stroke-width="14" />
</svg>
<hr>
<svg width="300px" height="200px">
  <line x1="150" y1="0" x2="150" y2="200" stroke="red" stroke-width="10" />
  <line x1="20" y1="10" x2="280" y2="10" stroke="violet" stroke-width="10" stroke-opacity="0.0" />
  <line x1="20" y1="30" x2="280" y2="30" stroke="violet" stroke-width="10" stroke-opacity="0.1" />
  <line x1="20" y1="50" x2="280" y2="50" stroke="violet" stroke-width="10" stroke-opacity="0.2" />
  <line x1="20" y1="70" x2="280" y2="70" stroke="violet" stroke-width="10" stroke-opacity="0.3" />
  <line x1="20" y1="90" x2="280" y2="90" stroke="violet" stroke-width="10" stroke-opacity="0.5" />
  <line x1="20" y1="110" x2="280" y2="110" stroke="violet" stroke-width="10" stroke-opacity="0.6" />
  <line x1="20" y1="130" x2="280" y2="130" stroke="violet" stroke-width="10" stroke-opacity="0.7" />
  <line x1="20" y1="150" x2="280" y2="150" stroke="violet" stroke-width="10" stroke-opacity="0.8" />
  <line x1="20" y1="170" x2="280" y2="170" stroke="violet" stroke-width="10" stroke-opacity="0.9" />
  <line x1="20" y1="190" x2="280" y2="190" stroke="violet" stroke-width="10" stroke-opacity="1.0" />
</svg>
<hr>
<svg width="300px" height="200px">
  <line x1="20" y1="10" x2="280" y2="10" stroke="grey" stroke-width="2" stroke-dasharray="5, 5" /> <!-- stroke-dasharray = "그리고, 비우고 " -->
  <line x1="20" y1="30" x2="280" y2="30" stroke="grey" stroke-width="2" stroke-dasharray="5, 10" />
  <line x1="20" y1="50" x2="280" y2="50" stroke="grey" stroke-width="2" stroke-dasharray="10, 5" />
  <line x1="20" y1="70" x2="280" y2="70" stroke="grey" stroke-width="2" stroke-dasharray="5, 1" />
  <line x1="20" y1="90" x2="280" y2="90" stroke="grey" stroke-width="2" stroke-dasharray="1, 5" />
  <line x1="20" y1="110" x2="280" y2="110" stroke="grey" stroke-width="2" stroke-dasharray="0.9" />
  <line x1="20" y1="130" x2="280" y2="130" stroke="grey" stroke-width="2" stroke-dasharray="15, 10, 5" />
  <line x1="20" y1="150" x2="280" y2="150" stroke="grey" stroke-width="2" stroke-dasharray="15, 10, 5, 10" />
  <line x1="20" y1="170" x2="280" y2="170" stroke="grey" stroke-width="2" stroke-dasharray="15, 10, 5, 10, 15" />
  <line x1="20" y1="190" x2="280" y2="190" stroke="grey" stroke-width="2" stroke-dasharray="5, 5, 1, 5" />
</svg>
<hr>
<svg width="300px" height="200px">
  <line x1="20" y1="50" x2="280" y2="50" stroke="black" stroke-linecap="butt" stroke-width="20" />
  <line x1="20" y1="100" x2="280" y2="100" stroke="black" stroke-linecap="round" stroke-width="20" />
  <line x1="20" y1="150" x2="280" y2="150" stroke="black" stroke-linecap="square" stroke-width="20" />
</svg>
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
<h1>패스</h1>
<hr>
<svg width="300px" height="200px">
  <!-- single line: Move pen to (10, 10); Draw a line to (290, 190) -->
  <path d="M 10 10 L 290 190" stroke="black" fill="none" /> <!-- M은 옮겨 가는거고 L은 선을 그리면서 옮겨 간다 -->
</svg>
<hr>
<svg width="300px" height="200px">
  <!-- a angle: Move pen to (280,20); Draw a line to (10,190); Draw a line to (280,190) -->
  <path d="M 280,20 L 10,190 280,190" fill="none" stroke="brown" stroke-width="2" />
</svg>
<hr>
<svg width="300px" height="200px">
  <!-- a angle: Move pen to (280,20); Draw a line to (10,190); Draw a line to (280,190) -->
  <path d="M 280,20 L 10,190 280,190Z" fill="none" stroke="brown" stroke-width="2" /> <!-- 끝에다가 Z를 붙이면 시작위치로 간다. -->
</svg>
</body>
</html>
```

#### 실습 exam6

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG</title>
		<style>
			svg {
				width : 320px;
				height : 240px;
				border : 1px solid red;
			} 
		</style>
	</head>
	<body>
		<h1>SVG로 도형 그리기</h1>
		<svg>
			<rect x="10" y="20" width="180" height="160" stroke-width="4px"  stroke="black"  fill="orange"/>
			<circle cx="190" cy="140" r="80" opacity="0.75" fill="blue"/>
		</svg>
	</body>
</html>
```

#### 실습 exam7

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG</title>
		<style>
			svg {
				width : 320px;
				height : 240px;
				border : 1px solid red;
			}
			rect {
				stroke-width : 4px;
				stroke : black;
				fill : orange;
			}
			circle {
				opacity : 0.75;
				fill : blue;
			}
		</style>
	</head>
	<body>
		<h1>SVG로 도형 그리기</h1>
		<svg>
			<rect x="10" y="20" width="180" height="160" />
			<circle cx="190" cy="140" r="80" />
		</svg>
	</body>
</html>
```

#### 실습 exam8

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>가로형 막대그래프</title>
		<style>
			svg {
				border: 1px solid black;
			}
		</style>
		<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script> <!-- d3 라이브러리 -->
	</head>
	<body>
		<h1>프로그램으로 SVG 요소 생성</h1>
		<div id="graphArea"></div>
		<script>
		d3.select("#graphArea")		// svg 요소를 생성하는 div 요소를 지정
		.append("svg")					// svg 요소를 추가
		.attr("width", "320px")		// svg 요소의 가로 넓이를 설정
		.attr("height", "240px")	// svg요소 세로 높이를 설정
		// d3 chaining 방식을 사용하고 있다. 리턴 방식도 d3여서 d3끼리 호환이 잘되있다.
		</script>
	</body>
</html>
```

#### 실습 exam9

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>둥근 모서리 사각형</h1>
		<svg>
			<rect x="30" y="20" width="200" height="100" rx="20" ry="20" /> <!-- rx, ry 속성 적용 -->
		</svg>
	</body>
</html>
```

#### 실습 exam10

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>원</h1>
		<svg width="300" height="300" style="border:1px solid red">
			<circle cx="160" cy="120" r="100" />
		</svg>
	</body>
</html>
```

#### 실습 exam11

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>원</h1>
		<svg width="300" height="300">
			<circle cx="160" cy="120" r="100" fill="red" stroke="blue" stroke-width="8"/>
		</svg>
	</body>
</html>
```

#### 실습 exam12

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>패스(직선)</h1>
		<svg width="300" height="300" style="border:1px solid red">
			<path d="M80,50 L220,90 L280,200"/>
		</svg>
	</body>
</html>
```

#### 실습 exam13

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>패스(직선)</h1>
		<svg width="300" height="300">
			<path d="M80,50 L220,90 L280,200" fill="red" 
			       stroke="blue" stroke-width="8"/>
		</svg>
	</body>
</html>
```

#### 실습 exam14

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>패스(직선)</h1>
		<svg width="300" height="300">
			<path d="M80,50 L220,90 L280,200Z" fill="red" stroke="blue" stroke-width="8"/>
		</svg>
	</body>
</html>
```

#### 실습 exam15

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>스타일을 SVG에서 지정</h1>
		<svg>
			<rect x="30" y="20" width="200" height="100" style="fill:red;stroke:blue;stroke-width:10px" />
		</svg>
	</body>
</html>
```

#### 실습 exam16

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
		<style>
			rect {
				fill:red;
				stroke:blue;
				stroke-width:10px;
			}
		</style>
	</head>
	<body>
		<h1>스타일을 CSS로 지정</h1>
		<svg>
			<rect x="30" y="20" width="200" height="100" />
		</svg>
	</body>
</html>
```

#### 실습 exam17

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
		<style>
			rect {
				fill:red;
			}
			#box {
				stroke:blue;
				stroke-width:30px;		
			}
		</style>
	</head>
	<body>
		<h1>ID 이름을 사용하여 지정</h1>
		<svg width="300" height="300">
			<rect x="30" y="20" width="200" height="100" />
			<rect x="80" y="70" width="200" height="100" id="box" />
		</svg>
	</body>
</html>
```

#### 실습 exam18

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
		<style>
			rect {
				fill:red;
			}
			.box {
				stroke:blue;
				stroke-width:10px;
			}
		</style>
	</head>
	<body>
		<h1>CSS 클래스로 지정</h1>
		<svg style="border:1px solid red">
			<rect x="30" y="20" width="200" height="100" />
			<rect x="80" y="70" width="200" height="100" class="box" />
			<rect x="130" y="120" width="200" height="100" class="box" />
		</svg>
	</body>
</html>
```

#### 실습 exam19

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>SVG학습</title>
</head>
<body>
	<!-- C(Control point) 조절점 S 반대편 조절점--> <!-- S자 곡선 을 그리고 싶으면 S를 사용한다. -->
	<h1>배지에 곡선 표시</h1>
	<svg>
		<path
			d="M10 80 C 40 10, 65 10, 95 60 S 150 150, 180 80"
			stroke="#eb6e4c" fill="none" stroke-width="6" stroke-linecap="round"/>
	</svg>
	<hr>
	<svg>
		<path
			d="M10 80 C 40 10, 65 10, 95 80"
			stroke="green" fill="none" stroke-width="6" stroke-linecap="round"/>
	</svg>
	<hr>
	<svg>
		<path
			d="M10 80 C 40 10, 150 150, 180 80"
			stroke="blue" fill="none" stroke-width="6" stroke-linecap="round"/>
	</svg>

</body>
</html>
```

#### 실습 exam20

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>문자의 글꼴 지정</h1>
		<svg >
			<text x="25" y="40" font-size="24px" style="fill:black">SVG 텍스트 예제</text>
			<text x="25" y="80" font-size="24px" font-family="바탕" style="fill:black">SVG 텍스트 예제</text>
			<text x="25" y="120" font-size="24px" font-family="궁서" style="fill:black">SVG 텍스트 예제</text>
		</svg>
	</body>
</html>
```

#### 실습 exam21

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>도형 그룹화</h1>
		<svg width="500">
			<g style="opacity:0.25"> <!-- 그룹으로 묶음 -->
				<rect x="100" y="50" width="100" height="80" />
				<text x="100" y="40"  style="fill:black">Sample Text</text>
			</g>
			<rect x="300" y="50" width="100" height="80" />
			<text x="300" y="40"  style="fill:black">Sample Text</text>
		</svg>
	</body>
</html>
```

#### 실습 exam22

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>
		<h1>도형 이동</h1>
		<svg> <!-- 크롬의 svg width height 기본값 300 150  -->
			<g transform="translate(-200, 40)">
				<rect x="200" y="50" width="100" height="80" />
				<text x="200" y="40" text-anchor="start" style="fill:black">Sample Text</text>
			</g>
		</svg> 
	</body>
</html>
```

#### 실습 exam23

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>SVG로 그리기</title>
</head>
<body>
<h1>도형 회전</h1>
<svg width="200" height="200">
  	<rect x="1" y="1" width="199" height="199" fill="none" stroke="grey"
			stroke-width="1" />

	<!-- taransfrom 시계 방향 +, 반시계 방향 -, 100 100 을 기준으로 회전 -->
  	<g stroke-width="12" stroke-linecap="round">
    <line x1="100" y1="100" x2="150" y2="100" stroke="red"
			transform="rotate(0  100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="blue"
			transform="rotate(180  100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="orange"
			transform="rotate(45   100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="yellow"
			transform="rotate(-45  100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="pink"
			transform="rotate(90   100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="green"
			transform="rotate(-90  100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="steelblue"
			transform="rotate(135  100 100)" />
   <line x1="100" y1="100" x2="150" y2="100" stroke="magenta"
			transform="rotate(-135 100 100)" />
  </g>
  
</svg>
</body>
</html>
```

#### 실습 exam24

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>SVG로 그리기</title>
	</head>
	<body>	
		<h1>도형 확대</h1>
		<svg width="500" height="500">
			<g>
				<rect x="20" y="50" width="100" height="80" />
				<text x="20" y="40"  style="fill:black">Sample Text</text>
			</g>
			<g transform="scale(2.0)"> <!-- 2배 -->
				<rect x="20" y="150" width="100" height="80" />
				<text x="20" y="140"  style="fill:black">Sample Text</text>
			</g>
		</svg>
	</body>
</html>
```

#### 실습 exam25

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<svg>
  <!-- No translation -->
  <rect x="5" y="5" width="40" height="40" fill="green" />
 
  <!-- Horizontal translation -->
  <rect x="5" y="5" width="40" height="40" fill="blue"
        transform="translate(50)" />
 
  <!-- Vertical translation -->
  <rect x="5" y="5" width="40" height="40" fill="red"
        transform="translate(0 50)" />
 
  <!-- Both horizontal and vertical translation -->
  <rect x="5" y="5" width="40" height="40" fill="yellow"
         transform="translate(50,50)" />
</svg>
</body>
</html>
```

#### 실습 exam26

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<svg width="400" height="500" 
    xmlns="http://www.w3.org/2000/svg">
   <defs>
      <linearGradient  id="MyGradient">
          <stop offset="5%" stop-color="#F00" />
          <stop offset="35%" stop-color="#FF0" />
          <stop offset="65%" stop-color="#0F0" />
          <stop offset="95%" stop-color="#00F" />
      </linearGradient>
   </defs>
   <rect fill="none" stroke="url(#MyGradient)" 
       stroke-width="40" x="1" y="1" width="400" height="398"/>
   <rect fill="url(#MyGradient)" stroke="black" 
       stroke-width="5" x="100" y="100" width="200" height="200"/>
</svg>
</body>
</html>
```

#### 실습 exam27

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>group 태그</h1>
<hr>
<svg width="300px" height="200px"">
  <title>Grouped Drawing</title>
  <desc>Stick-figure drawings of a house and people</desc>
  <g id="house" style="fill: none; stroke: black;">
    <desc>House with door</desc>
    <rect x="6" y="50" width="60" height="60"/>
    <polyline points="6 50, 36 9, 66 50"/>
    <polyline points="36 110, 36 80, 50 80, 50 110"/>
  </g>
  <g id="man" style="fill: none; stroke: black;">
    <desc>Male human</desc>
    <circle cx="85" cy="56" r="10"/>
    <line x1="85" y1="66" x2="85" y2="80"/>
    <polyline points="76 104, 85 80, 94 104" />
    <polyline points="76 70, 85 76, 94 70" />
  </g>
  <g id="woman" style="fill: none; stroke: black;">
    <desc>Female human</desc>
    <circle cx="110" cy="56" r="10"/>
    <polyline points="110 66, 110 80, 100 90, 120 90, 110 80"/>
    <line x1="104" y1="104" x2="108" y2="90"/>
    <line x1="112" y1="90" x2="116" y2="104"/>
    <polyline points="101 70, 110 76, 119 70" />
  </g>
</svg>
<hr>
<svg width="300px" height="200px""> <!-- 위에 내용 그대로 가져와서 위치이동하여 사용! -->
  <use xlink:href="#house" x="70" y="80"/>
  <use xlink:href="#woman" x="-80" y="80"/>
  <use xlink:href="#man" x="-30" y="80"/>  
</svg>
</body>
</html>
```

#### 실습 exam28

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>defs 태그</h1>
<hr>
<svg width="300px" height="250px">
  <title>Grouped Drawing</title>
  <desc>Stick-figure drawings of a house and people</desc>
  <defs>
    <g id="house1" style="stroke: black;">
      <desc>House with door</desc>
      <rect x="0" y="41" width="60" height="60" />
      <polyline points="0 41, 30 0, 60 41" />
      <polyline points="30 101, 30 71, 44 71, 44 101" />
    </g>
    <g id="man1" style="fill: none; stroke: black;">
      <desc>Male human</desc>
      <circle cx="10" cy="10" r="10"/>
      <line x1="10" y1="20" x2="10" y2="44" />
      <polyline points="1 58, 10 44, 19 58" />
      <polyline points="1 24, 10 30, 19 24" />
    </g>
    <g id="woman1" style="fill: none; stroke: black;">
      <desc>Female human</desc>
      <circle cx="10" cy="10" r="10" />
      <polyline points="10 20, 10 34, 0 44, 20 44, 10 34" />
      <line x1="4" y1="58" x2="8" y2="44" />
      <line x1="12" y1="44" x2="16" y2="58" />
      <polyline points="1 24, 10 30, 19 24" />
    </g>
    <g id="couple1">
      <desc>Male and female human</desc>
      <use xlink:href="#man1" x="0" y="0" />
      <use xlink:href="#woman1" x="25" y="0" />
    </g>
  </defs>
  <!-- make use of the defined groups -->
  <use xlink:href="#house1" x="0" y="0" style="fill: #cfc;" />
  <use xlink:href="#couple1" x="70" y="40" />
  <use xlink:href="#house1" x="120" y="0" style="fill: #99f;" />
  <use xlink:href="#couple1" x="190" y="40" />
  <use xlink:href="#woman1" x="0" y="145" />
  <use xlink:href="#man1" x="25" y="145" />
  <use xlink:href="#house1" x="65" y="105" style="fill: #c00;" />
</svg>
</body>
</html>
```

#### 실습 exam29

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>애니메이션</h1>
<hr>
<svg width="300px" height="300px">
  <circle cx="150" cy="150" r="10" fill="none" stroke="purple" stroke-width="2">
    <animate attributeName="r" to="150" dur="120s" repeatCount="indefinite" />
  </circle>
  <circle cx="150" cy="150" r="10" fill="none" stroke="royalblue" stroke-width="2">
    <animate attributeName="r" to="150" dur="60s" repeatCount="indefinite" />
  </circle>
</svg>
</body>
</html>
```

#### 실습 exam30

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>애니메이션</h1>
<hr>
<svg width="600" height="400">
  <g id="graphics" font-size="30">
    <rect width="100%" height="100%" fill="lightyellow"/>
    <g>
    <circle cx="50" cy="100" r="50" fill="gray">
      <animate attributeName="cx" attributeType="XML" 
               begin="0;graphics.click"
               values="50;500;300;400;50" 
               dur="20s"
               calcMode="linear" />
      <animate attributeName="fill" attributeType="XML"  
               begin="0;graphics.click"
               dur="20s" 
               values="gray;darkred;red;cyan;lightcyan;green;purple;gray"
               calcMode="linear" />
    </circle>
    <text x="50" y="100">linear</text>
    </g>
    <g>
    <circle cx="50" cy="300" r="50" fill="gray">
      <animate attributeName="cx" attributeType="XML"  
               begin="0;graphics.click"
               values="50;500;300;400;50" 
               dur="20s"
               calcMode="discrete" />
      <animate attributeName="fill" attributeType="XML" 
               begin="0;graphics.click"
               dur="20s" 
               values="gray;darkred;red;cyan;lightcyan;green;purple;gray"
               calcMode="discrete" />
    </circle>
    <text x="50" y="300">discrete</text>
  </g>
  </g>
</svg>
</body>
</html>
```

#### 실습 exam31

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
		@import url('https://cdn.rawgit.com/YJSoft/Webfonts/0.1/BM_JUA.css');
</style> <!-- svg 안에다가 style 태그 사용해도된다. -->
</head>
<body>
<h1>애니메이션</h1>
<hr>
<svg width="160" height="100" style="border: 1px solid black;" xmlns="http://www.w3.org/2000/svg">	
	<text  x="5" y="40" font-family='BM JUA,배달의민족 주아' font-size="40pt" fill="#4e86b1">UNICO
	<animate dur="3.5s" values="#000000; #4e86b1; #000000"  attributeName="fill" repeatCount="indefinite"/></text>
  	<text x="5" y="80" font-family='BM JUA,배달의민족 주아' font-size="40pt" fill="black">UNICO
  	<animate dur="3.5s" values="#4e86b1; #000000; #4e86b1"  attributeName="fill" repeatCount="indefinite"/></text>
</svg>
</body>
</html>
```

#### 실습 exam32

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>SVG파일을 읽어와서 랜더링 하자</h1>
<hr>
<img src="../images/my.svg">
<hr>
<img src="../images/my.svg" width="100" height="100">
<hr>
<img src="../images/my.svg" width="50">
</body>
</html>
```

#### 실습 exam33

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>SVG파일을 읽어와서 랜더링 하자</h1>
<hr>
<img src="../images/logo.svg">
<hr>
<img src="../images/logo.svg" width="100" height="100">
<hr>
<img src="../images/logo.svg" width="50">
</body>
</html>
```



