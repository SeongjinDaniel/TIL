# MySQL TroubleShooting

#### Problem 

```sql
mysql> select @@global.time_zone, @@session.time_zone;
+--------------------+---------------------+
| @@global.time_zone | @@session.time_zone |
+--------------------+---------------------+
| SYSTEM             | SYSTEM              |
+--------------------+---------------------+
1 row in set (0.00 sec)
```

`SET GLOBAL time_zone='Asia/Seoul';`
`SET time_zone='Asia/Seoul';`

위 명령이 실행이 되지 않고 에러가 나서 해결을 해야했다.



#### Solution

https://dev.mysql.com/downloads/timezones.html

↑↑↑↑↑↑↑↑↑ 위 링크 클릭



- mysql 5.6 이하
  - (POSIX - UNIX기반 OS 유저)
- mysql 5.7 이상
  - (POSIX - UNIX기반 OS 유저)

버전에 맞게 설치 해주면 된다.(`select version();`문 실행을 통해 확인 가능)

윈도우 유저는 Non POSIX with leap seconds 받으면 된다.



1. `use mysql`  문을 먼저 실행 후 
2. 버전에 맞게 다운로드 받은 파일을 실행
3. 약 4만 줄이 넘는 sql을 mysql 스키마에 실행한다.

![image](https://user-images.githubusercontent.com/55625864/87674467-024d9880-c7b1-11ea-99b3-bb9ec497981b.png)

 

`SELECT @@global.time_zone, @@session.time_zone;`

위 명령을 실행하면 SYSTEM이라고 나올것이다.

`SET GLOBAL time_zone='Asia/Seoul';`
`SET time_zone='Asia/Seoul';`

이것을 실행한 후 다시

`SELECT @@global.time_zone, @@session.time_zone;`

실행 해보면

```sql
mysql> select @@global.time_zone, @@session.time_zone; 
+--------------------+---------------------+ 
| @@global.time_zone | @@session.time_zone |
+--------------------+---------------------+ 
| Asia/Seoul 		 | Asia/Seoul 		   | 
+--------------------+---------------------+ 
1 row in set (0.00 sec)
```



해결 완료!!