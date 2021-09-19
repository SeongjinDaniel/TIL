# Logging & Monitoring 모의고사



1. We have deployed a POD hosting an application. Inspect it. Wait for it to start.

2. A user - `USER5` - has expressed concerns accessing the application. Identify the cause of the issue.

   Inspect the logs of the POD

   ```
   $ kubectl get pods
   $ kubectl logs webapp-1 | grep USER5
   ```

   

3. We have deployed a new POD - `webapp-2` - hosting an application. Inspect it. Wait for it to start.

4. A user is reporting issues while trying to purchase an item. Identify the user and the cause of the issue.

   Inspect the logs of the webapp in the POD

   **solution**

   Run: `kubectl logs webapp-2 -c simple-webapp` and identify which user has issues purchasing the item and the reason why

   ```
   # -c를 사용하여 컨테이너를 지정해야 한다. 그러면 여기에서 DB와 simplle-webapp이라는 두 개의 컨테이너가 있음을 알 수 있습니다.
   $ kubctl logs webapp-2 -c
   db        simple-webapp
   ```

   