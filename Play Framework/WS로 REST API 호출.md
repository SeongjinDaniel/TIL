# WS로 REST API 호출



때때로 우리는 Play 애플리케이션 내에서 다른 HTTP 서비스를 호출하고 싶습니다. Play는 비동기 HTTP 호출을 수행하는 방법을 제공하는 [WS ( 'WebService') 라이브러리](https://www.playframework.com/documentation/2.8.x/api/java/play/libs/ws/package-summary.html) 를 통해이를 지원 합니다.

WS API 사용에는 두 가지 중요한 부분, 즉 요청 작성과 응답 처리가 있습니다. 먼저 GET 및 POST HTTP 요청을 만든다.



HTTP 요청을 작성하려면로 시작 `ws.url()`하여 URL을 지정합니다.

```java
import javax.inject.Inject;

import play.mvc.*;
import play.libs.ws.*;
import java.util.concurrent.CompletionStage;

public class MyClient implements WSBodyReadables, WSBodyWritables {
  private final WSClient ws;

  @Inject
  public MyClient(WSClient ws) {
    this.ws = ws;
  }
  // ...
}
```



```java
WSRequest request = ws.url("http://example.com");
```



#### 참조

- [Calling REST APIs with Play WS](https://www.playframework.com/documentation/2.8.x/JavaWS)