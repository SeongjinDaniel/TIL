# 가상머신 없이 도커 엔진만으로 Minikube 설치



**minikebe, kubectl  내려받기**

```
curl -Lo minikube \
https://storage.googleapis.com/minikube/releases/v1.12.0/minikube-linux-amd64 && chmod +x minikube && \
mv minikube /usr/local/bin/ 
```

```
curl -Lo kubectl \
https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/linux/amd64/kubectl && chmod +x kubectl && \
mv kubectl /usr/local/bin
```



```
minikube start --vm-driver=none
```

```
* minikube v1.12.0 on Ubuntu 16.04 (xen/amd64)
* Using the none driver based on user configuration
X Sorry, Kubernetes 1.18.3 requires conntrack to be installed in root's path
```

위와 같은 에러발생 했다면 `sudo apt-get install conntrack` conntrack을 설치



설치가 완료된 뒤에는 다음 명령어로 쿠버네티스가 정상적으로 설치됐는지 확인합니다.

```
kubectl version --short
```



Minikube를 삭제하려면 minikube delete 명령어를 사용합니다.

