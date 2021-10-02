# Service 모의고사



1. How many Services exist on the system?

   in the current(default) namespace

   ```
   $ kubectl get services
   ```



2. That is a default service created by Kubernetes at launch

3. What is the type of the default `kubernetes` service?

   ```
   $ kubectl get services
   ```



4. What is the `targetPort` configured on the `kubernetes` service?

   ```
   $ kubectl describe svc kubernetes
   ```

   

5. How many labels are configured on the `kubernetes` service?

   Hint: Run the command `kubectl describe service` and look at Labels.

   ```
   $ kubectl describe svc kubernetes
   ```

   

6. How many Endpoints are attached on the `kubernetes` service?

   Hint: Run the command `kubectl describe service` and look at Endpoints.

   ```
   $ kubectl describe svc kubernetes
   ```

   

7. How many Deployments exist on the system now?

   in the current(default) namespace

   ```
   $ kubectl describe deployment
   ```



8. What is the image used to create the pods in the deployment?

   ```
   $ kubectl describe deployment simple-webapp-deployment | grep -i image
   ```



9. Are you able to accesss the Web App UI?

   Try to access the Web Application UI using the tab simple-webapp-ui above the terminal.

   `Answer: No`



10. Create a new service to access the web application using the service-definition-1.yaml file

    `Name:` webapp-service
    `Type:` NodePort
    `targetPort:` 8080
    `port:` 8080
    `nodePort:` 30080
    `selector:` simple-webapp

    ```
    $ kubectl expose deployment simple-webapp-deployment --name=webapp-service --type=NodePort --target-port=8080 --port=8080 --dry-run=client -o yaml > svc.yaml
    ```

    