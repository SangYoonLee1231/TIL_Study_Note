# TypeScript - 타입 설명 방식

> 참고 자료 : <a href="https://nomadcoders.co/react-masterclass">노마드 코더 - React JS 마스터클래스</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/typescript_explain_type.md#%EC%A7%81%EC%A0%91-%ED%83%80%EC%9E%85%EC%9D%84-%EC%A0%95%EC%9D%98%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D">직접 타입을 정의하는 방식</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/typescript_explain_type.md#%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-interface-%EB%B0%A9%EC%8B%9D">인터페이스 (interface) 방식</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/typescript_explain_type.md#optional-props-%EC%84%A0%ED%83%9D%EC%A0%81%EC%9D%B8-props">Optional Props (선택적인 Props)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/typescript_explain_type.md#usestate%EC%95%A0%EC%84%9C%EC%9D%98-typescript">useState애서의 TypeScript</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/typescript_explain_type.md#event-%EA%B0%9D%EC%B2%B4%EC%97%90-%ED%83%80%EC%9E%85%EC%9D%84-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0">event 객체에 타입을 추가하기</a>
<!-- - <a href=""></a> -->

<br/><br/>

## 직접 타입을 정의하는 방식

```ts
const x = (a: number, b: number) => a + b;
```

<br/><br/>

## 인터페이스 (interface) 방식

- TypeScript에게 객체 (Object) 의 타입을 설명해주는 틀이다.

  ```ts
  interface PlayerShape {
    name: string;
    age: number;
  }

  const sayHello = (playerObj: PlayerShape) =>
    `Hello ${playerObj.name}. You are ${playerObj.age} yeats old.`;

  sayHello({ name: "SangYoonLee", age: 25 });
  sayHello({ name: "SangYoonLee", age: "25" }); // 에러 발생!
  ```

- 실제 React 코드 예시를 살펴보자.

  ```ts
  import styled from "styled-components";

  const Container = styled.div`
    ... (코드 생략) ...
  `;

  interface CircleProps {
    bgColor: string;
  }

  function Circle(props: CircleProps) {
    return <Container bgColor={props.bgColor} />;
  }

  export default Circle;
  ```

  - 아래처럼 구조분해 할당을 이용하여 작성해도 괜찮다.

  ```js
  function Circle({ bgColor, x }: CircleProps) {
    return <Container bgColor={bgColor} />;
  }
  ```

<br/>

- <code>styled-components</code>에서 해당 컴포넌트의 props를 사용하려면 (+ 타입 설명), 새 interface를 생성하여 다음과 같이 코드를 작성해주면 된다.

  ```ts
  import styled from "styled-components";

  interface ContainerProps {
    bgColor: string;
  }

  const Container = styled.div<ContainerProps>`
    width: 200px;
    height: 200px;
    background-color: ${(props) => props.bgColor};
    border-radius: 100px;
  `;

  interface CircleProps {
    bgColor: string;
  }

  function Circle({ bgColor }: CircleProps) {
    return <Container bgColor={bgColor} />;
  }

  export default Circle;
  ```

<br/><br/>

## Optional Props (선택적인 Props)

- interface에서 정의한 props은 반드시 들어가야 하는 required(필수적인) props이다.

- 만일 들어가도 되고 안들어가도 괜찮은 optional한(선택적인) props를 정의하려면 `?`를 붙여주면 된다.

  ```ts
  interface CircleProps {
    bgColor: string; // required
    borderColor?: string; // optional
    text?: string; // optional
  }
  ```

<br/><br/>

## useState애서의 TypeScript

- TypeScript는 똑똑해서 **state의 초기값을 바탕으로 타입을 추론할 수 있다.**

- 다만 state에 2가지 이상의 타입을 지정하기 위한 용도로 state에 type을 지정하려면, Generics안에 지정해주면 된다.

  ```ts
  function Circle({
    bgColor,
    borderColor,
    text = "default text",
  }: CircleProps) {
    /* TS는 counter의 타입을 number으로 알아서 추론한다. */
    const [counter, serCounter] = useState(1);
    /* state에 type 지정하기 */
    const [value, setValue] = useState<number | string>(1);
    serCounter(2);
    setValue("hello");

    return (
      <Container bgColor={bgColor} borderColor={borderColor ?? "white"}>
        {text}
      </Container>
    );
  }
  ```

- state에 초기값을 지정 시 TS가 자동으로 타입을 유추하기 때문에 굳이 state에 타입을 직접 지정해주지 않아도 되지만, 다음과 같은 상태일 때는 지정해주는 것이 좋다.

  - state의 상태가 undefined 또는 null이 될 수 있음

  - state에 객체 또는 배열이 저장되는 상황

<br/><br/>

## event 객체에 타입을 추가하기

- 다음과 같이 코드를 작성하여 구현할 수 있다.

  ```ts
  import React, { useState } from "react";

  function App() {
    const [value, setValue] = useState("");
    /* 주목 */
    const onChange = (event: React.FormEvent<HTMLInputElement>) => {
      // console.log(event.currentTarget.value);
      const {
        currentTarget: { value },
      } = event;
      setValue(value);
    };
    /* 주목 */
    const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      console.log("hello", value);
    };

    return (
      <div>
        <form onSubmit={onSubmit}>
          <input
            value={value}
            onChange={onChange}
            type="text"
            placeholder="username"
          />
          <button>Log in</button>
        </form>
      </div>
    );
  }

  export default App;
  ```

<br/><br/>
