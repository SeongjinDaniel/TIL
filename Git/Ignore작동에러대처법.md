# gitignore 작동 에러 대처법



.gitignore가 제대로 작동되지 않아서 **ignore처리된 파일이 자꾸 changes에 나올때**가 있습니다.
git의 캐시가 문제가 되는거라 아래 명령어로 캐시 내용을 전부 삭제후 다시 add All해서 커밋하시면 됩니다.

```bash
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```

- [참고](https://stackoverflow.com/questions/11451535/gitignore-is-not-working)

#### 참조

- [.gitignore가 작동하지 않을때 대처법](https://jojoldu.tistory.com/307)