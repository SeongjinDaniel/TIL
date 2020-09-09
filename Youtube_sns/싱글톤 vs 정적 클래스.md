#  싱글톤 vs 정적 클래스

![image](https://user-images.githubusercontent.com/55625864/92617843-b45d9880-f2fa-11ea-994b-80b37ebe0e6a.png)



1. 싱글 톤 객체는 **힙** 에 저장 되지만 정적 객체는 **스택에** 저장됩니다 .
2. 우리는 싱글 톤 객체를 **복제**할 수 있습니다. (디자이너는 그것을 허용하지 않은 경우), 그러나 우리는 정적 클래스 개체를 복제 할 수 없습니다.
3. 싱글 톤 클래스는 **OOP** (객체 지향 원칙)를 따르지만 정적 클래스는 그렇지 않습니다.
4. `interface`Singleton 클래스를 사용하여를 구현할 수 있지만 클래스의 정적 메서드 (예 : C # `static class`)는 구현할 수 없습니다.



- Singleton에는 인스턴스 / 객체가 있고 정적 클래스는 여러 정적 메소드입니다.
- 정적 클래스는 할 수 없지만 인터페이스를 통해 싱글 톤을 확장 할 수 있습니다.
- SOLID 원칙에서 개방 / 폐쇄 원칙을 지원하는 싱글 톤은 상속 될 수 있지만 정적 클래스는 상속 될 수 없으므로 자체적으로 변경해야합니다.
- 인스턴스가없는 정적 클래스는 매개 변수로 전달할 수 없으므로 정적 클래스를 사용하는 동안 Singleton 객체를 메서드에 전달할 수 있습니다
- 

주목할만한 차이점 중 하나는 싱글 톤과 함께 제공되는 다른 인스턴스입니다.

정적 클래스를 사용하면 CLR에 의해 생성되며 제어 할 수 없습니다. 싱글 톤을 사용하면 액세스하려는 첫 번째 인스턴스에서 객체가 인스턴스화됩니다.



백엔드에 연결하는 DB 프레임 워크가 있습니다. 여러 사용자에 대한 더티 읽기를 방지하기 위해 단일 인스턴스를 사용하여 언제든지 단일 인스턴스를 사용할 수 있습니다.



#### 참고

- [정적 클래스와 싱글톤 패턴의 차이점은 무엇입니까?](https://c10106.tistory.com/1860)
- [Difference between Singleton Pattern vs Static Class in Java](https://javarevisited.blogspot.com/2013/03/difference-between-singleton-pattern-vs-static-class-java.html)
- [Singleton pattern(싱글톤) vs. static](https://m.blog.naver.com/PostView.nhn?blogId=satang50&logNo=195684802&proxyReferer=https:%2F%2Fwww.google.com%2F)

- 