# kubectl 명령어



#### Imperative

```
# Create Objects
> kubetcl run --image=nginx nginx
> kubetcl create deployment --image=nginx nginx
> kubetcl expose deployment nginx --port 80

# Update Objects
> kubetcl edit deployment nginx
> kubetcl scale deployment nginx --replicas=5
> kubectl set image deployment nginx nginx=nginx:1.18

> kubectl create -f nginx.yaml
> kubectl replace -f nginx.yaml
> kubetcl delete -f nginx.yaml
```



#### Declarative

```
apiVersion:
kind:
metadata:
spec:
```



#### Imperative Object Configuration Files

**Create objects**

` > kubectl create -f nginx.yaml`

`> kubectl apply -f /path/to/config-files`

**Update Objects**

`> kubectl edit deployment nginx`

`> kubectl replace -f nginx.yaml`

`> kubectl replace --force -f nginx.yaml` 

- 완전히 삭제하고 다시 만듦

```
# nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    type: front-end
spec:
  containers:
  - name: nginx-container
    image: nginx

```

