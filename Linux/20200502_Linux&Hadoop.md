# 20200502 HADOOP

https://hadoop.apache.org/ 

추후에 하둡 내용이 필요하다면 이 사이트를 방문할것!!



fruits.txt를 HDFS의 /edudata에 저장



### Hadoop MapReduce

MapReduce는 구글에서 대용량 데이터 처리를 분산 병렬 컴퓨팅에서 처리하기 위한 목적으로 제작하여 2004년 발표한 소프트웨어 프레임워크다. 이 프레임워크는 페타바이트 이상의 대용량 데이터를 신뢰도가 낮은 컴퓨터로 구성된 클러스터 환경에서 병렬 처리를 짖원하기 위해서 개발되었다.

![MapReduce Overview Map Shuffle Reduce](https://image.slidesharecdn.com/datasciencewebinar061312-120618165932-phpapp02/95/how-salesforcecom-uses-hadoop-41-728.jpg?cb=1340920667)

Map : 필요한 데이터를 뽑아내고, 뽑아낸것을 가지고 적당히 변환한다. 각각의 block을 가지고 각각 처리한다. 이결과를 하나의 machine한테 보내고 여기서 리눅스를 진행한다. 주로 셀렉트 변환!!

Reduce : 집계과정을 한다.



MapReduce는 Hadoop 클러스터의 데이터를 처리하기 위한 시스템으로 총 2개(Map, Reduce)의 단계로 구성된다. Map과 Reduce 사이에는 shuffle과 sort라는 단계가 존재한다. 각 Map task는 전체 데이터 셋에 대해서 별개의 부분에 대한 작업을 수행하게 되는데, 기본적으로 하나의 HDFS block을 대상으로 수행하게 된다. 모든 Map 태스크가 종료되면, MapReduce 시스템은 중간(intermediate) 데이터를 Reduce 단계를 수행할 노드로 분산하여 전송한다.

Distributed File System에서 수행되는 MapReduce 작업이 끝나면 HDFS에 파일이 써지고, MapReduce 작업이 시작할 때는 HDFS로 부터 파일을 가져오는 작업이 수행된다.

Reduce 과정이 필요하지 않으면 Mapper 과정만 적용도 가능하다. 예를 들어 뉴욕타임즈 pdf 변환, 이미지 모자이크 처리 등이있다.

Mapper는 데이터지만 Mapper에서 나가는것은 keyvalue이다. 나머지도 다 keyvalue이다. 이것을 잘 생각하고 프로그램을 구현해야한다.

1. m1,m2,m3,m4  기동( 오라클 끔)

2. hadoop 데몬 기동 

   ```
    start-dfs.sh 
   ```

3. fruits.txt  HDFS의 /edudata에 저장한다.

   ```
   hdfs dfs -put /root/sampledata/fruits.txt /edudata
   ```

4. 잘들어 갔는지 확인해보기 

   ```
   hdfs dfs -ls /edudata 
   ```

   

mrexam폴더를 이클립스 hadoopexam에 붙이기!!

### 예제 WordCount

병렬처리가 되어야하지만 속도가 느리다!! hadoop은 int나 integer를 사용할 때 serializable을 상속하고 있다. 이로써 직렬화 알고리즘을 사용한다. 자바 직렬화 알고리즘 보다 더 컴팩트한 알고리즘을 다시 설계해서 속도를 개선했다.

```java
package mrexam;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

// mapreduce를 관리하는 클래스를 driver 클래스라고 한다.
public class WordCount {
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		conf.set("fs.default.name", "hdfs://192.168.111.120:9000");

		Job job = Job.getInstance(conf, "WordCount");

		job.setJarByClass(WordCount.class); // 드라이버 클래스의 클래스 객체
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);

		// hdfs 입출력 처리한다. 아래 2개
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		// reducer로 최종적으로 key value로 넘어간다. int로 개수 단위로 넘어간다.
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		//"/edudata/president_moon.txt"이거을 읽고
		FileInputFormat.addInputPath(job, new Path("/edudata/president_moon.txt"));
		// /result/wc1 폴더를 만든다. 이미 있으면 에러가 난다!! 다시 테스트 하고 있으면 이름을 변경해야한다.. 아니면 기존 폴더 삭제후 테스트!
		// 파일명을 지정하지 않으면 자동으로 파일명을 지정해서 생성한다.
		FileOutputFormat.setOutputPath(job, new Path("/result/wc1"));

		job.waitForCompletion(true);
		System.out.println("처리가 완료되었습니다.");
	}
}
```

4개 머신 모두 yarn-site.xml을 편집한다.

master에서 start-dfs.sh와 start-yarn.sh를 수행시킨다.



### WordCountMapper.java

```java
package mrexam;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// generic구문 내에 type들은 Mapper가 내보내는 key value type이다.
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

	private final static IntWritable one = new IntWritable(1);
	private Text word = new Text();
	
	// key를 사용해서 처리하는것은 잘 사용하지 않는다.
	
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
		StringTokenizer itr = new StringTokenizer(value.toString());
		while (itr.hasMoreTokens()) {
			word.set(itr.nextToken());
			context.write(word, one);
		}
	}
}
```

### WordCountReducer.java

```java
package mrexam;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	private IntWritable result = new IntWritable(); // int형

	// Iterable 
	public void reduce(Text key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException {
		System.out.println("\nREDUCE: " + key + "---");
		int sum = 0;
		// word마다 몇번 돌지 다름.
		for (IntWritable val : values) {
			int data = val.get();
			System.out.print(data + " ");
			sum += val.get();
		}
		result.set(sum);
		context.write(key, result);
	}
}
```







다음 기능들을 구현하기 위해서 Mapper 소스를 수정해야겠는지 Reduce 소스를 
수정해야겠는지를 파악하는것이 핵심...

[ Hadoop MapReduce 실습 (1) ]

[ 구현 기능 ]  

(1) mapred 패키지 폴더의 
     WordCount.java, WordCountMapper.java, WordCountReducer.java 를  
     exercise1 패키지 폴더로 복사한다.
(2) 단어의 길이가 3자 이상이고 5자 이하의 경우에만 결과를 만들어내도록 수정한다.
(3) 수행 결과는 /result/exerout1 에 저장한다.
(4) 리눅스 터미널에서 /result/exerout1/part-r-00000 파일의 내용을 출력한다.
     리눅스 터미널 화면을 덤프하여 그림판에 붙여서 exercise1.png 파일로 저장한다.

```java
package exercise1;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

// mapreduce를 관리하는 클래스를 driver 클래스라고 한다.
public class WordCount {
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		conf.set("fs.default.name", "hdfs://192.168.111.120:9000");

		Job job = Job.getInstance(conf, "WordCount");

		job.setJarByClass(WordCount.class); // 드라이버 클래스의 클래스 객체
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);

		// hdfs 입출력 처리한다. 아래 2개
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		// reducer로 최종적으로 key value로 넘어간다. int로 개수 단위로 넘어간다.
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		//"/edudata/president_moon.txt"이거을 읽고
		FileInputFormat.addInputPath(job, new Path("/edudata/fruits.txt"));
		// /result/wc1 폴더를 만든다. 이미 있으면 에러가 난다!! 다시 테스트 하고 있으면 이름을 변경해야한다.. 아니면 기존 폴더 삭제후 테스트!
		// 파일명을 지정하지 않으면 자동으로 파일명을 지정해서 생성한다.
		FileOutputFormat.setOutputPath(job, new Path("/result/exerout1"));

		// job을 받으면 resource 매니저가 잡을 받아서 처리를 한다. 
		// resource, node(실제 맵리듀스 작업 처리) 매니저가 있다.
		// resource 매니저가 먼저 처리후 node 매니저가 처리한다.
		job.waitForCompletion(true);
		System.out.println("처리가 완료되었습니다.");
	}
}
```

```java
package exercise1;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// generic구문 내에 type들은 Mapper가 내보내는 key value type이다.
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

	private final static IntWritable one = new IntWritable(1);
	private Text word = new Text();
	
	// key를 사용해서 처리하는것은 잘 사용하지 않는다.
	
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
	
			StringTokenizer itr = new StringTokenizer(value.toString());
			int length = 0;
			while (itr.hasMoreTokens()) {
				word.set(itr.nextToken());
				length = word.toString().length();
				if(length >= 3 && length <= 5) {
					context.write(word, one);
				}
			}
//		}
		
	}
}
```

```java
package exercise1;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	private IntWritable result = new IntWritable(); // int형

	// Iterable 
	public void reduce(Text key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException {
		System.out.println("\nREDUCE: " + key + "---");
		int sum = 0;
		// word마다 몇번 돌지 다름.
		for (IntWritable val : values) {
			int data = val.get();
			System.out.print(data + " ");
			sum += val.get();
		}
		result.set(sum);
		context.write(key, result);
	}
}
```



[ Hadoop MapReduce 실습 (2) ]

[ 구현 기능 ]

(1) mapred 패키지 폴더의 
     WordCount.java, WordCountMapper.java, WordCountReducer.java 를  
     exercise2 패키지 폴더로 복사한다.
(2) 단어의 갯수가 4개 이상인 경우에만 결과를 만들어내도록 수정한다.
(3) 수행 결과는 /result/exerout2 에 저장한다.
(4) 리눅스 터미널에서 /result/exerout2/part-r-00000 파일의 내용을 출력한다.
     리눅스 터미널 화면을 덤프하여 그림판에 붙여서 exercise2.png 파일로 저장한다.

```java
package exercise2;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

// mapreduce를 관리하는 클래스를 driver 클래스라고 한다.
public class WordCount {
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		conf.set("fs.default.name", "hdfs://192.168.111.120:9000");

		Job job = Job.getInstance(conf, "WordCount");

		job.setJarByClass(WordCount.class); // 드라이버 클래스의 클래스 객체
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);

		// hdfs 입출력 처리한다. 아래 2개
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		// reducer로 최종적으로 key value로 넘어간다. int로 개수 단위로 넘어간다.
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		//"/edudata/president_moon.txt"이거을 읽고
		FileInputFormat.addInputPath(job, new Path("/edudata/fruits.txt"));
		// /result/wc1 폴더를 만든다. 이미 있으면 에러가 난다!! 다시 테스트 하고 있으면 이름을 변경해야한다.. 아니면 기존 폴더 삭제후 테스트!
		// 파일명을 지정하지 않으면 자동으로 파일명을 지정해서 생성한다.
		FileOutputFormat.setOutputPath(job, new Path("/result/exerout2"));

		// job을 받으면 resource 매니저가 잡을 받아서 처리를 한다. 
		// resource, node(실제 맵리듀스 작업 처리) 매니저가 있다.
		// resource 매니저가 먼저 처리후 node 매니저가 처리한다.
		job.waitForCompletion(true);
		System.out.println("처리가 완료되었습니다.");
	}
}
```

```java
package exercise2;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

// mapreduce를 관리하는 클래스를 driver 클래스라고 한다.
public class WordCount {
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		conf.set("fs.default.name", "hdfs://192.168.111.120:9000");

		Job job = Job.getInstance(conf, "WordCount");

		job.setJarByClass(WordCount.class); // 드라이버 클래스의 클래스 객체
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);

		// hdfs 입출력 처리한다. 아래 2개
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		// reducer로 최종적으로 key value로 넘어간다. int로 개수 단위로 넘어간다.
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		//"/edudata/president_moon.txt"이거을 읽고
		FileInputFormat.addInputPath(job, new Path("/edudata/fruits.txt"));
		// /result/wc1 폴더를 만든다. 이미 있으면 에러가 난다!! 다시 테스트 하고 있으면 이름을 변경해야한다.. 아니면 기존 폴더 삭제후 테스트!
		// 파일명을 지정하지 않으면 자동으로 파일명을 지정해서 생성한다.
		FileOutputFormat.setOutputPath(job, new Path("/result/exerout2"));

		// job을 받으면 resource 매니저가 잡을 받아서 처리를 한다. 
		// resource, node(실제 맵리듀스 작업 처리) 매니저가 있다.
		// resource 매니저가 먼저 처리후 node 매니저가 처리한다.
		job.waitForCompletion(true);
		System.out.println("처리가 완료되었습니다.");
	}
}
```

```java
package exercise2;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	private IntWritable result = new IntWritable(); // int형

	// Iterable 
	public void reduce(Text key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException {
		System.out.println("\nREDUCE: " + key + "---");
		int sum = 0;
		// word마다 몇번 돌지 다름.
		for (IntWritable val : values) {
			int data = val.get();
			System.out.print(data + " ");
			sum += val.get();
		}
		if(sum >= 4) {
			result.set(sum);
			context.write(key, result);
		}
		
	}
}
```

### FruitsResultSort.java 예제

```java
package mrexam;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class FruitsResultSort {

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "hdfs://192.168.111.120:9000");
		FileSystem hdfs = FileSystem.get(conf);
		FSDataInputStream in = hdfs.open(new Path("/result/fruits1/part-r-00000"));

		BufferedReader br = new BufferedReader(new InputStreamReader(in));

		Map<String, Integer> map = new HashMap<String, Integer>();

		while (br.ready()) {
			String line = br.readLine();
			String data[] = line.split("\\s+");
			map.put(data[0], Integer.parseInt(data[1]));
		}

		List<String> keySetList = new ArrayList<>(map.keySet());

		// 오름차순 System.out.println("------value 오름차순------");
		Collections.sort(keySetList, (o1, o2) -> (map.get(o1).compareTo(map.get(o2))));

		for (String key : keySetList) {
			System.out.println("key : " + key + " / " + "value : " + map.get(key));
		}

		System.out.println();

		// 내림차순 System.out.println("------value 내림차순------");
		Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
		for (String key : keySetList) {
			System.out.println("key : " + key + " / " + "value : " + map.get(key));
		}

	}

}
```

