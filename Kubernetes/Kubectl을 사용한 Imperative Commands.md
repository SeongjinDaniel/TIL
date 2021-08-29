# Kubectl을 사용한 Imperative Commands

명령 명령어는 정의 파일을 사용하여 대부분 선언적인 방식으로 작업하는 동안 한 번 실행 작업을 빠르게 수행할 수 있을 뿐만 아니라 정의 템플릿을 쉽게 생성할 수 있습니다. 이렇게 하면 시험 시간을 상당히 절약할 수 있습니다.

시작하기 전에 다음 명령어를 사용할 때 유용하게 사용할 수 있는 두 가지 옵션을 숙지하십시오.

`--dry-run`: 기본적으로 명령을 실행하는 즉시 리소스가 생성됩니다. 명령을 테스트하려면 `--dry-run=client` 옵션을 사용하십시오. 대신 리소스를 만들 수 있는지 여부와 명령이 올바른지 여부를 알려주지 않습니다.

`-o yaml`: 그러면 화면에 리소스 정의가 YAML 형식으로 출력됩니다.



Use the above two in combination to generate a resource definition file quickly, that you can then modify and create resources as required, instead of creating the files from scratch.



### POD

**Create an NGINX Pod**

```
kubectl run nginx --image=nginx
```



**Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)**

```
kubectl run nginx --image=nginx --dry-run=client -o yaml
```



### Deployment

**Create a deployment**

```
kubectl create deployment --image=nginx nginx
```



**Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)**

```
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml
```



**Generate Deployment with 4 Replicas**

```
kubectl create deployment nginx --image=nginx --replicas=4
```



You can also scale a deployment using the `kubectl scale` command.

```
kubectl scale deployment nginx --replicas=4
```

**Another way to do this is to save the YAML definition to a file and modify**

```
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml
```



You can then update the YAML file with the replicas or any other field before creating the deployment.



### Service

**Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379**

```
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml
```

(This will automatically use the pod's labels as selectors)

Or

`kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml` (This will not use the pods labels as selectors, instead it will assume selectors as **app=redis.** [You cannot pass in selectors as an option.](https://github.com/kubernetes/kubernetes/issues/46191) So it does not work very well if your pod has a different label set. So generate the file and modify the selectors before creating the service)



**Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:**

```
kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml
```

(This will automatically use the pod's labels as selectors, [but you cannot specify the node port](https://github.com/kubernetes/kubernetes/issues/25478). You have to generate a definition file and then add the node port in manually before creating the service with the pod.)

Or

```
kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml
```

(This will not use the pods labels as selectors)

Both the above commands have their own challenges. While one of it cannot accept a selector the other cannot accept a node port. I would recommend going with the `kubectl expose` command. If you need to specify a node port, generate a definition file using the same command and manually input the nodeport before creating the service.

#### **Reference:**

https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands

https://kubernetes.io/docs/reference/kubectl/conventions/