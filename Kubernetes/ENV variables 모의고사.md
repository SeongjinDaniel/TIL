# ENV variables 모의고사



1. How many PODs exist on the system?

   in the current(default) namespace

   ```
   $ kubectl get pods
   ```

2. What is the environment variable name set on the container in the pod?

   ```
   $ kubectl describe pod
   ```

3. What is the value set on the environment variable `APP_COLOR` on the container in the pod?

   ```
   $ kubectl describe pod
   ```

4. View the web application UI by clicking on the `Webapp Color` Tab above your terminal.

   This is located on the right side.

5. Update the environment variable on the POD to display a `green` background

   Note: Delete and recreate the POD. Only make the necessary changes. Do not modify the name of the Pod.

   - Pod Name: webapp-color
   - Label Name: webapp-color
   - Env: APP_COLOR=green

   **Hint**

   - Set the environment option to `APP_COLOR` - `green`.

   **Solution**

   - Replace the env variable value to `green`.

     ```yaml
     ---
     apiVersion: v1
     kind: Pod
     metadata:
       labels:
         name: webapp-color
       name: webapp-color
       namespace: default
     spec:
       containers:
       - env:
         - name: APP_COLOR
           value: green
         image: kodekloud/webapp-color
         name: webapp-color
     ```

   ```
   $ kubectl get pod webapp-color -o yaml > pod.yaml
   # 위의 Solution과 같이 변경
   $ vi pod.yaml
   
   $ kubectl apply -f pod.yaml
   ```

   

6. View the changes to the web application UI by clicking on the `Webapp Color` Tab above your terminal.

   If you already have it open, simply refresh the browser.

7. How many `ConfigMaps` exist in the environment?

   ```
   $ kubectl get configmaps
   ```

8. Identify the database host from the config map `db-config`

   ```
   $ kubectl describe configmap db-config
   ```

9. Create a new ConfigMap for the `webapp-color` POD. Use the spec given below.

   - ConfigName Name: webapp-config-map
   - Data: APP_COLOR=darkblue

   **Solution**

   ```
   $ kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue
   ```

10. Update the environment variable on the POD to use the newly created ConfigMap

    Note: Delete and recreate the POD. Only make the necessary changes. Do not modify the name of the Pod.

    - Pod Name: webapp-color
    - EnvFrom: webapp-config-map

    **Solution**

    ```yaml
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        name: webapp-color
      name: webapp-color
      namespace: default
    spec:
      containers:
      - envFrom:
        - configMapRef:
             name: webapp-config-map
        image: kodekloud/webapp-color
        name: webapp-color
    ```

    

    ```
    $ kubectl delete pod webapp-color
    $ kubectl explain pods --recuresive | grep envFrom -A3
             envFrom        <[]Object>
                configMapRef        <Object>
                   name     <string>
                   optional <boolean>
    --
             envFrom        <[]Object>
                configMapRef        <Object>
                   name     <string>
                   optional <boolean>
    --
             envFrom        <[]Object>
                configMapRef        <Object>
                   name     <string>
                   optional <boolean>
                   
    위와 같이 설명이 나오고 복사해서 사용하면 된다.
    $ kubectl apply -f pod.yaml
    ```

11. View the changes to the web application UI by clicking on the `Webapp Color` Tab above your terminal.

    If you already have it open, simply refresh the browser.

    

