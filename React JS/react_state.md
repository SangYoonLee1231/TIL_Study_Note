# React JS - State

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_state.md#reactusestate-%ED%95%A8%EC%88%98"><code>React.useState()</code> 함수</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_state.md#state-%ED%95%A8%EC%88%98">State 함수</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_state.md#state-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0">State 활용하기</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_state.md#input%EC%97%90-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0"><code>input</code>에 활용하기</a>

<br/><br/>

## <code>React.useState()</code> 함수

- React에서 변수를 다루는 유용한 방법

- 반드시 컴포넌트 내부에서만 사용할 수 있다.

<br/>

- <code>React.useState()</code> 호출 시 '<strong>변수값</strong>'과 '<strong>modifier 함수</strong>' 2개의 원소가 배열로 묶여 반환된다.

  ```javascript
  const root = document.getElementById("root");
  const App = () => {
    // 주목할 부분
    const data = React.useState(0);
    console.log(data);
    // 여기까지
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

  - <strong>undefined</strong> : 데이터 (변수)

  - <strong>f</strong> : 데이터를 바꾸는 modifier 함수

<br/>

- <strong><a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9">구조분해할당</a></strong>을 활용하면 좀 더 효율적으로 코드를 작성할 수 있다.

  ```javascript
  const root = document.getElementById("root");
  const App = () => {
    // 주목할 부분
    const [counter, setCounter] = React.useState(0);
    const onClick = () => {
      setCounter(counter + 1);
    };
    // 여기까지
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

- ✨ modifier 함수를 통해 state(값)을 변경하면 컴포넌트가 새 값을 가지고 재생성(리랜더링)된다.

<br/><br/>

## State 함수

- state 변경 시 이전 값을 바탕으로 현재 값을 설정하는 더 안전한 방법은 함수를 사용하는 것이다.

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

<br/>

- setState 함수는 비동기적으로 동작한다.

<br/><br/>

## State 활용하기

### <code>input</code>에 활용하기

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

<br/>

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
  ```
