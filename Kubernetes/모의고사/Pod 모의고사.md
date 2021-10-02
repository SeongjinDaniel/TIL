# Pod 모의고사



문제에 대한 정답을 알기위해  `kubectl` 명령어를 이용한다.

1. **How many PODs exist on the system?**
   **in the current(default) namespace**

   ```
   $ kubectl get pods
   ```

   

2.  **Create a new pod with the NGINX image**

   ```
   $ kubectl run nginx --image=nginx
   pod/nginx created
   ```

   

3. **How many pods are created now?**

   **Note: We have created a few more pods. So please check again.**

   ```
   $ kubectl get pods
   ```

   

4. **What is the image used to create the new pods?**

   **You must look at one of the new pods in detail to figure this out.**

   ```
   $ kubectl get pods
   # 여기서 나온 새로운 pod에서
   $ kubectl describe pod [새로운 pod 이름] | grep -i image
   ```

   

5. **Which nodes are these pods placed on?**

   **You must look at all the pods in detail to figure this out.**

   ```
   $ kubectl get pods -o wide
   ```



6. **How many containers are part of the pod ‘webapp’?**

   **Note: We just created a new POD. Ignore the state of the POD for now.**

   ```
   $ kubectl get pods webapp
   ```



7. **What images are used in the new ‘webapp’ pods?**

   **You must look at all the pods in detail to figure this out**

   ```
   $ kubectl describe pod webapp
   ```



8. **What is the state of the container ‘agentx’ in the pod ‘webapp’?**

   **Wait for it finish the ‘Container Creating’ state**

   ```
   $ kubectl describe pod webapp
   ```



9. **Why do you think the container ‘agentx’ in pod ‘webapp’ is in error?**

   **Try to figure it out from the events section of the pod**

   ```
   $ kubectl describe pod webapp
   ```

   

10. **What does the READY column in the output of the ‘kubectl get pods’ command indicate?**

    ```
    $ kubectl get pods webapp
    ```



11. **Delete the ‘webapp’ Pod.**

    **Once deleted, wait for the pod to fully terminate.**

    ```
    $ kubectl delete pod webapp
    ```

    

12. **Create a new pod with the name ‘redis’ and with the image ‘redis123’**
    **Use a pod-definition YAML file. And yes the image name is wrong!**

    - **Name: redis**
    - **Image Name: redis123**

    ```
    $ kubectl run redis --image=redis123 --dry-run=client -o yaml > pod.yaml
    # 위의 명령어로 아래 yaml 파일을 생성했음을 알 수 있다.
    $ vi pod.yaml
    $ kubectl apply -f pod.yaml
    ```



13. **Now fix the image on the pod to ‘redis’.**

    **Update the pod-definition file and use ‘kubectl apply’ command or use ‘kubectl edit pod redis’ command.**

    ```
    $ kubectl edit pod redis
    # - image: redis123을 redis로 수정한다.
    $ kubectl get pods
    ```

