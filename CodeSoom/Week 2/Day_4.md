# 2주차 Day 4 TIL

#### 2022.08.11

<br/>

## 배운 것 (간략히 정리)

### 【0】 ✨ Fork한 코드숨 과제 Repository - 업데이트 순서

- 경로 이동 :<code>cd cd react-week?-assignment-?</code>

- NPM 초기화 : <code>npm init -y</code>

- Webpack 업데이트 : <code>npx webpack serve --mode development</code> (모두 설치)

- ESLint 업데이트 : <code>npm i -D eslint</code>

- ESLint 설정 : <code>npx eslint --init</code>

- webpack 서버 띄울 시 경로 설정 바뀌어 있는지 확인 (<code>index.js</code>=><code>index.jsx</code>)

    ```javascript
    // webpack.config.js
    const path = require('path');

    module.exports = {
        entry: path.resolve(__dirname, 'src/index.jsx'),
        mode: 'development',
        module: {
            rules: [
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    use: 'babel-loader',
                },
            ],
        },
        resolve: {
            extensions: ['.js', '.jsx'],
        },
    };
    ```

- <code>.eslintrc.js</code> 파일 수정

    ```javascript
    // .eslintrc.js
    module.exports = {
        env: {
            browser: true,
            es2021: true,
        },
        extends: [
            'plugin:react/recommended',
            'airbnb',
        ],
        parserOptions: {
            ecmaFeatures: {
            jsx: true,
            },
            ecmaVersion: 12,
            sourceType: 'module',
        },
        plugins: [
            'react',
        ],
        globals: {
            Atomics: 'readonly',
            SharedArrayBuffer: 'readonly',
            actor: 'readonly',
            Feature: 'readonly',
            Scenario: 'readonly',
        },
        rules: {
            'linebreak-style': 0,
            indent: ['error', 2],
            'no-trailing-spaces': 'error',
            curly: 'error',
            'brace-style': 'error',
            'no-multi-spaces': 'error',
            'space-infix-ops': 'error',
            'space-unary-ops': 'error',
            'no-whitespace-before-property': 'error',
            'func-call-spacing': 'error',
            'space-before-blocks': 'error',
            'keyword-spacing': ['error', { before: true, after: true }],
            'comma-spacing': ['error', { before: false, after: true }],
            'comma-style': ['error', 'last'],
            'comma-dangle': ['error', 'always-multiline'],
            'space-in-parens': ['error', 'never'],
            'block-spacing': 'error',
            'array-bracket-spacing': ['error', 'never'],
            'object-curly-spacing': ['error', 'always'],
            'key-spacing': ['error', { mode: 'strict' }],
            'arrow-spacing': ['error', { before: true, after: true }],

            'react/prop-types': 'off',
            'react/react-in-jsx-scope': 'off',
            'react/jsx-no-bind': 'off',
        },
    };

    ```

<br/><br/>

### 【1】 과제1 진행하면서 겪은 것 + 배운 것

- 코드의 오류가 도저히 보이지 않음에도 서버 페이지가 계속 백지 상태면  

    <strong>VS Code와 페이지를 끄고 다시 실행해보자.</strong> 그럼 정상적으로 다시 표시될 수도 있다. (원인는 모르겠음)

<br/>

- <strong>컴포넌트에 key 속성을 부여하면 해당 컴포넌트에서 값을 제대로 읽지 못한다..</strong> 이는 prop이 아니라고 한다.

- 하지만 <a href="https://ko.reactjs.org/docs/lists-and-keys.html#extracting-components-with-keys">React 공식문서의 해당 부분</a>을 살펴보면, <strong>컴포넌트에 key 속성을 부여하는 것이 옳바른 사용법이다.</strong>

- <strong>그럼 어떻게 해야 할까?</strong> (코드숨 트레이너님께 질문 남겼음)

    ```jsx
    <Button key={i} onClick={onClick} />
    ```

    ```
    react.development.js:210 Warning: Button: `key` is not a prop.
    Trying to access it will result in `undefined` being returned.
    If you need to access the same value within the child component,
    you should pass it as a different prop.
    ```

<br/>

- <strong>분리한 컴포넌트를 각 파일에 나눠 담을 때</strong>

    - (React를 사용하므로) <code>import React from 'react';</code>는 모든 파일의 최상단에 꼭 작성해주어야 한다.

        - useState Hook을 같이 사용한다면 <code>import React, { useState } from 'react';</code> 이렇게 작성해주면 된다.

    <br/>

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

### 【2】 과제2 진행을 위한 지식 학습

- <strong>이벤트 처리</strong>

- <strong>리스트와 key</strong>

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

- <a href="https://github.com/CodeSoom/react-week2-assignment-2/pull/157">PR 기록 바로가기</a>

    - 아직 PR만 보냈다. (과제 요구사항 정리, 과제 수행 계획 수립)

    - 넘 어려워보인다.

<br/><br/>

## Feeling

- 오늘 코드 리뷰를 받고 조금 답답한 기분이 들었다. 혹시 제가 질문한 것을 못 보셨나 싶은 생각이 들었다.

- 역시 이번에도 답을 가르쳐주지 않고 방향만을 제시해줌으로 인해 혼자서 문제를 해결해줄 수 있도록 유도하시는구나.

- 비록 답답하고 고통스럽지만 이런 과정을 통해 내가 성장하고, 깨달은 지식이 비로소 내 것이 되는 것을 알고 있으니, 충분히 납득이 된다.

- 내일 key에 대해서 다시 한 번 공부해보며 막힌 문제를 해결해보자.

<br/>

- 오늘은 넘 답답해서 저녁에 공부 대신 바람을 좀 쐬고 왔다. 잘한 선택인 것 같다.

- 답답한 기분이 좀 가셨으니 낼 다시 힘내보자.

- 내일은 코딩 테스트 캠프의 밀린 과제 수행을 위주로 해야할 것 같다. 코드숨에 관해선 key에 대해 다시 공부해보고 첫 번째 과제를 마무리 짓는 걸 목표로 해보자.