# git에서 원격저장소에 있는 폴더 삭제하기 

`git rm {파일 및 폴더명}` // 원격 저장소와 로컬 저장소에 있는 파일을 삭제한다.

`git rm -rf {파일 및 폴더명}` // 위에가 안되면 이렇게 해보세요

`git rm -r --cached {파일 및 폴더명}` // 원격 저장소에 있는 파일을 삭제한다. 로컬 저장소에 있느 파일은 삭제하지 않는다.

 

`git commit -m "remove webstom {파일 및 폴더명} directory"`

 

`git push origin master`



출처: https://jjunii486.tistory.com/55 [준수한쭈니네]