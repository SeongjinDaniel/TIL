# ObjectNode and JsonNode



Json으로 나타난 정보에서



**[ ]** 표시로 시작되는 건 배열이기 때문에 Arraynode 이며 **{ }** 표시로 시작하는 건 Json 값이기 때문에 JsonNode 이다.

그런데 JsonNode는 값을 불러올 수는 있지만 넣을 수는 없기 때문에 값을 넣기 위해서는 ObjectNode를 사용한다. ObjectNode는 값을 불러오고 넣을 수도 있다.



**결론**

 JsonNode는 값을 읽을 수만 있고 **ObjectNode는 값을 읽고 쓸 수 있다.**

#### 참조

- https://yonoo88.tistory.com/135