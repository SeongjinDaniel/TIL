# Mock Exam2



1. 

   

2. 



3. 



4. 



5. 



6. 

   `kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development`

   `kubectl create rolebinding developer-role-binding --role=developer --user=john --namespace=development`

   **검증**

   `$ kubectl auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL]`

   - `kubectl auth can-i update pods --as=john`

     위와 같이 하면 pod를 수정할 수 있는지 체크하게 되는데 결과는 no이다. 네임스페이스를 명명하고 다시 실행하면 yes가 나올것이다.

   - `kubectl auth can-i update pods -n development --as=john`

**참조**

- https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#normal-user



7. 

   `kubectl run nginx-resolver --image=nginx --port=80`

   `kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP`



8. Create a static pod on `node01` called `nginx-critical` with image `nginx` and make sure that it is recreated/restarted automatically in case of a failure.

   Use `/etc/kubernetes/manifests` as the Static Pod path for example.