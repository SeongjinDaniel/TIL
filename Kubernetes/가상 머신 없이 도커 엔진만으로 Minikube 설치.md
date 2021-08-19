# 가상머신 없이 도커 엔진만으로 Minikube 설치



**minikebe, kubectl  내려받기**

```
curl -Lo minikube \
https://storage.googleapis.com/minikube/releases/v1.12.0/minikube-linux-amd64 && chmod +x minikube && \
sudo mv minikube /usr/local/bin/ 
```

```
curl -Lo kubectl \
https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/linux/amd64/kubectl && chmod +x kubectl && \
sudo mv kubectl /usr/local/bin
```



```
minikube start --vm-driver=none
```

설치가 완료된 뒤에는 다음 명령어로 쿠버네티스가 정상적으로 설치됐는지 확인합니다.

```
kubectl version --short
```



