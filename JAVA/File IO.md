# File I/O



**File 객체**

- 스트림이란 **프로그램과 I/O 객체를 연결하여 데이터를 송수신 하는 길**을 말한다.

  InputStream은 데이터를 읽어 들이는 객체이고, OutputStream은 데이터를 써서 보내는 객체이다.

**byte 단위(I/O)**

- binary 데이터를 입출력하는 스트림이다.
- 이미지, 동영상 등을 송수신할 때 주로 사용한다.

**문자단위(Reader, Writer)**

- 말 그대로 text 데이터를 입출력하는데 사용하는 스트림이다.
- HTML 문서, 텍스트 파일을 송수신할 때 주로 사용한다.



flush() : 버퍼의 내용을 강제로 출렿강여 비움. close()하면 suto-flush 발생!



**Byte 단위**

- InputStream -> FileInputStream -> BufferedInputStream

- OutputStream -> FileOutputStream ->  BufferedOutputStream



**문자(char) 단위**

- Reader -> fileReader -> BufferedReader

- Writer -> fileWriter -> BufferedWriter

- 기본적으로 Character 기반 스트림은 UTF-8 인코딩이 되어있다.



Java **Byte** 스트림은 8 비트 바이트의 입력 및 출력을 수행하는 데 사용되는 반면 Java **Character** 스트림은 16 비트 유니 코드의 입력 및 출력을 수행하는 데 사용됩니다.

![image](https://user-images.githubusercontent.com/55625864/96092330-b2908180-0f05-11eb-9b24-9821cbad9f7f.png)



### FileInputStream

This stream is used for reading data from the files. Objects can be created using the keyword **new** and there are several types of constructors available.

Following constructor takes a file name as a string to create an input stream object to read the file −

```
InputStream f = new FileInputStream("C:/java/hello");
```

Following constructor takes a file object to create an input stream object to read the file. First we create a file object using File() method as follows −

```
File f = new File("C:/java/hello");
InputStream f = new FileInputStream(f);
```

Once you have *InputStream* object in hand, then there is a list of helper methods which can be used to read to stream or to do other operations on the stream.

| Sr.No. |                     Method & Description                     |
| ------ | :----------------------------------------------------------: |
| 1      | **public void close() throws IOException{}**This method closes the file output stream. Releases any system resources associated with the file. Throws an IOException. |
| 2      | **protected void finalize()throws IOException {}**This method cleans up the connection to the file. Ensures that the close method of this file output stream is called when there are no more references to this stream. Throws an IOException. |
| 3      | **public int read(int r)throws IOException{}**This method reads the specified byte of data from the InputStream. Returns an int. Returns the next byte of data and -1 will be returned if it's the end of the file. |
| 4      | **public int read(byte[] r) throws IOException{}**This method reads r.length bytes from the input stream into an array. Returns the total number of bytes read. If it is the end of the file, -1 will be returned. |
| 5      | **public int available() throws IOException{}**Gives the number of bytes that can be read from this file input stream. Returns an int. |

There are other important input streams available, for more detail you can refer to the following links −

- [ByteArrayInputStream](https://www.tutorialspoint.com/java/java_bytearrayinputstream.htm)
- [DataInputStream](https://www.tutorialspoint.com/java/java_datainputstream.htm)

## FileOutputStream

FileOutputStream is used to create a file and write data into it. The stream would create a file, if it doesn't already exist, before opening it for output.

Here are two constructors which can be used to create a FileOutputStream object.

Following constructor takes a file name as a string to create an input stream object to write the file −

```
OutputStream f = new FileOutputStream("C:/java/hello") 
```

Following constructor takes a file object to create an output stream object to write the file. First, we create a file object using File() method as follows −

```
File f = new File("C:/java/hello");
OutputStream f = new FileOutputStream(f);
```

Once you have *OutputStream* object in hand, then there is a list of helper methods, which can be used to write to stream or to do other operations on the stream.

| Sr.No. |                     Method & Description                     |
| ------ | :----------------------------------------------------------: |
| 1      | **public void close() throws IOException{}**This method closes the file output stream. Releases any system resources associated with the file. Throws an IOException. |
| 2      | **protected void finalize()throws IOException {}**This method cleans up the connection to the file. Ensures that the close method of this file output stream is called when there are no more references to this stream. Throws an IOException. |
| 3      | **public void write(int w)throws IOException{}**This methods writes the specified byte to the output stream. |
| 4      | **public void write(byte[] w)**Writes w.length bytes from the mentioned byte array to the OutputStream. |

file:/E:/DispatcherServlet.jpg

#### 참조

- https://programmingsummaries.tistory.com/64
- https://victorydntmd.tistory.com/134
- https://wikidocs.net/227
- https://velog.io/@ssseungzz7/Java-File-inputoutput
- https://coding-factory.tistory.com/282
- https://loco-motive.tistory.com/58

- https://www.tutorialspoint.com/java/java_files_io.htm