# 람다(Lambda) 기능

**기능**

- [프로그래밍 모델](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel)
- [확장](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-scaling)
- [동시성 제어](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-concurrency)
- [비동기식 호출](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-async)
- [이벤트 소스 매핑](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-eventsourcemapping)
- [대상](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-destinations)
- [함수 블루프린트](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-blueprints)
- [테스트 및 배포 도구](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-tools)
- [애플리케이션 템플릿](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-templates)



## 프로그래밍 모델

작성 관련 세부 사항은 런타임마다 다르지만, 모든 런타임은 코드와 런타임 코드 사이의 인터페이스를 정의하는 일반적인 프로그래밍 모델을 공유합니다. 함수 구성에서 *핸들러*를 정의함으로써 런타임에게 어떤 메서드를 실행할지 알려주면 런타임은 그 메서드를 실행합니다. 런타임은 호출 *이벤트*와 *컨텍스트*(예: 함수 이름, 요청 ID)를 포함하는 핸들러로 객체를 전달합니다.



핸들러가 첫 번째 이벤트 처리를 완료하면 런타임이 다른 이벤트를 보냅니다. 함수의 클래스가 메모리에 유지되므로, *초기화 코드*에서 핸들러 메서드 외부에서 선언된 클라이언트 및 변수를 재사용할 수 있습니다. 후속 이벤트에 대한 처리 시간을 절약하려면 초기화 중에 AWS SDK 클라이언트와 같은 재사용 가능한 리소스를 생성합니다. **초기화된 후에는 함수의 각 인스턴스가 수천 개의 요청을 처리할 수 있습니다.**



초기화는 함수 인스턴스가 처리하는 첫 번째 호출의 소요 시간에 포함되어 요금이 청구됩니다. [AWS X-Ray 추적](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/services-xray.html)이 활성화된 경우 런타임이 초기화와 실행에 대해 별도의 하위 세그먼트를 기록합니다.



#### 참조

- [Lambda 기능](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html)