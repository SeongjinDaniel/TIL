# Mybatis Day2

1. DB 서버를 직접 구현하는 것이 아니라 Mybatis 전체 Tool이 대신해준다.
2. return 값은 List 타입이다.
3. 

```java
package model.dao;

import java.io.InputStream;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import model.vo.VisitorVO;

public class VisitorMybatisDAO {	
	final String resource = "resource/mybatis-config.xml"; // src 폴더 기준 -> 반드시 src 밑에 있어야 읽을수있다.
	public List<VisitorVO> listAll() {
		System.out.println("Mybatis 를 사용 DB 연동-listAll");
		List<VisitorVO> list = null;		
		SqlSession session = null;
		try {			
			InputStream inputStream = 
					Resources.getResourceAsStream(resource);
			SqlSessionFactory sqlSessionFactory = 
					new SqlSessionFactoryBuilder().build(inputStream);
			session = sqlSessionFactory.openSession();
			String statement = "resource.VisitorMapper.selectVisitor"; // resource.VisitorMapper : namespace
			list = session.selectList(statement);
			System.out.println(session.getClass().getName());		
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			session.close();
		}
		return list;
	}
	public List<VisitorVO> search(String keyword) {
		System.out.println("Mybatis 를 사용 DB 연동-search");
		List<VisitorVO> list = null;
		SqlSession session = null; 
		try {			
			InputStream inputStream = Resources.getResourceAsStream(resource);
			SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
			session = sqlSessionFactory.openSession();
			String statement = "resource.VisitorMapper.searchVisitor";
			list = session.selectList(statement, keyword);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			session.close();
		}
		return list;		
	}

	public boolean insert(VisitorVO vo) {
		System.out.println("Mybatis 를 사용 DB 연동-insert");
		boolean result = false;
		SqlSession session = null;
		try {
			InputStream inputStream = 
					Resources.getResourceAsStream(resource);
			SqlSessionFactory sqlSessionFactory = 
					new SqlSessionFactoryBuilder().build(inputStream);
			session = sqlSessionFactory.openSession(true);
			String statement = "resource.VisitorMapper.insertVisitor";
			if(session.insert(statement, vo) == 1) // return 값이 1이 이니면 error	
				result = true;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(session != null)
				session.close();
		}
		return result;
	}	
}

```

```java
package controller;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.dao.VisitorDAO;
import model.dao.VisitorMybatisDAO;
import model.vo.VisitorVO;
@WebServlet("/visitormybatis")
public class VisitorServletDB2 extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String keyword = request.getParameter("keyword");
		
		VisitorMybatisDAO dao = new VisitorMybatisDAO();
		if(keyword == null) {
			List<VisitorVO> list = dao.listAll();
			for(VisitorVO vo : list) {
				System.out.println(vo.getMemo());
			}
			request.setAttribute("list", list);
		} else {
			List<VisitorVO> list = dao.search(keyword);
			if(list.size() == 0) {
				request.setAttribute("msg", keyword+"를 담고있는 글이 없어용(mybatis)");
			} else {
				request.setAttribute("list", list);
			}
		}
		request.getRequestDispatcher("/jspexam/visitorView.jsp")
        .forward(request, response);
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");		
		String name = request.getParameter("name");
		String memo = request.getParameter("content");
		VisitorMybatisDAO dao = new VisitorMybatisDAO();
		VisitorVO vo = new VisitorVO();
		vo.setName(name);
		vo.setMemo(memo);
		boolean result = dao.insert(vo);
		if(result) {
			request.setAttribute("msg", name+"님의 글이 성공적으로 입력되었어요!!..(mybatis)");
		} else {
			request.setAttribute("msg", name+"님의 글이 입력에 실패했어요!!(mybatis)");
		}
		request.getRequestDispatcher("/jspexam/visitorView.jsp")
		           .forward(request, response);
	}
}

```

- **명령어 종류**  : 데이터 조작어(DML :  Data Manipulation Language)

  **명령어** : SELECT 

  - **설명** : 데이터베이스에 들어 있는 데이터를 조회하거나 검색하기 위한 명령어를 말하는 것으로 RETRIEVE 라고도 함

  **명령어** : INSERT, UPDATE, DELETE 

  - **설명** : 데이터베이스의 테이블에 들어 있는 데이터에 변형을 가하는 종류(데이터 삽입, 수정, 삭제)의 명령어들을 말함. 

----------

- **명령어 종류**  : 데이터 정의어(DDL : Data Definition Language)

  **명령어** : CREATE, ALTER, DROP, RENAME, TRUNCATE 

  **설명** : 테이블과 같은 데이터 구조를 정의하는데 사용되는 명령어들로 (생성, 변경, 삭제, 이름변경) 데이터 구조와 관련된 명령어들을 말함.

-------

- **명령어 종류**  : 데이터 제어어(DCL : Data Control Language) 

  **명령어** : GRANT, REVOKE

  - **설명** : 데이터베이스에 접근하고 객체들을 사용하도록 권한을 주고 회수하는 명령어들을 말함.

---------

**명령어 종류** : 트랜잭션 제어어(TCL : Transaction Control Language)

- **명령어** : COMMIT, ROLLBACK, SAVEPOINT 

  **설명** : 논리적인 작업의 단위를 묶어서 DML에 의해 조작된 결과를 작업단위(트랜잭션) 별로 제어하는 명령어를 말함.



### Spring MVC 프로젝트에서도 Mybatis 를 사용해 보자.

1. pom.xml 에 다음 태그 추가하기

```xml
<dependency>
    <groupId>com.jslsolucoes</groupId>
    <artifactId>ojdbc6</artifactId>
    <version>11.2.0.1.0</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.0.2.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.4.1</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.3.2</version>
</dependency>
```

2. servlet-context.xml 에 다음 태그 추가하기

```xml
<beans:bean id="dataSource" 
	class="org.springframework.jdbc.datasource.DriverManagerDataSource">
<beans:property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"/>
		<beans:property name="url" value="jdbc:oracle:thin:@localhost:1521:XE" />
		<beans:property name="username" value="jdbctest" />
		<beans:property name="password" value="jdbctest" />		
</beans:bean>
	
<beans:bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">	
		<beans:property name="dataSource" ref="dataSource"/>
		<beans:property name="configLocation" 
			value="classpath:/resource/mybatis-config.xml"/>
		<beans:property name="mapperLocations" 
			value="classpath:/resource/*Mapper.xml"/> 	<!-- classpath -> source 폴더에 : src/main/java, *Mapper.xml : Mapper라고 쓰여지모든것을 읽음-->
</beans:bean> 

<beans:bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate"  
destroy-method="clearCache">
		<beans:constructor-arg index="0"  ref="sqlSessionFactory" />
</beans:bean>

```

sqlSession객체를 spring이 알아서 생성