# Validation



|           | null        | ""          | " "         |
| --------- | ----------- | ----------- | ----------- |
| @NotNull  | **Invalid** | **Valid**   | **Valid**   |
| @NotEmpty | **Invalid** | **Invalid** | **Valid**   |
| @NotBlank | **Invalid** | **Invalid** | **Invalid** |



#### 참고

- [@Valid 를 이용해 @RequestBody 객체 검증하기](https://jyami.tistory.com/55)

