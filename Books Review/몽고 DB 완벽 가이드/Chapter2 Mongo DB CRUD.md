# Mongo DB CRUD



생성(create), 읽기(read),  갱신(update), 삭제(delete)의 네 가지 기본적인 작업(CRUD)을 한다.



### 생성

**insertOne** 함수는 컬렉션에 도큐먼트를 추가한다.

```
> movie = {"title : "Star Wars: "Episode IV - A New Hope",
... "director"  : "George Lucas",
... "year" : 1977}
{
	"title : "Star Wars: "Episode IV - A New Hope",
	"director"  : "George Lucas",
	"year" : 1977
}
```

이 객체는 유효한 몽고DB 도큐먼트이며 insertOne 함수를 이용해 movies 컬렉션에 저장할 수 있다.

```
> db.movies.insertOne(movie)
{
	"acknowledged" : true,
	"insertedId" : ObjectId("571794b379c32b32a012b11")
}
```



### 읽기

**find**와 **findOne**은 컬렉션을 쿼리하는 데 사용한다. 컬렉션에서 단일 도큐먼트를 읽으려면 findOne을 사용한다.

```
> db.movies.findOne()
{
	"_id" : ObjectId("5712794b349c32b32a012b11"),
	"title" : "Star Wars: "Episode IV - A New Hope",
	"director" : "George Lucas",
	"year" : 1977
}
```

find와 findOne은 쿼리 도큐먼트(query document)형태로 조건 전달도 가능하다. 따라서 쿼리에서 일치하는 도큐먼트로 결과를 제한한다. 셸은 find와 일치하는 도큐먼트를 20개까지 자동으로 출력하지만 그 이상도 가져올 수 있다.



### 갱신

게시물을 갱신하려면 **updateOne**을 사용한다. updateOne의 매개변수는 최소 두 개다. 첫 번째는 수정할 도큐먼트를 찾는 기준이고, 두 번째는 갱신 작업을 설명하는 도큐먼트다.
갱신 하려면 갱신 연산자(update operator)인 set을 이용한다.

```
> db.movies.updateOne({title : "Star Wars: Episode IV -A New Hope"},
...{$set : {reviews: []}})
WriteResult({"nMatched": 1, "nUpserted": 0, "nModified": 1})
```

책에서는 WriteResult의 결과가 위와 같지만 조금 다르게 나온것을 확인했다.

```
// 아래와 같은 결과를 확인했음.
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

이제 도큐먼트에는 “*reviews*” 키가 생겼다. *find*를 호출해 새로운 키를 확인하자.

```
> db.movies.find().pretty()
{
	"_id" : ObjectId("5721794b349c32b32a012b11"),
	"title" : "Star Wars: Episode IV -A New Hope",
	"director" : "George Lucas",
	"year" : 1977,
	"revies" : [ ]
}
```



### 삭제

**deleteOne**과 **deleteMany**는 도큐먼트를 데이터베이스에서 영구적으로 삭제한다. 두 함수 모두 필터 도뮤먼트로 삭제 조건을 지정한다.

```
> db.movies.deleteOne({"title" : "Star Wars: Episode IV -A New Hope"})
```

필터와 일치하는 모든 도큐먼트를 삭제하려면 deleteMany를 사용한다.