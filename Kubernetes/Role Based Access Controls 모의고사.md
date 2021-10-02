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



8. 