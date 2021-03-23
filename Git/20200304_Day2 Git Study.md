# Git Study Day2

Git의 세 가지 단계는 `Working directory`, `Staging area`, `Git directory` 단계로 나뉜다. Git은 파일을 `Committed`, `Modified`, `Staged` 이렇게 세 가지 상태로 관리한다.

## Committed

데이터가 로컬 데이터베이스에 안전하게 저장되었다는 것을 의미한다.

## **Modified**

수정한 파일을 아직 로컬 데이터베이스에 커밋 하지 않은 것을 의미한다.

## **Staged**

현재 수정한 파일을 곳 커밋 할 것이라고 표시한 상태를 의미한다.

위의 세 가지 상태는 Git의 세 가지 단계와 연결돼 있다.

**Git directory**는 Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳을 말한다. `Git directory`가 Git의 핵심이다. 다른 컴퓨터에 있는 저장소를 `Clone` 할 때 `Git directory`가 만들어진다.

**Working directory**는 프로젝트의 특정 버전을 `Checkout` 한 것이다. Git 디렉토리는 지금 작업하는 디스크에 있고 그 디렉터리에 압축된 데이터베이스에서 파일을 가져와서 워킹 디렉터리를 만든다.

**Staging area**는 Git 디렉터리에 있다. 단순한 파일이고 곧 커밋 할 파일에 대한 정보를 저장한다. 종종 인덱스라고 불리기도 하지만, `Staging area`라는 명칭이 표준이 되어가고 있다.

Git으로 하는 일은 기본적으로 아래와 같다

- `Working directory`에서 파일을 수정한다.
- `Staging area`에 파일을 `Stage` 해서 커밋 할 스냅샷을 만든다.
- `Staging area`에 있는 파일들을 커밋해서 Git 디렉터리에 영구적인 스냅샷으로 저장한다.

Git 디렉터리에 있는 파일들은 `Committed` 상태이다. 파일을 수정하고 `Staging area`에 추가했다면 `Staged`이다. 그리고 `Checkout` 하고 나서 수정했지만, 아직 `Staging area`에 추가하지 않았으면 `Modified`이다.

--------



### 워킹트리를 정리하는 git clean

git 명령어 중에서 워킹트리의 내용을 변경하는 대표적인 명령은 checkout과 reset이다. 그런데 워킹트리의 내용을 변경하는 대부분의 git 명령은 untracked 상태인 파일은 건드리지 않는 경향이 있다. 그래서 파일의 상태가 untracked인 것이다. 사람으로 따지면 '관심없어' 정도에 해당하는 느낌이다.

그런데 작업을 하다보면 명확한 이유는 없지만 다양한 상황에서 많은 수의 untracked파일과 폴더가 생겨나서 이를 한꺼번에 삭제해야 될 경우가 자주 생긴다. 이럴 때 git clean 명령을 사용할 수 있다. git clean 명령을 모른다면 수동으로 삭제해도 되지만 프로젝트가 복잡해졌을 때 untracked만 골라서 삭제하기는 쉽지 않다.

- untracked 상태의 파일들을 삭제합니다. 파일 또는 경로 이름을 지정하지 않은 경우 모든 untracked 파일들을 삭제합니다.

  ```
  git clean -f -d <파일 또는 폴더 이름>
  ```

#### clean을 이용한 untracked 파일 정리

```
$ git status
nothing to commit, working tree clean
$ echo "some" > some.txt # 1 some.txt 생성
$ mkdir somedir # 2 somedir 이라는 이름의 폴더 생성
$ echo "some2" > somedie/some2.txt # 3 somdir 아래에 some2.txt 생성

$ git status # 4 상태 확인

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	some.txt
	somedir/
nothing added to commit but untracked files present (use "git add" to track)

$ git clean -f -d # 5 clean 명령으로 전체 정리
Removing some.txt
Removing somedir/

$ git status # 6 다시 상태 확인
nothing to commit, working tree clean

```

위 실습에서는 간단하게 파일과 폴더들을 생성한 상태에서 git clean 명령을 적용해서 이들을 다시 정리.

1. some.txt 파일을 생성한다.
2. mkdir 명령으로 somedir 폴더를 생성한다.
3. 생성한 somedir 폴더 아래 some2.txt 파일을 생성한다.
4. 상태를 확인해 보면 폴더와 파일이 untracked 상태인 것을 알 수 있다.
5. git clean -f -d 명령으로 모든 untracked 파일들을 정리합니다.
6. 다시 상태를 확인해 보면 파일들을 생성하기 전 상태로 돌아가 있는 것을 확인할 수 있다.

git clean 명령은 편리하지만 조심해서 사용해야 한다. untracked 파일들은 아직 커밋되기 전 상태이기 때문에 한 번 삭제하면 복구가 불가능하기 때문이다. 그래도 한번에 모든 untracked파일들을 정리해 주기 때문에 유용한 CLI 명령어중 하나이다.

### 입문자들이 선호하는 reset --hard

세 가지의 git reset 명령은 공통적으로 커밋을 되돌릴 때 사용. 각각의 동작 방식에는 차이가 있는데 많이 사용하는 명령은 hard  reset인 reset --hard이다.

- hard reset이라고 부르며 해당 커밈ㅅ으로 되돌리고 싶을 때 사용한다. 워킹트리의 내용도 함께 초기화된다.

  ```
  git reset --hard <커밋체크섬>
  ```

- 옵션을 생략할 경우 기본인 mixed 모드입니다. 이 경우 워킹트리의 파일은 남아 있고 스테이지만 초기화합니다.

  ```
  git reset --mixed <커밋체크섬>
  ```

- soft reset 모드에서는 HEAD만 이동한다. 커밋을 될돌아갔지만 스테이지와 워킹트리의 내용은 변경되지 않는다.

  ```
  git reset --soft <커밋체크섬>
  ```

| 구분                | soft     | mixed(기본) | hard   |
| ------------------- | -------- | ----------- | ------ |
| 현재 브랜치(HEAD)   | 초기화   | 초기화      | 초기화 |
| 스테이지            | 남아있음 | 초기화      | 초기화 |
| 워킹트리의 변경사항 | 남아있음 | 남아있음    | 초기화 |

-모드에 따른 git reset 명령의 차이점

#### CLI를 이용한 hard reset

```
$ git checkout master # master 브랜치 체크아웃
$ git checkout -b reset-test # 1 테스트용 브랜치 생성 및 체크아웃

(reset-test) $ git log --oneline -n1 # log 확인
88d8e0f (HEAD -> reset-test, origin/master, master) master 커밋 2
$ echo "reset1" > reset.txt # 2 파일 생성 및 커밋
$ git add reset.txt
$ git commit
[reset-teset 378c96e] reset 테스트용 커밋
1 file changed, 1 insertion(+)
$ git log --oneline -n3 # 3 log 확인, 마지막 커밋의 체크섬을 메모장에 기록하자
378c96e (HEAD -> reset-test)reset 테스트용 커밋
a3c0f7e (origin/master, origin/HEAD, master) master 커밋 2

$ git reset --hard HEAD~ # 4 2번째 부모 커밋까지 되돌림
HEAD is now at a3c0f7e master 커밋 2

$ ls # reset.txt가 사라졌다!
feature1.txt feature2.txt file1.txt master.txt

$ git status # 6 스테이지도 깨끗해 진 것을 확인
On branch reset-test
nothing to commit, working tree clean

$ git log --oneline -n1 # 7 HEAD의 위치 확인
a3c0f7e (origin/master, origin/HEAD, master) master 커밋 2
```

1. 먼저 [master] 브랜치로부터 [reset-test] 브랜치를 생성하고 체크아웃한다.
2. reset1.txt 파일을 생성하고 커밋을 한다.
3. git log로 커밍 히스토리를 확인하는데 여기서 마지막 커밋의 커밋체크섬을 메모장에 꼭 기록해 놓아야 합니다.
4. git reset -- hard HEAD~ 명령으로 커밋을 되돌립니다. HEAD~ 은 부모 커밋인 378c96e 커밋을 가르킨다.
5. ls 명령을 이용해 파일을 보면 방금 만들었던 reset.txt가 사라진 것을 확인할 수 있음.
6. git status 명령으로 스테이지를 보면 마찬가지로 스테이지도 깨끗하다.
7. HEAD의 위치가 최초 브랜치를 생성했던 [master]브랜치로 돌아간 것을 볼 수 있다.

### hard reset의 복구

```
(reset-test) $ git reset --hard 378c96e # 1 메모장에 기록해둔 체크섬을 이용해서 원래대로 돌아감
HEAD is now at 378c96e reset 테스트용 커밋

$ cat reset.txt # 2 파일 내용 확인
reset1

$ git log --oneline -n2 # 3 로그 확인
378c96e (HEAD -> reset-test)reset 테스트용 커밋
a3c0f7e (origin/mster, origin/HEAD, master) master 커밋 2
```

1. 메모장에 기록해 둔 커밋 체크섬을 이용해 병합했다.
2. 파일 내용을 확인해 보니 정상적으로 복구되었다.
3. 로그도 마찬가지로 되살아난 것을 볼 수 있다.

로컬저장소의 커밋은 없어지지 않는다. 사라진 것처럼 안 보일 뿐이다. 우리는 이전 실습에서 메모장에 커밋 체크섬을 기록해 뒀기 때문에 쉽게 다시 살릴 수 있었다. 그럼 커밋 체크섬을 항상 기억해야 할까?

--------



