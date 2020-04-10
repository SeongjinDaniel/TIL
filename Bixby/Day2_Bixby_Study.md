# Day2 Bixby Developer(강의 정리)

##  3-1강. Modeling - Action & Concept

### Action 뜯어보기

- Action명 : Action의 이름
- Type : Action 종류를 설정하는 부분, Bixby 시스템이 Action 을 검색할 때 힌트를 줌
- Input : Action 실행에 필요한 입력 값을 지정하는 부분
  - 변수명: ACiton에서 해당 Concept이 사용되는 이름
  - Concept명 : Concept의 이름
  - Min & Max : 발화로부터 이 input이 몇개 받아들일지 결정
- Output: Action 실행의 결과

![image-20200119142852624](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119142852624.png)

- inupt rightOperand : 변수명

- type RightOperand : concept명

- Min 

  - Required(입력 값이 꼭 포함되어야 한다. )

    만약 input의 min이 사용자의 발화에서 해당 input이 해당 되지 않는다면 Bixby는 자동으로 해당 input에 대하여 물어보게 된다.

  - Optionary(입력 값이 포함 되지 않아도 된다.)

- Max

  - One

    해당 input이 하나 !, 만약 input이 여러개 들어온다면 맨 처음에 있던 것만 시스템적으로 받아 들이게 된다.

  - Many

    해당 input이 여러개 !

- output

  액션을 실행할 결과를 어떤 형식으로 결과를 발행할지를 결정한다.

  output 괄호 안에 해당 concept명을 넣어서 해당 concept의 형식대로 action의 발화의 결과를 나타낼수 있게 한다.

### Concept의 종류

- Primitives(다른 프로그래밍 언어와 같이 기본 자료형이라고 불리는 것과 같다.)

  - Bolean, Integer, Decimal, Name, Text, Enum, Qualified

    - Primitive 타입은 기본형 변수라고도 하며, 9가지가 있음.
    - Boolean은 True/False를 저장하는 타입
    - Decimal은 실수형 숫자를 저장하는 타입
    - Integer은 정수형 숫자를 저장하는 타입
    - Enum은 열거할 수 있는 문자열을 저장하는 타입*
    - Name은 짧은 문자열을 저장하는 타입*
    - Qualified는 Name과 기본적으로 비슷하지만 지정 패턴에 맞는 데이터를 저장
    - Text는 긴 문자열을 저장하는 타입*

    별 표시된 타입은 문자열을 저장하는 공통점, 그러나 NL 트레이닝시에 역할이 상이(뒤에서 더 다룰 예정)

    ![image-20200119145210997](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119145210997.png)

- Structure(C언어의 구조체와 비슷하다.)

  - Primitive 타입들을 묶어서 하나의 객체로서 사용하는 타입
  - C의 구조체와 비슷한 역할
  - Structure 구조
    - Structure명: Structure의 이름
    - Property: Structure의 일부분이 될 Concept
      - Property명: 해당 structure에서 사용될 Concept의 이름
      - Type : Concept 이름
      - Min & Max : 해당 structure에서 가질 수 있는 Concept의 갯수

![image-20200119145633744](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119145633744.png)

서로 다른 기본형 변수들을 묶어서 사용하는 객체 타입(C의 구조체)

Structure 이름은 action이나 view에서 호출할때 사용된다. 

property는 구현하려는 기본형 변수를 넣고 이름을 지정할수 있다. 이름은 structure 혹은 action에서 호출 할 때 사용된다.

type은 primitive concept 명을 넣어주면 된다.

min의 경우는 이 property의 대입이 들어갈것이냐 아니냐를 결정한다.

max의 경우는 이 property의 한개를 받을 것이냐 여러개를 list형식으로 받아 들일것이냐를 결정한다.

#

## 모델링 동작

action은 Bixby가 사용자를 대신하여 수행 할 수 있는 action을 정의합니다. concept이 명사이면 actions은 동사이다. 동작의 예는 다음과 같다.

FindRestaurants: 식당을 검색한다.

ConvertTemperature: 온도 변환 계산을 수행한다.

BookHotel: 호텔 객실을 예약하는 거래 작업을 수행한다.

프로그래밍 용어로 너는 action model을 인터페이스 사양으로 생각하여 action inputs와 action output을 설명할 수 있다. 또한 API 요청 및 계산과 같은 실제 작업을 수행하려면 JavaScript function을 구현해야합니다. 해당 JavaScript function에 접근 하려면 너는 endpoints 선언(endpoints.bxb)을 포함해야합니다.

## 3-2강. 유연한 Modeling을 만드는 여러 기법

### 유연한 Modeling을 만드는 여러 기법

- 01 Bixby 값 검증 및 에러 처리
- 02 Default Init
- 03 Evaluate
- 04 Input Group
- 05 Computed Input
- 06 Role-of & Extends

### Bixby 값 검증 및 에러 처리

- Validation : Input 값이 의도대로 저장 되었는지를 검증
  - Replace : Validation을 통과하지 못할 경우, 특정 값으로 대체
  - Replan : Validation을 통과하지 못할 경우, 다른 Action을 실행
  - Halt : Validation을 통과하지 못할 경우, Action 실행을 멈추고 에러 메시지를 화면에 띄움
  - Unlock : 실행을 멈추고 기기에 lock screen을 띄움
- Relaxation : Action의 결과가 없을 경우, 이 다음 상황을 어떻게 만들지를 구성
  - On-empty : 이 문법을 사용하며, 사용법은 Validation과 유사하다.
- Throws : Javascript에서 던진 에러를 처리하는 부분

![image-20200119155325965](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119155325965.png)

Validation↑↑↑↑↑↑↑↑↑↑↑↑

![image-20200119155403407](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119155403407.png)

output 값이 존재 하지 않을때↑↑↑↑↑↑↑↑↑↑↑↑!! Validation과 비슷하지만 ouput 구문에서 사용하는 것이 다르다.

![image-20200119155654105](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119155654105.png)

Throws는 Javascipt와 관련이 있다. 자바스크립트의 에러를 받아서 처리!

------

### Default init

Default-init: 해당 Concept의 값이 업을 경우, 기본적으로 실행할 action 혹은 값을 지정

![image-20200119155906864](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119155906864.png)

input으로 phoneInfo값을 받게 되는데 이 값이 없을 경우 ShowPhoneList값을 실행하라 라는 의미를 가지게 됩니다. 

### Evaluate

Evaluate: 일반적으로 action에는 항상 action의 output을 만들기 위한 JS 코드가 필요, 그러나 이 input을 그대로 전달하는 식의 간단한 logic이면 evaluate 기능을 사용해서 JS 코드 없이 action을 수행 가능.

![image-20200119160845330](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119160845330.png)

액션에 입력한 값을 그대로 결과값으로 보내는 정도의 행동만 하게 되는 코드들이 간혹 있습니다. 그럴 경우에 아래 노란 박스 처럼 간단하게 구현이 가능하다. 이럴 때 evaluate 기능을 사용하게 된다. 그러면 자바스크립트 코드없이 액션에서 해당 로직을 수행할 수 있다. 이러면 action과 이어주는 endpoints 파일을 추가할 필요가 없어진다.

### Input-group

Input-group: 여러 input을 한가지로 묶어서 이 그룹에 대한 최대 최소 개수를 input들을 관리

- OneOf: input group의 멤버중 한가지만 받음
- OneOrMoreOf: input group의 멤버중 한가지 또는 그 이상을 받음
- ZeroOrOneOf: input group의 멤버들을 안받거나 그 중 한가지만 받음.
- ZeroOrMoreOf: input group의 멤버들을 안받거나 여러 멤버를 받음

=> requires(~~) 문법으로 정의가 가능하다.

​		requires(OneOf), requires(OneOrMoreOf), requires(ZeroOrOneOf), requires(ZeroOrMoreOf)

![image-20200119163946510](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119163946510.png)

현재 예제 에서는 requires(Oneof)라고 적혀 있는 것을 보니 아래 많은 input들 중에서 한가지만 받겠다.!!라는 뜻이다.

### Computed- input

Computed-input: 다른 input값을 가져와 사용하거나 action 실행등을 하기 위한 안전한 방법

- 해당 액션에서 다른 input 값 가져옴
- 다른 액션에서 값 얻어옴
- 해당 액션에 input 값을 가져오거나 다른 액션에서 다른 concept값을 가져오거나

![image-20200119164629285](C:\Oliver\blueboy\documents\git\TIL\Bixby\image-20200119164629285.png)

### Role-of & Extends

공통점 : 기존에 만들어진 Concept을 재사용

Role-of : 기존 Concept을 복제

extends : 기존 Concept을 상속

![image-20200119164953062](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200119164953062.png)