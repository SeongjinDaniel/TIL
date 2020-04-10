# Day13

------

## 컬렉션 프레임웍

### 특징

Collection API : 데이터들을 저장하여 사용하는 방의 역할을 하는 API

저장할 수 있는 데이터의 타입에 제한이 없다.

저장할 수 있는 데이터의 갯수에 제한이 없다.

## 1. List

- 저장되는 데이터의 순서를 유지한다.
- 저장되는 데이터의 중복을 허용한다.
- ArrayList, LinkedList, Vector -> Java쪽에서는 Vector보다는 ArrayList를 써라라고 권장

## 2. Set

- 저장되는 데이터의 순서를 유지 하지 않는다.
- 저장되는 데이터의 중복을 허용한다.

## 3. Map

- 데이터 이름과 데이터 값을 쌍으로 저장한다.

- 데이터 이름은 중복저장이 불가능하다.

  (키)

  key-value 쌍으로 데이터 저장

  HashMap, Hashtable -> Java쪽에서는 Hashtable보다는 HashMap을 써라!! 라고 권장중

Collections 클래스 : Collection API들을 도와주는 도우미 클래스

- **실습1 GenericTest**

```java
package day13;
import java.util.*;
public class GenericTest {
	public static void main(String[] args) {
		LinkedList list = new LinkedList();
		list.add("java");
		list.add("100"); // list.add(100); xxxxx
		list.add("servlet");
		list.add("jdbc");
		
		//첫번째 방법 -> 속도는 가장 느림
		for(int i=0; i < list.size(); i++)
			System.out.println(list.get(i));
		System.out.println();
		
		//↓↓↓↓↓↓↓밑에 방법이 모두 사용 가능↓↓↓↓↓↓↓
		//두번째 방법 -> 속도는 가장 빠름
		for(Object value : list) {
			String s = (String)value;		
			System.out.println(s);
		}
		System.out.println();
		
		//세번째 방법 -> 규격화한 방법 
		// -> itertor는 arrayList든 LinkedList든 다 사용가능
		Iterator iter = list.iterator(); 
		while(iter.hasNext()){
			Object value = iter.next();
			String s = (String)value;		
			System.out.println(s);
		}
	}
}

```

- **실습2 GenericTestNew**

```java
package day13;
import java.util.*;
public class GenericTestNew {
	public static void main(String[] args) {
		// 제네릭스 라는 구문이 적용되어 만들어진 클래스의 객체 생성시
		// 타입 파라미터라는 것을 사용한다. 
		LinkedList<String> list = new LinkedList<String>();  // 타입파라미터
		list.add("java");
		list.add("100");
		list.add("servlet");
		list.add("jdbc");
		
		for(int i=0; i < list.size(); i++)
			System.out.println(list.get(i));
		System.out.println();		
		
		for(String value : list) {			
			System.out.println(value);
		}
		System.out.println();
		
		Iterator<String> iter = list.iterator();
		while(iter.hasNext()){
			String s = iter.next();			
			System.out.println(s);
		}
	}
}
```

- 실습3 CreateGenericTest

```java
//실습3 CreateGenericTest
package day13;
import java.util.Date;
public class CreateGenericTest {
	public static void main(String[] args) {
		Value1 o1 = new Value1();
		o1.put("abc");
		String s1 = o1.get(); 
		System.out.println(s1);		
		
		Value2 o2 = new Value2();
		o2.put("abc");
		String s2 = (String)o2.get(); 
		System.out.println(s2);
		
		// JAVA 8에서 부터는 new Value3<String> 꺽쇠안에 객체 이름 안써도된다
		Value3<String> o3 = new Value3<>();		
		o3.put("abc");
		String s3 = (String)o3.get(); 
		System.out.println(s3);	
		
		Value3<Date> o4 = new Value3<Date>();	
		o4.put(new Date());
		Date s4 = o4.get(); 
		System.out.println(s4);
	}
}

// 오로지 String만 저장 가능
class Value1 {
	String obj;
	void put(String obj){
		this.obj = obj;
	}
	String get() {
		return obj;
	}
}
// 
class Value2 {
	Object obj;
	void put(Object obj){
		this.obj = obj;
	}
	Object get() {
		return obj;
	}
}
// Value3<Card> v = new Value3<card>();
// Value3<String> v = new Value3<String>();

// 받고 싶은 많큼 꺽쇠 괄호 안에다가 쓰면된다
// TT는 객체 생성할 때 class, 객체 변수 모두 가능 -> 객체만 가능!!
class Value3<T> {
	T obj;
	void put(T obj){
		this.obj = obj;
	}
	T get() {
		return obj;
	}
}
```

### ArrayList

### LinkedList

- 데이터를 searching 할때 ArrayList보다 늦는다. 왜? 옆 배열끼리 참조되어 연결되어 있기 때문이다.

  -> for each구문이나 ~~ 를 사용해서 문제를 개선

### Stack

- **실습4 Stack**

```java
//실습4 StackExample
package day13;
import java.util.*;
public class StackExample {

	public static void main(String[] args) {
			LinkedList<Integer> stack = new LinkedList<Integer>();
			stack.addLast(new Integer(12));
			stack.addLast(new Integer(59));
			stack.addLast(new Integer(7));
			while(!stack.isEmpty()){
				Integer num = stack.removeLast();
				System.out.println(num);
		}
	}
}
```

### Queue

- **실습5 Queue**

```java
//실습5 Queue
package day13;

import java.util.*;
public class QueueExample {
	public static void main(String[] args) {
		LinkedList<String> queue = new LinkedList<String>();
		queue.offer("토끼");
		queue.offer("사슴");
		queue.offer("호랑이");
		while (!queue.isEmpty()) {
			String str = queue.poll();
			System.out.println(str);
		}
	}
}
```

import java.util.LinkedList;

import java.util.Iterator;

↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 한번에 적용가능

import.java.util.*

### HashSet

- 실습6 SetExample1

```java
package day13;
import java.util.*;
public class SetExample1 {
    public static void main(String args[]) {
    	// LinkedHashSet을 사용하면 순서를 유지 할 수 있다.
        HashSet<String> set = new HashSet<String>();
        System.out.println(set.add("자바"));
        System.out.println(set.add("카푸치노"));
        System.out.println(set.add("에스프레소"));
        System.out.println(set.add("자바"));
        System.out.println("저장된 데이터의 수 = " + set.size());
        
        Iterator<String> iterator = set.iterator();
        while (iterator.hasNext()) {
            String str = iterator.next();
            System.out.println(str);
        }
        System.out.println(set);
    }
}
```

- 실습7 LottoMachine2

```java
package day13;
import java.util.*;
public class LottoMachine2 {
	public static void main(String[] args) {
		HashSet<Integer> set = new HashSet<Integer>();
		Random rand = new Random();
		
		while(set.size() != 10) {
			set.add(rand.nextInt(21) + 10);
		}
		
		System.out.print(set);
		
//		Iterator<Integer> iter = set.iterator();
//		System.out.printf("오늘의 로또 번호 : [%d", iter.next());
//		while(iter.hasNext()) {
//			int temp = iter.next();
//			System.out.printf(", %d", temp);
//		}
//		System.out.print("]");
	}
}
```

### HashMap

- 같은 것이 들어가면 하나는 아무거로나 변경하고 추가한다. -> 주의!!!!

- 해쉬 테이블 생성 방법

  HashMap<String, Integer> hashtable = new HashMap<String, Integer>();

- 100 개의통으로구성된해쉬테이블생성하기

  HashMap<String, Integer> hashtable = new HashMap<String, Integer>(100);

- **실습8 HashMapLab1**

```java
package day13;
import java.util.*;
public class HashMapLab1 {
	public static void main(String[] args) {
		HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
		Scanner scan = new Scanner(System.in);
		String country;
		int population;
		
		Iterator<String> iter;
		String key;
		int value;

		while(hashMap.size() != 5) {
			System.out.print("나라이름을 입력하세요 : ");
			country = scan.next();
			System.out.print("인구수를 입력하세요 : ");
			population = scan.nextInt();
			
			if(!hashMap.containsKey(country)) {
				hashMap.put(country, population);
				System.out.printf("저장되었습니다.\n");
			}
			else {
				System.out.printf("나라명 %s는 이미 저장되었습니다.\n", country);
			}
		}
		
		iter = hashMap.keySet().iterator();
		System.out.printf("%d개가 모두 입력되었습니다.\n", hashMap.size());
		System.out.printf("입력된 데이터 : ");
		
		while(true) {
			key = iter.next();
			value = hashMap.get(key);
			System.out.printf("%s(%d)", key, value);
			if(iter.hasNext()) System.out.print(", ");
			else break;
		}
		scan.close();
	}
}
```

- **실습9 ListTest**

```java
package day13;

import java.util.*;

class CreateList {
	public ArrayList<Integer> convertList(int arr[]) {
		ArrayList<Integer> arrList = new ArrayList<Integer>();
		for(int i = arr.length - 1; i >= 0; i--) {
			arrList.add(arr[i]);
		}
		return arrList;
	}
}
public class ListTest {
	public static void main(String[] args) {
		CreateList createList = new CreateList();
		int array[] = {3, 4, 2, 5, 2, 3, 6, 7, 5, 7, 9};
		ArrayList<Integer> arrList = new ArrayList<Integer>();
		
		arrList = createList.convertList(array);
		
		for(int arr : arrList) {
			System.out.println(arr);
		}
	}

}
```

