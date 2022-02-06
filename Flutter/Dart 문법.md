# Dart 문법

**DartPad**

:bulb: DartPad는 온라인 상에서 Dart를 실행할 수 있는 웹사이트입니다.

- 코드스니펫을 복사한 뒤 주소창에 붙여 넣으면, DartPad로 접속합니다.
  
  - **[[코드스니펫] DartPad 접속](https://dartpad.dev/?id=02d3c1600e40dd95d65af5ca6a3e4d16&null_safety=true)**
  
  ```dart
  main() {
    // 여기서 부터 시작합니다.
    print("Hello Dart"); 
  }
  ```
  
  - 실행 순서
    💡 `main`은 Dart에서 처음 시작 시 호출하는 약속된 함수입니다.
    
    ```dart
    main() {
    }
    ```
    
    ![image](https://user-images.githubusercontent.com/55625864/152087512-66da0d1a-f434-4aed-a5d7-5c3d9674f4ce.png)
  
  - `//` : 주석으로 컴퓨터가 읽지 않습니다. 주로 개발하면서 메모할 때 사용합니다.
  
  - `print()` : print의 소괄호 안쪽에 값을 넣으면 오른쪽 `Console`에 값이 출력 됩니다. 정상적으로 잘 작동하는지 확인(디버깅) 할 때 사용합니다.
  
  - `;` : Dart에서는 마지막에 세미콜론(semicolon)을 찍어줍니다.
  
  - 에러 로그 읽는 법
    💡 아래 이미지를 보면 3번 째 줄에 마지막 세미콜론이 빠졌습니다. 이 상태로 `Run`을 하게되면 우측에 에러 메세지가 나옵니다.
    
    **에러 메세지를 보면 문제가 발생하는 위치와 해결 방법을 알 수 있습니다!** 앞으로 에러가 발생한다면 에러 메세지 부터 확인해 주세요 🙂
    
    ![image](https://user-images.githubusercontent.com/55625864/152087661-a6d75369-ec51-4445-9ee7-7d7b121c21a6.png)
  
  - :bulb:DartPad에서 Reset 버튼을 누르면, 변경한 내용이 초기화 됩니다.
    
    ![image](https://user-images.githubusercontent.com/55625864/152087708-4b15f553-a062-43e6-870d-c210345262c0.png)
1. **변수**
   
   1. 변수 만들기
      
      :bulb: 변수는 어떤 값을 담는 바구니라고 생각하시면 쉽습니다.
      
      ```dart
      var name = '철수'
       1    2      3
      ```
      
      1. 자료형 (= 바구니에 담을 수 있는 값의 종류)
         
         `var` : 처음 담긴 값으로 타입이 지정됩니다.
         
         `String` : 문자만 담을 수 있습니다.
         
         `String?` : 문자 또는 비어있는(`null`) 상태일 수 있습니다.
         
         `final String` : 문자를 한 번 담은 뒤 재할당 불가능합니다.
      
      2. 변수명 (= 바구니 이름)X
         
         :bulb: Dart의 변수명 만드는 규칙
         
         1. `영문` / `_` / `$` / `숫자`만 사용
         
         2. `숫자`로 시작 불가능
         
         3. 카멜케이스(camelCase) 사용
         
         :bulb: 카멜케이스(camelCase)란?
         
         소문자로 시작하며, 단어와 단어 사이를 대문자로 구분하는 방법
         낙타의 혹과 같이 생겨서 camelCase라고 부릅니다.
         
         예) helloWorld, whereAreYouFrom
         
         변수의 이름을 부르면 변수에 담긴 값이 나옵니다.
         
         ```dart
         var name = "철수";
         print(name); // 철수
         ```
      
      3. 변수에 담으려는 값 (= 바구니에 담기는 값)
         
         :bulb: 변수에는 문자, 숫자 등 여러 자료형을 담을 수 있는데, 뒤에서 상세히 배워보도록 하겠습니다.
   
   2. 아래 코드스니펫을 복사한 뒤 주소창에 붙여 넣으면, DartPad에서 변수 자료를 확인할 수 있습니다.
      
      [[코드스니펫] DartPad 변수 학습](https://dartpad.dev/?id=d388c74a3fbfd492159b889419317044&null_safety=true)
      
      ![image](https://user-images.githubusercontent.com/55625864/152088558-6ac60f86-5208-4e34-80ef-066553718bd4.png)

2. 자료형
   
   :bulb: String 이외에도 다양한 자료형이 있습니다. 우측에 DartPad 링크를 클릭하여 어떻게 동작하는지 이해해 봅시다.
   
   <img src="https://user-images.githubusercontent.com/55625864/152088994-4ca8dac9-83a5-404c-823f-2a7ba8ec9c7d.png" title="" alt="image" width="555">
   
   :bulb: 각 자료형이 가진 내장된 기능 굉장히 많습니다. 이 기능들은 외울 필요 없이 필요할 때 검색하여 사용하시면 됩니다.
   
   내장함수 검색 방법
   ex) Dart String
   
   코드스니펫을 복사해 새 탭에서 열어주세요.
   
   - [**[코드스니펫] String 공식문서 링크**](https://api.dart.dev/stable/2.14.4/dart-core/String-class.html)
     
     ![image](https://user-images.githubusercontent.com/55625864/152089395-c8230ff8-c221-45ab-8e40-470f9d482e47.png)

3. 흐름 제어문
   
   :bulb:Dart 프로그램은 main 함수로 부터 시작되어 아래로 진행됩니다.
   프로그램의 실행되는 순서(흐름)를 제어하는 방법을 배워보도록 합시다.
   
   :bulb: if문이라고도 불리며 조건에 따라 실행하고 싶은 코드를 분기할 때 사용합니다.
   
   ```dart
   if (bool1) {
       // bool1이 **true**면 실행
   } else {
       // bool1이 **false**면 실행
   }
   ```
   
   :bulb: 조건문은 `else if` 형태로 계속해서 꼬리에 꼬리를 물 수 있습니다. 앞에서 부터 하나씩 비교해서 진행하면서 하나라도 **true**가 되어 실행되면, 뒤에 있는 조건문은 실행되지 않습니다.
   
   ```dart
   if (bool1) {
       // bool1이 **true**면 실행
   } else if (bool2) {
       // bool1이 **false**이고, bool2가 **true**이면 실행
   } else if (bool3) {
       // bool1과 bool2가 **false**이고, bool3가 **true**이면 실행
   } else {
       // bool1, bool2, bool3가 모두 **false**이면 실행
   }
   ```
   
   - AND와 OR 연산자
     💡 `&&`는 AND 연산자라 불립니다. `bool1 && bool2`와 같이 좌우에 bool 값이 오는데, 두 값이 모두 `true` 일 때 전체 값을 `true`로 반환 합니다.
     💡 `||`는 OR 연산자라 불립니다. `bool1 || bool2`와 같이 좌우에 bool 값이 오는데, 둘 중 하나라도 `true` 라면 전체 값을 `true`로 반환합니다.

4. :bulb: 반복문은 특정한 코드를 반복해서 실행하도록 흐름을 제어하는 방법으로 `for문` 이라고 불리기도 합니다.
   
   - **[[코드스니펫] DartPad 반복문 학습](https://dartpad.dev/?id=e6c465cfb15da2ee31453d683ae54529&null_safety=true)**
     
     ```jsx
     <https://dartpad.dev/?id=e6c465cfb15da2ee31453d683ae54529&null_safety=true>
     ```
   
   :bulb: 직접 입력하면 5줄을 작성해야 하지만,
   
   ```dart
   hello 1
   hello 2
   hello 3
   hello 4
   hello 5
   ```
   
   반복문을 사용하면 3줄로 작성할 수 있습니다.
   
   ```dart
   for (int i = 0; i < 5; i++) {
       print('hello ${i + 1}');
   }
   ```
   
   5줄이 아니라 100만줄이 되어도, 반복문을 사용하면 3줄만에 가능합니다 👍👍
   
   - 반복문 구성
     
     1 : `int i = 0` → `i`라는 변수가 0으로 시작합니다. (한 번만 실행됩니다)
     
     2 : `i < 5` → `i`의 값이 5보다 작은지 조건을 확인합니다. (false → 반복문 종료 / true → 3번)
     
     3 : `중괄호 안쪽 영역` → 반복해 실행하는 코드들이 들어있습니다.
     
     4 : `i++` → `i`값을 1만큼 증가 시키고 2번으로 흐름이 다시 넘어갑니다.
   
   - 배열과 반복문
     
     :bulb: 반복문에 있는 `i`를 보면 0부터 5까지 1씩 증가합니다. 이를 배열에 원소를 꺼내는 index에 적용하면 배열의 모든 원소를 손쉽게 꺼낼 수 있습니다.
     
     - **[[코드스니펫] DartPad 배열과 반복문 학습](https://dartpad.dev/?id=bae349ac364c19fb6b237132ec4d600e&null_safety=true)**
       
       ```jsx
       <https://dartpad.dev/?id=bae349ac364c19fb6b237132ec4d600e&null_safety=true>
       ```

5. 함수
   
   :bulb:함수(function)는 여러 코드를 묶어둔 상자입니다.

6. 클래스(class)
   
   :bulb: 클래스는 변수와 함수를 모아둔 틀입니다.
   
   






