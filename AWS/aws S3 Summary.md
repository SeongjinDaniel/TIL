# aws S3 Summary



## S3 (Simple Storage Service)



- 안전하고 가변적인 Object 저장공간을 제공( ex: Google Cloud)
- 편리한 UI 인터페이스를 통해 어디서나 쉽게 데이터를 저장하고 불러올 수 있음
- 파일 크기는  0KB부터 5TB까지 지원
- 저장공간 무제한
- Bucket이라는 이름을 사용함 (디렉토리와 유사함)
- Bucket은 보편적인 namespace를 사용함



#### S3 Object 구성요소

- Key
- Value
- Version ID

<img src="https://user-images.githubusercontent.com/76925694/109262200-76224a00-7844-11eb-8078-00517c751976.png" alt="image" style="zoom:67%;" />

- Metadata
- CORS (Cross Origin Resource Sharing)



#### S3 Data Consistency Model

1. **Read after Write Consistency** (PUT)
2. **Eventual Consistency** (UPDATE, DELETE)



#### 다양한 s3  스토리지 타입

- **일반 s3**
- **S3 - IA (Infrequent Access)**
- **S3 - One Zone IA**
- **Glacier**
- **Intelligent Tiering**



#### 일반 S3

- 가장 보편적으로 사용되는 스토리지 타입
- 높은 내구성, 가용성(Durability, Availability)



#### S3 - IA (Infrequent Access)

- 자주 접근되지는 않으나 접근시 빠른 접근이 요구 되는 파일이 많을시 유용
- 일반 S3에 비해 비용은 저렴하나 접근시 추가 비용 발생
- 멀티 AZ를 통한 데이터 저장



#### S3 - One Zone IA

- 단일 AZ를 통한 데이터 저장
- 단일 AZ에 의한 데이터 접근 제한 (조금 낮은 가용성)
- 데이터 접근시 S3 - IA보다 20% 비용 저렴



#### Glacier

- 거의 접근하지 않을 데이터 저장 시 유용
- 매우 저렴한 비용
- 데이터 접근시 대략 4-5시간 소요

<img src="https://user-images.githubusercontent.com/76925694/109271011-42e6b780-7852-11eb-8113-413f52067c0b.png" alt="image" style="zoom:67%;" />



#### Intelligent Tiering

- 데이터 접근 주기가 불규칙할 때 매우 유용
- 2가지 티어 존재
  - Frequent Tier
  - Infrequent Tier
- 데이터 접근주기에 따라 두가지 티어중 하나로 선택됨
- Frequent Tier가 비용이 약간 더 비쌈
- 최고의 비용 절감 효율을 누릴 수 있음



#### S3 요금

- GB당 비용 측정
-  PUT, GET, COPY 요청 회수당
- 데이터 다운로드시 / 다른 리소스로 전송시
- Metadata (object tag)



## S3 - 버켓 생성시 알아야 할것들



#### S3 사용 용례

- 파일 저장소 (로그, 다양한 파일들(이미지, 비디오, 압축파일 등))

- 웹사이트 호스팅

- CORS(Cross Origin Resource Sharing)

  Buccket A에서 Bucket B에 들어있는 데이터 접근을 한다고 가정

  그렇다면 에러가 뜰것이다.

  이러한 문제를 해결하는 것이 CORS이다.

  

  최초 S3 버켓 생성시 -> 비공개(PRIVATE)

  외부에서 S3에 접근한다면 Access Denied가 뜰것이다.
  **위 문제 해결점**

  1. 버켓 정책 변경 (Bucket Policy)

  2. 접근 제어 리스트 변경 (Access Contol List)





## S3 - 암호화 (Encryption)



####  [1] 파일 업로드/다운로드시

- SSL(Secure Sockets Layer) / TLS(Transport Layer Secure)



#### [2] 가만히 있을시

**SSE(Server-Side Encryption)**

1. SSE-S3 
   - 마스터키(AES-256)를 가지고 있다. 일정시간 마다 key 값을 변경시킨다.
2. SSE-KMS
   - 암호화 key를 통하여 언제, 누가, 어떻게 암호를 풀었는지를 가지고 있음(SEE-S3는 이런 기능이 없다.)
3. SSE-C
   - 암호 key를 직접 다룰수 있다. 따라서 key 값을 우리가 변경시켜 줘야한다.



#### S3 암호화 과정



- PUT 요청이 생성됨

<img src="https://user-images.githubusercontent.com/76925694/109273243-462f7280-7855-11eb-8284-2d63c638f1b0.png" alt="image" style="zoom:67%;" />

<img src="https://user-images.githubusercontent.com/76925694/109273531-aaeacd00-7855-11eb-9fe2-7891d6fcb506.png" alt="image" style="zoom:67%;" />

x-amz-server-side-encryption-parameter에서 내가 원하는 암호화 기법을 제시할 수 있음





