# @SessionAttributes vs HttpSession



@SessionAttributes 와  HttpSession중에 무엇을 사용해야 좋을지에 대한 반론을 할 수 없어서 서칭을 해보았음.



---

Spring 참조 문서에 따르면 `@ModelAttribute`주석이 달린 메소드 인수는 다음과 같이 해결됩니다.

- 존재하는 경우 모델 객체에서 검색 (일반적으로 `@ModelAttribute`주석이 달린 메서드 를 통해 추가됨 )
- 을 사용하여 HTTP 세션에서 검색합니다 `@SessionAttributes`.
- `@ModelAttribute`변환기를 통해 이름 과 일치하는 URI 경로 변수를 사용하여 생성
- 기본 생성자를 사용하여 생성하고 `Model`.

핸들러 클래스는 `@SessionAttributes`이름 목록을 인수로 사용하여 주석을 달 수 있습니다 . 이것은 `@SessionAttributes`주석에 지정된 이름과 일치하는 모델 데이터에 존재하는 데이터 항목을 (세션에서) 유지하도록 Spring에 지시하는 것 입니다.

따라서 메서드의 `@ModelAttribute`인수는 `@SessionAttributes`위에서 언급 한 해결 방법으로 인해 필드로 해결됩니다 .

---



HttpSession은 모델과의 연관성을 따지지 않으므로 Model을 사용하지 않으면 Session 집중할 수 있는 HttpSession을 사용하는것이 바람직하다.



#### 참고

- [Spring MVC - @SessionAttributes Annotation](https://goodgid.github.io/Spring-MVC-SessionAttributes/)
- [핸들러 메서드: @SessionAttributes, @SessionAttribute](https://sun-22.tistory.com/53)
- [@SessionAttributes vs HttpSession](https://stackoverflow.com/questions/27191798/spring-sessionattributes-vs-httpsession)
- [Spring SessionAttributes or httpsession](https://stackoverflow.com/questions/27175069/spring-sessionattributes-or-httpsession)
- https://stackoverflow.com/questions/4914071/i-am-confused-about-how-to-use-sessionattributes