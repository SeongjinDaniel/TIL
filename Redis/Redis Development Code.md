# Redis Development Code



**gradle build**

- lettuce 추가

```
/**
 * redis
 */
implementation group: 'io.lettuce', name: 'lettuce-core', version: '6.1.1.RELEASE'
```



#### **참고할 코드**



#### RedisTest.java

```java
package redis;

import io.lettuce.core.RedisClient;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.api.sync.RedisCommands;

public class RedisTest {
    RedisClient redisClient;
    StatefulRedisConnection<String, String> redisConnection;
    RedisCommands<String, String> redisCommand;

    final String HOSTNAME = "192.168.0.71";
    final String PORT = "6379";

    public int DB_INDEX_TEST0 = 0;
    public final int DB_INDEX_TEST1 = 1;
    public final int DB_INDEX_TEST2 = 2;
    public final int DB_INDEX_TEST3 = 3;
    public final int DB_INDEX_TEST4 = 4;
    public final int DB_INDEX_TEST5 = 5;
    public final int DB_INDEX_TEST6 = 6;
    public final int DB_INDEX_TEST7 = 7;
    public final int DB_INDEX_TEST8 = 8;
    public final int DB_INDEX_TEST9 = 9;
    public final int DB_INDEX_TEST10 = 10;
    public final int DB_INDEX_TEST11 = 11;
    public final int DB_INDEX_TEST12 = 12;
    public final int DB_INDEX_TEST13 = 13;
    public final int DB_INDEX_TEST14 = 14;
    public final int DB_INDEX_TEST15 = 15;

    public void connectRedis() {
        this.redisClient = RedisClient.create("redis://" + HOSTNAME + ":" + PORT + "/");
        this.redisConnection = this.redisClient.connect();
        this.redisCommand = this.redisConnection.sync();
    }

    public void leftRightPush(String message) {
        redisCommand.select(DB_INDEX_TEST7);
        // list의 왼쪽 끝에 value들을 추가합니다.
        redisCommand.lpush("Test", message);
        // list의 오른쪽 끝에 value들을 추가합니다.
//        redisCommand.rpush("Test1", message + "!!!!!!");
//        redisCommand.lpush("Test1", "left" + "!");
//        redisCommand.rpush("Test1", "right" + "!");

    }

    public void pop(String message) {
        redisCommand.select(DB_INDEX_TEST7);
        // list의 왼쪽 끝에 value들을 추가합니다.
        redisCommand.lpush("Test", message);
        // list의 오른쪽 끝에 value들을 추가합니다.
        redisCommand.rpush("Test1", message + "!!!!!!");
    }

    public void setKey(int dbIndex, String key, String value) {
        redisCommand.select(dbIndex);
        redisCommand.set(key, value);
    }

    public void checkKey(int dbIndex, String key) {
        redisCommand.select(dbIndex);
        if (redisCommand.exists(key) == 0) {
            // 해당 key에 대해서 value + 1
            redisCommand.incr(key);
        }
    }
}

```



#### DBRedisTest.java

```java
import redis.RedisTest;
import service.database.TestDatabaseService;

public class DBRedisTest {
    public static void main(String[] args) {
        TestDatabaseService testDatabaseService = new TestDatabaseService();
        RedisTest redisTest = new RedisTest();
        redisTest.connectRedis();
//        redisTest.leftRightPush("success");
        redisTest.setKey(redisTest.DB_INDEX_TEST15, "Test", "success!!");
        redisTest.checkKey(redisTest.DB_INDEX_TEST7, "Test");
    }
}
```