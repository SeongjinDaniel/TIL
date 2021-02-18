# Day5 JavaScript

#### 실습1 exercise13_1

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	button{
		font-weight : bolder;
		width : 100px;
		height : 50px;
		background-color : #0066ff;
		color : white;
	}
</style>
</head>
<body>
<button onclick="imgVisible(this, true)">이미지 보이기</button>
<button onclick="imgVisible(this, false)">이미지 숨기기</button>
<br>

<img src="/edu/images/duke_luau.png" style="visibility:hidden">
<script>

	//style.display="none"
	//style.display=""
	var image = document.getElementsByTagName('img')[0];
	var imgVisible = function(me, isbool){
		if(isbool) image.style.visibility = "visible";
		else{
			image.style.visibility = "hidden";
		}
	}

</script>
</body>
</html>
```

#### 실습2 exercise13_2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	button{
		font-weight : bolder;
		width : 100px;
		height : 50px;
		background-color : #0066ff;
		color : white;
	}
</style>
</head>
<body>
<button id = "hidden" onclick="imgVisible(this, true)">이미지 보이기</button>
<button id = "visible" onclick="imgVisible(this, false)">이미지 숨기기</button>
<br>

<img src="/edu/images/duke_luau.png" style="visibility:hidden">
<script>
	//style.display="none"
	//style.display=""
	var image = document.getElementsByTagName('img')[0];
	var btns = document.getElementsByTagName("button");
	
	var imgVisible = function(){
		if(this.id == "hidden") image.style.visibility = "visible";
		else image.style.visibility = "hidden";
	};
	
	for(var i in btns)
		btns[i].onclick = imgVisible;

</script>
</body>
</html>
```

#### 실습3 exercise13_3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	button{
		font-weight : bolder;
		width : 100px;
		height : 50px;
		background-color : #0066ff;
		color : white;
	}
</style>
</head>
<body>
<button id = "hidden" onclick="imgVisible(this, true)">이미지 보이기</button>
<button id = "visible" onclick="imgVisible(this, false)">이미지 숨기기</button>
<br>

<img src="/edu/images/duke_luau.png" style="visibility:hidden">
<script>
	//style.display="none"
	//style.display=""
	var image = document.getElementsByTagName('img')[0];
	var btns = document.getElementsByTagName("button");
	
	var imgVisible = function(){
		if(this.id == "hidden") image.style.visibility = "visible";
		else image.style.visibility = "hidden";
	};
	
	for(var i in btns)
		btns[i].addEventListener("click", imgVisible);

</script>
</body>
</html>
```

