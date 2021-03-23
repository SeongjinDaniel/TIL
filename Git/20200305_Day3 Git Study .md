# Git Study Day3

## 4. mixed reset, soft reset

reset의 기본 옵션은 mixed reset이다. mixed reset은 작업 폴더를 건드리지 않는다. soft reset은 HEAD와 참조하는 브랜치만 수정한다.

### 조금은 안전한 mixed reset

#### mixed reset

```
$ git log --oneline -n2
378c96e (HEAD -> reset-test) reset 테스트용 커밋
a3c0f7e (origin/master, origin/HEAD, master) master 커밋 2

$ git reset HEAD~ # 1 mixed reset

$ cat reset.txt # 2 파일 상태 확인, 변화가 없다!

$ git status # 3 스테이지 상태 확인, 스테이지에서 해당 파일이 사라졌다.
On branch feature1
Your branch is up to date with 'origin/feature1'.

Untracked files:
	(use "git add <file>..." to include in what will be committed)
		
		reset.txt
nothing added to commit but untracked files present (use "git add" to track)

$ git log --ineline -n1 # 4 커밋 히스토리 확인
a3c0f7e (origin/master, origin/HEAD, master) master 커밋
```

1. **git reset HEAD~** 명령으로 **직전 커밋으로 돌아간다**. --mixed 옵션을 사용하지는 않았지만 기본이 mixed 모드이기 대문에 옵션을 생략하면 mixed reset이 된다.
2. cat reset.txt 명령으로 reset.txt 파일 내용을 봅니다. reset 전과 달라진게 없다. mixed reset은 작업 폴더의 내용은 건드리지 않는다.
3. git status 명령으로 확인해 보면 변경된 파일들이 스테이지에 없기 때문에 untracked 상태가 된다. 
4. 커밋 히스토리는 이전으로 돌아갔다.

실습의 내용을 통해 확인한 것처럼 mixed reset은 작업 폴더의 내용을 변경하지 않기 때문에 hard reset보다 조금 안전하게 사용할 수 있습니다. 그리고 파일명과 함께 mixed reset을 사용해서 특정 파일을 언스테이징할 수 있다는 것도 기억!!!

### HEAD만 옮기는 soft reset

git reset --soft 명령으로 사용하는 soft reset는 워킹트리와 스테이지는 수정하지 않는다. 단지 지정한 커밋 체크섬으로 HEAD와 HEAD가 가리키는 branch를 함께 옮긴다. 그 외에는 달라지는 것이 없다.

soft reset도 직접 명령을 수행해 보고 결과를 확인해 보자.

#### soft reset 실습

```
$ git merge 378c96e # 1 원래 상태로 복귀

$ git log --oneline -n2

378c96e (HEAD -> reset-test) reset 테스트용 커밋

a3c0f7e (origin/master, origin/HEAD, master) master 커밋 2

$ git reset --soft HEAD~ # 2 soft reset

$ git status

Changes to be committed:

	(use "git reset HEAD <file>..." to unstage)

		new file: reset.txt
```

1. 다시 merge와 체크섬을 이용해서 reset 전 단계로 되돌아 갔다.
2. git reset --soft HEAD~ 명령으로 soft reset을 수행한다. 상태를 확인해 보면 mixed reset과는 달리 변경사항이 이미 스테이지에 올라가 있는 것을 알 수 있다.

reset은 신중하게 해야한다!!! 특히 이미 원격저장소에 올라간 커밋들을 reset으로 되돌리고 그 상태에서 다시 커밋을 하게 되면 git push --force 명령으로 강제 푸시가 필요한 경우도 있다. 이런 상태는 피하는 것이 좋으므로 가급적이면 rebase와 마찬가지로 reset 명령도 로컬에만 있는 커밋들에 대해 사용하는 것이 좋다.

## reflog로 사라진 커밋 되살리기

앞 절에서 git log 명령으로는 찾을 수 없는 커밋으로 병합하기 위해서 메모장에 있었던 커밋 체크섬을 사용했다. 그런데 메모장에 적지 않으면 여기 지시대로 해야한다.

### 간단한 reflog 사용법

reflog라는 것은 로컬 저장소의 커밋 또는 브랜치의 변경사항을 기록해 놓은 로그를 말합니다. 그리고 git reflog 명령을 사용하면 reflog를 화면에 보여줍니다.

- reflog를 보여주는 명령 -n 숫자 옵션으로 갯수를 제한해서 볼수 있다.

  ```
  git reflog [-n숫자]
  ```

  한번 커밋은 영원히 남는다. 우리가 찾지 못할 뿐!! 앞 절에서 커밋 체크섬을 메모장에 저장했지만 사실은 그럴 필요도 없습니다. 간단한 실습을 통해서 확인하자!!

  #### reflog를 이용한 복원

  ```
  $ git reflog # 1 reflog 명령 수행
  06be8e8 (HEAD -> master, origin/master) HEAD@{0}: commit: 20200304 git reset-test
  e68131d HEAD@{1}: commit: 20200303 Deep Learning Study
  164a07c HEAD@{2}: pull: Merge made by the 'recursive' strategy.
  4d0503e HEAD@{3}: commit: 20200301 git study
  88d8e0f HEAD@{4}: checkout: moving from reset-test to master
  88d8e0f HEAD@{5}: checkout: moving from master to reset-test
  88d8e0f HEAD@{6}: checkout: moving from master to master
  88d8e0f HEAD@{7}: commit: 20200227 web jQuery study
  6f1a129 HEAD@{8}: commit: 20200226 git and web login study
  dd14526 HEAD@{9}: commit: 20200225 web login
  62cc994 HEAD@{10}: pull: Fast-forward
  271ed9b HEAD@{11}: commit: 20200223 algorithm and web study
  b7d7f75 HEAD@{12}: pull: Fast-forward
  6d58890 HEAD@{13}: pull: Fast-forward
  ... 뒷부분 생략
  
  $ git reset --hard HEAD@{0}
  ```

1. git reflog 명령을 수행하면 지금까지의 모든 로컬저장소의 작업에 대해 커밋 체크섬을 볼 수 있습니다. 우리가 원하는 커밋인 "reset 테스트용 커밋"의 체크섬은 06be8e8이고 옆에는 HEAD@{0}라는 표기도 볼 수 있다. HEAD@{0}은 0번 전 HEAD가 여기 있었다라는 뜻인데 이 표기를 커밋 체크섬 대신으로도 사용할 수 있다.
2. 이 기호를 이용해서 hard reset을 한다. 확인해 보면 정상적으로 초기화된 것을 알 수 있다.

reflog를 사용하면 이렇게 git log 명령으로는 확인할 수 없는 커밋들을 확인 할 수 있다. 단 여기에도 조건이 하나 있는데 reflog의 유효범위는 로컬저장소이다. 원격저장소에서는 해당 내용 존재하지 않는다. reflog 명령도 유용하게 사용될 때가 종종 있는 명령이다.

------------

# 중급 CLI 명령어 2

## 커밋 수정하기

CLI에서도 커밋을 수정할 수 있다. commit --amend를 이용해서 커밋을 수정해 본다. 그리고 커밋을 수정하면 어떤 일이 벌어지는 지도 함께 살펴 본다.

### commit --amend로 커밋 수정

CLI에서는 commit 명령어 뒤에 --amend 옵션을 사용한다. amend는 '개정하다'라는 뜻을 갖고 있다. 말 그대로 이전 커밋을 고친다는 뜻이다. --amend로 커밋을 고치는 경우는 보통 아래와 같은 경우이다.

- HEAD가 가르키는 커밋, 즉 현재 커밋을 수정하고 싶은 경우
- 커밋 메시지를 바꾸고 싶은 경우
- 이전 커밋의 파일 내용을 조금 수정하고 싶은 경우
- 깜박 잊고 이전 커밋에 일부 중요 파일을 추가하지 않은 경우

커밋 메시지에 실수로 오타가 들어가서 이를 수정할 때 많이 사용한다. 주의할 점이 하나 있는데 commit을 수정하면 커밋의 해시 체크섬 값도 바뀌에 된다. 바꾸어 말하자면 커밋을 수정해도 실제로는 새로운 커밋이 하나 생성되어 바뀐다는 것이다. 프로그래밍 언어적인 관점에서 본다면 자바나 JS의 문자열처럼 커밋도 immutable(불변) 속성을 가진다고 볼 수 있다.

### Commit 메시지 수정하기

hello-git-cli 프로젝트에서 Git Bash를 열고 커밋 메시지를 고쳐본다.

```
$ git log -n1 --stat # 1 마지막 로그의 메시지 및 요약 정보 보기
commit a3c0f7~~~~ (HEAD -> master, origin/master, origin/HEAD)
Author : Seongjin Yoo
Date : Thu~~~~~~~
	'전에 사용했던 커밋 메시지 나옴'
	.. 이하 생략
$ git commit --amend -m "수정할 커밋 메시지" # 2 커밋 메시지 수정
[master 520d2fa] '수정할 커밋메시지 나옴'
Author : Seongjin Yoo
Date : Thu~~~~~~~
..이하 생략
$ git log -n1 --oneline --stat # 바뀐 메시지 확인
520d2fa (HEAD -> master) '바뀐 커밋 메시지 나옴'
올라간 파일 나옴 |
..이하 생략
```

1. HEAD 커밋의 정보를 봅니다. --stat 옵션을 주면 간단히 커밋의 요약 정보를 볼 수 있다.
2. commit --amend를 이용해서 커밋 메시지만 수정했다.
3. 바뀐 커밋 메시지를 확인한다.

앞서 말한 것처럼 커밋의 해시 체크섬이 1에서는 a3c0f7이었는데 3에서는 520dfa인 것을 볼 수 있다. 이 상태에서 푸시를 할 수 있을까? 1의 로그를 잘보면[master]와 [origin/master]가 같은 커밋을 가리키고 있다는 것을 알 수 있다. 하지만 3에서 [origin/master]가 사라진 것으로 봐서 [origin/master]는 여전히 1의 커밋을 가리키고 있고 --amend로 새로운 커밋을 생성한 것을 알 수있다.

지금 상태에서 git push 명령을 수행하면 잘 될까? 그렇지 않다. 이 경우 원격저장소인 [origin]과 로컬저장소의 [master] 브랜치의 커밋이 서로 달라졌기 때문에 충돌이 일어난다. 이 경우 강제 푸시를 위해서 git push --force 명령을 사용해야 한다.

일반적으로 git push --force가 일어나는 상황은 좋지 않은 상황이다. git commit --amend는 원격저장소에 이미 해당 커밋이 올라가 있는 경우에는 가급적이면 사용하지 않는 편이 좋다.

------

git push --force는 무조건 쓰지 말아야 할까요?

위험한 명령들(중요 데이터가 사라지거나 커밋 히스토리가 이상하게 꼬이게 만들 수 있다) 가장 대표적인 것은 원격에 푸시된 커밋들의 rebase와 방금 언급한 git push --force이다. 그 외에도 reset --hard와 stash 명령도 조금 위험하다. 그렇지만 이런 명령을 무조건 쓰지 말아야 한다는 것은 아니다. Git 동작 원리를 잘 이해하고 있다면 Git에서 제공하는 모든 명령을 사용해도 괜찮다. 그리고 데이터의 손실을 줄 수 있는 명령들을 수행하기 전에는 반드시 내가 의도한 바대로 수행되는지를 꼼꼼히 점검하고 명령을 실행하는 습관을 들여야한다.



### Commit에 변경 내용 추가하기

이전 커밋에 변경사항을 추가하고 싶을 때가 있다. 변수명 한 글자 바꾸기와 같은 아주 작은 커밋을 해야 하거나 이전 커밋에 작지만 심각한 실수가 있어서 반드시 바꾸고 싶은 경우에 주로 사용한다. 물론 새로운 커밋을 만들어도 되지만 굳이 불필요한 커밋을 남기고 싶지 않다면 그럴 때는 commit --amend를 사용해서 커밋을 수정하는 편이 더 낫다.

커밋에 변경 내용 추가는 매우 쉽다. 그냥 평범한 커밋과 마찬가지로 git add를 이용해 스테이지에 변경사항을 추가한 이후 커밋 명령에 --amend 명령만 붙이면 된다.

```
$ echo "master 2-2" >> master2.txt

$ git add .

$ git commit --amend # 1 마지막 커밋 수정

$ git log -n1 --oneline --stat # 마지막 커밋 정보 보기
```

1. 기존 파일에 텍스트를 한 줄 추가한 후 이를 스테이징해서 커밋 내용을 수정했다. 이번에는 커밋 메시지는 수정하지 않기 때문에 메시지 편집 창이 뜨면 그대로 닫으면 된다. 그다지 어렵지 않게 마지막 커밋을 수정할 수 있지만 역시 사용에는 주의가 필요하다. 

그런데 현재 커밋, 즉 HEAD가 아닌 커밋도 수정하라 수 있을까? Git의 도움말을 살펴 보면 --amend 옵션은 현재 브랜치의 최신 커밋을 수정할 때 사용한다라고 나와 있다. 즉 오래된 커밋을 수정할 수는 없다.

하지만 대부분 그렇듯이 조금 복잡하지만 할 수 있는 방법이 있습니다. 워ㅜㄴ리 자체는 간단한데 수정하고 싶은 커밋의 순서를 바꿔서 가장 마지막 커밋으로 위치를 바꾸고 커밋을 수정합니다. 수정하고 싶은 커밋이 HEAD 커밋이니까 commit -amend로 해당 커밋을 수정할 수 있게 된다. 그리고 나서 다시 원래의 위치로 커밋을 되돌리면 된다. 

git rebase -i 명령을 사용하면 그냥 오래된 커밋을 수정할 수 있다.

--------

추가 설명

#### echo 명령어 

echo 명령어는 새로운 파일과 그 파일의 내용을 생성한다.

```
$ echo 'Project Start' > README
```

위와 같이 사용하면, 위의 명령어는 'README'라는 파일을 생성하며, 그 안의 내용은 'Project Start'라는 내용이 들어간다.

-------

