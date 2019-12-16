# Day8

- **실습1 문제**

[클래스 정의와 객체 생성 실습 4]

```java
// SalaryExpr
- bonus : int 
---------------
SalaryExpr()
SalaryExpr(bonus : int)
getSalary(grade : int): int
// SaleryExam
+main(String[]) : void
---------------
SalaryExpr() - 멤버변수 bonus 에 0 을 할당한다.
SalaryExpr(int bonus) 멤버변수에 매개변수 bonus 값을 할당한다.
getSalary(int grade) : int
    grade 의 값이 1 이면 
    멤버 변수 bonus 에 100 더한 후 이 값을 리턴. 
    grade 의 값이 2 이면 
    멤버 변수 bonus 에 90 더한 후 이 값을 리턴.
    grade 의 값이 3 이면 
    멤버 변수 bonus 에 80 더한 후 이 값을 리턴.
    grade 의 값이 4 이면 
    멤버 변수 bonus 에 70 더한 후 이 값을 리턴.
main()
    1~12의 난수, 1~4의 난수를 추출하여 각각
	month 변수와 grade 변수에 저장한다.
	month : 월 정보
    (짝수달 : 보너스 달, 홀수달 : 보너스달이 아님)
    grade : 등급(1-4)
    보너스 달이면 
    SalaryExpr(100) 를 가지고 SalaryExpr의 인스턴스를 생성하여 grade 값을 전달하면서 getSalary() 	를 호출한 결과 값을 화면에 표준 출력한다. (등급 관계없이 보너스 금액은 100 으로 설정한다.) 
    보너스 달이 아니면 
    SalaryExpr() 를 가지고 SalaryExpr의 인스턴스를 생성하여 grade 값을 전달하면서 getSalary() 를 		호출한 결과를 화면에 표준 출력한다. 
    - 출력 형식 : “..... 월 ..... 등급의 월급은 ..... 입니다.” 
```

```java
//실습1 SaleryExam
import day6.MethodLab3;
class SalaryExpr{
	int bonus;
	SalaryExpr(){
		bonus = 0;
	}
	SalaryExpr(int bonus){
		this.bonus = bonus;
	}
	int getSalary(int grade){
		int salary = 0;
		if(grade == 1) salary += 100;
		else if(grade == 2) salary += 90;
		else if(grade == 3) salary += 80;
		else salary += 70;
		
		return salary;
        // -----others-----
        // salary = 100;
        // return salary - (grade -1) * 10;
	}
}
public class SaleryExam {
	public static void main(String[] args) {
		int month = MethodLab3.getRandom(1, 12);
		int grade = MethodLab3.getRandom(1, 4);
		SalaryExpr salaryExpr = null;
		if(month % 2 == 0) {
			salaryExpr = new SalaryExpr(100);
		}
		else {
			salaryExpr = new SalaryExpr();
		}
		System.out.println(month + "월 " + grade + "등급의 " + "월급은 " + salaryExpr.getSalary(grade) + "입니다.");
	}
}
```

```java
[방법1]
import dy6.MethodLab3;
class 클래스명{
    main() 메서드 헤더{
        int month = MethodLab3.getRandom(12);
    }
}
[방법2]
class 클래스명{
    main() 메서드 헤더{
        int month = day6.MethodLab3.getRandom(12);
    }
}
```

## static(정적, 고정)

- 제어자

- 멤버변수와 메서드 앞에 지정 가능하다.

- static을 설정한 멤버변수와 메서드는 객체생성을 하지 않아도 자동으로

  메모리 영역을 할당 하거나 호출 가능한 상태가 된다.

- 다른 클래스에서 또 다른 클래스의 static 타입의 멤버를 사용할 때는

  클래스명.멤버명 으로 사용한다.

- 클래스에 정의되는 멤버들중 어떤 멤버에 static 부여 하는가?

  변수(멤버)

  메서드

- **상수(final) vs 정적(static)**

  상수는 값을 변경하지 못하고 정적 변수는 메모리 영역이 고정이다.

- Loading 만해서 main 메소드를 사용할 수 있어야 하기 때문에

  main 메소드에서는 static을 사용한다.

```java
// 실습2 CardTest
public class Card{	
	String kind ;			        // 카드의 무늬 - 인스턴스 변수
	int number;			            // 카드의 숫자 - 인스턴스 변수
	static int width = 100;			// 카드의 폭   - 클래스 변수
	static int height = 250;		// 카드의 높이 - 클래스 변수
}
```

```java
// 실습2 CardTest
public class CardTest{
	public static void main(String args[]) throws Exception{	
		System.out.println("CardTest 수행이 시작었습니다.");
		Thread.sleep(10000); // ms
		Card c1 = new Card();		
		c1.kind = "Heart";
		c1.number = 7;	
		System.out.println("첫 번째 Card 객체가 생성됨");
		Thread.sleep(10000);
		Card c2 = new Card();		
		c2.kind = "Spade";
		c2.number = 4;
		System.out.println("두 번째 Card 객체가 생성됨");
		Thread.sleep(5000);
		System.out.println("c1은 " + c1.kind + ", " + c1.number 
				+ "이며, 크기는 (" + Card.width + ", " + Card.height + ")");
		System.out.println("c2는 " + c2.kind + ", " + c2.number
				+ "이며, 크기는 (" + Card.width + ", " + Card.height + ")");	
		Card.width = 50;
		Card.height = 80;
		System.out.println("c1은 " + c1.kind + ", " + c1.number 
				+ "이며, 크기는 (" + Card.width + ", " + Card.height + ")" );
		System.out.println("c2는 " + c2.kind + ", " + c2.number 
				+ "이며, 크기는 (" + Card.width + ", " + Card.height + ")" );
	}
}
```

-> Run Configurations

-> Arguments

-> VM arguments

-> **verbose:class** - JVM 옵션

​	클래스 로딩 정보를 보여주면서 자바 프로그램을 수행시켜라!!

​	자바는 동적 로딩한다. 필요할 때마다 로딩한다.

--------------------------

### 선언의  위치에 따른 변수의 종류

변수의 타입은 변수에 저장할 값의 종류에 따라 결정된다.

변수의 선언위치에 따른 종류가 또 있다.

변수가 어디에 선언되었는가에 따라 변수의 종류와 범위가 결정된다.

여기서 범위라는 것은 변수가 유효한 범위, 즉 변수를 사용할 수 있는 범위를 말한다.

변수의 선언위치에 따라 결정되는 변수의 종류는 세가지, 클래스변수, 인스턴스변수, 지역변수입니다.

클래스 영역은 클래스 블럭~~ 여기부터 여기까지를 의미한다.

**이 영역에 선언되면 인스턴스변수가 됩니다. 여기에 키워드 static을 붙이면 클래스변수가 된다.**

**인스턴스 변수와 클래스 변수는 클래스의 구성요소, 즉 멤버라서 멤버변수라고 한다.**

**그만큼 클래스 내에서 광범위하게 사용되는 중요한 변수들이라 할 수 있다.**

**그리고 메서드영역에 선언되면 지역변수가 된다.. 메서드 영역은 메서드의 블럭의 시작과 끝...**

**변수가 클래스영역에 선언되지 않았다면, 모두 지역변수라고 보면 된다.**

**즉, 클래스변수와 인스턴스변수가 아니라면 모두 지역변수이다.**

**그리고 지역변수에는 static을 붙일 수 없다.**

**클래스변수는 클래스가 메모리에 올라갈때 자동적으로 생성된다.**

그래서... 원하는 때면 언제든지 바로 사용가능합니다. 인스턴스를 생성하지 않고도 사용할 수 있다.

반면에 인스턴스변수는 인스턴스를 생성해야 만들어지므로 사용하기 전에 반드시 인스턴스를 생성해야합니다.

마지막으로 지역변수는 메서드가 호출되어 해당하는 변수선언문이 수행될 때 만들어집니다.

-----------------------------

### 블록 스코프

```java
메서드 헤더 {
    int a;
    // int b;
    if( .... ){
        int b;
          :
    }
    
    int c;
    int b;
}
```

### 메서드(method)

▶ 메서드란?

- 작업을 수행하기 위한 명령문의 집합

- 어떤 값을 입력받아서 처리하고 그 결과를 돌려준다. 

   (입력받는 값이 없을 수도 있고 결과를 돌려주지 않을 수도 있다.)

▶ 메서드의 장점과 작성지침

- 반복적인 코드를 줄이고 코드의 관리가 용이하다.
- 반복적으로 수행되는 여러 문장을 메서드로 작성한다.
- 하나의 메서드는 한 가지 기능만 수행하도록 작성하는 것이 좋다.
- 관련된 여러 문장을 메서드로 작성한다.
- 반환값이 있는 메서드는 모든 경우에 return문이 있어야 한다.
- return문의 개수는 최소화하는 것이 좋다.

#### 클래스 메서드(static 메서드)와 인스턴스 메서드

- 인스턴스 메서드
  - 인스턴스 생성 후, ‘참조변수.메서드이름()’으로 호출
  - 인스턴스변수나 인스턴스메서드와 관련된 작업을 하는 메서드
  - 메서드 내에서 인스턴스변수 사용가능
- 클래스메서드(static메서드)
  - 객체생성없이 ‘클래스이름.메서드이름()’으로 호출
  - 인스턴스변수나 인스턴스메서드와 관련없는 작업을 하는 메서드
  - 메서드 내에서 인스턴스변수 사용불가
  - 메서드 내에서 인스턴스변수를 사용하지 않는다면 static을 붙이는 것을 고려한다.

```java
class MyMath2 {
	long a, b;
	
	long add() {	// 인스턴스메서드
		return a + b;
	}

	static long add(long a, long b) { // 클래스메서드(static메서드)
		return a + b;
	}
}
```

```java
class MyMathTest2 {
	public static void main(String args[]) {
		System.out.println(MyMath2.add(200L,100L); // 클래스메서드 호출
		MyMath2 mm = new MyMath2(); // 인스턴스 생성
		mm.a = 200L;
		mm.b = 100L;
		System.out.println(mm.add()); // 인스턴스메서드 호출
	}
}
```

--------------------

### JVM 메모리 구조

#### 메서드 영역(Method Area)

클래스 정보와 클래스변수가 저장되는 곳

#### 호출스택(Call Stack)

메서드의 작업공간. 메서드가 호출되면 메서드 수행에 필요한 메모리공간을 할당받고 메서드가 종료되면 사용하던 메모리를 반환한다.

- 호출 스택의 특징

메서드가 호출되면 수행에 필요한 메모리를 스택에 할당받는다.

메서드가 수행을 마치면 사용했던 메모리를 반환한다.

호출스택의 제일 위에 있는 메서드가 현재 실행중인 메서드다.

아래에 있는 메서드가 바로 위의 메서드를 호출한 메서드다.	

#### 힙(Heap)

인스턴스가 생성되는 공간. new연산자에 의해서 생성되는 배열과 객체는 모두 여기에 생성된다.

----------------

## 표준입력(Standard Input)

- 프로그램이 수행하는 동안 필요로 하는 데이터를 시스템(컴퓨터)의 표준 입력 장치로 부터 받아오는 것

  표준 입력 장치 - 키보드

- java에서는 표준 입력을 어떻게 처리 하느냐...

  **System.in**

  **System.in.read();** -> 단점 : 한글을 깨뜨린다. 다른 API  도움을 받아야한다.

  ​												무조건 문자로만 입력 받아야한다.

- Java 5(JDK 1.5)

  java.util.Scanner 클래스를 제공하여 좀더 편하게 데이터 입력받을 수 있게 API를 추가했다.

  **Scanner scan = new Scanner(System.in);**

  scan.next() - retrun type은 String

  scan.nextLine() - 하나의 행을 읽어온다.

  scan.nextInt()

  scan.nextDouble()

  ​				:

- Scanner는 외부 입력 장치를 사용하기 때문에 **sc.close();** 더이상 쓰지 않을 때는 닫아야 좀더 효율적으로 사용할수있다.

- **실습3 String Input**

```java
//실습3 ScannerTest1
import java.util.Scanner;
public class ScannerTest1 {
	public static void main(String[] args) {
		System.out.print("입력 : ");
		Scanner sc = new Scanner(System.in);
		String a,b,c,d;
		a = sc.next();
		b = sc.next();
		c = sc.next();
		d = sc.next();
		System.out.println("a = [" + a + "]");
		System.out.println("b = [" + b+ "]");
		System.out.println("c = [" + c+ "]");
		System.out.println("d = [" + d+ "]");	
		sc.close();
	}
}
```

- **실습4 String 한행 전체 Input**

```java
//실습4 ScannerTest2
import java.util.Scanner;
public class ScannerTest2 {
	public static void main(String[] args) {
		System.out.print("입력 : ");
		Scanner sc = new Scanner(System.in);
		String a,b,c,d;
		a = sc.nextLine();
		b = sc.nextLine();
		c = sc.nextLine();
		d = sc.nextLine();
		System.out.println("a = [" + a + "]");
		System.out.println("b = [" + b+ "]");
		System.out.println("c = [" + c+ "]");
		System.out.println("d = [" + d+ "]");	
		sc.close();
	}
}
```

- **실습5 int 및 double Input**

```java
//실습5 ScannerTest3
import java.util.Scanner;
public class ScannerTest3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("두 개의 숫자(정수)를 입력해 주세요 : ");
		int number1 = sc.nextInt();
		int number2 = sc.nextInt();
		System.out.printf("합 : %d%n", number1 + number2);// \n
		System.out.print("두 개의 숫자(실수)를 입력해 주세요 : ");
		double number3 = sc.nextDouble();
		double number4 = sc.nextDouble();
		System.out.printf("합 : %.2f%n", number3 + number4);
		sc.close();
	}
}
```

- **실습6 next vs nextln**

  - Test Example

    ```java
    1.
    aa
    bb
    cc     
        sc.nextLine();을 주석 했을 때의 상태
        ------> aa\nbb\ncc\n  : 왼쪽에서 2두번째 \n를 nextln이 읽는다.
                  				next는 필요한것만 읽어가고
        						nextln은 필요한것 + \n까지 모두 읽어간다.
        그래서 여기서 출력을 확인하면 3번째 입력에서 \n을 읽게된다.
        
    2.
    aa bb       cc     dd
    ```

    

```java
//실습6 ScannerTest4
import java.util.Scanner;
public class ScannerTest4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.printf("데이터를 입력하세요 : ");
		String str1 = sc.next();
		String str2 = sc.next();
		sc.nextLine();  // 입력버퍼에 남아있는 개행문자를 청소하는 기능
		String line1 = sc.nextLine();
		String line2 = sc.nextLine();
		System.out.printf("[%s] [%s] [%s] [%s]", str1, str2, line1, line2);
		sc.close();
	}
}
```

- **실습7 문제**

1. 클래스명 : ScannerLab1 
2. 표준입력으로 숫자 두 개와 연산자 문자 한 개를 입력받아서
    각각 변수에 저장한다.
    첫 번째 숫자를 입력하세요 :
    두 번째 숫자를 입력하세요 :
    연산자(+, -, *, /)를 입력하세요 :
    nextInt(), nextInt(), next()
    nextLine() -> 숫자 입력시 다시 숫자로 변환하는 작업 필요
                        int Integer.parseInt(String)
3. switch 문 사용
    입력된 연산자가 "+" 이면 입력된 두 개 숫자의 덧셈을 처리한다.
    입력된 연산자가 "-" 이면 입력된 두 개 숫자의 뺄셈을 처리한다.
    입력된 연산자가 "/" 이면 입력된 두 개 숫자의 나눗셈을 처리한다.
    입력된 연산자가 "*" 이면 입력된 두 개 숫자의 곱셈을 처리한다.
4. 결과는 다음과 같이 출력한다.
   
    XX 와 YY의 X 연산 결과는 ZZ 입니다.

```java
//실습7 ScannerLab1
import 	java.util.Scanner;
public class ScannerLab1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1, num2;
		int result = 0;
		String op;
		boolean flag = false;
		
		System.out.print("첫 번째 숫자를 입력하세요 : ");
		num1 = sc.nextInt();
		System.out.print("두 번째 숫자를 입력하세요 : ");
		num2 = sc.nextInt();
		System.out.print("연산자(+, -, *, /)를 입력하세요 : ");
		op = sc.next();
		
		switch(op) {
		case "+":
			result = num1 + num2;
			break;
		case "-":
			result = num1 - num2;
			break;
		case "/":
			result = num1 / num2;
			break;
		case "*":
			result = num1 * num2;
			break;
		default :
			flag = true;
		}
		
		if(flag == true) {
			System.out.println("+, -, *, / 를 입력하숑");
		}
		else {
			System.out.println(num1 + "와 " + num2 + "의 " + op + " 연산 결과는 " + result + "입니다.");
		}
        sc.close();
	}
}
```

**문자열 비교는 등가로 안된다!**

만약 쓴다면

```java
if (op.equals("+") || op == "-" || op == "*" || op == "/"){
}
else{
}
```

- **실습8 class Parent & Child**

```java
//실습8 ParentChildTest
// java.lang.Object가 최상위 클래스
class Parent{	// java.lang.Object 가 자동으로 부모가 된다.
	int x = 1, y = 2;
	public String toString() {
		return "Parent 클래스의 객체 입니당";
	}
}


// Parent의 상속된 모든 클래스를 사용할수 있다.
class Child extends Parent{
	int x = 10;
	void printInfo() {
		int x = 100;
		System.out.println(x);			// 100
		System.out.println(this.x);		// 10
		System.out.println(super.x);	// 1
		System.out.println(y);			// 2
		System.out.println(this.y);		// 2
		System.out.println(super.y);	// 2
//		System.out.println(z);
	}
	public String toString() {
		return "Child 클래스의 객체 입니당";
	}
}

public class ParentChildTest {
	public static void main(String[] args) {
		Parent p = new Parent();
		System.out.println(p.toString());
		System.out.println(p);
		System.out.println("출력1" + p);
		Card c = new Card();
		System.out.println(c.toString());
		System.out.println("출력2" + c);
		java.util.Date d = new java.util.Date();
		System.out.println(d.toString());
		System.out.println("출력 3" + d);
		Child ch = new Child();
		// Parent를 상속할 때와 안할 때의 출력값이 달라진다.
		// toString 메서드를 추가하면 Child내의 메서드를 오버로딩하여 출력한다.
		System.out.println("출력 4" + ch);
		ch.printInfo();
	}
}

```

