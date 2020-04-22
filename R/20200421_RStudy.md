# 20200421 R Study (R & Java 연동)



[ Java와 R 연동 테스트용 프로젝트 생성 ]
(1) redu 라는 Spring MVC Project 을 생성한다.
    중간에 입력하는 top-level 패키지명 : edu.spring.redu
(2) pom.xml 에서 3페이지에 있는 <dependency> 태그 추가하기
     Rserve 를 사용하기 위해 API 설치를 위해서 하는 거임
(3) pom.xml 에서 Java 버전과 Spring 버전 정보 수정하기
     project facet 도 수정한다. Java 1.8 로....
(4) Query 문자열 추출시 한글 문제가 해결되도록 환경 설정 추가하기
     --> web.xml에 한글처리 필터 클래스 등록
(5) 소스 내용을 검토하고 servlet-context.xml 에 
     component-scan 태그를 추가한다.
	<context:component-scan base-package="rtest" />	
	<context:component-scan base-package="service" />

------

[ Rserve 기동 ] (1) RStudio 에서 기동시키기

 Rserve(args="--RS-encoding utf8") 

(2) CMD 창에서 단독으로 기동시키기(단독 기동 가능, 오류 메시지 확인 장점) C:\Users\student\Documents\R\win-library\3.6\Rserve\libs\x64(윈도우10) 

C:\Program Files\R\R-3.6.1\library\Rserve\libs\x64(윈도우7)의 모든 파일을 

C:\Program Files\R\R-xxxx\bin\x64 디렉토리에 복사한 후에

cmd 창을 띄우고 C:\Program Files\R\R-xxxx\bin\x64 

디렉토리에 가서 다음 명령을 수행시킨다. 

`C:\Program Files\R\R-3.6.3\bin\x64` -> 내 컴퓨터 route

**Rserve --RS-encoding utf8**



--> R Server 기동 완료!!! 

--------

```R
install.packages("Rserve")
library(Rserve)
```



-----------

pom_xml파일에추가

```xml
<dependency>
			<groupId>com.github.lucarosellini.rJava</groupId>
			<artifactId>JRIEngine</artifactId>
			<version>0.9-7</version>
		</dependency>
		<dependency>
			<groupId>net.rforge</groupId>
			<artifactId>Rserve</artifactId>
			<version>0.6-8.1</version>
		</dependency>
```

#### RServeExmple.java

Java Resouces -> rjavaapp 패키지 추가

```java
package rjavaapp;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.RList;
import org.rosuda.REngine.Rserve.RConnection;
import org.rosuda.REngine.Rserve.RserveException;

public class RServeExample {
	public static void getString() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		String s = "가나다";
		// java의 특정 변수 값을 r에 대입
		// 첫번째 아규먼트 : r 변수를 준다. , 두번째 아규먼트 x변수에 s를 대입(할당할 값)
		rc.assign("x", s);
		// y라는 객체를 새로 만들면서 s값을 넣어준다. // 위 rc.assign과 같다.
		rc.eval("y<- '" + s + "'");
		rc.eval("if(x == '가나다') print('XXX')");
		rc.eval("if(y == '가나다') print('YYY')");
		// assign쓸때는 이방법을 사용
		rc.eval("Encoding(x)<- 'UTF-8'");
		// eval에서 대입해서 쓸때는 이방법을 사용
		rc.eval("y<-iconv(y, 'CP949', 'UTF-8')");
		//rc.eval 안에 있는 것들은 R code이다.
		// R.version.string : string에 version 정보를 가지고 있다. R version 정보를 가지고있다.
		// java에서 r의 값들을 가져올때는 REXP변수를 사용해야한다.
		REXP x = rc.eval("paste(R.version.string,x,y)");
		// x 변수를 String으로 사용할때는 as.String을 사용하면 된다.
		System.out.println("R 버전 정보 : " + x.asString());
		rc.close();
	}

	public static void getInteger() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("length(LETTERS)");
		System.out.println("알파벳 갯수 : " + x.asInteger());
		rc.close();
	}

	public static void getDoubles() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("rnorm(20)");
		double[] d = x.asDoubles();
		for (int i = 0; i < d.length; i++) {
			System.out.println(d[i]);
		}
		rc.close();
	}

	public static void getIntegers() throws REngineException, REXPMismatchException {
		RConnection rc = new RConnection();
		int[] dataX = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		rc.assign("x", dataX);
		rc.eval("y <- x + 10");
		int[] resultX = rc.eval("y").asIntegers();
		for (int i = 0; i < resultX.length; i++) {
			System.out.println(resultX[i]);
		}
		rc.close();
	}

	public static void getDataFrame1() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("d<-data.frame(LETTERS[11:20],c(11:20), stringsAsFactors=F)");
		RList list = x.asList();
		int v_size = list.size();
		int d_length = list.at(0).length();
		System.out.println("데이터(관측치)의 갯수 : " + d_length);
		System.out.println("변수의 갯수 : " + v_size);

		int arrayRows = v_size;
		int arrayCols = d_length;
		String[][] s = new String[arrayRows][]; // 데이터프레임의 변수 갯수로 행의 크기를 정한다.

		for (int i = 0; i < arrayRows; i++) {
			s[i] = list.at(i).asStrings();
		}

		for (int i = 0; i < arrayRows; i++) {
			for (int j = 0; j < arrayCols; j++) {
				System.out.print(s[i][j] + "\t");
			}
			System.out.println();
		}
		rc.close();
	}

	public static void getDataFrame2() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("imsi<-source('C:/Oliver/Rstudy/rjavatest.R'); imsi$value");
		RList list = x.asList();

		String pid = list.at("product").asString();
		System.out.print("PID : " + pid);

		int clickcount = list.at("clickcount").asInteger();
		System.out.println("\tCLICKCOUNT : " + clickcount);
		rc.close();
	}

	public static void main(String[] args) throws REXPMismatchException, REngineException {
		System.out.println("------------ R에서 버젼정보 가져오기 --------------");
		RServeExample.getString();
		System.out.println("------------ R에서 정수 데이터 가져오기 --------------");
		RServeExample.getInteger();
		System.out.println("------------ R에서 더블 데이터들 가져오기 -------------");
		RServeExample.getDoubles();
		System.out.println("------------  R에서 데이터 주입 연산후 가져오기 ------");
		RServeExample.getIntegers();
		System.out.println("------------  R에서 데이터 생성(데이터 프레임) 연산후 가져오기------");
		RServeExample.getDataFrame1();
		System.out.println("------------ R에서 데이터 프레임 가져오기 --------------");
		RServeExample.getDataFrame2();

	}
}
```

----

#### R 예제

```R
library(dplyr)
pdf <- read.table("C:/Oliver/Rstudy/data/product_click.log")
names(pdf) <- c("logdate", "product")
pdf <- pdf %>% select(product) %>% group_by(product) %>% summarise(clickcount = n()) %>% arrange(desc(clickcount)) %>% head(1)
pdf <- as.data.frame(pdf)
pdf
str(pdf)
```

#### JAVA 예제

```java
package rjavaapp;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.RList;
import org.rosuda.REngine.Rserve.RConnection;
import org.rosuda.REngine.Rserve.RserveException;

public class RServeExample {
	public static void getString() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		String s = "가나다";
		// java의 특정 변수 값을 r에 대입
		// 첫번째 아규먼트 : r 변수를 준다. , 두번째 아규먼트 x변수에 s를 대입(할당할 값)
		rc.assign("x", s);
		// y라는 객체를 새로 만들면서 s값을 넣어준다. // 위 rc.assign과 같다.
		rc.eval("y<- '" + s + "'");
		rc.eval("if(x == '가나다') print('XXX')");
		rc.eval("if(y == '가나다') print('YYY')");
		// assign쓸때는 이방법을 사용
		rc.eval("Encoding(x)<- 'UTF-8'");
		// eval에서 대입해서 쓸때는 이방법을 사용
		rc.eval("y<-iconv(y, 'CP949', 'UTF-8')");
		//rc.eval 안에 있는 것들은 R code이다.
		// R.version.string : string에 version 정보를 가지고 있다. R version 정보를 가지고있다.
		// java에서 r의 값들을 가져올때는 REXP변수를 사용해야한다.
		REXP x = rc.eval("paste(R.version.string,x,y)");
		// x 변수를 String으로 사용할때는 as.String을 사용하면 된다.
		System.out.println("R 버전 정보 : " + x.asString());
		rc.close();
	}
	
	// 예외처리 해주지 않으면 에러난다.
	public static void getInteger() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("length(LETTERS)");
		System.out.println("알파벳 갯수 : " + x.asInteger());
		rc.close();
	}

	public static void getDoubles() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		// 20개의 난수를 추출해준다.
		REXP x = rc.eval("rnorm(20)");
		double[] d = x.asDoubles();
		for (int i = 0; i < d.length; i++) {
			System.out.println(d[i]);
		}
		rc.close();
	}

	public static void getIntegers() throws REngineException, REXPMismatchException {
		RConnection rc = new RConnection();
		int[] dataX = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		rc.assign("x", dataX);
		rc.eval("y <- x + 10");
		int[] resultX = rc.eval("y").asIntegers();
		for (int i = 0; i < resultX.length; i++) {
			System.out.println(resultX[i]);
		}
		rc.close();
	}

	public static void getDataFrame1() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("d<-data.frame(LETTERS[11:20],c(11:20), stringsAsFactors=F)");
		RList list = x.asList();
		int v_size = list.size();
		int d_length = list.at(0).length();
		System.out.println("데이터(관측치)의 갯수 : " + d_length);
		System.out.println("변수의 갯수 : " + v_size);
		System.out.println(list);
		System.out.println(list.at(0));
		System.out.println(list.at(1));

		// 위에 코드를 2차원으로 변경 여기서는 2행 10열으로 선언!!
		// 변수값이 같아야하니까 String으로!!
		int arrayRows = v_size;
		int arrayCols = d_length;
		String[][] s = new String[arrayRows][]; // 데이터프레임의 변수 갯수로 행의 크기를 정한다.

		for (int i = 0; i < arrayRows; i++) {
			s[i] = list.at(i).asStrings();
		}

		for (int i = 0; i < arrayRows; i++) {
			for (int j = 0; j < arrayCols; j++) {
				System.out.print(s[i][j] + "\t");
			}
			System.out.println();
		}
		rc.close();
	}

	public static void getDataFrame2() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		// source는 r 코드를 행단위로 실행한다., 
		// imsi$value : source로 return된 값에서 결과 값을 읽어 오겠다 할 때 이렇게 사용하면 된다.
		REXP x = rc.eval("imsi<-source('C:/Oliver/Rstudy/rjavatest.R'); imsi$value");
		RList list = x.asList();

		String pid = list.at("product").asString();
		System.out.print("PID : " + pid);

		int clickcount = list.at("clickcount").asInteger();
		System.out.println("\tCLICKCOUNT : " + clickcount);
		rc.close();
	}

	public static void main(String[] args) throws REXPMismatchException, REngineException {
		System.out.println("------------ R에서 버젼정보 가져오기 --------------");
		RServeExample.getString();
		System.out.println("------------ R에서 정수 데이터 가져오기 --------------");
		RServeExample.getInteger();
		System.out.println("------------ R에서 더블 데이터들 가져오기 -------------");
		RServeExample.getDoubles();
		System.out.println("------------  R에서 데이터 주입 연산후 가져오기 ------");
		RServeExample.getIntegers();
		System.out.println("------------  R에서 데이터 생성(데이터 프레임) 연산후 가져오기------");
		RServeExample.getDataFrame1();
		System.out.println("------------ R에서 데이터 프레임 가져오기 --------------");
		RServeExample.getDataFrame2();

	}
}
```



----

#### 실습

#### R 관련 소스

```R
library(Rserve)
library(KoNLP)

hotel_data <- readLines("C:/Oliver/Rstudy/oliver_txt/hotel.txt")
nouns_data <- extractNoun(hotel_data)
cdata <- unlist(nouns_data)

result_data <- gsub("[^가-힣]", "", cdata)
result_data2 <- Filter(function(x) {nchar(x) >= 2} ,result_data)
# View(result_data2)

wordcount <- table(result_data2) 
top10 <- head(sort(wordcount, decreasing=T),10)
# str(top10)
# View(top10)

result <- data.frame(top10)
names(result) <- c('noun', 'count')
result
# result
# str(result)
# real <- result$"result_data2"

# str(result$"result_data2")
# View(top10$"result_data2")

```

#### Java JavaRLab1.java 실습

```java
package rjavaapp;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.Rserve.RConnection;
import org.rosuda.REngine.Rserve.RserveException;
//클래스명 : JavaRLab1
//구현 기능 : R 코드로 제시된 hotel.txt를 읽고 제일 많이 나온 명사 10개를 
//     Java 코드로 전달하여 
//             다음과 같이 Java 코드로 출력한다.

//     R 이 보내온 최빈 명사들 : xxx, xxx, xxx, xxx ...., xxx

public class JavaRLab1 {
	public static void getResult() throws RserveException, REXPMismatchException {
//		System.out.println("start");
		RConnection rc = new RConnection();

		rc.eval("library(Rserve)");
		rc.eval("library(KoNLP)");
		rc.eval("hotel_data <- readLines(\"C:/Oliver/Rstudy/oliver_txt/hotel.txt\")");
		rc.eval("nouns_data <- extractNoun(hotel_data)");
		rc.eval("cdata <- unlist(nouns_data)");
		rc.eval("result_data <- gsub(\"[^가-힣]\", \"\", cdata)");
		rc.eval("result_data2 <- Filter(function(x) {nchar(x) >= 2} ,result_data)");
//		rc.eval("View(result_data2)");
		rc.eval("wordcount <- table(result_data2)");
		rc.eval("top10 <- head(sort(wordcount, decreasing=T),10)");
		rc.eval("result <- data.frame(top10)");
		rc.eval("real <- result$\"result_data2\"");
		
//		rc.eval("top<-iconv(real, 'CP949', 'UTF-8')");
		
		REXP result = rc.eval("real");
		String[] top10 = result.asStrings();
		System.out.print("R이 보내온 최빈 명사들 : ");
//		for(String data : top10) {
//			System.out.print(data + ", ");
//			
//		}
		
		for(int i=0; i < top10.length; i++) {
			System.out.print(top10[i]);
			if(i != top10.length - 1) System.out.print(", ");
		}
		
		System.out.println();

		rc.close();
//		System.out.println("end");
	}
	public static void main(String[] args) throws REXPMismatchException, REngineException{
		JavaRLab1.getResult();
	}

}

```

Java JavaRLab2.java 실습

```java
package rjavaapp;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.RList;
import org.rosuda.REngine.Rserve.RConnection;
import org.rosuda.REngine.Rserve.RserveException;

public class JavaRLab2 {
//	클래스명 : JavaRLab2
//	구현 기능 : R 코드로 제시된 hotel.txt를 읽고 제일 많이 나온 명사 10개를 
//	             명칭과 횟수로 구성되는 데이터프레임을 생성해서 
//	             Java 코드로 전달하여 
//	             다음과 같이 Java 코드로 출력한다.
//
//	             R 이 보내온 최빈 명사들 :
//	             xxx  nn
//	             xxx  nn
//				 xxx  nn
	public static void getResult() throws RserveException, REXPMismatchException {
		RConnection rc = new RConnection();
		
		REXP x = rc.eval("imsi<-source('C:/Oliver/Rstudy/lab.R', encoding=\"UTF-8\"); imsi$value");
//		System.out.println(x);
		RList list = x.asList();

		String[] noun = list.at("noun").asStrings();
		int[] count = list.at("count").asIntegers();

		if(noun != null) {
			for(int i = 0; i < noun.length; i++) {
				System.out.print(noun[i] + " ");
				System.out.print(count[i]);
				System.out.println();
			}			
		}
		
		rc.close();
		
	}
	public static void main(String[] args) throws REXPMismatchException, REngineException{
		JavaRLab2.getResult();
	}
}
```

