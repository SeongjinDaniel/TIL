# AWS IAM Documentation 정리



# IAM이란 무엇인가요?

AWS Identity and Access Management(IAM)는 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. IAM을 사용하여 리소스를 사용하도록 인증(로그인) 및 권한 부여(권한 있음)된 대상을 제어합니다.



AWS 계정을 처음 생성할 때는 해당 계정의 모든 AWS 서비스 및 리소스에 대한 완전한 액세스 권한이 있는 SSO(Single Sign-In) ID로 시작합니다. 이 자격 증명은 AWS 계정 *루트 사용자*라고 하며, 계정을 생성할 때 사용한 이메일 주소와 암호로 로그인하여 액세스합니다. 일상적인 작업은 물론 관리 작업에도 루트 사용자를 사용하지 않는 것이 좋습니다. 대신 [IAM 사용자를 처음 생성할 때만 루트 사용자를 사용하는 모범 사례](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users)를 준수하십시오. 그런 다음 루트 사용자 자격 증명을 안전하게 보관해 두고 몇 가지 계정 및 서비스 관리 작업을 수행할 때만 해당 자격 증명을 사용합니다.



## IAM 기능

#### AWS 계정에 대한 공유 액세스

- 암호나 액세스 키를 공유하지 않고도 AWS 계정의 리소스를 관리하고 사용할 수 있는 권한을 다른 사람에게 부여할 수 있습니다.

#### 세분화된 권한

- 리소스에 따라 여러 사람에게 다양한 권한을 부여할 수 있습니다. 예를 들어 일부 사용자에게는 Amazon Elastic Compute Cloud(Amazon EC2), Amazon Simple Storage Service(Amazon S3), Amazon DynamoDB, Amazon Redshift 및 기타 AWS 서비스에 대한 전체 액세스 권한을 허용하고 다른 사용자에게는 일부 S3 버킷에 대한 읽기 전용 권한, 일부 EC2 인스턴스를 관리할 수 있는 권한 또는 결제 정보에만 액세스할 수 있는 권한을 허용할 수 있습니다.

#### Amazon EC2에서 실행되는 애플리케이션을 위한 보안 AWS 리소스 액세스

- EC2 인스턴스에서 실행되는 애플리케이션의 경우 IAM 기능을 사용하여 자격 증명을 안전하게 제공할 수 있습니다. 이러한 자격 증명은 애플리케이션에 다른 AWS 리소스에 액세스할 수 있는 권한을 제공합니다. 예를 들면 이러한 리소스에는 S3 버킷 및 DynamoDB 테이블이 있습니다.

#### 멀티 팩터 인증(MFA)

- 보안 강화를 위해 계정과 개별 사용자에게 2팩터 인증을 추가할 수 있습니다. MFA를 사용할 경우 계정 소유자나 사용자가 계정 작업을 위해 암호나 액세스 키뿐 아니라 특별히 구성된 디바이스의 코드도 제공해야 합니다.

#### 자격 증명 연동

- 기업 네트워크나 인터넷 자격 증명 공급자와 같은 다른 곳에 이미 암호가 있는 사용자에게 AWS 계정에 대한 임시 액세스 권한을 부여 할 수 있습니다.

#### 보장을 위한 자격 증명 정보

- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)을 사용하는 경우 계정의 리소스를 요청한 사람에 대한 정보가 포함된 로그 레코드를 받게 됩니다. 이 정보는 IAM 자격 증명을 기반으로 합니다.

#### PCI DSS 준수

- IAM에서는 전자 상거래 웹사이트 운영자 또는 서비스 공급자에 의한 신용 카드 데이터의 처리, 저장 및 전송을 지원하며, Payment Card Industry(PCI) Data Security Standard(DSS) 준수를 검증 받았습니다. AWS PCI 규정 준수 패키지의 사본을 요청하는 방법 등 PCI DSS에 대해 자세히 알아보려면 [PCI DSS 레벨 1](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/)을 참조하십시오.

#### 많은 AWS 서비스와의 통합

- IAM과 함께 사용할 수 있는 AWS 서비스의 목록은 [IAM으로 작업하는 AWS 서비스](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html)를 참조하십시오.

#### 최종 일관성

- IAM은 다른 많은 AWS 서비스처럼 [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency)에 해당됩니다. IAM에서는 전 세계의 Amazon 데이터 센터 내의 여러 서버로 데이터를 복제함으로써 고가용성을 구현합니다. 일부 데이터를 변경하겠다는 요청이 성공하면 변경이 실행되고 그 결과는 안정하게 저장됩니다. 그러나 변경 사항은 IAM에 두루 복제되어야 하고, 여기에는 일정한 시간이 걸립니다. 그러한 변경 사항에는 사용자, 그룹, 역할 또는 정책을 만들거나 업데이트한 것이 포함됩니다. 그러한 IAM 변경 사항을 애플리케이션의 중요한 고가용성 코드 경로에 포함시키지 않는 것이 좋습니다. 대신 자주 실행하지 않는 별도의 초기화 루틴이나 설정 루틴에서 IAM을 변경하십시오. 또한 프로덕션 워크플로우에서 변경 사항을 적용하기 전에 변경 사항이 전파되었는지 확인하십시오. 자세한 내용은  [변경 사항이 매번 즉시 표시되는 것은 아닙니다](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) 섹션을 참조하세요.

#### 무료 사용

AWS Identity and Access Management(IAM) 및 AWS Security Token Service(AWS STS)은 추가 비용 없이 AWS 계정에 제공되는 기능입니다. IAM 사용자 또는 AWS STS 임시 보안 자격 증명을 사용하여 다른 AWS 서비스에 액세스하는 경우에만 요금이 부과됩니다. 다른 AWS 제품 요금에 대한 자세한 내용은 [Amazon Web Services 요금 페이지](https://aws.amazon.com/pricing/)를 참조하십시오.



## IAM에 액세스

다음 방법 중 하나를 사용하여 AWS Identity and Access Management(으)로 작업할 수 있습니다.



#### AWS Management 콘솔

- 콘솔은 IAM 및 AWS 리소스를 관리하기 위한 브라우저 기반 인터페이스입니다. 콘솔을 통한 IAM 액세스에 대한 자세한 내용은 [IAM 사용자 또는 루트 사용자로 AWS Management 콘솔에 로그인](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/console.html) 단원을 참조하십시오. 콘솔 사용법을 안내하는 자습서는 [첫 번째 IAM 관리자 및 그룹 생성](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/getting-started_create-admin-group.html)을 참조하십시오.

#### AWS 명령줄 도구

- AWS 명령줄 도구를 통해 시스템 명령줄에서 명령을 실행하여 IAM 및 AWS 작업을 수행할 수 있습니다. 명령줄을 사용하는 것이 콘솔을 사용하는 것보다 더 빠르고 편리할 수 있습니다. AWS 작업을 수행하는 스크립트를 작성할 때도 명령줄 도구가 유용합니다.

  AWS에서는 [AWS Command Line Interface](https://aws.amazon.com/cli/)(AWS CLI) 및 [Windows PowerShell용 AWS 도구](https://aws.amazon.com/powershell/)라는 두 가지 명령줄 도구 세트를 제공합니다. AWS CLI 설치 및 사용에 대한 자세한 내용은 [AWS Command Line Interface 사용 설명서](https://docs.aws.amazon.com/cli/latest/userguide/) 단원을 참조하십시오. Windows PowerShell용 도구 설치 및 사용에 대한 자세한 내용은 [Windows PowerShell용 AWS 도구 사용 설명서](https://docs.aws.amazon.com/powershell/latest/userguide/) 단원을 참조하십시오.

#### AWS SDK

- AWS에서는 다양한 프로그래밍 언어 및 플랫폼(Java, Python, Rubu, .NET, iOS, Android 등)을 위한 라이브러리와 샘플 코드로 구성된 소프트웨어 개발 키트(SDK)를 제공합니다. SDK를 사용하면 편리하게 IAM 및 AWS에 프로그래밍 방식으로 액세스할 수 있습니다. 예를 들어 SDK는 요처어에 암호화 방식으로 서명, 오류 관리 및 자동으로 요청 재시도와 같은 작업을 처리합니다. 다운로드 및 설치 방법을 비롯하여 AWS SDK에 대한 자세한 내용은 [Amazon Web Services용 도구](https://aws.amazon.com/tools/) 페이지를 참조하십시오.

#### IAM HTTPS API

- 서비스로 직접 HTTPS 요청을 실행할 수 있는 IAM HTTPS API를 사용하여 프로그래밍 방식으로 IAM 및 AWS에 액세스할 수 있습니다. HTTPS API를 사용할 때는 자격 증명을 사용하여 요청에 디지털 방식으로 서명하는 코드를 포함해야 합니다. 자세한 내용은 [HTTP 쿼리 요청을 사용하여 IAM API 호출](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/programming.html) 및 [IAM API Reference](https://docs.aws.amazon.com/IAM/latest/APIReference/) 섹션을 참조하세요.







#### 참조

- [IAM이란 무엇인가요?](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)