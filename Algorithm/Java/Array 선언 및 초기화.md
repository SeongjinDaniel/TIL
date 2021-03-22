# 배열 선언 및 초기화



```java
//타입[] 변수명으로 선언
int [] numberArray;


//타입 변수명 [] 으로 선언
int numberArray[];


//특정 값 대입하며 배열 선언
int [] intArray = { 1, 2, 3, 4 };
int [] intArray = new int [] { 1, 2, 3, 4 };


//객체이므로 doubleArray에는 null이 대입된다.
double [] doubleArray;


//배열 생성해 할당하면(초기화) 배열의 주소가 들어가게 된다.
doubleArray = new double[10];


//Boolean 형태로 배열을 선언하고 초기화하는 예제
boolean [] bitList;
bitList = new boolean[10]; //기본값으로 초기화
Arrays.fill(bitList, false); //특정 값으로 초기화


//배열의 길이
bitList.length // 10
```

 

**배열을 주소형태로 파라메터값으로 넘기기**

C언에서는 파라메터로 배열 등의 포인터를 전달해줄 수 있는데, 마찬가지로 동일하게 자바에서도 파라메터로 주소값을 넘길 수 있다.