# Day2 JDBC

[JDBC 프로그램의 구현 순서]

1. JDBC Driver 로딩 - Class, forName()

2. DBMS에 접속 - DriverManager.getConnection("*jdbc url", "계정", "암호")

3. Statement/PreparedStatement 객체 생성

4. 처리하려는 기능에 따라서 SQL 문을 전달하고 수행시킨다.

5. 결과 처리

   ResultSet 객체

   next(), getXXX()

   SELECT 명령의 수행 결과 여부에 관계없이 ResultSet 객체는 리턴

6. 종료시 close() 필수

**DatabaseMetaData** - 접속된 DB에 대한 정보, JDBC 드라이버에 대한 정보 추출/체크

**ResultSetMetaData** - SELECT 명령을 수행하고 생성된 ResultSet 객체에 대한 정보를 추출

```java
//ResultSetMetaData 예시
String sql = "select ename, sal, deptno from emp " +
			"where deptno = " + num;
ResultSet rs = stmt.executeQuery(sql);
```

**JDBC 실습1 SelectEmpLab**

[문제]

작성 클래스명 : SelectEmpLab
접속 오라클 계정 : scott

1. scott 계정으로 접속한다.
2. true 와 false 랜덤값을 추출한다.

3. true 이면
   emp 테이블에서 모든 직원들의 이름과 월급, 두 개의 컬럼을 추출한다.
   다음 형식으로 표준 출력한다.

   XXX 직원의 월급은 x,xxx원입니다. 
   XXX 직원의 월급은 x,xxx원입니다.
   XXX 직원의 월급은 xx,xxx원입니다.
         :
4. false 이면
   emp 테이블에서 모든 직원들의 이름과 입사 날짜, 두 개의 컬럼을 추출한다.
   다음 형식으로 표준 출력한다.

   XXX 직원은 xxxx년 xx월 xx일에 입사하였습니다. 
   XXX 직원은 xxxx년 xx월 xx일에 입사하였습니다. 
   XXX 직원은 xxxx년 xx월 xx일에 입사하였습니다. 
         :

```java
// 실습1 SelectEmpLab
package jdbcsrc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Random;

public class SelectEmpLab {

	public static boolean getRandomBoolean() {
		Random random = new Random();
		return random.nextBoolean();
	}

	public static void main(String[] args) {
		try {
			Class.forName("oracle.jdbc.OracleDriver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		String sql = String.format("SELECT ENAME, TO_CHAR(SAL,'999,999,999')||'원' AS SAL FROM EMP");
		String sql2 = String.format("SELECT ENAME, TO_CHAR(HIREDATE, 'yyyy\"년\" mm\"월\" dd\"일\"') AS HIREDATE FROM EMP");
		if (getRandomBoolean() == true) {
			try (Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "scott", "tiger");
					Statement stmt = conn.createStatement();
					ResultSet rs = stmt.executeQuery(sql);) {
				if (rs.next()) {
					do {
						System.out.print(rs.getString("ename") + "\t");
						System.out.print("직원의 월급은" + "\t");
						System.out.print(rs.getString("sal"));
						System.out.print("입니다.");
						System.out.println();
					} while (rs.next());

				} else {
					System.out.println("추출된 행이 없숑!!");
				}
			} catch (Exception e) {
				System.err.println("오류 발생 : " + e);
			}
		} else {
			try (Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "scott", "tiger");
					Statement stmt = conn.createStatement();
					ResultSet rs = stmt.executeQuery(sql2);) {
				if (rs.next()) {
					do {
						System.out.print(rs.getString("ename") + "\t");
						System.out.print("직원은\t");
						System.out.print(rs.getString("HIREDATE"));
						System.out.print("에 입사하였습니다.");
						System.out.println();
					} while (rs.next());

				} else {
					System.out.println("추출된 행이 없숑!!");
				}
			} catch (Exception e) {
				System.err.println("오류 발생 : " + e);
			}
		}
	}
}
```



