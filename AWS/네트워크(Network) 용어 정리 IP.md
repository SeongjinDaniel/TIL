# 네트워크(Network) 용어 정리(IP)



## IP(Internet Protocol)



> **인터넷 프로토콜 주소** ( **IP 주소** )가 연결된 각 장치에 할당 된 수치 레이블 [컴퓨터 네트워크](https://en.wikipedia.org/wiki/Computer_network) 용도 [인터넷 프로토콜](https://en.wikipedia.org/wiki/Internet_Protocol) 통신. [[1\] ](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc760-1)[[2\]](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc791-2) IP 주소는 호스트 또는 네트워크 인터페이스 [식별](https://en.wikipedia.org/wiki/Identification_(information)) 및 위치 [주소 지정](https://en.wikipedia.org/wiki/Network_address) 이라는 두 가지 주요 기능을 제공합니다 .
>
> [인터넷 프로토콜 버전 4](https://en.wikipedia.org/wiki/IPv4) (IPv4)는 IP 주소를 [32 비트](https://en.wikipedia.org/wiki/32-bit) 숫자 로 정의합니다 . [[2\]](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc791-2) 그러나 [인터넷](https://en.wikipedia.org/wiki/Internet) 의 성장 과 [사용 가능한 IPv4 주소](https://en.wikipedia.org/wiki/IPv4_address_exhaustion) 의 [고갈로](https://en.wikipedia.org/wiki/IPv4_address_exhaustion) 인해 IP 주소로 128 비트를 사용 하는 새로운 버전의 IP ( [IPv6](https://en.wikipedia.org/wiki/IPv6) )가 1998 년에 표준화되었습니다. [[3\] ](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc1883-3)[[4\] ](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc2460-4)[[5 \]](https://en.wikipedia.org/wiki/IP_address#cite_note-rfc8200-5) [IPv6 구축](https://en.wikipedia.org/wiki/IPv6_deployment) 은 2000 년대 중반부터 계속되고 있습니다.
>
> IP 주소는 IPv4의 *172.16.254.1* 및 IPv6의 *2001 : db8 : 0 : 1234 : 0 : 567 : 8 : 1* 과 같이 [사람이 읽을 수있는](https://en.wikipedia.org/wiki/Human-readable) 표기법 으로 작성되고 표시됩니다 . 어드레스의 라우팅 프리픽스의 크기에 지정 [CIDR 표기법](https://en.wikipedia.org/wiki/CIDR_notation) 의 수의 어드레스를 부기 [상위 비트](https://en.wikipedia.org/wiki/Bit_numbering) , 예를 들어, *192.168.1.15* */* *24* 역사적 사용 동등, [서브넷 마스크가 ](https://en.wikipedia.org/wiki/Subnet_mask)*255.255.255.0* .
>
> IP 주소 공간에 의해 전 세계적으로 관리되는 [인터넷 할당 번호 관리 기관](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority) (IANA), 다섯하여 [지역 인터넷 레지스트리](https://en.wikipedia.org/wiki/Regional_Internet_registry) 에 할당 자신의 지정된 지역에서 책임 (RIR의) [지역 인터넷 레지스트리](https://en.wikipedia.org/wiki/Local_Internet_registry) 같은, [인터넷 서비스 제공](https://en.wikipedia.org/wiki/Internet_service_provider) 업체 (ISP) 및 기타 [끝 사용자](https://en.wikipedia.org/wiki/End_user) . IPv4 주소는 IANA에 의해 각각 약 1,680 만 주소 블록으로 RIR에 배포되었지만 2011 년부터 IANA 수준에서 고갈되었습니다. RIR 중 하나만 아프리카에서 로컬 할당을 위해 여전히 공급하고 있습니다. [[6\]](https://en.wikipedia.org/wiki/IP_address#cite_note-6) 일부 IPv4 주소는 [사설 네트워크](https://en.wikipedia.org/wiki/Private_network) 용으로 예약되어 있으며 전역 적으로 고유하지 않습니다.
>
> [네트워크 관리자](https://en.wikipedia.org/wiki/Network_administrator) 는 네트워크에 연결된 각 장치에 IP 주소를 할당합니다. 이러한 할당은 네트워크 관행 및 [소프트웨어](https://en.wikipedia.org/wiki/Software) 기능 에 따라 *정적* (고정 또는 영구적) 또는 *동적* 기반 일 수 있습니다.



#### IP(Internet Protocol)

**Internet Protocol**의 약자로 **패킷 교환 네트워크(인터넷)에서 데이터를 주고받을 때의 통신 규약**이다. OSI계층에서 IP계층은 호스트의 주소지정과 패킷분할 및 조립 기능을 담당한다.

##### 데이터 패킷(Packet)

- 패킷은 패키지(package)와 덩어리를 뜻하는 버킷(bucket)의 합성어로 통신망을 통해 전송하기 쉽도록 자른 데이터의 전송 단위입니다. 본래 패킷은 소포를 뜻하는 용어인데 우체국에서 화물을 적당한 덩어리로 나누어 행선지를 표시하는 붙이는 작업을 데이터 통신에 접목한 용어로 사용하고 있다.
- 데이터를 전송할 때 송신측과 수신측에 하나의 단위가 되어 전송되는 집합체를 뜻하는데 쉽게 말해서 우리가 인터넷을 이용해 주고받는 이메일, 채팅 메시지, 금융 거래 내용 등 다양한 데이터의 내용을 작은 단위로 쪼갠 데이터로 이해할 수 있다.
- 패킷은 헤더, 데이터, 테일러로 이루어져 있는데 이미 헤더에는 수신처의 인터넷 주소와 순서 등이, 테일러에는 에러 정보가 기록되어 있습니다. 일반적으로 2계층으로 내려가기 전까지는 3~4계층의 데이터 단위를 패킷이라고 정의하고 1~2 계층의 데이터 단위는 프레임이라고 지칭합니다.

![image](https://user-images.githubusercontent.com/55625864/107866588-df55a500-6eb5-11eb-9f8f-0a8ce911ec70.png)

-  **IP주소의 사용이유는 각각의 Host들을 구분**하기위해 사용되며, 부여받은 IP는 자기 고유의 IP가 되기에 다른 사람이 사용하면 안됩니다. 하지만 **현재 사용되는 IPv4방식의 IP 수는 한정**되어 있기에 모든 Host에게 고유의 IP를 할당하지 못합니다. 그렇다고 하여서 하나의 호스트에 하나의 IP만 사용되는건 아닙니다. 이는 한 컴퓨터에 여러 개의 NIC(Network Interface Card / 흔히 랜카드라 불리는 장치)를 장착하여 여러 개의 IP를 사용하는 형태를 생각하시면 쉽겠습니다. 대표적인 네트워크 장비로 라우터를 생각하셔도 되겠습니다.

   일반 가정같은 경우에는 PC의 '네트워크 설정'에서 확인하실 수 있는  TCP/IP Protocol을 보시면 아시겠지만 고정 IP가 아닌 유동 IP로 설정이 되어 있는데, 이는 평범한 가정에서 사용하는 PC의 경우 전원이 Off되어 IP 주소가 필요없는 경우가 대부분이기에 모든 기기에 IP를 부여하게 되면 심각한 IP 부족현상이 나타나기 때문입니다. 그래서 DHCP Server를 이용하여 전원이 켜져있는 컴퓨터에게만 IP를 할당하며, 컴퓨터가 Off되면 IP를 회수하게 됩니다.

#### IP Address(Internet Protocol Address)

- 우리는 편지를 보낼때 도착 주소를 반드시 명시해야한다. 그래야 그 편지는 우리가 원하는 목적지에 잘 전달될 것이다. 그리고 보낸 곳이 어딘지 정확히 명시해 주어야 받는 사람이 알 수 있을 것이다.



## What is Network

두 대 이상의 컴퓨터가 논리적 또는 물리적으로 연결되어 통신이 가능한 상태.

일방적으로 규모에 따른 네트워크 종류는 아래와 같다.

1. **PAN ( Personal Area Network )** : 가장 작은 규모의 네트워크

2. **LAN ( Local Area Network )** : 근거리 영역 네트워크

   근거리 통신 망을 의미하며 지역적 좁은 범위 내에서 고속 통신이 가능한 통신망.

3. **Man ( Metropolitan Area Network )** : 대도시 영역 네트워크

4. **Wan ( Wide Area Network )** : 광대역 네트워크

   Wild Area Network 로써 광대역 통신망으로써 LAN 보다 넓은 지역을 나타내며 지역과 지역, 지방과 지방, 나라와 나라 또는 대륙과 대륙을 연결하는 통신망.

![image](https://user-images.githubusercontent.com/55625864/107866935-4d4f9b80-6eb9-11eb-8bee-97318f2891af.png)

## 1. What is IP address

네트워킹이 가능한 장비를 `식별`하는 주소. 네트워크 상에서 통신을 하기 위해서는 몇 가지 `통신규약(protocol)`을 따라야 하는데, 그런 규약들 중에는 "네트워킹을 하는 장비들에게 `숫자 12개의 고유한 주소`를 주어, 그 주소를 통해 서로를 인식하고 통신하도록 하자" 라는 의미의 규약이 존재한다.

### 1.1. IPv4 주소

IP version 4 주소, 줄여서 IPv4 주소는 오늘날 일반적으로 사용하는 IP 주소이다. 이 주소의 범위는 `32비트`로 보통 0~255 사이의 `10진수 넷`을 쓰고 `.`으로 구분하여 나타낸다. 따라서 `0.0.0.0`부터 `255.255.255.255`까지가 된다. 이론적으로 42억9496만7296개의 IP가 존재한다. 중간의 일부 번호들은 특별한 용도를 위해 예약되어 있다. 이를테면 127.0.0.1은 localhost(로컬 호스트)로 자기 자신을 가리킨다.

### 1.2. IPv6 주소

IP address 라는 개념이 처음 생겼을 당시에는 지금처럼 네트워킹이 가능한 장비의 종류가 다양하지 않았지만, 기술이 발전하고 한 사람이 가지는 네트워킹 가능한 단말기의 수가 2 ~ 3개가 되어버리자 약 IPv4 주소의 수가 부족해진다. 그래서 등장한 것이 IPv6이다. IPv6에서는 주소 길이를 `128비트`로 늘려 사용가능한 주소의 갯수가 2의 128제곱개 정도 된다. 약 **43억x43억x43억x43억개**... IPv6 주소는 보통 두 자리 `16진수 여덟 개`를 쓰고 각각을 `:` 기호로 구분한다.



## 2. IP주소의 클래스(A,B,C class)란?

IP주소에는 `클래스`라는 개념이 있고 이 클래스의 개념을 알아야 어디까지가 네트워크 영역이고 호스트 영역인지 알 수 있다. 즉, 다시말해 클래스는 **하나의 IP주소에서 네트워크 영역과 호스트 영역을 나누는 방법이자, 약속**이다. IP주소를 3개의 클래스로 나누는 이유는 네트워크 크기에 따른 구분이라 생각하면 쉽다. 하나의 네트워크에서 **몇 개의 호스트 IP까지 가질 수 있는가에 따라**서 클래스를 나눌 수 있다. 즉, 네트워크 범위가 커질수록 호스트 주소 범위는 작아지는 반비례 관계이다.

![image](https://user-images.githubusercontent.com/55625864/107867081-dadfbb00-6eba-11eb-99b2-c62854843d50.png)

IP주소 클래스는 총 5개가 있다. A클래스, B클래스, C클래스, D클래스 E클래스. 하지만 보통 A, B, C 3개 정도만 알고있으면 충분하다. (나머지 D, E 클래스는 멀티캐스트용, 연구용으로 사용)



### 2.1 A클래스

먼저 A클래스는 하나의 네트워크가 가질 수 있는 호스트 수가 제일 많은 클래스이다. IP주소를 32자리 2진수로 표현했을때, 맨 앞자리 수가 항상 `0` 인 경우가 바로 A클래스이다. 즉 `0xxx xxxx. xxxx xxxx. xxxx xxxx. xxxx xxxx` 와 같이 되어있다. x 는 0 또는 1. 이 범위를 10진수로 표현하면 `0.0.0.0 ~ 127.255.255.255` 이다.

**그런데 A클래스에서 네트워트 주소는 `1.0.0.0 ~ 126.0.0.0` 까지로 규정되어있다. 약속이다. 그래서 IP주소 중 1부터 126으로 시작하는 네트워크는 A클래스라고 생각하면 된다.**

그리고 호스트 주소가 가질 수 있는 갯수는 `(2^24) - 2`개 이다. (-2 이유는 모두가 1인경우 브로드캐스트 주소로 사용하고 모두 0인 경우엔 네트워크 주소로 사용하기 때문) 예를 들어 A클래스로 13.0.0.0 네트워크 주소를 할당 받았을 때, 가능한 호스트 IP를 10진수로 나타내면 13.0.0.0 ~ 13.255.255.255 가 될 것이다. 하지만 여기서 **13.0.0.0 은 네트워크 주소를 표현**하기 위해서 호스트IP로 사용하면 안된다. 또, **13.255.255.255 역시 브로드캐스트 주소로 사용**하기 때문에 호스트 IP로 사용하면 안된다. 따라서 (2^24) - 2 를 해주는 것이다.

### 2.2 B클래스

B클래스의 IP주소를 32자리 2진수로 표현했을때, 맨 앞자리 수는 항상 `10` 이여야 한다. 즉 `10xx xxxx. xxxx xxxx. xxxx xxxx. xxxx xxxx`. 이 범위를 10진수로 표현하면 **`128.0.0.0 ~ 191.255.255.255` .**

네트워크 주소 범위는 **10xx xxxx. xxxx xxxx** 에서 x들이 가질 수 있는 경우의 수, `2^14` 개 이고,

호스트 주소 범위는 **xxxx xxxx. xxxx xxxx** 에서 x들의 경우의 수인 `(2^16) - 2` 개 이다.

내가 지금 공부를 하고 있는 카페의 IP주소는 `172.30.1.12` 니까, 이 IP는 **B클래스** 인 것이다. B클래스임을 알게 되면 네트워크 부분과 호스트 부분을 나눌 수 있다. 각각 172.30 과 1.12.

### 2.3 C클래스

C클래스의 IP주소는 2진수로 표현했을 때 반드시 `110`으로 시작한다. 즉 `110x xxxx. xxxx xxxx. xxxx xxxx. xxxx xxxx`. 이 범위를 10진수로 표현하면 `192.0.0.0 ~ 223.255.255.255`.

네트워크 범위는 **110x xxxx. xxxx xxxx.** **xxxx xxxx** 에서 x들이 가질 수 있는 경우의 수, `2^21` 개 이고,

호스트 주소 범위는 **xxxx xxxx** 에서 x들이 가질 수 있는 경우의 수, `(2^8 )-2` 개 이다.

### 2.4 표로 보는 클래스

| 클래스  | 첫 고정 비트 | 네트워크주소영역 | 호스트주소영역  |
| ------- | ------------ | ---------------- | --------------- |
| A class | 0            | 8bit(2^7개)      | 24bit(2^24-2개) |
| B class | 10           | 16bit(2^14개)    | 16bit(2^16-2개) |
| C class | 110          | 24bit(2^21개)    | 8bit(2^8-2개)   |



## IP 주소의 NetworkID와 HostID

 **하나의 IP주소에는 Network ID와 Host ID가 존재**하고 있습니다. 먼저 **Network ID**는 인터넷 상에서 모든 Host들을 전부 관리하기 힘들기에 한 Network의 범위를 지정하여 관리하기 쉽게 만들어 낸 것입니다. 그리고 **Host ID**는 호스트들을 개별적으로 관리하기 위해 사용하게 된 것입니다. 따라서 **우리가 인터넷을 사용할 때 Routing으로 목적지를 알아내고 찾아가는 등의 역할을 할 때에는 NetworkID와 HostID가 합쳐진 IP주소를 보게 됩니다.** 서브넷 마스크에 대해 알고자 하실 때에는 이 부분이 매우 중요합니다.

 Subnet mask를 활용하여 Network ID를 올리거나 낮출 수 있게 됩니다. 반대로 Host ID는 줄어들거나 늘어날 수 있게 됩니다. 라우터끼리의 통신에서는 IP를 사용하기에 Network ID와 Host ID보고 목적지가 어떤 네트워크에 속하는지 알 수 있게 됩니다.

 쉬운 예를 들어보겠습니다. 홍대리는 집에 장롱이 필요하여 가구회사에 주문을 하였습니다. 장롱을 가져다 주는 배달원은 주소를 보고 홍대리의 집이 '부산광역시 해운대구 우동 792번지'라는걸 확인하고 도착하였습니다. 그런데 배달원은 집까지 가져왔지만 어느 곳에 두어야 할 지 모릅니다. 이 때 홍대리가 작은 방의 한쪽 구석을 가리키며 정확한 위치를 알려주었습니다. 이 예시를 보면 배달원의 역할은 최종 목적지가 속한 지역(집)까지 전달하는 Network ID에 해당합니다. 그리고 홍대리는 자신의 지역(집)에서 최종적으로 장롱을 두어야 하는 위치를 안내하여 주기에 Host ID의 역할로 보시면 되겠습니다. 나름 생각하고 만들었는데 적절한 비유인지는 모르겠으나 이 예시를 통해 이해에 도움이 되었으면 좋겠습니다.

#### IP Class 개념

 Network ID와 Host ID를 설명드린 이유는 바로 IP Class의 개념을 알기 이전에 필요한 내용입니다. **IP Class의 경우 A, B, C, D, E Class로 나누어 Network ID와 Host ID를 구분**하게 됩니다. 

 A Class의 경우 처음 8bit(1byte)가 Network ID이며, 나머지 24bit(3byte)가 Host ID로 사용됩니다. 비트가 0으로 시작하기에 네트워크 할당은 0~127입니다 . 즉, 128 곳에 가능하며, 최대 호스트 수는 16,777,214개입니다. 

 B Class의 경우 처음 16bit(2byte)가 Network ID이며, 나머지 16bit(2byte)가 Host ID로 사용됩니다. 비트가 10으로 시작하기에 네트워크 할당은 16,384 곳에 가능하며, 최대 호스트 수는 65,534개입니다. 

 C Class의 경우 처음 24bit(3byte)가 Network ID이며, 나머지 8bit(1byte)가 Host ID로 사용됩니다. 비트가 110으로 시작하기에 네트워크 할당은 2,097,152 곳에 가능하며, 최대 호스트 수는 254개입니다.

아래의 표를 보시면 더 빠르게 이해하실 수 있습니다.

![image](https://user-images.githubusercontent.com/55625864/107877510-43a55280-6f10-11eb-9f9e-591706f122f4.png)

 그럼 D Class와 E Class에 대해 설명드리도록 하겠습니다. **실제 Network에서 사용되는 Class는 A, B, C Class**이며, **D Class는 Multicast(멀티캐스트), E Class는 미래에 사용**하기 위해 남겨둔 것으로 예약되어 있습니다. 그리고 D와 E Class의 경우 실제 사용되는 경우가 거의 없습니다.

#### Class 구분하는 방법

 **각각의 Class를 구분하는 방법은 의외로 간단하게 제일 첫 번째 옥텟(Octet)으로 구분**하실 수 있습니다. Octet은 위에서도 잠깐 언급이 된 내용으로 2진수 8개(8bit)를 묶음으로 표현하는 것을 Octet이라고 합니다. 만약 IP가 164.58.94.125라고 할 때 첫 번째 Octet은 164가 되는 것입니다. 

 IP 주소에서 쓸  수 있는 숫자의 범위는 0~255로 되어 있기에 첫 번째 Octet에서 0~255까지의 숫자를 5개로 나누어서 A, B, C, D, E Class로 구분 되는 것입니다.

- A Class : 0 ~ 127 (0.0.0.0 ~ 127.255.255.255)
- B Class : 128 ~ 191 (128.0.0.0 ~ 191.255.255.255)
- C Class : 192 ~ 223 (192.0.0.0 ~ 223.255.255.255)
- D Class : 224 ~ 239 (224.0.0.0 ~ 239.255.255.255)
- E Class : 240 ~ 255 (240.0.0.0. ~ 255.255.255.255)

 숫자로 이루어진 클래스 범위를 무작정 외우기에는 쉽지 않습니다. 그래서 쉬운 방법을 생각해 보았는데 의외로 정말 간단한 방법으로 외우게 되었습니다. 먼저 특징을 말씀드리자면 "주소체계 범위의 각 클래스 시작이 짝수이고 끝이 홀수"라는 것과, "범위가 반으로 나누어지게 된다는 것(n / 2)"입니다.

1. IP에 입력하는 범위가 256개가 존재한다 (0 ~ 255)
2. 256부터 2씩 나눈다.
3. 256 / 2 = 128 - 1 = 127 (A Class 범위 : 0 ~ 127)
4. 128 / 2 = 64 + 127 = 191 (B Class 범위 : 128 ~ 191)
5. 64 / 2 = 32 + 191 = 223 (C Class 범위 : 192 ~ 223)
6. 남은 32의 수는 16씩 나누어서 D Class와 E Class가 가진다.

 또 다른 방법으로는 첫 번째 bit를 알면 됩니다. B클래스를 보신다면 Network ID와 Host ID 둘 다 16bit(2byte) 씩 나눠서 가지고 있습니다. 그런데 할당 가능한 수가 Network ID는 16,384개이고 Host ID는 65,534개로 차이가 납니다. 이는 위에서 잠깐 언급되었는데 각 클래스를 구분하기 위해서 bit를 사용하기 때문입니다. A클래스는 0으로 시작하고, B클래스는 10으로 시작하고, C클래스는 110으로 시작하기에 사용되는 비트만큼 Network ID로 할당 가능한 수가 줄어들게 됩니다.



#### 참조

- https://en.wikipedia.org/wiki/IP_address

- https://blog.daum.net/gmania65/137

- [IP address 란?](https://velog.io/@hidaehyunlee/IP-address%EB%9E%80)

- [IP 주소체계와 클래스 구별법 (IPV4)](http://korean-daeddo.blogspot.com/2015/12/ip.html)