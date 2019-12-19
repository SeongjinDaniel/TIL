# Day12

java.lang- Object, Math, Integer, String, StringBuffer, Character ...

​		**String** : 문자열 처리와 관련된 메서드들을 가지고 있다.

​					String  객체가 생성된 이후 초기화된 문자열 내용은 변경 불가하다.

​					읽기 용도로만 사용 가능하다.

​					"abc" + "가나다" -> "abc가나다"

​					"a" + "b" + "c" + "d" -> 1, 2, 3번 객체를 생성, 2번 객체를 가비지에서 제거

​													-> JAVA version이 높아 지면서 알아서 Compiler가 StringBuffer로 바꿔서 사용을 한다.

​		**StringBuffer** : 문자열 편집하는 용도 

```java
StringBuffer sb = new StringBuffer();
    sb.append("a");
    sb.append("b");
    sb.append("c");
    sb.append("d");
```

```java
equals() : Object 클래스 : == 연산과 동일
Book b1 = new Book("짱구", "xxx", 100000);
Book b2 = new Book("짱구", "xxx", 100000);
Book b3 = b2;
b1 == b2 ? false
b1.3 == b2 ? true
b1.equals(b2) ? false
b3.equals(b2) ? true
// 만약 equals를 수정해서 사용하려면 overriding 하여 사용할 수 있다.
// 객체가 만들어질 때 객체의 내용과 내용을 비교하겠다면 equals를 오버라이딩을 해야 한다.

```

### API : Application Programming Interface (라이브러리, 패키지)

​		자주 사용되는 기능을 미리 만들어 놓은 프로그램

​		자바 : 클래스, abstract 클래스, 인터페이스..

​		C: 함수

## Equals

- **실습1 Equals**

```java
//실습1 Equals
package day12;

import java.util.Date;

class Value {
	int value;
	Value(int value){
		this.value = value;
	}
	public boolean equals(Object obj) {
		boolean result = false;
        if(obj != null && obj instanceof Value)
        	if(value == ((Value)obj).value)
        		result = true;
		return result;
    }
}
public class EqualsTest {
	public static void main(String[] args) {
		Value v1 = new Value(10);
		Value v2 = new Value(10);
		Value v3 = new Value(20);
		System.out.println(v1.equals(null)); // f
		System.out.println(v1.equals(v3));   // f
		System.out.println(v1.equals(v2));   // t
		System.out.println(v1.equals(new Date()));   // f value 객체가 아니다
		/*if(v1.equals(v2)) 
			System.out.println("v1과 v2는 같습니다.");
		else 
			System.out.println("v1과 v2는 다릅니다.");
		v2 = v1;
		if(v1.equals(v2)) 
			System.out.println("v1과 v2는 같습니다.");
		else 
			System.out.println("v1과 v2는 다릅니다.");*/
		String s1 = "가나다";
		String s2 = "가나다";
		String s3 = new String("가나다");
		String s4 = new String("가나다");
		
		System.out.println(s1 == s2);		// true -> 같은 문자열을 쓰면 객체는 실제로 하나만 만들어진다.
		System.out.println(s3 == s4);		// false
		System.out.println(s1.equals(s2));	// true
		System.out.println(s3.equals(s4));	// true
		
	}
}
```

## Integer

- **실습2 Integer**

```java
//실습2 Integer
package day12;
public class IntegerTest {
	public static void main(String[] args) {
		if(args.length != 2) {
			System.out.println("프로그램 아규먼트 2개를 숫자로 입력하세요");
		} else {
			System.out.println(Integer.parseInt(args[0])
					 +Integer.parseInt(args[1]));
		}
		String s1 = Integer.toBinaryString(12);
		String s2 = Integer.toBinaryString(88);
	    
		System.out.printf("%s\n", s1);
		System.out.printf("%s\n", s2);
		
		int num1 = Integer.parseInt(s1 ,2);
		int num2 = Integer.parseInt(s2, 2);
		
		System.out.printf("%d\n", num1);
		System.out.printf("%d\n", num2);
	}
}
```

## StringBuffer

- **실습3 StringBuffer**

```java
//실습3 StringBuffer
package day12;
public class StringBufferTest {
	public static void main(String[] args) {

		StringBuffer buffer = new StringBuffer();
		String str = "자바프로그래밍";
		buffer.append(str);

		System.out.printf("%s\n", buffer);
		buffer.reverse();
		System.out.printf("%s\n", buffer);
		System.out.printf("길이 : %d\n", buffer.length());

		StringBuffer buffer2 = new StringBuffer();
		buffer2.append("자");
		buffer2.append("바");
		buffer2.append("프");
		buffer2.append("로");
		buffer2.append("그");
		buffer2.append("래");
		buffer2.append("밍");

		System.out.println(buffer == buffer2);
		System.out.println(buffer.equals(buffer2));
		System.out.println(buffer.toString().equals(buffer2.toString()));
	}
}
```

- **실습4 StringTest**

```java
//실습4 StringTest
package day12;
public class StringTest {
	public static void main(String[] args) {
		System.out.println("1".length());
		System.out.println("가나다".length());
		System.out.println("abc".charAt(1)); 		// index는 0부터 ~		
		System.out.println("abc".toUpperCase());
		String str1 = "ABCDEFGHIJ";
		String str2 = "abcdefgfhij";
		
		// subString은 첫인덱스는 포함 끝 인덱스는 미포함 
		System.out.println(str1.substring(4));     		        
		System.out.println(str1.substring(0, 3));  		
		System.out.println(str2.indexOf("f"));	 	// 앞에 0부터 ~       		  
		System.out.println(str2.lastIndexOf("f"));  // 뒤에서 부터
		System.out.println(str2.replace('h', 'H')); // 내부적으로 또하나의 객체가 생성된다 
													// replace를 많이 사용할 때는 StringBuffer를 사용해라
		
		String str3 = "java:html5:css3:javascript";
		String[] ary = str3.split(":");   
		
		for(int i=0; i < ary.length; i++){
			System.out.println(ary[i]);
		}		
		// toCharArray -> 한문자한문자 char형 배열에 저장하여 return한다.
		char ch[] = str3.toCharArray();
		System.out.println(str3.length() + " ---- " + ch.length);
		System.out.println(ch);
		for(int i=0; i < ch.length; i++){
			System.out.print(ch[i] + " ");
		}
	}
}
```

- **실습5 AutoBoxingUnboxingTest**

```java
// 실습5 AutoBoxingUnboxingTest
package day12;
public class AutoBoxingUnboxingTest {
	public static void main(String[] args) {
		Integer obj = new Integer(10);
		obj = 100;  // 기본 --> 객체 - 오토박싱
		int result = obj + 10; // 객체 --> 기본 - 오토언박싱
		System.out.println(result);
	}
}
```

