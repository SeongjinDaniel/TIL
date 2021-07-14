# MySQL 아시아 서울 시간으로 변경하기



**우리나라 시간대로 변경**

```mysql
set time_zone = 'Asia/Seoul';
```



**현재 시간 조회**

```mysql
SELECT now();
SELECT CURRENT_TIMESTAMP;
```



**time zone 조회**

```mysql
select @@system_time_zone;
SHOW GLOBAL VARIABLES LIKE '%zone%';
```

