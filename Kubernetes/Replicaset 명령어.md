# Replicaset 명령어



- `kubectl create -f replicaset-definition.yml`
- `kubectl get replicaset`
- `kubectl delete replicaset myapp-replicaset`
- `kubectl replace -f replicaset-definition.yml`
  - 복제본 세트와 큐브를 교체하거나 업데이트하는 제어 교체 명령어이다.
- `kubectl scale -replicas=6 -f replicaset-definition.yml`
  - 파일을 수정할 필요 없이 명령중에서 간단하게 scale 명령 scale replica set를 제어한다.





