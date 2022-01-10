# Kubernetes Command 정리



1. nslookup

   ```sh
   $  kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
   ```

   