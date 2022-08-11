# 2주차 Day 4 TIL

#### 2022.08.11

<br/>

## 배운 것 (간략히 정리)

### 【1】 과제1 진행하면서 겪은 것 + 배운 것

- 코드의 오류가 도저히 보이지 않음에도 서버 페이지가 계속 백지 상태면  

    <strong>VS Code와 페이지를 끄고 다시 실행해보자.</strong> 그럼 정상적으로 다시 표시될 수도 있다. (원인는 모르겠음)

<br/>

- <strong>컴포넌트에 key 속성을 부여해선 안된다.</strong> 이는 prop이 아니란다.

    ```jsx
    <Button key={i} onClick={onClick} />
    ```

    ```
    react.development.js:210 Warning: Button: `key` is not a prop. Trying to access it will result in `undefined` being returned. If you need to access the same value within the child component, you should pass it as a different prop.
    ```

<br/>

- <strong>분리한 컴포넌트를 각 파일에 나눠 담을 때</strong>

    - (React를 사용하므로) <code>import React from 'react';</code>는 모든 파일의 최상단에 꼭 작성해주어야 한다.

        - useState Hook을 같이 사용한다면 <code>import React, { useState } from 'react';</code> 이렇게 작성해주면 된다.

    - 다른 컴포넌트를 불러올 때 <code>import</code>를 사용한다.

    - 컴포넌트를 다른 파일로 내보낼 때 <code>export</code>를 사용한다.


    ```jsx
    import React, { useState } from 'react';
    import Page from './Page';

    function App() {
        const [number, setNumber] = useState({
            count: 0,
        });

        const { count } = number;

        function handleClick(value) {
            // ...
        }
    }

    export default App;
    ```

<br/><br/>

## 과제 진행

### 과제1. Counter 앱 만들고 파일 분리하기

- <a href="https://github.com/CodeSoom/react-week2-assignment-1/pull/173">PR 기록 바로가기</a>

    - 과제의 요구사항을 모두 만족하도록 구현하는데 성공했다.

    - <strong>목표 계획</strong>

        - [x] <strong>1차 목표</strong>. 우선 하나의 컴포넌트에 Counter앱 기능이 제대로 동작하도록 구현

        - [x] <strong>2차 목표</strong>. 하나의 파일에서 컴포넌트를 하나씩 분리하기

        - [x] <strong>3차 목표</strong>. 파일을 여러 개로 나누어 분리한 컴포넌트를 하나씩 담기

        - [ ] <strong>4차 목표</strong>. 리펙토링을 통한 코드 개선

<br/>

### 과제 2 - 간단한 사칙 연산 계산기 구현

(수행하지 못함)

<br/><br/>

## Feeling