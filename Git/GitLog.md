# log



- **모든 log를 그림으로 볼수 있음**
  - `git log --graph --oneline --decorate --all`

- **Merge log**

  - (“Triple Dot” 문법을 이용하면 Merge 에 사용한 양 브랜치의 모든 커밋의 목록을 얻을 수 있음. 자세한 문법은 Triple Dot를 참고)

    - `git log --oneline --left-right HEAD...MERGE_HEAD`

    - Triple Dot

      - Triple Dot은 양쪽에 있는 두 Refs 사이에서 공통으로 가지는 것을 제외하고 서로 다른 커밋만 보여준다. 범위를 설명하는데 사용할 예제의 커밋 히스토리를 다시 보자. 만약 master 와 experiment 의 공통부분은 빼고 다른 커밋만 보고 싶으면 아래와 같이 하면 된다.

        ```
        $ git log master...experiment
        F
        E
        D
        C
        ```

        우리가 아는 log 명령의 결과를 최근 날짜순으로 보여준다. 이 예제에서는 커밋을 네 개 보여준다.
        그리고 log 명령에 --left-right 옵션을 추가하면 각 커밋이 어느 브랜치에 속하는지도 보여주기 때문에 좀 더 이해하기 쉽다. 

        ```
        $ git log --left-right master...experiment
        < F
        < E
        > D
        > C
        ```

  - git log 명령에 --merge 옵션을 추가하면 충돌이 발생한 파일이 속한 커밋만 보여줌

    - `git log --oneline --left-right --merge`

  -`-merge` 대신 `-p` 를 사용하면 충돌 난 파일의 변경사항만 볼 수 있다. 이건 왜 충돌이 났는지 또 이를 해결하기 위해 어떻게 해야 하는지 이해하는 데 **진짜로** 유용하다.





#### 참조

- Pro Git