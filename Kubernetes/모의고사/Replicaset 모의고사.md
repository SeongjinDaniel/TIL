# Replicaset 모의고사



1. **How many PODs exist on the system?**

   **In the current(default) namespace.**

   ```
   $ kubectl get pods
   ```

   

2. **How many ReplicaSets exist on the system?**

   **In the current(default) namespace.**

   ```
   $ kubectl get replicasets.apps
   ```

   

3. **How about now? How many ReplicaSets do you see**

   **We just made a few changes!**

   ```
   $ kubectl get replicasets.apps
   ```



4. **How many PODs are DESIRED in the `new-replica-set`?**

   ```
   $ kubectl get replicasets.apps
   ```



5. **What is the image used to create the pods in the `new-replica-set`?**

   ```
   $ kubectl get replicasets.apps
   $ kubectl describe replicaset.apps new-replica-set
   
   or
   $ kubectl describe replicaset
   ```



6. **How many PODs are READY in the `new-replica-set`?**

   ```
   $ kubectl get replicasets.apps
   $ kubectl describe replicaset.apps new-replica-set
   ```

   

7. **Why do you think the PODs are not ready?**

   ```
   $ kubectl get pods
   new-replica-set-745zc   0/1     ImagePullBackOff   0          45m
   new-replica-set-qrnrk   0/1     ImagePullBackOff   0          45m
   new-replica-set-r7nhj   0/1     ImagePullBackOff   0          45m
   new-replica-set-zzxpk   0/1     ImagePullBackOff   0          45m
   $ kubectl describe pods new-replica-set-745zc
   ```

   Events Section

   ```
   Warning  Failed     43m (x4 over 45m)      kubelet            Failed to pull image "busybox777": rpc error: code = Unknown desc = Error response from daemon: pull access denied for busybox777, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
   ```

   

8. **Delete any one of the 4 PODs.**

   ```
   $ kubectl delete pod new-replica-set-745zc
   ```



9. **How many PODs exist now?**

   ```
   $ kubectl get pods
   ```



10. **Why are there still 4 PODs, even after you deleted one?**

    ```
    ReplicaSet ensures that desired number of PODs always run
    ```



11. **Create a ReplicaSet using the `replicaset-definition-1.yaml` file located at `/root/`.**

    **There is an issue with the file, so try to fix it.**

    apiVersion을 apps/v1으로 변경 하여 재설정

    ```
    $ kubectl apply -f replicaset-definition-1.yaml
    ```



12. **Fix the issue in the `replicaset-definition-2.yaml` file and create a `ReplicaSet` using it.**

    **This file is located at `/root/`.**

    matchLabels와 labels의 tier를 같게 변경하여 재설정

    ```
    $ kubectl apply -f replicaset-definition-2.yaml
    ```

    

13. **Delete the two newly created ReplicaSets - `replicaset-1` and `replicaset-2`**

    ```
    $ kubectl get replicasets.apps
    
    $ kubectl delete replicaset.apps replicaset-1
    $ kubectl delete replicaset.apps replicaset-2
    
    $ kubectl get replicasets.apps
    ```



14. **Fix the original replica set `new-replica-set` to use the correct `busybox` image.**

    **Either delete and recreate the ReplicaSet or Update the existing ReplicaSet and then delete all PODs, so new ones with the correct image will be created.**

    

    ```
    $ kubectl get replicasets.apps
    NAME              DESIRED   CURRENT   READY   AGE
    new-replica-set   4         4         0       24m
    $ kubectl edit replicasets.apps new-replica-set
    # image 이름을 busybox로 변경
    
    $ kubectl get pods
    NAME                    READY   STATUS             RESTARTS   AGE
    new-replica-set-pwl5t   0/1     ImagePullBackOff   0          26m
    new-replica-set-rgnxv   0/1     ImagePullBackOff   0          23m
    new-replica-set-rqsj4   0/1     ImagePullBackOff   0          26m
    new-replica-set-t28x9   0/1     ImagePullBackOff   0          26m
    
    # pod를 모두 삭제
    $ kubectl delete pod new-replica-set-pwl5t
    $ kubectl delete pod new-replica-set-rgnxv
    $ kubectl delete pod new-replica-set-rqsj4
    $ kubectl delete pod new-replica-set-t28x9
    
    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    new-replica-set-8kg2s   1/1     Running   0          4m10s
    new-replica-set-hdt5f   1/1     Running   0          68s
    new-replica-set-qb4xx   1/1     Running   0          3m46s
    new-replica-set-v4nfc   1/1     Running   0          2m46s
    ```

    

15. **Scale the ReplicaSet to 5 PODs.**

    **Use `kubectl scale` command or edit the replicaset using `kubectl edit replicaset`.**

    Hint: Make use of `kubectl edit replicaset new-replica-set` or the `kubectl scale replicaset` command.

    ```
    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    new-replica-set-8kg2s   1/1     Running   0          4m10s
    new-replica-set-hdt5f   1/1     Running   0          68s
    new-replica-set-qb4xx   1/1     Running   0          3m46s
    new-replica-set-v4nfc   1/1     Running   0          2m46s
    
    $ kubectl scale replicaset --replicas=5 new-replica-set
    
    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    new-replica-set-68wrc   1/1     Running   0          12s
    new-replica-set-8kg2s   1/1     Running   0          10m
    new-replica-set-hdt5f   1/1     Running   0          7m20s
    new-replica-set-qb4xx   1/1     Running   0          9m58s
    new-replica-set-v4nfc   1/1     Running   0          8m58s
    ```

    복제본 세트의 이름을 설정하고 복제본은 5와 같다.



16. **Now scale the ReplicaSet down to 2 PODs.**

    **Use the `kubectl scale` command or edit the replicaset using `kubectl edit replicaset`.**

    Hint: Make use of `kubectl edit replicaset new-replica-set` or the `kubectl scale replicaset` command.

    ```
    $ kubectl scale replicaset --replicas=2 new-replica-set
    
    $ kubectl get pods
    NAME                    READY   STATUS        RESTARTS   AGE
    new-replica-set-68wrc   1/1     Terminating   0          3m21s
    new-replica-set-8kg2s   1/1     Running       0          13m
    new-replica-set-hdt5f   1/1     Terminating   0          10m
    new-replica-set-qb4xx   1/1     Running       0          13m
    new-replica-set-v4nfc   1/1     Terminating   0          12m
    
    # Terminating 이 끝나면 
    $ kbuctl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    new-replica-set-8kg2s   1/1     Running   0          14m
    new-replica-set-qb4xx   1/1     Running   0          14m
    ```

    