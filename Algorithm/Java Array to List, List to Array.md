# Java Array to List, List to Array



## Array to List

```JAVA
String[] stringArray = {"a", "b", "c"};
        // java.util.Arrays.ArrayList != java.util.ArrayLit, Arrays.ArrayList는 불변한 리스트를 리턴한다. add() 메소드 사용불가
        List<String> stringList = Arrays.asList(stringArray);  // stringList는 고정길이 값을 가지게 된다(불변). add() 메소드 사용불가
        List<String> stringList2 = Arrays.asList(new String[]{"a", "b", "c"}); // stringList는 고정길이 값을 가지게 된다(불변). add() 메소드 사용불가
        // add()메소드를 사용하려면, new ArrayList 생성자를 이용한다.
        ArrayList<String> arrayStringList = new ArrayList<>(Arrays.asList(stringArray));
        List<String> arrayStringList2 = new ArrayList<>(Arrays.asList(stringArray));
        int[] intArray = {1, 2, 3, 4};
        // List<Integer> integerList = Arrays.asList(intArray); //  컴파일 불가, List는 기본형(primitive)타입은 지원하지 않음
        // java 1.8 이후 버전에서는 stream을 이용하여 변환가능하다.
        // boxed()는 int, long, double 기본형 타입을 각각 Integer, Long, Double 타입으로 변환하여 리턴한다.
        List<Integer> intList = Arrays.stream(intArray).boxed().collect(Collectors.toList());
        Integer[] integerArray = {1, 2, 3, 4};
        List<Integer> integerList = Arrays.asList(integerArray); // 사용가능
```



## List to Array

```JAVA
 // List to Array
List<String> stringList3 = Arrays.asList("a", "b", "c");
String[] stringArray3 = stringList3.toArray(new String[stringList3.size()]);
// 위의 stringArray3을 풀어쓴 것. List.toArray(array)는 array에 리스트 값을 채우는 메소드이다.
String[] stringArray4 = new String[stringList3.size()];
stringList3.toArray(stringArray4);
// String to Char Array
String str = "abc";
char[] charArray = str.toCharArray();
// Integer List to int Array
List<Integer> integerList = Arrays.asList(1, 2, 3);
int[] intArrays = integerList.stream().mapToInt(Integer::intValue).toArray();
```

