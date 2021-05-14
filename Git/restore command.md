# restore comm



깃 버전 2.23부터 작업 트리에서 수정한 파일 되돌리기 명령어가 다음과 같이 바뀌었습니다. 

 

git checkout -- test.txt ==> **git restore test.txt**

 

checkout이라는 명령어가 작업 트리에서 수정한 파일을 되돌릴 때도 사용되었을 뿐더러 브랜치를 바꿀 때도 사용되었는데 변경 되어 더 명시적인 명령이 되었습니다.

 

또한 스테이징 되돌리기 명령어는 다음과 같이 바뀌었습니다. 스테이징을 되돌린다는 말은 git add를 통해 스테이지에 올라간 것을 다시 내린다는 뜻입니다. 

 

git reset HEAD test.txt ==> **git restore --staged test.txt**

 

restore라는 명령어가 새로 생기면서 한결 단순해진 느낌입니다. 