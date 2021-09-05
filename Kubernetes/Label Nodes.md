# Label Nodes



```
$ kubectl label nodes <node-name> <label-key>=<label-value>
```

```
$ kubectl label node node-1 size=Large
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
    
  nodeSelector:
    size: Large
```

```
$ kubectl create -f pod-definition.yml
```

