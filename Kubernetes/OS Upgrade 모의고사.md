# OS Upgrade 모의고사



1. Let us explore the environment first. How many nodes do you see in the cluster?

   Including the controlplane and worker nodes.

   ```
   $ kubectl get nodes
   ```

2. How many applications do you see hosted on the cluster?

   Check the number of deployments.

   ```
   $ kebectl get deployments
   
   ```

3. Which nodes are the applications hosted on?

   ```
   $ kubectl get pods -o wide
   ```

4. We need to take `node01` out for maintenance. Empty the node of all applications and mark it unschedulable.

   - Node node01 Unschedulable
   - Pods evicted from node01

   ```
   $ kubectl drain node01 --ignore-daemonsets
   ```

5. What nodes are the apps on now?

   ```
   $ kubectl get pods -o wide
   ```

6. The maintenance tasks have been completed. Configure the node `node01` to be schedulable again.

   - Node01 is Schedulable

   ```
   $ kubectl uncordon node01
   ```

7. How many pods are scheduled on `node01` now?

   ```
   $ kubectl get pods -o wide
   ```

8. Why are there no pods on `node01`?

   **Solution**

   - Running the `uncordon` command on a node will not automatically schedule pods on the node. When new pods are created, they will be placed on node01.

   `Answer: Only when new pods are created they will be scheduled`

9. Why are the pods placed on the `controlplane` node?

   Check the controlplane node details.

   **Solution**

   ```
   root@controlplane:~# kubectl describe node controlplane | grep -i  taint
   Taints:             <none>
   root@controlplane:~# 
   ```

   - Since there are no taints on the controlplane node, all the pods were started on it when we ran the `kubectl drain node01` command.

   ```
   $ kubectl describe node controlplane | grep -i taint
   ```

   `Answer: controlplane node does not have any taints`

10. Time travelling to the next maintenance window…

11. We need to carry out a maintenance activity on `node01` again. Try draining the node again using the same command as before: `kubectl drain node01 --ignore-daemonsets`

    Did that work? `Answer: No`

12. Why did the drain command fail on `node01`? It worked the first time!

    `Answer: there is a pod in node01 which is not part of a replicaset`

13. What is the name of the POD hosted on `node01` that is not part of a replicaset?

    ```
    $ kubectl get pods -o wide
    ```

14. What would happen to `hr-app` if `node01` is drained forcefully?

    Try it and see for yourself.

    **Hint**

    - A forceful drain of the node will delete any pod that is not part of a replicaset.

    `Answer: hr-app will be lost forever`

15. Oops! We did not want to do that! `hr-app` is a critical application that should not be destroyed. We have now reverted back to the previous state and re-deployed `hr-app` as a deployment.

16. `hr-app` is a critical app and we do not want it to be removed and we do not want to schedule any more pods on `node01`.
    Mark `node01` as `unschedulable` so that no new pods are scheduled on this node.

    Make sure that `hr-app` is not affected.

    - Node01 Unschedulable
    - hr-app still running on node01?

    **Hint**

    - Run the command `kubectl cordon node01`

    **Solution**

    - Do not drain `node01`, instead use the `kubectl cordon node01` command. This will ensure that no new pods are scheduled on this node and the existing pods will not be affected by this operation.

    ```
    $ kubectl cordon node01
    ```