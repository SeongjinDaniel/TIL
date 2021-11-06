# Mongo DB 조회방법



1. 해당 변수 존재 하면 조회
   - db.getCollection('user_skills').find({'collection_info':{$exists: true}})

2. 해당 변수 0보다 큰거 조회
   - db.getCollection('dragon').find({"atk_gem":{$gt:0}})

3. and 연산 조회
   - db.getCollection('dragon').find({$and:[{uid:"60e79fbc5c608e43072c867d"},{did:100307}]})
4. 범위 조회(likes 값이 10보다 크고 30보다 작은 Document 조회)
   - db.articles.find( { “likes”: { $gt: 10, $lt: 30 } } )

5. $where 연산자

   - $where 연산자를 통하여 javascript expression 을 사용 할 수 있습니다.

   - comments field 가 비어있는 Document 조회

   - db.articles.find( { $where: “this.comments.length == 0” } )

     > db.articles.find( { "comments": { $elemMatch: { "name": "Charlie" } } } )
     > { "_id" : ObjectId("56c0ab6c639be5292edab0c4"), "title" : "article01", "content" : "content01", "writer" : "Velopert", "likes" : 0, "comments" : [ ] }

6. $elemMatch 연산자

   - $elemMatch 연산자는 Embedded Documents 배열을 쿼리할때 사용됩니다. 저희 mock-up data 에서는 comments 가 Embedded Document에 속합니다.

   - comments 중 “Charlie” 가 작성한 덧글이 있는 Document 조회

   - db.articles.find( { “comments”: { **$elemMatch**: { “name”: “Charlie” } } } )

     > db.articles.find( { "comments": { $elemMatch: { "name": "Charlie" } } } )
     > { "_id" : ObjectId("56c0ab6c639be5292edab0c6"), "title" : "article03", "content" : "content03", "writer" : "Bravo", "likes" : 40, "comments" : [ { "name" : "Charlie", "message" : "Hey Man!" }, { "name" : "Delta", "message" : "Hey Man!" } ] }





#### 참조

- https://velopert.com/479