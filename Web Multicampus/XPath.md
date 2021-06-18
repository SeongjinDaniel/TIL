## XPath

XPath란 XML Path Language를 의미한다. XPath는 XML 문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어이다. XPath는 W3C 표준 권고안으로, XSLT와 XPointer에 사용될 목적으로 만들어졌습니다. 또한, XML DOM에서 노드를 검색할 때에도 사용할 수 있다. 이 책의 예제에서 사용된 XPath 표현식에 대한 소개이다. XPath 표현식에서 EL 변수를 사용할 때는 변수명 앞에 $ 기호를 사용한다.

**XPath**(XML Path Language)는 [W3C](https://ko.wikipedia.org/wiki/W3C)의 표준으로 [확장 생성 언어](https://ko.wikipedia.org/wiki/XML) 문서의 구조를 통해 경로 위에 지정한 구문을 사용하여 항목을 배치하고 처리하는 방법을 기술하는 언어이다. XML 표현보다 더 쉽고 약어로 되어 있으며, XSL 변환([XSLT](https://ko.wikipedia.org/wiki/XSLT))과 XML 지시자 언어([XPointer](https://ko.wikipedia.org/wiki/XPointer))에 쓰이는 언어이다. XPath는 XML 문서의 노드를 정의하기 위하여 경로식을 사용하며, 수학 함수와 기타 확장 가능한 표현들이 있다.

```
<wikimedia>
  <projects>
    <project name="Wikipedia" launch="2001-01-05">
      <editions>
        <edition language="English">en.wikipedia.org</edition>
        <edition language="German">de.wikipedia.org</edition>
        <edition language="French">fr.wikipedia.org</edition>
        <edition language="Polish">pl.wikipedia.org</edition>
      </editions>
    </project>
    <project name="Wiktionary" launch="2002-12-12">
      <editions>
        <edition language="English">en.wiktionary.org</edition>
        <edition language="French">fr.wiktionary.org</edition>
        <edition language="Vietnamese">vi.wiktionary.org</edition>
        <edition language="Turkish">tr.wiktionary.org</edition>
      </editions>
    </project>
  </projects>
</wikimedia>
```

포함관계에 한에서 부모 자식관계가 생성되니까 이것을 이용해서 사용한다.

아래의 XPath 식은

```
/wikimedia/projects/project/@name
```

모든 project 요소의 name 속성을 선택하고, 아래의 XPath 식은

```
/wikimedia/projects/project/editions/edition[@language="English"]/text()
//edition[@language="English"]         // 이 문자는 어떤 부모가 있던 간에 라는 뜻
/wikimedia//edition[@language="English"]       // 이문자를 중간에 사용해도된다.
```

모든 영문 Wikimedia 프로젝트의 주소(`language` 속성이 *English*인 모든 `edition` 요소의 문자열)를 선택하고, 아래의 XPath 식은

```
/wikimedia/projects/project[@name="Wikipedia"]/editions/edition/text()
```

모든 위키백과의 주소(*Wikipedia*의 이름 특성을 가진 `project` 요소 아래에 존재하는 모든 `edition` 요소의 문자열)를 선택한다.

Xpath는 속성명을 주려면 @문자를 사용해야한다. 

------------

\<abc\>

​	ㅋㅋㅋ

​	\<def\>MMM\</def\>

​	ㅠㅠㅠ

\</abc\>

------

