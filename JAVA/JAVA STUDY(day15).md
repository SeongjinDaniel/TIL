# Day15

- I18N : 국제화

- 인터넷에서 컨텐츠를 가져오는것을 웹 크롤링이라고 한다.

```java
//실습1 Arrays
package day15;

import java.util.Arrays;
import java.util.List;

public class ArraysTest {

	public static void main(String[] args) {
		int[] ary = { 2, 4, 3, 7, 21, 9, 98, 76, 74 };
		System.out.printf("ary 배열 원소들 : %s\n", Arrays.toString(ary));
		System.out.printf("ary 배열 크기 : %d\n", ary.length);

		Arrays.sort(ary);
		System.out.printf("소트후 ary 배열 원소들 : %s\n", Arrays.toString(ary));

		int idx = Arrays.binarySearch(ary, 21);
		System.out.printf("21 이라는 값이 있는 원소의 인덱스 : %d\n\n", idx);

		int[] copyOfArray = Arrays.copyOf(ary, 11);
		System.out.printf("copyOfArray 배열 크기: %d\n", copyOfArray.length);
		System.out.printf("copyOfArray 배열 원소들 : %s\n\n", Arrays.toString(copyOfArray));

		int[] copyOfRangeArray = Arrays.copyOfRange(ary, 5, 8);
		System.out.printf("copyOfRangeArray  배열 원소들 : %s\n\n", Arrays.toString(copyOfRangeArray));

		int[] fillArray = new int[5];
		System.out.printf("fillArray (before): %s\n", Arrays.toString(fillArray));
		Arrays.fill(fillArray, 1);
		System.out.printf("fillArray (after): %s\n\n", Arrays.toString(fillArray));

		Integer[] objAry = new Integer[ary.length];
		for (int i = 0; i < ary.length; i++)
			objAry[i] = ary[i];
		List<Integer> integerList = Arrays.asList(objAry);
		System.out.printf("리스트 크기 : %d\n", integerList.size());
		System.out.printf("리스트의 원소들 : ");
		for (Integer i : integerList) {
			System.out.printf("%d ", i);
		}
	}
}

```

```java
//실습2 SimpleDateFormatTest
package day15;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatTest {

	public static String timeToStrDate(long time) {
		DateFormat formatter = 
				new SimpleDateFormat("yyyy-MM-dd");
		return formatter.format(time);
	}

	public static Date parseStrDate(String strDate) throws ParseException {
		DateFormat formatter = 
				new SimpleDateFormat("yyyy년 MM월 dd일");
		return formatter.parse(strDate);
	}

	public static void main(String[] args) throws ParseException {
		System.out.println(timeToStrDate(new Date().getTime()));
		System.out.println(parseStrDate("2019년 12월 25일")); 		
	}
}
```

```java
//실습3 AdvancedDateTest
package day15;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class AdvancedDateTest {

	public static void main(String[] args) {
		LocalDate currentDate = LocalDate.now();    // 컴퓨터의의 현재 날짜 정보를 저장한 LocalDate 객체를 리턴한다. 결과 : 2016-04-01 
		LocalDate targetDate = LocalDate.of(2020, 1, 1); // 내가 줄수 있는 년월일의 객체
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd E");
		String text1 = currentDate.format(formatter);
		String text2 = targetDate.format(formatter);
		LocalDate parsedDate = LocalDate.parse("2019 12 25 수", formatter);
		String text3 = parsedDate.format(formatter);
		System.out.println(text1);
		System.out.println(text2);
		System.out.println(text3);
	}

}
```

```java
//실습4 URLTest1
package day15;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public class URLTest1 {
	public static void main(String[] args) throws Exception { // 소극적인 예외처리
		URL url = new URL("https://movie.naver.com/");
		InputStream is = url.openStream();
		// UTF-8을 추가하면 한글이 깨지지 않고 잘 나온다.
		BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
		String line = null;
		while (true) {
			line = br.readLine();
			if (line == null)
				break;
			System.out.println(line);
		}
	}
}
```

```java
//실습4 URLTest2
package day15;

import java.net.*;
import java.io.*;
public class URLTest2 {
	public static void main(String[] args) {
		try {
			URL req = new URL("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168064000");
			InputStream is = req.openStream();
			BufferedReader reader = new BufferedReader(
					                       new InputStreamReader(is, "UTF-8"));
			String lineStr = "";
			while(true) {
				lineStr = reader.readLine();
				if(lineStr == null)
					break;
				System.out.println(lineStr);				
			}			
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		}
	}
}
```

```java
//실습5 URLTest3
package day15;

import java.net.*;
import java.io.*;
public class URLTest3 {
	public static void main(String[] args) {
		try {
			URL req = new URL("http://img.etnews.com/news_ebuzz/afieldfile/2012/01/04/c_bk010101_87984_3.jpg");
			InputStream is = req.openStream();
			FileOutputStream fos = new FileOutputStream("c:/iotest/duke.jpg");
			int input=0;
			while(true) {
				input = is.read();
				if(input == -1)
					break;
				fos.write(input);				
			}
			fos.close();
			System.out.println("duke.jpg가 성공적으로 생성되었습니다.");
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		} 
	}
}
```

```java
//실습6 URLTest4
package day15;

import java.net.*;
import java.io.*;
public class URLTest4 {
	public static void main(String[] args) {
		InputStream is = null;
		BufferedReader reader = null;
		BufferedWriter fw = null;
		try {
			URL req = new URL("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168064000");
			is = req.openStream();
			reader = new BufferedReader(
					                       new InputStreamReader(is, "utf-8"));
			fw = new BufferedWriter(new OutputStreamWriter(
					     new FileOutputStream("c:/iotest/weather.xml"), "utf-8"));
			String lineStr = "";
			while(true) {
				lineStr = reader.readLine();
				if(lineStr == null)
					break;
				fw.write(lineStr+"\r\n");				
			}	
			System.out.println("weather.xml이 성공적으로 생성되었습니다.");
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		}  finally {
			try {
				if (fw != null) 
					fw.close();
				if (reader != null) 
					reader.close();
				if (is != null) 
					is.close();
			} catch (IOException e) {
				e.printStackTrace();
			}			
		}
	}
}
```

- **실습6 문제**

  클래스명 : CopyExam

  제공된 sample.txt 파일을 읽고
  sample_yyyy_mm_dd.txt 파일에 그대로 출력하는 프로그램을
  구현해 봅니다. 이 파일은 append 모드로 오픈하여
  여러번 테스트하면 sample.txt 파일의 내용이 
  sample_yyyy_mm_dd.txt 파일에  계속 추가되게 합니다.

  정상적으로 수행되면 
  화면에 “저장 완료되었습니다.”
  예외 발생시
  화면에 "처리하는 동안 오류가 발생했습니다."
  를 출력하는 프로그램을 구현하여 제출하세요.

```java
//실습6 문제 CopyExam
package day15;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class CopyExam {
	public static String timeToStrDate(long time) {
		DateFormat formatter = new SimpleDateFormat("yyyy_MM_dd");
		return formatter.format(time);
	}

	public static void main(String[] args) {
		String day = timeToStrDate(new Date().getTime());
		String path = "C:/iotest/";
		String newFileName = "sample_" + day + ".txt";
		File isDir = new File(path);
		if (!isDir.exists()) {
			isDir.mkdirs();
		}

		try (FileReader reader = new FileReader("c:/iotest/sample.txt");
				BufferedReader br = new BufferedReader(reader);
				FileWriter writer = new FileWriter(path + newFileName, true);) {

			String data = null;
			while (true) {
				data = br.readLine();
				if (data == null)
					break;

				writer.write(data + "\r\n");
//				System.out.println(data);
			}

			System.out.println("저장 완료되었습니다.");

		} catch (Exception e) {
			System.out.println("처리하는 동안 오류가 발생했습니다.");
		}
	}
}
```

