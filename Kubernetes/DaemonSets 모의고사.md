# DeamonSets 모의고사



1. How many `DaemonSets` are created in the cluster in all namespaces?

   **Hint**

   - Check all namespaces `kubectl get daemonsets --all-namespaces`

   ```
   $ kubectl get daemonsets --all-namespaces
   ```

   

2. Which namespace are the `DaemonSets` created in?

   ```
   $ kubectl get daemonsets --all-namespaces
   ```

   

3. Which of the below is a `DaemonSet`?

   ```
   $ kubectl get daemonsets --all-namespaces
   ```

   

4. On how many nodes are the pods scheduled by the **DaemonSet** `kube-proxy`

   ```
   $ kubectl describe daemonset kube-proxy --namespace=kube-system
   ```

   

5. What is the image used by the POD deployed by the `kube-flannel-ds` **DaemonSet**?

   ```
   $ kubectl describe daemonset kube-flannel-ds --nsmaspace=kube-system
   ```



6. Deploy a **DaemonSet** for `FluentD` Logging.

   Use the given specifications.

   - Name: elasticsearch
   - Namespace: kube-system
   - Image: k8s.gcr.io/fluentd-elasticsearch:1.20

**Hint**

- An easy way to create a DaemonSet is to first generate a YAML file for a Deployment with the command `kubectl create deployment elasticsearch --image=k8s.gcr.io/fluentd-elasticsearch:1.20 -n kube-system --dry-run=client -o yaml > fluentd.yaml`. Next, remove the **replicas** and **strategy** fields from the YAML file using a text editor. Also, change the **kind** from `Deployment` to `DaemonSet`.

  Finally, create the **Daemonset** by running `kubectl create -f fluentd.yaml`

**Solution**

Create the file fluentd.yaml with the content below:

```yaml
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    app: elasticsearch
  name: elasticsearch
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      containers:
      - image: k8s.gcr.io/fluentd-elasticsearch:1.20
        name: fluentd-elasticsearch
```

Then run kubectl apply -f fluentd.yaml