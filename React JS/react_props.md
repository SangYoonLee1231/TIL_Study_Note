# React JS - Props

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## Props란?

- Props는 컴포넌트의 속성값이다.

- Props는 부모 컴포넌트로부터 전달받은 데이터를 지니고 있는 객체이다.

- Props를 이용하면 부모 컴포넌트에서 자식 컴포넌트에게 어떤 값이든 (문자, 숫자, 변수, 함수 등) 전달할 수 있다.

<br/><br/>

## State와 Props를 함께 활용하기

```js
// Parents.js
import React, { useState } from "react";
import Child from "./Child";

const Parent = () => {
  const [color, setColor] = useState("blue");

  const changeColor = () => {
    setColor("green");
  };

  return (
    <>
      <div>부모 컴포넌트</div>
      <Child color={color} changeColor={changeColor} />
    </>
  );
};

export default Parent;
```

```js
// Child.js
import React from "react";

const Child = (props) => {
  return (
    <>
      <div>자식 컴포넌트</div>
      <p>{props.color}</p>
      <button onClick={props.changeColor}>색상 바꾸기</button>
    </>
  );
};

export default Child;
```

- 자식 컴포넌트에서 발생한 이벤트로 부모 컴포넌트의 state가 변경되었고, 그 변경된 값이 다시 자식 컴포넌트에 반영되었다. 이를 <strong>State 끌어올리기</strong>라 한다.

<br/>

- <strong>데이터의 단방향성</strong>

  - 데이터는 부모 컴포넌트에서 자식 컴포넌트로 흐른다. 즉 자식에서 부모로 데이터가 이동할 수 없다.

  - 만일 자식 컴포넌트에서 State를 선언했다면 부모 컴포넌트에서 이 데이터를 사용할 방법이 없다. 따라서 부모 컴포넌트에서 State를 선언하고 Prop를 통해 자식 컴포넌트로 데이터를 흘려주는 방식을 사용하는 것이다.
