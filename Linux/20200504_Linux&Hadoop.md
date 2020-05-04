# 20200504 Hadoop

[테스트 환경 준비]

(1) JDK 설치

​	JAVA_HOME 설정, PATH 설정

(2) Tomcat 설치 - **HTTP포트정보 : 8000, 마지막 페이지에서 체크박스 해제**

(3) **Eclipse 설치**

(4) **본인만의 폴더 워크스페이스 폴더 복사**

(5) **Rstudy 폴더 복사** 

(6) **이클립스를 기동하면서 본인의 워크스페이스 폴더 사용**

(7) VMWare Workstation Player 12 설치

(8) cmd창에서 ipconfig를 수행시켜서 VMWare 8의 IP주소 확인

   -----> 192.168.111.1

(9) c:/hadoop 복사한 후에

​	HADOOP_HOME, PATH 설정

(10) VM 4개 기동

(11) start-dfs.sh ,  start-yarn.sh를 master에서 실행시킨다.

(12) hadoopexam 패키지

 		FileSystem

​		FileSystemCat ---> 결과

(13) HDFS에 /edudata/message.txt이 존재하는지 확인 후에

http://localhost:8000/springedu/hadoophdfs?action=get













`yarn jar fruitswc.jar mrexam.WordCount`

