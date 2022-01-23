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

5. **pod 강제 해당 yaml 파일과 변경하기**
   
   ```shell
   $ kubectl replace -f test.yaml --force
   ```

6. **daemonsets에 할당된 pod 조회**
   
   ```shell
   $ kubectl describe daemonset kube-proxy -n kube-system
   ```

7. **daemonsets 생성하기**
   
   ```shell
   $ kubectl create deployment elasticsearch --image=k8s.gcr.io/fluentd-elasticsearch:1.20 -n kube-system --dry-run=client -o yaml > fluentd.yaml. 
   
   Next, remove the replicas, strategy and status fields from the YAML file using a text editor.
   Also, change the kind from Deployment to DaemonSet.
   Finally, create the Daemonset by running kubectl create -f fluentd.yaml
   ```

8. **static pod 구분 방법**
   
   - -controlplane라고 써있는 이름들은 static pod이다. 아마도 해당 node 이름이 마지막에 붙은 것을 추측할 수 있다.

9. **CPU & MEMORY 확인**
   
   - `kubectl top node`
   
   - `kubectl top pods`

10. **configmap 생성 예제**
    
    ```shell
    $ kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue
    ```

11. How many secrets are defined in the `default-token` secret?
    
    Run the command `kubectl describe secrets default-token-<id>` and look at the `data` field.  
    There are three secrets - `ca.crt`, `namespace` and `token`.

12. **secret 생성**
    
    ```shell
    $ kubectl create secret generic db-secret --from-literal=DB_Host=sql01 --from-literal=DB_User=root --from-literal=DB_Password=password123
    ```

13. **node drain 생성**
    
    ```shell
    $ kubectl drain node01 --ignore-daemonsets
    ```
    
    node01에 만약 설정된 pod가 있다면 drain할 때 --force를 사용해야한다.
    
    ```shell
    $ kubectl drain node01 --ignore-daemonsets --force
    ```
    
    drain을 하면 기존에 생성된 pod들은 영원히 삭제된다.
    
    그러나 cordon을 하면 pod는 남아 있는다.

14. How many nodes can host workloads in this cluster?
    
    Inspect the applications and taints set on the nodes.
    
    ```shell
    $ kubectl describe node controlplane | grep -i taint
    $ kubectl describe node node01 | grep -i taint
    ```

15. What is the version of ETCD running on the cluster?
    
    ```shell
    $ kubectl logs etcd-controlplane -n kube-system
    Look at the ETCD Logs using the command
    $ kubectl describe pod etcd-controlplane -n kube-system
    check the image used by the ETCD pod
    ```

16. **kubeconfig**
    
    ```shell
    $ kubectl config view
    $ kubectl config use-context
    $ kubectl config --kubeconfig=/root/my-kube-config use-context research
    To use that context, run the command
    $ kubectl config --kubeconfig=/root/my-kube-config current-context
    ```

17. Check if the user can list pods in the `default` namespace.
    
    ```shell
    $ kubectl get pods --as dev-user
    ```

18. secret type 확인
    
    ```shell
    $ kubectl create secret --help 
    
    Available Commands:
      docker-registry Create a secret for use with a Docker registry
      generic         Create a secret from a local file, directory or literal value
      tls             Create a TLS secret
    ```

19. secret 생성
    
    ```shell
    $ kubectl create secret docker-registry private-reg-cred --docker-username=dock_user --docker-password=dock_password --docker-server=myprivateregistry.com:5000 --docker-email=dock_user@myprivateregistry.com
    ```
    
    위 명령어는 도큐먼트에서 참고 할 수 있음

20. What is the user used to execute the sleep process within the `ubuntu-sleeper` pod?
    
    ```shell
    $ kubectl exec ubuntu-sleeper -- whoami
    ```

21. pod 로그 저장하는 방법
    
    ```shell
    $ kubectl exec [pod name] -- cat /var/app.log
    $ kubectl exec webapp -- cat /log/app.log
    ```

22. node01 mac address 찾는 법
    
    ```shell
    $ arp node01
    ```

23. If you were to ping google from the master node, which route does it take?
    
    What is the IP address of the Default Gateway?
    
    ```shell
    $ ip route show default
    default via 172.25.0.1 dev eth1
    ```

24. kube-scheduler의 port는 무엇이냐?
    
    ```shell
    $ netstat -nplt | grep scheduler
    tcp 0 0 127.0.0.1:10259 0.0.0.0:* LISTEN 3865/kube-scheduler
    ```

25. Inspect the kubelet service and identify the network plugin configured for Kubernetes.
    
    ```shell
    $ ps -aux | grep kubelet | grep --color network-plugin=
    ```

26. What is the path configured with all binaries of CNI supported plugins
    
    ```shell
    /opt/cni/bin
    ```

27. What is the CNI plugin configured to be used on this kubernetes cluster
    
    ```shell
    $ ls /etc/cni/net.d
    ```

28. What binary executable file will be run by kubelet after a container and its associated namespace are created.
    
    - Look at the `type` field in file `/etc/cni/net.d/10-flannel.conflist`

29. weave IPALLOC_RANGE 설정 
    
    Deploy `weave-net` networking solution to the cluster.
    
    Replace the default IP address and subnet of `weave-net` to the `10.50.0.0/16`
    
    ```shell
    $ kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')&env.IPALLOC_RANGE=10.50.0.0/16"
    ```

30. What is the POD IP address range configured by weave?
    
    - `ip addr show weave`

31. What is the default gateway configured on the PODs scheduled on node01?
    
    Try scheduling a pod on node01 and check ip route output
    
    ```shell
    $ ip addr show weave
    ```

32. What type of proxy is the kube-proxy configured to use?
    
    ```shell
    $ kubectl -n kube-system describe pod [proxy pod name]
    ```

33. 