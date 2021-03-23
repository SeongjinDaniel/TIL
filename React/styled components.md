# styled-components



클래스명을 실수로 중복으로 만들어 놓고 또 CSS를 해버리는 실수를 방지할 수 있다.

**CSS in JS**라고도 한다.



#### 설치 command

```
yarn add styled-componen
또는
npm install styled-components
```



#### import

```react
import styled from 'styled-components';

// 미리 생성 스타일을 입혀서 적용시킨다.
let 박스 = styled.div`
	padding : 20px;
`;

<박스>wow</박스>
```

