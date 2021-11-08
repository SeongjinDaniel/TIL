# Mock-Exam 1



1. 

   ```
   $ kubectl run nginx-pod --image=nginx:alpine
   $ kubectl get pods
   ```

2. 

   ```
   $ kubectl run messaging --image=redis:alpine -l tier=msg
   $ kubectl get pods --show-labels
   ```

3. 

   ```
   $ kubectl create ns apx-x9984574
   ```

4. 

   ```
   $ kubectl get nodes -o json
   $ kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json
   ```

5. 

   ```
   $ kubectl expose pod messaging --name messaging-service --port 6379 --targer-port 6379
   $ kubectl describe svc messaging-service
   #위 명령어를 사용하면 Endpoints를 확인할 수 있다.
   ```

6. 

   ```
   $ kubectl create deployment hr-web-app --image=kidekloud/webapp-color
   $ kubectl scale deployment hr-web-app --replicas=2
   $ kubectl get deployments.apps
   ```

7. 

   ```
   $ kubectl run static-busybox --image=busybox --command sleep 1000 --dry-run=client -o yaml > static-busybox.yaml
   $ cat static-busybox.yaml
   $ ls -l /etc/kubenetes/manifests/
   $ cd /var/lib/kubelet/
   $ grep -i staticPod config.yaml
   staticPodPath: /etc/kubernetes/manifests
   $ mv static-busybox.yaml /etc/kubernetes/manifests/
   $ kubectl get pods
   ```

8. 

   ```
   $ kubectl run temp-bus --image=redis:alpine --namespace finance --dry-run=client -o yaml > pod.yaml
   # namespace 명령이 제대로 작동하지 않았으므로 vi pod.yaml 에서 수정해준다.
   metadata.namespace: finance
   $ kubectl apply -f pod.yaml
   $ kubectl -n finance get pods
   ```

9. 

   ```
   $ kubectl get deployments.apps
   $ kubectl get pods
   $ kubectl describe pod orange
   # sleeeep 이상 하다는 것을 알수 있다.
   수정하고 
   $ kubectl delete pod orange
   $ kubectl apply -f pod.yaml
   $ kubectl get pods # 러닝 되는지 확인
   ```

10. 

    ```
    $ kubectl expose deployment hr-web-app --name hr-eweb-app-service --type=NodePort --port 8080 --target-port 8080 --dry-run=client -o yaml > svc.yaml
    # spec.ports.nodePort: 30082을 추가
    $ kubectl apply -f svc.yaml
    $ kubectl describe svc hr-web-app-service
    # 위 명령어로 Endpoints를 확인한다.
    ```

11. 

    ```
    $ kubectl get nodes -o jsonpath='{.items[*].status}'
    $ kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo}'
    $ kubectl get nodes -o json | less
    $ kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.osImage}' > /opt/outputs/nodes_os_x43kj56.txt
    ```

12. 

    k8s documentation에서 persistent volume yaml 적절한 예제를 찾아서 복붙 하면서 해결한다.

    ```
    ~~~~~
    $ kubectl explain pv --recursive | less
    ...
    $kubectl create -f pv.yaml
    $ kubectl get pv
    $ kubectl describe pv pv-analytics
    ```

    