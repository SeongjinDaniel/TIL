# Namespace 모의고사



1. How many Namespaces exist on the system?

   ```
   $ kubectl get namespaces
   # or
   $ kubectl get namespaces
   # or 
   $ kubectl get ns --no-headers | wc -l
   10
   ```



2. How many pods exist in the `research` namespace?

   ```
   $ kubectl get pods --namespace=research
   # or
   $ kubectl -n research get pods --no-headers
   ```

   

3. Create a POD in the `finance` namespace.

   Use the spec given below.

   - Name: redis
   - Image Name: redis

   Hint: Use the `-n <namespace>` flag with the `kubectl run` command

   ```
   $ kubectl run redis --image=redis --dry-run=client -o yaml > pod.yaml
   $ vi pod.yaml
   # 위 파일에서 metadata 아래에 namespace: finance를 추가
   $ kubectl apply -f pod.yaml
   $ kubectl -n finance get pod redis
   ```

   

4. Which namespace has the `blue` pod in it?

   ```
   kubectl get pods --all-namespaces
   # or 
   kubectl get pods --all-namespaces | grep blue
   ```



5. Access the Blue web application using the link above your terminal

   From the UI you can ping other services

6. What DNS name should the Blue application use to access the database `db-service` in its own namespace - `marketing`.

   You can try it in the web application UI. Use port `6379`.

   ```
   Host Name
   db-service
   Host Port
   6379
   ```

   



7. What DNS name should the Blue application use to access the database 'db-service' in the 'dev' namespace

   You can try it in the web application UI. Use port 6379.

   ```
   $ kubectl -n dev get svc
   
   Host Name
   db-service.dev.svc.cluster.local
   Host Port
   6379
   ```