# AWS Site-to-Site VPN이란 무엇입니까?



기본적으로 Amazon VPC로 시작하는 인스턴스는 자체(원격) 네트워크와 통신할 수 없습니다. AWS Site-to-Site VPN(Site-to-Site VPN) 연결을 생성하고 연결을 통해 트래픽을 전달하도록 라우팅을 구성하여 VPC에서 원격 네트워크에 대한 액세스를 활성화할 수 있습니다.



*VPN 연결*이라는 용어는 일반적인 용어지만 이 설명서에서 VPN 연결은 VPC와 자체 온프레미스 네트워크 간의 연결을 의미합니다. Site-to-Site VPN은 인터넷 프로토콜 보안(IPsec) VPN 연결을 지원합니다.



:bell: On-premise

> 프레미스(On-premise)란 소프트웨어 등 솔루션을 클라우드 같이 원격 환경이 아닌 자체적으로 보유한 전산실 서버에 직접 설치해 운영하는 방식을 말한다.



Site-to-Site VPN 연결은 AWS Classic VPN 또는 AWS VPN입니다. 자세한 내용은 [Site-to-Site VPN 범주](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/vpn-categories.html) 단원을 참조하십시오.

## 개념

다음은 Site-to-Site VPN의 주요 개념입니다.

- **VPN 연결**: 온프레미스 장비와 VPC 간의 보안 연결입니다.

- **VPN 터널**: 데이터가 고객 네트워크에서 AWS와 주고받을 수 있는 암호화된 링크입니다.

  각 VPN 연결에는 고가용성을 위해 동시에 사용할 수 있는 두 개의 VPN 터널이 포함되어 있습니다.

- **고객 게이트웨이**: 고객 게이트웨이 디바이스에 대한 정보를 AWS에 제공하는 AWS 리소스입니다.

- **고객 게이트웨이 디바이스**: Site-to-Site VPN 연결을 위해 고객 측에 설치된 물리적 디바이스 또는 소프트웨어 애플리케이션입니다.

- **가상 프라이빗 게이트웨이**: Site-to-Site VPN 연결의 Amazon 측에 있는 VPN 집선기입니다. 가상 프라이빗 게이트웨이나 전송 게이트웨이를 Site-to-Site VPN 연결의 Amazon 측 게이트웨이로 사용합니다.

- **전송 게이트웨이**: VPC와 온프레미스 네트워크를 상호 연결하는 데 쓸 수 있는 전송 허브입니다. 전송 게이트웨이나 가상 프라이빗 게이트웨이를 Site-to-Site VPN 연결의 Amazon 측 게이트웨이로 사용합니다.



## Site-to-Site VPN 구성 요소

Site-to-Site VPN 연결은 AWS 측의 가상 프라이빗 게이트웨이 또는 전송 게이트웨이와 원격(온프레미스) 측의 고객 게이트웨이(VPN 디바이스를 나타냄) 사이에 두 개의 VPN 터널을 제공합니다.



### 가상 프라이빗 게이트웨이(Virtual private gateway)

*가상 프라이빗 게이트웨이*는 Site-to-Site VPN 연결의 Amazon 측에 있는 VPN 집선기입니다. 가상 프라이빗 게이트웨이를 생성하여 Site-to-Site VPN 연결을 생성할 VPC에 연결합니다.

![image](https://user-images.githubusercontent.com/76925694/108033542-7d449d80-7077-11eb-9fe5-52d6401c3321.png)

가상 프라이빗 게이트웨이를 생성할 때 Amazon 측 게이트웨이의 프라이빗 자율 시스템 번호(ASN)를 지정할 수 있습니다. ASN을 지정하지 않는 경우 가상 프라이빗 게이트웨이는 기본 ASN(64512)으로 생성됩니다. 가상 프라이빗 게이트웨이를 만든 후에는 ASN을 변경할 수 없습니다. ASN에서 가상 프라이빗 게이트웨이를 확인하려면 Amazon VPC 콘솔의 **가상 프라이빗 게이트웨이** 화면에서 세부 정보를 보거나 [describe-vpn-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-gateways.html) AWS CLI 명령을 사용합니다.

### 전송 게이트웨이(transit gateway)

전송 게이트웨이는 가상 프라이빗 클라우드(VPC)와 온프레미스 네트워크를 상호 연결하는 데 사용할 수 있는 전송 허브입니다. 자세한 내용은 [Amazon VPC 전송 게이트웨이](https://docs.aws.amazon.com/vpc/latest/tgw/)를 참조하십시오. 전송 게이트웨이의 연결로 Site-to-Site VPN 연결을 생성할 수 있습니다.

![image](https://user-images.githubusercontent.com/76925694/108034620-1e802380-7079-11eb-9283-34467c72b8ef.png)

가상 프라이빗 게이트웨이에서 전송 게이트웨이로 Site-to-Site VPN 연결의 대상 게이트웨이를 수정할 수 있습니다. 자세한 내용은 [Site-to-Site VPN 연결의 대상 게이트웨이 수정](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/modify-vpn-target.html) 단원을 참조하십시오.

### 고객 게이트웨이 디바이스

*고객 게이트웨이 디바이스*는 Site-to-Site VPN 연결을 위해 고객 측에 설치된 물리적 디바이스 또는 소프트웨어 애플리케이션입니다. Site-to-Site VPN 연결로 작업하도록 디바이스를 구성 합니다. 자세한 내용은 [고객 게이트웨이 디바이스](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/your-cgw.html) 단원을 참조하십시오.

기본적으로 고객 게이트웨이 디바이스는 트래픽을 생성하고 IKE(Internet Key Exchange) 협상 프로세스를 시작하여 Site-to-Site VPN 연결을 위한 터널을 표시해야 합니다. 그 대신 AWS가 IKE 협상 프로세스를 시작해야 하는 것으로 지정하도록 Site-to-Site VPN 연결을 구성할 수 있습니다. 자세한 내용은 [Site-to-Site VPN 터널 시작 옵션](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/initiate-vpn-tunnels.html) 단원을 참조하십시오.

### 고객 게이트웨이

*고객 게이트웨이*는 온프레미스 네트워크의 고객 게이트웨이 디바이스를 나타내는 AWS에서 생성하는 리소스입니다. 고객 게이트웨이를 생성할 때 디바이스에 대한 정보를 AWS에 제공합니다. 자세한 내용은 [Site-to-Site VPN 연결을 위한 고객 게이트웨이 옵션](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/cgw-options.html) 단원을 참조하십시오.

Site-to-Site VPN 연결에서 Amazon VPC를 사용하려면 사용자 또는 네트워크 관리자가 원격 네트워크에서 고객 게이트웨이 디바이스 또는 애플리케이션도 구성해야 합니다. Site-to-Site VPN 연결을 생성하면 사용자에게 필요한 구성 정보가 제공되며 일반적으로 네트워크 관리자가 이 구성을 수행합니다. 고객 게이트웨이 요구 사항 및 구성에 대한 자세한 내용은 [고객 게이트웨이 디바이스](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/your-cgw.html) 단원을 참조하십시오.



#### 참조

- [AWS Site-to-Site VPN이란 무엇입니까?](https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/VPC_VPN.html)