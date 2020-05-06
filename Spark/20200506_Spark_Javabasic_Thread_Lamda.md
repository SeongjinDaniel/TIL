# **20200506** Spark 사전지식

## 프로세스와 쓰레드(process & thread)

- 프로그램 -> 프로세스
- 멀티 쓰레드 : 2개이상의 쓰레드로 실행을 하는 것
- `ps` : 프로세스의 상태를 본다(cmd)
- `ps -ef` : 프로세스의 모든 정보를 보여줘라
- `ps -ef|more` : 페이지 단위로 확인가능!!
- `ps -ef > process.txt`  : 새로운 파일로 생성해서 확인 가능하다.
- `ps -ef | grep init` : ps 행마다 init이라는 행만 출력!!
- `grep unico *.java` : 현재 디렉토리에 자바 source가 30개가 있으면 갑자기 팀장이 30개 source중에 unico같은 파일을 열어보라고 하면 다 열어 볼 수 있다.

- 프로세스 : 실행 중인 프로그램, 자원(resources)과 쓰레드로 구성

- 쓰레드 : 프로세스 내에서 실제 작업을 수행

- 모든 프로세스는 하나 이상의 쓰레드를 가지고 있다.

  - 프로세스 : 쓰레드 = 공장 : 일꾼

- 싱글 쓰레드 프로세스

  = 자원 + 쓰레드

- 멀티 쓰레드 프로세스

  = 자원 + 쓰레드 + 쓰레드 + ... + 쓰레드

## 멀티프로세스 vs. 멀티쓰레드

"하나의 새로운 프로세스를 생성하는 것보다 

 하나의 새로운 쓰레드를 생성하는 것이 더 적은 비용이 든다."

**아래 내용들은 Java의 정석 pdf 참고!!** 

![image-20200506102627507](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506102627507.png)

![image-20200506102654409](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506102654409.png)

![image-20200506102616585](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506102616585.png)

![image-20200506102756899](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506102756899.png)

## 내부클래스

내부 클래스란 클래스의 내부에 정의되는 클래스로서 특정 클래스의 내에서만 주로 사용되는 클래스를 내부 클래스로 정의한다 . 내부 클래스에서는 외부 클래스의 멤버들을 접근할 수 있으며 캡슐화를 통해 코드의 복잡성을 줄일 수 있다 .

- 내부 클래스의 종류
  내부 클래스는 정의되는 위치에 따라 멤버 클래스와 로컬 클래스로 나뉜다 . 멤버 변수와 지역 변수로 나뉘는 변수와 같이 내부 클래스도 클래스의 멤버로 정의되는 멤버 클래스와 메서드 내에 정의되는 로컬 클래스로 나뉘며 각각 변수와 비슷한 유효범위와 성격을 지원한다

![image-20200506135440748](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506135440748.png)

멤버클래스는 인스턴스 클래스와 스태틱 클래스로 구성되며 로컬 클래스는 이름이 있는 로컬
클래스와 이름이 없는 로컬 클래스 (anonymous 클래스 로 나뉜다 .
내부클래스는 다른 클래스내에 포함되어 정의되지만 클래스 파일은 독립적으로 만들어 다음과
같은 규칙으로 파일명이 정해진다

| 내부 클래스의 종류   | 생성되는 클래스명의 규칙      |
| -------------------- | ----------------------------- |
| 인스턴스 클래스      | 외부클래스$내부클래스.class   |
| 스태틱 클래스        | 외부클래스$내부클래스.class   |
| 이름있는 로컬 클래스 | 외부클래스$N$내부클래스.class |
| 이름없는 로컬 클래스 | 외부클래스$N.class            |

로컬 클래스의 경우에는 Java 소스에 정의되는 순서에 따라서 클래스명 중간 또는 뒤에 1 부터 시작하는 숫자 가 자동으로 부여된다

```
C:\Oliver\eclipse-workspace\hadoopexam\target\classes\innerexam

--> Outer$Inner
--> Outer$Static_Inner
--> LocalTest$1Local 등등
이렇게 $가 들어가있으면 inner 클래스라는 것을 알 수 있다.
```



- 멤버 클래스

  동일 클래스에서는 물론이고 다른 클래스에서도 이 클래스들을 사용할 수 있다 . 멤버 변수와 비슷한
  성격을 갖는다 . 인스턴스 클래스 와 스태틱 클래스 로 나뉜다.

  ![image-20200506142757429](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506142757429.png)

  인스턴스 클래스는 외부 클래스의 인스턴스 멤버처럼 다루어 지며 주로 외부 클래스의 인스턴스
  멤버들과 관련된 작업에 사용될 목적으로 정의된다 . 인스턴스 클래스 내에서는 static 멤버를
  정의할 수 없다.
  스태틱 클래스는 외부 클래스의 클래스 멤버 (static 멤버 처럼 다루어 지며 주로 외부 클래스의
  클래스 메서드내에서 사용될 목적으로 정의된다 .
  멤버 클래스들도 멤버 변수들과 비슷한 방법으로 접근 제어자 지정이 가능하며 동일 클래스에서
  뿐만 아니라 외부 클래스의 밖에서도 접근하고자 하는 경우에는 각각 다음과 같은 방법으로 사용할
  수 있다.

  | 인스턴스 클래스   | A a =new A();<br/>A.B b = a.new B();<br/>b.멤버 |
  | ----------------- | ----------------------------------------------- |
  | **스태틱 클래스** | **A.C.멤버**                                    |

- 로컬 클래스
  메서드 내에 정의되는 클래스로서 로컬 변수와 비슷한 성격을 갖으며 , 활용 범위가 정의되어 있는
  메서드 블럭 내부로 제한된다 . Interface 는 로컬로 정의될 수 없다 . 포함하는 클래스의 멤버
  변수와 포함하는 메서드의 final 로컬변수 , final 매개변수사용이 가능하다 .
  로컬 클래스는 이름이 있는 로컬 클래스와 이름이 없는 로컬 클래스로 나뉘며 이름이 있는 로컬
  클래스를 로컬 클래스 , 이름이 없는 로컬 클래스를 익명 클래스 라고 부른다 .

![image-20200506142940918](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506142940918.png)



- 익명 클래스

![image-20200506143002278](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506143002278.png)

익명 클래스의 경우 new 키워드 뒤의 생성자 메서드의 명칭이 기존 클래스 명인 경우에는 ,
자동적으로 이 클래스의 자손 클래스가 되며 , 인터페이스 명인 경우에는 이 인터페이스를 구현하여
추가 상속하는 클래스로서 부모 클래스는 Object 이 된다 .

![image-20200506143037765](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200506143037765.png)

메서드 호출 시 매개변수의 타입이 추상 클래스 형이거나 인터페이스 형이어서 가볍게 자손
클래스를 구현하고 객체를 생성해서 전달하려는 경우 유용하게 사용될 수 있는 구문이다 .



## Java 8의 인터페이스 구문

추상 메서드 외에도 디폴트메서드와 스태틱 메서드 정의가 가능하다.

**디폴트 메서드 선언**
자바8에서 추가된 인터페이스의 새로운멤버

```
[public] default 리턴타입 메소드명(매개 변수, ...) {...}
```

실행 블록을 가지고 있는 메서드
default 키워드를 반드시 붙여야함
public 접근제한이 자동으로 붙음

**스태틱 메서드 선언**

```
[public] static 리턴타입 메소드명(매개 변수, ...) {...}
```

**익명 구현 객체**

- 구현 클래스 작성을 생략하고 바로 구현 객체를 얻는 방법

  - 이름 없는 구현 클래스 선언과 동시에 객체생성

    ```
    인터페이스 변수 = new 인터페이스() {
    	//인터페이스에 선언된 추상 메소드의 실체 메소드 선언
    }
    ```

  - 인터페이스의 추상 메서드들을 모두 재정의 해야 함

  - 추가적으로 필드와 메서드 선언가능하지만 익명 객체 안에서만 사용가능 하며 인터페이스 변수로는 접근 불가

**디폴트 메서드 사용**

- 인터페이스로 직접 사용 불가
  구현 객체가 인터페이스 변수에 대입되어야 호출할 수 있는 인스턴스 메서드
- 모든 구현 객체가 가지고 있는 기본 메서드로 사용
  필요에 따라 구현클래스가 디폴트 메서드를 재정의할 수 있음
- 정적 메서드 사용
  인터페이스로 바로 호출 가능

## 람다식이란?

**자바 8부터 함수적 프로그래밍 위해 람다식 지원**

- 람다식(Lambda Expressions)을 언어 차원에서 제공

  - 람다식: "식별자없이 실행가능한 함수"
  - 익명함수(anonymous function)를 생성하기 위한 식

- 자바에서 람다식을 수용한 이유

  - 코드가 매우 간결해진다.
  - 컬렉션요소(대용량데이터)를 필터링 또는 매핑해서 쉽게 집계할 수 있다.

- 자바는 람다식을 함수적 터페이스의 익명 구현 객체로 취급

  ```
  람다식 -> 매개변수를 가진 코드 블록 -> 익명 구현 객체
  ```

  - 어떤 인터페이스를 구현할지는 대입되는 인터페이스에 달려있음

  ```
  Runnable runnable = () -> {...}; // 람다식
  ```

### 람다식이란

람다식(lambda expression)이란간단히말해메서드를하나의식으로표현한것이다.

```
//메서드
int min(int x, int y) {
return x < y ? x : y;
}
//람다표현식
(x, y) -> x < y ? x : y;
```

위의 예제처럼 메서드를 람다식으로 표현하면, 클래스를 작성하고 객체를 생성하지 않아도 메서드로 사용할 수 있으며, 다른 메서드 호출시 아규먼트로 전달될 수도 있고, 메서드의 결과값으로 반환될 수도있다.

- No arguments: () -> System.out.println("Hello")

- One argument: s -> System.out.println(s)

- Two arguments: (x, y) -> x + y

- With explicit argument types:

  ```
  (Integer x, Integer y) -> x + y
  ```

- Multiple statements

  ```
  (x, y) -> {
  	System.out.println(x);
  	System.out.println(y);
  	return ( x + y);
  }
  ```

### 람다식 기본 문법

함수적 스타일의 람다식 작성법

```
(타입 매개변수, ...) -> {실행문; ...}
```

```
(int a) -> {System.out.prinln(a);}
```

- 매개변수의 타입은 실행시에 대입 값 따라 자동 결정 -> 생략가능
- 하나의 매개 변수만 있을 경우에는 괄호( ) 생략가능
- 하나의 실행문만 있다면 중괄호{ } 생략 가능
- 매개변수 없다면 괄호( ) 생략 불가
- 리턴값이 있는 경우, return 문사용
- 중괄호{ }에 return 문만 있을 경우, 중괄호 생략가능

### 타겟 타입과 함수적 인터페이스

**타겟타입(target type)**

- 람다식이 대입되는 인터페이스
- 익명 구현 객체를 만들 때 사용할 인터페이스

```
인터페이스 변수 = 람다식;
```

**함수적 인터페이스(functional interface)**

- 하나의 추상 메서드만 성언된 인터페이스
- @FunctionalInterface 어노테이션 정의
  하나의 추상메서드만을 가지는지 컴파일러가 체크하여 두 개 이상의 추상 메서드가 선언되어 있으면 컴파일 오류 발생

### 타겟 타입과 함수적 인터페이스

**매개변수와 리턴값이 없는 람다식**

```
@FunctionalInterface
public interface MyFunctionalInterface{
	public void method();
}
```

MyFunctionalInterface fi = () -> {...}

fi.method();

**매개변수가 있는 람다식**

```
@FunctionalInterface
public interface MyFunctionalInterface{
	public void method(x);
}
```

MyFunctionalInterface fi = (x) -> {...} 또는 x -> { ...}

fi.method(5);

**리턴값이 있는 람다식**

```
@FunctionalInterface
public interface MyFunctionalInterface{
	public void method(int x, int y);
}
```

MyFunctionalInterface fi = (x, y) -> {...; return 값;}

int result = fi.method(2, 5);

```
MyFunctionalInterface fi = (x, y) -> {
	return x + y;
}
```

MyFunctionalInterface fi = (x, y) -> x + y;

```
MyFunctionalInterface fi = (x, y) -> {
	return sum(x, y);
}
```

MyFunctionalInterface fi = (x, y) -> sum(x, y);

## 클래스 멤버와 로컬 변수 사용

### 클래스의 멤버 사용

- 람다식 실행 블록에는 클래스의 멤버인 필드와 메서드를 제약없이 사용 가능
- 람다식 실행 블록내에서 this는 **람다식을 실행한 객체를 참조**

### 로컬 변수의 사용

- 람다식은 함수적 인터페이스의 익명 구현 객체를 생성한다.
- 람다식에서 사용하는 외부  로컬 변수는 final 특성을 갖는다

#### 예제1

```java
package lamdaexam;

@FunctionalInterface // 이것이 되기 위한 조건은 메서드가 하나여야한다
public interface MyFunctionalInterface1 {
	public static void pr() {
		System.out.println("ㅋㅋ");
	}
    public void method1();
//    public void method2();
}


```



```java
package lamdaexam;

public class MyFunctionalExam1 { 
	public static void main(String[] args) {
		MyFunctionalInterace1 fi; // 타겟 타입이 될수 있다.
		
		MyFunctionalInterface1.pr();
		fi= () -> { // 어차피 abstract 메서드가 하나니까 이름없이 사용해도 된다.(method1 메서드!!)
			String str = "method call1";
			System.out.println(str);
		};
		fi.method1();
		
		fi = new MyFunctionalInterface1 () {
			public void method1() { // 조상이 가지고 있는 abstract method명과 같아야한다.
				System.out.println("method call2"); 
			}
		};
		fi.method1();		
	}
}
```



#### 예제2

```java
package lamdaexam;

@FunctionalInterface
public interface MyFunctionalInterface2 {
    public void method2(int x);
}
```



```java
package lamdaexam;

public class MyFunctionalExam2 { 
	public static void main(String[] args) {
		MyFunctionalInterface2 fi;
		
		fi= (x) -> {
			int result = x * 5;
			System.out.println(result);
		};
		fi.method2(2);
		
		// 매개변수가 하나일때는 소괄호 생략 가능
		fi = x -> { System.out.println(x*5); };
		fi.method2(2);
		
		// 수행문장이 하나라서 중괄호 생략 가능
		// x -> System.out.println(x*5); -> 객체 !!
		fi = x -> System.out.println(x*5);
		fi.method2(2);
	}
}
```

