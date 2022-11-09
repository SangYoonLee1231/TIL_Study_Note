# React JS - Side Effect와 useEffect

> 참고 자료 : 부트캠프 학습 자료

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## Side Effect란?

- Side Effect란 <strong>부작용</strong>이다.

- <strong>부작용 === 부수효과</strong>

  - <strong>부수효과</strong> : 주요한 효과에 따라서 발생하는 부수적인 효과

- <strong>부작용이란 용어 자체는 부정적인 의미를 내포하지 않는다.</strong> 단지 부수적으로 발생하는 효과를 의미하는 단어이다.

<br/>

### 프로그래밍에서 Side Effect (부작용) 란?

- 코드가 의도한 주된 효과 외에 <strong>추가적으로 발생하는 효과</strong>

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

- 프로그래밍에서 Side Effect는 기피해야 하는 대상이다. 그 이유는..

  - Side Effect가 있는 함수는 동작 결과를 예측하기 어렵게 만든다.

  - 이는 곧 프로그래밍이 어떻게 동작할 지 예측하기 힘들게 만들어 유지 보수의 어려움도 야기한다.

- 하지만 프로그래밍에서 외부의 값을 읽어오거나 변경하는 행위를 완전히 무시할 순 없다. 오히려 프로그래밍에 반드시 있어야 하는 동작이다.

- 따라서 개발자들은 Side Effect를 최소화하면서 프로그램을 설계하되, Side Effect를 적재적소에 사용하고 통제할 수 있도록 하여, 관리 시 예측 가능하고 유지 보수하기 쉬운 프로그램을 만들어야 한다.

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

  - Data Fetching

  - DOM 접근 및 조작

  - 구독 (Subscribe)

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

- 시간은 계속해서 변하기에, 특정 시간이 지났을 때 액션을 취하거나(<code>setTimeout</code> 매서드), 특정 시간 주기마다 액션을 취하는(<code>setInterval</code> 매서드) 등의 행위를 시간을 구독함으로서 구현할 수 있다.

- 이 또한 외부의 값의 변화를 계속해서 관찰하고 거기에 맞춰 동작을 하는 것이기에 Side Effect이다.
