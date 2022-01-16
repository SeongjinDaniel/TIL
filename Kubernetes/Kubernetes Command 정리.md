# Kubernetes Command 정리

1. **nslookup**
   
   ```sh
   $  kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
   ```

2. **pod selector 및 label 검색**
   
   ```shell
   $ kubectl get pods --selector env=dev
   $ kubectl get pods --selector bu=finance
   $ kubectl get all --selector env=prod,bu=finance,tier=frontend
   $ kubectl get pods --show-lables
   ```

3. **taint 제거**
   
   ```shell
   $ kubectl taint nodes controlplane node-role.kubernetes.io/master:NoSchedule-
   or
   $ kubectl edit nodes controlplane
   명령어를 이용해서 해당 관련 코드를 삭제한다.
   ```

4. **affinity 적용**
   
   해당 node label과 key, value가 맞으면 적용 가능!!

5. pod 강제 해당 yaml 파일과 변경하기
   
   ```shell
   $ kubectl replace -f test.yaml --force
   ```

6. daemonsets에 할당된 pod 조회
   
   ```shell
   $ kubectl describe daemonset kube-proxy -n kube-system
   ```

7. daemonsets 생성하기
   
   ```shell
   $ kubectl create deployment elasticsearch --image=k8s.gcr.io/fluentd-elasticsearch:1.20 -n kube-system --dry-run=client -o yaml > fluentd.yaml. 
   
   Next, remove the replicas, strategy and status fields from the YAML file using a text editor.
   Also, change the kind from Deployment to DaemonSet.
   Finally, create the Daemonset by running kubectl create -f fluentd.yaml
   ```

8. static pod 구분 방법
   
   - -controlplane라고 써있는 이름들은 static pod이다. 아마도 해당 node 이름이 마지막에 붙은 것을 추측할 수 있다.

9. CPU & MEMORY 확인
   
   - `kubectl top node`
   
   - `kubectl top pods`

10. configmap 생성 예제
    
    ```shell
    $ kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue
    ```

11. How many secrets are defined in the `default-token` secret?
    
    Run the command `kubectl describe secrets default-token-<id>` and look at the `data` field.  
    There are three secrets - `ca.crt`, `namespace` and `token`.

12. secret 생성
    
    ```shell
    $ kubectl create secret generic db-secret --from-literal=DB_Host=sql01 --from-literal=DB_User=root --from-literal=DB_Password=password123
    ```

13. node drain 생성
    
    ```shell
    $ kubectl drain node01 --ignore-daemonsets
    ```
    
    node01에 만약 설정된 pod가 있다면 drain할 때 --force를 사용해야한다.
    
    ```shell
    $ kubectl drain node01 --ignore-daemonsets --force
    ```
    
    drain을 하면 기존에 생성된 pod들은 영원히 삭제된다.
    
    그러나 cordon을 하면 pod는 남아 있는다.
    
    