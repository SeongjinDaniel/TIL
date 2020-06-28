# AssertJ

- [공식문서 핵심 챕터](http://joel-costigliola.github.io/assertj/assertj-core.html)

#### AssertJ란 무엇인가

AssertJ는 많은 assertion(직역: 주장, 행사)을 제공하는 자바 라이브러리이다. 에러 메세지와 테스트 코드의 가독성을 매우 높여주고 각자 좋아하는 IDE에서 쓰기 굉장히 쉽다.

junit에서 제공하는 assertEquals에 비해 훨씬 가독성이 올라간다. junit의 assertEquals의 인자순서는 헷갈릴 가능성이 크다.

```
assertEquals(expected, actual);

assertThat(actual).isEqualTo(expected);
```

밑의 코드가 AssertJ의 assertThat이다. 왼쪽에서 오른쪽으로 자연스럽게 읽히는 것을 알 수 있다.



##### A Simple Example (아주 간단한 예제)

```
@Test void a_few_simple_assertions() { 
assertThat("The Lord of the Rings").isNotNull() 
                                    .startsWith("The") 
                                    .contains("Lord") 
                                    .endsWith("Rings"); 
}
```

설명이 필요없을 정도로 직관적이다. 저 "The Lord of the Rings"라는 문자열이 널이 아니고 The로 시작하며 Lord를 포함하고 Rings로 끝난다라고 바로 알 수 있다.



##### Assertion description (Assertion 설명)

assertion이 수행될 때 상황을 설명하는 것이 중요할 때가 있다. 특히 boolean assertion의 경우에 그렇다.

as라는 메서드로 지정을 할 수가 있는데 assertion이 수행되기 **전에** 작성해야 한다.

```java
TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, Race.HOBBIT);
// 실패하는 테스트 예시 그리고 중요한 것은 as()를 assertion이전에 호출해야 한다!
assertThat(frodo.getAge()).as("check %s's age", frodo.getName())
    						.isEqualTo(100);
```



##### Filtering assertions - iterables나 arrays에 적용되는 filtering

특정 filter를 자바 람다식을 이용하여 표현할 수 있는 유용한 기능이다. 예제코드를 직접 작성해 보았다.

```java
@Test
void filter_test() {
    List<Human> list = new ArrayList<>();
    Human kim = new Human("Kim", 22);
    Human park = new Human("Park", 25);
    uman lee = new Human("Lee", 22);
    Human amy = new Human("Amy", 25);
    Human jack = new Human("Jack", 22);
    
    list.add(kim); 
    list.add(park);
    list.add(lee); 	
    list.add(amy);
    list.add(jack);
    
    assertThat(list).filteredOn(human -> human.getName().contains("a"))
        			.containsOnly(park, jack); }

```





출처: https://pjh3749.tistory.com/241 [JayTech의 기술 블로그]

