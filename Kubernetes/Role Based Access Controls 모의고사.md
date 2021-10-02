# Role Based Access Controls 모의고사



1. Inspect the environment and identify the authorization modes configured on the cluster.

   Check the `kube-apiserver` settings.

   **Hint**

   -  Use the command `kubectl describe pod kube-apiserver-controlplane -n kube-system` and look for `--authorization-mode`.

   ```
   $ kubectl describe pod kube-apiserver-controlplane -n kube-system
   ```

2. How many roles exist in the `default` namespace?

   **Hint**

   - Use the command `kubectl get roles` to list the available `roles` in the `default` namespace.

   ```
   $ kubectl get roles -n default
   ```

   

3. How many roles exist in all namespaces together?

   ```
   $ kubectl get roles --all-namespaces --no-headers | wc -l
   ```

   

4. What are the resources the `kube-proxy` role in the `kube-system` namespace is given access to?

   ```
   $ kubectl describe roles kube-proxy -n kube-system
   ```

   

5. What actions can the `kube-proxy` role perform on `configmaps`?

   ```
   $ kubectl describe roles kube-proxy -n kube-system
   ```



6. Which of the following statements are true?

   `Answer: kube-proxy role can get details of configmap object by the name kube-proxy`

   

7. Which account is the `kube-proxy` role assigned to it?

   ```
   $ kubectl describe rolebinding kube-proxy -n kube-system
   ```



8. A user `dev-user` is created. User's details have been added to the `kubeconfig` file. Inspect the permissions granted to the user. Check if the user can list pods in the `default` namespace.

   Use the `--as dev-user` option with `kubectl` to run commands as the `dev-user`.

   **Hint**

   - Run the command: `kubectl get pods --as dev-user`

   ```
   $ kubectl get pods --as dev-user
   ```

   

9. Create the necessary roles and role bindings required for the `dev-user` to create, list and delete pods in the `default` namespace.

   Use the given spec:

   - Role: developer
   - Role Resources: pods
   - Role Actions: list
   - Role Actions: create
   - RoleBinding: dev-user-binding
   - RoleBinding: Bound to dev-user

   **Hint**

   Use the command `kubectl create` to create a role `developer` and rolebinding `dev-user-binding` in the `default` namespace.

   **Solution**

   To create a Role:`kubectl create role developer --namespace=default --verb=list,create --resource=pods`
   To create a RoleBinding:- `kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user`
   OR

   Solution manifest file to create a role and rolebinding in the `default` namespace:

   ```yaml
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     namespace: default
     name: developer
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["list", "create"]
   
   ---
   kind: RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: dev-user-binding
   subjects:
   - kind: User
     name: dev-user
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: developer
     apiGroup: rbac.authorization.k8s.io
   ```



10. The `dev-user` is trying to get details about the `dark-blue-app` pod in the `blue` namespace. Investigate and fix the issue.

    We have created the required roles and rolebindings, but something seems to be wrong.

    - Issue Fixed

    **Hint**

    - New roles and role bindings are created in the `blue` namespace.
      Check it out the `resourceNames` configured on the role.

    **Solution**

    - Run the command: `kubectl edit role developer -n blue` and correct the `resourceNames` field. You don't have to delete the role.

11. Grant the `dev-user` permissions to create deployments in the `blue` namespace.

    Remember to add both groups `"apps"` and `"extensions"`.

    - Create Deployments

    **Hint**

    - Use the command `kubectl create` to create a role and rolebinding for user `dev-user` to grant permissions to create a deployments in the `blue` namespace.

    **Solution**

    Solution manifest file to create a role and rolebinding in the `blue` namespace:

    ```yaml
    ---
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: blue
      name: deploy-role
    rules:
    - apiGroups: ["apps", "extensions"]
      resources: ["deployments"]
      verbs: ["create"]
    
    ---
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: dev-user-deploy-binding
      namespace: blue
    subjects:
    - kind: User
      name: dev-user
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: deploy-role
      apiGroup: rbac.authorization.k8s.io
    ```

    ```
    $ kubectl create rolebinding dev-user-deploy-binding --namespace=blue -role=deploy-role -user=dev-user
    $ kubectl edit role deploy-role -n blue
    ----> 이후 apiGroups 에 apps, extensions 추가(apps는 이미 있을듯)
    
    $ kubectl create rolebinding dev-user-deploy-binding --namespace=blue --role=deploy-role --user=dev-user
    ```

    