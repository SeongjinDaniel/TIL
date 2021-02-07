# Swegger Annotation



#### @ApiInfo

- API정보를 담을 수 있게 해주는 객체

```java
@Api(tags = "직원 정보 관리")
```



#### @ApiOperation

- 특정 경로에 대한 작업 또는 일반적으로 HTTP 메서드를 설명합니다.
- 동등한 경로가있는 작업은 단일 작업 개체로 그룹화됩니다. HTTP 메서드와 경로의 조합은 고유 한 작업을 만듭니다.
- https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiOperation.html

```java
@ApiOperation(value = "직원 추가", notes = "직원 정보를 입력해 직원을 추가할 수 있습니다.")
```



#### @ApiImplicitParam

- API 작업에서 단일 매개 변수를 나타냅니다.
- [`ApiParam`](https://docs.swagger.io/swagger-core/current/apidocs/io/swagger/annotations/ApiParam.html)JAX-RS 매개 변수, 메소드 또는 필드에 바인드되는 동안 이를 통해 미세 조정 된 방식으로 매개 변수를 수동으로 정의 할 수 있습니다. 이것은 Servlet 또는 기타 비 JAX-RS 환경을 사용할 때 매개 변수를 정의하는 유일한 방법입니다.

- 이 주석은 [`ApiImplicitParams`](https://docs.swagger.io/swagger-core/current/apidocs/io/swagger/annotations/ApiImplicitParams.html) 구문 분석을 위해 값으로 사용되어야합니다 .
- https://docs.swagger.io/swagger-core/current/apidocs/io/swagger/annotations/ApiImplicitParam.html

```java
@ApiImplicitParam(name = "resource", value = "추가할 직원 정보", paramType = "body", dataType = "inc.sdt.hr.api.employee.member.MemberResource")
```



#### @ApiResponse

- 작업의 가능한 응답을 설명합니다.
- REST API 호출에서 가능한 성공 및 오류 코드를 설명하는 데 사용할 수 있습니다. 작업의 반환 유형을 설명하는 데 사용하거나 사용하지 않을 수 있지만 (일반적으로 성공적인 코드), 성공적인 응답은 [`ApiOperation`](https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiOperation.html).
- API가 이러한 응답에 대해 다른 응답 클래스를 사용하는 경우 여기에서 응답 클래스를 응답 코드와 연결하여 설명 할 수 있습니다. Swagger는 단일 응답 코드에 대해 여러 응답 유형을 허용하지 않습니다.
- 이 주석은 직접 사용되지 않으며 Swagger에서 구문 분석하지 않습니다. 내에서 사용해야합니다 [`ApiResponses`](https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiResponses.html).

- https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiResponse.html



#### @ApiModel

- Swagger 모델에 대한 추가 정보를 제공합니다.

- 클래스는 작업의 유형으로 사용되므로 자동으로 검사되지만 모델의 구조를 조작 할 수 있습니다.
- https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiModel.html



#### @ApiModelProperty

- 모델 속성의 데이터를 추가하고 조작합니다.

- https://docs.swagger.io/swagger-core/v1.5.0/apidocs/io/swagger/annotations/ApiModelProperty.html