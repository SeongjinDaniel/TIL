# 쿠버네티스 리소스(CPU/Memory)



### 리소스 관리

**Pod에 대한 스케줄링시에 , Pod내의 애플리케이션이 동작할 수 있는 충분한 자원 (CPU, 메모리 등)이 확보되어야 한다.** 쿠버네티스 입장에서는 애플리케이션에서 필요한 자원의 양을 알아야, 그만한 자원이 가용한 노드에  Pod를 배포할 수 있다.

쿠버네티스에서는 이런 컨셉을 지원하기 위해서 컨테이너에 필요한 리소스의 양을 명시할 수 있도록 지원하고 있다.

### 리소스 단위

리소스를 정의하는데 사용되는 단위는 CPU의 경우에는 ms(밀리 세컨드)를 사용한다. 해당 컨테이너에 얼마만큼의 CPU 자원을 할당할것인가인데, 대략 1000ms가 1 vCore (가상 CPU 코어) 정도가 된다. 클라우드 벤더에 따라 또는 쿠버네티스를 운영하는 인프라에 따라서 약간씩 차이가 있다. 

메모리의 경우에는 Mb를 사용한다. 



### Request & Limit

컨테이너에 적용될 리소스의 양을 정의하는데 쿠버네티스에서는 request와 limit이라는 컨셉을 사용한다.

request는 컨테이너가 생성될때 요청하는 리소스 양이고, limit은 컨테이너가 생성된 후에 실행되다가 리소스가 더 필요한 경우 (CPU가 메모리가 더 필요한 경우) 추가로 더 사용할 수 있는 부분이다. 



1G (Gigabyte) = 1,000,000,000 bytes

1M (Megabyte = 1,000,000 bytes

1K (Kilobyte) = 1,000 bytes



1Gi (Gibibyte) = 1,073,741,824 bytes

1 Mi (Mebibyte) = 1,048,576 bytes

1 Ki (Kibibyte) = 1,024 bytes



컨테이너는 제한보다 많은 CPU 리소스를 사용할 수 없습니다. 그러나 메모리의 경우에는 그렇지 않습니다. 컨테이너는 제한보다 많은 메모리 리소스를 사용할 수 있습니다. 따라서 Pod가 지속적으로 제한보다 많은 메모리를 사용하려고 하면 해당 부분이 종료됩니다.



#### 참조

- [쿠버네티스 리소스(CPU/Memory)할당과 관리](https://bcho.tistory.com/1291)
- [컨테이너 및 파드 메모리 리소스 할당](https://kubernetes.io/ko/docs/tasks/configure-pod-container/assign-memory-resource/) - documentation
- [네임스페이스에 대한 기본 CPU 요청량과 상한 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/) - documentation

- [네임스페이스에 대한 기본 메모리 요청량과 상한 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/) - documentation