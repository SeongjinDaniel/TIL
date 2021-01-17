# AWS ARN



> 복수개의 가용영역은 매우 중요합니다. 만약 A라는곳에서 불이나도 B와 C가 있다면 서울리전에서의 서비스를 정상적으로 작동합니다. 단순계산으로 만약 데이터센터를 한곳만 돌렸을때 에러가 발생할 확률이 천분에 1이라고 한다면 2곳의 데이터센터가 동시에 문제가 발생할 확률은 1백만분에 1로 기하급수적으로 내려가게됩니다. (물론 실제로[ 그 일](http://www.zdnet.co.kr/view/?no=20181122113510)은 아주 쉽게 일어났습니다…)
>
> 또한가지, 가용영역을 더 잘 이해하기 위해서는 ARN에 대해서도 이해해야합니다. ARN은 Amazon Resource Number의 약자로 우리가 람다함수를 생성할때 EC2를 생성할때 생성되는 일련번호입니다. AWS에는 각각의 서비스에서 만든 리소스들을 ARN으로 구분하고 ARN이 다르다면 서로 다르게 취급됩니다. 일반적인 ARN은 아래와 같이 이루어져있습니다.
>
> ARN/파티션구분자/서비스명/리전/계정번호 + 서비스마다의 상세 구분자



---

> ARN이 너무 많이 쪼개지는것같다는 느낌이 들 수 있겠지만 ARN형식은 IAM을 통해 권한을 설정할때 정말 쉽게도와줍니다.

```
{ "Effect": "Allow", 
  "Action": "lambda:*", 
  "Resource": [ "     arn:aws:lambda:ap-northeast-2:964581251123123:function:lambda_api_billing",
```



#### 참조

- [AWS의 ARN 이해하기](https://medium.com/harrythegreat/aws%EC%9D%98-arn-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-8c20d0ccbbfd#:~:text=ARN%EC%9D%80%20Amazon%20Resource%20Number,%EB%A9%B4%20%EC%84%9C%EB%A1%9C%20%EB%8B%A4%EB%A5%B4%EA%B2%8C%20%EC%B7%A8%EA%B8%89%EB%90%A9%EB%8B%88%EB%8B%A4.)