# Node Affinity



Node Affinity 기능의 주요 목적은 pod가 특정 노드에서 호스팅되도록 하는 것이다.

```yaml
# pod-definition.yml

apiVersion:
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: data-processor
    image: data-processor
    
  nodeSelector:
  size: Large
```

```yaml
# pod-definition.yml

apiVersion:
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: data-processor
    image: data-processor
    
  affinity:
    nodeAffinity:
      requeiredDuringSchedulingIgnoreDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: size
            operator: In    # NotIn도 가능  # operator: Exists등 도 가능 (이하 삭제) 
            values:
            - Large         # Small도 가능
```



### Node Affinity Types

##### Available:

- `requeiredDuringSchedulingIgnoreDuringExecution`
- `preferredDuringSchedulingIgnoreDuringExecution`



##### Planned:

- `requeiredDuringSchedulingRequiredDuringExecution`

|        | DuringScheduling | DuringExecution |
| ------ | ---------------- | --------------- |
| Type 1 | Required         | Ignored         |
| Type 2 | Preferred        | Ignored         |
| Type 3 | Required         | Required        |

- DuringScheduling
  - Pod가 존재하지 않고 처음 생성된 상태이다.