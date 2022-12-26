# CSS-in-JS - <code>styled-components</code>

<br/>

> 참고 자료 : 부트캠프 학습 자료, 노마드 코더

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## CSS-in-JS

- 자바스크립트 파일 안에서 CSS를 작성할 수 있는 방법이다.

- 자바스크립트의 상태 값을 공유하여 동적으로 스타일링을 하기 위해 등장한 패러다임이다.

  - 인라일 스타일 이용 or 클래스 명으로 조건부 스타일링 <- 문제점이 있음

    - (전자: 스타일 재사용 X, 후자: 클래스 이름 중복 문제)

<br/>

### CSS-in-JS의 장점

- JS 파일 안에서 CSS 코드를 작성하기 때문에 CSS의 변수와 함수를 그대로 사용할 수 있다.

- 클래스 명이 해시 값으로 치환되기 때문에 클래스 이름의 중복 및 작명에 대한 걱정을 덜 수 있다.

- 현대 웹은 컴포넌트를 기반으로 발전하고 있으므로, 컴포넌트와 스타일을 하나의 파일에서 작성하는 CSS-in-JS는 모듈화가 수월해진다.

<br/><br/>

## Styled Components

- CSS-in-JS에는 여러 종류의 라이브러리가 있는데, 2022년 기준 가장 많이 사용되는 라이브러리가 <code>styled-components</code>이다.

<br/>

### 설치

```
npm install styled-components
```

<br/><br/>

## Styled Components 사용법

```jsx
const [컴포넌트명] = styled.[html태그]`
  [부여하고자 하는 css속성]
`;
```

```jsx
// 사용 예시
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;
const BoxOne = styled.div`
  background-color: teal;
  width: 100px;
  height: 100px;
`;
const BoxTwo = styled.div`
  background-color: tomato;
  width: 100px;
  height: 100px;
`;

function App() {
  return (
    <Father>
      <BoxOne />
      <BoxTwo />
    </Father>
  );
}

export default App;
```

- <strong>vscode-styled-components</strong> 익스텐션 : styled-component css 자동완성 기능 제공

<br/>

### props를 통해 중복되는 스타일 코드 제거하기

```js
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;
const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`;

function App() {
  return (
    <Father>
      <Box bgColor="teal" />
      <Box bgColor="tomato" />
    </Father>
  );
}

export default App;
```

<br/>

### 컴포넌트 스타일 확장하기

```js
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;
const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`;
const Circle = styled(Box)`
  border-radius: 50px;
`;

function App() {
  return (
    <Father>
      <Box bgColor="teal" />
      <Circle bgColor="tomato" />
    </Father>
  );
}

export default App;
```
