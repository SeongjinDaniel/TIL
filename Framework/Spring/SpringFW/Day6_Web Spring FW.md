# Spring Day6

#### 실습 문제

**[ @ResponseBody** **실습 ]**

**(1)** **다음 내용을 보관할 수 있는 TeamMemberVO 클래스를 구현한다.**

​      **String name, String nicName**

**(2)** **다음 내용을 보관할 수 있는 TeamVO 클래스를 구현한다.**

​      **String teamName, List teamMember**

**(3)** **객체 생성시에는 우리 팀원들의 정보로 저장한다.**

​      **/springedu/myteam/xml****로 요청하면 다음과 같이 XML 로 응답 되게 한다.**

​      **![img](file:///C:\Users\student\AppData\Local\Temp\msohtmlclip1\01\clip_image002.jpg)**

​       **/springedu/myteam/json** **로 요청하면 다음과 같이 JSON 로 응답 되게 구현한다.**

​       **![img](file:///C:\Users\student\AppData\Local\Temp\msohtmlclip1\01\clip_image004.jpg)**

**컨트롤러 클래스 이름 : MyTeamController**

**VO** **클래스 2개와 컨트롤러 클래스 1개의 자바 소스를 제출한다.**

```

```

```

```



**enctype**

enctype 속성은 다음 세가지의 값으로 지정될 수 있다.

1. application/www-form-urlencoded

   디폴트값이다. enctype을 따로 설정하지 않으면 이 값이 설정된다. 폼데이터는 서버로 전송되기 전에 URL-Encode 된다.

2. multipart/form-data

   파일이나 이미지를 서버로 전송할 경우 이 방식을 사용한다.

3. text/plain

   이 형식은 인코딩을 하지 않은 문자 상태로 전송한다.

   #### 실습 Fileupload1

```java
package my.spring.springedu;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import vo.FileVO;
@Controller
public class UploadController1 {
	@RequestMapping("/uploadForm1") // 아무 역할이 없고 uploadForm1.jsp쪽으로 넘겨서 uploadForm1.jsp가 응답함
	public void formFile() {
	}
	@RequestMapping("/upload")
	public ModelAndView saveFile(FileVO vo) {	    
	     String fileName =  vo.getUploadFile().getOriginalFilename();
	     byte[] content = null;
	     ModelAndView mav = new ModelAndView();
	     mav.setViewName("uploadForm1");
	     try {
	    	 content =  vo.getUploadFile().getBytes();
	    	 File f = new File("c:/uploadtest/"+fileName);
	    	 if ( f.exists() ) {
	    		 mav.addObject("msg", fileName + " : 파일이 이미 존재해요!!");
	    	 } else {
	    		 FileOutputStream fos = new FileOutputStream(f);
	    		 fos.write(content);
	    		 fos.close();
	    		 mav.addObject("msg", fileName + ": 파일이 저장되었어요!!");
	    	 }
	     } catch (IOException e) {
	    	 e.printStackTrace();
	    	 mav.addObject("msg", "오류가 발생했어요!!");
	     }	    
	    return mav;
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSP Test Example</title>
</head>
<body>
<h2>SpringMVC FileUpload</h2>
<hr>
<%
	if( request.getAttribute("msg") == null ) {
%>
<!-- 파일을 업로드 할때 <form>태그에서 ENCTYPE="multipart/form-data"라는 애트리뷰트를 반드시 써야 한다.
그렇게 하지 않으면 웹 서버로 데이터를 넘길때 파일의 경로명만 전송되고 파일 내용이 전송되지 않기 때문이다.
그리고 이때 METHOD 애트리뷰트에는 'POST' 값을 지정해야 한다. -->

<!-- 하나가 text파일이어도 multipart로 보내야한다. -->
<!-- 이번에 절달하는 쿼리문자열을 여러개의 form-data이다. 라는 뜻 -->
	<form action="/springedu/upload" 
	               enctype="multipart/form-data" method="post"> 
    	<input type="file" name="uploadFile"/>
    	<input type="submit" value="업로드"/>
	</form>
<%
	} else {
%>
	 ${ msg } <!-- 출력 -->
<%
	}
%>
</body>
</html>



```

```java
package vo;

import org.springframework.web.multipart.MultipartFile;

public class FileVO {
	private MultipartFile uploadFile;

	public MultipartFile getUploadFile() {		
		return uploadFile;
	}
	public void setUploadFile(MultipartFile uploadFile) {
		this.uploadFile = uploadFile;
	}
}
```

-------

#### 실습 Fileupload2

```java
package my.spring.springedu;

import java.io.File;
import java.io.IOException;
import java.util.List;

import javax.servlet.ServletContext;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartRequest;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class UploadController2 {
	@Autowired
	ServletContext context; 
	@RequestMapping("/uploadForm2")
	public void formFile() {
	}

	@RequestMapping("/upload2")
	public ModelAndView saveFile(MultipartRequest mreq) { //MultipartRequest 때문에 file이 여러개여도 추출할 수 있다.
		ModelAndView mav = new ModelAndView();
		List<MultipartFile> list = mreq.getFiles("mfile"); // getFiles가 return하는 것은 list이다.
		String resultStr = "";
		String path = "c:/uploadtest/multi";
		File isDir = new File(path);
		if (!isDir.isDirectory()) {
			isDir.mkdirs();
		}
		mav.setViewName("uploadForm2");
		for (MultipartFile mfile : list) {
			String fileName = mfile.getOriginalFilename();
			try {
				File f = new File("c:/uploadtest/multi/" + fileName);
				//String fileInfo = context.getRealPath("/") + "resources/images/"+fileName;
				//File f = new File(fileInfo);
				if (f.exists()) {
					resultStr += fileName + " : 파일이 이미 존재해요!!<br>";
				} else {
					mfile.transferTo(f); // new!!
					resultStr += fileName + " : 파일이 저장되었어요!!<br>";
				}
			} catch (IOException e) {
				e.printStackTrace();
				resultStr += fileName + " : 오류가 발생했어요!!";				
			}
		}
		mav.addObject("msg", resultStr);	
		return mav;
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSP 테스트 예제</title>
</head>
<body>
<h2>SpringMVC FileUpload(Multiple)</h2>
<hr>
<%
	if( request.getAttribute("msg") == null ) {
%>
	<form action="/springedu/upload2" 
	               enctype="multipart/form-data" method="post">
    	<input type="file" name="mfile" multiple/> <!-- 추가 -->
    	<input type="submit" value="파일올리기"/>
	</form>
<%
	} else {
%>
	 ${ msg }
<%
	}
%>
</body>
</html>
```

#### 실습 Fileupload3

```java

```

```jsp

```



#### 실습 Fileupload4

```java
package my.spring.springedu;

import java.io.File;
import java.io.IOException;
import java.util.List;

import javax.servlet.ServletContext;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartRequest;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class UploadController4 {
	@Autowired
	ServletContext context; 
	@RequestMapping("/uploadForm3")
	public String formFile() {
		return "uploadForm2";
	}

	@RequestMapping("/upload3")
	public ModelAndView saveFile(MultipartRequest mreq) {
		ModelAndView mav = new ModelAndView();
		List<MultipartFile> list = mreq.getFiles("mfile");
		String resultStr = "";
		mav.setViewName("uploadForm2");
		for (MultipartFile mfile : list) {
			String fileName = mfile.getOriginalFilename();
			try {
				String fileInfo = context.getRealPath("/") + "resources/images/"+fileName;
				File f = new File(fileInfo);
				if (f.exists()) {
					resultStr += fileName + " : 파일이 이미 존재해요!!<br>";
				} else {
					mfile.transferTo(new File(fileInfo));
					resultStr += fileName + " : 파일이 저장되었어요!!<br>";
				}
			} catch (IOException e) {
				e.printStackTrace();
				resultStr += fileName + " : 오류가 발생했어요!!";				
			}
		}
		mav.addObject("msg", resultStr);	
		return mav;
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSP 테스트 예제</title>
</head>
<body>
<h2>SpringMVC FileUpload(Multiple)</h2>
<hr>
<%
	if( request.getAttribute("msg") == null ) {
%>
	<form action="/springedu/upload3" 
	               enctype="multipart/form-data" method="post">
    	<input type="file" name="mfile" multiple/> <!-- 추가 -->
    	<input type="submit" value="파일올리기"/>
	</form>
<%
	} else {
%>
	 ${ msg }
<%
	}
%>
</body>
</html>
```



브라우저에서 요청할 수 있는 파일은 프로젝트 안에 있어야 가능하다!!

resources내에 있는 폴더만 브라우저에서 요청해서 사용이 가능하다.

servletContext에 getRealPath를 사용해서 파일을 업로드하거나 읽는다.(context.getRealPath("/")) -> 이 컨트롤러가 수행하고 있는 최상위 폴더를 추출하는 메서드

​	

--------

**bean 설정파일에 설정**

```xml
<resources mapping="/mypage/**" location="/mypage/" /> <!-- resoures 밑에 하기 싫으면 여기서 추가해서 폴더를 추가해서 만들수있다. -->
```

--> webapp 폴더 밑에 폴더를 생성해서 사용한다.