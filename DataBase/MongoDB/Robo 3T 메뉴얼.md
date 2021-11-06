# **Robo 3T 메뉴얼**

### **1. 다음 사이트로 이동**

https://robomongo.org/download

### **2. [Download Robo 3T Only] 클릭**

![image](https://user-images.githubusercontent.com/83576599/140470361-d482808e-e052-43ef-9f06-3fe99c0a28b8.png)

### **3. Email 등 정보 입력 후 다운로드**

![image](https://user-images.githubusercontent.com/83576599/140470406-d7952742-579f-40c5-893a-e716d88b7c98.png)

설치는 그냥 Next …. 계속 누르면 된다.

### **4. 실행**

라이선스 동의해주고, 정보 입력은 그냥 Finish 눌러서 넘어가도 된다.

![image](https://user-images.githubusercontent.com/83576599/140470434-248d1fdf-ed13-4cab-a1a7-49ae19f24344.png)



------

# **2. MongoDB 연결**

### **1. create 클릭**

![image](https://user-images.githubusercontent.com/83576599/140470578-9fdf5689-8c9c-4ed3-84eb-7eb5c52db779.png)

### **2. 서버 관련 정보 작성 및 save**

Name은 해당 커넥션의 이름으로 알아볼 수 있게 마음껏 적으면 된다.
Address는 서버의 주소로 연결하고자 하는 MongoDB 서버의 주소를 적는다.

![image](https://user-images.githubusercontent.com/83576599/140470594-834db00e-fb8b-4fdf-8787-734a01912293.png)

### **3. Connect**

위에서 저장한 연결 정보를 통해 연결한다.

![image](https://user-images.githubusercontent.com/83576599/140470643-89bef6fc-b0e6-470e-a6a3-cf923e9ba4ee.png)

### **4. 연결 완료**

각종 컬렉션을 확인 가능하다.

![image](https://user-images.githubusercontent.com/83576599/140470695-33f715ff-880a-40a0-93f4-3323c3d31fe3.png)

------

# **3. 간단 쿼리 사용법**

### 1. find

```
1db.collection.find( query, projection ) 
```

| **param**  | **mean**                                       | **example**                                                  |
| :--------- | :--------------------------------------------- | :----------------------------------------------------------- |
| query      | 컬렉션에서 찾으려는 데이터 조건을 걸 수 있음   | {name:'AB'} :  name 필드가 AB인 데이터<br />{value:{$gt:160}}: value 필드가 160보다 큰 데이터<br />{value:{$in:[180, 190]}}: value 필드가 180부터 190까지<br /> {$and: [{name:'AB'}, {value: {$gt:160}}]}: name 필드가 AB이고, value가 160보다 큰 데이터 |
| projection | 데이터의 특정 필드만을 보여준다거나 할 수 있음 | 없으면 모든 필드 표기 {item: 1, name : 1}표시할 필드만 쓰거나{item: 0, value : 0} 표시하지 않을 필드만 쓴다. {item : 1, value : 0} 이러면 오류남. |

### 2. 데이터 수정

Robo 3T를 이용하면 데이터를 수정할 수 있다.

![image](https://user-images.githubusercontent.com/83576599/140470708-b659ffff-0f6d-4faa-a764-4d816ad50714.png)



| parameter  | Type     | 설명                                                         |
| :--------- | :------- | :----------------------------------------------------------- |
| query      | document | Optional(선택적). 다큐먼트를 조회할 때 기준을 정합니다. 기준이 없이 컬렉션에 있는 모든 다큐먼트를 조회 할때는 이 매개변수를 비우거나 비어있는 다큐먼트 { } 를 전달하세요. |
| projection | document | Optional. 다큐먼트를 조회할 때 보여질 field를 정합니다.      |