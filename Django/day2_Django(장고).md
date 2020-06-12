# day2 Django

**Django mdn**

https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction



#### 검색

View 함수가 2개가 필요하다.

1. 사용자로부터 입력을 받는 form을 보여주는 view
2. 입력된 데이터를 받아서 처리하는 view





WSGIRequest -> Web Server G Interface

**throw catch**

**HTTP 요청 메서드**

http method mdn 구글에 검색

[`GET`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/GET)

`GET` 메서드는 특정 리소스의 표시를 요청합니다. `GET`을 사용하는 요청은 오직 데이터를 받기만 합니다.

- HTTP method 중 GET 요청은 서버로부터 정보를 조회하는데 사용됩니다.
- 서버의 데이터나 상태를 변경시키지 않기 때문에 단순 조회(html)할 때 사용.
- 데이터를 전송할 때 http body가 아니라 쿼리스트링을 통해 전송. (URL로 데이터가 넘어간다. 이것을 query string이라고 한다.)  - ?뒤쪽을 쿼리스트링이라고한다.

[`POST`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/POST)

`POST` 메서드는 특정 리소스에 엔티티를 제출할 때 쓰입니다. 이는 종종 서버의 상태의 변화나 부작용을 일으킵니다.





**form에서 중요한 것**

1. 데이터를 어디로 보낼 것인지 => action
2. 어떤 방식으로 보낼지 => method
3. 어떤 데이터를 보낼지 => input, type
4. 데이터의 이름은 어떻게 붙일지 => name
5. 제출 => submit