# aws word summary

- **Elastic Beanstalk**
- **CloudTrail**

- **CloudFormation**
- **ECS**
- **Fargate**
- **Cognito**

- **SSL/TLS server certificates**

  > **AWS Certificate Manager(ACM)란 무엇입니까?**
  >
  > AWS Certificate Manager는 AWS 서비스 및 연결된 내부 리소스에 사용할 공인 및 사설 SSL/TLS(Secure Sockets Layer/전송 계층 보안) 인증서를 손쉽게 프로비저닝, 관리 및 배포할 수 있도록 지원하는 서비스입니다. SSL/TLS 인증서는 네트워크 통신을 보호하고 인터넷상에서 웹 사이트의 자격 증명과 프라이빗 네트워크상에서 리소스의 자격 증명을 설정하는 데 사용됩니다. AWS Certificate Manager는 SSL/TLS 인증서를 구매, 업로드 및 갱신하는 데 드는 시간 소모적인 수동 프로세스를 대신 처리합니다. AWS Certificate Manager에서는 사용자가 신속하게 인증서를 요청하고, Elastic Load Balancer, Amazon CloudFront 배포, API Gateway 기반 API와 같은 AWS 리소스에 배포한 후, AWS Certificate Manager가 인증서 갱신을 처리하도록 할 수 있습니다. 또한, 내부 리소스에 대한 사설 인증서를 생성하고 중앙에서 인증서 수명 주기를 관리할 수도 있습니다. AWS Certificate Manager를 통해 프로비저닝되고 ACM 통합 서비스(Elastic Load Balancing, Amazon CloudFront, Amazon API Gateway 등)에만 전용으로 사용되는 공인 및 사설 SSL/TLS 인증서는 무료입니다. 사용자는 애플리케이션을 실행하기 위해 생성한 AWS 리소스에 대한 비용을 지불합니다. 고객은 각 사설 CA의 운영에 대해 해당 CA를 삭제할 때까지 그리고 발급한 사설 인증서 중 [ACM 통합 서비스](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html) 이외 다른 서비스에서도 사용된 인증서에 대해 월별 요금을 지불합니다.

  > **SSL/TLS 인증서란 무엇입니까?**
  >
  > SSL/TLS 인증서는 SSL/TLS(Secure Sockets Layer/전송 계층 보안) 프로토콜을 사용하여 웹 브라우저가 웹 사이트에 대해 암호화된 네트워크 연결을 확인하고 설정할 수 있게 해줍니다. 인증서는 퍼블릭 키 인프라(PKI)로 알려진 암호화 시스템 내에서 사용됩니다. 양쪽 모두가 인증 기관으로 알려진 타사를 신뢰하는 경우, PKI는 한쪽에서 인증서를 사용하여 다른 쪽의 자격 증명을 설정할 수 있는 방법을 제공합니다. ACM 사용 설명서의 [개념](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html) 항목에 추가 배경 정보와 정의가 나와 있습니다.

- **AssumeRole**

  - https://docs.aws.amazon.com/ko_kr/STS/latest/APIReference/API_AssumeRole.html

- **X-Ray**
  **프로덕션 분산 애플리케이션의 분석 및 디버깅**

  > **AWS X-Ray는 개발자가 마이크로 서비스 아키텍처를 사용하여 구축 된 것과 같은 프로덕션 분산 애플리케이션을 분석하고 디버깅하는 데 도움이됩니다.** X-Ray를 사용하면 성능 문제 및 오류의 근본 원인을 식별하고 해결하기 위해 애플리케이션 및 기본 서비스의 성능을 이해할 수 있습니다. X-Ray는 요청이 애플리케이션을 통과 할 때 요청에 대한 종단 간보기를 제공하고 애플리케이션의 기본 구성 요소 맵을 표시합니다.
  >
  > X-Ray를 사용하여 AWS 계정에서 데이터를 수집 할 수 있습니다. X-Ray 에이전트는 실행중인 계정과 다른 계정에 데이터를 게시하는 역할을 맡을 수 있습니다. 이를 통해 애플리케이션의 다양한 구성 요소에서 중앙 계정으로 데이터를 게시 할 수 있습니다.

  - [https](https://aws.amazon.com/xray/) : [//aws.amazon.com/xray/](https://aws.amazon.com/xray/)

- **VPC 흐름 로그** 

  - VPC 흐름 로그는 VPC의 네트워크 인터페이스에서 송수신되는 IP 트래픽에 대한 정보를 캡처 할 수있는 기능입니다. 흐름 로그 데이터는 네트워크 추적을 분석하는 데 사용되며 네트워크 보안에 도움이됩니다. 흐름 로그 데이터는 Amazon CloudWatch Logs 또는 Amazon S3에 게시 할 수 있습니다. **VPC 흐름 로그를 사용하여 계정간에 데이터를 디버깅하고 추적 할 수 없습니다.**

- **CloudWatch Events**
  - Amazon CloudWatch Events는 Amazon Web Services (AWS) 리소스의 변경 사항을 설명하는 거의 실시간에 가까운 시스템 이벤트 스트림을 제공합니다. 이는 AWS 서비스에서 발생하는 변경 사항에 따라 알림을 트리거하는 데 도움이됩니다. CloudWatch 이벤트를 사용하여 계정간에 데이터를 디버깅하고 추적 할 수 없습니다.

- **CloudTrail** 
  - **CloudTrail을** 사용하면 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록하고, 지속적으로 모니터링하고, 유지할 수 있습니다. AWS CloudTrail을 사용하여 "이 리소스를 수정하기 위해 API를 호출 한 사람은 누구입니까?"와 같은 질문에 답할 수 있습니다. CloudTrail은 AWS 계정 활동의 이벤트 기록을 제공하여 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 가능하게합니다. **CloudTrail을 사용하여 계정간에 데이터를 디버깅하고 추적 할 수 없습니다.**
- **SSL / TLS**
  - https://blog.naver.com/PostView.nhn?blogId=nine01223&logNo=221593556488&parentCategoryNo=&categoryNo=16&viewDate=&isShowPopularPosts=false&from=postView

- **Application Load Balancer**

  - https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/introduction.html

-  AWS Serverless Application Model (AWS SAM)

  - SAM은 다음 리소스 유형을 지원합니다.

    - AWS :: 서버리스 :: Api

    - AWS :: 서버리스 :: 애플리케이션

    - AWS :: 서버리스 :: 기능

    - AWS :: 서버리스 :: HttpApi

    - AWS :: 서버리스 :: LayerVersion

    - AWS :: 서버리스 :: SimpleTable

    - AWS :: 서버리스 :: StateMachine

      **AWS :: Serverless :: Function-** 이 리소스는 함수를 트리거하는 Lambda 함수, IAM 실행 역할 및 이벤트 소스 매핑을 생성합니다.

      **AWS :: Serverless :: Api** -HTTPS 엔드 포인트를 통해 호출 할 수있는 Amazon API Gateway 리소스 및 메서드 모음을 생성합니다. API를 구성 할 때 완전한 제어와 유연성을 원하는 고급 사용 사례에 유용합니다.

      **AWS :: Serverless :: SimpleTable-** 단일 속성 기본 키가있는 DynamoDB 테이블을 생성합니다. 기본 키를 통해서만 데이터에 액세스해야 할 때 유용합니다.

- **UserPool**

  - UserPool은 모바일 앱 및 웹 인증에 사용되는 Cognito 서비스에 적용됩니다. 서버리스 애플리케이션 모델에는 UserPool이라는 리소스가 없습니다.

- **CNAME swap**

  - EB(Elastic Beanstalk)에서 나오는 개념
  - 말그대로 2개의 리소스? 코드?를 swap

- **AWS Elastic Beanstalk에 대한 구성 파일을 생성 할 때 따라야하는 명명 규칙은 무엇입니까?**

  - .ebextensions/<mysettings>.config
    - `.ebextensions`웹 애플리케이션의 소스 코드에 AWS Elastic Beanstalk 구성 파일 ( )을 추가 하여 환경을 구성하고 여기에 포함 된 AWS 리소스를 사용자 지정할 수 있습니다. 구성 파일은 .ebextensions라는 폴더에 배치하고 애플리케이션 소스 번들에 배포하는 .config 파일 확장자가있는 YAML 또는 JSON 형식 문서입니다.

- KMS(AWS **K**ey **M**anagement **S**ervice(KMS))

  > AWS KMS(Key Management Service)를 사용하면 손쉽게 암호화 키를 생성 및 관리하고 다양한 AWS 서비스와 애플리케이션에서의 사용을 제어할 수 있습니다. AWS KMS는 FIPS 140-2에 따라 검증되었거나 검증 과정에 있는 하드웨어 보안 모듈을 사용하여 키를 보호하는 안전하고 복원력 있는 서비스입니다. 또한, AWS KMS는 AWS CloudTrail과도 통합되어 모든 키 사용에 관한 로그를 제공함으로써 각종 규제 및 규정 준수 요구 사항을 충족할 수 있게 지원합니다.

  - https://aws.amazon.com/ko/kms/

- AWS CloudHSM

  **AWS 클라우드상의 관리형 하드웨어 보안 모듈(HSM).**

  - https://aws.amazon.com/ko/cloudhsm/

  > AWS CloudHSM은 AWS 클라우드에서 자체 암호화 키를 손쉽게 생성 및 사용할 수 있도록 지원하는 클라우드 기반 하드웨어 보안 모듈(HSM)입니다. CloudHSM에서는 FIPS 140-2 레벨 3 인증 HSM을 사용하여 자체 암호화 키를 관리할 수 있습니다. CloudHSM은 PKCS#11, Java Cryptography Extensions(JCE) 및 Microsoft CryptoNG(CNG) 라이브러리와 같은 업계 표준 API를 사용하여 애플리케이션과 통합할 수 있는 유연성을 제공합니다.
  >
  > CloudHSM은 표준을 준수하며 구성에 따라 모든 키를 대부분의 상용 HSM으로 내보낼 수 있습니다. 사용자를 위해 하드웨어 프로비저닝, 소프트웨어 패치, 고가용성, 백업 등 시간 소모적인 관리 작업을 자동화하는 완전관리형 서비스입니다. 또한, CloudHSM을 사용하면 선결제 비용 없이 온디맨드로 HSM 용량을 추가 및 제거하여 신속하게 확장/축소할 수 있습니다.

- **KMS**

  **KMS는 CMK를 저장하고 클라이언트로부터 데이터를 수신하여 암호화하고 다시 보냅니다.**

  고객 마스터 키 (CMK)는 마스터 키의 논리적 표현입니다. CMK에는 키 ID, 생성 날짜, 설명 및 키 상태와 같은 메타 데이터가 포함됩니다. CMK에는 데이터 암호화 및 해독에 사용되는 키 자료도 포함되어 있습니다. KMS, AWS CloudHSM 클러스터에서 CMK를 생성하거나 키 관리 인프라에서 가져올 수 있습니다.

  AWS KMS는 대칭 및 비대칭 CMK를 지원합니다. 대칭 CMK는 암호화 및 암호 해독에 사용되는 256 비트 키를 나타냅니다. 비대칭 CMK는 암호화 및 복호화 또는 서명과 확인 (둘다는 아님)에 사용되는 RSA 키 쌍 또는 서명 및 확인에 사용되는 ECC (타원 곡선) 키 쌍을 나타냅니다.

  AWS KMS는 고객 관리 형 CMK, AWS 관리 형 CMK 및 AWS 소유 CMK의 세 가지 유형의 CMK를 지원합니다.

  ~~KMS는 암호화 호출마다 클라이언트로부터 CMK를 수신하고이를 통해 데이터를 암호화합니다~~ .-자신의 CMK (고객 마스터 키)를 가져올 수 있지만 한 번만 수행하면 필요에 따라 암호화 / 복호화 할 수 있습니다.

  ~~KMS는 CMK를 클라이언트에 전송하여 암호화를 수행 한 다음 CMK를 삭제합니다.~~ KMS는 CMK를 클라이언트에 전송하지 않고 KMS 자체가 암호화 한 다음 데이터를 해독합니다.

  ~~KMS는 각 Encrypt 호출에 대해 새 CMK를 생성하고 데이터를 암호화합니다.~~ KMS는 매번 새 키를 생성하지 않지만 KMS가 키를 교체하도록 할 수 있습니다. 모범 사례는 암호화 키의 광범위한 재사용을 권장하지 않으므로 새 키를 생성하는 것이 좋습니다.

- **MFA**

  - **SMS 문자 메시지 기반 MFA**
    - IAM 사용자 설정에 사용자의 SMS 호환 모바일 디바이스의 전화 번호가 포함 된 MFA 유형입니다. 사용자가 로그인하면 AWS는 SMS 문자 메시지로 6 자리 숫자 코드를 사용자의 모바일 디바이스로 보냅니다. 사용자는 로그인하는 동안 두 번째 웹 페이지에 해당 코드를 입력해야합니다. **SMS 기반 MFA는 IAM 사용자 만 사용할 수 있으며 AWS 계정 루트 사용자로는이 유형의 MFA를 사용할 수 없습니다.**
  - **하드웨어 MFA 디바이스**
    - 이 하드웨어 디바이스는 6 자리 숫자 코드를 생성합니다. 사용자는 로그인하는 동안 두 번째 웹 페이지에 장치에서이 코드를 입력해야합니다. 사용자에게 할당 된 각 MFA 디바이스는 고유해야합니다. 사용자는 인증 할 다른 사용자의 장치에서 코드를 입력 할 수 없습니다. **루트 사용자 인증에 사용할 수 있습니다.**
  - **U2F 보안 키** 
    - 컴퓨터의 USB 포트에 연결하는 장치입니다. U2F는 FIDO Alliance에서 호스팅하는 개방형 인증 표준입니다. U2F 보안 키를 활성화하면 수동으로 코드를 입력하는 대신 자격 증명을 입력 한 다음 장치를 탭하여 로그인합니다. **루트 사용자 인증에 사용할 수 있습니다.**

  - **가상 MFA 디바이스** 

    - 휴대폰 또는 기타 디바이스에서 실행되고 물리적 디바이스를 에뮬레이트하는 소프트웨어 앱입니다. 장치는 6 자리 숫자 코드를 생성합니다. 사용자는 로그인하는 동안 두 번째 웹 페이지에 장치의 유효한 코드를 입력해야합니다. 사용자에게 할당 된 각 가상 MFA 디바이스는 고유해야합니다. 사용자는 다른 사용자의 가상 MFA 디바이스에서 코드를 입력하여 인증 할 수 없습니다. **루트 사용자 인증에 사용할 수 있습니다.**

    