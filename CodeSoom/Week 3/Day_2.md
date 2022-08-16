# 3주차 Day 2 TIL

#### 2022.08.16

<br/>

## 배운 것 (간략히 정리)

### 【1】 지난 주 복습

- <strong>컴포넌트 key에 대한 추가 학습</strong>

    - 자식 컴포넌트의 key 속성을 바꿔주면 다른 컴포넌트로 인식해서 기존 컴포넌트를 언마운트 시키고, 새로운 컴포넌트를 렌더링 시킨다.  
    (<a href="https://velog.io/@ansrjsdn/컴포넌트의-key가-바뀌었을-때-리렌더링-언마운트">참고 자료</a>)

<br/>

- <strong>지난 주 2번째 과제 (간단한 Todo App 만들기) 코드 학습</strong>

    - <strong>해설 코드</strong>

        - index.jsx

            ```jsx
            import React from 'react';
            import ReactDOM from 'react-dom';
            import App from './App';

            ReactDOM.render(<App />, document.getElementById('app'));

            ```

        - App.jsx

            ```jsx
            import React, { useState } from 'react';
            import Page from './Page';

            export default function App() {
                const [state, setState] = useState({
                    newId: 3,
                    newTask: '',
                    tasks: [
                        { id: 1, title: '아무 것도 하지 않기' },
                        { id: 2, title: '아무 것도 하지 않기 #2' },
                    ],
                });

                const { newId, newTask, tasks } = state;

                function handleChangeTitle(event) {
                    setState({
                        ...state,
                        newTask: event.target.value,
                    });
                }

                function handleClickAddTask() {
                    setState({
                        ...state,
                        newId: newId + 1,
                        newTask: '',
                        tasks: [...tasks, { id: newId, title: newTask }],
                    });
                }

                function handleClickDeleteTask(id) {
                    setState({
                        ...state,
                        tasks: tasks.filter((task) => task.id !== id),
                    });
                }

                return (
                    <Page
                        newTask={newTask}
                        onChangeTitle={handleChangeTitle}
                        onClickAddTask={handleClickAddTask}
                        onClickDeleteTask={handleClickDeleteTask}
                        tasks={tasks}
                    />
                );
            }
            ```
        
        - Page.jsx

            ```jsx
            import React from 'react';
            import Input from './Input';
            import List from './List';

            export default function Page({
                newTask, onChangeTitle, onClickAddTask,
                onClickDeleteTask, tasks,
            }) {
                return (
                    <div>
                        <h1>To-do</h1>
                        <Input
                            onChange={onChangeTitle}
                            newTask={newTask}
                            onClickAddTask={onClickAddTask}
                        />
                        <List
                            tasks={tasks}
                            onClickDeleteTask={onClickDeleteTask}
                        />
                    </div>
                );
            }

            ```

        - Input.jsx

            ```jsx
            import React from 'react';

            export default function Input({ onChange, newTask, onClickAddTask }) {
                return (
                    <p>
                        <input
                            type="text"
                            placeholder="할 일을 입력해 주세요"
                            value={newTask || ''}
                            onChange={onChange}
                        />
                        <button type="button" onClick={onClickAddTask}>추가</button>
                    </p>
                );
            }

            ```

        - List.jsx

            ```jsx
            import React from 'react';
            import Item from './Item';

            export default function List({ tasks, onClickDeleteTask }) {
                return (
                    <ol>
                        {tasks.map((task) => (
                            <Item
                            key={task.id}
                            task={task}
                            onClick={onClickDeleteTask}
                            />
                        ))}
                    </ol>
                );
            }
            ```

        - Item.jsx

            ```jsx
            import React from 'react';

            export default function Item({ task: { id, title }, onClick }) {
                return (
                    <li key="id">
                        id=
                        {id}
                        {' '}
                        -
                        {' '}
                        {title}
                        <button type="button" onClick={() => onClick(id)}>❌</button>
                    </li>
                );
            }
            ```

    <br/>

    - <strong>새로 알게된 점</strong>

        - 객체 매개변수 구조 분해 할당 방법

            ```javascript
            export default function Item({ task: { id, title } }) {
                // ...
            }
            ```

        - setState 설정시

            ```javascript
            setState({
                ...state,
                newTask: event.target.value,
            });
        ```

<br/><br/>

### 【2】 React 테스트 - 개념 학습

- Jest : 자바스크립트 테스팅 라이브러리

    - Jest 설치 -> <code>npm i -D jest @types/jest babel-jest</code>

- Assertion : 단정문. 기댓값이 실제값과 일치하는 지 확인하는 데 사용

- Signature : 모든 연산의 명세 (연산 이름, 매개변수, 반환값)

<br/>

- <strong>TDD (테스트 주도 개발 / Test Driven Development)</strong>

    - <strong>단위 테스트</strong> : 구현에 대한 테스트

    - <strong>TDD</strong> : 테스트가 개발을 주도하는 방법

        - 자동화된 단위 테스트 코드를 먼저 작성함으로써 테스트가 개발을 이끌어 나가도록 하는 방식

        - 테스트 코드가 자동으로 돌아가도록 한다.

        - 어떤 결과를 원하는지 명확히 알고, 그 결과가 도출되는 과정 또한 명확히 안 후, 이를 구체적으로 (코드로) 표현할 수 있어야 한다.

            - Test First Programming

    <br/>

    - <strong>2가지 룰</strong>

        - 테스트에 실패하는 코드가 없을 경우, 더 이상 새 코드를 작성하지 않는다.

        - 중복된 코드를 제거한다.

    <br/>

    - <strong>TDD 사이클 (How - Red Green Refactoring)</strong>

        1. [Red] 처음에는 통과하지 못하는 테스트를 작성하라

        2. [Green] 그 다음 테스트를 통과할 수 있도록 코드를 작성하라.

        3. [Refactor] 통과한 코드를 리펙토링을 통해 개선하라. (TDD의 핵심)

    <br/>

    - <strong>React testing library</strong>

        - 설치 : <code>npm i -D @testing-library/react @testing-library/jest-dom</code>

    <br/>

    - TDD 라이브 코딩 시청

        👉 <a href="https://youtu.be/L1dtkLeIz-M">링크</a>

<br/><br/>

### 【3】 React 테스트 - 실전 연습

- <code>test.js</code> 롹장자를 가진 파일 생성

- <code>.eslintrc.js</code> 업데이트

    ```javascript
    module.exports = {
        env: {
            browser: true,
            es2021: true,
            jest: true,  <-- '이거 추가'
        },
        extends: [
            'plugin:react/recommended',
            'airbnb',
        ],

        ...

    };
    ```

<br/>

- <strong>테스트 실행 명령어</strong>

    - <code>npx jest</code> : 테스트 파일 한 번 검사
    
    - <code>npx jest --watchAll</code> : 프로젝트에 있는 모든 테스트 파일 감시 (테스트 파일 저장 시 해당 파일 검사)

<br/>

- 코드 작성

    ```javascript
    test('simple', () => {
        expect(1 + 1).toBe(2);
    })
    ```

    - 테스트의 기본 구조 : <strong>단언문 (Assertion)</strong>
    
      - <strong>A</strong>는 <strong>B</strong>어야 한다. => A(<strong>실제값, actual</strong>)는 B(<strong>기대값, expect</strong>)어야 한다.

    ```javascript
    test('테스트 이름', 테스트 할 코드를 실행하는 함수 {
        expect(A).toBe(B)
        => '실제값(A)'이 '기대값(B)'이기를 기대한다.
    })
    ```

<br/>

- 다른 테스트 코드 예시

    - Step 1 > RED

        ```javascript
        function add() {
            // TODO
        }

        test('add', () => {
            expect(add(1, 3)).toBe(4);
        })
        ```

        - 여기서 우리는 <code>add</code>라는 <strong>Signature</strong>을 정의했다.

            - name(add), parameters(x, y), return(result)

    <br/>

    - Step 2 > GREEN

        ```javascript
        function add() {
            return 4;
            // return 1 + 3;
        }

        test('add', () => {
            expect(add(1, 3)).toBe(4);
        })

    <br/>

    - Step 3 > Refactoring

        ```javascript
        function add(x, y) {
            return x + y;
        }

        test('add', () => {
            expect(add(1, 3)).toBe(4);
        })
