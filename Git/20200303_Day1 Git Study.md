# Git Study Day1

- 워킹트리에 등록되어 있는 원격저장소 목록을 보여 줍니다.

  ```
  git remote -v
  ```

- 새로운 원격저장소를 지정한 이름으로 등록합니다. 최초의 원격저장소는 관례상 origin으로 정합니다.

  ```
  git remote add <저장소이름> <url>
  ```

- 원격저장소의 이름을 새로운 이름으로 변경합니다.

  ```
  git remote rename <이전이름> <새이름>
  ```

- 지정한 원격저장소를 삭제합니다.

  ```
  git remote remove <저장소이름>
  ```



실습을 위해서 저장소를 포크 !!(by Hanbit)

웹 브라우저를 열고 https://github.com/Cat-Hanbit/remote-test로 접속한다.(GitHub에 로그인합니다.) GitGub 오른쪽 위에 fork를 클릭해서 내 계정으로 포크해 온다.  이제 이 사본 저장소를 CLI를 이용해서 클론해 오고 우너본 저장소를 추가 저장소로 등록해 보도록 한다.

#### 새 프로젝트 클론 및 두번째 원격저장소 등록

```
$ cd ~/Documents/ 	# 1. 프로젝트 상위 폴더로 이동
$ git clone https://github.com/Oct-Hanbit/remote-test	# 2. 내 프로젝트 클론
$ cd remote-test/

$ git remote -v # 원격저장소 정보 확인
origin https://github.com/SeongjinOliver/remote-test (fetch)
origin https://github.com/SeongjinOliver/remote-test (push)

$ git remote add upstream origin https://github.com/cat-hanbit/remote-test 	# 3. 원격저장소 추가 등록

$ git remote -v # 4. 추가 목록 확인
origin  https://github.com/SeongjinOliver/remote-test (fetch)
origin  https://github.com/SeongjinOliver/remote-test (push)
upstream        https://github.com/cat-hanbit/remote-test (fetch)
upstream        https://github.com/cat-hanbit/remote-test (push)

```

1. 프로젝트를 만들기 위해서 상위 폴더로 이동.
2. 포크하 프로젝트를 클론합니다. 여러분은 문어 계정 대신에 여러분의 아이디를 사용해야 하는 점에 주의.
3. 두번째 우너격저장소를 upstream이란 이름으로 등록한니다. 관례상 origin을 내 저장소 혹은 첫번째 원격저장소의 이름으로 사용하는 것처럼 포크해온 저장소는 upstream이란 이름을 많이 사용한다. 참고로 upstream은 '물의 상류'라는 뜻을 가지고 있다. 적절한 이름이라는 생각이 든다.
4. 등록된 원격저장소를 확인하면 [origin]과 [upstream] 두저장소가 등록되어 있는 것을 알 수 있다.

### CLI를 이용한 upstream fet 및  push

앞에서 생성한 [origin]저장소는 내 계정의 저장소이므로 pull / push 모두 가능하지만 [upstream]는 pull (또는 fetch)만 가능하므로, upstream에 내가 변경한 내용을 반영하고 싶다면 GitHub의 pull request 기능을 이용해야 한다. 이렇게 저장소를 구성하게 되면 먼저 [upstream]의 최신 버전을 가져오고 로컬에서 개발 후 [origin]에 푸시한다. 그리고 나서 pull request 및 코드 리뷰 과정을 거쳐 [upstream]에 개발 내용을 반영하게 된다.

#### upstream에서 특정 브랜치만 가져오고 추가 커밋해보기

```
$ git fetch upstream master # 1 upstream의 master 브랜치의 내용만 가져옴
$ git log --oneline --graph -- decorate --all -n1 # log 확인
* a3c0f7e (HEAD -> master, upstream/master, origin/master, origin/HEAD) master 커밋 2
$ echo "master3" > master3.txt # 3 master 브랜치에 추가 커밋 생성
$ git add .
$ git commit
[master 570e2eb] master 브랜치 커밋 3
$ git push # 4 origin에 push
$ git log --oneline --all -n2 # 5 로그 확인
a3c0f7e (HEAD -> master, upstream/master, origin/master, origin/HEAD) master 커밋 2

$ git push upstream master # 6 upstream에 push 시도
remote: Permission to cat-hanbit/remote-test.git denied to SeongjinOliver.
fatal: unable to access 'https://github.com/cat-hanbit/remote-test/': The requested URL returned error: 403
```

원격저장소를 추가 등록해서 기본 저장소인 [origin] 외에 추가 저장소가 생긴 경우에는 push, pull, fetch와 같은 저장소를 동기화하는 명령에 저장소 이름을 옵션으로 사용할 수 있다. 만약 저장소 이름을 생략할 경우에는 기본적으로 origin을 사용한 것으로 간주한다.

\- **git add** : 해당 파일을 추적(stage)시키는 명령어입니다. 추적되고 있는 파일만 커밋에 포함됩니다. 주로 git add . 의 형태로 사용합니다. git add . 명령어는 변경이 일어난 모든 파일을 추적하게 합니다.

\- **git remote** : 원격과 로컬 저장소를 연결시키는 명령어입니다.

1. git fetch upstream master 명령으로 [upstream] 저장소의 [master] 브랜치의 내용만 가져왔다. 전체 브랜치를 가져올 경우 저장소가 복잡해지기 때문에 [master] 브랜치를 선택해서 가져왔다. 또한 pull을 사용하지 않았기 때문에 병합은 수행하지 않습니다.
2. 로그를 확인하면 [upstream/master]가 생긴 것을 알 수 있습니다.
3. [master] 브랜치에 새로운 커밋을 생성합니다.
4. [origin]에 푸시합니다. git push에서 옵션을 생략했기 때문에 자동으로 [origin]의 [master]로 푸시를 수행합니다.
5. 다시 로그를 확인했는데 [origin/master]와 [upstream/master]가 달라진 것을 확인할 수 있다.

6. [upstream]에 푸시해 보지만 권한이 없는 저장소이기 때문에 푸시는 실패합니다.  앞서 말한 것 처럼 [upstream]에 변경사항을 적용하기 위해서는 GitHub의 pull request 기능을 이용해야 한다.

![image-20200226170630682](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200226170630682.png)

## fetch, pull, push 명령어의 옵션들

fetch, pull, push는 보통 옵션을 생략하고 사용하는 경우가 많은데 이 경우 동작 방식이 각각 다르다.

- 원격저장소의 커밋과 브랜치, 태그들을 로컬 저장소로 가져온다. 워킹 트리의 내용은 변하지 않는다. 저장소의 이름을 생략할 경우에는 origin에서 가져온다.

  ```
  git fetch [원격저장소이름] [브랜치이름]
  ```

- fetch를 수행한 이후에 merge도 함께 수행합니다. 워킹트리의 내용은 해당 브랜치의 최신 내용으로 갱신됩니다.

  ```
  git pull [원격저장소이름] [브랜치이름]
  ```

- 해당 브랜치의 커밋들을 원격저장소로 업로드합니다.

  ```
  git push [-u 원격저장소이름 브랜치 이름]
  ```

- 로컬저장소의 모든 브랜치의 커밋들을 한꺼번에 원격저장소로 업로드합니다.

  ```
  git push [원격저장소이름] --all
  ```

- 로컬저장소의 모든 태그들을 원격저장소로 업로드합니다.

  ```
  git push [원격저장소이름] --tags
  ```

\- **git checkout** : 커밋을 불러오는 명령어입니다. git checkout (커밋 해시) 형식으로 사용합니다. 커밋 해시는 전부 적을 필요는 없고 다른 커밋 해시와 중복되지 않아 고유하다면 앞의 몇 자리만 기입해도 인식됩니다. (팁: 가장 최근의 커밋을 기준으로 하여 작업공간에서 발생한 변경사항을 모두 버리고 원래 상태로 돌아가는 명령어는 git checkout -- . 입니다.)

## CLI를 이용해서 원격저장소 수동 백업하기

먼저 GitHub에 비어 있는 새 저장소를 만들어 보도록 합시다. ex) remote-backup이라는 프로젝트를 만든다.(비어 있는 프로젝트 생성)

생성한 프ㅗ젝트를 backup이라는 이름의 언격저장소로 등록하고 현재 [origin] 저장소의 브랜치와 태그들을 업로드 한다.

#### 저장소 백업하기

```
$ git remote add backup https://github.com/SeongjinOliver/remote-backup # 1 새로운 원격저장소 등록
$ git checkout master
$ git push backup --all # 2 master 브랜치만 push
$ git checkout feature1 # 3 로컬 브랜치 생성
$ git push backup --all # 4 feature1 브랜치도 push

$ git push backup --tags # 5 tag push

$ git branch -rv # 6 저장소 상태 확인
  backup/feature1 4d1fef4 기능 1 개선
  backup/master   a3c0f7e master 커밋 2
  origin/HEAD     -> origin/master
  origin/feature1 4d1fef4 기능 1 개선
  origin/feature2 ab212a1 기능 2-2 추가
  origin/hotfix   e07e822 hotfix 실습
  origin/master   a3c0f7e master 커밋 2
  upstream/master a3c0f7e master 커밋 2
```

1. 앞서 만든 저장소의 주소를 backup이라는 이름으로 등록한다.
2. --all 옵션을 사용해서 로컬 브랜치 전부를 [backup] 저장소에 푸시합니다. GitHub 페이지를 보면 원래의 [master] 브랜치의 커밋들이 [backup] 저장소에 업로드 된 것을 확인할 수 있습니다. 그런데 [master] 브랜치를 제외한 다른 브랜치는 [backup] 저장소에 없습니다. 아쉽게도 이런 방식으로 저장소를 백업하기 위해서는 로컬 브랜치가 생성된 상태여야한다.
3. [feature1] 브랜치를 체크아웃한다.
4. 다시 푸시를 시도하면 이번에는 [featyre1] 브랜치도 [backup] 저장소에 푸시된다.
5. 태그들도 푸시한다.
6. 마지막으로 git branch -rv 명령을 통해 각 저장소의 상태를 확인. 로컬에 없는 [hotfix] 브랜치는 [backup] 저장소에는 없는 것도 알 수 있다.

여기까지 한 후에 GitHub의 프로젝트 페이지를 새로고침하면 두 개의 브랜치와 한 개의 태그가 정상적으로 업로드된 것을 확인 할 수 있다.

한번에 [origin]의 모든 브랜치들을 다 푸시하면 좋을텐데, 그런 기능은 아직 없다. 물론 스크립트 등을 이용해서 짤 수도 있긴한데 조금 아쉬운 부분이다.

[origin] 저장소의 내용을 [backup] 저장소에 업로드한 것처럼 반대로 [backup] 저장소의 내용도 [origin]으로 업로드할 수 있다. 

----------

참고 사이트 : http://minsone.github.io/git/git-addtion-and-modified-delete-tag

#### git tag 설명글

저장소의 소스 버전을 간간히 표시하기 위해서는 커밋 메시지 또는 브랜치로 해서 표시하는 것 보단 태그로 깔끔하게 하는 것이 좋습니다.

#### 태그 조회하기

태그를 전체를 조회할 때는 `git tag`를 사용하여 조회합니다.

```
# git tag
v1.0.0
v1.0.1
v1.1.0
```

만약 원하는 태그명을 조건으로 검색하고자 한다면 `git tag -l v1.1.*`과 같이 사용합니다.

```
# git tag -l v1.1.*
v1.1.0
```

#### 태그 붙이기

태그는 Lightweight와 Annotated 두 종류가 있습니다. Lightweight 태그는 특정 커밋을 가르키는 역할만 합니다. 한편 Annotated 태그는 태그를 만든 사람, 이메일, 날짜, 메시지를 저장합니다. 그리고 [GPG(GNU Privacy Guard)](http://ko.wikipedia.org/wiki/GNU_프라이버시_가드)로 서명할 수도 있습니다.

Lightweight 태그는 `git tag [Tag Name]`으로 붙일 수 있습니다.

```
# git tag v1.0.2
# git tag
v1.0.2
```

Annotated 태그는 `-a` 옵션을 사용합니다.

```
# git tag -a v1.0.3 -m"Release version 1.0.3"
```

`git show v1.0.3`을 통해 태그 메시지와 커밋을 확인할 수 있습니다.

```
# git show v1.0.3

tag v1.0.3
Tagger: minsOne <cancoffee7+github@gmail.com>
Date:   Sat Feb 15 17:53:49 2014 +0900

Release version 1.0.3

commit 4bb37290cb55490a9829b4ff015b340d513f132a
Merge: e0d819c 12aa1b0
Author: Markus Olsson <j.markus.olsson@gmail.com>
Date:   Thu Feb 13 15:26:47 2014 +0100

    Merge pull request #947 from IonicaBizau/patch-1
    
    Updated the year :-)
```

***태그를 이전 커밋에 붙여야 한다면 커밋 해쉬를 추가하여 사용할수 있습니다. ?????***

```
# git tag v1.0.5 03c0beb080

# git tag -a v1.0.4 -m"Release version 1.0.4" 432f6ed

# git tag
v1.0.4
v1.0.5

# git show v1.0.4

tag v1.0.4
Tagger: minsOne <cancoffee7+github@gmail.com>
Date:   Sat Feb 15 18:02:02 2014 +0900

Release version 1.0.4

commit 432f6edf3876a5e2aa8ea545fd15f99953339aba
Author: Denis Grinyuk <denis.grinyuk@gmail.com>
Date:   Mon Feb 3 14:52:36 2014 +0400

    Additional comments
```

***만약 GPG 서명이 있다면 `-s` 옵션을 사용하여 태그에 서명할 수 있습니다. ??????***

```
# git tag -s v1.0.3 -m"Release version 1.0.3"
```

#### 태그 원격 저장소에 올리기

태그를 만들고 원격 저장소에 올려야할 필요가 있다면 브랜치를 올리는 방법과 같이 사용할 수 있습니다.

```
# git push origin v1.0.3
```

모든 태그를 올리려면 `--tags`를 사용합니다.

```
# git push origin --tags
```

#### 태그 삭제하기

필요없거나 잘못 만든 태그를 삭제하기 위해선 `-d`옵션을 사용하여 삭제할 수 있습니다.

```
# git tag -d v1.0.0
```

원격 저장소에 올라간 태그를 삭제하기 위해선 `:`를 사용하여 삭제할 수 있습니다.

```
# git push origin :v1.0.0
```

***태그 이름을 지정하여 checkout 하거나 reset(아직 안 배웠어요!) 함으로써, 간단하게 과거의 특정 상태로 되돌릴 수 있답니다! ????????????????????????***

--------

#### Reset과 Revert

작업을 진행하다가 실수로 중요한 파일을 삭제했거나 제대로 병합이 안됐을 경우, 잘 작동이 되던 이전 버전으로 돌아가야 합니다.

이것이 바로 버전 관리를 하는 이유이며, 이 때 사용하는 명령어가 git reset과 git revert라는 명령어입니다.

git reset을 명령어는 특정 커밋으로 되돌아갈 수 있는데, 되돌린 버전 이후의 버전들은 **히스토리에서 삭제**됩니다.

git revert는 reset처럼 특정 버전으로 되돌아갈 수 있지만, 되돌린 버전 이후의 버전들의 **이력은 남아있다**는 점에서 차이가 있습니다.

reset과 revert 명령어를 통해 과거 버전으로 돌아갈 수 있지만 그 밖에 잘못된 병합을 취소할수도 있는 기능이 있습니다.

이 글에서 이전 버전으로 되돌리기, 병합 취소 등의 기능에 대해 알아보도록 하겠습니다.

**2. 명령어**

- **git checkout** 

- - .

  - - working directory에서 수정한 모든 파일(git add이전)을 현재 버전으로 되돌리기

  - -- {file}

  - - working directory에서 수정한 특정 파일(git add이전)을 현재 버전으로 되돌리기

- **git reset**

- - .

  - - 현재 버전으로 되돌리기 ( add 무효화하기 )

  - {commit번호}

  - - 특정 버전으로 되돌리지만, 커밋 이력 삭제
    - 파일 내용은 유지

  - --hard {commit번호}

  - - 파일 내용까지 되돌림

- - --soft {commit번호}

  - - 파일 내용은 그대로 유지하면서 staging area에 올림 ( add 상태 )

  - -merge ORIG_HEAD

  - - 바로 이전 병합 취소

- **git revert**

- - {commit번호}

  - - 특정 버전으로 되돌리는데, 파일 내용은 그대로 유지하고 되돌린 버전 이후의 모든 commit 이력은 그대로 보존

  - --mainline 숫자

  - - 과거 병합을 취소
    - 숫자로 명시된 브랜치 라인을 기준으로 되돌아간다.

**3. 되돌리기 - working directory 내용 비우기**

아직 add 명령어를 하지 않은 상태에서 작업했던 내용을 모두 되돌리고 싶은 경우입니다.

즉, HEAD가 가장 최근에 커밋된 버전으로 이동하는 것이죠.

이 때 사용하는 명령어는 reset, revert도 아니지만 되돌리기와 관련된 기능이므로 언급하도록 하겠습니다.

실습 진행을 위해 텍스트 파일을 생성하여 내용을 작성하고, 커밋을 해줍니다.

```
# git add
# git commit -m "메시지"
```

다음으로 파일을 아무렇게나 수정합니다.

이 때 git add 명령어를 실행하면 안됩니다. ( add를 안했을 때 되돌리는 명령어니까요. )



그리고 상태를 확인해보도록 할게요.

```
# git status
```

![img](https://t1.daumcdn.net/cfile/tistory/99FB98335A28145026)





당연히 commit을 한 후에, 파일을 수정 했으니 add할 것이 있다고 하겠죠?



이 상황에서 방금 수정한 파일을 수정한 적이 없던 것처럼 하려면 status에서 보는 것처럼 다음 명령을 실행하면 됩니다.

```
# git checkcout -- { file }
```



**모든 파일**을 working directory에서 되돌리고 싶다면, git checkcout . 명령어를 실행하면 되고,

폴더를 되돌리고 싶다면 git checkcout { 폴더명 } 명령어를 실행하면 됩니다. 

```
# git checkcout .
# git checkcout { 폴더명 } 
```



정말로 되돌아 갔는지 확인을 위해 상태를 보겠습니다.

이번에는 수정할 것이 없다고 합니다.

![img](https://t1.daumcdn.net/cfile/tistory/996D49335A28146718)

**4.** **reset으로** **되돌리기 -** **add를 무효화**

이번에는 git add를 한 상태에서, 변경된 staging area를 무효화해서 가장 최근 버전으로 되돌아가는 방법에 대해 알아보겠습니다.

이전 예제처럼 working directory에서 txt 파일을 아무렇게나 수정하고, 차례대로 아래의 명령어를 실행해보겠습니다.

```
# git status
# git add .
# git status
# git reset {파일명}
# git status
```

![img](https://t1.daumcdn.net/cfile/tistory/99C981335A1DD70935)
파일을 수정한 후, 상태를 보면 변경 내역이 있다고 합니다.

그리고 git add 명령어를 실행하면 newFile.txt 파일은 staging area에 올라간 상태가 됩니다.

이 때, add된 것을 무효화 하려면 reset 명령어를 실행합니다.

git reset { 파일명 } 명령어를 실행하면 working directory 상태로 돌아가게 됩니다.

즉, **수정된 내용은 유지한 채로 add 이전 상태로 되돌린 것**입니다.

**5. reset으로 되돌리기 - 다양한 옵션으로 버전 되돌리기**

이번에는 이미 커밋된 과거의 커밋으로 버전을 되돌리는 reset 명령어의 옵션에 대해 알아보겠습니다.

실습을 위해 파일을 적절하게 수정하고 커밋을 해줍니다.

```
# git add .
# git commit -m "메시지 1"
# git add .
# git commit -m "메시지 2"
# git add .
# git commit -m "메시지 3"
# git add .
# git commit -m "메시지 4"
```

![img](https://t1.daumcdn.net/cfile/tistory/99A26B495CBACB2F1E)



**
**

**1) --hard 옵션**

git reset 명령어로 메시지3 버전( a979452 )으로 되돌아 가고자 합니다.

이 때, --hard 옵션을 주면 working directory의 내용까지 모두 바꿉니다.

```
# git reset --hard {버전명}
```

![img](https://t1.daumcdn.net/cfile/tistory/99C67E485CBACC3431)



reset --hard 명령을 실행한 후, log를 확인해보니 "메시지 4"가 사라졌습니다.

그리고 상태를 확인해보니 working directory도 깔끔합니다.

**2) 옵션 없이**

이번에는 옵션 없이 reset해서 working directory 내용은 유지하고, 커밋 이력만 삭제하도록 하겠습니다.

마찬가지로 다음과 같이 히스토리 있을 때, 메시지3 버전( a97945e )으로 되돌아가겠습니다.

```
# git reset {버전명}
```

![img](https://t1.daumcdn.net/cfile/tistory/994CEE3E5CBACEB328)

--hard 옵션과 마찬가지로 커밋 이력은 삭제됐습니다.

그런데 상태를 보면, working directory 내역이 남아있는 것을 확인할 수 있습니다.

**3) --soft 옵션**

이번에는 옵션없이 실행해서 add까지 된, 즉 staging area까지 적용되는 상태를 --soft 옵션을 추가해서 reset 해보겠습니다.

```
# git reset --soft {버전명}
```

![img](https://t1.daumcdn.net/cfile/tistory/99BC8C345CBAD02730)

마찬가지로 커밋 이력은 삭제 됐습니다.

그런데 상태를 보니 add까지 적용되어 있는 것을 확인할 수 있습니다.

**6. revert로** **되돌리기**

reset은 버전을 되돌리면서 되돌린 버전 이후의 히스토리를 모두 삭제하는 반면,

revert는 버전을 되돌리지만 모든 히스토리를 유지합니다.



reset 예제와 마찬가지로 히스토리와 다음과 같을 때, revert 명령으로 메시지3 버전( a97945e )으로 되돌아가보겠습니다.

```
# git revert {버전명}
```

![img](https://t1.daumcdn.net/cfile/tistory/99CA9A505CBAD27504)

reset과 비교해보겠습니다.

먼저 revert 명령을 실행할 때, 충돌이 발생한 것을 확인할 수 있습니다.

reset의 경우는 커밋이력이 사라지기 때문에 충돌이 발생하지 않지만, revert의 경우 커밋이력이 남기 때문에 같은 곳을 수정했다면 충돌이 발생할 것입니다.

그리고 메시지4 커밋 이력은 그대로 남아 있네요.

상태를 확인해보니 working directory도 그대로 유지하고 있습니다.

즉, 그대로 유지하려다 보니 충돌이 발생한 것이겠죠.

**7. reset으로 병합 취소하기**

reset 명령어로 브랜치 간의 병합을 취소할 수도 있습니다.



예를 들어, master와 child 두 브랜치가 있을 때, master 브랜치에서 child 브랜치를 병합하려고 했는데 병합을 하면 안되는 작업이었던 것이었습니다.

이 경우에 병합을 한 후, 바로 병합을 취소해야 합니다.



병합은 위험한 작업이기 때문에 Git은 병합을 하기 전에, 최신 커밋에 포인터를 지정( **ORIG_HEAD** )합니다.

따라서 **방금 병합한 것을 되돌리려면** -merge 옵션과 ORIG_HEAD 포인터를 지정하여 reset 명령어를 실행하면 됩니다.

```
# git reset –merge ORIG_HEAD
```

**8.** **revert로** **병합 취소하기**

reset과 마찬가지로 revert 명령어를 통해 병합을 취소할 수도 있습니다.

reset은 방금 병합한 것을 취소할 때 사용하지만, 조금 시간이 지난 병합을 취소하고 싶다면 revert 명령어로 병합을 취소하면 됩니다.

이 때 rebase로 병합을 했다면 merge에 대한 커밋 이력이 남지 않기 때문에 불가능합니다.



우선 병합 상태를 --graph 옵션을 통해 확인해보겠습니다.

 

![img](https://t1.daumcdn.net/cfile/tistory/99BCE9355B8938D236)



master와 child 브랜치가 있고, master 브랜치에서 child 브랜치를 병합한 상황입니다.



그런데 이 병합이 잘못된 것을 알게 되어 병합을 하기 전인, beb1e77으로 되돌아가고자 합니다.

revert의 --mainline 옵션을 사용해서 병합을 취소할 수 있습니다.



**mainline**이란 병합을 취소한 후에, 어느 라인을 기준으로 되돌아 갈 것인지 기준을 정하는 것입니다.

mainline은 병합 그래프를 기준으로 왼쪽에서부터 1로 계산을 합니다.

즉, beb1e77가 1이 되고, 22d2f35는 2가 됩니다.



따라서 아래과 같이 --mainline 숫자 옵션으로 명령어를 실행하면 병합을 취소하고 beb1e77 버전으로 되돌아갈 수 있게 됩니다.

```
# git revert --mainline 1 {취소할 병합 커밋ID}
```

{취소할 병합 커밋ID}는 병합이 완료된 커밋ID를 말하며, 여기서는 1a83efc가 되겠네요.





명령어를 실행하면 편집기 창이 나오면서 커밋 메시지를 작성하라고 합니다.

메시지를 작성한 후, 로그를 살펴보면 다음과 같습니다.



![img](https://t1.daumcdn.net/cfile/tistory/99964D3A5B8938E50B)



또한 되돌린 파일 내역을 보시면 beb1e77 버전을 기준으로 맞춰져 있을 것입니다.



만약 병합이 merge로 이루어진 것이 아니라 rebase를 통해 이뤄졌다면, 병합된 커밋을 찾기가 힘들어집니다.

팀원과 잘 상의를 한 후에..... 커밋을 찾았다면, 아래의 명령어를 실행해서 과거의 버전으로 되돌아 가면 됩니다.

```
# git checkout { 커밋ID }
```

**9. reset과 revert의 차이점**

그렇다면 언제 git reset을 쓰고 언제 git revert를 사용할까요?



git reset은 remote repository까지 컨트롤할 수 없습니다.

커밋 이력이 삭제되므로, remote와 싱크가 안맞아서 결국 push 할 수 없습니다.

따라서 **이미 원격 저장소에 push를 한 상태에서 되돌리고 싶다면 git revert를 사용해야 합니다.**



병합 과정에서는 revert 명령어가 더 먼 과거의 버전으로 돌아갈 수 있다는 점이 다르네요.

https://victorydntmd.tistory.com/79 -> 참고 사이트

[http://www.devpools.kr/2017/01/31/%EA%B0%9C%EB%B0%9C%EB%B0%94%EB%B3%B4%EB%93%A4-1%ED%99%94-git-back-to-the-future/](http://www.devpools.kr/2017/01/31/개발바보들-1화-git-back-to-the-future/)

-> 이해를 돕기위한 만화

[https://www.devpools.kr/2017/02/05/%EC%B4%88%EB%B3%B4%EC%9A%A9-git-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0-reset-revert/](https://www.devpools.kr/2017/02/05/초보용-git-되돌리기-reset-revert/)

-> 설명 글

```
git reset <옵션> <돌아가고싶은 커밋>
```

옵션이 몇가지 있는데 자주 쓰는 것 hard, mixed, soft 세가지가 있다. 

1. hard

   돌아가려는 이력이후의 모든 내용을 지워 버립니다. 이렇게 하면 이후 커밋 내용들이 모두 지워 지고 모든것이 초기화됩니다.

   ```
   $ git reset --hard  <돌아가고싶은 커밋>
   ```

2. soft

   돌아가려 했던 이력으로 되돌아 갔지만, 이후의 내용이 지워지지 않고, 해당 내용의 인덱스(또는 스테이지)도 그대로 있다. 바로 다시 커밋할 수 있는 상태로 남아있는 것입니다. 기억은 되돌려졌지만, 이 후에 커밋 했던 것들은 따로 저장되어 있는 상태입니다.

3. ***mixed ( 옵션을 적지 않으면 mixed로 동작) ?????***

   역시 이력은 되돌려진다. 이후에 변경된 내용에 대해서는 남아있지만, 인덱스는 초기화 됩니다. 커밋을 하려면 다시 변경된 내용은 추가해야 하는 상태입니다. 기억도 되돌려 졌고, 표와 팝콘 그리고 사이다는 사야겠다는 마음만 남아있다고 할 수 있습니다.

```
$ git reset HEAD~6
```

위와 같이 현재부터 6개 이전 이력으로 돌아가라라고 상대적으로 지정할 수도 있습니다.

------------

> **Git merge (브랜치 병합) 하는 방법**

Git을 버전관리시스템으로 두고 같이 협업하는 과정에서 브랜치를 만들어서 각자 개발을 했다면,

언젠가는 소스코드를 합쳐서 테스트도 해보고 시스템에 적용도 해보고 해야한다.

그런 상황에서 브랜치를 합치는 것(병합)을 merge라 한다.

*** 사용법**

A브랜치에서 B브랜치를 병합한다 (= A로 B를 가져온다. A<-B)

: **git merge B브랜치명** (ex. git merge exp)

merge에는 크게 **두 가지 상황**이 존재한다.

**1**. 서로 다른 파일을 수정했을 때

**2**. 서로 같은 파일을 수정했을 때

먼저 1번의 상황은 불편할 것이 하나도 없다.

만약 A라는 사람이 A.java 파일을 수정했고 B라는 사람이 B.java 파일을 수정했을 때 merge 한다면 git이 자동으로 소스코드를 합쳐줄 것이다. (충돌 없음)

2번의 상황은 또 다시 세부적으로 두가지 경우로 나뉠 수 있다.

2-1) 서로 같은 이름의 파일을 수정했지만 수정한 부분이 다를 때

2-2) 서로 같은 이름의 파일을 수정하고 수정한 부분이 겹칠 때

예를 들어 2-1)의 상황은 A라는 사람이 X라는 파일의 1~200번째 줄까지 수정했고 B라는 사람이 X라는 파일의 400~600번째 줄까지 수정했다면 이 역시도 1번 상황과 마찬가지로 git이 자동으로 소스코드를 합쳐줄 것이다.

2-2)의 상황은 A라는 사람이 X라는 파일의 특정 메서드 f()의 특정 부분을 수정했다고 하고, B라는 사람이 똑같이 X라는 파일의 특정 메서드f()의 특정 부분을 수정했다면 (최소 한줄이라도 같은 부분을 수정했다고 가정) git은 자동으로 merge를 해줄 수 없는 상황이라고 사용자에게 알리고 사용자가 그 부분을 수정해주기를 위임한다.

이런 상황을 **conflict** 충돌이 일어났다고 한다.

git이 auto merge를 해주는 상황에서는 할말이 없다.

충돌나는 부분이 없으니 훌륭하게 git이 처리해주었기 때문이다.

그러나 2-2) 와 같은 상황처럼 충돌이 일어나면 개발자가 직접 해당 부분의 소스코드를 고쳐주어야 한다.

![img](https://t1.daumcdn.net/cfile/tistory/993C3B335A253FF00B)

master브랜치와 exp브랜치가 서로 공유하는 mergetest.txt라는 파일이 있다고 가정한다.

exp브랜치에서는 아래와 같이 소스를 수정하고 commit을 했고

```javascript
function a(x, y){
    console.log(x);
    console.log(y);
    console.log(x+y);
    return x+y;
}
```

master브랜치에서는 아래와 같이 소스를 수정하고 commit을 했다.

```javascript
function a(x, y){
    console.log(y);// x -> y
    console.log(y);
    return x*y;// x+y -> x*y
}
```

이 상황에서 master브랜치에서 exp브랜치를 merge하기 위해 "git merge exp" 라는 명령어를 치면 어떨까?

예상대로 conflict message를 주고 git status 명령어에서도 알려준다.

특히 conflict가 발생한 파일을 열어보면 쉽게 알 수 있다.

![img](https://t1.daumcdn.net/cfile/tistory/99ED31335A2541631B)

보면 <<<<<< HEAD 부터 >>>>>>까지가 충돌이 일어난 부분이고

<<<<<< HEAD 부터 ======까지는 master브랜치의 소스코드고

======부터 >>>>>> exp까지는 exp브랜치의 소스코드다.

git이 이 부분을 알려주니 그 부분의 코드를 잘 수정해서 파일을 저장한 후 다시 commit을 해주면 올바르게 merge가 된다.

\* **merge에서 메세지 파악**하기

\1. **fast-foward** : 빨리감기라는 뜻으로 예를 들어 A브랜치에서 급하게 다른 것을 만들어보려고 B브랜치를 생성하고 B브랜치는 여러번의 commit이 있었다.

이런 상황에서 A브랜치에서 B브랜치를 merge한다고 가정할 때, A브랜치에서 B브랜치를 분기해준 것외에 별 다른 commit이 없었으므로 A브랜치는 B브랜치만큼 그냥 "빨리감기"하면 되는 상황이다.

그래서 이런 상황일 때 별도의 commit log없이 B브랜치가 만든 최신의 commit log를 가리키게 만드는 것을 fast-foward라고 한다.

\2. **recursive strategy** : 재귀적인 전략으로 예를 들어 A브랜치에서 B브랜치를 생성했다. 그 후 A브랜치도 commit이 여러번 있었고 B브랜치도 commit이 여러번 있었을 때 A브랜치에서 B브랜치를 merge한다.

이러면 fast-foward할 수 없고 git은 A브랜치와 B브랜치의 조상 commit을 찾아 내부적으로 3way merge라는 방법을 이용하여 merge를 해준다.

> **실전에서는 어떻게 사용해야할까? [충돌예방법]
> **

혼자 개발하는 것이 아니기 때문에 충돌을 줄이기 위해 프로젝트의 큰 흐름인 master브랜치로 내맘대로 merge할 수는 없다.

그렇다고 merge 없이 1개월이든 6개월이든 내 branch안에서 개발만해서도 안된다.

-merge 때 conflict 수정이 엄청나게 많아지기 때문.

따라서 내 브랜치에 충돌을 최대한 예방하는 방법을 사용해야 한다.

즉, **master 브랜치의 변화를 지속적으로 내 브랜치로 가져와서 충돌나는 부분을 매번 제거하면서** 내 브랜치를 만들어야 먼 훗날에 master 브랜치로 병합할 때 충돌이 적게할 수 있다.

출처: https://jeong-pro.tistory.com/106 [기본기를 쌓는 정아마추어 코딩블로그]

------------

# 병합

## B 브랜치를 A 브랜치로 병합(merge)할 때 (B => A)

```
$ git checkout A
$ git merge B
```

## 병합(merge) 확인

```
❯ git log --branches --graph --decorate --oneline
*   d66cc18 (HEAD -> master) Merge branch 'exp'
|\
| * 7ba6cb1 (exp) 6
| * 019d8ce 5
| * d239731 4
| * 410316d 3
* | 2e6dadd 7
|/
* db667dd 2
* 932645b 1
```

## B 브랜치를 삭제할 때

```
$ git branch -d B
Deleted branch B (was d66cc18).
```

------

# 충돌

- merge 과정에서 파일의 이름이 같으면 충돌이 발생한다.
- 파일이 다르면 무조건 자동으로 합쳐준다.
- 파일이 같아도 수정한 부분이 다르다면 자동으로 합쳐준다. (버전관리를 사용하는 정말 중요한 이유중의 하나)

## 충돌이 생기면 아래와 같은 메시지가 뜬다.

```
❯ git merge exp
Auto-merging common.txt
CONFLICT (content): Merge conflict in common.txt
Automatic merge failed; fix conflicts and then commit the result.
```

## git status를 하면 충돌이 일어난 파일을 찾을 수 있다.

```
❯ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   common.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

## 충돌이 발생한 파일을 수정한다.

- 개발자가 직접 둘 중에 어느 수정 사항을 반영할 것인지 판단하여 수정

### merge conflict 발생 후 common.txt 파일 상태

- 이 정보를 참고로해서 두개의 코드를 병합한 후에 특수기호들을 제거한다.
- 수정 후 add, commit 진행하면 정상적으로 merge commit이 진행된다.

```
❯ vim common.txt
  1 function b
  2 <<<<<<< HEAD        # 현재 checkout 한 브랜치의 상태
  3 fucntion a(master)  
  4 =======             # 구분자 ====================
  5 fucntion a(exp)      
  6 >>>>>>> exp         # 병합하려는 대상인 exp 브랜치의 상태
  7
  8 function c
```