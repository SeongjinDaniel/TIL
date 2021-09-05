# LABELS AND SELECTORS 모의고사



1. We have deployed a number of PODs. They are labelled with `tier`, `env` and `bu`. How many PODs exist in the `dev` environment?

   Use selectors to filter the output

   ```
   $ kubectl get pods --show-labels
   $ kubectl get pods -l env=dev --no-headres | wc -l
   
   #or 
   
   $ kubectl get pods --selector env=dev --no-headers | wc -l
   ```



2. How many PODs are in the `finance` business unit (`bu`)?

   ```
   $ kubectl get pods -l bu=finance --no-headers | wc -l
   
   #or 
   
   $ kubectl get pods --selector bu=finance --no-headers | wc -l
   ```



3. How many objects are in the `prod` environment including PODs, ReplicaSets and any other objects?

   ```
   $ kubectl get all -l env=prod --no-headers | wc -l
   
   #or 
   
   $ kubectl get all --selector env=prod --no-headers | wc -l
   ```

   

4. Identify the POD which is part of the `prod` environment, the `finance` BU and of `frontend` tier?

   ```
   $ kubectl get all -l env=prod,bu=finance,tier=frontend
   
   #or 
   
   $ kubectl get all --selector env=prod,bu=finance,tier=frontend
   ```



5. A ReplicaSet definition file is given `replicaset-definition-1.yaml`. Try to create the replicaset. There is an issue with the file. Try to fix it.

   - ReplicaSet: replicaset-1
   - Replicas: 2

   `Solution`

   ```yaml
   Update the /root/replicaset-definition-1.yaml file as follows:
   
   ---
   apiVersion: apps/v1
   kind: ReplicaSet
   metadata:
      name: replicaset-1
   spec:
      replicas: 2
      selector:
         matchLabels:
           tier: frontend
      template:
        metadata:
          labels:
           tier: frontend
        spec:
          containers:
          - name: nginx
            image: nginx 
   Then run kubectl apply -f replicaset-definition-1.yaml
   ```

   

   