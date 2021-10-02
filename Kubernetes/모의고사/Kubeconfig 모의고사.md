# Kubeconfig 모의고사



1. Where is the default kubeconfig file located in the current environment?

   Find the current home directory by looking at the HOME environment variable.

   **Hint**

   - Use the command `ls -a` and look for the kube config file under `/root/.kube`.

   `Answer: /root/.kube/config`

2. How many clusters are defined in the default kubeconfig file?

   **Hint**

   - Run the `kubectl config view` command and count the number of clusters.

3. How many Users are defined in the default kubeconfig file?

   **Hint**

   - Run the command: `kubectl config view` and count the number of users.

4. How many contexts are defined in the default kubeconfig file?

   ```
   $ kubectl config view
   ```

5. What is the user configured in the current context?

   ```
   $ kubectl config view
   ```

6. What is the name of the cluster configured in the default kubeconfig file?

   ```
   $ kubectl config view
   ```

7. A new kubeconfig file named `my-kube-config` is created. It is placed in the `/root` directory. How many clusters are defined in that kubeconfig file?

   ```
   $ ls
   $ vi my-kube-config
   ```

8. 

   ```
   $ ls
   $ vi my-kube-config
   ```

9. What user is configured in the `research` context?

   ```
   $ ls
   $ vi my-kube-config
   ```

10. What is the name of the client-certificate file configured for the `aws-user`?

    ```
    $ ls
    $ vi my-kube-config
    ```

11. What is the current context set to in the `my-kube-config` file?

    ```
    $ ls
    $ vi my-kube-config
    ```

12. I would like to use the `dev-user` to access `test-cluster-1`. Set the current context to the right one so I can do that.

    Once the right context is identified, use the `kubectl config use-context` command.

    - Current context set

    **Hint**

    - To use that context, run the command: `kubectl config --kubeconfig=/root/my-kube-config use-context research`
      To know the current context, run the command: `kubectl config --kubeconfig=/root/my-kube-config current-context`

13. We don't want to have to specify the kubeconfig file option on each command. Make the `my-kube-config` file the default kubeconfig.

    - Default kubeconfig file configured

    **Hint**

    - Replace the contents in the `default` kubeconfig file with the content from `my-kube-config` file.

    ```
    
    ```

14. With the current-context set to `research`, we are trying to access the cluster. However something seems to be wrong. Identify and fix the issue.

    Try running the `kubectl get pods` command and look for the error. All users certificates are stored at `/etc/kubernetes/pki/users`.

    - Issue fixed

    **Hint**

    - The path to certificate is incorrect in the kubeconfig file. Correct the certificate name which is available at `/etc/kubernetes/pki/users/`.

    ```
    
    ```

    

    