# CLI에서 mongodb 명령어



### MongoDB 쉘 실행

> \> mongo

```
$ mongo localhost:4707
```

포트만 설정한 경우는 아래와 같이 접속할 수 있다. 해당 데이터 베이스로 접근한다.  admin 은 관리자 데이터베이스이다. admin은 해당하는 [db이름]을 사용해서 해당 db에서도 접속해서 데이터를 다룰수 있다.

```
$ use admin
```



### 데이터베이스 생성

> *> use <DB 이름>*



#### 현재 모든 DB 조회

> *> show dbs*

#### 현재 사용하고 있는 db

> \> db

#### 컬렉션 생성 및 보기 

> \> db.createCollection("[COLLECTION_NAME]")

`> show dbs` 를 하면 databse db가 생성된 것을 볼 수 있다. 

#### 현재 생성된 collection 조회

> \> show collections



### Document 

#### insert()

> \> db.[db명].insert({"nickname":"freekim", "email":"[test@google.com](https://freekim.tistory.com/test@google.com)"})



#### collection 삭제

현재 db에 "users"라는 이름의 collection이 있다고 가정하자.

```
> db.getCollectionNames()
[ "system.indexes", "users" ]
```

현재 db에서 users collection을 삭제하는 명령은 drop이다.

```
> db.users.drop()
true
> db.getCollectionNames()
[ "system.indexes" ]
```

drop 명령을 통해 collection이 삭제된 것을 확인할 수 있다.



#### db 삭제

먼저 "test"라는 이름의 db를 생성한다:

```
> use test
switched to db test
> show dbs
local  0.078GB
test   0.078GB
```

db를 삭제하는 명령어는 dropDatabase이다.

```
> db.dropDatabase()
{ "dropped" : "test", "ok" : 1 }
> show dbs
local  0.078GB
```



#### collection 내용 삭제

해당 collection의 내용을 전체 삭제하는 명령어는 remove이다:

```
> use test
switched to db test
> db.users.insert({username: "gchoi"})
WriteResult({ "nInserted" : 1 })
> db.users.insert({username: "jmpark"})
WriteResult({ "nInserted" : 1 })
> db.users.insert({username: "hskim"})
WriteResult({ "nInserted" : 1 })
> db.users.insert({username: "tjkwak"})
WriteResult({ "nInserted" : 1 })
>
> db.users.find().pretty()
{ "_id" : ObjectId("5533b7e365ab6551bc5be2a7"), "username" : "gchoi" }
{ "_id" : ObjectId("5533b7ea65ab6551bc5be2a8"), "username" : "jmpark" }
{ "_id" : ObjectId("5533b7ef65ab6551bc5be2a9"), "username" : "hskim" }
{ "_id" : ObjectId("5533b7f465ab6551bc5be2aa"), "username" : "tjkwak" }
>
> db.users.remove({})
WriteResult({ "nRemoved" : 4 })
> db.users.find().pretty()
>
```