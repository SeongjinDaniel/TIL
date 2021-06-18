# Day1 Ajax

jstl-1.2.jar 파일을 WebContent/WEB-INF/lib에 붙여넣는다.

[ Query String (쿼리 문자열)]

웹 클라이언트에서 웹 서버에 정보를 요청할 때 추가로 전달하는 문자열이 문자열을 정해 규칙으로 구성되어 전달되어야 하는데 이 규칙을 URL encoding 또는query encoding 규칙이라 한다.

- 모든 데이터들은 name-value 형식이어야 한다.
- 여러개의 name=value쌍을 전달할 때는 & 기로호 반드시 구분해야한다.
- 공백은 + 문자로 변환되어 전달된다.
- 영문과 숫자 그리고 일부 특수문자를 제외하고 % 기호와 함께 16진수 코드값으로 전달되어야 한다.



[https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=ABCabc+123%EA%B0%80%EB%82%98%EB%8B%A4](https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=ABCabc+123가나다)

id=%EA%B0%80%EB%82%98%EB%8B%A4&passwd=dasdf

id=100%20200&passwd=12345





