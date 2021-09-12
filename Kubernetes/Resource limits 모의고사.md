# Resource limits 모의고사



1. A pod called `rabbit` is deployed. Identify the CPU requirements set on the Pod

   in the current(default) namespace

   Hint: Run the command `kubectl describe pod rabbit` and inspect requests.

   ```
   $ kubectl describe pod rabbit # 이 명령어로 확인 가능
   ```



2. Delete the `rabbit` Pod.

   Once deleted, wait for the pod to fully terminate.

   - Delete Pod rabbit

   ```
   $ kubectl delete pod rabbit
   ```



3. Another pod called `elephant` has been deployed in the default namespace. It fails to get to a running state. Inspect this pod and identify the `Reason` why it is not running.

   **Solution**

   The reason for the pod not running is `OOMKilled`. This means that the pod ran out of memory.

   ```
   $ kubectl describe pod elephant  | grep -A5 State: 
       State:          Waiting
         Reason:       CrashLoopBackOff
       Last State:     Terminated
         Reason:       OOMKilled
         Exit Code:    1
         Started:      Sun, 25 Apr 2021 15:13:07 +0000
         Finished:     Sun, 25 Apr 2021 15:13:07 +0000
       Ready:          False
   ```



4. The status `OOMKilled` indicates that it is failing because the pod ran out of memory. Identify the memory limit set on the POD.



5. The `elephant` pod runs a process that consume 15Mi of memory. Increase the limit of the `elephant` pod to 20Mi.

   Delete and recreate the pod if required. Do not modify anything other than the required fields.

   - Pod Name: elephant

   - Image Name: polinux/stress

   - Memory Limit: 20Mi

   **Solution**

   Create the file elephant.yaml by running command `kubectl get po elephant -o yaml > elephant.yaml` and edit the file such as memory limit is set to 20Mi as follows:

   ```yaml
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: elephant
     namespace: default
   spec:
     containers:
     - args:
       - --vm
       - "1"
       - --vm-bytes
       - 15M
       - --vm-hang
       - "1"
       command:
       - stress
       image: polinux/stress
       name: mem-stress
       resources:
         limits:
           memory: 20Mi
         requests:
           memory: 5Mi
   ```

   then run `kubectl replace -f elephant.yaml --force`. This command will delete the existing one first and recreate a new one from the YAML file.



6. Inspect the status of POD. Make sure it's running

   

7. Delete the `elephant` Pod.

   Once deleted, wait for the pod to fully terminate.

   - Delete Pod elephant

   ```
   $ kubectl delete pod elephant
   ```

   