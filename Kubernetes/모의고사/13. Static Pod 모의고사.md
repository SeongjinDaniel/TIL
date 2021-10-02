# Static Pod 모의고사



1. How many static pods exist in this cluster in all namespaces?

   **Hint**

   - Run the command `kubectl get pods --all-namespaces` and look for those with `-controlplane` appended in the name

   ```
   $ kubectl get pods --all-namespace
   ```



2. Which of the below components is NOT deployed as a static pod?

   **Hint**

   - Run `kubectl get pods --all-namespaces` and look for the pod from the list that does not end with `-controlplane`

   ```
   $ kubectl get pods --all-namespace
   ```



3. Which of the below components is NOT deployed as a static POD?

   **Solution**

   - `kube-proxy` is deployed as a `DaemonSet` and hence, it is not a staic pod.

   ```
   $ kubectl get pods --all-namespace
   ```

   

4. On which nodes are the static pods created currently?

   ```
   $ kubectl get pods --all-namespaces -o wide
   ```



5. What is the path of the directory holding the static pod definition files?

   **Hint**

   Run the command `ps -aux | grep kubelet` and identify the config file - `--config=/var/lib/kubelet/config.yaml`. Then check in the config file for staticPodPath.

   **Solution**

   First idenity the kubelet config file:

   ```
   root@controlplane:~# ps -aux | grep /usr/bin/kubelet
   root      3668  0.0  1.5 1933476 63076 ?       Ssl  Mar13  16:18 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --network-plugin=cni --pod-infra-container-image=k8s.gcr.io/pause:3.2
   root      4879  0.0  0.0  11468  1040 pts/0    S+   00:06   0:00 grep --color=auto /usr/bin/kubelet
   root@controlplane:~# 
   ```

   From the output we can see that the kubelet config file used is `/var/lib/kubelet/config.yaml`

   Next, lookup the value assigned for `staticPodPath`:

   ```
   root@controlplane:~# grep -i staticpod /var/lib/kubelet/config.yaml
   staticPodPath: /etc/kubernetes/manifests
   root@controlplane:~# 
   ```

   As you can see, the path configured is the `/etc/kubernetes/manifests` directory.

   or

   ```
   $ ps -ef | grep kubelet
   $ grep -i static /var/lib/kubelt/config.yaml
   $ cd /etc/kubernetes/manifests
   $ ls
   ```

   



6. How many pod definition files are present in the manifests folder?

   ```
   $ ls /etc/kubernetes/manifests
   etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml
   ```

   

7. What is the docker image used to deploy the kube-api server as a static pod?

   **Hint**

   - Check the image defined in the `/etc/kubernetes/manifests/kube-apiserver.yaml` manifest file.

   ```
   $ vi /etc/kubernetes/manifests/kube-apiserver.yaml
   ```

   or

   ```
   grep -i image kube-apiserver.yaml
   ```

   

8. Create a static pod named `static-busybox` that uses the `busybox` image and the command `sleep 1000`

   - Name: static-busybox
   - Image: busybox

   **Hint**

   - Create a pod definition file called `static-busybox.yaml` with the provided specs and place it under `/etc/kubernetes/manifests` directory.

   **Solution**

   - Create a pod definition file in the manifests folder. To do this, run the command:
     `kubectl run --restart=Never --image=busybox static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml`

   ```
   $ kubectl run --restart=Never --image=busybox static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
   ```

   or

   ```
   $ kubectl run --restart=Never --image=busybox static-busybox --dry-run=client -o yaml --command -- sleep 1000 > static-busybox.yaml
   $ kubectl get pods
   ```

   

9. Edit the image on the static pod to use `busybox:1.28.4`

   - Name: static-busybox
   - Image: busybox:1.28.4

   **Solution**

   Simply edit the static pod definition file and save it. If that does not re-create the pod, run: `kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml`

   ```
   $ kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
   ```



10. We just created a new static pod named **static-greenbox**. Find it and delete it.

    This question is a bit tricky. But if you use the knowledge you gained in the previous questions in this lab, you should be able to find the answer to it.

    - Static pod deleted

    **Hint**

    Identify which node the static pod is created on, ssh to the node and delete the pod definition file.
    If you don't know the IP of the node, run the `kubectl get nodes -o wide` command and identify the IP.
    Then, SSH to the node using that IP. For static pod manifest path look at the file `/var/lib/kubelet/config.yaml` on node01

    **Solution**

    1. First, let's identify the node in which the pod called **static-greenbox** is created. To do this, run:

    ```
    root@controlplane:~# kubectl get pods --all-namespaces -o wide  | grep static-greenbox
    default       static-greenbox-node01                 1/1     Running   0          19s     10.244.1.2   node01       <none>           <none>
    root@controlplane:~#
    ```

    From the result of this command, we can see that the pod is running on node01.

    

    1. Next, SSH to node01 and identify the path configured for static pods in this node.
       `Important`: The path need not be `/etc/kubernetes/manifests`. Make sure to check the path configured in the kubelet configuration file.

    ```
    root@controlplane:~# ssh node01 
    
    root@node01:~# ps -ef |  grep /usr/bin/kubelet 
    root       752   654  0 00:30 pts/0    00:00:00 grep --color=auto /usr/bin/kubelet
    root     28567     1  0 00:22 ?        00:00:11 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --network-plugin=cni --pod-infra-container-image=k8s.gcr.io/pause:3.2
    root@node01:~# grep -i staticpod /var/lib/kubelet/config.yaml
    staticPodPath: /etc/just-to-mess-with-you
    root@node01:~# 
    ```

    Here the staticPodPath is `/etc/just-to-mess-with-you`

    

    1. Navigate to this directory and delete the YAML file:

    ```
    root@node01:/etc/just-to-mess-with-you# ls
    greenbox.yaml
    root@node01:/etc/just-to-mess-with-you# rm -rf greenbox.yaml 
    root@node01:/etc/just-to-mess-with-you#
    ```

    1. Exit out of node01 using `CTRL + D` or type `exit`. You should return to the `controlplane` node. Check if the `static-greenbox` pod has been deleted:

    ```
    root@controlplane:~# kubectl get pods --all-namespaces -o wide  | grep static-greenbox
    root@controlplane:~# 
    ```

    

    