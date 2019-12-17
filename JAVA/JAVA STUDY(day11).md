# Day11

---------

## 인터페이스

- 클래스, final 클래스, abstract 클래스

- 인터페이스는 모든 메서드가 abstract 메서드만 클래스를 의미한다.

- 자바는 단일 상속을 지원하는 OOP 언어이다.

  모든 메서드가 abstract인 클래스를 상속한 경우 다른 클래스는 상속이 불가하다.

  ----> **인터페이스는 추가 상속이 가능한 특별한 형태의 클래스이다.**

- 인터페이스는 abstract 클래스와 비슷한 자바 프로그램의 구조로서

  객체 생성은 불가하고 상속으로만 사용이 가능하다.

- 모든 멤버변수는 public static final 이어야 하며, 이를 생략할 수 있다.

- 모든 메서드는 public abstract 이어야하며 이를 생략할 수 있다.

  ```java
  interfaace 인터페이스이름{
      public static final 타입 상수이름 = 값;
      public abstract 메서드이름(매개변수목록);
  }
  ```

  ```java
  interface PlayingCard{
      public static final int SPADE = 4;
      final int DIAMOND = 3; 		// public static final int DIAMOND = 3;
      static int HEART = 2;		// public static final int HEART = 2;
      int CLOVER = 1;				// public static finl int CLOVER = 1;
      
      public abstract String getcardNumber();
      String getCardKind();		// public abstract String getCarKind();
  }
  ```

- 인터페이스 생성 방법

  ```java
  interface 인터페이스이름 {
  		상수 						// 일반 변수는 올수 없다.
  		abstract 메서드		//만 가능 (일단은!)
  }
  ```

- 인터페이스 사용 방법 : 상속

  ```java
  interface 인터페이스이름 extends 부모인터페이스이름 {
  }
  class 클래스명 extends 부모클래스명 implenments 부모인터페이스이름{
  }
  ```

- 실습1 TVUser

```java
package day11.case1;
public class LgTV {
	public void turnOn(){
		System.out.println("LgTV --- 전원을 켠다.");
	}
	public void turnOff(){
		System.out.println("LgTV --- 전원을 끈다.");
	}
	public void soundUp(){
		System.out.println("LgTV --- 소리를 높인다.");
	}
	public void soundDown(){
		System.out.println("LgTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case1;
public class SamsungTV {
	public void powerOn(){
		System.out.println("SamsungTV --- 전원을 켠다.");
	}
	public void powerOff(){
		System.out.println("SamsungTV --- 전원을 끈다.");
	}
	public void volumnUp(){
		System.out.println("SamsungTV --- 소리를 높인다.");
	}
	public void volumnDown(){
		System.out.println("SamsungTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case1;
public class TVUser {
	public static void main(String[] args) {
		SamsungTV tv = new SamsungTV();
		tv.powerOn();
		tv.volumnUp();
		tv.volumnDown();
		tv.powerOff();
	}
}
```

- 실습2 TVUser

```java
package day11.case2;
public class LgTV implements TV {
	public void powerOn(){
		System.out.println("LgTV --- 전원을 켠다.");
	}
	public void powerOff(){
		System.out.println("LgTV --- 전원을 끈다.");
	}
	public void volumnUp(){
		System.out.println("LgTV --- 소리를 높인다.");
	}
	public void volumnDown(){
		System.out.println("LgTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case2;
public class SamsungTV implements TV{
	public void powerOn(){
		System.out.println("SamsungTV --- 전원을 켠다.");
	}
	public void powerOff(){
		System.out.println("SamsungTV --- 전원을 끈다.");
	}
	public void volumnUp(){
		System.out.println("SamsungTV --- 소리를 높인다.");
	}
	public void volumnDown(){
		System.out.println("SamsungTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case2;
public interface TV {
	// abstract 자동으로!!
	public void powerOn();
	public void powerOff();
	public void volumnUp();
	public void volumnDown();
}
```

```java
package day11.case2;
public class TVUser {
	public static void main(String[] args) {
		TV tv = new LgTV();
		tv.powerOn();
		tv.volumnUp();
		tv.volumnDown();
		tv.powerOff();
	}
}
```

- 실습3 TVUser

```java
package day11.case3;
public class LgTV implements TV {
	public void powerOn(){
		System.out.println("LgTV --- 전원을 켠다.");
	}
	public void powerOff(){
		System.out.println("LgTV --- 전원을 끈다.");
	}
	public void volumnUp(){
		System.out.println("LgTV --- 소리를 높인다.");
	}
	public void volumnDown(){
		System.out.println("LgTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case3;
public class SamsungTV implements TV{
	public void powerOn(){
		System.out.println("SamsungTV --- 전원을 켠다.");
	}
	public void powerOff(){
		System.out.println("SamsungTV --- 전원을 끈다.");
	}
	public void volumnUp(){
		System.out.println("SamsungTV --- 소리를 높인다.");
	}
	public void volumnDown(){
		System.out.println("SamsungTV --- 소리를 낮춘다.");
	}
}
```

```java
package day11.case3;
public interface TV {
	public void powerOn();
	public void powerOff();
	public void volumnUp();
	public void volumnDown();
}
```

```java
package day11.case3;
// 관례 적으로 ~~Factory라는 명이 있으면
// TV라는 객체를 대신 생성해 준다는 뜻이다.
public class TVFactory {
	// TV라는 인터페이스로 리턴타입을 맞추어 객체 return 
	public static TV getTV(String beanName){
		TV obj = null;
		if(beanName.equals("samsung")){
			obj = new SamsungTV();
		} else if(beanName.equals("lg")){
			obj = new LgTV();
		}
		return obj;
	}
}
```

```java
package day11.case3;
public class TVUser {
	public static void main(String[] args) {		
		TV tv = TVFactory.getTV(args[0]);
		if(tv != null) {
			tv.powerOn();
			tv.volumnUp();
			tv.volumnDown();
			tv.powerOff();
		} else {
			System.out.println("프로그램 아규먼트로 samsung 또는 lg 를 입력해 주세요..");
		}
	}
}
```

- 실습4 DrawableTest

```java
package day11;
import java.util.Random;
// interface 이름을 정할때 보통 일반적으로 ~able이라는 단어를 붙인다.
interface Drawable {
	// 자동으로 public abstract가 생성된다!!는 것을 기억하고 있어야한다.
	 void draw();
}
// abstract한다는것은 모조리 오버라이딩 한다는것과 다름없다.
abstract class Rect implements Drawable {
	public void draw() {
		System.out.println("사각형을 그립니다.");
	}
}
class Circle implements Drawable {
	public void draw() {
		System.out.println("원을 그립니다.");
	}
}
class Diamond implements Drawable  {
	public void draw() {
		System.out.println("마름모를 그립니다.");
	}
}
public class DrawableTest {
	public static void main(String[] args) {
		Random rand = new Random();
		int num = rand.nextInt(3);
		Drawable d = null;
		if(num == 0)
//			d = new Rect();
			d = () -> System.out.println("사각형을 그립니다.");
		else if(num == 1)
			d = new Circle();		
		else if(num == 2)
			d = new Diamond();		
		output(d);
	}
	public static void output(Drawable d){
		System.out.println("전달된 객체의 클래스명 : "+
	                        d.getClass().getName());
		d.draw();
	}
}
```

--------

## JDK API

**JDK 1.0 | JDK 1.1**

**8개       |   23개**

java.nnn		- 기본
		java-lang, java.uti., java.io, java.net, java.sql....
javax.nnn	  - 확장
		javax.sql, javax.nio....
----------> 자바언어에서만 지원하는 API
ogr.nnn		  - 
----------> 자바에서만 지원하지 않고 다른 프로그래밍 언어에서도 지원되는 API로
	  어떤 표준화 위원회나 조직에서 정한 API를 자바에도 지원하기
	  위해 만든 API

-------

## 오류처리

- 컴파일 오류 : 구문오류, API 사용 오류

- 실행 오류 : 에러 - JVM 영역에서 발생하는 오류로서 치명적이라

  ​							 JVM이 프로그램 실행을 중단시키고 callstack 정보를 화면에 출력한다.

  ​							 미리예측하고 대비하는 코드를 작성불가

  ​				   예외 - 자바 프로그램 영역에서 발생하는 실행 오류로 다소 가벼운 잘못된 상황

  ​							  런타임 예외 - 발생 원인이 프로그램 코드 - 버그 - 예외 처리 선택

  ​							  일반 예외 - 발생 원인이 외부적인 요인이다. - 예외 처리 필수

- 예외 처리 방법

  1. 적극적인 예외 처리

     ```java
     try{
     	예외가 발생할 수도 있는 코드
     }catch(처리해야하는 예외 클래스의 변수선언){
     	처리 코드
     } finally{
         예외 발생 여부와 관계없이 마지막에 수행을 보장하는 코드
     }
     ```

  2. 소극적인 예외 처리

     ```java
     메서드 헤더에 throws 처리해야하는 예외 클래스 '절을 추가'
     ```

  - 예외 발생

    ```java
    throw 발생시키고자하는예외클래스의객체
     throw new IOException(["예외메시지"])
    예외를 발생시키는 코드를 가지고 있는 메서드는 헤더 throws 절을 사용해서 이메서드는 호출시 예외가 발생할 수도 있다는 것을 알려야 한다.
    ```

- 실습5 ExceptionTest1

```java
package day11;
public class ExceptionTest1 {
	public static void main(String[] args) {
		System.out.println("수행시작");
		try { // try 블럭에서 예외가 발생하면 try 블럭 진행 안함
			int num1 = Integer.parseInt(args[0]);
			int num2 = Integer.parseInt(args[1]);
			int result = num1/num2;
			System.out.println("연산 결과 : " + result);
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("프로그램 아규먼트를 2개 전달하세요!!");
		} catch (ArithmeticException e) {
             e.
			System.out.println("두번째 프로그램 아규먼트는 0이 아닌 값을 전달하세요!!");
             return // return을 해도 finally는 반드시 수행을 한다!!
		} catch (NumberFormatException e) {
			System.out.println("프로그램 아규먼트로 숫자를 전달하세요!!");
		} finally {
			System.out.println("항상 수행!!");
		}
		System.out.println("수행종료");
	}
}
```

- 실습6 LottoMachine

```java
//실습6 LottoMachine
package day11;

import java.util.Random;

class DuplicateException extends Exception {
    DuplicateException() {
    super("중복된 로또 번호가 발생했습니다.");
    }
}
public class LottoMachine {
	private int nums[];
	// 6개의 원소를 갖는 int 타입의 배열을 생성하여 nums 변수에 저장한다.
	public LottoMachine() {
		this.nums = new int[6];
	}
	// 1-20 사이의 6 개 숫자를 추출하여 배열에 저장한다. (Random 클래스를 사용한다.)
	public void createLottoNums() {
		Random rand = new Random();
		for(int i = 0; i < 6; i++) {
			this.nums[i] = rand.nextInt(20) + 1;
		}
	}
	// 6개의 모든 숫자들이 유니크한지 채크하고 중복숫자가 발견되면 DuplicateException을 발생시킨다.(throw, throws)
	public void checkLottoNums() throws DuplicateException{
		boolean checkNum[] = new boolean[21];
		for(int i = 0; i < 6; i++) {

			if(!checkNum[this.nums[i]]) {
				checkNum[this.nums[i]] = true;				
			}
			else {
				throw new DuplicateException();
			}
		}
	}
	// nums 를 리턴한다.
	public int[] getNums() {
		return this.nums;
	}
}
```

```java
package day11;

public class LottoGame {

	public static void main(String[] args) {
//		1. LottoMachine의 객체를 생성한다. 
//		2. createLottoNums()를 호출하여 로또 번호들을 배열에 구성한다.
//		3. checkLottoNums()를 호출하고 
//		예외가 발생하지 않으면 getNums() 를 호출하여 로또 넘버들을 화면
//		에 출력(x, x, x, x, x, x)하고 예외가 발생하면 예외 메시지
//		(“중복된 로또 번호가 발생했습니다”)를 출력하고 종료한다.
		int arr[] = new int[6];
		LottoMachine lottoMachine = new LottoMachine();
		lottoMachine.createLottoNums();
		
		try {
			lottoMachine.checkLottoNums();			
		} catch(Exception e) {
			System.out.println(e.getMessage());
			return;
		}
		
		arr = lottoMachine.getNums();
		for(int i = 0; i < 6; i++) {
			System.out.print(arr[i] + " ");			
		}
		System.out.println();
	}
}
```

