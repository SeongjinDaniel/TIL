# Lightning Lab - 1

1. Upgrade the current version of kubernetes from `1.19` to `1.20.0` exactly using the `kubeadm` utility. Make sure that the upgrade is carried out one node at a time starting with the master node. To minimize downtime, the deployment `gold-nginx` should be rescheduled on an alternate node before upgrading each node.

   Upgrade `controlplane` node first and drain node `node01` before upgrading it. Pods for `gold-nginx` should run on the `controlplane` node subsequently.

   - Cluster Upgraded?
   - pods 'gold-nginx' running on controlplane?

   

   참조

   - https://v1-20.docs.kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/#kubeadm-upgrade-%ED%98%B8%EC%B6%9C

2. Print the names of all deployments in the `admin2406` namespace in the following format:
   `DEPLOYMENT CONTAINER_IMAGE READY_REPLICAS NAMESPACE`
   `<deployment name> <container image used> <ready replica count> <Namespace>`
   . The data should be sorted by the increasing order of the `deployment name`.

   Example:
   `DEPLOYMENT CONTAINER_IMAGE READY_REPLICAS NAMESPACE`
   `deploy0 nginx:alpine 1 admin2406`
   Write the result to the file `/opt/admin2406_data`.

   - Task completed?

   아래 명령은 쿠버네티스 치트시트 참고

   ```
   $ kubectl get deploy --namespace admin2406 --output=custom-columns="DEPLOYMENT:.metadata.name,CONTAINER_IMAGE:.spec.template.spec.containers[*].image,READY_REPLICAS:.status.readyReplicas,NAMESPACE:.metadata.namespace" > /opt/admin2406_data
   ```

3. A kubeconfig file called `admin.kubeconfig` has been created in `/root/CKA`. There is something wrong with the configuration. Troubleshoot and fix it.

   - Fix /root/CKA/admin.kubeconfig

   ```
   $ kubectl config view
   $ vi /root/CKA/admin.kubeconfig
   에서 포트 수정
   ```

4. Create a new deployment called `nginx-deploy`, with image `nginx:1.16` and `1` replica. Next upgrade the deployment to version `1.17` using `rolling update`.

   - Image: nginx:1.16
   - Task: Upgrade the version of the deployment to 1:17

   아래 명령은 쿠버네티스 치트시트 참고

   ```
   $ kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record
   $ kubectl rollout history deployment/nginx-deploy
   위 명령어로 확인
   ```

5. A new deployment called `alpha-mysql` has been deployed in the `alpha` namespace. However, the pods are not running. Troubleshoot and fix the issue. The deployment should make use of the persistent volume `alpha-pv` to be mounted at `/var/lib/mysql` and should use the environment variable `MYSQL_ALLOW_EMPTY_PASSWORD=1` to make use of an empty root password.

   Important: Do not alter the persistent volume.

   - Troubleshoot and fix the issues

   **Solution**

   ```yaml
   Use the command kubectl describe and try to fix the issue.
   Solution manifest file to create a pvc called mysql-alpha-pvc as follows:
   
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: mysql-alpha-pvc
     namespace: alpha
   spec:
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
         storage: 1Gi
     storageClassName: slow
   ```

6. Take the backup of ETCD at the location `/opt/etcd-backup.db` on the `controlplane` node.

   참조
   https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/

   ```
   $ kubectl get pods -A
   위 조회해서 나온 etcd를 describe 하면 아래 필요한 내용을 얻을 수 있음
   $ kubectl describe get pod <etcd-pod>
   $ ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
     --cacert=<trusted-ca-file> --cert=<cert-file> --key=<key-file> \
     snapshot save <backup-file-location>
   ```

   

7. Create a pod called `secret-1401` in the `admin1401` namespace using the `busybox` image. The container within the pod should be called `secret-admin` and should sleep for `4800` seconds.

   The container should mount a `read-only` secret volume called `secret-volume` at the path `/etc/secret-volume`. The secret being mounted has already been created for you and is called `dotfile-secret`.

   - Pod created correctly?

   pod 생성

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     creationTimestamp: null
     labels:
       run: secret-1401
     name: secret-1401
     namespace: admin1401
   spec:
     containers:
     - image: busybox
       name: secret-admin
       resources: {}
       command: ["sleep", "4800"]
       volumeMounts:
       - mountPath: /etc/secret-volume
         name: secret-volume
     volumes:
     - name: secret-volume
       secret:
         secretName: dotfile-secret
     dnsPolicy: ClusterFirst
     restartPolicy: Always
   status: {}
   ```

   