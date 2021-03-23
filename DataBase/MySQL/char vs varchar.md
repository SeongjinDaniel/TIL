# char vs varchar



### 저장 영역

1. CHAR형은 고정형. 최대 길이는 255.
2. VARCHAR형은 가변형. 최대 길이는 255,
   MySQL 5.0.3 이후부터는 65,535까지 가능.  –> 무슨이유 때문인지 모르겠지만 varchar(21841)까지만 지정할 수 있음. -> 추후 알아봐야할 문제



- varchar 가변길이 → 실제 문자 값  (길이에 따라 + 1 or 2 저장)
- char 고정길이 → 선언한 문자열 자릿수로 저장



#### 참조

- [[SQL] varchar, char 성능 상의 차이점](https://dog-foot-story.tistory.com/100)

- [[공유\] 데이터형 CHAR와 VARCHAR의 차이점](https://coding-restaurant.tistory.com/156)
- https://dev.mysql.com/doc/refman/8.0/en/char.html