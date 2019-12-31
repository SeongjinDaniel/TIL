# Day1 JDBC

# [JDBC(Java DataBase Connectivity) 프로그래밍]

- Java API

  java.sql

  javaxsql

- DBMS에 무관하게 프로그램을 개발할 수 있다. (JDBC에 가장 큰 장점!!!)

- 구성 : JDBC API     +     JDBC Driver

  ​		  (인터페이스)       (인터페이스들의 구현클래스)

  ​		  DBMS에 무관 	 DBMS에 따라 달라진다.

  - 인터페이스 : 메서드들의 수행 코드는 있으나 데이터는 없다.

팩토리 메서드 : 객체 생성을 대신 해주는 일반 메서드

SQL 명령을 수행시키는 기능을 지원한는 객체 - Statement

​													executeQuery():ResultSet - SELECT

​													executeUpdate():int - 그외의 모든 SQL

Statement stmt = new Statement();  --> X 안됨

Statement stmt = Connection 객체의 createStatement();

-> Statement Factory 메세지를 알아야한다.

- **JDBC 프로그램의 구현 순서**

  1. JDBC Driver 로딩 - Class, forName()

  2. DBMS에 접속 - DriverManager.getConnection(""*jdbc url", "계정", "암호")

  3. Statement/PreparedStatement 객체 생성

  4. 처리하려는 기능에 따라서 SQL 문을 전달하고 수행시킨다.

  5. 결과 처리

     ResultSet 객체

     next(), getXXX() -> column의 type 마다 달라진다!! e.g) getInt, getString, getVarchar

     SELECT 명령의 수행 결과 여부에 관계없이 ResultSet 객체는 리턴

  6. 종료시 close() 필수

JDBC 

![image-20191231155135136](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191231155135136.png)

[URL]

URL - 인터넷 사이트(웹 사이트, 웹 페이지)의 주소 문자열

​		   -----------------------------------------------------------------------------------> http URL

​			Uniform Resource Locator의 약어로 어떤 자원의 위치를 알리는 단일화된(규격화된) 형식의 문자열

프로토콜명 : ........................................

프로토콜 : 통신 규약

http(s)://www.naver.com/

http://www.html5test.com/

http://www.w3schools.com/

http://www.w3.org/

jdbc url : 어떤 DBMS를 어떤 JDBC Driver를 통해서 접속할 것인지 하나의 문자열로 구성

jdbc:DBMS이름:JDBCDriver이름:Driver에서원하는대로

jdbc:oracle:thin:@DBMS네트워크주소



![image-20191231170550398](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191231170550398.png)

![image-20191231170631248](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191231170631248.png)

![image-20191231170652687](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191231170652687.png)

![image-20191231170720811](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191231170720811.png)



```java
	ResultSet rs = stmt.executeQuery(sql); // ************
	// -> 답이 없으면 비어 있는 resultSet이 출려된다. ****************
```
- **실습1 ReadVisitor**

```java
// 실습1
package jdbcsrc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class ReadVisitor {

	public static void main(String[] args) throws Exception{
//		1. JDBC Driver 로딩 - Class, forName()
		// oracle jdbc 대장 클래스를 지정!
		// 임의로 이 루틴을 찾아달라고한것임
		Class.forName("oracle.jdbc.driver.OracleDriver");
//		2. DBMS에 접속 - DriverManager.getConnection("*jdbc url", "계정", "암호")
		Connection conn = DriverManager.getConnection(
							"jdbc:oracle:thin:@localhost:1521:XE", "jdbctest", "jdbctest");
		System.out.println(conn); // Tostring 결과를 확인 할 수 있음
		// -> C:\oraclexe\app\oracle\product\11.2.0\server\jdbc\lib 이곳에 들어가서
		// ojdbc5.jar를 build path에 적용하면된다.
//		3. Statement/PreparedStatement 객체 생성
		Statement stmt = conn.createStatement();
		//-----------
		Scanner scan = new Scanner(System.in);
		System.out.print("검색할 이름을 입력하세요 : ");
		String searchName = scan.nextLine();
		scan.close();
//		4. 처리하려는 기능에 따라서 SQL 문을 전달하고 수행시킨다.
		// 세미콜론 붙이면 안된다 sql명령어만 사용해야한다.
		String sql = "select name, writedate, memo from visitor " +
						"where name = '" + searchName + "'";
		ResultSet rs = stmt.executeQuery(sql); // ************
		// -> 답이 없으면 비어 있는 resultSet이 출려된다. ****************
//		5. 결과 처리
		if(rs.next()) {
			System.out.println(rs.getString("name") + ":"+
					rs.getDate("writedate")+"," + rs.getString("memo"));
		}
		else {
			System.out.println(searchName + "님이 작성한 글이 없습니다.");
		}
		System.out.println("---------------끝------------------");
		rs.close();
		stmt.close();
		conn.close();
	}
}
```

```java
// 실습2 ReadEmp
package jdbcsrc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class ReadEmp {

	public static void main(String[] args) throws Exception{

		Class.forName("oracle.jdbc.driver.OracleDriver");

		Connection conn = DriverManager.getConnection(
							"jdbc:oracle:thin:@localhost:1521:XE", "scott", "tiger");
		System.out.println(conn); // Tostring 결과를 확인 할 수 있음

		Statement stmt = conn.createStatement();
		//-----------
		Scanner scan = new Scanner(System.in);
		System.out.print("검색할 부서번호를 입력하세요 : ");
		String num = scan.nextLine();
		scan.close();

		String sql = "select ename, sal, deptno from emp " +
						"where deptno = " + num;
		ResultSet rs = stmt.executeQuery(sql);
		
		if(rs.next()) {
			do {
				System.out.println(rs.getString("ename") + ":"+
						rs.getInt("sal")+"," + rs.getInt("deptno"));
			}while(rs.next());
		}
		else {
			System.out.println(num + "번 부서에 근무하는 직원이 없습니다.");
		}
		System.out.println("---------------끝------------------");
		rs.close();
		stmt.close();
		conn.close();
	}
}
```

