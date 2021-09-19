# Configuring Environment Variables



```
$ docker run -e APP_COLOR=pink simple-webapp-color
```

**pod-definition.yaml**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
    ports:
      - containerPort: 8080
    env:
      - name: APP_COLOR
        value: pink
```

```yaml
    env:
      - name: APP_COLOR
        valueFrom:
          configMapKeyRef:
```

```yaml
    env:
      - name: APP_COLOR
        valueFrom:
          secretKeyRef:
```

<img src="https://user-images.githubusercontent.com/83576599/133922764-52d1e447-aae6-4379-9e35-1e8246183a47.png" alt="image" style="zoom:50%;" />

<img src="https://user-images.githubusercontent.com/83576599/133922780-97e21c42-184a-457c-bafc-4d3d7ea8269c.png" alt="image" style="zoom:50%;" />

#### Create ConginMaps

**Imperative**

```
$ kubectl create configmap \
     app-config --from-literal=APP_COLOR=blue \
                --from-literal=APP_MOD=prod
```

```
$ kubectl create configmap
     <config-name> --from-file=<path-ro-file>
```

```
$ kubectl create configmap
     app-config --from-file=app_config.properties
```

**Declarative**

```
$ kubectl create –f
```

**config-map.yaml**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```

```
$ kubectl create –f config-map.yaml
```

![image](https://user-images.githubusercontent.com/83576599/133923146-ed5fa2ed-d049-47b0-a1f7-5af25d0523ee.png)



**get & describe command**

```
$ kubectl get configmaps
```

```
$ kubectl describe configmaps
```

<img src="https://user-images.githubusercontent.com/83576599/133923249-467a96a5-b6f4-452f-853f-6e5a5709ce29.png" alt="image" style="zoom:50%;" />



**pod에 환경 변수 설정의 3가지 방법**

<img src="https://user-images.githubusercontent.com/83576599/133923311-a8e86377-2743-468b-9d2c-775aaafa5d6d.png" alt="image" style="zoom:50%;" />







