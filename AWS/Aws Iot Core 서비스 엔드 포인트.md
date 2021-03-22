## AWS IoT Core 서비스 엔드포인트



서비스 엔드포인트는 AWS IoT Core 솔루션을 제어하고 관리하는 함수에 대한 액세스를 제공합니다. AWS IoT

- **Endpoints**

  서비스 엔드포인트는 리전별로 다르며 AWS IoT CoreAWS [코어 엔드포인트 및 할당량IoT에 나열되어 있습니다.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html) 서비스 엔드포인트의 형식은 다음과 같습니다.AWS IoT Core

| 엔드포인트 용도          | 엔드포인트 형식                                              |
| :----------------------- | :----------------------------------------------------------- |
| AWS IoT Core 컨트롤      | `iot.aws-region.amazonaws.com`                               |
| AWS IoT Core 데이터      | [디바이스 엔드포인트AWS IoT](https://docs.aws.amazon.com/ko_kr/iot/latest/developerguide/connect-to-iot.html#iot-device-endpoint-intro) 단원을 참조하십시오. |
| AWS IoT Core 작업 데이터 | `data.jobs.iot.aws-region.amazonaws.com`                     |
| AWS IoT Core 보안 터널링 | `api.tunneling.iot.aws-region.amazonaws.com`                 |

| 리전 이름                  | 리전           | Endpoint                         | Protocol |
| :------------------------- | :------------- | :------------------------------- | :------- |
| 미국 동부(오하이오)        | us-east-2      | iot.us-east-2.amazonaws.com      | HTTPS    |
| 미국 동부(버지니아 북부)   | us-east-1      | iot.us-east-1.amazonaws.com      | HTTPS    |
| 미국 서부(캘리포니아 북부) | us-west-1      | iot.us-west-1.amazonaws.com      | HTTPS    |
| 미국 서부(오레곤)          | us-west-2      | iot.us-west-2.amazonaws.com      | HTTPS    |
| 아시아 태평양(홍콩)        | ap-east-1      | iot.ap-east-1.amazonaws.com      | HTTPS    |
| 아시아 태평양(뭄바이)      | ap-south-1     | iot.ap-south-1.amazonaws.com     | HTTPS    |
| 아시아 태평양(서울)        | ap-northeast-2 | iot.ap-northeast-2.amazonaws.com | HTTPS    |



### AWS IoT Core for LoRaWAN 게이트웨이 및 디바이스

AWS IoT Core for LoRaWAN는 무선 게이트웨이와 디바이스를 AWS IoT Core에 연결합니다.

- **Endpoints**

  AWS IoT Core for LoRaWAN는 계정 및 리전별 AWS IoT Core 엔드포인트에 대한 게이트웨이 연결을 관리합니다. 게이트웨이는 AWS IoT Core for LoRaWAN에서 제공하는 계정의 Cupiguration and Update Server(Cupdate Server) 엔드포인트에 연결할 수 있습니다.

  | 엔드포인트 용도             | 엔드포인트 형식                                              |
  | :-------------------------- | :----------------------------------------------------------- |
  | 구성 및 업데이트 서버(CUPS) | **account-specific-prefix**.cups.lorawan.**aws-region**.amazonaws.com:443 |
  | LoRaWAN 네트워크 서버(LNS)  | **account-specific-prefix**.gateway.lorawan.**aws-region**.amazonaws.com:443 |



## AWS IoT Core for LoRaWAN 게이트웨이 및 디바이스

AWS IoT Core for LoRaWAN는 무선 게이트웨이와 디바이스를 AWS IoT Core에 연결합니다.

- **Endpoints**

  AWS IoT Core for LoRaWAN는 계정 및 리전별 AWS IoT Core 엔드포인트에 대한 게이트웨이 연결을 관리합니다. 게이트웨이는 AWS IoT Core for LoRaWAN에서 제공하는 계정의 Cupiguration and Update Server(Cupdate Server) 엔드포인트에 연결할 수 있습니다.

  | 엔드포인트 용도             | 엔드포인트 형식                                              |
  | :-------------------------- | :----------------------------------------------------------- |
  | 구성 및 업데이트 서버(CUPS) | **account-specific-prefix**.cups.lorawan.**aws-region**.amazonaws.com:443 |
  | LoRaWAN 네트워크 서버(LNS)  | **account-specific-prefix**.gateway.lorawan.**aws-region**.amazonaws.com:443 |

  



#### 참조

- [AWS IoT Core 연결](https://docs.aws.amazon.com/ko_kr/iot/latest/developerguide/connect-to-iot.html)