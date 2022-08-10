# 2주차 Day 2 TIL

#### 2022.08.09

<br/>

## 배운 것 (간략히 정리)

### 【1】 저번주 과제 2 코드 복습

- 1주차 과제 2를 다시 풀어보고, 해설 강의를 돌려보며 풀이 과정을 최대한 이해하였다.

- 중간에 직접 디버깅까지 해보며 최대한 혼자 힘으로 과제를 해결하려 노력했다.

<br/><br/>

### 【2】 React 이어 학습 + 강의 보며 실습

- <strong>컴포넌트 (Component)</strong>

    - 일종의 JavaScript 함수

    - 임의의 입력값(props)을 받아 화면에 어떻게 표시할 지를 기술하는 React 엘리먼트(element)를 반환한다.

        - 입력값 : props (객체로 전달) / 출력값 : React element
    
    <br/>

    - <strong>컴포넌트 합성</strong> : 한 컴포넌트 내에 다른 컴포넌트가 참조될 수 있다.

    - <strong>컴포넌트 분리</strong> : 한 컴포넌트를 재사용이 용이하도록 별도의 작은 컴포넌트들로 분리하는 것이 좋다.

    - props는 내부의 값을 수정할 수 없다. (순수 함수처럼 동작해야 함)

    <br/>

    - <strong>State</strong>

    <br/>

    - <strong>리액트 Hook, useState</strong>

        ```javascript
        const [count, setCounnt] = setCount(0);
        ```

<br/>

- +<strong> 추가로 학습한 것</strong>

    - ✨ webpack 서버 띄울 시 경로 설정 바꾸기 (<code>index.js</code>=><code>index.jsx</code>)

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
        };
        ```

<br/><br/>

## 과제 진행

(진행 하지 못함)

<br/><br/>

## Feeling

- 오늘은 그 동안 피로가 쌓였는 지 아침에 밥을 먹고 잠시 잠들어버렸다.

- 그래서 오늘도 공부를 저번주만큼 많이 하지 못했다. (사실 신병 드라마를 몰아본 탓도 있었다)

- 이틀 연속으로 이러니 맘이 좀 불안하다. 정말 초심이 흐트러져 버린 걸까.

- 그래도 이번 주 진도는 그리 많지 않아서 내일이면 과제 진행까지 할 수 있을 것 같다.

- 좀 더 고생할수록 얻는 것도 그만큼 많을 거다. 놀고 싶고 흐트러지고 싶어도 조금만 참자. 그래야 나중에 웃는다.
