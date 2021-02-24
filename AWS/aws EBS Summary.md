# aws EBS



### **EBS (Elastic Block Storage)**

- 저장 공간이 생성되어 지며 EC2 인스턴스에 부착된다.
- 디스크 볼륨 위에  File System이 생성된다.
- EBS는 특정 가용 영역(Availability Zone(AZ))에 생성된다.

<img src="https://user-images.githubusercontent.com/76925694/108973003-3d109b00-76c7-11eb-8599-ab35705cfa2d.png" alt="image" style="zoom:67%;" />



#### EBS 볼륨 타입

#### <<SSD군>>

1. **General Purpose SSD (GP2**) : 최대 10K IOPS를 지원하며 1GB당 3IOPS 속도가 나옴
2. Provisioned IOPS SSD (IO1) : 극도의 I/O률을 요구하는 (예시 : 매우 큰 DB관리) 환경에서 주로 사용됨. 10K 이상의 IOPS를 지원함.

#### <<Magnetic/HDD군>>

3. **Throughput Optimized HDD (ST1)** : 빅데이터 Datawarehouse, Log 프로세싱시 주로 사용 (boot volume으로 사용 가능 X)
4. **CDD HDD (SC1)** : 파일 서버와 같이 드문 volume 접근시 주로 사용, 역시 boot volume으로 사용 불가능하나 비용은 매우 저렴함
5. **Magnetic (Standard)** : 디스크 1GB당 가장 싼 비용을 자랑함. Boot volume으로 유일하게 가능함.







