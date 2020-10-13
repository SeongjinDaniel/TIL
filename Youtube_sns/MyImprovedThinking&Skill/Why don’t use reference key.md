# Why don’t use Reference key



외래키를 사용하게 되면 참조 무결성을 지킬 수 있어서 좋지만 더 큰 단점이 될 수 있어서 사용하지 않습니다.

이것에 대한 이유는 대용량 데이터를 취급할 때 첫번째로 고려해야할 대상입니다. sql을 사용해서 insert, update, delete 할 때 성능에 대한 이슈가 있습니다.

메인 테이블에 적용된 데이터와 참조된 데이터에서 오래된 데이터들을 일일이 삭제해서 유지 보수하는 것이 현실적으로 어렵기 때문입니다.



#### 참조

- [왜 DBMS에 있는 외래키(Foreign Key)를 사용하지 않는걸까?](https://youngyoungsw2020.github.io/dbms/database/foreignkey/%EC%99%9C%EB%9E%98%ED%82%A4%20%EC%82%AC%EC%9A%A9%EC%95%88%ED%95%98%EB%8A%94%20%EC%9D%B4%EC%9C%A0/2020/05/20/db-foreignKey-not-used.html)

- [[DBA\] foreign key(외래키) 단점과 위험성에 대해](https://mozi.tistory.com/344)

- [[데이터베이스] FK의 사용](https://ncookie.tistory.com/71)

  

