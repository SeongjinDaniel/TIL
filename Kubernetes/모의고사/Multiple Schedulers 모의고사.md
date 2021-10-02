# Multiple Schedulers 모의고사



1. What is the name of the POD that deploys the default kubernetes scheduler in this environment?

   ```
   $ kubectl get pods --namespace=kube-system
   or
   # 스케줄러 포드가 실행 중인지 확인합니다.
   $ kubectl get pods -n kube-system
   ```

   

2. What is the image used to deploy the kubernetes scheduler?

   Inspect the kubernetes scheduler pod and identify the image

   **Hint**

   Run the command `kubectl describe pod kube-scheduler-controlplane --namespace=kube-system`

   ```
   $ kubectl describe pod kube-scheduler-controlplane --namespace=kube-system | grep -i image
   ```



3. Deploy an additional scheduler to the cluster following the given specification.

   Use the manifest file used by kubeadm tool. Use a different port than the one used by the current one.

   - Namespace: kube-system
   - Name: my-scheduler
   - Status: Running
   - Custom Scheduler Name

   **Solution**

   Copy **kube-scheduler.yaml** from the directory **/etc/kubernetes/manifests/** to any other location and then change the name to my-scheduler.

   Add or update the following command arguments in the YAML file:

   ```
   - --leader-elect=false
   - --port=10282
   - --scheduler-name=my-scheduler
   - --secure-port=0
   ```

   Here, we are setting **leader-elect** to false for our new custom scheduler called **my-scheduler**.

   We are also making use of a different port **10282** which is not currently in use in the controlplane.

   The default scheduler uses **secure-port** on port 10259 to serve HTTPS with authentication and authorization. This is not needed for our custom scheduler, so we can disable HTTPS by setting the value of **secure-port** to 0.

   

   Finally, because we have set **secure-port** to 0, replace HTTPS with HTTP and use the correct ports under liveness and startup probes.

   The final YAML file would look something like this:

   ```yaml
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       component: my-scheduler
       tier: control-plane
     name: my-scheduler
     namespace: kube-system
   spec:
     containers:
     - command:
       - kube-scheduler
       - --authentication-kubeconfig=/etc/kubernetes/scheduler.conf
       - --authorization-kubeconfig=/etc/kubernetes/scheduler.conf
       - --bind-address=127.0.0.1
       - --kubeconfig=/etc/kubernetes/scheduler.conf
       - --leader-elect=false
       - --port=10282
       - --scheduler-name=my-scheduler
       - --secure-port=0
       image: k8s.gcr.io/kube-scheduler:v1.19.0
       imagePullPolicy: IfNotPresent
       livenessProbe:
         failureThreshold: 8
         httpGet:
           host: 127.0.0.1
           path: /healthz
           port: 10282
           scheme: HTTP
         initialDelaySeconds: 10
         periodSeconds: 10
         timeoutSeconds: 15
       name: kube-scheduler
       resources:
         requests:
           cpu: 100m
       startupProbe:
         failureThreshold: 24
         httpGet:
           host: 127.0.0.1
           path: /healthz
           port: 10282
           scheme: HTTP
         initialDelaySeconds: 10
         periodSeconds: 10
         timeoutSeconds: 15
       volumeMounts:
       - mountPath: /etc/kubernetes/scheduler.conf
         name: kubeconfig
         readOnly: true
     hostNetwork: true
     priorityClassName: system-node-critical
     volumes:
     - hostPath:
         path: /etc/kubernetes/scheduler.conf
         type: FileOrCreate
       name: kubeconfig
   status: {}
   ```

   Run **kubectl create -f my-scheduler.yaml** and wait sometime for the container to be in running state.

   

   ```
   $ cd /etc/kubernetes/manifests/
   $ ls
   $ cp kube-scheduler.yaml /root/my-scheduler.yaml
   $ cd
   $ pwd
   $ vi my-scheduler.yaml
   $ kubectl apply -f my-scheduler.yaml
   ```

   

4. A POD definition file is given. Use it to create a POD with the new custom scheduler.

   File is located at `/root/nginx-pod.yaml`

   - Name: nginx
   - Uses custom scheduler
   - Status: Running

   Set schedulerName property on pod specification as my-scheduler.

   ```
   ---
   apiVersion: v1 
   kind: Pod 
   metadata:
     name: nginx 
   spec:
     schedulerName: my-scheduler
     containers:
     - image: nginx
       name: nginx
   ```

   Run `kubectl create -f nginx-pod.yaml`

   ```
   $ watch "kubectl get pods"
   ```

   

