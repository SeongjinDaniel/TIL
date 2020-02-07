# Spring Day2

autowire="byName"  : setter
(1) 프로퍼티명과 동일한 명칭의 빈을 찾아서 해당 객체 주입
(2) 없으면 null 주입

autowire="byType"  : setter
(1) 타입으로 찾아서 1개이면 해당 객체 주입
(2) 타입으로 찾아서 2개 이상이면 NoUniqueBeanDefinitionException 발생
(3) 없으면 null 주입

autowire="constructor"  : constructor
(1) 타입으로 찾아서 1개이면 해당 객체 주입
(2) 타입으로 찾아서 2개 이상이면 매개변수명과 동일한 id 값을 갖는 객체 주입
(3) 없으면 null 주입

### sample 6

```

```



