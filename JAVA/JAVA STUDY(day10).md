## Day 10

== 

숫자나 문자는 등가 연산자로 값이 동일한지 비교 가능하지만

문자열은 등가 연산자로 비교할 수 있는 경우도 있지만 일반적으로 API를 사용해야 한다.



equals() 메서드를 사용해야 한다.

String 클래스가 제공



자바는 문자열 리터럴은 String 객체로 취급된다.

* 'y' - 문자형
  * :char 타입, 기본형
*  "y" - 문자열형
  * :String 타입, 객체형(참조형)
  * "y".equals("....") 처럼 .을 붙여서 각종 연산자로 사용할 수 있다.

#### abstract

- 미완성 클래스라서 상속만 가능 하고 객체 생성은 할 수 없다.
- It should be overriding 
- abstract method가



#### 다형성

다형성, 추상클래스(abstract class), 인터페이스, 예외처리

**[다형성]**

참조형 변수(클래스 타입)는 타입에 지정된 클래스 객체뿐만 아니라 타입에 지정된 클래스의 자손의 객체도 참조할 수 있다.

```java
A obj;
object = new A();
object = new B();
object = new C();
```

어떤 클래스의 변수이느냐에 따라서 ! 

```java
void 메서드 (A ojb){
}

Object o = new Date(); // 오브젝트가 갖고 있는 멤버까지만 접근 가능! 
						// ELSE, impossible 
						// 추가된 아이들한테는 접근 불가
Date d= new Date();
Member m = new DATA(); (X)
```

### day 10 실습 1

```java
package day10;

abstract class Mobile {// 상속으로만 활용할 수 있는 클래스!! abstrat class
	private String mobileName;
	private int batterySize;
	private String osType;

	public Mobile() {
	}

	public Mobile(String mobileName, int batterySize, String osType) {
		this.mobileName = mobileName;
		this.batterySize = batterySize;
		this.osType = osType;
	}

	abstract public void opearte(int time);
	abstract public void charge(int time);

	// 밑 부분 혼자 구현해보기
	public String getMobileName() {
		return this.mobileName;
	}
	public void setMobileName(String mobileName) {
		this.mobileName = mobileName;
	}
	public int getBatterySize() {
		return this.batterySize;
	}
	public void setBatterySize(int batterySize) {
		this.batterySize = batterySize;
	}
	public String getOsType() {
		return this.osType;
	}
	public void setOsType(String osType) {
		this.osType = osType;
	}
}

class Ltab extends Mobile {

	public Ltab() {
	}

	public Ltab(String mobileName, int batterySize, String osType) {
		super(mobileName, batterySize, osType);
	}

	public void operate(int time) { // 이 부분 다시 코딩해보기
		setBatterySize(getBatterySize() - 10*time);
	}

	public void charge(int time) {
		setBatterySize(getBatterySize() + 10*time);
	}

}

class Otab extends Mobile {
	public Otab() {
	}

	public Otab(String mobileName, int batterySize, String osType) {

	}

	public void operate(int time) { // 이 부분 다시 코딩해보기
		setBatterySize(getBatterySize() - 12*time);
	}

	public void charge(int time) {
		setBatterySize(getBatterySize() + 12*time);
	}


public class MobileTest {

   public static void main(String[] args) {
      Mobile mobile = new Ltab("Ltab", 500, "ABC-01");
      Mobile mobile2 = new Otab("Otab", 1000, "ABC-20");
      printTitle();
      printMobile(mobile);
      printMobile(mobile2);
      
      mobile.charge(10);
      mobile2.charge(10);
      System.out.println("[ 10분 충전 ]");   
      printTitle();
      printMobile(mobile);
      printMobile(mobile2);
      System.out.println("[ 5분 통화 ]");
      printTitle();
      mobile.operate(5);
      mobile2.operate(5);
      printMobile(mobile);
      printMobile(mobile2);
   }
   
    public static void printMobile(Mobile mobile) {
       System.out.println(mobile.getMobileName() + "\t\t" + mobile.getBattery() + "\t\t" + mobile.getOsType());
    }
    public static void printTitle() {
       System.out.printf("Mobile\t\tBattery\t\tOS\n");
       System.out.printf("---------------------------------------\n");
    }


}
```

overriding 



super.setFuelSize(super.getFuelSize()-(distance*30));