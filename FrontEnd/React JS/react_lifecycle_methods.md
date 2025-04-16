# React JS - 라이프사이클 기능 (Lifecycle Methods)

<br/>

## React에서 라이프사이클이란?

- 컴포넌트가

  - 화면에 나타나고(Mount),

  - 업데이트되며(Update),

  - 사라지는(Unmount)

- 주기마다 실행되는 특별한 메서드들(혹은 개념적 단계)을 의미한다.

<br/>

- 클래스 컴포넌트에서는 componentDidMount, componentDidUpdate, componentWillUnmount 같은 전용 메서드가 있으며,

- 함수형 컴포넌트에서는 주로 useEffect Hook을 통해 이 로직들을 통합하여 간단히 관리한다.

<br/><br/>

## 라이프사이클 단계

- React(클래스 컴포넌트 기준)에서 라이프사이클(Lifecycle)은 크게 <strong>마운트(Mount)</strong>, <strong>업데이트(Update)</strong>, <strong>언마운트(Unmount)</strong>, 그리고 <strong>에러 처리(Error Handling)</strong> 단계로 나눌 수 있다.

- 더 간단히 이해하려면 <strong>마운트(생성)</strong>, <strong>업데이트(변경)</strong>, <strong>언마운트(소멸)</strong> 3단계로 나눠서 볼 수 있다.

<br/>

### 마운트(Mount) - 생성

- 컴포넌트가 처음으로 DOM에 삽입되어 화면에 나타날 때 실행되는 단계이다.

- 하는 일

  - 초기 데이터 설정, API 호출, 이벤트 리스너 등록 등

- 예시 코드

  ```jsx
  import React, { useState, useEffect } from "react";

  function SimpleComponent() {
    const [data, setData] = useState(null);

    // 마운트될 때 실행: 컴포넌트가 화면에 나타났을 때 API 호출
    useEffect(() => {
      console.log("마운트: 컴포넌트가 생성되었습니다!");
      // 예: API 호출
      fetch("/api/example")
        .then((res) => res.json())
        .then((result) => setData(result));
    }, []); // 빈 배열 []는 오직 최초 마운트 시에만 실행되도록 함

    return <div>{data ? "데이터를 불러왔습니다!" : "로딩중..."}</div>;
  }
  ```

<br/>

### 업데이트(Update) - 변경

- 컴포넌트 내의 상태나 부모로부터 전달받은 props가 바뀌면, 화면의 내용이 달라지는 단계이다.

- 하는 일

  - 상태가 바뀌면 그에 따라 UI를 다시 그린다.
  - 변경 후 필요한 추가 작업(업데이트된 데이터를 다시 사용하여 다른 효과 실행 등)을 실행한다.

- 예시 코드

  ```jsx
  import React, { useState, useEffect } from "react";

  function Counter() {
    const [count, setCount] = useState(0);

    // count 값이 변경될 때마다 실행됨 (업데이트)
    useEffect(() => {
      console.log(`업데이트: count가 ${count}로 변경되었습니다!`);
    }, [count]); // count가 변경될 때마다 effect 실행

    return (
      <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>증가</button>
      </div>
    );
  }
  ```

<br/>

### 3. 언마운트 (소멸)

- 컴포넌트가 화면에서 사라지기 전에 실행되는 단계이다.

- 하는 일

  - 타이머 종료, 이벤트 리스너 제거 등 정리(cleanup) 작업을 수행한다.

- 예시 코드

  ```jsx
  import React, { useState, useEffect } from "react";

  function TimerComponent() {
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
      console.log("타이머 시작!");
      const intervalId = setInterval(() => {
        setSeconds((prev) => prev + 1);
      }, 1000);

      // cleanup 함수: 컴포넌트가 언마운트되기 전에 실행됩니다.
      return () => {
        console.log("타이머 중지 및 정리!");
        clearInterval(intervalId);
      };
    }, []); // 오직 마운트될 때만 생성, 언마운트 시 cleanup 실행

    return <div>Seconds: {seconds}</div>;
  }
  ```

<br/>
