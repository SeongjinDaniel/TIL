# Pod 생성 및 삭제



```
apiVersion: v1
kind: Pod
metadata:
  name: my-nginx-pod
spec:
  containers:
  - name: my-nginx-container
    image: nginx:latest
    ports:
    - containerPort: 80
      protocol: TCP
```



**apiVersion**: YAML 파일에서 정의한 오브젝트의 API  버전을 나타냅니다.

**kind**: 이 리소스의 종류를 나타냅니다.

**metadata**: 라벨, 주석(annotation), 이름 등과 같은 리소소의 부가 정보들을 입력합니다.

**spec**: 리소스를 생성하기 위한 자세한 정보를 입력합니다. 위 예시에서는 포드에서 실행될 컨테이너 정보를 정의하는 containers 항목을 작성한 뒤, 하위 항목인 image에서 사용할 도커 이미지를 지정했습니다. name 항목에서는 컨테이너의 이름을, ports 항목에서는 Nginx 컨테이너가 사용할 포트인 80을 입력했습니다.



작성한 YAML 파일은 `kubectl apply -f` 명령어로 쿠버네티스에 생성할 수 있습니다.

```
$ kubectl apply -f nginx-pod.yaml
pod/my-nginx-pod created
```



`kubectl get <오브젝트 이름>`을 사용하면 특정 오브젝트의 목록을 확인할 수 있습니다. kubectl get pods 명령어는 현재 쿠버네티스에 존재하는 포드의 목록을 출력합니다.

```
$ kubectl get pods
NAME           READY   STATUS    RESTARTS   AGE
my-nginx-pod   1/1     Running   0          2m19s
```



쿠버네티스에는 kubectl exec 명령으로 포드의 컨테이너에 명령어를 전달할 수 있습니다. 예를 들어 다음과 같이 my-nginx-pod에서 배시 셸을 실행하되, -it 옵션으로 셸을 유지할 수 있습니다.

```
$ kubectl exec -it my-nginx-pod bash

root@my-nginx-pod:/# ls /etc/nginx/
conf.d fastcgi_paramskoi-utf koi-win ...

root@my-nginx-pod:/# exit # 포드에서 빠져나옵니다.
```



오브젝트는 kubectl delete -f 명령어로 쉽게 삭제할 수 있습니다.

```
$ kubectl delete -f nginx-pod.yaml
pod "my-nginx-pod" delete

$ # 또는 kubectl delete pod <포드 이름>을 사용해도 됩니다.
```



