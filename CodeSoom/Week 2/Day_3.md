# 2주차 Day 3 TIL

#### 2022.08.10

<br/>

## 배운 것 (간략히 정리)

### 【1】 React 관심사의 분리

- <strong>관심사의 분리</strong>

    - 프로그램을 구별된 '개개의 관심사를 해결하는 부분'으로 분리하는 디자인 원칙

    - 컴포넌트 별로 관심사를 분리하여 확장성과 재사용성을 높인다.

<br/>

- <strong>관심사의 분리 실습</strong>

    - 아직 익숙하지 않으므로 아래 실습 코드를 참고하여 어떻게 컴포넌트를 나눠야 할 지 감을 익히자. 

        ```javascript
        /* @jsx React.createElement */
        import React, { useState } from 'react';
        import ReactDOM from 'react-dom';

        function Counter({ count, onClick }) {
            return (
                <button type="button" onClick={onClick}>
                    Click me!
                    (
                    {count}
                    )
                </button>
            );
        }

        function Button({ children }) {
            return (
                <button type="button">
                    {children}
                </button>
            );
        }

        function Buttons() {
            return (
                <p>
                    {[1, 2, 3].map((i) => (
                        <Button key={i}>
                            {i}
                        </Button>
                    ))}
                </p>
            );
        }

        function Page({ count, onClick }) {
            return (
                <div>
                    <p>Counter</p>
                    <Counter count={count} onClick={onClick} />
                    <Buttons />
                </div>
            );
        }

        function App() {
            const [state, setState] = useState({
                count: 0,
            });

            const { count } = state;

            function handleClick() {
                setState({
                    count: count + 1,
                });
            }

            return <Page count={count} onClick={handleClick} />;
        }

        ReactDOM.render(<App />, document.getElementById('app'));
        ```

<br/><br/>

## 과제 진행

### 과제1. Counter 앱 만들고 파일 분리하기

- <a href="https://github.com/CodeSoom/react-week2-assignment-1/pull/173">PR 기록 바로가기</a>

    - 우선 컴포넌트 분리는 신경쓰지 않고 '동작하도록' 만드는 것에 집중했다.

    - <strong>목표 계획</strong>

        - [x] <strong>1차 목표</strong>. 우선 하나의 컴포넌트에 Counter앱 기능이 제대로 동작하도록 구현

        - [ ] <strong>2차 목표</strong>. 하나의 파일에서 컴포넌트를 하나씩 분리하기

        - [ ] <strong>3차 목표</strong>. 파일을 여러 개로 나누어 분리한 컴포넌트를 하나씩 담기

        - [ ] <strong>4차 목표</strong>. 리펙토링을 통한 코드 개선

<br/>

- <strong>컴포넌트 분리 시도</strong> (2차 목표)

    - 화면에 요소를 그려주는 Page 컴포넌트 분리 성공 (props 에러 때문에 조금 골머리를 앓았지만)

<br/>

### 과제 2 - 간단한 사칙 연산 계산기 구현

(수행하지 못함)

<br/><br/>

## Feeling

- 코테 대비 캠프 수업도 있었고 가족 저녁 외식도 있었지만, 오늘도 주어진 시간동안 묵묵히 할 일을 해서 그런지 만족스러웠다.

- 다만 외식 후 집에 들어와서 롤드컵 영상을 보느라 밤 시간을 조금 낭비한 것이 아쉬운 점이다.

<br/>

- 과제가 생각보다 시간이 더 걸릴 것 같다. 컴포넌트를 분리하는 것도 이번이 처음이다 보니 조금 헷갈린다.

   일단 남은 이틀동안 계속 더 해보자.