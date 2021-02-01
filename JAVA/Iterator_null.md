# Iterator null 반환?



null을 반환 할 수 없습니다. 항상 Iterable 유형 (Iterable 인터페이스 구현) 인 클래스의 객체를 반환합니다.

메소드 `iterator()`는 new 키워드를 사용하여 새로운 반복 가능한 객체를 반환하므로 null 가능성이 없습니다. 

`Condition 'iterator != null' is always 'true'`



what's the difference between  Iterator 자체가 null인지 여부를 확인합니다. 기본적으로 기존 컬렉션에서 반복자를 반환하면 `colIter == null` 가 발생하지 않습니다.  모두 Iterator.

`!colIter.hasNext()` 문서에 따라 `colIter == null` 를 리턴하는 Iterator에서 호출 된 메소드입니다.  반복에 `null` 의 후속 호출을 의미하는 더 많은 요소가있는 경우  요소를 반환하고 `colIter.hasNext()` 를 던지지 않습니다. .

true