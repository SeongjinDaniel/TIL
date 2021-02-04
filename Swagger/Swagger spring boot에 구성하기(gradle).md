# Swagger 구성



#### Swagger 의존성 추가

```json
ext {
    setProperty("springfoxSwaggerVersion", "3.0.0")//버전은 알아서..
    setProperty("springfoxBootStarterVersion", "3.0.0")//버전은 알아서..
}

dependencies {
	...
	implementation("io.springfox:springfox-swagger2:${springfoxSwaggerVersion}")
	implementation("io.springfox:springfox-boot-starter:${springfoxBootStarterVersion}")
	...
}
```

#### SpringFoxConfig 클래스 생성

```java
@Configuration
@EnableSwagger2
public class SpringFoxConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.basePackage("inc.sdt.hr")) // 현재  / inc.sdt.hr/**인 url들만 필터링해서 RequestMapping으로 할당된 모든 URL 리스트를 추출
                .paths(PathSelectors.any())
                .build()
                .useDefaultResponseMessages(false)
                .apiInfo(apiInfo());
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("SDT Human Resource Management API")
                .description("SDT 사내 업무지원 시스템")
                .build();
    }
}
```



일반 Spring 프로젝트에서는 Swagger 2를 명시 적으로 활성화해야합니다. 이렇게하려면 **구성 클래스** **에서 @ EnableSwagger2WebMvc 를 사용해야합니다** .

```java
@Configuration
@EnableSwagger2WebMvc
public class SpringFoxConfig {                                    
}
```



### apis(RequestHandlerSelectors.basePackage("패키지명"))

- Swagger를 적용할 패키지를 지정할 수 있다.

- [springfox_github_issues_3620](https://github.com/springfox/springfox/issues/3620)

  > I have been informed that @EnableSwagger2 is no longer used as of Swagger 3.0.0. I have been then told to use @EnableSwagger2WebMvc, but that has been deprecated. I haven't been able to find anywhere what to use instead of these two. Can anyone inform me?

  @ EnableSwagger2는 Swagger 3.0.0부터 더 이상 사용되지 않는다는 알림을 받았습니다. 그런 다음 @ EnableSwagger2WebMvc를 사용하라는 지시를 받았지만 더 이상 사용되지 않습니다. 나는 이 두 가지 대신에 무엇을 사용할지 어디에서도 찾을 수 없었다. 누구든지 내게 알릴 수 있습니까?

  > @EnableOpenApi

### ApiInfo

API정보를 담을 수 있게 해주는 객체

### ApiInfoBuilder

ApiInfo 객체의 값을 초기화 하고 생성시켜주는 Builder

### ApiInfoBuilder의 메서드

- ApiInfoBuilder **contact (Contact contact)**
  - 이 api를 담당하는 사람의 연락처 정보 초기화

- ApiInfoBuilder **description (String description)**
  - api설명 초기화
- ApiInfoBuilder **extensions (List<VendorExtension> extensions)**
  - api에 대한 확장을 추가 (?)

- ApiInfoBuilder license (String license)
  - api 라이선스 정보 초기화
- ApiInfoBuilder licenseUrl (String licenseUrl)
  - api 라이선스 URL 초기화
- ApiInfoBuilder termsOfServiceUrl (String termsOfServiceUrl)
  - 서비스 약관 URL 초기화
- ApiInfoBuilder title (String title)
  - api 제목 초기화
- ApiInfoBuilder version (String version)
  - api 버전 정보 초기화





---

### **9.1. Swagger의 응답을위한 필터링 API**

전체 API에 대한 문서를 노출하는 것이 항상 바람직하지는 않습니다. *Docket* 클래스 의 ***apis ()*** 및 ***paths ()*** 메서드에 매개 변수를 전달하여 Swagger의 응답을 제한 할 수 있습니다 .

위에서 볼 수 있듯이 *RequestHandlerSelectors* 는 *any* 또는 *none* 조건자를 사용할 수 있지만 기본 패키지, 클래스 주석 및 메서드 주석에 따라 API를 필터링하는 데 사용할 수도 있습니다.

***PathSelectors*** 는 애플리케이션의 요청 경로를 스캔하는 술어로 추가 필터링을 제공합니다. 우리가 사용할 수 *있는 ()* , *없음 (),* *정규식 ()* , 또는 *개미 ()* .

아래 예제에서는 *ant ()* 술어를 사용하여 특정 경로가있는 특정 패키지의 컨트롤러 만 포함하도록 Swagger에 지시합니다 .

```java
@Bean
public Docket api() {                
    return new Docket(DocumentationType.SWAGGER_2)          
      .select()                                       
      .apis(RequestHandlerSelectors.basePackage("com.baeldung.web.controller"))
      .paths(PathSelectors.ant("/foos/*"))                     
      .build();
}
```



- #### 참조

  - https://www.baeldung.com/swagger-2-documentation-for-spring-rest-api