# Day4 Servlet

[ HttpSession 객체를 이용한 상태정보 유지]
HttpSession 객체를 이용하는 상태 정보 유지는 다음과 같은 특징을 지원한다

- 상태 정보 는 객체로 만들어서 서버에 보관한다
- 상태 정보가 유지되는 최대 시간은 요청을 보내온 브라우저가 기동되어 있는 동안이다.
- 구현 방법
  (1) HttpSession
  객체를 생성하거나 추출한다 .
  (2) HttpSession
  객체에 상태정보를 보관할 객체를 등록한다 . 한번만 등록하면 된다
  (3) HttpSession
  객체에 등록되어 있는 상태정보 객체의 참조 값을 얻어 사용한다 읽기 , 변경
  (4) HttpSession
  객체에 등록되어 있는 상태정보 객체가 더 이상 필요 없으면 삭제 가능하 다
- request.getSession() : HttpSession 객체를 추출하거나 새로이 생성한다 .
  request.getSession(true) 와 동 일하다 r equest.getSession(false) 는
  HttpSession 객체를 추출하여 리턴하는데 없으면 null 을 리턴한다
- session.setAttribute( xxx ””, new Data()) : 보관하려 는 정보를 객체로 만들어
  HttpSession
  객체에 저장한다 xxx 라는 이름으로 객체의 참조 값을 보관한다
- session.getAttribute( xxx ””) : xxx 라는 이름으로 보관된 객체의 참조 값을 리턴한다
- session.removeAttribute( xxx ””) : xxx 라는 이름으로 보관된 객체 의 참조 값을 삭제한다
- session.invalidate() : HttpSession 객체를 강제로 삭제한다

[오늘]

{"p001":3, "p003":4, "p007":2} ---> obj.p001, obj.p003 ....

{"msg": "상품이 모두 삭제되었습니다."} ---> obj.msg

```java
if(obj.msg){
	msg 값 출력
}else{
    선택된 상품 갯수 리스트 출력
}
```



1. charAt(인수) - 인수번째의 문자를 읽어 냅니다.

   예) "javascript".charAt(2)에는 'v'가 읽어 집니다. 0부터 시작하기 때문에 3번째인 'v'가 읽어 집니다.

2. indexOf(인수) - 인수가 들어있는 위치를 알려 줍니다.

   예) "javascript".indexOf("s")에는 4가 읽어 집니다. 0부터 시작하기 때문입니다.(lastIndexOf는 뒤에서부터 셈)

3. substring(인수, 인수) - charAt은 문자하나를 읽어내지만 substring은 문자열을 읽어 냅니다.

   예) "javascript".substring(1, 3)은 "ava"를 추출해냅니다. 0부터 시작하기 때문입니다.