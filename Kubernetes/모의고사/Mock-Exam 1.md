# Mock-Exam 1



1. Deploy a pod named `nginx-pod` using the `nginx:alpine` image.

   Once done, click on the `Next Question` button in the top right corner of this panel. You may navigate back and forth freely between all questions. Once done with all questions, click on `End Exam`. Your work will be validated at the end and score shown. Good Luck!

   - Name: nginx-pod
   - Image: nginx:alpine

   ```
   $ kubectl run nginx-pod --image=nginx:alpine
   $ kubectl get pods
   ```

2. Deploy a `messaging` pod using the `redis:alpine` image with the labels set to `tier=msg`.

   - 
     Pod Name: messaging
   - Image: redis:alpine
   - Labels: tier=msg

   ```
   $ kubectl run messaging --image=redis:alpine -l tier=msg
   $ kubectl get pods --show-labels
   ```

3. Create a namespace named `apx-x9984574`.

   - Namespace: apx-x9984574

   ```
   $ kubectl create ns apx-x9984574
   ```

4. Get the list of nodes in JSON format and store it in a file at `/opt/outputs/nodes-z3444kd9.json`.

   - Task completed

   ```
   $ kubectl get nodes -o json
   $ kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json
   ```

5. Create a service `messaging-service` to expose the `messaging` application within the cluster on port `6379`.

   Use imperative commands.

   - 
     Service: messaging-service
   - Port: 6379
   - Type: ClusterIp
   - Use the right labels

   ```
   $ kubectl expose pod messaging --name messaging-service --port 6379 --targer-port 6379
   $ kubectl describe svc messaging-service
   #위 명령어를 사용하면 Endpoints를 확인할 수 있다.
   ```

6. Create a deployment named `hr-web-app` using the image `kodekloud/webapp-color` with `2` replicas.

   - 
     Name: hr-web-app
   - Image: kodekloud/webapp-color
   - Replicas: 2

   ```
   $ kubectl create deployment hr-web-app --image=kidekloud/webapp-color
   $ kubectl scale deployment hr-web-app --replicas=2
   $ kubectl get deployments.apps
   ```

7. Create a static pod named `static-busybox` on the controlplane node that uses the `busybox` image and the command `sleep 1000`.

   - 
     Name: static-busybox
   - Image: busybox

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

8. Create a POD in the `finance` namespace named `temp-bus` with the image `redis:alpine`.

   - Name: temp-bus
   - Image Name: redis:alpine

   ```
   $ kubectl run temp-bus --image=redis:alpine --namespace finance --dry-run=client -o yaml > pod.yaml
   # namespace 명령이 제대로 작동하지 않았으므로 vi pod.yaml 에서 수정해준다.
   metadata.namespace: finance
   $ kubectl apply -f pod.yaml
   $ kubectl -n finance get pods
   ```

9. A new application `orange` is deployed. There is something wrong with it. Identify and fix the issue.

   - Issue fixed

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

10. Expose the `hr-web-app` as service `hr-web-app-service` application on port `30082` on the nodes on the cluster.

    The web application listens on port `8080`.

    - 
      Name: hr-web-app-service
    - Type: NodePort
    - Endpoints: 2
    - Port: 8080
    - NodePort: 30082

    ```
    $ kubectl expose deployment hr-web-app --name hr-eweb-app-service --type=NodePort --port 8080 --target-port 8080 --dry-run=client -o yaml > svc.yaml
    # spec.ports.nodePort: 30082을 추가
    $ kubectl apply -f svc.yaml
    $ kubectl describe svc hr-web-app-service
    # 위 명령어로 Endpoints를 확인한다.
    ```

11. Use JSON PATH query to retrieve the `osImage`s of all the nodes and store it in a file `/opt/outputs/nodes_os_x43kj56.txt`.

    The `osImages` are under the `nodeInfo` section under `status` of each node.

    - Task Completed

    ```
    $ kubectl get nodes -o jsonpath='{.items[*].status}'
    $ kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo}'
    $ kubectl get nodes -o json | less
    $ kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.osImage}' > /opt/outputs/nodes_os_x43kj56.txt
    ```

12. Create a `Persistent Volume` with the given specification.

    - 
      Volume Name: pv-analytics
    - Storage: 100Mi
    - Access modes: ReadWriteMany
    - Host Path: /pv/data-analytics

    k8s documentation에서 persistent volume yaml 적절한 예제를 찾아서 복붙 하면서 해결한다.

    ```
    ~~~~~
    $ kubectl explain pv --recursive | less
    ...
    $kubectl create -f pv.yaml
    $ kubectl get pv
    $ kubectl describe pv pv-analytics
    ```

    **Solution**

    Solution manifest file to create a persistent volume `pv-analytics` as follows:

    ```yaml
    ---
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: pv-analytics
    spec:
      capacity:
        storage: 100Mi
      volumeMode: Filesystem
      accessModes:
        - ReadWriteMany
      hostPath:
          path: /pv/data-analytics
    ```

