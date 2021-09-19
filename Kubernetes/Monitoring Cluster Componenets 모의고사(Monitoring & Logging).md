# Monitoring Cluster Componenets 모의고사(Monitoring & Logging)



1. We have deployed a few PODs running workloads. Inspect them.

   Wait for the pods to be ready before proceeding to the next question.



2. Let us deploy metrics-server to monitor the PODs and Nodes. Pull the git repository for the deployment files.
   Run: `git clone https://github.com/kodekloudhub/kubernetes-metrics-server.git`



3. Deploy the metrics-server by creating all the components downloaded.

   Run the `kubectl create -f .` command from within the downloaded repository.

   - Metrics server deployed?

   ```
   root@controlplane:~# pwd
   /root
   
   root@controlplane:~# cd kubernetes-metrics-server/
   
   root@controlplane:~/kubernetes-metrics-server# kubectl create -f .
   clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
   clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
   rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
   apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created
   serviceaccount/metrics-server created
   deployment.apps/metrics-server created
   service/metrics-server created
   clusterrole.rbac.authorization.k8s.io/system:metrics-server created
   clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
   ```



4. It takes a few minutes for the metrics server to start gathering data.

   Run the `kubectl top node` command and wait for a valid output.

   `kubectl top node` 명령어를 사용하면, 노드의 사용현황을 볼 수 있습니다.



5. Identify the node that consumes the `most` CPU.

   ```
   $ kubectl top node
   ```



6. Identify the node that consumes the `most` Memory.

   ```
   $ kubectl top node
   ```



7. Identify the POD that consumes the `most` Memory.

   ```
   $ kubectl top pod
   ```

   

8. Identify the POD that consumes the `least` CPU.

   ```
   $ kubectl top pod
   ```

   

