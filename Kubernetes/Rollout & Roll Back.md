# Rollout & Roll Back



## Rollout

**command**

```
# 롤아웃 상태를 실행하여 롤아웃 상태를 볼 수 있습니다.
$ kubectl rollout status deployment/myapp deployment
```

```
# 배포 이름으로 롤아웃의 revision 및 기록을 볼 수 있습니다.
$ kubectl rollout history deployment/myapp deployment
```



#### 배포 전략 두가지

여러 애플리케이션을 배포했다고 가정.

1. **Recreate**: 모든 애플리케이션을 다 다운되었가 다 같이 살림.
   - 애플리케이션이 다운되어 사용자가 액세스할 수 없음.
2. **Rolling Update**: 한번에 모든 애플리케이션을 파괴하지 않고 분할하여 다운시키고 다운된 것만 새로운 애플리케이션으로 업데이트하는 방식. 이 방식이 kubernetes에서는 default.





## Roll Back

쿠버네티스는 배포를 통해 이전 버전으로 롤백하여 변경 사항을 취소할 수 있습니다.



**command**

```
# deployment 이름 뒤에 오는 undo 명령을 롤아웃합니다. 그런 다음 replica는 새 replica set의 일부를 제거하고 이전 replica set를 가져옵니다.
$ kubectl rollout undo deployment/myapp-deployment
```





#### Summarize Commands

- Create

  `kubectl create -f deployment-definition.yml`

- Get

  `kubectl get deployments`

- Update

  `kubectl apply -f deployment-definition.yml`

  `kubectl set image deployment/myapp-deployment nginx=nginx:1.9.1`

- Status

  `kubectl rollout status deployment/myapp-deployment`

  `kubectl rollout history deployment/myapp-deployment`

- Rollback

  `kubectl rollout`

