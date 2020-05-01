# 20200501 Linux & Hadoop

`cat $HADOOP_HOME/etc/hadoop/core-site.xml` : 특정한 환경변수의 값을 사용할 때는 리눅스의 경우에는 $기호를 사용한다.​

**hdfs-site.xml** 

`cat $HADOOP_HOME/etc/hadoop/hdfs-site.xml`

```
   <property>
      <name>dfs.replication</name>
      <value>3</value>
   </property>
```

3개의 복제본을 복사해주세요 라는 것 !! main하나에 복제본 2개

```
   <property>
      <name>dfs.name.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/name</value>
   </property>
```

namenode를 보관하는 곳 ↑

/root/hadoop-2.7.7/hdfs/name 이루트로 들어가서 ls하면 하둡 파일에 대한 전반적으로 담고 있는 이미지 파일이 들어있다.

m1

```
   <property>
      <name>dfs.data.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/data</value>
   </property>
```

datanode를 보관하는 곳 ↑

/root/hadoop-2.7.7/hdfs/data 이 루트로 들어가서 더 들어가야한다. 순서대로 써보면 `cd current` `cd BP-128어쩌구저쩌구` `cd finalized` `cd current` `cd current` 에서 ll 치면 여기에 파일들이 숨어있다. `cat명령어를 사용해서 확인해보자!

m2, m3, m4

```
   <property>
      <name>dfs.support.append</name>
      <value>true</value>
   </property>
```

파일 시스템을 수정하지 않고 그냥 append만 한다. !! 파일이 너무 수정할 것이 많을것이고 수정하는게 어떤 파일을 해야할지 모르니까 그냥 안하는게 좋다고 판단하여 넣고 읽는것만 가능하고 새롭게 넣는 방식을 사용한다.

--------

**예제 FileSystemOperations.java**

```java
package hdfsexam;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class FileSystemOperations {
  public void addFile(String source, String dest, Configuration conf) throws IOException {
    FileSystem fileSystem = FileSystem.get(conf);

    String filename = source.substring(source.lastIndexOf('/') + 1,source.length());

    if (dest.charAt(dest.length() - 1) != '/') {
      dest = dest + "/" + filename;
    } else {
      dest = dest + filename;
    }

    Path path = new Path(dest);
    if (fileSystem.exists(path)) {
      System.out.println("File " + dest + " already exists");
      return;
    }

    FSDataOutputStream out = fileSystem.create(path);
    InputStream in = new BufferedInputStream(new FileInputStream(new File(
        source)));

    byte[] b = new byte[1024];
    int numBytes = 0;
    while ((numBytes = in.read(b)) > 0) {
      out.write(b, 0, numBytes);
    }
    in.close();
    out.close();
    fileSystem.close();
  }

  public void readFile(String file, Configuration conf) throws IOException {
    FileSystem fileSystem = FileSystem.get(conf);

    Path path = new Path(file);
    if (!fileSystem.exists(path)) {
      System.out.println("File " + file + " does not exists");
      return;
    }

    FSDataInputStream in = fileSystem.open(path);

    String filename = file.substring(file.lastIndexOf('/') + 1,
        file.length());

    OutputStream out = new BufferedOutputStream(new FileOutputStream(
        new File(filename)));

    byte[] b = new byte[1024];
    int numBytes = 0;
    while ((numBytes = in.read(b)) > 0) {
      out.write(b, 0, numBytes);
    }

    in.close();
    out.close();
    fileSystem.close();
  }

  public void deleteFile(String file, Configuration conf) throws IOException {
    FileSystem fileSystem = FileSystem.get(conf);

    Path path = new Path(file);
    if (!fileSystem.exists(path)) {
      System.out.println("File " + file + " does not exists");
      return;
    }

    fileSystem.delete(new Path(file), true);

    fileSystem.close();
  }

  public void mkdir(String dir, Configuration conf) throws IOException {
    FileSystem fileSystem = FileSystem.get(conf);

    Path path = new Path(dir);
    if (fileSystem.exists(path)) {
      System.out.println("Dir " + dir + " already not exists");
      return;
    }

    fileSystem.mkdirs(path);

    fileSystem.close();
  }

  public static void main(String[] args) throws IOException {

    if (args.length < 1) {
      System.out.println("Usage: FileSystemOperations add/read/delete/mkdir"
          + " [<local_path> <hdfs_path>]");
      System.exit(1);
    }

    FileSystemOperations client = new FileSystemOperations();

    Configuration conf = new Configuration();
	conf.set("fs.defaultFS", "hdfs://192.168.111.120:9000");

    if (args[0].equals("add")) {
      if (args.length < 3) {
        System.out.println("Usage: hdfsclient add <local_path> "
            + "<hdfs_path>");
        System.exit(1);
      }

      client.addFile(args[1], args[2], conf);

    } else if (args[0].equals("read")) {
      if (args.length < 2) {
        System.out.println("Usage: hdfsclient read <hdfs_path>");
        System.exit(1);
      }

      client.readFile(args[1], conf);

    } else if (args[0].equals("delete")) {
      if (args.length < 2) {
        System.out.println("Usage: hdfsclient delete <hdfs_path>");
        System.exit(1);
      }

      client.deleteFile(args[1], conf);

    } else if (args[0].equals("mkdir")) {
      if (args.length < 2) {
        System.out.println("Usage: hdfsclient mkdir <hdfs_path>");
        System.exit(1);
      }

      client.mkdir(args[1], conf);

    } else {
      System.out.println("Usage: hdfsclient add/read/delete/mkdir"
          + " [<local_path> <hdfs_path>]");
      System.exit(1);
    }

    System.out.println("Done!");
  }
}
```

윈도우에서 **run configuration:** **mkdir mytemp** 하면 폴더를 추가 할 수 없다. 왜냐 ? 윈도우는 윈도우 계정이고 root 계정이 아니기 때문이다

**run configuration:** **mkdir mytemp** 

**run configuration:** **add c:/temp/파일이름및.xxx /edudata**

...

-------

실습 TomcatLogHDFS_Save.java

[ Hadoop HDFS 실습 : 빅데이터플랫폼 수행평가(1) ]

1. 클래스명 : TomcatLogHDFS_Save
2. 프로그램 형식 : Java Application
3. 기능
    Tomcat의 모든 ACCESS LOG 파일들을 하나의 파일로 만들어서 저장한다.
    (파일의 생성 위치는 임의로 정한다. 로그파일이 마땅치 않으면 logs 폴더를
     가져가서 작업한다.)
    파일명 : tomcat_access_log.txt
4. HDFS의 /edudata 폴더에 저장한다.
5. 저장이 끝난 다음에는 저장된 파일의 사이즈를 화면에 표준 출력하고 종료한다.

```java
package hdfsexam;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class TomcatLogHDFS_Save {
	public void addFile(String source, String dest, Configuration conf) throws IOException {
	    FileSystem fileSystem = FileSystem.get(conf);

	    String filename = source.substring(source.lastIndexOf('/') + 1,source.length());

	    if (dest.charAt(dest.length() - 1) != '/') {
	      dest = dest + "/" + filename;
	    } else {
	      dest = dest + filename;
	    }

	    Path path = new Path(dest);
	    if (fileSystem.exists(path)) {
	      System.out.println("File " + dest + " already exists");
	      return;
	    }

	    FSDataOutputStream out = fileSystem.create(path);
	    InputStream in = new BufferedInputStream(new FileInputStream(new File(
	        source)));

	    byte[] b = new byte[1024];
	    int numBytes = 0;
	    while ((numBytes = in.read(b)) > 0) {
	      out.write(b, 0, numBytes);
	    }
	    in.close();
	    out.close();
	    fileSystem.close();
	  }

	public static void main(String[] args) {
		// 폴더 내의 모든 파일 읽기!!
		String path = "c:/Temp/logs/";
		String pathWrite = "c:/Temp/";
		
		File dir = new File(path);
		File[] fileList = dir.listFiles();
		
		for(File file : fileList) {
			if(file.isFile()) {
				
				String fileName = file.getName();
				System.out.println(fileName);
				
				try (FileReader reader = new FileReader(path + fileName);
						BufferedReader br = new BufferedReader(reader);
						FileWriter  writer = new FileWriter(pathWrite + "tomcat_access_log.txt", true);){  
					String data;
					while (true) {
						data = br.readLine();
						if (data == null)
							break;
						
						writer.append(data);
						writer.append('\n');
					}
				} catch (FileNotFoundException fnfe) {
					System.out.println(fnfe);
					System.out.println("파일이 존재하지 않습니다.");
				} catch (IOException ioe) {
					System.out.println(ioe);
				}
				
			}
		}
		
		try {
			Configuration conf = new Configuration();
			conf.set("fs.defaultFS", "hdfs://192.168.111.120:9000");
			FileSystemOperations client = new FileSystemOperations();

			client.addFile("c:/Temp/tomcat_access_log.txt", "/edudata", conf);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```



(1) 시스템 환경변수 설정
Spring MVC에서 Hadoop 연동하여 HDFS 나 MapReduce 기능을 사용하려면
hadoop 폴더를 c:\ 에 저장한 후에 HADOOP_HOME, PATH
HADOOP_HOME  ---> c:\hadoop
PATH  ---> %HADOOP_HOME%\bin
을 추가 설정한다.

cmd 창을 열고 echo %HADOOP_HOME%, echo %PATH%

(2) Eclipse 재기동

(3) pom.xml 편집

```xml

		<!-- https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-common -->
		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-common</artifactId>
			<version>2.7.7</version>
		</dependency>

		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-client</artifactId>
			<version>2.7.7</version>
		</dependency>
		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-mapreduce-client-core</artifactId>
			<version>2.7.7</version>
		</dependency>

		<dependency>
			<groupId>commons-io</groupId>
			<artifactId>commons-io</artifactId>
			<version>2.6</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.data</groupId>
			<artifactId>spring-data-hadoop</artifactId>
			<version>2.5.0.RELEASE</version>
		</dependency>
```

추가 저장, 저장 후 다 실행 될때까지 대기할 것!!

(4) servlet-contexl.xml

namespace에서 hadoop 체크 한 후

```xml
	<hadoop:configuration id="hdConf">
		fs.defaultFS=hdfs://192.168.111.120:9000
	</hadoop:configuration>
```

이 내용을 추가하고 저장, 이렇게 하면 자동으로 configuration 객체가 생성된다.



http://localhost:8000/springedu/hadooprw?filename=springdata.txt

확인!!



**HadoopDAO.java**

```java
package dao;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.springframework.stereotype.Repository;

@Repository
public class HadoopDAO {
	public String readwrite(String name) {
		String result ="";
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "hdfs://192.168.111.120:9000");
		FileSystem hdfs = null;
		try  {
			hdfs = FileSystem.get(conf);
			Path filePath = new Path("/edudata/"+name);
			if(hdfs.exists(filePath)) {
				BufferedReader r = new BufferedReader(new InputStreamReader(hdfs.open(filePath), "utf-8"));
				String line = null;
				while((line=r.readLine())!=null) {
					System.out.println(line);
					result += line;
				}
				r.close();
			} else {
				FSDataOutputStream out = hdfs.create(filePath, false);
				out.write("스프링에서 하둡에 보낸 데이터임!!".getBytes("utf-8"));
				out.flush();
				result = filePath.getName() + "으로 저장 완료되었어요. 하둡가서 확인해보세요.";
				out.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (hdfs != null)
					hdfs.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return result;
	}
}
```

**HadoopDAO2.java**

위와 다른 점은 servlet-context.xml에서 Configuration 객체를 설정해서 사용!!

```java
package dao;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
@Repository
public class HadoopDAO2 {
	@Autowired
	private Configuration conf;
	
	public String read(String name) {	
		String result = "";	
		FileSystem hdfs = null;
		try {
			hdfs = FileSystem.get(conf);
			Path filePath = new Path(name);
			if (hdfs.exists(filePath)) {
				BufferedReader r = new BufferedReader(new InputStreamReader(hdfs.open(filePath), "utf-8"));
				String line = null;
				while ((line = r.readLine()) != null) {
					System.out.println(line);
					result += line;
				}
				r.close();
			} else {
				result = "파일이 존재하지 않습니다!!";
			}
		} catch (Exception e) {
			e.printStackTrace();
			result = "오류가 발생했어요";
		} finally {
			try {
				if (hdfs != null)
					hdfs.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return result;
	}
	public String write(String msg) {
		String result = "";
		String filename = "/edudata/message.txt";
		FileSystem hdfs = null;
		try {
			hdfs = FileSystem.get(conf);
			Path filePath = new Path(filename);
			if (hdfs.exists(filePath)) {
				hdfs.delete(filePath, true);
			}	
			FSDataOutputStream out = hdfs.create(filePath, false);
			out.write(msg.getBytes("utf-8"));
			out.flush();
			result = filename + "으로 저장 완료되었어요.. 하둡가서 확인해 보세요..";
			out.close();			
		} catch (Exception e) {
			e.printStackTrace();
			result = "오류가 발생했어요";
		} finally {
			try {
				if (hdfs != null)
					hdfs.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return result;
	}	
	public String delete() {
		String result = "";
		String filename = "/edudata/message.txt";
		try (FileSystem hdfs=FileSystem.get(conf)){
			Path filePath = new Path(filename);
			hdfs.delete(filePath, true);
			result = filename + " 파일이 삭제되었어요.. 확인해 보세요..";
		} catch (Exception e) {
			e.printStackTrace();
			result = "오류가 발생했어요";
		} 
		return result;
	}
}
```

**HadoopController.java**

```java
package my.spring.springedu;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import dao.HadoopDAO;

@Controller
public class HadoopController {
	@Autowired
	HadoopDAO dao;
	@RequestMapping("/hadooprw")
	public ModelAndView put(String filename) {
		String result = dao.readwrite(filename);
		ModelAndView mav = new ModelAndView();
		mav.addObject("hadooprw", result);
		mav.setViewName("hadoopView");
		return mav;
	}
}

```

**HadoopController2.java**

```java
package my.spring.springedu;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import dao.HadoopDAO2;
@Controller
public class HadoopController2 {
	@Autowired
	HadoopDAO2 dao;	
	public HadoopController2() {
		System.out.println("HadoopController2");
	}
	@RequestMapping("/hadoophdfs")  
	public ModelAndView put(String action){
		String result = "";
		if(action.equals("put"))
			result = dao.write("하둡 입력을 테스트 합니다...\n"+
		                                                  new Date());
		else if(action.equals("get")) 
			result = dao.read("/edudata/message.txt");
		else if(action.equals("delete")) 
			result = dao.delete();
		ModelAndView mav = new ModelAndView();
		mav.addObject("hadooprw", result);
		mav.setViewName("hadoopView");		
		return mav;
	}	
}
```

**hadoopView.jsp**

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>하둡 입출력 예제</title>
</head>
<body>
	<h1>하둡 입출력의 처리 결과</h1>
	<hr>
	${hadooprw}
</body>
</html>
```

