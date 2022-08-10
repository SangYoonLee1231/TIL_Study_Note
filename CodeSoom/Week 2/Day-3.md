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