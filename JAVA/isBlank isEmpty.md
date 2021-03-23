# isBlank vs isEmpty



#### StringUtils.isBlank: 공백을 빈값으로 처리

```java
StringUtils.isBlank(null)      = true
StringUtils.isBlank("")        = true  
StringUtils.isBlank(" ")       = true  
```



#### StringUtils.isEmpty: 공백을 비어있지 않다고 처리

```java
StringUtils.isEmpty(null)      = true
StringUtils.isEmpty("")        = true  
StringUtils.isEmpty(" ")       = false  
```



#### StrungUtils.isNotEmpty: 공백을 비어있지 않다고 처리

```java
StringUtils.isNotEmpty(" ")    = true
```

