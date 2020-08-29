# 20200403 Git Branch Study

가장 큰 줄기는 master branch로 설정한다.

각각이 브랜치를 만들고 Merge를 해야한다. branch를 생성할때는 master branch로 가push 서 생성해야 된다. 그래야 master브랜치를 큰 줄기로 나머지 작은 줄기들로 merge를 할 수 있기 때문이다.

---------



### Git 브랜치를 Git Hub에 저장하기

`git push --set-upstream origin 브랜치명`

--------



--no-off 옵션

- 새로운 커밋 객체를 만들어 브랜치에 merge한다.
- 이것은 'feature' 브랜치에 존재하는 커밋 이력을 모두 합쳐서 하나의 새로운 커밋 객체를 만들어 'develop' 브랜치로 병합(merge)하는 것이다.

----------



#### Git 브랜치 삭제

`git branch -d 브랜치명`