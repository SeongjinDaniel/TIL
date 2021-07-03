# Insert selectKey after 예제



```sql
<insert id="insertUser" parameterType="user">
    /* user 테이블은 AUTO_INCREMENT 설정이 되어 있습니다. */
    INSERT INTO user(user_name, column1, column2)
    VALUES (#{userName}, #{column1}, #{column2})

    /* order="AFTER" 삽입 후에 조회 */
    /* INSERT 구문이 실행된 후, 방금 넣은 데이터의 ID를 조회하면 자동으로 DTO 객체에 설정됩니다. */
    <selectKey keyProperty="userId" resultType="int" order="AFTER">
        SELECT LAST_INSERT_ID()
    </selectKey>
</insert>
```



### select key 컬럼 여러 개 사용 (Multiple selectKey)

Mybatis 3.2.6 버전부터는 selectKey에 여러 개 컬럼의 데이터를 조회할 수 있습니다. 여러 개의 컬럼을 가져오기 위해서는 `keyColumn`이라는 속성을 설정해주어야합니다.

```sql
<insert id="insertUser">
    INSERT INTO user(user_id, user_name, column1, column2)
    VALUES (#{userId}, #{userName}, #{column1}, #{column2})

    <selectKey keyColumn="user_id,user_name" keyProperty="userId,userName" resultType="map" order="AFTER">
        SELECT user_id, user_name
        FROM user
        WHERE column1 = #{column1} AND column2 = #{column2}
    </selectKey>
</insert>
```



#### 참조

- https://deeplify.dev/back-end/spring/select-key