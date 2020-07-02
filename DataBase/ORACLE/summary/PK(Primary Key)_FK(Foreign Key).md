# [PK(Primary Key), FK(Foreign Key)](https://keep-cool.tistory.com/51)

**PK(Primary Key)와 FK(Foreign Key)는 테이블의 필수 요소로써 모든 테이블은 이들 둘 중 하나 이상을 반드시 포함하고 있다.**



#### PRIMARY KEY(PK)

**Primary Key 설정**

```sql
CREATE TABLE 테이블(

…

CONSTRAINT 제약_조건_이름 PRIMARY KEY (컬럼)

);
```

```sql
CREATE TABLE 테이블(

컬럼 데이터타입 CONSTRAINT 제약_조건_이름 PRIMARY KEY,

…
```

- 테이블을 생성할 때 PK를 정의한다.

- PK는 각 행을고유하게 식별하는 역할을 담당한다.

- 테이블당 하나만 정의 가능하다.

- 지정된 컬럼에는 중복된 값이나 NULL값이 입력될 수 없다.

- - NOT NULL + UNIQUE(UK)를 한 것과 같은 기능을 한다.

- PK로 지정 가능한 컬럼이 여러 개 있을 때는 검색에 많이 사용되고 간단하고 짧은 컬럼을 지정한다.

- 주 식별자, 주키 등으로 불린다.

- 고유 인덱스(Unique index)가 자동으로 생성된다.



#### FOREIGN KEY(FK)

**Foreign Key 설정**

```sql
CREATE TABLE 테이블(

…

CONSTRAINT 제약_조건_이름 FOREIGN KEY (컬럼)

REFERENCES 참조할_테이블 (참조할_컬럼)

[ON DELETE CASCADE | ON DELETE SET NULL]

);
```

```sql
CREATE TABLE 테이블(

컬럼 데이터타입 CONSTRAINT 제약_조건_이름 FOREIGN KEY

REFERENCES 참조할_테이블 (참조할_컬럼)

[ON DELETE CASCADE | ON DELETE SET NULL]

…
```

- 테이블을 생성할 때 FK를 정의한다.

- FK가 정의된 테이블이 자식 테이블이다.

- 참조되는 테이블을 부모 테이블이라고 한다.

- 부모 테이블은 미리 생성되어 있어야 한다.

- 부모 테이블의 참조되는 컬럼에 존재하는 값만을 입력 할 수 있다.

- 부모 테이블은 FK로 인해 삭제가 불가능하다.

- REFERENCES : 참조할 부모 테이블과 부모 테이블에 있는 컬럼을 정의한다.

- ON DELETE CASCADE : 참조되는 부모 테이블의 행에 대한 DELETE를 허용한다.

- - 부모 테이블의 행이 지워지면 자식 테이블의 행도 같이 지워진다.

- ON DELETE SET NULL : 참조되는 부모 테이블의 행에 대한 DELETE를 허요한다.

- - 부모 테이블의 행이 지워지면 자식 테이블의 행은 NULL 값으로 설정된다.

- 데이터 타입이 반드시 일치해야 한다.

- 참조되는 컬럼은 PK이거나 UK(Unique key)만 가능하다.

- 외부키, 참조키, 외부 식별자 등으로 불린다.

```sql
insert into countries values ('KR', 'Korea', 3);
```

1 행 이(가) 삽입되었습니다.