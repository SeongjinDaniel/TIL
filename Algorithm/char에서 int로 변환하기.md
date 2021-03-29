# char에서 int로 변환하기

숫자 CHAR(0~9)는 ASCII 코드 48부터 시작하므로, 48을 빼주면 숫자를 얻을 수 있다.

```java
char ch = '3'; 
int n = 0; 
n = ch - 48;
```

하지만, 아래와 같이 하는 편이 더욱 직관적이다.

```java
char ch = '3';
int n = 0; 
n = ch - '0';
```

