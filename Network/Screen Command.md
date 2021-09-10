# Screen Command



### screen 내부 명령어

`Ctrl+a, d` : 현재 스크린으로부터 탈출(Deattach). (스크린은 꺼지지 않고 여전히 동작 중)

`Ctrl+a, c` : 스크린에서 새창 띄우기

`Ctrl+a, 숫자` : 해당 번호의 스크린으로 이동

`Ctrl+a, n` : 다음 창으로 이동 (Ctrl+a, space와 동일)

`Ctrl+a, p` : 이전 창으로 이동 (Ctrl+a, Backspace와 동일) 



### 자주 사용하는 옵션

`screen -S [스크린 이름]` : screen에 **이름을 지정하며 진입**.

`screen -R [스크린 이름]` : screen이 **존재한다면 다시 진입(Reattach)**하고, screen이 **없다면 해당 스크린 이름을 만들며 진입**.

`screen -ls (screen -list)` : 현재 존재하는 **스크린 리스트 출력**

`screen -x [스크린 이름]` : **실행 중인 스크린에 다시 진입(Reattach)**. (-R 옵션은 Single display mode, -x 옵션은 Multi display mode이다. 즉, -R옵션은 해당 스크린에 여러 명이 들어가도 서로 무슨 명령을 치는지 모르지만, **-x 옵션은 해당 스크린에 여러명이 들어가도 마치 한 화면처럼 움직여, 상대방이 무슨 명령어를 치는지까지 다 볼 수 있다.**)

`screen -S [스크린 이름] -X quit` : 해당 **스크린 종료** (해당 스크린 삭제됨). [스크린이름] 대신 스크린 번호를 써도 된다. 또는 **사용하고 있는 스크린에서 모든 창을 exit으로 꺼버려도 해당 스크린은 종료**됩니다.