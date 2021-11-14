# Mock-Exam 3



1. Create a new service account with the name `pvviewer`. Grant this Service account access to `list` all PersistentVolumes in the cluster by creating an appropriate cluster role called `pvviewer-role` and ClusterRoleBinding called `pvviewer-role-binding`.
   Next, create a pod called `pvviewer` with the image: `redis` and serviceAccount: `pvviewer` in the default namespace.
   - 
     ServiceAccount: pvviewer
   - ClusterRole: pvviewer-role
   - ClusterRoleBinding: pvviewer-role-binding
   - Pod: pvviewer
   - Pod configured to use ServiceAccount pvviewer ?

```
$ kubectl create serviceaccount pvviewer
$ kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
$ kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --
serviceaccount=default:pvviewer
$ kubectl run pvviewer --image=redis --dry-run=client -o yaml > pod.yaml
$ vi pod.yaml

apiVersion: v1
kind: Pod
metadata:
  name: pvviewer
spec:
  containers:
  - image: redis
    name: pvviewer
  serviceAccountName: pvviewer

$ kubectl apply -f pod.yaml
```



**Solution**

Pods authenticate to the API Server using ServiceAccounts. If the serviceAccount name is not specified, the default service account for the namespace is used during a pod creation.
Reference: `https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/`

Now, create a service account `pvviewer`:

```sh
kubectl create serviceaccount pvviewer
```

To create a clusterrole:

```sh
kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
```

To create a clusterrolebinding:

```sh
kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --serviceaccount=default:pvviewer
```

Solution manifest file to create a new pod called `pvviewer` as follows:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: pvviewer
  name: pvviewer
spec:
  containers:
  - image: redis
    name: pvviewer
  # Add service account name
  serviceAccountName: pvviewer
```



2. List the `InternalIP` of all nodes of the cluster. Save the result to a file `/root/CKA/node_ips`.

   Answer should be in the format: `InternalIP of controlplane`<space>`InternalIP of node01` (in a single line)

   - Task Completed

   

   **참조**

   https://kubernetes.io/docs/reference/kubectl/cheatsheet/

   ```
   # Get ExternalIPs of all nodes
   kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}'
   ```

   ExternalIP를 InternalIP로 변경

   ```
   $ kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' > /root/node_ips
   ```

   

3. Create a pod called `multi-pod` with two containers.
   Container 1, name: `alpha`, image: `nginx`
   Container 2: name: `beta`, image: `busybox`, command: `sleep 4800`

   Environment Variables:
   container 1:
   `name: alpha`

   Container 2:
   `name: beta`

   - Pod Name: multi-pod
   - Container 1: alpha
   - Container 2: beta
   - Container beta commands set correctly?
   - Container 1 Environment Value Set
   - Container 2 Environment Value Set



4. Create a Pod called `non-root-pod` , image: `redis:alpine`
   runAsUser: 1000
   fsGroup: 2000
   - Pod non-root-pod fsGroup configured
   - Pod non-root-pod runAsUser configured



5. We have deployed a new pod called `np-test-1` and a service called `np-test-service`. Incoming connections to this service are not working. Troubleshoot and fix it.
   Create NetworkPolicy, by the name `ingress-to-nptest` that allows incoming connections to the service over port `80`.

   Important: Don't delete any current objects deployed.

   - Important: Don't Alter Existing Objects!
   - NetworkPolicy: Applied to All sources (Incoming traffic from all pods)?
   - NetWorkPolicy: Correct Port?
   - NetWorkPolicy: Applied to correct Pod?

   

   https://kubernetes.io/docs/concepts/services-networking/network-policies/

   ```
   kubectl describe svc np-test-service
   kubectl get netpol
   kubectl describe netpol default-deny
   ```

   - 정책이 그냥 모든 인그레스 트래픽 거부

   - 새로 만들어서 port 80 허용하는 network policy 만들자

   ```
   apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: ingress-to-nptest
     namespace: default
   spec:
     podSelector:
       matchLabels:
         run: np-test-1
     ingress:
       ports:
       -  protocol: TCP
          port: 80
     policyTypes:
     - Ingress
   ```

   #### 연결 테스트 방법

   ```
   $ kubectl run test-np --image=busybox:1.28 --rm -it -- sh
   nc -z -v -w 2 np-test-service 80
   ```

   `nc`: netcat
   `-z`: 스캔 시 사용, 연결되면 바로 닫는 용도
   `-v`: verbose
   `-w secs`: secs 시간 후 타임아웃

6. Taint the worker node `node01` to be Unschedulable. Once done, create a pod called `dev-redis`, image `redis:alpine`, to ensure workloads are not scheduled to this worker node. Finally, create a new pod called `prod-redis` and image: `redis:alpine` with toleration to be scheduled on `node01`.

   key: `env_type`, value: `production`, operator: `Equal` and effect: `NoSchedule`

   - 
     Key = env_type
   - Value = production
   - Effect = NoSchedule
   - pod 'dev-redis' (no tolerations) is not scheduled on node01?
   - Create a pod 'prod-redis' to run on node01

   

   https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

   ```
   $ kubectl taint node node01 env_type=production:NoSchedule
   $ kubectl run dev-redis --image=redis:alpine
   ```

   node01에 할당되지 않은 것 확인

   ```
   $ kubectl get pods -o wide
   ```

   toleration pod 생성

   ```
   $ kubectl run prod-redis --image=redis:alpine --dry-run=client -o yaml > pod.yaml
   $ vi pod.yaml
   
   apiVersion: v1
   kind: Pod
   metadata:
     name: prod-redis
   spec:
     containers:
     - name: prod-redis
       image: redis:alpine
     tolerations:
     - key: "env_typey"
       operator: "Equal"
       value: "production"
       effect: "NoSchedule"
   ```

   생성 및 확인

   ```
   $ kubectl apply -f pod.yaml
   $ kubectl get pods -o wide
   ```



7. Create a pod called `hr-pod` in `hr` namespace belonging to the `production` environment and `frontend` tier .
   image: `redis:alpine`

   Use appropriate labels and create all the required objects if it does not exist in the system already.

   - hr-pod labeled with environment production?
   - hr-pod labeled with tier frontend?

   

   ```
   $ kubectl create ns hr
   $ kubectl run hr-pod  --image=redis:alpine --labels=environment=production,tier=frontend --namespace=hr
   ```

   확인

   ```
   $ kubectl -n hr get pods --show-labels
   ```



8. A kubeconfig file called `super.kubeconfig` has been created under `/root/CKA`. There is something wrong with the configuration. Troubleshoot and fix it.

   - Fix /root/CKA/super.kubeconfig

   ```
   $ kubectl config view
   # server 어쩌구 port 6443 확인
   $ vi /root/CKA/super.kubeconfig
   # port 9999에서 6443으로 수정
   ```

   

9. We have created a new deployment called `nginx-deploy`. scale the deployment to 3 replicas. Has the replica's increased? Troubleshoot the issue and fix it.

   - deployment has 3 replicas

   

   https://kubernetes.io/docs/reference/kubectl/cheatsheet/

   ```
   kubectl scale deployment nginx-deploy --replicas=3
   kubectl describe deployment.app nginx-deploy
   kubectl -n kube-system get pods
   ```

   kube-controller-manager-master가 문제

   ```
   cd /etc/kubernetes/manifests
   vi kube-controller-manager.yaml
   ```

   contro1ler로 되어있는걸 controller로 수정

   `sed -i 's/kube-contro1ler-manager/kube-controller-manager/g' /etc/kubernetes//manifests/kube-controller-manager.yaml`