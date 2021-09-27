# Cluster Upgrade Process 모의고사



1. This lab tests your skills on **upgrading a kubernetes cluster**. We have a production cluster with applications running on it. Let us explore the setup first.

   What is the current version of the cluster?

   **Hint**

   - Run: `kubectl get nodes` and look at the `VERSION`

   ```
   $ kubectl get nodes
   ```

   Or

   ```
   $ kubectl version --short
   ```

2. How many nodes are part of this cluster?

   Including master and worker nodes

   ```
   $ kubectl get nodes
   ```

3. How many nodes can host workloads in this cluster?

   Inspect the applications and taints set on the nodes.

   **Hint**

   - Check the taints on both `controlplane` and `node01`. If none exists, then both nodes can host workloads.

   **Solution**

   - By running the `kubectl describe node` command, we can see that neither nodes have taints.

   ```
   root@controlplane:~# kubectl describe nodes  controlplane | grep -i taint
   Taints:             <none>
   root@controlplane:~# 
   root@controlplane:~# kubectl describe nodes  node01 | grep -i taint
   Taints:             <none>
   root@controlplane:~# 
   ```

   This means that both nodes have the ability to schedule workloads on them.

4. How many applications are hosted on the cluster?

   Count the number of deployments.

   ```
   $ kubectl get deployments
   ```

5. What nodes are the pods hosted on?

   ```
   $ kubectl get pods -o wide
   ```

6. You are tasked to upgrade the cluster. User's accessing the applications must not be impacted. And you cannot provision new VMs. What strategy would you use to upgrade the cluster?

   **Hint**

   - In order to ensure minimum downtime, upgrade the cluster one node at a time, while moving the workloads to another node. In the upcoming tasks you will get to practice how to do that.

   `Answer: Upgrade one node at a time while moving the workloads to the other` 

7. What is the latest stable version available for upgrade?

   Use the `kubeadm` tool

   ```
   $ kubeadm upgrade plan
   ```

8. We will be upgrading the master node first. Drain the master node of workloads and mark it `UnSchedulable`

   - Master Node: SchedulingDisabled

   **Hint**

   - Run the `kubectl drain controlplane --ignore-daemonsets`

   **Solution**

   - There are `daemonsets` created in this cluster, especially in the **kube-system** namespace. To ignore these objects and drain the node, we can make use of the **--ignore-daemonsets** flag.

9. Upgrade the `controlplane` components to exact version `v1.20.0`

   Upgrade kubeadm tool (if not already), then the master components, and finally the kubelet. Practice referring to the kubernetes documentation page. Note: While upgrading kubelet, if you hit dependency issue while running the `apt-get upgrade kubelet` command, use the `apt install kubelet=1.20.0-00` command instead

   - controlplane Upgraded to v1.20.0
   - controlplane Kubelet Upgraded to v1.20.0

   **Solution**

   On the controlplane node, run the command run the following commands:

   1. `apt update`
      This will update the package lists from the software repository.
   2. `apt install kubeadm=1.20.0-00`
      This will install the kubeadm version 1.20
   3. `kubeadm upgrade apply v1.20.0`
      This will upgrade kubernetes controlplane. Note that this can take a few minutes.
   4. `apt install kubelet=1.20.0-00` This will update the kubelet with the version 1.20.
   5. You may need to restart kubelet after it has been upgraded.
      Run: `systemctl restart kubelet`

10. Mark the `controlplane` node as "Schedulable" again

    - Master Node: Ready & Schedulable

    ```
    $ kubectl uncordon controlplane
    ```

11. Next is the worker node. `Drain` the worker node of the workloads and mark it `UnSchedulable`

    - Worker node: Unschedulable

    ```
    $ kubectl drain node01 --ignore-daemonsets
    ```

12. Upgrade the worker node to the exact version `v1.20.0`

    - 
      Worker Node Upgraded to v1.20.0
    - Worker Node Ready

    **Solution**

    On the node01 node, run the command run the following commands:

    1. If you are on the master node, run `ssh node01` to go to `node01`
    2. `apt update`
       This will update the package lists from the software repository.
    3. `apt install kubeadm=1.20.0-00`
       This will install the kubeadm version 1.20
    4. `kubeadm upgrade node`
       This will upgrade the node01 configuration.
    5. `apt install kubelet=1.20.0-00` This will update the kubelet with the version 1.20.
    6. You may need to restart kubelet after it has been upgraded.
       Run: `systemctl restart kubelet`
    7. Type `exit` or enter `CTL + d` to go back to the controlplane node.

    

13. Remove the restriction and mark the worker node as schedulable again.

    ```
    $ kubectl uncordon node01
    ```

    