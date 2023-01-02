# TypeScript - 타입 설명 방식

> 참고 자료 : <a href="https://nomadcoders.co/react-masterclass">노마드 코더 - React JS 마스터클래스</a>

<br/>

### 목차

- <a href="">직접 타입을 정의하는 방식</a>
- <a href="">인터페이스 (interface) 방식</a>

<br/><br/>

## 직접 타입을 정의하는 방식

```ts
const x = (a: number, b: number) => a + b;
```

<br/>

## 인터페이스 (interface) 방식

- TypeScript에게 객체 (Object) 의 타입을 설명해주는 틀이다.

  ```ts
  interface PlayerShape {
    name: string;
    age: number;
  }

  const sayHello = (playerObj: PlayerShape) =>
    `Hello ${playerObj.name}. You are ${playerObj.age} yeats old.`;

  sayHello({name: "SangYoonLee", age: 25});
  sayHello({name: "SangYoonLee", age: 25,  hello: 1}); // 에러 발생!
  sayHello({name: "SangYoonLee", age: "25"}, hello: 1); // 에러 발생!
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
