# ArrayList 정렬

```java
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
list.add(4);
list.add(6);
list.add(2);
list.add(5);

System.out.println("정렬 전  : " + list.toString());
list.sort(null);
System.out.println("오름차순 : " + list.toString());
```

```
정렬 전  : [1, 4, 6, 2, 5]
오름차순 : [1, 2, 4, 5, 6]
```



---



```java
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
list.add(4);
list.add(6);
list.add(2);
list.add(5);
System.out.println("정렬 전  : " + list.toString());
list.sort(Comparator.naturalOrder());
System.out.println("오름차순 : " + list.toString());
```

```
정렬 전  : [1, 4, 6, 2, 5]
오름차순 : [1, 2, 4, 5, 6]
```



---



```java
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
list.add(4);
list.add(6);
list.add(2);
list.add(5);
System.out.println("정렬 전  : " + list.toString());
list.sort(Comparator.naturalOrder());
System.out.println("오름차순 : " + list.toString());
list.sort(Comparator.reverseOrder());
System.out.println("내림차순 : " + list.toString());
```

```
정렬 전  : [1, 4, 6, 2, 5]
오름차순 : [1, 2, 4, 5, 6]
내림차순 : [6, 5, 4, 2, 1]
```



**sort 메소드 파해치기**

우리는 지금까지 java doc을 살펴보며 sort 메소드는 메게변수로 전달되는 Comparator를 통해 값을 비교해 오름차순으로 정렬하며 TimSort 알고리즘을 사용한다는 것을 알았다.

그렇다면 오름차순으로 정렬해주는 Comparator.naturalOrder() 메소드는 어떻게 구현되어 있을까?

궁금하면 직접 까봐야 직성이 풀리기 때문에 판도라의 상자를 열어보았다.

(jdk설치경로/src.zip에 자바 소스코드가 모두 들어있다.)

```java
@Override
public int compare(Comparable<Object> c1, Comparable<Object> c2) {
return c1.compareTo(c2);
}
```

해당 메소드는 java/utill/Comparators.java 파일에 들어있다.

간단한 형태이며, c1과 c2를 비교해 작은 값을 맨 앞으로 배치시키는 듯 하다.

여기서 한가지 알 수 있는 사실은 compareTo 메소드를 활용한다는 점이다.

그렇기 때문에 해당 interface 메소드를 가지고있는 interface class인 Comparable을 implements한 object만 sort의 사용이 가능하다는 것이다.

그렇다면, 반대로 내림차순으로 list를 정렬해주는 Comparator.reserveOrder() 의 원형은 어떨까?

```java
public int compare(Comparable<Object> c1, Comparable<Object> c2) {
    return c2.compareTo(c1);
}
```

naturalOrder()와 비슷하지만 compareTo 메소드를 부르는 오브젝트의 순서가 다르다.

이는 오름차순에서 사용된 "크다"의 의미가 "작다"로 바뀐다는 것이며, 큰수가 맨 앞으로 오도록 정렬하게 해준다.



#### 참고

- https://manorgass.tistory.com/60