# Leflet 라이브러리

1. 새로운  Dynamic Web Project 생성 : d3edu
2. character encoding : UTF-8
3. Tomcat 서버에 등록
4. 

## GeoJSON



[ 대한민국 행정동 경계 좌표 추출 ]

https://woonizzooni.tistory.com/entry/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%ED%96%89%EC%A0%95%EB%8F%99-%EA%B2%BD%EA%B3%84-%EC%A2%8C%ED%91%9C-%EC%B6%94%EC%B6%9C-1-GeoJSON

[ 국가 공간정보 포탈 ]

http://www.nsdi.go.kr/lxportal/?menuno=2679

[ leaflet 도큐먼트 ]

https://leafletjs.com/reference-1.6.0.html

[ geojson 문서 생성 사이트 ]

http://geojson.io/#map=10/33.4051/126.5048

[ SVG 학습시 ]

https://thenounproject.com/



#### 실습

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
</head>
<body>
   <p id="demo">위치정보를 추출하려면 실행 버튼을 클릭하세요:</p>
   <button onclick="getLocation()">실행</button>
   <hr>
   <div id="mapid" style="width: 600px; height: 400px;"></div>
   <script>
      var x=document.getElementById("demo");
	  function getLocation() {
         if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition,showError);
         }
         else {
        	 x.innerHTML=" 이 브라우저는 geolocation을 지원하지 않습니다.";        	
       	 }         
      }
      function showPosition(position) {
          x.innerHTML="위도: " + position.coords.latitude + "<br />경도: " + position.coords.longitude;
          var lat = position.coords.latitude;
          var lng = position.coords.longitude;
          var mymap = L.map('mapid').setView([lat, lng], 1)
          	// 이정보를 쓰면 지도 오른쪽 아래에 Leflet 지도라는 것이 기재된다.
			L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
				maxZoom: 18,
				attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
					'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
					'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
				id: 'mapbox.streets'
			}).addTo(mymap);

       		// L.marker를 통해서 표시해줌
			// bindPopup("<b>우리가 있는 곳... 쬠 이상하다ㅜ") 팝업창을 보여줌
			// openPopup하면 마커만 출력 되는게 아니라 팝업창도 같이 출력된다.
			L.marker([lat, lng]).addTo(mymap)
				.bindPopup("<b>우리가 있는 곳... 쬠 이상하다ㅜ").openPopup(); 
			
      }
      function showError(error) {
         switch(error.code) {
            case error.PERMISSION_DENIED:
               	x.innerHTML="사용자가 위치 기능 사용을 거부했습니다."
            	break;
 
            case error.POSITION_UNAVAILABLE:
            	x.innerHTML="위치를 구할 수 없습니다.";
           	 	break;
 
            case error.TIMEOUT:
           	 	x.innerHTML="사용자가 위치 기능 사용을 거부했습니다.";
            	break;
            case error.UNKNOWN_ERROR:
            	x.innerHTML="기타 에러";            	
         }
      }
</script>
</body>
</html>
```

------------

#### 실습

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
</head>
<body>
   <p id="demo">위치정보를 추출하려면 실행 버튼을 클릭하세요:</p>
   <button onclick="getLocation()">실행</button>
   <hr>
   <div id="mapid" style="width: 600px; height: 400px;"></div>
   <script>
      var x=document.getElementById("demo");
	  function getLocation() {
         if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition,showError);
         }
         else {
        	 x.innerHTML=" 이 브라우저는 geolocation을 지원하지 않습니다.";        	
       	 }         
      }
      function showPosition(position) {
          x.innerHTML="위도: " + position.coords.latitude + "<br />경도: " + position.coords.longitude;
          var lat = position.coords.latitude;
          var lng = position.coords.longitude;
          var mymap = L.map('mapid').setView([lat, lng], 1)
          	// 이정보를 쓰면 지도 오른쪽 아래에 Leflet 지도라는 것이 기재된다.
			L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
				maxZoom: 18,
				attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
					'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
					'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
				id: 'mapbox.streets'
			}).addTo(mymap);

       		// L.marker를 통해서 표시해줌
			// bindPopup("<b>우리가 있는 곳... 쬠 이상하다ㅜ") 팝업창을 보여줌
			// openPopup하면 마커만 출력 되는게 아니라 팝업창도 같이 출력된다.
			L.marker([lat, lng]).addTo(mymap)
				.bindPopup("<b>우리가 있는 곳... 쬠 이상하다ㅜ").openPopup(); 
			
      }
      function showError(error) {
         switch(error.code) {
            case error.PERMISSION_DENIED:
               	x.innerHTML="사용자가 위치 기능 사용을 거부했습니다."
            	break;
 
            case error.POSITION_UNAVAILABLE:
            	x.innerHTML="위치를 구할 수 없습니다.";
           	 	break;
 
            case error.TIMEOUT:
           	 	x.innerHTML="사용자가 위치 기능 사용을 거부했습니다.";
            	break;
            case error.UNKNOWN_ERROR:
            	x.innerHTML="기타 에러";            	
         }
      }
</script>
</body>
</html>
```

----------

#### 실습

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="http://code.jquery.com/jquery-1.7.js"></script>
</head>
<body>
	<h1>주소와 좌표 변환 프로그램</h1>
	<button onclick="addToCoord();">주소를 좌표로</button>
	<button onclick="coordToAddr();">다시 주소로</button>
	<script>
	var latlng;
		function addToCoord() {
			var address = prompt("주소를입력하세요");
			var lat;
			var lng;
			if (address) {
				$.getJSON("https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyD8k2DWC_7yFHCrH6LDR3RfITsmWMEqC8c&address="+encodeURIComponent(address), function(data) {
					lat = data.results[0].geometry.location.lat;
					lng = data.results[0].geometry.location.lng;
					alert("좌표로 : " + lat + ":" + lng);		
					latlng = encodeURIComponent(lat+","+lng);											
				});		
				
			}
		}
	    function coordToAddr() {
	    	$.getJSON("https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyD8k2DWC_7yFHCrH6LDR3RfITsmWMEqC8c&latlng="+latlng, function(data) {
				alert("다시 주소로 : " + data.results[0].formatted_address);				
										
			});
	    }
	</script>
</body>
</html>
```

--------

#### 실습

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
</head>
<body>
	<h1>주소와 좌표 변환 프로그램</h1>
	<button onclick="addToCoord();">주소입력</button>
	<hr>
	<div id="mapid" style="width: 600px; height: 400px;"></div>
	<script>
	var mymap;
	function addToCoord() {
		var address = prompt("주소를입력하세요");
		var lat;
		var lng;
		
		if (address) {		
			var xhr = new XMLHttpRequest();
			xhr.onload =  function() { 
				if(xhr.status == 200) {
					var data = JSON.parse(xhr.responseText);
					lat = data.results[0].geometry.location.lat;
					lng = data.results[0].geometry.location.lng;
					alert("좌표로 : " + lat + ":" + lng);
					if(mymap)
						mymap.remove();
					mymap = L.map('mapid').setView([lat, lng], 16)
					L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
						maxZoom: 18,
						attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
							'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
							'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
						id: 'mapbox.streets'
					}).addTo(mymap); 

					L.marker([lat, lng]).addTo(mymap).bindPopup("<b>여기...").openPopup();   
				}
			};
			
			xhr.open("GET", "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyD8k2DWC_7yFHCrH6LDR3RfITsmWMEqC8c&address="+encodeURIComponent(address), true);
			xhr.send();
		}		
	}
	</script>
</body>
</html>
```

---------

#### 실습 exam1

```html
<html>
<head>
  <title>A Leaflet map!</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  <style>
    #mapid{ height: 100% }
  </style>
</head>
<body>

  <div id="mapid"></div>

  <script>

  // initialize the map
  var mymap = L.map('mapid').setView([42.35, -71.08], 3);

  // load a tile layer
  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

    var xhr = new XMLHttpRequest();
	xhr.onload =  function() { 
		if(xhr.status == 200) {
			var data = JSON.parse(xhr.responseText);
  	  		L.geoJson(data).addTo(mymap).bindPopup(function (layer) {
      			return layer.feature.properties.name;
  			});
		}
 	 };
    xhr.open("GET", "countries.geojson", true);
	xhr.send();

  </script>
</body>
</html>
```

------------

#### 실습 exam10

```html
<html>
<head>
  <title>A Leaflet map!</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
  <script src="http://code.jquery.com/jquery-2.1.4.min.js"></script>
  <style>
    #mapid{ height: 100% }
  </style>
</head>
<body>
	<div id="mapid" style="width: 600px; height: 400px;"></div>
  	<script>
  	var mymap = L.map('mapid').setView([37.566, 126.978], 12);

  	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
			maxZoom: 18,
			attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
			id: 'mapbox.streets'
	}).addTo(mymap);
  	
    var xhr = new XMLHttpRequest();
	xhr.onload =  function() { 
		if(xhr.status == 200) {
			var data = JSON.parse(xhr.responseText);
  	  		L.geoJson(data).addTo(mymap).bindPopup(function (layer) {
      			return layer.feature.properties.adm_nm;
  			});
		}
 	 };
    xhr.open("GET", "20190403.geojson", true);
	xhr.send();  	
  	</script>
</body>
</html>
```

------------

#### 실습 exam2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
    //서울시청 위도,경도 : 37.5662952,126.97794509999994
	var mymap = L.map('mapid').setView([37.566, 126.978], 18); // 18이 최고 줌 레벨

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	L.marker([37.566, 126.978]).addTo(mymap)
		.bindPopup("<b>안녕하세요! 난 팝업이야..</b><br />여기가 서울시청입니다...").openPopup(); // html형식에 맞춰서 rendering 해줌  
	//mymap.dragging.disable();
</script>



</body>
</html>
```

-----------

#### 실습 exam3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
div {
	display : inline-block;  
}
</style>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid1" style="width: 600px; height: 400px;"></div>
<div id="mapid2" style="width: 600px; height: 400px;"></div>
<div id="mapid3" style="width: 600px; height: 400px;"></div>
<div id="mapid4" style="width: 600px; height: 400px;"></div>
<script>
	var mymap1 = L.map('mapid1', { center : [37.566, 126.978], zoom : 18});
	var mymap2 = L.map('mapid2').setView([37.566, 126.978], 1);
	var mymap3 = L.map('mapid3').setView([37.566, 126.978], 5);
	var mymap4 = L.map('mapid4').setView([37.566, 126.978], 10);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap1);
	
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.m/* apbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap2);
	
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.m/* apbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap3); 
	
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.m/* apbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap4); 

</script>
</body>
</html>
```

---------------

#### 실습 exam4

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
	var mymap = L.map('mapid').setView([37.566, 126.978], 14);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	function onMapClick(e) {
		 L.popup()	  
		    .setLatLng(e.latlng)
	        .setContent("여기를 클릭했슈!!!  " + e.latlng)
	        .openOn(mymap);
	}

	mymap.on('click', onMapClick);

</script>
</body>
</html>
```

-----------

#### 실습 exam5

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
	var mymap = L.map('mapid').setView([37.566, 126.978], 16);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
	
	L.marker([37.566, 126.978]).addTo(mymap);
 
	L.circle([37.566, 126.978], 50, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.4
	}).addTo(mymap).bindPopup("나는 원!");

	L.polygon([
		[37.5672, 126.9735],
		[37.5646, 126.9741],
		[37.5647, 126.9767],
		[37.5661, 126.9768]
	], {
		color: 'blue',
		fillColor: 'skyblue',
		fillOpacity: 0.4
	}).addTo(mymap).bindPopup("나는 다각형");

</script>



</body>
</html>
```

-----------

#### 실습 exam6

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
 <style>
 	b {
 		color : red;
 	}
 </style> 
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
	var mymap = L.map('mapid').setView([37.5017, 127.0409], 16);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	var myIcon = L.icon({
	    iconUrl: '/d3edu/images/duke.png',
	    iconSize: [30, 50]
	});
	var content = "<b>우리가 있는 곳!!</b> <img src='/d3edu/images/duke.png' width='20'><hr>여기가 멀티캠퍼스입니다...<br>우리는 1504호에서 공부합니다."
	L.marker([37.5022, 127.0409], {icon: myIcon}).addTo(mymap).bindPopup(content);
   
</script>
</body>
</html>
```

--------------

#### 실습 exam7

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
    //멀티캠퍼스 위도, 경도 : 37.5017, 127.0409
	var mymap = L.map('mapid').setView([37.5017, 127.0409], 16);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	var myIcon = L.icon({
	    iconUrl: '/d3edu/images/duke.png',
	    iconSize: [30, 50]
	});
	// Tooltip은 마우스만 올라가도 팝업이 뜬다. 출력 위치 조정 가능
	// 상하좌우 에서 보이게 가능
	L.marker([37.5022, 127.0409], {icon: myIcon}).addTo(mymap).bindTooltip("우리가 있는 곳!! <br>여기가 멀티캠퍼스입니다...", {direction: 'right', offset :[20,3]})
</script>

</body>
</html>
```

---------

#### 실습 exam 8

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
    //멀티캠퍼스 위도, 경도 : 37.5017, 127.0409
	var mymap = L.map('mapid').setView([37.5017, 127.0409], 16);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	var myIcon = L.icon({
	    iconUrl: '/d3edu/images/duke.png',
	    iconSize: [30, 50]
	});
	
	var m1 = L.marker([37.5022, 127.0409], {icon: myIcon, title:"나 1번이야!!"});
	var m2 = L.marker([37.5032, 127.0409], {icon: myIcon, title:"나 2번이야!!"});
	var m3 = L.marker([37.5022, 127.0439], {icon: myIcon, title:"나 3번이야!!"});
	var m4 = L.marker([37.5032, 127.0429], {icon: myIcon, title:"나 4번이야!!"});
	var m5 = L.marker([37.5012, 127.0429], {icon: myIcon, title:"나 5번이야!!"});
	
	// marking을 여러곳에 할수있음
	var group = L.layerGroup([m1, m2, m3, m4, m5])

	group.addTo(mymap);
</script>
</body>
</html>
```

----

#### 실습 exam 9

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
  
</head>
<body>
<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
    //서울시청 위도,경도 : 37.5662952,126.97794509999994
	var mymap = L.map('mapid').setView([37.566, 126.978], 18);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets-satellite' // 여기!!! 위성지도를 통해서 보여줌!!
	}).addTo(mymap);

	L.marker([37.566, 126.978]).addTo(mymap)
		.bindPopup("<b>안녕하세요! 난 팝업이야..</b><br />여기가 서울시청입니다...").openPopup();   

</script>
</body>
</html>
```

