# Taints and Tolerations 모의고사



1. How many `nodes` exist on the system?

   Including the `controlplane` node.

   ```
   $ kubectl get nodes --no-headers | wc -l
   ```



2. Do any taints exist on `node01` node?

   ```
   $ kubectl describe node node01 | grep -i taints
   ```



3. Create a taint on `node01` with key of `spray`, value of `mortein` and effect of `NoSchedule`

   ```
   $ kubectl taint nodes node01 spray=mortein:NoSchedule
   ```

   

4. Create a new pod with the `NGINX` image and pod name as `mosquito`.

   - Image name: nginx

   `Solution:`

   ```yaml
   Solution manifest file to create a pod called mosquito as follows:
   
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: mosquito
   spec:
     containers:
     - image: nginx
       name: mosquito
   then run kubectl create -f <FILE-NAME>.yaml
   ```


   or

   ```
   $ kubectl run --image=nginx mosquito
   ```



5. What is the state of the POD?

   ```
   $ kubectl get pods
   ```



6. Why do you think the pod is in a pending state?

   ```
   Answer: POD Mosquito cannot tolerate taint Mortein
   ```



7. Create another pod named `bee` with the `NGINX` image, which has a toleration set to the taint `mortein`.

   - Image name: nginx
   - Key: spray
   - Value: mortein
   - Effect: NoSchedule
   - Status: Running

   ```
   $ kubectl run --image=nginx bee --dry-run=client -o yaml > nginx-taint.yaml
   ```

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: bee
   spec:
     containers:
     - image: nginx
       name: bee
     tolerations:
     - key: "spray"
       operator: "Equal"
       value: "mortein"
       effect: NoSchedule
   ```

   ```
   $ kubelctl apply -f nginx-taint.yaml 
   ```

   

8. Notice the `bee` pod was scheduled on node `node01` despite the taint.

   ```
   OK
   ```



9. Do you see any taints on `controlplane` node?

   ```
   $ kubectl describe nodes controlplane | grep -i taint
   ```



10. Remove the taint on `controlplane`, which currently has the taint effect of `NoSchedule`.

    - Node name: controlplane

    `Hint:`

    `Run the command: kubectl taint nodes controlplane node-role.kubernetes.io/master:NoSchedule- to untaint the node.`

    ```
    $ kubectl taint nodes controlplane node-role.kubernetes.io/master:NoSchedule-
    ```

    

11. What is the state of the pod `mosquito` now?

    ```
    $ kubectl get pods
    ```



12. Which node is the POD `mosquito` on now?

    ```
    $ kubectl get pods -o wide
    ```

    