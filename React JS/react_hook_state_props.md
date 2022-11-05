# React JS - Hook & State & Props

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="">Hook이란?</a>

- <a href="">State란?</a>
- <a href="">State의 Modifier 함수</a>
- <a href="">Props란?</a>
- <a href="">State와 Props를 함께 활용하기</a>

<br/><br/>

## Hook이란?

- Hook은 클래스 컴포넌트에서만 사용할 수 있었던 <strong>상태 관리</strong>와 <strong>라이프 사이클 관리 기능</strong>을 함수 컴포넌트에서도 사용할 수 있도록 연동해주는 함수를 의미한다.

- 미리 만들어 둔 함수를 가져와서 사용을 해 주는 것이기 때문에 Hook이라는 이름을 사용한다.

- Hook의 모음을 Hooks라 한다.

<br/>

### Hook의 등장 배경

- 기존엔 클래스 컴포넌트만을 사용하여 컴포넌트를 생성하였는데, 함수 컴포넌트의 장점으로 인해 이를 사용하고자 하는 니즈가 점점 많아지게 되었다.

  - <strong>함수 컴포넌트의 장점</strong> : 선언하기 편리함, 직관적, 메모리 자원을 덜 사용함

- 이로 인해 <strong>클래스 컴포넌트에서만 가능했던 기능을 함수 컴포넌트에서도 사용하고자</strong> Hook이 등장하였다.

<br/><br/>

### Hook의 특징

- <strong>함수 컴포넌트에서만 사용 가능하다.</strong>

- <strong>Hook의 이름은 반드시 <code>use-</code>로 시작한다.</strong>

  따라서 함수 이름을 보고 Hook임을 짐작할 수 있다.

- <strong>내장 Hook이 존재한다. (<code>useState</code>, <code>useEffect</code>)</strong>

  이런 Hook들은 외부 라이브러리 설치 없이 사용할 수 있다.

- <strong>직접 Hook을 만들어 사용할 수도 있다.</strong> 이를 <strong>Custom Hook</strong>이라 한다.

<br/>

### Hook의 사용 규칙

- Hook은 <strong>함수 컴포넌트 혹은 Custom Hook 안에서만 호출할 수 있다.</strong>

  그 외의 장소에서는 Hook을 사용할 수 없다.

- Hook은 <strong>함수 컴포넌트 내의 최상위(at the top level) 에서만 호출해야 한다.</strong>

  반복문, 조건문 등 중첩 함수 내에서는 Hook을 호출할 수 없다.

<br/><br/><br/>

## State란?

- 컴포넌트 내부에서 가지고 있는 컴포넌트의 상태값

- 컴포넌트 내에서 정의하고 사용하며, 변수처럼 얼마든지 변경할 수 있다.

<br/><br/>

## <code>React.useState()</code> 함수

- <strong>React의 내장 Hook</strong>으로, React에서 변수를 다루는 유용한 방법이다.

- Hook이기 때문에 <strong>반드시 컴포넌트 내부에서만 사용할 수 있다.</strong>

<br/>

- <code>React.useState()</code> 호출 시 '<strong>변수값</strong>'과 '<strong>modifier 함수</strong>' 2개의 원소가 배열로 묶여 반환된다.

  ```javascript
  const root = document.getElementById("root");

  const App = () => {
    // 주목할 부분!!
    const data = React.useState(0);
    console.log(data);
    // 여기까지!!

    return (
      <div>
        <h3>Total clicks: {counter}</h3>
        <button>Click Me</button>
      </div>
    );
  };
  ReactDOM.render(<App />, root);
  ```

  ```
  [undefined, f ]
  ```

  - 첫 번째 요소 : <strong>undefined</strong>

    ➡️ 데이터 (변수)

  - 두 번째 요소 : <strong>f</strong>

    ➡️ 데이터를 바꾸는 Modifier 함수

<br/>

- <strong><a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9">구조분해할당</a></strong>을 활용하면 좀 더 효율적으로 코드를 작성할 수 있다.

  ```javascript
  const root = document.getElementById("root");

  const App = () => {
    // 주목할 부분!!
    const [counter, setCounter] = React.useState(0);

    const onClick = () => {
      setCounter(counter + 1);
    };
    // 여기까지!!

    return (
      <div>
        <h3>Total clicks: {counter}</h3>
        <button onClick={onClick}>Click Me</button>
      </div>
    );
  };
  ReactDOM.render(<App />, root);
  ```

<br/>

- ✨ <strong>modifier 함수를 통해 state(값)을 변경하면 컴포넌트가 새 값을 가지고 재생성 (리랜더링) 된다.</strong>

  이것이 React에서 변수 대신 <strong>State를 사용하는 이유</strong>이다.

<br/><br/><br/>

## State의 Modifier 함수

- <strong>setState 함수는 비동기적으로 동작한다.</strong> 따라서 의도한 대로 동작하지 않을 수 있다.

  - 관련 내용에 대해 정리한 블로그 포스트 👉<a href="https://sylagape1231.tistory.com/61">바로가기</a>

- state 변경 시 이전 값을 바탕으로 현재 값을 설정하는 더 안전한 방법은 <strong>함수를 사용하는 것</strong>이다.

  ```javascript
  // 덜 안전한 방법
  const [counter, setCounter] = React.useState(0);

  const onClick = () => {
    setCounter(counter + 1);
  };
  ```

  ```javascript
  // 더 안전한 방법 - 함수 사용
  const [counter, setCounter] = React.useState(0);

  const onClick = () => {
    setCounter((current) => current + 1);
  };
  ```

- 함수를 사용하면 state 값이 외부에서 변경되는 경우로 인해 예상과 다른 결과가 나오는 상황을 대비할 수 있다.

<br/>

- ❓ modifier 함수 (setState 함수) 내에 변수 명을 current로 설정해도 무방한 이유

  - setState는 그 인자값이 객체인지 함수인지 판별하는 부분이 있다. 만일 함수일 경우 알아서 현재 state값을 찾아 매핑해준다.

<br/><br/>

### State 활용하기

#### <code>input</code>에 활용하기

- <strong>시간 / 분 단위 변환기</strong>

  ```javascript
  const App = () => {
    const [amount, setAmount] = React.useState(0);
    const [inverted, setInverted] = React.useState(false);

    const onChange = (event) => {
      setAmount(event.target.value);
    };

    const onFlip = () => {
      setInverted((inverted) => !inverted);
      reset();
    };

    const reset = () => setAmount(0);

    return (
      <div>
        <h1>Super Converter</h1>
        <div>
          <label htmlFor="minutes">Minutes</label>
          <input
            value={inverted ? amount : amount * 60}
            id="minutes"
            placeholder="Minutes"
            type="number"
            onChange={onChange}
            disabled={!inverted}
          />
        </div>
        <div>
          <label htmlFor="hours">Hours</label>
          <input
            value={inverted ? Math.floor(amount / 60) : amount}
            id="hours"
            placeholder="Hours"
            type="number"
            onChange={onChange}
            disabled={inverted}
          />
        </div>
        <button onClick={reset}>Reset</button>
        <button onClick={onFlip}>Flip</button>
      </div>
    );
  };

  ReactDOM.render(<App />, root);
  ```

<!-- <br/>

- <strong>업그레이드 단위 변환기 (기능 선택 옵션 추가)</strong>

  ```javascript
  const MinutesToHours = () => {
    // (코드 생략)
  };
  const KmToMiles = () => {
    // (코드 생략)
  };
  const App = () => {
    const [index, setIndex] = React.useState("xx");
    const onSelect = (event) => {
      setIndex(event.target.value);
    };
    return (
      <div>
        <h1>Super Converter</h1>
        <select value={index} onChange={onSelect}>
          <option value="xx">Select Your Units</option>
          <option value="0">Minutes & Hours</option>
          <option value="1">Km & Miles</option>
        </select>
        <hr />
        {index === "xx" ? "Please select your units" : null}
        {index === "0" ? <MinutesToHours /> : null}
        {index === "1" ? <KmToMiles /> : null}
      </div>
    );
  };
  ReactDOM.render(<App />, root);
  ``` -->

<br/><br/><br/>

## Props란?

- Props는 <strong>컴포넌트의 속성값</strong>이다.

- Props는 <strong>부모 컴포넌트로부터 전달받은 데이터를 지니고 있는 객체</strong>이다.

- ✨ Props를 이용하면 부모 컴포넌트에서 자식 컴포넌트에게 어떤 값이든 (문자, 숫자, 변수, 함수 등) 전달할 수 있다.

<br/><br/>

## ✨ State와 Props를 함께 활용하기

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
