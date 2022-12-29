# CSS-in-JS - <code>styled-components</code>

<br/>

> 참고 자료 : 부트캠프 학습 자료, 노마드 코더

<br/>

### 목차

- <a href="">CSS-in-JS</a>
- <a href="">Styled Components</a>
- <a href="">Styled Components 사용법 및 문법</a>

  - <a href="">컴포넌트의 props 속성값에 따라 서로 다른 스타일 부여하기 - <code>${(props) => props.[props 속성 이름]}</code></a>
  - <a href="">컴포넌트 스타일 확장하기 - <code>styled([컴포넌트])</code></a>
  - <a href="">컴포넌트의 HTML 태그 재설정하기 - <code>as</code> props</a>
  - <a href="">컴포넌트의 HTML 태그에 속성 직접 추가하기 - <code>styled.[태그].attrs({ [속성] })</code></a>
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

## Styled Components 사용법 및 문법

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

### 컴포넌트의 props 속성값에 따라 서로 다른 스타일 부여하기 - <code>${(props) => props.[props 속성 이름]}</code>

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

- 이 문법을 활용하면 중복되는 스타일 코드를 하나로 나타낼 수 있으므로 코드가 더욱 깔끔해진다.

<br/>

### 컴포넌트 스타일 확장하기 - <code>styled([컴포넌트])</code>

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

<br/>

### 컴포넌트의 HTML 태그 재설정하기 - <code>as</code> props

```js
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;
const Btn = styled.button`
  color: white;
  background-color: tomato;
  border: 0;
  border-radius: 15px;
`;

function App() {
  return (
    <Father as="header">
      <Btn>Log In</Btn>
      <Btn as="a" href="/">
        Log In
      </Btn>
    </Father>
  );
}

export default App;
```

```html
<div id="root">
  <header class="sc-dIfARi kqAazX">
    <button class="sc-hHTYSt iKcUmj">Log In</button
    ><a href="/" class="sc-hHTYSt iKcUmj">Log In</a>
  </header>
</div>
```

- 스타일은 그대로 두되, 컴포넌트의 태그를 바꾸고자 할 때 <code>as</code> props를 활용한다.

<br/>

### 컴포넌트의 HTML 태그에 속성 직접 추가하기 - <code>styled.[태그].attrs({ [속성] })</code>

```js
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;
const Input = styled.input.attrs({ required: true, minLength: 10 })`
  background-color: tomato;
`;

function App() {
  return (
    <Father as="header">
      <Input></Input>
      <Input></Input>
      <Input></Input>
      <Input></Input>
      <Input></Input>
    </Father>
  );
}

export default App;
```

```html
<div id="root">
  <header class="sc-fLcnxK hjukqa">
    <input required="" class="sc-bBABsx iPtiKZ" minlength="10" /><input
      required=""
      class="sc-bBABsx iPtiKZ"
      minlength="10"
    /><input required="" class="sc-bBABsx iPtiKZ" minlength="10" /><input
      required=""
      class="sc-bBABsx iPtiKZ"
      minlength="10"
    /><input required="" class="sc-bBABsx iPtiKZ" minlength="10" />
  </header>
</div>
```

<br/>

### styled-components 안에서 애니메이션 추가하기 - <code></code>

- 우선 helper 함수인 <code>keyframes</code>를 import 해주어야 한다.

```js
import styled, { keyframes } from "styled-components";

const Wrapper = styled.div`
  display: flex;
`;

const rotateAnimation = keyframes`
  0% {
    transform: rotate(0deg);
    border-radius: 0px;
  }
  50% {
    transform: rotate(180deg);
    border-radius: 100px;
  }
  100% {
    transform: rotate(360deg);
    border-radius: 0px;
  }
`;

const Box = styled.div`
  height: 200px;
  width: 200px;
  background-color: tomato;
  animation: ${rotateAnimation} 1s linear infinite;
`;

function App() {
  return (
    <Wrapper>
      <Box />
    </Wrapper>
  );
}

export default App;
```

<br/>

### styled-components 가상 선택자

```js
import styled from "styled-components";

const Wrapper = styled.div`
  display: flex;
`;

const Box = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  width: 200px;
  background-color: tomato;

  span {
    font-size: 36px;

    &:hover {
      font-size: 40px;
    }
    &:active {
      opacity: 0;
    }
  }
`;

function App() {
  return (
    <Wrapper>
      <Box>
        <span>🙂</span>
      </Box>
    </Wrapper>
  );
}

export default App;
```

```js
import styled from "styled-components";

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
`;

const Emoji = styled.span``;

const EmojiTwo = styled.span``;

const Box = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  width: 200px;
  background-color: tomato;

  ${Emoji} {
    font-size: 36px;

    &:hover {
      font-size: 90px;
    }
    &:active {
      opacity: 0;
    }
  }

  ${EmojiTwo}:hover {
    font-size: 90px;
  }
`;

function App() {
  return (
    <Wrapper>
      <Box>
        <Emoji>🙂</Emoji>
        <EmojiTwo>🙁</EmojiTwo>
      </Box>
    </Wrapper>
  );
}

export default App;
```

<br/>

### theme

- 모든 색상을 가지고 있는 Object

```js
// index.js
import React from "react";
import ReactDOM from "react-dom/client";
import { ThemeProvider } from "styled-components";
import App from "./App";

const darkTheme = {
  textColor: "whitesmoke",
  backgroundColor: "#111",
};

const lightTheme = {
  textColor: "#111",
  backgroundColor: "whitesmoke",
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <ThemeProvider theme={darkTheme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);
```

```js
// App.js
import styled, { keyframes } from "styled-components";

const Title = styled.h1`
  color: ${(props) => props.theme.textColor};
`;

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background-color: ${(props) => props.theme.backgroundColor};
`;

// ... (코드 생략) ...

function App() {
  return (
    <Wrapper>
      <Title>Hello</Title>
      <Box>
        <Emoji>🙂</Emoji>
        <EmojiTwo>🙁</EmojiTwo>
      </Box>
    </Wrapper>
  );
}

export default App;
```
