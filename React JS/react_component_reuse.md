# React JS - Component의 분리와 재사용 (관심사의 분리)

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_component_reuse.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EB%B6%84%EB%A6%AC">컴포넌트 분리</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_component_reuse.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EB%B6%84%EB%A6%AC-%EA%B3%BC%EC%A0%95">컴포넌트 분리 과정</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_component_reuse.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EB%B6%84%EB%A6%AC-%EC%98%88%EC%8B%9C">컴포넌트 분리 예시</a>

<br/><br/>

## 컴포넌트 분리

### 관심사의 분리

- 관심사의 분리란 <strong>복잡한 코드를 비슷한 기능을 하는 코드끼리 별도로 관리하는 것</strong>을 말한다.

- 프로그램을 구별된 '개개의 관심사를 해결하는 부분'으로 분리하는 디자인 원칙이다.

- 컴포넌트 별로 관심사를 분리하면 <strong>확장성</strong>과 <strong>재사용성</strong>을 높일 수 있다.

<br/>

### 컴포넌트를 분리하는 이유

- React에서 컴포넌트는 다양한 역할을 한다.

  - 어떤 컴포넌트는 <strong>UI를 표현</strong>하고자 하고, 또 어떤 컴포넌트는 <strong>동작하는 로직</strong>을 담을 수 있다.

  - 위의 두 역할을 모두 담는 컴포넌트 또한 존재하고, 하나도 담지 않는 컴포넌트도 존재할 수 있다.

- 이처럼 컴포넌트는 재사용할 수 있는 최소 UI 단위임에도 불구하고, 웹의 복잡도와 해당 컴포넌트에서 수행하려고 하는 역할에 따라 <strong>얼마든지 복잡해질 수 있다.</strong>

- 따라서 '관심사의 분리' 원칙에 따라 컴포넌트를 분리해서 관리하여야 한다.

<br/>

### 컴포넌트를 분리하는 기준

- 공식 문서의 기준

  - <strong>UI 일부가 여러 번 사용</strong>되거나, <strong>UI 일부가 자체적으로 복잡한 경우</strong> 분리하는 것이 좋다.

- UI로 기준을 잡는 것 외에 프로젝트마다 기준점을 어디에 잡는지에 따라 다양한 컴포넌트 분리 기준이 존재한다.

  - '<strong>View와 로직을 분리</strong>' 또는 '<strong>State에 따라서 분리</strong>' 등등..

- 프로젝트에 적용하기 용이한 적절한 컴포넌트 분리 기준 예시

  - <strong>해당 컴포넌트가 너무 길어서 가독성이 떨어지지 않는지?</strong>

  - <strong>다른 컴포넌트에서 재사용될 수 있는 컴포넌트인지?</strong>

<br/><br/>

## 컴포넌트 분리 과정

- <strong>재사용하고자 하는 컴포넌트의 UI를 보면서 그 중 동일한 요소는 무엇인지, 다른 요소는 무엇인지 파악한다.</strong>

- <strong>다른 요소들을 데이터로 구성한다.</strong>

- <strong>해당 데이터를 하나의 컴포넌트에서 필요한 곳에 사용한다.</strong>

<br/><br/>

## 컴포넌트 분리 예시

### 예시 1

```javascript
/* @jsx React.createElement */
import React, { useState } from "react";
import ReactDOM from "react-dom";

function Counter({ count, onClick }) {
  return (
    <button type="button" onClick={onClick}>
      Click me! ({count})
    </button>
  );
}

function Button({ children }) {
  return <button type="button">{children}</button>;
}

function Buttons() {
  return (
    <p>
      {[1, 2, 3].map((i) => (
        <Button key={i}>{i}</Button>
      ))}
    </p>
  );
}

function Page({ count, onClick }) {
  return (
    <div>
      <p>Counter</p>
      <Counter count={count} onClick={onClick} />
      <Buttons />
    </div>
  );
}

function App() {
  const [state, setState] = useState({
    count: 0,
  });

  const { count } = state;

  function handleClick() {
    setState({
      count: count + 1,
    });
  }

  return <Page count={count} onClick={handleClick} />;
}

ReactDOM.render(<App />, document.getElementById("app"));
```

<br/>

### 예시 2

```js
const isSelectLogin = true;

const LOGIN_DATA = {
  title: "로그인",
  text: "계정이 없으신가요?",
  url: "/signup",
};

const SIGNUP_DATA = {
  title: "회원가입",
  text: "이미 가입하셨나요?",
  url: "/login",
};

return (
  <>
    <p>왓챠피디아 예제</p>
    <User data={isSelectLogin ? LOGIN_DATA : SIGNUP_DATA} />
  </>
);
```

```js
// User.js

const User = ({ data }) => {
  const { title, text, url } = data;

  return (
    <div className="layout">
      <img alt="logo" src="http://~~~" />
      <h1>{title}</h1>
      <form>
        {title === "회원가입" && <input type="text" placeholder="이름" />}
        <input type="email" placeholder="이메일" />
        <input type="password" placeholder="비밀번호" />
      </form>
      <button>{title}</button>
      <Link to={url}>{text}</Link>
    </div>
  );
};

export default User;
```
