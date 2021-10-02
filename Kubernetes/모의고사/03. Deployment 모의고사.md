# Deployment 모의고사



1. How many PODs exist on the system?

   In the current(default) namespace.

   ```
   $ kubectl get pods
   ```

   

2. How many ReplicaSets exist on the system?

   In the current(default) namespace.

   ```
   $ kubectl get replicasets
   ```

   

3. How many Deployments exist on the system?

   In the current(default) namespace.

   ```
   $ kubectl get deployments
   ```



4. How many Deployments exist on the system now?

   We just created a Deployment! Check again!

   ```
   $ kubectl get deployments
   ```

   

5. How many ReplicaSets exist on the system now?

   ```
   $ kubectl get replicasets
   ```

   

6. How many PODs exist on the system now?

   ```
   $ kubectl get pods
   ```



7. Out of all the existing PODs, how many are ready?

   ```
   $ kubectl get pods
   # or 
   $ kubectl get deployments
   ```

   

8. What is the image used to create the pods in the new deployment?

   ```
   $ kubectl describe deployments frontend-deployment | grep -i image
   ```



9. Why do you think the deployment is not ready?

   ```
   $ kubectl get pods
   ```

   ```
   $ kubectl describe [pods name]
   ```



10. Create a new Deployment using the `deployment-definition-1.yaml` file located at `/root/`.

    There is an issue with the file, so try to fix it.

    - Name: deployment-1

    ```
    $ vi deployment-definition-1.yaml # --> name Deployment로 수정
    $ kubectl apply -f deployment-definition-1.yaml
    ```



11. Create a new Deployment with the below attributes using your own deployment definition file.

    Name: `httpd-frontend`;
    Replicas: `3`;
    Image: `httpd:2.4-alpine`

    ```
    # 해당 파일에서 수정한 후 아래 명령어 시행
    $ kubectl apply -f deployment-definition-1.yaml
    
    # or
    
    $ kubectl create deployment httpd-frontend --image=httpd:2.4-alpine
    $ kubectl scale deployment --replicas=3 httpd-frontend
    $ kubectl get deployments httpd-frontend
    NAME             READY   UP-TO-DATE   AVAILABLE   AGE
    httpd-frontend   3/3     3            3           92s
    ```

    