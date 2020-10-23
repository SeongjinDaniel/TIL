# Contructor injection 권장 사항 5가지



1. 단일 책임의 원칙

- 생성자의 인자가 많을 경우 코드량도 많아지고, 의존관계도 많아져 단일 책임의 원칙에 위배된다. 그래서 Constructor Injection을 사용함으로써 의존관계, 복잡성을 쉽게 알수 있어 리팩토링의 단초를 제공하게 된다.

2. 테스트 용이성

- DI 컨테이너에서 관리되는 클래스는 특정 DI 컨테이너에 의존하지 않고 POJO여야 한다. DI 컨테이너를 사용하지 않고도 인스턴스화 할 수 있고, 단위 테스트도 가능하며, 다른 DI 프레임 워크로 전환할 수도 있게 된다. 또한, 생성자 주입은 단위 테스트 작성을 단순화합니다.

3. Immutability

- Constructor Injection에서는 필드는 final로 선언할 수 있다. 불변 객체가 가능한데 비해 Field Injection은 final는 선언할 수 없기 때문에 객체가 변경 가능한 상태가 된다. 생성자의 주입이 개체를 만드는 유일한 방법이기 때문에 생성자 주입은 [변경 불가능한 개체](https://reflectoring.io/java-immutables) 를 만드는 데 도움이 됩니다.

4. 의존성 명시

- 의존 객체 중 필수는 Constructor Injection을 옵션인 경우는 Setter Injection을 활용할 수 있다.

5. 순환 의존성

- Constructor Injection에서는 멤버 객체가 순환 의존성을 가질 경우 BeanCurrentlyInCreationException이 발생해서 순환 의존성을 알 수 있게 된다.