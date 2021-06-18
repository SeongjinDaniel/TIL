# @NotBlank 유효성 검사 실패 사례



**@NotBlank**가 동작하지 않아서 어려움이 있었습니다.

우선적으로 @NotBlank가 동작하기 위해서는

`A class -> NotBlank에서 Validation 실행 -> B class` 이런 메커니즘만 허용됩니다. 즉, 제가 실패한 사례는 `A method -> NotBlank 적용 -> B method` 이러한 사례는 실패할 수 있습니다. 위 내용에서 절대 이해가 가지 않으실거라 생각하고, 바로 아래 내용을 확인하시기 바랍니다.

그 이유는 **NotBlank 애노테이션은 상호 Bean 사이에서만 동작할 수 있기 때문입니다.** 문제를 해결했던 부분 @NotBlank Validation을 적용하려고 했지만 적용이 안되서 어떤 매커니즘이 있는지 찾아보았고 @NotBlank는 Bean Validation이라 각 계층에 걸쳐서 적용이 된다는 것을 알았습니다. 여기서 계층이라함은 Presentation Layer, Business Layer, Data Access Layer를 이야기합니다.



아래와 같이 실패한 사례를 이야기 하겠습니다.

#### Controller

```java
public MemberResource register(@RequestBody @Valid MemberResource resource) {
    log.info("[POST] {}", resource);
    Member parameter = memberResourceConverter.to(resource);
    Member added = memberService.add(parameter);
    return memberResourceConverter.from(added);
}
```

- service add메서드를 호출

#### 실패한 Service 코드

```java
@Override
public synchronized Member add(@NotNull Member member) {
    log.debug("[add] {}", member);
    if (!this.validateEmail(member.getEmail())) {
        throw new DuplicateKeyException(member.getEmail());
    }
    final String id = this.generateKey(member.getJoinedAt());
    MemberEntity parameter = memberConverter.to(member);
    parameter.setId(id);
    MemberEntity added = memberRepository.save(parameter);
    log.info("[add] {} added.", added);
    return memberConverter.from(added);
}

private boolean validateEmail(@NotBlank String email) {
    Iterable<MemberEntity> existMemberEntities = this.getMemberEntitiesByEmail(email);
    return !existMemberEntities.iterator().hasNext();
}
```

- 위에서 설명한것과 같이 add method validateEmail을 호출할 때 @NotBlank를 적용하여 @NotBlank 적용에 실패한 사례입니다.

#### 성공한 Service 코드

```java
@Override
public synchronized Member add(@NotNull Member member) {
    log.debug("[add] {}", member);
    if (!this.validateEmail(member.getEmail())) {
        throw new DuplicateKeyException(member.getEmail());
    }
    final String id = this.generateKey(member.getJoinedAt());
    MemberEntity parameter = memberConverter.to(member);
    parameter.setId(id);
    MemberEntity added = memberRepository.save(parameter);
    log.info("[add] {} added.", added);
    return memberConverter.from(added);
}

private boolean validateEmail(String email) {
    validateNotBlankEmail(email);
    Iterable<MemberEntity> existMemberEntities = this.getMemberEntitiesByEmail(email);
    return !existMemberEntities.iterator().hasNext();
}

private void validateNotBlankEmail(String email) {
    Assert.hasText(email, "email 형식으로 입력해주세요.");
}
```

- 위와 같이 적용하여 NotBlank를 적용하면 해결할수 있다는 것을 알게되었습니다.



