# MAC AWS 인증키 적용 방법



```shell
$ sudo chmod [자신이 ec2에서 다운 받은 key path]
Password: [자신의 맥 비밀번호]

$ ssh -i [자신이 ec2에서 다운 받은 key path] ubuntu@[ec2 public ip]
yes
```

위와 같이 하면 우리가 산 AWS EC2에 접속할 수 있다.
