# equals() & equalsIgnoreCase() & compareTo() & compareToIgnoreCase() & matches()



equals() 메소드는 대소문자를 구분하여 비교하고

equalsIgnoreCase() 메소드는 대소문자를 구분하지 않고 비교하므로

원하는 비교 형태를 확인하시고 선택 / 사용하면 더욱 유용합니다.



equals(), equalsIgnoreCase() 메소드 이외에도 

String 클래스에서 제공해주는 다양한 메소드를 활용할 수도 있습니다.

```java
// compareTo(), compareToIgnoreCase()
System.out.println(str2.compareToIgnoreCase(str3) == 0);    // true
        
// matches(regex)
System.out.println(str2.matches(str3));    // true
```

두 문자열의 길이가 같은지, 각각의 순서에 맞게 char 로 비교한 결과를 리턴하는

compareTo(), compareToIgnoreCase() 메소드는 두 문자열이 같다면 0 를 반환하게 됩니다.

또한 matches() 메소드는 파라미터로 정규식(regex) 를 입력받아, 문자열이 정규식과 일치하는지 확인하는 데 사용되지만 위에서와 같이 문자열 비교에도 이용할 수 있습니다.



#### 참조

- https://library1008.tistory.com/37