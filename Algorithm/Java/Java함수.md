# Java 함수



## 배열



### 여러가지 배열 선언

```java
 //int 타입 배열 선언
int[] i_array;
int i_array[]; 
		
//배열 생성후 초기화하면 배열의 주소가 할당된다.
int[] i_array = new int[8]; //초기값 0
String[] s_array = new String[8]; //초기값 ""
		
//배열 선언만 해놓고 나중에 초기화를 시킬수도 있다.
int[] i_array;
i_array = new array[8];
```



### 객체배열 사용법

```java
//길이가 8인 자동차 객체배열 선언
Car [] car = new Car[8];
// 각 배열에는 아직 NULL값만 존재한다.
System.out.println(car[0]);
		
//배열안의 자동차클래스를 초기화시켜주어야한다.
for(int i = 0; i < car.length; i++) {
	car[i] = new Car();
}
		
//배열에 주소값이 제대로 설정된다.
System.out.println(car[0]);
```



### 여러가지 배열 초기화

```java
//배열에 특정값 대입하며 선언
int[] i_array = {1,2,3,4,5};
String[] s_array = {"a","b","c","d"};
		
//배열의 주소를 모두 같은값으로 초기화
Arrays.fill(i_array,1); //i_array의 모든 index값을 1로 초기화
	
//for문을 통해 값을 대입
for(int i = 0;i < i_array.length; i++) {
    i_array[i]=i;
}

//foreach문을 통한 배열출력
for(int i : i_array) {
    System.out.print(i);
}		
```



---

---

