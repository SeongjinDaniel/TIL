# Jackson



객체의 직렬화, 역직렬화에서 가장 선호하는 방법은 JSON(JavaScript Object Notation)입니다. 일단 JSON 포맷의 확장성과 간결함이 좋습니다. 그리고 웬만한 포맷들은 JSON을 지원하여 변환이 가능합니다.



- 다목적으로 사용 가능한 JSON 처리 라이브러리
- Java 세상의 최고 갑인 Spring에서 사용하는 JSON 라이브러리
- Mapper 패턴으로 CSV 등 다른 포맷으로도 변환이 용이



Jackson의 경우 다양한 추가 모듈이 존재해서 JSON을 Avro, BSON, CBOR, CSV, Smile, (Java) Properties, Protobuf, XML or YAML으로 저장하기 등의 추가 기능으로 확장하기 좋습니다. 그래서 의존성 패키지들이 덕지 덕지 붙긴하지만 편리합니다.



#### 참고

- [Java Library Jackson](https://blog.lulab.net/programming-java/java-library-jackson/)

- https://github.com/FasterXML/jackson-modules-java8

- [[Java] ObjectMapper 클래스](https://nowonbun.tistory.com/289)

- [RedisTemplate 과 Json Serializer 설정](https://somoly.tistory.com/134)

  