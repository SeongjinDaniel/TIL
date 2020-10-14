# Primary Key(MySQL)

#### 

## Problem



#### Error

`Error Code: 1822. Failed to add the foreign key constraint. Missing index for constraint 'FK_board_user_user_id' in the referenced table 'user' 0.016 sec`



#### Code

```mysql
CREATE TABLE user
(
    `id`      	   INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `user_id`      CHAR(20)        NOT NULL    COMMENT '유저 아이디',
    `pw`           CHAR(128)       NOT NULL    COMMENT '비밀번호',
    `name`         CHAR(20)        NOT NULL    COMMENT '이름',
    `email`        CHAR(45)        NOT NULL    COMMENT '이메일',
    `addr`         VARCHAR(100)    NOT NULL    COMMENT '주소',
    `signup_date`  CHAR(45)        NOT NULL    COMMENT '가입 날짜',
    `phone`        VARCHAR(45)     NOT NULL    COMMENT '핸드폰',
    PRIMARY KEY (id, user_id)
);
ALTER TABLE user COMMENT '회원 정보';

-- user Table Create SQL
CREATE TABLE board
(
    `id`               INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디', 
    `user_id`          CHAR(20)        NOT NULL    COMMENT '유저 아이디', 
    `title`            VARCHAR(100)    NOT NULL    COMMENT '제목', 
    `detail_contents`  VARCHAR(200)    NOT NULL    COMMENT '세부 내용', 
    `reg_date`         CHAR(45)        NOT NULL    COMMENT '등록 날짜', 
    `like_count`       INT             NOT NULL    COMMENT '좋아요 개수', 
    `bad_count`        INT             NOT NULL    COMMENT '싫어요 개수', 
    `hits`             INT             NOT NULL    COMMENT '조회수',
    PRIMARY KEY (boadr_no),
    constraint FK_board_user FOREIGN KEY (user_id) REFERENCES user (user_id)
);
ALTER TABLE board COMMENT '게시글';
```

#### 

## Solution

부모 테이블에 있는 인덱스 2개를 자식 테이블에서 모두 같은 type과 name으로 선언하고 둘다 참조를 하니까 해결했다.



#### Code

```mysql
-- board 테이블에 user_id 참조를 하지 못하는 문제가 있었음!

-- user Table Create SQL
CREATE TABLE user
(
    `user_no`      INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `user_id`      CHAR(20)        NOT NULL    COMMENT '유저 아이디',
    `pw`           CHAR(128)       NOT NULL    COMMENT '비밀번호',
    `name`         CHAR(20)        NOT NULL    COMMENT '이름',
    `email`        CHAR(45)        NOT NULL    COMMENT '이메일',
    `addr`         VARCHAR(100)    NOT NULL    COMMENT '주소',
    `signup_date`  CHAR(45)        NOT NULL    COMMENT '가입 날짜',
    `phone`        VARCHAR(45)     NOT NULL    COMMENT '핸드폰',
    PRIMARY KEY (user_no, user_id)
);

ALTER TABLE user COMMENT '회원 정보';

-- user Table Create SQL
CREATE TABLE board
(
    `boadr_no`               INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디', 
    `user_id`          CHAR(20)        NOT NULL    COMMENT '유저 아이디', 
    `title`            VARCHAR(100)    NOT NULL    COMMENT '제목', 
    `detail_contents`  VARCHAR(200)    NOT NULL    COMMENT '세부 내용', 
    `reg_date`         CHAR(45)        NOT NULL    COMMENT '등록 날짜', 
    `like_count`       INT             NOT NULL    COMMENT '좋아요 개수', 
    `bad_count`        INT             NOT NULL    COMMENT '싫어요 개수', 
    `hits`             INT             NOT NULL    COMMENT '조회수',
    
    `user_no`		   INT             NOT NULL,
    PRIMARY KEY (boadr_no),
    constraint FK_board_user FOREIGN KEY (user_no, user_id) REFERENCES user (user_no, user_id)
);
```



### Improved Solution

primary key는 한 테이블당 하나만 사용하는것이 바람직하다.



```mysql
CREATE TABLE user
(
    `id`           INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `user_id`      CHAR(20)        NOT NULL    COMMENT '유저 아이디',
    `pw`           CHAR(128)        NOT NULL    COMMENT '비밀번호',
    `name`         CHAR(20)        NOT NULL    COMMENT '이름',
    `email`        CHAR(45)        NOT NULL    COMMENT '이메일',
    `addr`         VARCHAR(100)    NOT NULL    COMMENT '주소',
    `signup_date`  CHAR(45)        NOT NULL    COMMENT '가입 날짜',
    `phone`        VARCHAR(45)     NOT NULL    COMMENT '핸드폰',
    PRIMARY KEY (id),
    UNIQUE (user_id)
);

CREATE TABLE board
(
    `id`               INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `user_id`          CHAR(20)        NOT NULL    COMMENT '유저 아이디', 
    `title`            VARCHAR(100)    NOT NULL    COMMENT '제목', 
    `detail_contents`  VARCHAR(200)    NOT NULL    COMMENT '세부 내용', 
    `reg_date`         CHAR(45)        NOT NULL    COMMENT '등록 날짜', 
    `like_count`       INT             NOT NULL    COMMENT '좋아요 개수', 
    `bad_count`        INT             NOT NULL    COMMENT '싫어요 개수', 
    `hits`             INT             NOT NULL    COMMENT '조회수', 
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE RESTRICT ON UPDATE RESTRICT
);
```

따라서 제약 조건 +1을 사용하여 고유 하게 만들어야 한다.



#### 결론

primary key가 매번 table당 하나만 사용해야 한다는 문구는 보았지만 무심코 넘어갔던 기억이 있다. 이것을 간과해서 이런 엄청난 삽질을 할 수 있었고, 나에게는 또하나의 지식을 가져다준 부분이 되었다.

앞으로는 primary key는 한테이블에 하나만 사용할 예정이고 unique도 섞어서 사용할 예정이다. 다음에는 unique가 2개가 되면 이런 현상이 나오는게 아닌가 생각해 볼 문제이다.

foreign key 제약 조건을 설정할 때 참조되는 테이블의 필드는 반드시 unique나 primary key 제약 조건이 설정되어 있어야 한다.

외래 키 관계의 경우 관계를 생성하는 상위 테이블 열은 `unique`또는 `primary`이어야하며 데이터 유형도 동일해야한다.



#### 참조

- https://stackoverflow.com/questions/52470537/failed-to-add-the-foreign-key-constraint-missing-index-for-constraint-error-cod
- 생활코딩 Index(MySQL)
- https://stackoverflow.com/questions/43511183/mysql-error-1822-failed-to-add-foreign-key-constraint-missing-index-for-contra
- http://www.tcpschool.com/mysql/mysql_constraint_foreignKey