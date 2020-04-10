# Day1 Bixby Developer

## 음성 인식과 자연어 이해

#### ASR, NLU

- ASR(Automatic Speech Recognition) : **발화**(=사람이 말하는 음성 언어)를 문자로 변환하는 기술

  Text: "오늘 서울 날씨 알려줘"

- NLU(Natural Language Understanding): 문장의 의미를 이해하는 기술

  Text: "오늘 서울 날씨 알려줘"

## Bixby 서비스 아키텍처

사용자 발화부터 시작하여 인식 결과가 나올 때까지

Client -> ASR -> NLU -> Dynamically Generate Plan(그래프를 이용해서 확인이 가능하다)-> Processing Plan -> Cell phone

[Capsule]

Concept, Action, Javascript Code, Bixby Views, Dialog, Training, Debugging

- Capsule 구조

  1. 모델링

     **Concepts**

     - 발화 인식 및 발화 결과를 리턴할 떄 필요한 값

     예) "햄버거 2개 주문해줘"

     ​		햄버거 -> FoodName, 2 -> NumberOfFood

     **Actions**

     - 캡슐이 사용자가 원하는 작업을 이해하도록 수행할 동작을 정의

  2. 비즈니스 로직

     **Javascript Code**

     - 사용자가 원하는 작업을 실제 수행하는 코드
     - 이 단계에서 서비스 API를 연동

  3. UI/UX

     **Bixby Views**

     - 최종 결과를 사용자에게 보여주는 레이아웃 작업

     **Dialog**

     - 사용자에게 되묻거나 결과를 응답해주는 응답문을 생성

  4. 트레이닝

     **발화 Training**

     - Capsule이 잘 동작하도록, 처리할 수 있는 발화를 생성하고 자연어 트레이닝(NL Training)을 진행

     **Debugging**

     - 개발한 캡슐이 구현한대로 동작하는지 확인

  ![image-20200112185813461](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200112185813461.png)

  