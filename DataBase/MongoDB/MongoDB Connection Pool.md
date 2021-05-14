# MongoDB Connection Pool



몽고디비는 자체 내부적으로 만들어 사용한다고 한다. 그러니까 기본적으로 따로 설정 하지 않아도 그냥 생성만 하면 내부적으로 필요한 만큼 알아서 생성 한다. *하지만 연결 요청이 많거나 자신이 직접 설정하고 싶다면 밑에서 확인해보자*

```java
import com.mongodb.MongoClientOptions.Builder;

Builder options = new Builder();
    Builder options() 
    {
         options.connectionsPerHost(30); // 시작 시 30개의 커넥션을 만들어둔다
         options.minConnectionsPerHost(20); // 최소 10개를 유지한다
         return options;
    }
```



#### 참조

- https://datamod.tistory.com/18
- https://datamod.tistory.com/19

- [MongoDB - 커넥션 풀 (Connection Pool)](https://cho1-w0n-san9.tistory.com/16)

