# Commands and Arguments 모의고사



1. How many PODs exist on the system?

   in the current(default) namespace

   ```
   $ kubectl get pods -n default
   # or
   $ kubectl get pods
   ```

2. What is the command used to run the pod `ubuntu-sleeper`?

   ```
   $ kubectl describe pod ubuntu-sleeper
   ```

3. Create a pod with the ubuntu image to run a container to sleep for 5000 seconds. Modify the file `ubuntu-sleeper-2.yaml`.

   Note: Only make the necessary changes. Do not modify the name.

   - Pod Name: ubuntu-sleeper-2

   - Command: sleep 5000

   **Solution**

   ```
   $ vim ubuntu-sleeper-2.yaml
   ```

   아래와 같이 수정

   ```yaml
   ---
   apiVersion: v1 
   kind: Pod 
   metadata:
     name: ubuntu-sleeper-2 
   spec:
     containers:
     - name: ubuntu
       image: ubuntu
       command:
         - "sleep"
         - "5000"
   ```

   ```yaml
   #or
       command: [ "sleep", "5000" ]
   ```

   ```
   $ kubectl apply -f ubuntu-sleeper-2.yaml
   ```

4. Create a pod using the file named `ubuntu-sleeper-3.yaml`. There is something wrong with it. Try to fix it!

   Note: Only make the necessary changes. Do not modify the name.

   - Pod Name: ubuntu-sleeper-3
   - Command: sleep 1200

   **Hint**

   Both sleep and 1200 should be defined as a string.

   ```
   $ kubectl apply -f ubuntu-sleeper-3.yaml
   ```

5. Update pod `ubuntu-sleeper-3` to sleep for 2000 seconds.

   Note: Only make the necessary changes. Do not modify the name of the pod. Delete and recreate the pod if necessary.

   - Pod Name: ubuntu-sleeper-3
   - Command: sleep 2000

   ```
   $ vim ubuntu-sleeper-3.yaml
   ```

   ```yaml
       command:
         - "sleep"
         - "2000"
   ```

   위와 같이 수정한 후

   ```
   $ kubectl apply -f ubuntu-sleeper-3.yaml
   # 에러가 있을시 ubuntu-sleeper-3 pod를 삭제하고 재생성하면 에러 해결된다.
   ```

6. Inspect the file `Dockerfile` given at /root/webapp-color. What command is run at container startup?

   ```
   $ cd webapp-color
   $ cat Dockerfile
   ```

   위와 같이 Dockerfile 안에 Entrypoint를 확인한다.

7. Inspect the file `Dockerfile2` given at /root/webapp-color. What command is run at container startup?

   ```
   $ cd webapp-color
   $ cat Dockerfile
   ```

   위와 같이 Dockerfile 안에 Entrypoint를 확인한다.

8. Inspect the two files under directory `webapp-color-2`. What command is run at container startup?

   Assume the image was created from the Dockerfile in this folder

   **Solution**

   Since the entrypoint is overridden in the pod definition, the command that will be run is just `--color green`

   ```
   $ cat webapp-color-pod.yaml
   ```

9. Inspect the two files under directory `webapp-color-3`. What command is run at container startup?

   Assume the image was created from the Dockerfile in this folder

   ```
   $ cat webapp-color-pod-2.yaml
   ```

10. Create a pod with the given specifications. By default it displays a `blue` background. Set the given command line arguments to change it to `green`

    - Pod Name: webapp-green
    - Image: kodekloud/webapp-color
    - Command line arguments: --color=green

    **Solution**

    ```yaml
    ---
    apiVersion: v1 
    kind: Pod 
    metadata:
      name: webapp-green
      labels:
          name: webapp-green 
    spec:
      containers:
      - name: simple-webapp
        image: kodekloud/webapp-color
        args: ["--color", "green"]
    ```

    ```
    $ kubectl apply -f webapp-color-pod-2.yaml
    ```

    