# AWS IAM이란?



- **AWS Identity and Access Management(IAM)**

  - **IAM는 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다.** IAM을 사용하여 리소스를 사용하도록 인증(로그인) 및 권한 부여(권한 있음)된 대상을 제어합니다.

  AWS 계정을 처음 생성할 때는 해당 계정의 모든 AWS 서비스 및 리소스에 대한 완전한 액세스 권한이 있는 SSO(Single Sign-On) ID로 시작합니다. 이 자격 증명은 AWS 계정 루트 사용자라고 하며, 계정을 생성할 때 사용한 이메일 주소와 암호로 로그인하여 액세스합니다. 일상적인 작업은 물론 관리 작업에도 루트 사용자를 사용하지 않는 것이 좋습니다. 대신 IAM 사용자를 처음 생성할 때만 루트 사용자를 사용하는 모범 사례를 준수하십시오. 그런 다음 루트 사용자 자격 증명을 안전하게 보관해 두고 몇 가지 계정 및 서비스 관리 작업을 수행할 때만 해당 자격 증명을 사용합니다.

## AWS IAM으로 뭘 할 수 있나요?

- AWS **서비스와 리소스에 대한 액세스**를 안전하게 관리
- AWS **사용자 및 그룹**을 만들고 관리
- **권한**을 사용해 **AWS 리소스**에 대한 **액세스를 허용 및 거부**

> **AWS 리소스**는 Amazon Elastic Compute Cloud(EC2) 인스턴스, Amazon Elastic Block Store(EBS) 볼륨, 보안 그룹 또는 Amazon Virtual Private Cloud(VPC)와 같이 AWS에서 사용할 수 있는 개체입니다. AWS Config에서 지원되는 AWS 리소스의 전체 목록은 지원되는 리소스 유형 단원을 참조하십시오. 참고 : [AWS Config란 무엇입니까?](https://docs.aws.amazon.com/ko_kr/config/latest/developerguide/WhatIsConfig.html)

## AWS IAM은 어떤 점이 좋은가요?

- AWS 리소스에 대한 사용자의 **액세스를 세부적으로 제어**
- 대부분의 **AWS 서비스 내에 통합**
- **유연한** 보안 자격 증명 관리
- 기존 자격 증명 시스템 활용 (**Federation**)
- AWS 계정에서 추가 비용 없이 제공되는 기능 (사용자가 사용한 다른 AWS 서비스에 대해서만 요금 부과)



- **참조**
  - [IAM이란 무엇인가요?](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)
  - [클라우드 여정을 성공적으로 수행하기 위한 AWS IAM 활용 전략::최원근:: AWS Summit Seoul 2018](https://www.slideshare.net/awskorea/aws-iam-usaged-strategy-for-successful-cloud-journey-wonkeun-choi)