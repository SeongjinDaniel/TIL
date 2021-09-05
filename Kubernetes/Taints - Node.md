# Taints - Node



```
$ kubectl taint nodes node-name key=value:taint-effect
```

value의 종류에는 `NoSchedule`, `PreferNoSchedule`, `NoExecute`

```
$ kubctl taint nodes node1 app=blue:NoSchedule
```

```yaml
apiVersion:
kind: Pod
metatdata:
  name: myapp-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "blue"
    effect: NoSchedule
```

