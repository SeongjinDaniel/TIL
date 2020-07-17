# Connection Pool

클라이언트의 요청에 따라 각 어플리케이션의 스레드에서 데이터베이스에 접근하기 위해서는 Connection 필요합니다.

Connection pool은 이런 Connection 여러 개 생성해 두어 저장해 놓은 공간(캐시), 또는 이 공간의 Connection을 필요할 때 꺼내 쓰고 반환하는 기법을 말합니다.



#### Connection Pool 라이브러리

Connection pool을 제공하는 라이브러리로는 대표적으로 Apache의 Commons DBCP와 Tomcat-JDBC, BoneCP, HikariCP 등이 있습니다.



#### DB에 접근하는 단계

- 웹 컨테이너가 실행되면서 DB와 연결된 Connection 객체들을 미리 생성하여 pool에 저장합니다.
- DB에 요청 시, pool에서 Connection 객체를 가져와 DB에 접근하고
- 처리가 끝나면 다시 pool에 반환합니다.



#### Connction이 부족하면?

모든 요청이 DB에 접근하고 있고 남은 Conncetion이 없다면, 해당 클라이언트는 대기 상태로 전환시키고 Pool에 Connection이 반환되면 대기 상태에 있는 클라이언트에게 순차적으로 제공됩니다.



#### 왜 사용할까?

- 매 연결마다 Connection 객체를 생성하고 소멸시키는 비용을 줄일 수 있습니다.
- 미리 생성된 Connection 객체를 사용하기 때문에, DB 접근 시간이 단축됩니다.
- DB에 접근하는 Connection의 수를 제한하여, 메모리와 DB에 걸리는 부하를 조정할 수 있습니다.



### Thread Pool

비슷한 맥락으로 Thread pool이라는 개념도 있습니다.

이 역시 매 요청마다 요청을 처리할 Thread를 만드는것이 아닌, 미리 생성한 pool 내의 Thread를 소멸시키지 않고 재사용하여 효율적으로 자원을 활용하는 기법입니다.



### Thread Pool과 Connection pool

WAS에서 Thread pool과 Connection pool내의 Thread와 Connection의 수는 직접적으로 메모리와 관련이 있기 때문에, 많이 사용하면 할 수록 메모리를 많이 점유하게 됩니다. 그렇다고 반대로 메모리를 위해 적게 지정한다면, 서버에서는 많은 요청을 처리하지 못하고 대기 할 수 밖에 없습니다.

보통 WAS의 Thread의 수가 Conncetion의 수보다 많은 것이 좋은데, 그 이유는 모든 요청이 DB에 접근하는 작업이 아니기 때문입니다.



### 참조

- http://brownbears.tistory.com/289
- [http://devbox.tistory.com/entry/JSP-커넥션-풀-1](http://devbox.tistory.com/entry/JSP-커넥션-풀-1)
- https://d2.naver.com/helloworld/5102792
- https://www.holaxprogramming.com/2013/01/10/devops-how-to-manage-dbcp/