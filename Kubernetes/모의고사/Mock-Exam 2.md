# Mock Exam2



1. Take a backup of the etcd cluster and save it to `/opt/etcd-backup.db`.

   - Backup Completed

   https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/

   

2. Create a Pod called `redis-storage` with image: `redis:alpine` with a Volume of type `emptyDir` that lasts for the life of the Pod.

   Specs on the below.

   - Pod named 'redis-storage' created
   - Pod 'redis-storage' uses Volume type of emptyDir
   - Pod 'redis-storage' uses volumeMount with mountPath = /data/redis

   

   https://kubernetes.io/docs/concepts/storage/volumes/

   ```
   $ kubectl run redis-storage --image=redis:alpine --dry-run=client -o yaml > redis-storage-pod.yaml
   
   apiVersion: v1
   kind: Pod
   metadata:
     creationTimestamp: null
     labels:
       run: redis-storage
     name: redis-storage
   spec:
     containers:
     - image: redis:alpine
       name: redis-storage
       resources: {}
       volumeMounts:
       - mountPath: /data/redis
         name: redis-volume
     volumes:
     - name: redis-volume
       emptyDir: {}
     dnsPolicy: ClusterFirst
     restartPolicy: Always
   status: {}
   ```

   수정 부분 

   ```
       volumeMounts:
       - mountPath: /data/redis
         name: redis-volume
     volumes:
     - name: redis-volume
       emptyDir: {}
   ```

   

3. Create a new pod called `super-user-pod` with image `busybox:1.28`. Allow the pod to be able to set `system_time`.

   The container should sleep for 4800 seconds.

   - 
     Pod: super-user-pod
   - Container Image: busybox:1.28
   - SYS_TIME capabilities for the conatiner?
   
   ```
   $ kubectl run super-user-pod --image=busybox:1.28 --command sleep 4800 --dry-run=client -o yaml > super-user-pod-03.yaml
   super-user-pod-03.yaml에서 아래 추가
   
   securityContext:
         capabilities:
           add: ["SYS_TIME"]
           
   $ kubectl create -f super-user-pod-03.yaml
   ```
   
   https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ 참고

4. A pod definition file is created at `/root/CKA/use-pv.yaml`. Make use of this manifest file and mount the persistent volume called `pv-1`. Ensure the pod is running and the PV is bound.

   mountPath: `/data`
   persistentVolumeClaim Name: `my-pvc`

   - persistentVolume Claim configured correctly
   - pod using the correct mountPath
   - pod using the persistent volume claim?

   https://kubernetes.io/docs/concepts/storage/persistent-volumes/

   pvc 생성

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: my-pvc
   spec:
     accessModes:
       - ReadWriteOnce
     volumeMode: Filesystem
     resources:
       requests:
         storage: 10Mi
   ```

   `kubectl get pvc`

   `kubectl get pv` 둘다 status bound인지 확인

   pod 생성

   ```
   $ kubectl run test-04-pod --image=nginx --dry-run=client -o yaml > test-04-pod.yaml
   ```

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     creationTimestamp: null
     labels:
       run: test-04-pod
     name: test-04-pod
   spec:
     containers:
     - image: nginx
       name: test-04-pod
       resources: {}
       volumeMounts:
         - mountPath: "/data"
           name: my-pvc
     volumes:
       - name: my-pvc
         persistentVolumeClaim:
           claimName: my-pvc
     dnsPolicy: ClusterFirst
     restartPolicy: Always
   status: {}
   ```

   수정 부분

   ```yaml
       volumeMounts:
         - mountPath: "/data"
           name: my-pvc
     volumes:
       - name: my-pvc
         persistentVolumeClaim:
           claimName: my-pvc
   ```

   ```
   $ kubectl apply -f test-04-pod.yaml
   ```

   확인

   ```
   $ kubectl get pods
   ```

   ***틀림***

   **Solution**

   Add a `persistentVolumeClaim` definition to pod definition file.

   Solution manifest file to create a pvc `my-pvc` as follows:

   ```yaml
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: my-pvc
   spec:
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
          storage: 10Mi
   ```

   And then, update the pod definition file as follows:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     creationTimestamp: null
     labels:
       run: use-pv
     name: use-pv
   spec:
     containers:
     - image: nginx
       name: use-pv
       volumeMounts:
       - mountPath: "/data"
         name: mypd
     volumes:
       - name: mypd
         persistentVolumeClaim:
           claimName: my-pvc
   ```

   Finally, create the pod by running: `kubectl create -f /root/CKA/use-pv.yaml`

   

5. Create a new deployment called `nginx-deploy`, with image `nginx:1.16` and `1` replica. Record the version. Next upgrade the deployment to version `1.17` using rolling update. Make sure that the version upgrade is recorded in the resource annotation.

   - Deployment : nginx-deploy. Image: nginx:1.16
   - Image: nginx:1.16
   - Task: Upgrade the version of the deployment to 1:17
   - Task: Record the changes for the image upgrade

   ***틀림***

   **Solution**

   Explore the `--record` option while creating the deployment while working with the deployment definition file. Then make use of the `kubectl apply` command to create or update the deployment.

   To create a deployment definition file `nginx-deploy`:

   ```sh
   $ kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > deploy.yaml
   ```

   To create a resource from definition file and to record:

   ```sh
   $ kubectl apply -f deploy.yaml --record
   ```

   To view the history of deployment `nginx-deploy`:

   ```sh
   $ kubectl rollout history deployment nginx-deploy
   ```

   To upgrade the image to next given version:

   ```sh
   $ kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record
   ```

   To view the history of deployment `nginx-deploy`:

   ```sh
   $ kubectl rollout history deployment nginx-deploy
   ```

6. Create a new user called `john`. Grant him access to the cluster. John should have permission to `create, list, get, update and delete pods` in the `development` namespace . The private key exists in the location: `/root/CKA/john.key` and csr at `/root/CKA/john.csr`.

   `Important Note`: As of kubernetes 1.19, the CertificateSigningRequest object expects a `signerName`.

   Please refer the documentation to see an example. The documentation tab is available at the top right of terminal.

   

   `kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development`

   `kubectl create rolebinding developer-role-binding --role=developer --user=john --namespace=development`

   **검증**

   `$ kubectl auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL]`
   
   - `kubectl auth can-i update pods --as=john`
   
     위와 같이 하면 pod를 수정할 수 있는지 체크하게 되는데 결과는 no이다. 네임스페이스를 명명하고 다시 실행하면 yes가 나올것이다.
   
     `kubectl auth can-i update pods -n development --as=john`
   

**참조**

- https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#normal-user

  

  **Solution**

  Solution manifest file to create a CSR as follows:

  ```yaml
  ---
  apiVersion: certificates.k8s.io/v1
  kind: CertificateSigningRequest
  metadata:
    name: john-developer
  spec:
    signerName: kubernetes.io/kube-apiserver-client
    request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZEQ0NBVHdDQVFBd0R6RU5NQXNHQTFVRUF3d0VhbTlvYmpDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRApnZ0VQQURDQ0FRb0NnZ0VCQUt2Um1tQ0h2ZjBrTHNldlF3aWVKSzcrVVdRck04ZGtkdzkyYUJTdG1uUVNhMGFPCjV3c3cwbVZyNkNjcEJFRmVreHk5NUVydkgyTHhqQTNiSHVsTVVub2ZkUU9rbjYra1NNY2o3TzdWYlBld2k2OEIKa3JoM2prRFNuZGFvV1NPWXBKOFg1WUZ5c2ZvNUpxby82YU92czFGcEc3bm5SMG1JYWpySTlNVVFEdTVncGw4bgpjakY0TG4vQ3NEb3o3QXNadEgwcVpwc0dXYVpURTBKOWNrQmswZWhiV2tMeDJUK3pEYzlmaDVIMjZsSE4zbHM4CktiSlRuSnY3WDFsNndCeTN5WUFUSXRNclpUR28wZ2c1QS9uREZ4SXdHcXNlMTdLZDRaa1k3RDJIZ3R4UytkMEMKMTNBeHNVdzQyWVZ6ZzhkYXJzVGRMZzcxQ2NaanRxdS9YSmlyQmxVQ0F3RUFBYUFBTUEwR0NTcUdTSWIzRFFFQgpDd1VBQTRJQkFRQ1VKTnNMelBKczB2czlGTTVpUzJ0akMyaVYvdXptcmwxTGNUTStsbXpSODNsS09uL0NoMTZlClNLNHplRlFtbGF0c0hCOGZBU2ZhQnRaOUJ2UnVlMUZnbHk1b2VuTk5LaW9FMnc3TUx1a0oyODBWRWFxUjN2SSsKNzRiNnduNkhYclJsYVhaM25VMTFQVTlsT3RBSGxQeDNYVWpCVk5QaGhlUlBmR3p3TTRselZuQW5mNm96bEtxSgpvT3RORStlZ2FYWDdvc3BvZmdWZWVqc25Yd0RjZ05pSFFTbDgzSkljUCtjOVBHMDJtNyt0NmpJU3VoRllTVjZtCmlqblNucHBKZWhFUGxPMkFNcmJzU0VpaFB1N294Wm9iZDFtdWF4bWtVa0NoSzZLeGV0RjVEdWhRMi80NEMvSDIKOWk1bnpMMlRST3RndGRJZjAveUF5N05COHlOY3FPR0QKLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tCg==
    usages:
    - digital signature
    - key encipherment
    - client auth
    groups:
    - system:authenticated
  ```

  To approve this certificate, run: `kubectl certificate approve john-developer`

  Next, create a role `developer` and rolebinding `developer-role-binding`, run the command:

  ```sh
  $ kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development
  
  $ kubectl create rolebinding developer-role-binding --role=developer --user=john --namespace=development
  ```

  To verify the permission from kubectl utility tool:

  ```sh
  $ kubectl auth can-i update pods --as=john --names ????????
  $ kubectl auth can-i update pods --as=john -name
  ```
  
  ```
  $ kubectl certificate approve john-developer
  ```
  
  ---
  
  `kubectl create sa john -n development`
7. Create a nginx pod called `nginx-resolver` using image `nginx`, expose it internally with a service called `nginx-resolver-service`. Test that you are able to look up the service and pod names from within the cluster. Use the image: `busybox:1.28` for dns lookup. Record results in `/root/CKA/nginx.svc` and `/root/CKA/nginx.pod`

   ```
   $ kubectl run nginx-resolver --image=nginx --port=80
   $ kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP
   
   or 
   
   $ kubectl run nginx-resolver --image=nginx --port=80 --expose --dry-run=client -o yaml > nginx-resolver.yaml
   ```

   

   **Solution**

   Use the command `kubectl run` and create a nginx pod and busybox pod. Resolve it, nginx service and its pod name from `busybox` pod.

   To create a pod `nginx-resolver` and expose it internally:

   ```sh
   kubectl run nginx-resolver --image=nginx
   kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP
   ```

   To create a pod `test-nslookup`. Test that you are able to look up the service and pod names from within the cluster:

   ```sh
   $  kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
   $  kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service > /root/CKA/nginx.svc
   ```

   Get the IP of the `nginx-resolver` pod and replace the dots(.) with hyphon(-) which will be used below.

   ```sh
   $  kubectl get pod nginx-resolver -o wide
   $  kubectl run test-nslookup --image=busybox:1.28 --r
   ```

$  kubectl get pod nginx-resolver -o wide
$  kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup <P-O-D-I-P.default.pod> > /root/CKA/nginx.pod
위는 아래와 같이
kubectl run test-nslookup --image=busybox:1.28 --restart=Never --rm -it -- nslookup 10-244-2-2.default.pod > /root/CKA/nginx.pod
   ```

   --rm 옵션은 실행이 끝나면 자동으로 Pod이 삭제되게끔 하는 옵션인데 이게 동작할려면 -it 옵션을 같이 붙여야 한다. (Pod가 이미 연결(attach)되어 있는 상태여야 한다는 의미). nslookup을 통해 파라미터로 전달된 이름에 대한 ip를 가져오는 방법을 통해 Service와 Pod을 찾아오는 방법으로 해결한다.

첫번째 줄은 Service인 nginx-resolver-service의 이름 자체를 nslookup의 파라미터로 전달하여 그 결과로 IP를 가져오게 된다. kubernetes는 그 안에 자체 DNS 서버를 운영하는데 Service의 경우 Service의 이름을 DNS에 등록해둔다. 그래서 nslookup 명령어를 사용할 때 서비스 이름만으로도 동작이 가능했던 것이다. 두번째 줄은 Pod인 nginx-resolver에 대해 문제를 풀은건데 Service와는 다른 구조로 되어 있다. 10-244-2-2.default.pod 을 던지는데 이것을 해석하는 방법은 **Pod이 가지고 있는 IP.Pod이 속한 namespace.Resource 타입** 으로 보면 된다. Pod이 가지고 있는 IP는 **kubectl get pod -o wide** 하면 나오게 되는데 이 Pod이 가지고 있던 IP는 10.244.2.2 이다. IP를 표현할때 **. 대신 -를 사용**한것이다(DNS 이름에서는 .은 이미 예약되어 있기 때문에 사용할 수 없으니까..) 그리고 이 **Pod이 속한 namespace가 default**여서 default가 들어간 것이고, 마지막엔 **해당 Resource Type이 pod** 이니까 pod을 넣은것이다.

- 참조
  - [Kubernetes Mock Exam 정리(Mock Exam 2)](https://zgundam.tistory.com/195)
   ```

8. Create a static pod on `node01` called `nginx-critical` with image `nginx` and make sure that it is recreated/restarted automatically in case of a failure.

   Use `/etc/kubernetes/manifests` as the Static Pod path for example.

   **Solution**

   To create a static pod called `nginx-critical` by using below command:

   ```sh
   kubectl run nginx-critical --image=nginx --dry-run=client -o yaml > static.yaml
   ```
   
   Copy the contents of this file or use `scp` command to transfer this file from `controlplane` to `node01` node.
   
   ```
      root@controlplane:~# scp static.yaml node01:/root/
   ```
   
   To know the IP Address of the `node01` node:
   
      ```shell
      root@controlplane:~# kubectl get nodes -o wide
      
      # Perform SSH
      root@controlplane:~# ssh node01
      OR
      root@controlplane:~# ssh <IP of node01>
      ```
   
      On `node01` node:
      Check if static pod directory is present which is `/etc/kubernetes/manifests`, if it's not present then create it.
   
      ```shell
      root@node01:~# mkdir -p /etc/kubernetes/manifests
      ```
   
      Add that complete path to the `staticPodPath` field in the kubelet `config.yaml` file.
   
      ```shell
      root@node01:~# vi /var/lib/kubelet/config.yaml
      ```
   
      now, move/copy the static.yaml to path `/etc/kubernetes/manifests/`.
   
      ```shell
      root@node01:~# cp /root/static.yaml /etc/kubernetes/manifests/
      ```
   
      Go back to the `controlplane` node and check the status of static pod:
   
      ```shell
      root@node01:~# exit
      logout
      root@controlplane:~# kubectl get pods 
      ```
   
   ---
   
   mkdir -p 옵션을 사용할 경우에는 존재하지 않는 중간의 디렉토리를 자동을 생성해 준다.
   
   예를 들면 아래 명령어를 입력하면 에러가 난다.
   
   ```
   mkdir f1/f2/f3
   > mkdir: f1/f2: No such file or directory
   ```
   
   하지만 mkdir -p 옵션을 이용하면 중간 디렉토리 역시 자동으로 생성해 준다.
   
   ```
   > mkdir -p f1/f2/f3
   ```
   
   성공적으로 수행!
   
   즉, mkdir -p 옵션은 안전하게 파일 경로를 생성해 준다.