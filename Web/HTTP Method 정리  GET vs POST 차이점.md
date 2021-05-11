# HTTP Method 정리 / GET vs POST 차이점



### GET

GET 메소드는 주로 데이터를 **읽거나(Read)** **검색(Retrieve)**할 때에 사용되는 메소드이다.

GET 요청은 idempotent하다. 즉, 같은 요청을 여러 번 하더라도 변함없이 항상 같은 응답을 받을 수 있다. 그러므로 GET을 데이터를 변경하는 등의 안전하지 않은 연산에 사용하면 안된다.

### POST

POST 메소드는 주로 새로운 리소스를 **생성(create)**할 때 사용된다. POST 요청은 안전하지도 않고 idempotent하지도 않다. 다시 말해서 같은 POST 요청을 반복해서 했을 때 항상 같은 결과물이 나오는 것을 보장하지 않는다는 것이다. 그러므로 두 개의 같은 POST 요청을 보내면 같은 정보를 담은 두 개의 다른 resource를 반환할 가능성이 높다.

### GET vs POST

HTTP POST 요청은 클라이언트에서 서버로 전송할 때 추가적인 데이터를 body에 포함할 수 있다. 반면에 GET 요청은 모든 필요한 데이터를 URL에 포함하여 요청한다. HTML의 **<form>**태그에 **method="POST"** 또는 **method="GET"**(기본값)을 모두 사용할 수 있다. 만약에 GET 메소드를 사용하면 모든 form data는 URL로 인코딩되어 action URL에 query string parameters로 전달된다. POST 메소드를 사용하면 form data는 HTTP request의 message body에 나타날 것이다.



#### 참조

- [[HTTP] HTTP Method 정리 / GET vs POST 차이점](https://im-developer.tistory.com/166)

