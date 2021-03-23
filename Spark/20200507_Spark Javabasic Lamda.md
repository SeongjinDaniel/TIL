# 20200507 Spark Javabasic

### 예제1

```java
package lamdaexam;

public class MyFunctionalExam3 { 
	public static void main(String[] args) {
		MyFunctionalInterface3 fi;
		
		fi = (x, y) -> {
			int result = x + y;
			return result;
		};
		System.out.println(fi.method3(2, 5));
		
		fi = (x, y) ->  {return x + y; };
		System.out.println(fi.method3(2, 5));
		
		fi = (x, y) -> x + y;
		System.out.println(fi.method3(2, 5));
		
		fi = (x, y) -> sum(x, y);
		System.out.println(fi.method3(2, 5));
	}
	
	public static int sum(int x, int y) {
		return x + y;
	}
}
```

```java
package lamdaexam;

@FunctionalInterface
public interface MyFunctionalInterface3 {
	public int method3(int x, int y);
}
```

### 예제2

```java
package lamdaexam;

public class UsingLocalVariable {
	void test_method(int arg) {  
		int localVar = 40; 	
		
		// 변경하고자 하는 변수가 밖에 있으면 anonymous 람다식 안에는 사용할 수 없다.
		// 읽기 용도만 가능!! 하고 밖에 있는 변수는 자동으로 final로 변경됨
		//arg = 31;  		
		//localVar = 41; 
		
		System.out.println(arg + ":" + localVar);
        
		//람다식
		MyFunctionalInterface5 fi= () -> {
			//로컬변수 사용
			System.out.println("arg: " + arg); 
			System.out.println("localVar: " + localVar + "\n");
		};
		fi.method5();
	}
}

```

```java
package lamdaexam;

public class UsingLocalVariableExample {
	//String[] == String... 
	public static void main(String... args) {
		UsingLocalVariable ulv = new UsingLocalVariable();
		ulv.test_method(20);
	}
}
```

```java
package lamdaexam;

public interface MyFunctionalInterface5 {
    public void method5();
}
```

### 예제3

```java
package lamdaexam;

public class UsingThis {
	public int outterField = 10;

	class Inner {
		int innerField = 20;

		void test_method() {
			//람다식
			MyFunctionalInterface4 fi= () -> {
				System.out.println("outterField: " + outterField);
				System.out.println("outterField: " + UsingThis.this.outterField + "\n");
				
				System.out.println("innerField: " + innerField);
				System.out.println("innerField: " + this.innerField + "\n");
			};
			fi.method4();
		}
	}
}

```

```java
package lamdaexam;

public class UsingThisExample {
	public static void main(String... args) {
		UsingThis usingThis = new UsingThis();
		UsingThis.Inner inner = usingThis.new Inner();
		inner.test_method();
	}
}
```

```java
package lamdaexam;

public interface MyFunctionalInterface4 {
    public void method4();
}
```

-------

### 실습

AnonyThreadLab.java 를 LamdaThreadLab.java 로 복사한다.
스레드 클래스를 객체 생성해서 java.lang.Thread 클래스의 객체를 생성하는 
부분을 람다식 정의로 변경해 본다...

```java
package lamdaexam;

import java.text.SimpleDateFormat;
import java.util.Date;

public class LamdaThreadLab {
	public static void main(String[] args) {
		new Thread(()->{
			try {
				for (int i = 0; i < 5; i++) {
					Date date = new Date();
					SimpleDateFormat format1 = new SimpleDateFormat("H시 m분 s초");
					Thread.sleep(5 * 1000); // 5초마다
					System.out.println(format1.format(date));
				}
			} catch (InterruptedException e) {

			}

		}).start();

	}
}
```

### annonymouse 객체 lamda로 변경하기

### 실습 

```java
package lamdatest;

interface Calculation {
	public int add(int a, int b);
}

public class Exercise1 {
	public static void exec(Calculation com) {
		int k = 10;
		int m = 20;
		int value = com.add(k, m);
		System.out.println("덧셈 결과 : " + value);
	}

	public static void main(String[] args) {
		// 추상 클래스는 new 객체 생성이 불가하다.
//		Calculation cc = (n1, n2) -> {
//			return n1 + n2;
//		};
//		exec(cc);

		exec((a, b) -> {
			return a + b;
		});

//		exec(new Calculation () {
//			public int add(int a, int b) {
//					return a + b;
//			   }
//		});

	}
}

//Cannot instantiate the type 클래스명
//
//원인 : 추상클래스를 인스턴스화 할 경우 발생
//해결 : 해당 클래스 추상화 제거
//
//추상클래스는 new() 객체 생성이 불가능하다. 
```

### 실습 

```java
package lamdatest;

@FunctionalInterface // 함수형 인터페이스 체크 어노테이션
interface MyNumber {
	int getMax(int num1, int num2);
}

public class Exercise2 {
	public static void main(String[] args) {
//		MyNumber max = new MyNumber() {
//			public int getMax(int x, int y) {
//				return (x >= y) ? x : y;
//			}
//		};
		
		MyNumber mn = (n1, n2) -> {
			return (n1 >= n2) ? n1 : n2;
		};
//		System.out.println(max.getMax(100, 300));
		System.out.println(mn.getMax(100, 300));
	}
}

```

### 실습 

```java
package lamdatest;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Exercise3 {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("abc", "aaa", "bbb", "ccc");
		Collections.sort(list);
		System.out.println("기본은 오름차순 : "+list);
		Collections.sort(list, (s1, s2) -> {
				return s2.compareTo(s1);
		});
//		Collections.sort(list, new Comparator<String>() {
//			public int compare(String s1, String s2) {
//				return s2.compareTo(s1);
//			}
//		});

		System.out.println("내림차순으로 정렬하려면 두번째 매개변수를 기준으로 비교하는 Comparator 객체 전달 : "+list);
	}
}
```

### 실습 

```java
package lamdatest;

interface Test {
	void run();
	void print();
}

public class Exercise4 {
	public static void main(String[] args) {
		Test test = new Test() {
			@Override
			public void run() {
				System.out.println("run");
			}
			@Override
			public void print() {
				System.out.println("print");
			}
		};
		test.run();
		test.print();
	}
}
```

###  실습 

```java
package lamdatest;

interface ActionExpression {
	void exec(Object... param);
}

interface FuncExpression<T> {
	T exec(Object... param);
}

public class Exercise5 {
	public static void Test1(ActionExpression action) {
		action.exec("hello world");
	}

	public static void Test2(FuncExpression<String> func) {
		String ret = func.exec("hello world");
		System.out.println(ret);
	}

	public static void main(String[] args) throws Exception {
		Test1((data) -> {
			System.out.println("Test1 - " + data[0]);
		});
//		Test1(new ActionExpression() {
//			public void exec(Object... data) {
//				System.out.println("Test1 - " + data[0]);
//			}
//		});
		Test2((data) -> {
				System.out.println(data[0]);
				return "OK";
		});
//		Test2(new FuncExpression<String>() {
//			public String exec(Object... data) {
//				System.out.println(data[0]);
//				return "OK";
//			}
//		});
	}
}
```



