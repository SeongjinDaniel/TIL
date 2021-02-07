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



---

## 

## AAA란 무엇인가?

![image](https://user-images.githubusercontent.com/55625864/107138249-b33aa100-6956-11eb-8832-e2fd253fb258.png)

![image](https://user-images.githubusercontent.com/55625864/107138289-fe54b400-6956-11eb-9a81-a3dbe1c1149a.png)

##  

## 인증(Authenticate)

![image](https://user-images.githubusercontent.com/55625864/107138299-0f052a00-6957-11eb-97c0-9b82466a37e3.png)



## MFA(Multi Factor Authentication)

- 누군가가 사용자의 **계정정보를 취득했더라도 비인가된 접근을 막아줌**
- **마스터 계정 / AWS IAM Users**에 적용 가능
- 아래 서비스/콘솔과 **통합**되어 있음.
  - AWS Management Console
  - S3(Secure Delete)
- **Virtual** MFA device / **Hardware** MFA device

![image](https://user-images.githubusercontent.com/55625864/107138373-660aff00-6957-11eb-9f8b-d07314743a0e.png)



## 인가(Authorize)

- 정책(Poicy) = Permission
  - "AWS 리소스에 대하여 누가, 어떤 Action을 수행할 수 있는가?"
  - JSON 형식으로 구성

| 유저 기반 정책(AWS IAM Policy)   | 리소스 기반 정책                                             |
| -------------------------------- | ------------------------------------------------------------ |
| - 사용자<br />- 그룹<br />- Role | - Amazon S3 buckets(policy)<br />- Amazon Glacier vaults<br />- Amazon SNS topics<br />- Amazon SQS queues<br />- VPC Endpoints<br />- AWS key Management Service encryption keys |



#### Amazon S3 Glacier이란 무엇입니까?

Amazon S3 Glacier는 데이터 보관 및 장기 백업을 위한 안전하고 안정적이며 비용이 매우 저렴한 Amazon S3 스토리지 클래스입니다.



S3 Glacier 고객은 데이터를 수개월, 수년 혹은 수십년까지 비용 효율적으로 저장할 수 있습니다. 또한 고객은 S3 Glacier를 통해 스토리지 운영 및 조정에 따른 관리 부담을 AWS에게 이관하여 용량 계획, 하드웨어 프로비저닝, 데이터 복제, 하드웨어 장애 탐지 및 복구, 시간이 오래 걸리는 하드웨어 마이그레이션 등에 대해 걱정할 필요가 없습니다.



#### ARN(Amazon Resource name)

- ARN (Amazon Resource Name)은 **AWS 리소스를 고유하게 식별**

- 모든 AWS 리소스는 고유한 자신의 ARN을 소유함

  ```
  ARN으로 정의 되는 리소스의 예: EC2 인스턴스, DynamoDB table, AWS IAM User 등
  * 주) EC2에 설치되는 OS 및 EBS 볼륨에 저장된 데이터는 AWS 리소스가 아님
  ```

  arn:aws:service:region:account-id:resource-type:resource

  arn:aws:service:region:account-id:resource-type/resource

**Amazon EC2 instance**

- arn:aws:ec2:us-east-1:123456789012:instance/i-1a2b3c4d

**Amazon RDS tag**

- arn:aws:rds:eu-west-1:001234567890:db:mysql-db



#### 정책(Policy) 구성요소 살펴보기

- **E**ffect - 접근을 허용하거나 명시적으로 **거부**
- **P**rincipal - **누가** 어떤 것을 할 수 있는지/없는지 (Resource-based Policy)
- **A**ction - **무엇**을 **할 수** 있는지/없는지
- **R**esource - 이 정책이 **적용되는 리소스**가 어떤 것인지
- **C**ondition - 이 정책이 **적용되는 조건**이 무엇인지

![image](https://user-images.githubusercontent.com/55625864/107145484-2529df00-6985-11eb-9f04-aaafa333ebc8.png)

---

 

## AWS IAM Role

- AWS의 **작업과 리소스에 대한 액세스를 부여**하는 권한 세트
- **정의된 권한**을 **다른 사용자나 서비스로 위임**
- AWS IAM users 또는 AWS services는 role에서 정의된 권한범위 내 AWS API를 사용할 수 있는 'temporary security credentials'를 얻을 수 있음
- **사용 예시**
  - EC2 role
  - Federations : Cross-Account, SAML2.0, Web Identity Provider
- 장점
  - 보안 향상: **보안 자격증명을 공유할 필요가 없음**
  - 강력한 권한 제어: 언제든지 **접근 권한 회수**가 가능
  - 각 사용자에게 매번 필요한 권한을 **일일이 부여할 필요 없음**



- EC2에서 S3에 접근해야 하는경우 Access Key와 같은 명시적인 권한 증명 없이 "EC2에 Role을 할당하여 접근"



## Identity Federation: Pain Point

![image](https://user-images.githubusercontent.com/55625864/107145790-50153280-6987-11eb-98d8-756bf3b82601.png)

![image](https://user-images.githubusercontent.com/55625864/107145799-5efbe500-6987-11eb-80f4-718344357e92.png)



## Audit(감사)

#### CloudTrail: 모든 Log를 모아모아 한곳으로

- AWS **IAM과 통합**
- CloudTrail을 활용: 유저를 6가지로 나누어 기록됨
  - Root / AWS IAM User / Assume Role / Federated User / Other Account / AWS Services
- AWS **계정 단위**로 이벤트 기록
- AWS에 요청되어 **승인된 모든 API call**들을 **로깅**
- 모든 리전의 로그를 하나의 **S3 bucket**에 통합 저장
- AWS KMS를 통해 **로그 파일 암호화** 가능(**권장**)
- **위변조에 대비**하기 위해 **Log File Integrity** (LFI) 체크 가능(**권장**)



## AWS IAM 모범사례

1. **Users** - 개별 사용자 생성
2. **Password** - 강력한 암호 정책 설정
3. **Rotate** - 보안 자격 증명을 정기적으로 순환
4. **MFA** - 권한이 있는 사용자에 대해 MFA 활성화
5. **Groups** - 권한 관리에 그룹 사용
6. **Permissions** - 최소한의 권한만 부여
7. **Sharing** - 접근제어를 공유하기 위해 AWS IAM Role 사용
8. **Role** - Amazon EC2 instances에 AWS IAM Role 사용
9. **Auditing** - API 호출 로그를 얻기 위해 AWS CloudTrail 활성화
10. **Root** - Root 계정의 사용을 줄이거나 없앰



#### 1. 개별 사용자 생성

**DO**

- 관리자 스스로도 AWS IAM 사용자 생성하여 그것을 이용
- 다른 사람들에게도 각각 사용자 생성하여 이용하도록 함

**Don't**

- Root 자격증명을 공유하거나 배포 (절대반지 대여)
- Root 계정 직접 사용 (절대반지 직접 착용)

**Benefits**

- 개별 자격증명 세트 관리
- 개별 권한 부여
- 세밀한 제어 가능
- 접근 권한 회수가 쉬움

#### **2. 강력한 암호 정책** 설정

**DO**

- 암호 만료 기한 설정
- 암호 정책은 강력하게(예시):
  - 암호 길이 최소 14이상
  - 한 개 이상 대문자 포함
  - 한 개 이상 소문자 포함
  - 특수문자 한 개 이상 포함
  - 숫자 한 개 이상 포함

**Benefits**

- 사용자와 그 데이터가 안전하게 보호됨
- 암호 복잡도에 대한 요구사항을 쉽게 만족시키고 적용 가능
- Brute Force 로그인 시도에 대한 안전도 상승

**패스워드 정책 관리**

- 사용자는 **다음 로그인 시에 암호 정책을 준수**하는지 확인

- ![image](https://user-images.githubusercontent.com/55625864/107146316-b18ad080-698a-11eb-8287-08f1991fcd02.png)



#### 3. 보안 자격 증명을 정기적으로 순환

**DO**

- AWS IAM users에 대해 보안 자격 증명 활성화
- 보안 자격 증명 순환 여부 확인/감사를 위해 Credential Report 를 활용
- **Credential Report** 의 **Access Key Last Used** 컬럼을 통해 일정 기간(예: 90일 이상)

**Benefits**

- 인가되지 않은 접근의 가능성을 최대한 낮춰줌

- 오래된 키가 도난당하거나 잃어버린 상태라고 해도 그 키를 통해 데이터에 접근하는 것을 방지할 수 있음

  

- ![image](https://user-images.githubusercontent.com/55625864/107146403-56a5a900-698b-11eb-8eeb-1e82bd27cc56.png)



#### 4. 권한이 있는 사용자에 대해 MFA 활성화

**DO**

- Root account에 대하여 **MFA** 활성화
- 민감한 action들에 대해서는 **MFA**로 보호

**Benefits**

- 추가적인 보호막 제공
- 콘솔과 programmatic 접근에 대한 보안 향상



#### 5. 권한 관리에 그룹 사용

**DO**

- 업무 기능과 연관된 그룹을 생성(Dev, Ops, QA, ...)
- 그룹에 정책(poicy)들을 붙임
- 그룹 멤버십을 권한 부여/회수하는데 사용

**Benefits**

- 사용자 증가에 따라 늘어나는 접근 제어 관리의 복잡도를 감소시킬 수 있음
- 사용자들이 갑자기 의도치 않게 과한 접근권한을 얻게 되는 일을 방지하거나 줄임
- 현재 직군의 role이 변경되었을 경우 (혹은 팀이 바뀐 경우) 쉽게 권한을 다시 할당
- 여러 사용자의 권한을 업데이트할 수 있는 쉬운 방법



#### 6. 최소한의 권한만 부여

**DO**

- 최소한의 권한 세트만으로 시작한 후에 필요에 따라 권한을 추가
- 특권에 대해서는 **Conditions**을 이용해 접근 제어
- 정기적으로 **Access Advisor**를 체크하여 권한을 제한
- **Resource-based** 정책을 이용해 특정 resource에 대한 접근 제어

**Benefits**

- 실수로 특권을 행사할 가능성을 최소화
- 서서히 풀어주는 것이 갑자기 조이는 것보다 쉬움
- 좀 더 정교한 제어 가능

**Access Advisor**

- ![image](https://user-images.githubusercontent.com/55625864/107146743-5e664d00-698d-11eb-9c02-3f4a69bc16f5.png)



#### 7. 접근제어를 공유하기 위해 AWS IAM Role 사용

**DO**

- 다음의 경우 Role 사용
  - 계정 간 접근 권한 위임
  - 동일 계정 내에 접근권한 위임
  - 연동된 사용자(federated users)

**Beefits**

- 보안 자격증명을 더 이상 **공유**할 필요 없음
- 장기(long-term) 자격증명을 **보관**할 필요 없음
- 누가 접근권한이 있는지를 **제어함**



#### 8. Amazon EC2 instances에 AWS IAM Role 사용

**DO**

- 장기(long-term) 자격증명을 사용하지 말고 Role을 사용
- 어플리케이션에 최소한의 권한만을 부여

**Benefits**

- EC2 instances 상의 access keys를 관리하기 쉬움
- Key 순환의 자동화
- AWS SDKs와 완전히 통합
- AWS CLI와 완전히 통합



#### 9. API 호출 로그를 얻기 위해 AWS CloudTrail 활성화

**DO**

- 모든 리전에서 **AWS CloudTrail**를 활성화
- **AWS CloudTrail**에서 **Log File Validation**가 활성화 되어 있는 것을 확인
- **CloudTrail** 로그를 저장하는 **Amazon S3** 버킷이 퍼블릭하게 접속 가능하지 않도록 설정

**Benefits**

- 각 계정의 API 활동내역을 모니터링 할 수 있음
- 보안 분석, 리소스 분석, 컴플라이언스 감사 등을 가능하게 함



**10. Reduce or remove use of root**

**DO**

- Root account 사용자에 대해 **MFA** 활성화
- 가능하면, root access keys를 삭제
- 각 계정들에 대하여 안전한(강력한) 비밀번호 사용

**Benefits**

- 우발적인 변경 및 고도의 권한이 부여 된 자격 증명의 의도하지 않은 노출과 같은 위험을 줄임



## Summary

- AWS IAM은 **AWS 계정과 AWS 리소스**들에 대해 **누가 어떤것을 할 수 있는지**를 **제어**하고 **관리**합니다.

- AWS IAM은 **기존**에 사용하던 **사용자 관리 환경과 연동**(federation) 가능합니다.
- AWS IAM 자격 **증명 연동(Identity Federation)**을 사용하면 AWS IAM 사용자를 생성하지 않고 외부 자격 증명으로 AWS 계정의 리소스에 안정하게 액세스할 수 있습니다.
- AWS IAM을 통해 사용자 관리를 수행할 때는 **모범 사례 10가지를 참조**하는 것이 좋습니다.





- **참조**
  - [IAM이란 무엇인가요?](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)
  - [클라우드 여정을 성공적으로 수행하기 위한 AWS IAM 활용 전략::최원근:: AWS Summit Seoul 2018](https://www.slideshare.net/awskorea/aws-iam-usaged-strategy-for-successful-cloud-journey-wonkeun-choi)