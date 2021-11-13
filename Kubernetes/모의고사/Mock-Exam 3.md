# Mock-Exam 3



1. Create a new service account with the name `pvviewer`. Grant this Service account access to `list` all PersistentVolumes in the cluster by creating an appropriate cluster role called `pvviewer-role` and ClusterRoleBinding called `pvviewer-role-binding`.
   Next, create a pod called `pvviewer` with the image: `redis` and serviceAccount: `pvviewer` in the default namespace.
   - 
     ServiceAccount: pvviewer
   - ClusterRole: pvviewer-role
   - ClusterRoleBinding: pvviewer-role-binding
   - Pod: pvviewer
   - Pod configured to use ServiceAccount pvviewer ?

```
$ kubectl create serviceaccount pvviewer
$ kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
$ kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --
serviceaccount=default:pvviewer
$ kubectl run pvviewer --image=redis --dry-run=client -o yaml > pod.yaml
$ vi pod.yaml

apiVersion: v1
kind: Pod
metadata:
  name: pvviewer
spec:
  containers:
  - image: redis
    name: pvviewer
  serviceAccountName: pvviewer

$ kubectl apply -f pod.yaml
```



2. 



3. 



4. 



5. 



6. 



7. 



8. 



9. 