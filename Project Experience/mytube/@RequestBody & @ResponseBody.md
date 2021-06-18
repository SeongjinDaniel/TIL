# @RequestBody & @ResponseBody



웹페이지에서 json으로 request한 파라미터들을 java에서 받으려면 java object로의 변환이 필요하며 

마찬가지로 response 시에도 java object에서 json으로 변환이 필요하다.

이러한 작업들을 해주는 어노테이션이 바로 @RequestBody 와 @ResponseBody 이다. 

컨트롤러에 두 어노테이션을 추가해주면, JSON이나 key/value 방식 xml 등으로 송수신 할 수 있다.



## @ResponseBody

**@RequestBody 어노테이션이란?**

- **HTTP 요청의 body 내용을 자바 객체로 매핑하는 역할을 합니다.**



이 어노테이션이 붙은 파라미터에는 HTTP 요청의 본문 body 부분이 그대로 전달된다. **RequestMappingHandlerAdapter**에는 **HttpMessageConverter** 타입의 메시지 변환기(message converter)가 여러 개 등록되어 있다. @RequestBody가 붙은 파라미터가 있으면 HTTP 요청의 미디어 타입과 파라미터의 타입을 먼저 확인한다. (dispatcher-servlet.xml 에서 확인) 메시지 변환기 중에서 해당 미디어 타입과 파라미터 타입을 처리할 수 있다면, HTTP 요청의 본문 부분을 통째로 변환해서 지정된 메소드 파라미터로 전달해준다.

**쉽게 말하자면 @RequestBody 어노테이션을 이용하면 HTTP 요청 Body를 자바 객체로 전달받을 수 있다.**

@RequestBody 어노테이션은 요청에서 Body부분을 살펴 요청된 데이터를 추출하여 파라미터로 변환해주는데, ‘GET’ 메소드 요청의 경우에는 HTTP Body에 요청이 전달되는 것이 아니라, URL의 파라미터로 전달 (ex: http://localhost:8080/test?id=admin&name=hanq…) 형식으로 전달되기 때문에 @RequestBody로 받으려고 해도 서로 다른 곳을 보며 데이터가 없다는 결과를 던질 수 밖에 없다.



## @ResponseBody

**@ResponseBody 어노테이션이란?**

- **자바 객체를 HTTP 요청의 body 내용으로 매핑하는 역할을 합니다.**



@ResponseBody는 @RequestBody와 비슷한 방식으로 동작한다. @ResponseBody가 메서드 레벨에서 부여되면 메서드가 리턴하는 오브젝트는 뷰를 통해 결과를 만들어내는 모델로 사용하는 대신, 메시지 컨버터를 통해 바로 HTTP 응답의 메시지 본문으로 변환된다.

**간단히 이야기 하자면, 요청한 형태에 맞춰서 메시지 변환기를 통해 결과값을 반환한다. @ResponseBody는 @RequestBody가 선택한 형식으로 결과값을 변환하여 반환한다고 보면 된다. 또한 @ResponseBody을 이용하면 자바 객체를 HTTP 응답 body로 전송할 수 있다.**



#### 참고

- https://devyj.tistory.com/3
- https://codelib.tistory.com/24

- [@ReqeustBody와 @ResponseBody 언제 사용할까?](https://medium.com/webeveloper/reqeustbody%EC%99%80-responsebody-%EC%96%B8%EC%A0%9C-%EC%82%AC%EC%9A%A9%ED%95%A0%EA%B9%8C-2efcab364edb)