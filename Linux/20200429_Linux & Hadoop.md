# 20200429 Linux

--------

Master 컴퓨터에서 실행할것!!!

SSH Key를 생성하여 다른 시스템과 공유한다.

비밀번호 없이 로그인이 가능하도록 하는 것으로 다음 명령을 master 시스템에서 수행시켜서 공개키를 만든다.(참고 : 시큐어 셀(Secure Shell, SSH)은 네트워크 상의 다른 컴퓨터에 로그인하거나 원격 시스테에서 명령을 실행하고 다른 시스템으로 파일을 복사할 수 있도록 해 주는 응용 프로그램 또는 그 프로토콜을 가리킨다.

ssh root@slave1` 

slave에 들어갈때 password를 치지 않게 환경을 설정해야한다.!! 그러기 위해서는 4컴퓨터만의 고유 비밀번호를 생성해서 사용해야한다.

`ssh-keygen -t rsa`

`cd .ssh`

`ll`

공개키를 생성한 다음에는 다음에는 다음 명령을 수행시켜서 공개키를 나머지 리눅스 시스테과 공유한다.

`ssh-copy-id -i /root/.ssh/id_rsa.pub root@slave1`

`ssh-copy-id -i /root/.ssh/id_rsa.pub root@slave2`

`ssh-copy-id -i /root/.ssh/id_rsa.pub root@slave3`

같은 공개키를 공유하기 위해서 마지막으로 master도 같이 실행해준다.

`ssh-copy-id -i /root/.ssh/id_rsa.pub root@master`



`ssh root@slave1`

`ssh root@slave2`

`ssh root@slave3`

`ssh root@master`

를 쳐서 패스워드 없이 로그인이 되는지 확인한다.



`hdfs namenode -format`  : 하둡 파일 시스템을 만들어주고 초기화해준다.

`cd hadoop-2.7.7`

`cd hdfs`

`ls` 치면 name이라고하면 success!!!!!!!!!!!!!!!!!

------

**위에서 ls 치면 name이라고 나오지 않을때 solution!!!**

하둡에 configuration 파일 확인

cd master에서

`cd`

`cd $HADOOP_HOME/etc`

`cd hadoop`

**core-site.xml 에 오타 확인!!**

**hdfs-site.xml에 오타확인!!**

-----

Hadoop의 HDFS를 기동시킨다

`start-dfs.sh`

Hadoop의 HDFS를 중지시킨다.

`stop-dfs.sh`

데몬이 제대로 수행되었는지 확인한다. -`jps` 사용

원래는 Master에서 namenode만 떠야하는데 현재는 datanode까지 같이 나와서 확인요망!!!!!!!!!!

-> 해결책!!!

`cd $HADOOP_HOME/etc/hadoop`

`ls` -> slaves1이 있었을것이고 `vi slaves`로 들어가서 localhost를 지우고

```
slave1
slave2
slave3
```

저장

`vi masters` 에 들어가서 slave1을 추가하고 저장

`cd hadoop-2.7.7`에가서 hdfs있으면 삭제!!!!  slave1, 2, 3에 도 있으면 다 삭제

master에서 `hdfs namenode -format` 를 다시 수행하고 

`start-dfs.sh` 실행 후 각각 4개 jps확인

master : namenode만 떠야한다.

slave1 : DataNode, SecondaryNameNode 떠야하고

slave2 : DataNode 뜸

slave3 : DataNode 뜸

하둡 DHFS 영역에 폴더를 구축한다. 

2008.csv.bz2, president_moon.txt, product_click.log 파일을 리눅스의 sampledata 디렉토리에 넣고 압축파일은 압축을 푼다.

`bzip2 -kd 2008.csv.bz2` 압축 파일 해제!!

`ll`로 확인

------

r w x

1 1 1 모두 됨

0 0 0 아무것도 암됨

-> 1은 가능 0은 불가능

000  

111  ---> 7

101 ---> 5

110 ---> 6

100 --> 4