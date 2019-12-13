# Day9

Scanner - next(), nextInt(), nextDouble(), nextLine()

readLine() : String

aaa bbb      ccc ddd\n

aaa\n
bbb\n
ccc\n
ddd\n

## 상속

- 자바의 모든 객체들은 상속이라는 객체지향언어의 특징을 지원한다.
- 자바에서 생성되는 모든 객체들은 기본적으로 java.lang.Object 이라는 객체를 상속하게 된다.
- 클래스 헤더에 exetends라는 절을 사용하는 부모 클래스를 설정하는데 하나의 부모 클래스만 설정 가능하다.
- 조상부터 물려받은 메서드들은 필요에 따라 대체할 수 있따. - 메서드 오버라이딩이라 한다.
- 어떤 클래스든 객체를 생성하면 해당 클래스만 메모리 할당하는 것이 아니라 조상 클래스들도 메모리 할당한다.

```java
//실습1 
package day9;

class A {
	A(){
		super(); // 자동으로 이미 생성 되어서 안넣는다.
				 // this method도 자동으로 생성 되어 안넣는다.
				 // 첫번째 줄에 this 호출 하면 super 안넣는다.
				 // 첫번째 줄에 super 호출 하면 this 안넣는다.
		System.out.println("A 클래스를 객체 생성합니다.");		
	}
}

class B extends A {
	B(int num){
		super(); // 자동으로 이미 생성 되어서 안넣는다.
				 // this method도 자동으로 생성 되어 안넣는다.
				 // 첫번째 줄에 this 호출 하면 super 안넣는다.
				 // 첫번째 줄에 super 호출 하면 this 안넣는다.
		System.out.println("B 클래스를 객체 생성합니다.");		
	}
}

class C extends B{
	C(){
		super(100); // 반드시 첫번째 줄에 써야 error가 나지 않는다.
		System.out.println("C 클래스를 객체 생성합니다.");		
	}
}

public class ABCTest {
	public static void main(String[] args) {
		new C();
	}
}
//----------------------------------------------------------------
만약 
class B extends A {
	B(int num){
		System.out.println("B 클래스를 객체 생성합니다.");		
	}
}

class C extends B{
	C(){
		System.out.println("C 클래스를 객체 생성합니다.");		
	}
}
// 이렇게 작성하면 C()생성자 error
// error 내용 : Implicit super constructor B() is undefined. Must explicitly invoke another constructor
// solution : -> C()생성자에 super(numTemp);를 사용한다.

```

- 자손클래스의 객체 생성시 생성자 메서드가 호출되면 바로 조상 클래스의 생성자도 호출된다. 내부적으로는 아규먼트 없는 생성자가 호출되는데 다른 생성자를 호출하려는 경우 super()라는 메서드를 사용한다.

- 객체를 참조하는 용도 : this, super -> 나의 멤버를 부르고 싶으면 this, 조상의 멤버를 부르고 싶으면 super

- 객체를 초기화하는 용도로 사용되는 생성자 메서드 호출에 : this(), super()

- this(), super() : 생성자 안에서만 호출 가능

- this, super : 객체 생성 시점에 초기화 된다. static, 메서드에서는 사용 불가하다.

  ​					non-static 메서드와 생성자 메서드에서만 사용 가능하다.

```java
public class PointTest {
	public static void main(String args[]) {
		Point3D p3 = new Point3D(1,2,3);	
		System.out.println(p3.getLocation());
	}
}
class Point {
	int x;	
	int y;
	Point(int x, int y) {		
		this.x = x;
		this.y = y;
	}
	String getLocation() {
		return "x :" + x + ", y :"+ y;
	}
}
class Point3D extends Point {
	int z;
	Point3D(int x, int y, int z) {
		super(x, y); // 생성자 아큐먼트 갯수가 다르면 super 호출은 필수다!
					 // 조상 멤버변수는 super을 호출하면된다.
		//this.x = x;
		//this.y = y;
		this.z = z;
	}
	String getLocation() {	// 오버라이딩
		return super.getLocation() + ", z :" + z;
		// getLocation()에 super를 빼면 재귀호출되면서 stack overflow난다.
		// super.getLocation : 조상에 있는 메서드
	}	
}
```

## 제어자 : modifier(수정자, 한정자, 제어자)

1. 접근 제어자

   public, protected, (default), private

2. 활용 제어자

   final, static, abstract, transient, synchronized

제어자란 클래스, 메서드, 변수앞에 설정되어 접근 가능 여부와 사용 방식을 제어하는 구문

```java
[제어자] class 클래스명 extends 부모클래스명{
    [제어자]멤버변수 선언
    [제어자]생성자 메서드 정의
    [제어자]메서드 정의
}
public final, abstract class 클래스명 extends 부모클래스명{
    모든 접근제어자, final, static 멤버변수 선언
    모든접근제어자 생성자 메서드 정의
    모든접근제어자, static final, abstract 메서드 정의
}
- 클래스에는 접근제어자를 두가지만 설정 가능 : public, (default)
    public이 설정된 클래스: 누구나
    (default) 클래스 : 동일 패키지내의 클래스
- final : 변경할 수 없는, 마지막의
  abstract : 반드시 변경해야 하는, 마지막 아닌, 미완성의
  final 클래스 : 상속 불가, 객체 생성 가능
  abstract 클래스 : 객체 생성 불가, 상속만 가능
- public - 누구나
  protected - 동일패키지 이거나 자손이면 접근 가능
  (default) - 동일 패키지
  private - 자손이든 객체 생성한 클래스든 접근 불가.
      	    멤버가 정의된 클래스 내에서만 사용 가능
      
  [클래스 설계시]
   + : public
   # : protected
   (), ~ : (default)
   - : private
       
- static, final 을 함께 지정하여 상수를 만든다.
  public class Math{
      public final static double PI = 3.14159;
  }
  Math.PI
  Integer.MAX_VALUE
- 메서드에
  final : 자손에 의해 오버라이딩이 불가능한 메서드를 정의
  abstract : 자손에 의해 반드시 오버라이딩 해야 하는 메서드를 정의
      		메서드의 헤더만 정의되고 바디가 없는 메서드
```

## 상속(inheritance)의 정의와 장점

### 1.1 상속(inheritance)의 정의와 장점

▶ 상속이란?

- 기존의 클래스를 재사용해서 새로운 클래스를 작성하는 것.
- 두 클래스를 조상과 자손으로 관계를 맺어주는 것.
- 자손은 조상의 모든 멤버를 상속받는다.(생성자, 초기화블럭 제외)
- 자손의 멤버개수는 조상보다 적을 수 없다.(같거나 많다.)

### 1.2 클래스간의 관계 – 상속관계(inheritance)



- 공통부분은 조상에서 관리하고 개별부분은 자손에서 관리한다.
- 조상의 변경은 자손에 영향을 미치지만, 자손의 변경은 조상에 아무런 영향을 미치지 않는다.

### 1.2 클래스간의 관계 – 포함관계(composite)

▶ 포함(composite)이란?

- 한 클래스의 멤버변수로 다른 클래스를 선언하는 것
- 작은 단위의 클래스를 먼저 만들고, 이 들을 조합해서 하나의 커다란 클래스를 만든다.

### 1.3 클래스간의 관계결정하기 – 상속 vs. 포함

- 가능한 한 많은 관계를 맺어주어 재사용성을 높이고 관리하기 쉽게 한다.

-  ‘is-a’와 ‘has-a’를 가지고 문장을 만들어 본다.

- 상속관계 - '~은 ~이다. (is-a)'

- 포함관계 - '~은 ~을 가지고 있다. (has-a)'

  e.g)  원(Circle)은 도형(Shape)이다.(A Circle is a Shape.) : 상속관계

  ​		원(Circle)은 점(Point)를 가지고 있다.(A Circle has a Point.) : 포함관계

### 1.4 단일상속(single inheritance)

- Java는 단일상속만을 허용한다.(C++은 다중상속 허용)
- 비중이 높은 클래스 하나만 상속관계로, 나머지는 포함관계로 한다.

### 1.5 Object클래스 – 모든 클래스의 최고조상

-  조상이 없는 클래스는 자동적으로 Object클래스를 상속받게 된다.

- 상속계층도의 최상위에는 Object클래스가 위치한다.

- 모든 클래스는 Object클래스에 정의된 11개의 메서드를 상속받는다.

  toString(), equals(Object obj), hashCode(), ...

```java
class TVCR extends TV, VCR { // 이와 같은 표현은 허용하지 않는다.
    
}
```

## 오버라이딩(overriding)

### 2.1 오버라이딩(overriding)이란?

“조상클래스로부터 상속받은 메서드의 내용을 상속받는 클래스에 맞게 변경하는 것을 오버라이딩이라고 한다.”

\* override - vt. ‘~위에 덮어쓰다(overwrite).’, ‘~에 우선하다.’

```java
class Point{
    int x;
    int y;
    
    String getLocation(){
        return "x :" + x + " , y : " + y;
    }
}

class Point3D extends Point{
    int z;
    String getLocation(){ // 오버라이딩
        return "x :" + x + " , y : " + y + ", z : " + z;
    }
}
```

- 오버로딩 - 기존에 없는 새로운 메서드를 정의하는 것(new)
- 오버라이딩(overriding) - 상속받은 메서드의 내용을 변경하는 것(change, modify)

- **실습2 문제**

[상속실습 1]

```java
class Person {
	private String name;
	Person(String name) {
		this.name = name;
	}
	public String getInfo() {
		return name;
	}
}
```

Person 클래스를 상속하여 Friend 라는 클래스를 다음과 같은 사양으로 구현한다.

```java
//Person
- name : String
--------------------
Person(String)
+ getInfo() : String
//-----------------------------
//Friend
- phoneNum : String
- email : String
----------------------------
Friend(String,String,String)
+getInfo():String  -> “이름    핸폰번호     이메일주소” 형식으로 리턴
//-----------------------------
//FriendTest
+ main(String args[]) : void
    
public class FriendTest {
    public static void main(String args[]) {
         // Friend 클래스 타입의 배열을 생성한다. (원소 5 개)   Friend 타입의 객체들을 저장
         // 5개의 Friend 객체를 생성한다. (객체 생성시 입력되는 정보는 임의로 정한다.)
         // 각 Firend 객체의 정보를 getInfo() 라는 메서드를 호출하여 실행 결과 예와 같이 출력 한다. 
    }
}
//실행 결과 예
이름    	  전화번호	메일주소
--------------------------------------------------
XXX	  XXXXXXXX	XXX@XXXXXX
```

```java
//[solution]
//실습2 FriendTest
class Person {
	private String name;

	Person(String name) {
		this.name = name;
	}

	public String getInfo() {
		return name;
	}
}

class Friend extends Person {
	private String phoneNum;
	private String email;

	Friend(String name, String phoneNum, String emailAddr) {
		super(name);
		this.phoneNum = phoneNum;
		this.email = emailAddr;
	}

	public String getInfo() {
		String full = super.getInfo() + " " + this.phoneNum + " " + this.email;
		return full;
	}
}

public class FriendTest {
	public static void main(String[] args) {
		Friend friend[] = new Friend[5];
		friend[0] = new Friend("arog\t", "010-1234-9876\t", "email1@gmail.com");
		friend[1] = new Friend("brog\t", "010-1464-9676\t", "email2@gmail.com");
		friend[2] = new Friend("crog\t", "010-1298-4676\t", "email3@gmail.com");
		friend[3] = new Friend("drog\t", "010-1434-9076\t", "email4@gmail.com");
		friend[4] = new Friend("erogg\t", "010-1464-9812\t", "email5@gmail.com");

		System.out.println("이름\t" + "전화번호\t\t" + "메일주소");
		System.out.println("-----------------------------------------");
		for (int i = 0; i < 5; i++) {
			System.out.println(friend[i].getInfo());
		}
		
         // test
		//String ss = String.format("%-20s%-20s\n", "aaa", "bbb");
		//System.out.println(ss);
	}
}
```

- **실습3 GuGuDan 문제**

다음과 같은 내용으로 Multiplication 클래스가 있다.

```java
class Multiplication {
	private int dan;
	private int number;
	Multiplication() {}
	Multiplication(int dan) {
		this.dan = dan;
	}
	Multiplication(int dan, int number){
		this.dan = dan;
		this.number = number;
	}
	void printPart() {
		if (number == 0) {	       
			for(int n=1; n <= 9; n++)
				System.out.print("\t"+dan + "*" + n+ "="+dan*n);
			System.out.println();
		} else {
			System.out.println(dan * number);
		}
	}
}
```

1. 상속 구문을 적용하여 GuGuDanExpr 클래스를 구현한다.
   - Multiplication 클래스를 상속한다.
   - GuGuDanExpr 클래스의 생성자 사양

```java
GuGuDanExpr()
GuGuDanExpr(int dan)
GuGuDanExpr(int dan, int number)
```

- GuGuDanExpr 클래스의 메서드 사양

```java
static void printAll()
```

다음에 제시된 출력 방식으로 1단부터 9단까지 모두 출력

2. 다음에 제시된 내용을 수행하는 메인 클래스 GuGuDan 을 구현한다.

1부터 20사이의 난수를 2개를 추출하여 각각 dan 변수와 number 변수에 담는다. 

(1) dan 과 number 이 모두 1~9 사이이면 dan*number 의 구구단을 출력한다.

GuGuDanExpr 객체를 생성(생성자를 통해서 dan과 number에 대한 데이터를 전달하여 초기화한다.)하고 printPart() 를 호출한다. 단이 3, number가 4로 추출된다면 3 * 4 = 12 를 출력한다.

(2) dan 은 1~9 사이이고 number 가 10 이상이면 GuGuDanExpr 객체를 생성

(생성자를 통해서 dan에 대한 정보를 전달하여 초기화한다.)하고 printPart() 

를 호출한다. 

추출된 dan의 숫자가 2 라면…. 

2단 : 2 * 1 = 1  2 * 2 = 2  2 * 3 = 6 ………………

(3) dan 의 값이 10 이상이면 GuGuDanExpr 의 static 메서드 printAll() 을 호출

하여 1단부터 9단까지의 값들을 행 단위로 출력한다. 

1 * 1 = 1  1 * 2 = 2  1 * 3 = 3 ………………..

2 * 1 = 1  2 * 2 = 2  2 * 3 = 6 ………………...

……………..

9 * 1 = 9  9 * 2 = 18 9 * 3 = 27………………...

```java
//Multiplication
- dan : int
- number : int
-------------------
Multiplication ()
Multiplication (dan : int)
Multiplication ( dan : int, number : int)
+ printPart() : void
//GuGuDanExpr
GuGuDanExpr ()
GuGuDanExpr (dan : int)
GuGuDanExpr ( dan : int, number : int)
+ printAll() : void
-------------------------------------
//GuGuDan
+ main(String args[]) : void
```

```java
//[solution]
//실습3 GuGuDan
import day6.MethodLab3;

class Multiplication {
	private int dan;
	private int number;

	Multiplication() {
	}

	Multiplication(int dan) {
		this.dan = dan;
	}

	Multiplication(int dan, int number) {
		this.dan = dan;
		this.number = number;
	}

	public void printPart() {
		if (number == 0) {
			for (int n = 1; n <= 9; n++)
				System.out.print("\t" + dan + "*" + n + "=" + dan * n);
			System.out.println();
		} else {
			System.out.println(dan * number);
		}
	}
}

class GuGuDanExpr extends Multiplication {
	GuGuDanExpr() {
	}

	GuGuDanExpr(int dan) {
		super(dan);
	}

	GuGuDanExpr(int dan, int number) {
		super(dan, number);
	}

	static void printAll() {
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				System.out.printf("%d*%d=%d ", i, j, i * j);
			}
			System.out.println();
		}
	}
}

public class GuGuDan {
	public static void main(String[] args) {
		int dan = MethodLab3.getRandom(1, 20);
		int number = MethodLab3.getRandom(1, 20);
		GuGuDanExpr guguDanExpr;
		System.out.println(dan + " " + number);
		if (dan >= 1 && dan <= 9 && number >= 1 && number <= 9) {
			guguDanExpr = new GuGuDanExpr(dan, number);
			System.out.print(dan + " * " + number + " = ");
			guguDanExpr.printPart();
			System.out.println();
		} else if (dan >= 1 && dan <= 9) {
			if (number >= 10) {
				guguDanExpr = new GuGuDanExpr(dan);
				guguDanExpr.printPart();
				System.out.println();
			}
		} else if (dan >= 10) {
			guguDanExpr = new GuGuDanExpr();
			guguDanExpr.printAll();
		}
	}
}
```

- **실습4 문제**

다음과 같은 조건을 만족하는 프로그램을 작성 하시오.
Human 이라는 부모 클래스를 상속 받은 Student 클래스를 이용하여 프로그래밍한다.
3개의 Student 객체를 생성 하여 배열에 셋팅 한 후 각 객체의 모든 정보를 출력한다.

1. 사용 데이터

   아래와 같이 3 개의 Student Object 를 생성 하여 프로그램 을 동작 시킨다

   name		나이		신장		몸무게		학번			 전공

   홍길동		20		  171			81			201101		영문

   고길동		21		  183			72			201102		건축

   박길동		22		  175			65			201103		컴공	

2. 구현 클래스 다이어그램

```java
//Human
- name :String
- age :int
- height:int
- weight:int
----------------
+ Human()
+ Human(name:String, age:int, height:int, weight:int)
+ printInformation():String
//Student
- String number
- String major
-----------------
+ Student()
+ Student (name:String, age:int, height:int, weight:int, String number, String major)
+ printInformation():String
//StudentTest
+ main(args:String [][]):void
```

3. 구현 클래스

   [Package명]

   exercise

   - Class명

     - Human

       - method

         +Human() - 설명: 기본 생성자

         +Human(name : String, age : int, height : int, weight : int) - 설명: 4개 인스턴스 변수의 값을 초기화 하는 생성자

         +printInformation():String - 설명: Human 정보를 리턴 한다.

     - Student

       - method

         - +Student() - 설명: 기본생성자

         - +Student(name : String,age : int, height : int,weight : int,String number, String major)

           설명: 6개 인스턴스 변수의 값을 초기화하는 생성자

         - +printInformation():String - 설명: Student 정보를 리턴 한다.

     - StudentTest

       - method
         - main(String args[]): void - 설명: main 함수 안에서 Student 타입의
           배열을 선언하여 동작 시킨다.

     클래스 명과 method 명은 변경 하지 않는다.

     위에 선언한 멤버변수와 메서드만을 이용한다.

4. StudentTest 클래스 구조

   Student 객체를 담을 수 있는 배열을 선언 하여 3개의 Student 객체를 생성 하여 담는다.

```java
public class StudentTest {
public static void main(String args[]) {
    Student arrays [] = new Student[3];
    // Student 객체를 3개 생성하여 배열에 넣는다.
    // 배열에 있는 객체 정보를 printInformation()을 호출하여 모두 출력 한다.
    }
}
```

5. 실행 결과

   ```java
   홍길동 20 171 81 201101 영문
   고길동 21 183 72 201102 건축
   박길동 22 175 65 201103 컴공
   ```

```java
//solution
//실습4 Package exercise
package exercise;

public class Human {
	private String name;
	private int age;
	private int height;
	private int weight;
	
	public Human() {
	}
	public Human(String name, int age, int height, int weight) {
		this.name = name;
		this.age = age;
		this.height = height;
		this.weight = weight;
	}
	// Human 정보를 리턴 한다.
	public String printInformation() {
		return name + "\t" + age + "\t" + height + "\t" + weight;
	}
}

public class Student extends Human {
	private String number;
	private String major;
	
	public Student() {
	}
	public Student(String name, int age, int height, int weight, String number, String major) {
		super(name, age, height, weight);
		this.number = number;
		this.major = major;
	}
	//Student 정보를 리턴한다.
	public String printInformation() {
		return super.printInformation()+ "\t" + number + "\t" + major;
	}
}
public class StudentTest {
	public static void main(String[] args) {
		Student arrays[] = new Student[3];
		arrays[0] = new Student("홍길동", 20, 171, 81, "201101", "영문");
		arrays[1] = new Student("고길동", 21, 183, 72, "201102", "건축");
		arrays[2] = new Student("박길동", 22, 175, 65, "201103", "컴공");
		for (int i = 0; i < 3; i++) {
			System.out.println(arrays[i].printInformation());
		}
	}
}
```

