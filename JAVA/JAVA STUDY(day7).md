# Day 7

```java
//실습 1 MethodTest10
public class MethodTest10 {
	public static void main(String[] args) {
		int p1[] = {20, 10, 14, 30};
		System.out.println("p1의 변수의 값 : " + p1);
		printArray(p1);
		int[] result = updateArray1(p1);
		printArray(result);
		printArray(p1);
		System.out.println("----------------------------");
		updateArray2(p1);
		printArray(p1);
	}
	static void printArray(int[] p1) {
		for(int data : p1) {
			System.out.printf("%d ", data);
		}
		System.out.printf("\n");
	}
	
	static int[] updateArray1(int[] p2){
		System.out.println("p1의 변수의 값 : " + p2);
		int[] result = new int[p2.length];
		for(int i = 0; i < result.length; i++) {
			result[i] = p2[i] * 2;
		}
		return result;
	}
	
	static void updateArray2(int[] p3){
		System.out.println("p3의 변수의 값 : " + p3);
		for(int i = 0; i < p3.length; i++) {
			p3[i] = p3[i] * 2;
		}
	}
}
```

## 객체지향언어

- 기존의 프로그래밍언어와 크게 다르지 않다.
- 코드의 재사용성이 높다.
- 코드의 관리가 쉬워졌다.
- 신뢰성이 높은 프로그램의 개발을 가능하게 한다.

### 클래스와 객체의 정의와 용도

- 클래스의 정의 - 클래스란 객체를 정의해 높은 것이다.
- 클래스의 용도 - 클래스는 객체를 생성하는데 사용된다.
- 객체의 정의 - 실제로 존재하는 것. 사물 또는 개념.
- 객체의 용도 - 객체의 속성과 기능에 따라 다름.

클래스 : 제품 설계도, TV 설계도, 붕어빵기계

객체     : 제품, TV, 붕어빵

### 객체와 인스턴스

- 객체는(object)는 인스턴스(instance)를 포하하는 일반적인 의미
- 인스턴스화 : 클래스로부터 인스턴스를 생성하는 것.

### 객체의 구성요소

- 객체는 속성과 기능으로 이루어져 있다.
- 속성은 변수로, 기능은 메서드로 정의한다.

속성 : 크기, 길이, 높이, 색상, 볼륨, 채널 등      ------> 변수 String color; boolean power; int channel;

기능 : 켜기, 끄기, 볼륨 높이기, 볼륨 낮추기, 채널 높이기 등 ------> 메서드 void power() { power = ! power;} ...

### 인스턴스의 생성과 사용

- 인스턴스의 생성방법

```java
클래스명 참조변수명; // 객체를 다루기 위한 참조변수 선언
참조변수명 = new 클래스명(); // 객체생성 후, 생성된 객체의
						 // 주소를 참조변수에 저장
TV t;
t = new Tv();

Tv t = new Tv(); // general
```

```java
//실습2 StudentTest
class Student { // public 클래스는 딱 하나 이어야한다. public 사용하면 error
	String name;
	int age;
	String subject;

	void printStudentInfo() {// static은 있어도 없어도 괜찮아
		System.out.println(name + " 학생은 나이가 " + age + "입니다");
	}
	void study() {
		System.out.println(name + " 학생은 " + subject + " 과목을 학습합니다");
	}
}

public class StudentTest {
	public static void main(String[] args) {
		Student st1 = new Student();
		System.out.println(st1);
		System.out.println(st1.name);
		System.out.println(st1.age);
		System.out.println(st1.subject);
		st1.printStudentInfo();
		st1.study();
		st1.name = "듀크";
		st1.age = 24;
		st1.subject = "HTML5";
		st1.printStudentInfo();
		st1.study();
		System.out.println();
		Student st2 = new Student();
		System.out.println(st2);
		System.out.println(st2.name);
		System.out.println(st2.age);
		System.out.println(st2.subject);
		st2.printStudentInfo();
		st2.study();
		st2.name = "턱시";
		st2.age = 30;
		st2.subject = "CSS3";
		st2.printStudentInfo();
		st2.study();
		
		st2 = st1;
		System.out.println(st1);
		System.out.println(st2);
		st1.printStudentInfo();
		st1.study();
		st2.printStudentInfo();
		st2.study();
	}
}
```

### 생성자 메서드: constructor

- 클래스를 객체 생성할 때 호출되는 메서드이다.

  ​	new 클래스명()

  ------------생성자 메서드

- 모든 클래스는 1개 이상의 생성자 메서드를 가지고 있어야 한다.

- 클래스의 소스에 생성자 메서드가 정의되어 있지 않으면 컴파일러가 생성자를

  만들어 준다. --> 디폰트 생성자

- 생성자 메서드 정의 방법

  (1) 메서드명은 클래스명과 동일해야 한다.

  (2) 매개변수는 선택적이다. (오버로딩 가능하다.)

  (3)  리턴값의 타입은 생략한다.

  (4) 객체 생성시 수행해야 하는 기능 또는 객체 생성시 데이터를 전달받아서

  ​	멤버변수들의 값을 초기화 하는 기능

```java
//실습3 DateTest
import java.util.Date;
import java.util.GregorianCalendar; // 현재 요일 정보를 알수 있는 메서드가 있다.
public class DateTest {

	public static void main(String[] args) {
		// Date
		Date d = new Date();
		System.out.println(d.toString());
		GregorianCalendar gc = new GregorianCalendar();
		System.out.println(gc.get(GregorianCalendar.DAY_OF_WEEK)); // 일 : 1, 월 : 2, 화 : 3......
		gc = new GregorianCalendar(1991, 2, 24); // 1월~12월 : 0~11
		System.out.println(gc.get(GregorianCalendar.DAY_OF_WEEK));
	}

}
```

```java
//실습4 StudentNew
class StudentNew { // public 클래스는 딱 하나 이어야한다. public 사용하면 error
	String name;
	int age;
	String subject;
	
	// 생성자를 사용해서 초기화
	StudentNew(String p1, int p2, String p3){
		name = p1;
		age = p2;
		subject = p3;
	}

	void printStudentInfo() {// static은 있어도 없어도 괜찮아
		System.out.println(name + " 학생은 나이가 " + age + "입니다");
	}
	void study() {
		System.out.println(name + " 학생은 " + subject + " 과목을 학습합니다");
	}
	void study(int hour) {
		System.out.println(name + " 학생은 " + subject + " 과목을 " + hour + "시간 동안 학습합니다");
	}
}

public class StudentTest2 {
	public static void main(String[] args) {
		StudentNew st1 = new StudentNew("듀크", 24, "JavaScript");
		System.out.println(st1);
		st1.study(2);
		StudentNew st2 = new StudentNew("둘리", 100, "Scala");
		System.out.println(st2);
		st2.study(2);
	}
}
```

```java
//실습5 StudentNew2
class StudentNew2 { 
	String name;
	int age;
	String subject;
	
	StudentNew2(){
		
	}
	StudentNew2(String p1, int p2){
		name = p1;
		age = p2;
		subject = "자바";
	}
	StudentNew2(String p1, int p2, String p3){
		name = p1;
		age = p2;
		subject = p3;
	}

	void printStudentInfo() {// static은 있어도 없어도 괜찮아
		System.out.println(name + " 학생은 나이가 " + age + "입니다");
	}
	void study() {
		System.out.println(name + " 학생은 " + subject + " 과목을 학습합니다");
	}
	void study(int hour) {
		System.out.println(name + " 학생은 " + subject + " 과목을 " + hour + "시간 동안 학습합니다");
	}
}

public class StudentTest3 {
	public static void main(String[] args) {
		StudentNew2 st1 = new StudentNew2("듀크", 24, "JavaScript");
		System.out.println(st1);
		st1.study(2);
		StudentNew2 st2 = new StudentNew2("둘리", 100);
		System.out.println(st2);
		st2.study(2);
		StudentNew2 st3 = new StudentNew2();
		System.out.println(st3);
		st3.study(2);
	}
}
```

- **실습6 문제**

[클래스 정의와 객체 생성(인스턴스)1]

Member 객체 (인스턴스)를 3개 생성하고 

각각의 멤버 변수에 정보를 저장한 후에 

각각 정보를 추출하여 다음 형식으로 출력하는 MemberTest 클래스를 구현한다.

 회원1 : 이름(계정,패스워드,생년)

 회원2 : 이름(계정,패스워드,생년)

 회원3 : 이름(계정,패스워드,생년)

```java
// Member
// 회원 객체
//--------
// 회원 이름
// 회원 계정
// 회원 암호
// 회원 생년
+name : String
+account : String
+passwd : String
+birthyear : int
```

```java
//실습6 MemberTest
class Member {
	String name;
	String account;
	String passwd;
	int birthyear;
}

public class MemberTest {

	public static void main(String[] args) {	
		Member member1 = new Member();
		Member member2 = new Member();
		Member member3 = new Member();
		
		member1.name = "듀크";
		member1.account = "ss";
		member1.passwd = "1234";
		member1.birthyear = 2019;
		System.out.print("회원1 : " + member1.name + "(" + member1.account + 
				"," + member1.passwd + "," + member1.birthyear + ")" + "\r\n");
		
		member2.name = "이크";
		member2.account = "aa";
		member2.passwd = "12345";
		member2.birthyear = 2018;
		System.out.print("회원2 : " + member2.name + "(" + member2.account + 
				"," + member2.passwd + "," + member2.birthyear + ")" + "\r\n");
		member3.name = "에크";
		member3.account = "bb";
		member3.passwd = "123456";
		member3.birthyear = 2017;
		System.out.print("회원3 : " + member3.name + "(" + member3.account + 
				"," + member3.passwd + "," + member3.birthyear + ")" + "\r\n");
	}

}
```

- **실습7 문제**
[클래스 정의와 객체 생성 실습 2]
```java
// Book
// title : String
// author : String
// price : int
// Book()
// Book(title:String, author:String, price:int)
// getBookInfo():
// String  -> "책이름 저자 가격"순으로 적당한 간격으로 리턴한다.

// BookTest
// +main(args:String[]:void)
```

Book 클래스의 객체(인스턴스)를 5개 생성하고 각각 변수에 저장한 후 각각의 책 정보를 행 단위로 출력하는 BookTest 클래스를 만든다. (아규먼트를 받지않는 생성자가 호출될 땐 “자바의 정석” 정보로 Book 객체의 정보를 초기화 하며, 다른 Book 객체들은 호출되는 생성자를 통해서 책 정보를 전달하면서 객체를 생성한다. 책 정보는 임의로 정한다.)

```java
//실습 7 BookTest
class Book {
	String title;
	String author;
	int price;

	Book() {
//		title = "JAVA의 정석";
//		author = "남궁성";
//		price = 20000;
		this("자바의 정석", "남궁 성", 30000); // Book(String title, String author, int price) 이 생성자를 호출한다.
	}

	Book(String title, String author, int price) {
		this.title = title;
		this.author = author;
		this.price = price;
	}
	
	String getBookInfo() {
		String result = "";
		result += "책이름 : " + title + ", ";
		result += "저자 : " + author + ", ";
		result += "가격 : " + price;
		
		return result;
	}
}

public class BookTest {

	public static void main(String[] args) {
		Book book1 = new Book();
		Book book2 = new Book("C", "듀크", 15000);
		Book book3 = new Book("C++", "이크", 16000);
		Book book4 = new Book("C#", "에크", 17000);
		Book book5 = new Book("Python", "취크", 18000);
		
		System.out.println(book1.getBookInfo());
		System.out.println(book2.getBookInfo());
		System.out.println(book3.getBookInfo());
		System.out.println(book4.getBookInfo());
		System.out.println(book5.getBookInfo());
	}
}
```

### this

- this : 자신의 객체의 참조값을 의미하는 리터럴

  ​		  this.xxxx 나의 멤버 xxxx

  this – 인스턴스 자신을 가리키는 참조변수. 인스턴스의 주소가 저장되어있음

  ​			모든 인스턴스 메서드에 지역변수로 숨겨진 채로 존재

  this() : 생성자 메서드내에서만 호출 가능

  ​			생성자 메서드의 첫 행에서만 호출 가능

  ​			동일한 클래스내에 있는 다른 생성자를 호출

  this() – 생성자, 같은 클래스의 다른 생성자를 호출할 때 사용

  ​			다른 생성자 호출은 생성자의 첫 문장에서만 가능

### 생성자

인스턴스가 생성될 때마다 호출되는 '인스턴스 초기화 메서드'

인스턴스 변수의 초기화 또는인스턴스 생성시 수행할 작업에 사용

몇가지 조건을 제외하고는 메서드와 같다

모든 클래스에는 반드시 하나 이상의 생성자가 있어야한다.

------------

int[] ary = new int[5];

Product[] p = new Product[5];

- **실습8 문제**
[클래스 정의와 객체 생성 실습 3]
```java
[Product]
-name : String
-balance : int
-price : int 
-------------------
Product()
Product(String, int, int)
getName() : String
getBalance() : int
getPrice() : int
[ProductTest]
+main(String[]) : void
* Product(String, int, int) - 파라미터로 전달된 값들로 각각의 멤버변수를 초기화한다.
* Product() - 상품이름에 “듀크인형”, 재고량에 5, 금액에 10000원을 초기화 한다.
* getName() : String - 상품명을 리턴한다.
* getBalance() : int - 재고량을 리턴한다.
* getPrice() : int - 가격을 리턴한다.
* main() - 5개의 원소를 갖는 Product 타입의 배열을 생성한 후에 Product 객체를 5개 생성하여 각각의 원			 소로 대입하고 Product 객체들의 각 정보들을 행 단위로 출력한다.(상품명   재고량   가격) 
		 – 가격은 천단위로 , 를 붙이고 금액 끝에 ‘원’도 붙여서 출력한다.
```

```java

//실습8 Product
class Product {
	String name;
	int balance;
	int price;

	Product() {
		this("듀크인형", 5, 10000);
	}

	Product(String name, int balance, int price) {
		this.name = name;
		this.balance = balance;
		this.price = price;
	}

	String getName() {
		return name;
	}
	int getBalance() {
		return balance;
	}
	int getprice() {
		return price;
	}
}

public class ProductTest {
	public static void main(String[] args) {
		Product product[] = new Product[5];
		
		// 초기화 안하면 error
		product[0] = new Product("사과", 1, 500);
		product[1] = new Product("배", 2, 1000);
		product[2] = new Product("바나나", 3, 2500);
		product[3] = new Product("포도", 4, 3000);
		product[4] = new Product("수박", 5, 4500);

		for (int i = 0; i < 5; i++) {
			System.out.print("상품명: " + product[i].name + ", 재고량 : " + product[i].balance + ", 가격 : ");
			System.out.printf("%,d원\n", product[i].price);
		}
	}
}
```

