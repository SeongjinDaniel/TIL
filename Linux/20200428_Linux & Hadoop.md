# 20200428 Linux Study

## 설치 환경 설정

VMware에서 root계정으로 로그인한다.

1. IP주소를 고정한다.

2. JDK 1.8 설치한다. -> 모든 사람들이 사용할 수 있게 환경설정도 할 것!

3. Eclipse 설치한다.

4. Tomcat 설치한다.

5. master 192.168.111.120

   - slave1 192.168.111.130

   - slave2 192.168.111.140

   - slave3 192.168.111.150

     참고) 이것이 리눅스다 p117

## :punch:Network 설정

**root 계정**

`cd /etc/sysconfig/network-scripts/` : 이 리포지토리로 들어감!!

`ls` : 를 쳐서 확인해야 할 것이 있음 왼쪽 맨 위에 `ifcfg-eno16777728`을 확인 !!

![image-20200428095800111](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200428095800111.png)

`gedit ifcfg-eno16777728` : network 설정창 켜기 명령

아래 와 같이 설정을 해준다.

```
IPADDR=192.168.111.120
NETMASK=255.255.255.0
GATEMAY=192.168.111.2
DNS1=192.168.111.2
```

### 환경 설치

java.sun.com 에서 다운로드 할것!!

리눅스 용으로 다운로드

![image-20200428100741345](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200428100741345.png)

그러나 빅데이터 플랫폼 파일에 이미 있음!!

리눅스에서 tools라는 폴더를 하나 생성하고 빅데이터 플랫폼에 있는 **tomcat**과 **eclipse**와 **hadoop**, **jdk**를 복사해서 linux에 붙여넣기 한다.

`java -version`을 확인해 보면 리눅스에서 제공하는 1.7버전을 확인한다. 그러나 1.7은 쿼리문같은 것을 사용못하니까 !! 1.8로 변경해야한다!!

**jdk를 설치한다.**

`cd `

`mkdir tools `

`cd tools `

`tar xvfz jdk-8u131-linux-x64.tar.gz`

`mv jdk1.8.9_131 /usr/local`

`cd /usr/local`

`ln -s jdk1.8.0_131 java`

`ls -l`

![image-20200428113034242](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200428113034242.png)

`vi /etc/profile`

`source /etc/profile`

`java -version`

**이클립스 설치**

`tar xvfz eclipse-jee-2018-12-R-linux-gtk-x86_64.tar.gz`

-> 다 끝나면 이클립스 폴더가 만들어짐

`cd eclipse`

`./eclipse` =>  환경변수에서 .을 설정안해 놓아서 ./를 해야 하고 이렇게 .을 환경변수에 설정안하는것이 보안상 문제에 더 좋다!!

workspace는 /root/eclipse-workspace에서 사용하겠음 !!

이클립스를 실행한 터미널은 이클립스만 사용가능하고 다른 터미널을 사용하고 싶으면 새롭게 하나 더 실행하면 된다.

File -> java project -> javaexam 만들고 -> Finish

![image-20200428114649398](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200428114649398.png)

Open Perspective 선택

### Tomcat 설치

`tar xvfz apache-tomcat-9.0.22.tr.gz`  -> 압축파일 해제

eclipse에서 File -> New -> Other -> server -> Tomcat v 9.0 Server -> Browse 클릭! -> root/tools/apach~ 선택하고 Okay!

Servers 폴더에서 server.xml 들어가서 63번째 줄에 port 번호 8000로 수정

linuxedu -> WebContent -> 우클릭 New -> first.html 파일 생성 후 테스트!!

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>안녕하세요? 리눅스의 웹 서비스입니다.</h1>
</body>
</html>
```

tomcat -> add and remove 에서 linuxedu를 추가한후 tomcat 기동하고 firefox 웹 브라우저에서

192.168.111.120:8000/linuxedu/first.html로 확인 가능!!

**Tomcat Open** 

window -> Show View -> Servers -> Open

**ecilpse 기동 command**

`./eclipse&` 라고 하면 새로운 command창을 안띄워도되고 그 command창에서 사용해도된다.

### Hadoop 설치

`cd tools`

`tar xvfz hadoop-2.7.7.tar.gz` 

`mv hadoop-2.7.7 ..`

`ls`

`cd ..`

/root 디렉토리로 이동됐음.

vi .bashrc

Hadoop의 설정파일 디렉토리로 옮겨간다.

`cd $HADOOP_HOME/etc/hadoop`

```
7. hadoop-env.sh 파일 끝에 다음 내용을 추가한다.
export JAVA_HOME=/usr/local/java
export HADOOP_HOME=/root/hadoop-2.7.7
export HADOOP_HEAPSIZE=500

8. mapred-env.sh 파일 끝에 다음 내용을 추가한다.
export JAVA_HOME=/usr/local/java
export HADOOP_JOB_HISTORYSERVER_HEAPSIZE=500
export HADOOP_HOME=/root/hadoop-2.7.7

9. yarn-env.sh 파일 끝에 다음 내용을 추가한다.
export JAVA_HOME=/usr/local/java
export HADOOP_HOME=/root/hadoop-2.7.7
export YARN_HEAPSIZE=500

10. core-site.xml 에 다음 내용을 편집한다.
<configuration>
   <property>
      <name>fs.defaultFS</name>
      <value>hdfs://master:9000/</value>
   </property>   
</configuration>

11. hdfs-site.xml 에 다음 내용을 편집한다.
<configuration>
   <property>
      <name>dfs.replication</name>
      <value>3</value>
   </property>
   <property>
      <name>dfs.name.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/name</value>
   </property>
   <property>
      <name>dfs.data.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/data</value>
   </property>
   <property>
      <name>dfs.support.append</name>
      <value>true</value>
   </property>
   <property>
      <name>dfs.namenode.secondary.http-address</name>
      <value>slave1:50090</value>
   </property>
   <property>
      <name>dfs.namenode.secondary.https-address</name>
      <value>slave1:50091</value>
   </property> 
</configuration>

12. mapred-site.xml 에 다음 내용을 편집한다.
<configuration>
   <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
   </property>
   <property>
      <name>yarn.resourcemanager.hostname</name>
      <value>master</value>
   </property>
</configuration>

13. yarn-site.xml 에 다음 내용을 편집한다. 
<configuration>
<!-- Site specific YARN configuration properties -->
   <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
   </property>
</configuration>
```

14. 완성된 VM을 복사하여 총 4개를 만든다.

    - m1, m2, m3, m4

    m1을 제외하고 각 폴더의 xxxxx.vmx파일을 메모장으로 열어서 수정한다. 다음과 같이 수정한다.

    ```
    displayName="m~~~"
    ```

    displayName="m1" --> displayName="m2"

    displayName="m1" --> displayName="m3"

    displayName="m1" --> displayName="m4"

    각각 수정한다.

VMware Workstation 에서 Open a Virtual Machine 눌러서 open하기! xxx.vmx를 연다.

## Command

`whoami` : 어떤 계정인지 보여줌

`date` : 현재 날짜 알려줌

`ifconfig` : ip주소 확인 가능

`hostname` : host name 확인 가능

`hostnamectl set-hostname master` : hostname을 master로 변경할 수 있음

ctrl+d : 로그아웃 단축키

`systemctl stop firewalld` : 방화벽 stop, window에서 크롬으로도 테스트가 가능하다.

`systemctl disable firewalld` : 방화벽 disable, window에서 크롬으로도 테스트가 가능하다.

## 설명

/root -> 읽는 방법 : root root 

- / : root라고 읽는다.



-------------

`su centos` : root 계정에서는 암호를 물어보지 않고 centos 계정으로 바로 이동 할 수 있다.

`pwd` : 하면 아직 이동 하지 않았고

`cd` : 하면 centos로 이동

`pwd` : 하면 확인 가능

`ls` : imsi 디렉토리 있는지 확인

`javac Example.java` -> 에러 나지 않으면

`java Example` 실행하면 확인가능!

ctrl+d : 로그아웃 단축키 

-> 루트로 다시 되돌아감
