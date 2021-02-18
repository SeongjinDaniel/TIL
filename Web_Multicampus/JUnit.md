# JUnit

- Java 언어를 위한 테스트 프레임워크이다 . JUnit 를 사용하면 클래스에 구현된 메서드가 주어진 기
  능을 제대로 수행하는지 단위테스트를 처리할 수 있다 .
- 메서드 이름을 가지고 순서대로 실행한다.

- VO 클래스 만들때 가급적이면 ToString 함수 오버라이딩 할것!

```java
package model.dao;

import java.util.List;
import org.junit.jupiter.api.Test;
import model.vo.VisitorVO;
import static org.junit.jupiter.api.Assertions.*;
import static java.lang.System.out;

class VisitorDAOTest {

	@Test
	void test() {
		VisitorDAO dao = new VisitorDAO(); // 같은 package 안에 있으니 import 필요없음
		List<VisitorVO> list = dao.listAll();
		System.out.println(list.size());
		for(VisitorVO vo : list) {
			System.out.println(vo); // 자동으로 ToString함수 호출
		}
	}
	
	@Test
	void test1() {
		System.out.println("검색 기능 테스트");
		VisitorDAO dao = new VisitorDAO(); // 같은 package 안에 있으니 import 필요없음
		List<VisitorVO> list = dao.search("목요일");
		System.out.println(list.size());
		for(VisitorVO vo : list) {
			System.out.println(vo); // 자동으로 ToString함수 호출
		}
	}
	
	@Test
	void test2() {
		System.out.println("삽입 테스트");
		VisitorDAO dao = new VisitorDAO(); // 같은 package 안에 있으니 import 필요없음
		VisitorVO vo = new VisitorVO();
		vo.setName("희동이ㅎㅎㅎㅎㅎㅎ");
		vo.setMemo("~~~오늘은 그냥 금요일~~~");
		boolean result = dao.insert(vo);
		if(result)
				System.out.println("삽입 성공");
		else fail("삽입실패");
	}

}
```