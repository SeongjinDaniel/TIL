# Logging



**event-simulator라는 도커 컨테이너가 하는 일은 웹을 시뮬레이션하는 임의의 이벤트를 생성하는 것이다.**

```
$ docker run kodekloud /event simulator
# 백그라운드에서 도커 컨테이너 실행 --> 로그를 볼수 없음
$ docker -d run kodekloud /event simulator
# 로그를 보고 싶다면 -f 옵션과 컨테이너 ID를 사용하여 볼 수 있습니다.
$ docker logs -f ecf
...
```



#### kubernetes command

```
$ kubectl create -f event-simulator.yaml
# -f 옵션을 사용하여 docker 명령처럼 실시간으로 로그를 스트리밍합니다.
$ kubectl logs -f event-simulator-pod
...
```

로그는 포드 내에서 실행되는 컨테이너에만 해당됩니다. 

**event-simulator.yaml**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: event-simulator-pod
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
```



yaml 파일에 컨테이너를 여러개 설정해서 해당하는 로그를 확인할 수 있습니다.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: event-simulator-pod
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
  - name: image-processor
    image: some-image-processor
```

```
$ kubectl logs -f event-simulator-pod event-simulator
...
```

