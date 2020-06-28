# Java 8

- https://altongmon.tistory.com/245

  자바 8부터 빈번하게 사용되는 함수적 인터페이스는 java.util.function 표준 API패키지로 제공합니다. 

  이 패키지에서 제공하는 함수적 인터페이스의 목적은  

  메서드 또는 생성자의 매개 타입으로 사용되어 람다식을 대입할 수 있도록 하기 위함 입니다. 

  자바 8부터 추가되었거나 변경된 API에서 이 함수적 인터페이스들을 매개 타입으로 많이 사용합니다. 

  물론 자체적으로 개발하는 메서드에도 이 함수적 인터페이스들을 매객 타입으로 사용할 수 있습니다.

   java.util.function 패키지의 함수적 인터페이스는 

  크게 Consumer, Supplier, Function, Operator, Predicate로 구분됩니다. 

  구분 기준은 인터페이스에 선언된 추상 메서드의 매개값과 리턴값의 유무입니다.

  ![image](https://user-images.githubusercontent.com/55625864/85914611-77951000-b87a-11ea-938c-a99344917621.png)

### Supplier

매개 변수는 없고 리턴값이 있는 getXXX()를 가지고 있고

이 메소드들은 실행 후 호촐한 곳으로 데이터를 공급(리턴)하는 역할을 함.

![image](https://user-images.githubusercontent.com/55625864/85914494-45cf7980-b879-11ea-9852-d997337a6fef.png)

```java
import java.util.function.IntSupplier;

public class SupplierExample  {

    public static void main(String[] args) {

        IntSupplier is = () -> {

            int a = (int) (Math.random()*6)+1;
            return a;
        };

        int aa = is.getAsInt();
        System.out.print(aa);

    }
}
```



출처: https://altongmon.tistory.com/245 [IOS를 Java]

