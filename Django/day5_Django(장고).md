# day5 django



### POST

- 사용자는 DJANGO에게 'html파일 줘!(GET)'가 아니라 '~한 레코드(글)을 생성해줘!(POST)'이기 때문에 http method POST를 사용해야 한다.
- 데이터는 URL에 직접 노출되서는 안된다. (우리가 URL에 접근하는 방식은 모두 get요청) / query의 형태를 통해 DB 구조(schema)를 유추할 수 있고 이는 보안적인 측면에서 매우 취약하다.
- DB를 조작하는 친구는 GET이 아닌 POST! 왜? 중요한 요청이기 때문에 **최소한의 신원 확인**이 필요!

---

### READ (DETAIL)

