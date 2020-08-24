# Mock Object

다른 누군가로부터 휴대 전화 서비스(CellphoneService) 기능을 제공 받아 이를 사용한 휴대 전화 문자 발신기(CellphoneMmsSender)를 프로그래밍 한다고 생각해 보자.

![Image for post](https://miro.medium.com/max/60/1*l1U7ejkPRK_UBEyCS4Idow.jpeg?q=20)

![Image for post](https://miro.medium.com/max/479/1*l1U7ejkPRK_UBEyCS4Idow.jpeg)

이를 간단하게 코드로 나타내면 아래와 같다.

![Image for post](https://miro.medium.com/max/60/1*haWJWaeTceXjxl6tlFM5Rg.png?q=20)

![Image for post](https://miro.medium.com/max/938/1*haWJWaeTceXjxl6tlFM5Rg.png)

CellphoneMmsSender의 send() 메소드에 대한 테스트 코드를 작성 하려면 어떻게 해야 할까? 먼저 반환값을 검증하는 것을 고려할 수 있을 것이다. 하지만 테스트 대상인 send() 메소드의 반환 타입은 void 이다. 반환 값이 아니라면 무엇을 검증해야 할까?

CellphoneMmsSender 테스트 관점에서 중요한 것은 실제 문자 메시지를 보내는 것이 아니다. 실제 문자 메시지를 보내는 것은 CellphoneService의 책임이다. 그렇다면 **CellphoneMmsSender send() 메소드에서 검증해야 하는 것은 전달 받은 메시지(msg)를 CellphoneService sendMMS()의 파라메터로 호출 했는지 여부이다.**

CellphoneService의 sendMMS 호출 여부를 테스트 하기 위해서는 CellphoneMmsSender가 참조하고 있는 CellphoneService 객체를 가짜(대역) 객체로 대체하고 이를 검증하는 방법이 있다. 여기서의 사용하는 가짜 객체를 Mock Object 라고 한다.



Mock Object는 [테스트 더블(Test Double)](https://medium.com/@SlackBeck/단위-테스트-케이스와-테스트-더블-test-double-2b88cccd6a96)중 하나 이며 위키피디아에서는 아래와 같이 정의 한다.

> In [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), **mock objects** are simulated objects that mimic the behavior of real objects in controlled ways. **A programmer typically creates a mock object to test the behavior of some other object**, in much the same way that a car designer uses a [crash test dummy](https://en.wikipedia.org/wiki/Crash_test_dummy) to [simulate](https://en.wikipedia.org/wiki/Simulation) the dynamic behavior of a human in vehicle impacts. — https://en.wikipedia.org/wiki/Mock_object

‘행위를 테스트 한다(*test the behavior of some other object*)’는 것은 무슨 의미일까? 위의 휴대 전화 문자 발신기 예제에서 ‘*전달 받은 메시지(msg)를 CellphoneService sendMMS()의 파라메터로 호출 했는지 여부’*가 행위에 해당하며 이를 테스트하는 것이다. 이를 **행위 검증(Behavior Verification)**이라고 한다.







#### 참고

- [Mock Object란 무엇인가?](https://attila.atlassian.net/wiki/pages/viewpage.action?pageId=40304642)