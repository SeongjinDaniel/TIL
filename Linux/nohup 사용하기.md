# nohup 사용하기



#### nohup 시작 명령어

`nohup python app.py &`



#### nohup 강제 종료하기 명령어

`ps -ef | grep 'python app.py' | awk '{print $2}' | xargs kill`



#### 강제 종료 확인하기 명령어

`ps -ef | grep 'app.py'`
