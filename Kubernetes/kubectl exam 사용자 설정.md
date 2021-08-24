# kubectl exam 사용자 설정

`

`.vimrc` 나 `.bashrc` 설정 자유롭게 할 수 있다. 설정은 아래와 같다.

```
# .vimrc
set et
set ts=2			   # Tab 너비(ts - 문서의 '\t' 값을 출력시 몇 개의 스페이스로 보여줄지에 대한 설정 값)
set sw=2
set nu                 # Line number 출력 설정

# .bashrc
alias k='kubectl'
source <(k completion bash) # auto completion enable
complete -F __start_kubectl k # auto completion with command 'k'
```



.vimrc 기능이 설정이 안되면 `sudo apt-get install vim`명령어를 사용하여 vim 에디터를 설치하자! 

`vi ~/.vimrc`를 통해서 .vimrc를 설정한다.



`.vimrc`의 경우 tab을 2 space로 바꾸고 라인표시를 위해서 사용한다. `.bashrc`의 경우 **kubectl 대신 k를 사용하도록** 그리고 [auto completion](https://kubernetes.io/docs/tasks/tools/install-kubectl/#enabling-shell-autocompletion)을 사용하도록 설정한다. 특히 **auto completion은 정말 좋은게 오타 걱정이 없다.** tab을 누르면 자동완성이 된다.

