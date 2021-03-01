# aws RDS Summary



## Relational DB Service(관계형 데이터 베이스)

- 데이터베이스
- 테이블
- 데이터
- 필드



#### Relational DB 종류 (AWS RDS에서 사용 가능)

Microsoft SQL, Oracle, MySQL, Postgre, Aurora(aws db), Maria DB



#### Data Warehousing

- Business Intelligence
- 리포트 작성, 데이터분석시 사용 (Production Database -> Data Warehousing)
- 매우 방대한 분량의 데이터 로드시 사용



:bulb: 중요

**OLTP VS OLAP**

- OLTP : INSERT와 같이 종종 사용되어지는, 혹은 규모가 작은 데이터를 불러올 때 사용되는 SQL쿼리가 필요할 때  유용
  - Order # 210에만 해당되는 customer 이름, 주소, 시간 정보 INSERT
- OLAP : 매우 큰 데이터를 불러올 때 사용. 주로 덩치가 큰 SELECT 쿼리가 사용됨
  - 특정 회사 부서의 Net Profit, Products



## Database Backups



- Automated Backups (자동 백업)
- DB Snapshots (데이터베이스 스냅샷)



#### Automated Backups(AB) - 자동 백업

1. Retention Period(1-35일) 안의 어떤 시간으로 돌아가게 할 수 있음
2. AB는 그날 생성된 스냅샷과 Transaction logs(TL)을 참고함
3. 디폴트로 AB기능이 설정되어 있으며 백업 정보는 S3에 저장
4. AB동안 약간의 I/O suspensiton이 존재할 수 있음 -> Latency



#### DB Snapshots (데이터베이스 스냅샷)

1. 주로 사용자에 의해 실행됨
2. 원본 RDS Instance를 삭제해도 스냅샷은 존재함 (vs AB)



데이터베이스 백업

<img src="https://user-images.githubusercontent.com/76925694/109161410-5ba38e80-77ba-11eb-9814-d0dab2fa8632.png" alt="image" style="zoom:67%;" />



## Multi AZ, Read Replicas



#### Multi AZ(Multi Availability Zone)

- 원래 존재하는 RDS DB에 무언가 변화(e.x : Write)가 생길 때 다른 Availability Zone에 똑같은 복제본이 만들어짐 = Synchronize
- AWS에 의해서 자동으로 관리가 이루어짐 (No admin intervention)
- 원본 RDS DB에 문제가 생길 시 자동으로 다른 AZ의 복제본이 사용됨
- **Disaster Recovery Only!**

<img src="https://user-images.githubusercontent.com/76925694/109164349-ac68b680-77bd-11eb-8d20-30b5eefe08c5.png" alt="image" style="zoom:67%;" />



<img src="C:\Users\oliver\AppData\Roaming\Typora\typora-user-images\image-20210225230416416.png" alt="image-20210225230416416" style="zoom:67%;" />



#### Read Replica

- Production DB의 읽기 전용 복제본이 생성됨
- 주로 Read-Heavy DB작업시 효율성의 극대화를 위해 사용됨 (Scaling)
- **Disaster Recovery 용도가 아님!**
- 최대 5개 Read Replica DB 허용
- Read Replica의 Read Replica 생성 가능 (단 Latency 발생)
- 각각의 Read Replica는 자기만의 고유 Endpoint 존재

<img src="https://user-images.githubusercontent.com/76925694/109165278-b50dbc80-77be-11eb-9b64-f0482429bc1c.png" alt="image" style="zoom:67%;" />

