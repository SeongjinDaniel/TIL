# [jQuery\] ajax로 값을 가져올 때 UTF-8 환경에서 한글깨짐 해결하기 - 자바(java)

요즘은 한글 뿐만이 아니라 국제화를 위해 다국어를 지원하기 위해 UTF-8 인코딩 상태에서 개발을 하는 경우가 많죠. 저도 어느 프로젝트를 가든 UTF-8로 작업을 하게 됨. 예전엔 iframe으로 숨겨서 작업하던 걸 요즘엔 jQuery ajax로 많이 작업을 함. 그런데, UTF-8에서 ajax를 사용하다보면 한글깨짐 현상이 발생함.

이렇게 한글이 깨지는 이유는 무엇인지 해결방법을 알아보자!!

##### ajaxTest.jsp

```javascript
$.ajax({
    type: "post",
    url: "ajaxTestJson.do",
    data: param,
    dataType: "json",
    success: function (jsonObj) {
        alert( jsonObj.ajaxName );
    }
});
```

##### ajaxTest.java

```java
@RequestMapping
@ResponseBody
public String ajaxTestJson(ajaxTestVO vo) throws Exception
       {
    String ajaxName = "Platform별 표준 오디오 설계 구축_I";
    
    JSONObject jsonObj = new JSONObject();
    jsonObj.put("ajaxName", JSONArray.fromObject(ajaxName, MarketingAnonymousClass.getJsonConfig()));
    
    return jsonObj.toString();
}
```

위 프로그램의 실행 순서는 다음과 같습니다.

1. ajax로 ajaxTestJson.do 호출

2. ajaxTextJson.do가 ajaxTest.java의 ajaxTestJson 메소드를 호출한다.

3. ajaxName 값을 가져와서 ajax 호출한 곳에 값을 보낸다. (인코딩 필요)

4. ajax로 ajaxName 값을 받는다. (디코딩 필요) 

5. ajaxName 값을 alert() 함수로 화면에 출력한다.

**java 파일에서 ajax로 값이 넘어올 때 한글이 깨지게 되므로 java 파일에서 UTF-8로 인코딩을 해서 ajax로 넘겨준 후에 ajax에서 받아서다시 디코딩을 해주면 한글이 깨지지 않고 잘 출력이 됩니다.**

##### ajaxTest.jsp

```javascript
$.ajax({
    type: "post",
    url: "ajaxTestJson.do",
    data: param,
    dataType: "json",
    success: function (jsonObj) {
 
        // 디코딩하여 변수에 담는다.
        var ajaxName = decodeURIComponent( jsonObj.ajaxName );
 
        alert( ajaxName );
    }
});
```

```
decodeURIComponent( 변수 ); 
```

##### ajaxTest.java

```java
@RequestMapping
@ResponseBody
public String ajaxTestJson(ajaxTestVO vo) throws Exception
       {
    String ajaxName = "Platform별 표준 오디오 설계 구축_I";
 
    // 한글깨짐 방지를 위해 인코딩하기
    URLEncoder.encode(ajaxName , "UTF-8");
    
    JSONObject jsonObj = new JSONObject();
    jsonObj.put("ajaxName", JSONArray.fromObject(ajaxName, MarketingAnonymousClass.getJsonConfig()));
    
    return jsonObj.toString();
}
```

```
URLEncoder.encode(변수, "UTF-8");
```

위와같이 인코딩/디코딩 변환을 해주면 한글이 깨지지 않고 잘 나오게 된다



그런데, 이렇게만 했을 때, 공백이 +로 변환되는 문제가 있어요. 아래처럼 디코딩하기 전에 +를 공백으로 바꿔주시면 해결!! 변수명이 con이라고 할때 아래처럼 하면 된당!!

```
var Ca = /\+/g;
decodeURIComponent( con.replace(Ca, " ") );
```

