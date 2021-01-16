# Docker MariaDB



**Docker 이미지 다운**

```
docker pull mariadb
```



**Docker 실행 명령어**

```
docker run --name sdt-mariadb -e MYSQL_ROOT_PASSWORD=sdtplatform -d mariadb:latest -p 3306:3306
```



#### 참조

- [[Docker] MariaDB 설치하기](https://logical-code.tistory.com/122)

