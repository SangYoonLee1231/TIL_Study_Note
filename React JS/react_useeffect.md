# React JS - Side Effect와 useEffect

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="">Side Effect란?</a>

- <a href="">Side Effect가 있는 함수</a>
- <a href="">Side Effect는 기피해야 하는 대상일까?</a>
- <a href="">React에서의 Side Effect</a>
- <a href="">React에서 Side Effect의 올바른 발생 시점</a>
- <a href="">useEffect</a>
- <a href="">Clean Up Effect</a>

<br/><br/>

## Side Effect란?

- Side Effect란 <strong>부작용</strong>이다.

- <strong>부작용 === 부수효과</strong>

  - <strong>부수효과</strong> : 주요한 효과에 따라서 발생하는 부수적인 효과

- <strong>부작용이란 용어 자체는 부정적인 의미를 내포하지 않는다.</strong> 단지 부수적으로 발생하는 효과를 의미하는 단어이다.

<br/>

### 프로그래밍에서 Side Effect (부작용) 란?

- 코드가 의도한 주된 효과 외에 <strong>추가적으로 발생하는 부수 효과</strong>

- 특히 프로그램을 구성하는 가장 작은 단위인 <strong>함수</strong>에서 자주 사용되는 용어

  - 함수의 본질적인 역할 (주된 효과)

    - Input을 받아서 Output을 산출하는 것

    - Input => Output

  - 함수의 부작용 (Side Effect)

    - <strong>Input을 받아서 Output을 산출하는 것 외의 모든 행위</strong>

      - 함수에서 함수 외부의 값을 읽어오는 행위

      - 함수에서 함수 외부의 값을 변경하는 행위

<br/><br/>

## Side Effect가 있는 함수

```js
const sun = (x) => {
  return x + 1;
};
```

- x를 입력받아서 x+1을 출력하는 함수

- Input을 받아서 Output을 내는 행위 외에 다른 행위를 하지 않으므로, 위 함수는 Side Effect가 없는 순수함수이다.

  - 순수 함수 : Side Effect가 없는 함수

<br/>

```js
const num = 1;

const sum = (x) => {
  num = x + 1;
  return num;
};
```

- 위 예시처럼 함수가 함수 내부의 값이 아닌 외부의 값을 읽어오거나 변경할 때 Side Effect가 있다고 표현할 수 있다.

<br/>

```js
const printNum = (x) => {
  console.log(x);
};
```

```js
const changeTitle = (newTitle) => {
  const title = document.getElementById("title");

  title.innerText = newTitle;
};
```

- 외부의 값 !== 외부의 변수

- 콘솔 패널에 문자를 출력하는 행위, DOM을 조작하는 행위 또한 함수 외부에 존재하는 DOM, 콘솔 상태를 변경시키는 것이다.

- 따라서 위 두 함수는 모두 Side Effect가 있는 함수이다.

<br/><br/>

## Side Effect는 기피해야 하는 대상일까?

- <strong>프로그래밍에서 Side Effect는 기피해야 하는 대상</strong>이다. 그 이유는..

  - Side Effect가 있는 함수는 동작 결과를 예측하기 어렵게 만든다.

  - 이는 곧 프로그래밍이 어떻게 동작할 지 예측하기 힘들게 만들어 유지 보수의 어려움도 야기한다.

- 하지만 프로그래밍에서 외부의 값을 읽어오거나 변경하는 행위를 <strong>완전히 무시할 순 없다.</strong> 오히려 프로그래밍에 반드시 있어야 하는 동작이다.

- <strong>따라서 개발자들은 Side Effect를 최소화하면서 프로그램을 설계하되, Side Effect를 적재적소에 사용하고 통제할 수 있도록 하여, 관리 시 예측 가능하고 유지 보수하기 쉬운 프로그램을 만들어야 한다.</strong>

<br/><br/>

## React에서의 Side Effect

### 함수 컴포넌트의 Input과 Output

- React에서 렌더링이란 state, props를 기반으로 UI를 그려내는 행위이다.

- React에서는 함수 컴포넌트를 통해 만든 컴포넌트를 조합하여 UI를 만들어낸다.

- 즉 React의 함수 컴포넌트는 state, props를 통해서 JSX를 만들어 내는 것이 본질적인 역할이다.

  - Input : state, props

  - Output : JSX

  - (state, props) => JSX

<br/>

### 함수 컴포넌트의 Side Effect

- React에서 함수 컴포넌트의 Side Effect는 함수 컴포넌트의 본질적인 역할 외 모든 행위를 의미한다.

  - <strong>Data Fetching</strong>

  - <strong>DOM 접근 및 조작</strong>

  - <strong>구독 (Subscribe)</strong>

<br/>

### Data Fetching

- 프론트엔드가 백엔드 API를 통해 필요한 데이터를 받아오는 행위로, 프론트와 백의 역할이 분리된 현대 개발에서 필수적인 행위이다.

- 하지만, 이 역시 외부에서 데이터를 가져오는 것이므로 Side Effect이다.

<br/>

### DOM 접근 및 조작

- 프론트엔드에서 웹 개발 시 DOM에 접근 및 조작하는 행위는 필수적이다.

- 그러나 React의 선언적인 개발 방식(DOM 조작을 직접 React에서 처리함)으로 인해, 이제 개발자가 직접 DOM에 접근할 일은 많지 않고 권장되지도 않는다.

- 하자만 특정 상황에서 직접 DOM(외부의 값)을 읽고 변경하는 일은 여전히 존재한다.

<br/>

### 구독 (Subscribe)

- 프로그래밍에서 구독이란 어떤 것을 계속 관찰하다가 변화가 생길 시 특정한 액션을 취하는 것이다.

- 개발에서 구독을 활용하는 보편적 예시는 "시간을 구독하는 것"이다.

- 시간은 계속해서 변하기에, 특정 시간이 지났을 때 액션을 취하거나(<code>setTimeout</code> 매서드), 특정 시간 주기마다 액션을 취하는(<code>setInterval</code> 매서드) 등의 행위는 시간을 구독함으로서 구현할 수 있다.

- 이 또한 외부의 값의 변화를 계속해서 관찰하고 거기에 맞춰 동작을 하는 것이기에 Side Effect이다.

<br/><br/><br/>

## React에서 Side Effect의 올바른 발생 시점

- 아래 코드처럼 함수 컴포넌트 본문에서 바로 Side Effect를 발생시킬 때의 문제점

  ```js
  const App = () => {
    const doSideEffect = () => {
      // do some side effect
    };

    doSideEffect();

    return <h1>Hello World</h1>;
  };
  ```

  1. Side Effect가 렌더링을 Blocking 한다.

  2. 매 렌더링마다 Side Effect가 수행된다.

<br/>

- React에서 Side Effect를 발생시키기 위한 조건

  1. 렌더링을 Blocking 하지 않기 위해서 <strong>렌더링이 모두 완료된 후에 Side Effect가 실행될 수 있어야 한다.</strong>

  1. 매 렌더링마다 Side Effect가 실행되는 것이 아니라 <strong>필요할 때만 Side Effect가 조건부로 실행되도록 해주어야 한다.</strong>

- React엔 위 두 조건을 모두 만족시켜주면서 편하게 Side Effect를 발생시켜주는 hook이 존재한다.

  => <strong>useEffect</strong>

<br/><br/>

## useEffect

- useEffect는 React에서 Side Effect를 편리하고 안전하게 발생시킬 수 있도록 도와주는 Hook이다.

- useEffect는 함수이고, 매개변수로 <strong>콜백 함수</strong>를 가진다. 이 콜백 함수에서 특정한 Side Effect를 수행시킬 수 있다.

  ```js
  useEffect(콜백 함수);
  ```

<br/>

### useEffect는 (Side Effect를 발생시키는) 콜백 함수를 랜더링 이후 실행시킨다.

```js
import { useEffect } from "react";

const App = () => {
  console.log("Side Effect 실행");
  useEffect(() => {
    // do some side effect
    console.log("Side Effect with useEffect");
  });

  console.log("render");
  return <h1>Hello World</h1>;
};

export default App;
```

```
Side Effect 실행
render
Side Effect with useEffect
```

- 코드의 실행결과를 확인하니, 랜더링이 모두 끝난 이후 콜백 함수가 실행되었다.

- 이를 통해 React에서 Side Effect를 발생시키기 위한 첫 번째 조건인 '렌더링이 모두 완료된 후에 Side Effect가 실행될 수 있어야 한다'는 것이 useEffect를 통해 만족될 수 있음을 알 수 있다.

<br/>

### useEffect는 (Side Effect를 발생시키는) 콜백 함수를 조건부로 실행시킨다.

- 또한, useEffect의 콜백 함수는 기본적으로 최초의 랜더링 과정에서만 한 번 실행되고 그 뒤로는 다시 실행되지 않는다.

- 만일 콜백 함수를 특정 조건에서 실행할 수 있도록 하려면, useEffect의 두 번째 인자에 들어가는 의존성 배열을 활용하면 된다.

  ```js
  useEffect(콜백 함수, 의존성 배열);
  ```

<br/>

- <strong>useEffect의 동작 방식</strong>

  - 첫 번째 렌더링 이후에는 무조건 useEffect에 전달된 콜백 함수를 호출하고, 다음 렌더링부터는 아래의 조건에 따라 동작한다.

    1. 의존성 배열이 전달되지 않았다면 매 렌더링마다 콜백 함수를 호출한다.

    2. 의존성 배열이 전달되었다면 의존성 배열의 값을 검사한다.

    - a. 의존성 배열에 있는 값 중 하나라도 이전 렌더링과 비교했을 때 달라졌다면 콜백 함수를 호출한다.
    - b. 의존성 배열에 있는 값이 이전 렌더링과 비교했을 때 모두 동일하다면 콜백 함수를 호출하지 않는다.

<br/>

- 이를 통해 React에서 Side Effect를 발생시키기 위한 두 번째 조건인 '필요할 때만 Side Effect가 조건부로 실행되도록 해주어야 한다'는 것이 useEffect를 통해 만족될 수 있음을 알 수 있다.

<br/><br/>

## Clean Up Effect

- <strong>컴포넌트가 삭제(언마운트)될 때</strong> 어떤 작업을 수행할 수 있도록 한 장치이다.

- Side Effect가 불필요하게 계속 남아있으면 프로그램이 비효울적으로 동작하거나 의도에 벗어나게 동작할 수 있다.

- 따라서 이러한 Side Effect는 반드시 Clean Up을 해주어야 한다.

<br/>

```js
function Hello() {
  function byFn() {
    console.log("byebye");
  }

  function hiFn() {
    console.log("hello");
    return byFn;
  }

  useEffect(hiFn, []);

  return <h1>Hello</h1>;
}
```

```js
const Hello = () => {
  useEffect(() => {
    console.log("hello");
    return () => console.log("byebye");
  }, []);

  return <h1>Hello</h1>;
};
```

- 만일 <code>Hello</code> 컴포넌트가 사라지면, useEffect 콜백 함수 <code>hiFn</code>의 반환 함수인 <code>byFn</code>이 실행된다.

<br/>

- <strong>useEffect에서 Clean Up 함수가 호출되는 조건</strong>

  - 다음 Side Effect를 발생하기 전

  - 컴포넌트가 Unmount될 때
