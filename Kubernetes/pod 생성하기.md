# pod 생성하기



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



