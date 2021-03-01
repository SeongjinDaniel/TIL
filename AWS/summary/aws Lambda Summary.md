# aws Lambda Summary



## AWS Lambda (기본)



- Serverless의 주축을 담당
- Events를 통하여 Lambda를 실행시킴
- NodeJS, Python, Java, GO등 다양한 언어 지원
- Lambda Function



## AWS Lambda (비용)



- Lambda Function이 실행될때만 돈 지불
- 매달 10,000,.000번 함수 호출 시 무료 (그 후로는 유료)



## AWS Lambda (기타)

- 최대 300초(5분)

- 512MB의 일시적인 디스크 공간 제공(/tmp/)
- 최대 50MB Deployment Package 허용



#### 사용 용례 (1)

- **S3 -> Lambda -> Database**
  - PutObject 이벤트로 S3에 파일을 업로드
- **IoT -> Lambda -> SNS**
  - IoT에서는 Topic이라는 것을 통해 IoT를 관리하게 됌

<img src="https://user-images.githubusercontent.com/76925694/109381101-97099e80-791b-11eb-871d-35b653fd51df.png" alt="image" style="zoom:80%;" />