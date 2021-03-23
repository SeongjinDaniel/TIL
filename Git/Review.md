# :tada: Git

사람이 사용할 수 있는 SW를 만들수 있는지!!?!!!!

http://abit.ly/r7if5x -> 강의때 사용 google spread

#### Github skill

Naming -> 일치시키기!!

**Readme에서 이런식으로 url 태그 걸어놓기**

[알고리즘잡스](https://github.com/SeongjinOliver/TIL/tree/master/Algorithm)

#### 참고 사이트

| TIL 예시                  | https://github.com/namjunemy/TIL                             |
| ------------------------- | ------------------------------------------------------------ |
| 프로젝트 관리 예시        | https://github.com/ejolie/miumbieub                          |
| 체대생 개발자 취업하기    | https://ryan-han.com/post/memoirs/memoirs2018/               |
| 개발자 면접 질문          | https://github.com/JaeYeopHan/Interview_Question_for_Beginner |
| AWS Invent                | https://reinvent.awsevents.com/                              |
| AWS 커뮤니티              | https://www.meetup.com/ko-KR/awskrug/                        |
|                           | https://www.meetup.com/ko-KR/awskrug/                        |
| 웹사이트 만들기 견적 가능 | https://insomenia.com/                                       |
| 스타트업 서칭             | http://main.primer.kr/primerclub-all                         |
| 우아한 형제들 branch 예제 | https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html |

------

#### 공유 블로그 등

https://www.gatsbyjs.org/ -> Gatsby

https://www.netlify.com/ -> 깃허브 그대로 가져와서 호스팅 할 수 있다!

https://devcenter.heroku.com/ -> heroku -> git 을 통해 쉽게 배포할 수 있는 사이트

-----------

#### Good Story

Real Artists Ship

Real Developers Deploy

-------------

- 가능한한 자동완성 기능을 자주 써야한다.

------

# :zap: Git

- Source Code Management(SCM): 코드 관리 도구

- 어떻게 관리? version을 통해 관리

  SCM -> VCS(Version Control System)

  - 커밋들로 version을 나눈다.
  - Post(게시글)와 Comment(댓글)와의 관계 는 1:N관계이다.
    - 1:1 관계
    - 1:N 관계
    - 아무런 없는 관계

- where(어떤 단위)?

  -> 폴더(디렉토리) -> (저장소, repository)

- **gitHub 내부 remote 이름은 origin**

- 포트폴리오 부트스트랩 주소

  - https://startbootstrap.com/themes/resume/
  
- Why? 문제를 잡아야 하는데, 코드

# 협업 시나리오

1. **push & pull**
   - 같은 저장소를 공유하고(저장소 공유가 필수)
   - Push와 Pull만을 통해서 협업 방식
   - (A)synchronous : 한 가지 task가 끝나야지 다음 task가 진행 될 수 있는
   - 끝말잇기
   - 
2. **Fork & PR(Pull Request)**
   - Open Source 운영(Contribute)
   - 저장소의 작성 권한이 없을 경우(공유가 되지 않은 경우)
   - 인턴
   - N행시 백일장
3. **Branching & PR with Shared Repository**
   - `git branch [브랜치의명]` : 브랜치를 생성
   - `git branch` : 현재 생성된 모든 branch를 보여줌
   - `git checkout [브랜치명]` : 브랜치를 이동
   - `git switch [브랜치명]` : 브랜치를 이동
   - `git branch -D [브랜치명]` : 브랜치 삭제
   - `git checkout -b [브랜치명]` : 브랜치 생성 & 이동

# 용도

- 코드 관리 도구 
- 협업 도구
- 배포 도구

# 코드 관리

SCM 

1. `git init` : git 으로 관리되는 폴더를 만듬
   - git 저장소(repository) 시작(**init**ialize)
2. `git status`
   - git 상태(status) 보기
3. `git add [파일명/폴더명]`
   - staging area에 파일을 추가(add)
4. `git rm --cached [파일명] (-r [폴더명])`
   - staging area에 파일을 삭제(unstaging)
   - `git rm --cached -r [폴더명]`
   - `git restore --staged [파일명]`
5. `git commit -m` "커밋 메세지"
   - 스냅샷을 찍기(현재 상태를 저장하기)
6. `git diff`
   - 어떤 코드들이 추가 변경 되었는지 확인할 수 있다.
7. `git log`
   - commit의 history(버전들의 내역
   - git log --oneline
   - git log --oneline -[갯수]
     - git log --oneline -1 -> 가장 최근 log
8. `git remote add [저장소의 이름] [저장소의 주소]`
   - `git remote add origin [저장소의 주소]` -> 처음 만드는 것을 origin을 만드는것이 관례
9. `git push [저장소의 이름] [브랜치의 이름]`
10. `git clone [git repo 이름]`
11. `git remote remove origin`
    - remote 삭제
12. `rm -rf [.git]` `rm -rf [폴더명]`
    - .git 파일 삭제!!
    - 디렉토리 파일 삭제!!
13. `touch [파일명]`
    - 파일을 생성함

`-, --` 두가지의 차이는 일반적으로 

- -줄임네임
- --풀네임

14. `git clean -f`
    - untracked 파일을 모두 제거하려면..
15. `git clean -fd`
    - untracked 파일 및 디렉토리까지 지우려면.. 위에서 **-d** 옵션을 추가로 주면 된다.

위의 결과처럼, 모두 제거되는 것을 확인할 수 있다.

아주 깨끗해진 로컬을 볼 수 있을 것인데, 한 가지 문제라면 모두 제거하는 것이므로, 지우고 싶지 않은 파일도 제거할 가능성이 존재한다.

이때, 사용할 수 있는 옵션은 **--dry-run**이다. 이 옵션을 사용하면, 어떤 파일이 제거될 예정인 지 확인할 수 있다.

16. `git clean -fd --dry-run`



# :fire: 실수들

- Git 폴더 안에 하부 디렉토리를 또다른 .init폴더를 만들면 안된다.
- 비밀번호를 저장할 때는 암호화해서 저장을 해야한다.(잘못 될 경우 철컹철컹...)
  - SHA256 hash function을 사용해서 DB에 저장하게된다.

--------

# 협업은 독재다

# Branch를 통한 협업 원칙

1. **master 브랜치는 절대 건드리지 않는다.**
2. 각자는 각자의 브랜치에서 먼저 작업을 한다.
   - 본인의 이름을 딴 브랜치를 생성 후 작업을 하고
   - 본인의 해당 브랜치를 push 한다.`git push origin [branch명]`
   - Pull Request를 보낸다.
3. 대장은 각자의 PR를 점검하고, merge를 진행한다.
4. **`merge` 후에는 `pull`을(`master`를 기준으로) 통해 코드 상태를 동기화 한다.**
5. 기존 브랜치는 삭제한다.
6. (대장/노예) Github에서 브랜치도 삭제한다. -> github에서 branch로 들어가서 삭제함
7. 1-5까지 반복

### Conflict를 두려워하지 말기

- merge 상황에서 발생함



### 1. Fast Forward Merge

- commit이 한쪽 branch에만 있는 경우

### 2. Auto Merge

\- 동일파일의 특정 변경 사항이 중복되지 않을 경우(특정 파일의 내용을 두 사람이 함께 변경하지 않은 경우)

### 3. Merge Conflict

\- 컨플릭트 나쁜거 아니야

------------

# 자소서

4개의 문항이 있으면 4개 모두 다른 경험을 쓴다!! -> 탈락!! -> 이것을 모두 하나의 경험으로 쓰면 완전 Goooooooooooooooood!

