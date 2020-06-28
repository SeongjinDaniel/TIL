# Java9



java용 REPL, JShell, JVM Logging 등장





#### 3. 다이아몬드 연산자(Diamond Operator)

Java7 에는 코드를 보다 읽기 쉽게 만드는데 도움되는 Diamond Operator라는 새로운 기능이 있었지만 익명 클래스(Anonymous Inner Class)에는 제한적이었다. ‘<>’(다이몬드 연산자)는 다음과 같은 코드를 작성하는 경우 익명 클래스와 함께 사용할 수 없다. - 컴파일 오류남.



```java
MyHandler<Integer> intHandler = new MyHandler<>(10){// Anonymous Class };
MyHandler<?> handler = new MyHandler<>("Onehundred"){// Anonymous Class };
```

Java 9는 익명 클래스에 대한 Diamond Operator를 허용한다.

```java
MyHandler<Integer> intHandler = new MyHandler<>(1){
    @Override
    public void handle(){
        // handling code...
    }
};
MyHandler<? extends Integer> intHandler1 = new MyHandler<>(10){
    @Override
    void handle(){
        // handling code...
    }
};
MyHandler<?> handler = new MyHandler<>("One hundred"){
    @Override
    void handle(){
        // handling code...
    }
};
```

