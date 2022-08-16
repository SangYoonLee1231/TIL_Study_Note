# 3주차 Day 2 TIL

#### 2022.08.16

<br/>

## 배운 것 (간략히 정리)

### 【1】 지난 주 복습

- <strong>컴포넌트 key에 대한 추가 학습</strong>

    - 자식 컴포넌트의 key 속성을 바꿔주면 다른 컴포넌트로 인식해서 기존 컴포넌트를 언마운트 시키고, 새로운 컴포넌트를 렌더링 시킨다.  
    (<a href="https://velog.io/@ansrjsdn/컴포넌트의-key가-바뀌었을-때-리렌더링-언마운트">참고 자료</a>)

<br/>

- <strong>지난 주 2번째 과제 (간단한 Todo App 만들기) 코드 이해하기</strong>

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

        - setState 설정시 (<code>...state</code>)

            ```javascript
            setState({
                ...state,
                newTask: event.target.value,
            });
            ```

<br/><br/>

### 【2】 React 테스트 - 개념 학습

- <strong>Jest</strong> : 자바스크립트 테스팅 라이브러리

    - <strong>Jest 설치</strong> : <code>npm i -D jest @types/jest babel-jest</code>

- <strong>Assertion</strong> : 단정문. 기댓값이 실제값과 일치하는 지 확인하는 데 사용

- <strong>Signature</strong> : 모든 연산의 명세 (연산 이름, 매개변수, 반환값)

<br/>

- <strong>TDD (테스트 주도 개발 / Test Driven Development)</strong>

    - <strong>단위 테스트</strong> : 구현에 대한 테스트

    - <strong>TDD</strong> : <strong>테스트가 개발을 주도하는 방법</strong>

        - 자동화된 단위 테스트 코드를 <strong>먼저 작성</strong>함으로써 테스트가 개발을 이끌어 나가도록 하는 방식

        - 테스트 코드가 <strong>자동</strong>으로 돌아가도록 한다.

        - ✨ 어떤 결과를 원하는지 명확히 알고, 그 결과가 도출되는 과정 또한 명확히 안 후, 이를 구체적으로 (코드로) 표현할 수 있어야 한다.

            - Test First Programming

    <br/>

    - <strong>2가지 룰</strong>

        - 테스트에 실패하는 코드가 없을 경우, 더 이상 새 코드를 작성하지 않는다.

        - 중복된 코드를 제거한다.

    <br/>

    - <strong>TDD 사이클 (How - Red Green Refactoring)</strong>

        1. <strong>[Red]</strong> 처음에는 통과하지 못하는 테스트를 작성하라

        2. <strong>[Green]</strong> 그 다음 테스트를 통과할 수 있도록 코드를 작성하라.

        3. <strong>[Refactor]</strong> 통과한 코드를 리펙토링을 통해 개선하라. (TDD의 핵심)

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

- 테스트의 기본 구조 : <strong>단언문 (Assertion)</strong>
    
    - <strong>A</strong>는 <strong>B</strong>어야 한다.
    
    - A(<strong>실제값, actual</strong>)는 B(<strong>기대값, expect</strong>)어야 한다.

        ```javascript
        test('simple', () => {
            expect(1 + 1).toBe(2);
        })
        ```
        ```javascript
        test('테스트 이름', 테스트 할 코드를 실행하는 함수 {
            expect(A).toBe(B)
            => '실제값(A)'이 '기대값(B)'이기를 기대한다.
        })
        ```

<br/>

- 다른 테스트 코드 예시

    - Step 1 > <strong>RED</strong>

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

    - Step 2 > <strong>GREEN</strong>

        ```javascript
        function add() {
            return 4;
            // return 1 + 3;
        }

        test('add', () => {
            expect(add(1, 3)).toBe(4);
        })

    <br/>

    - Step 3 > <strong>Refactoring</strong>

        ```javascript
        function add(x, y) {
            return x + y;
        }

        test('add', () => {
            expect(add(1, 3)).toBe(4);
        })

<br/>

- <strong>[ 오류 ❗ ] ReferenceError: document is not defined</strong>

    - render을 import했음에도 jest에서 document가 정의되지 않았다는 오류 발생

    - jsdom 실행 환경이 아니라서 발생한 문제

    - jest가 28버전 이상이 되면서 패키지 크기를 줄이기 위해 <code>jest-environment-jsdom</code>을 삭제했다고 한다.  

    (<a href="https://stackoverflow.com/questions/69227566/consider-using-the-jsdom-test-environment">참고한 StackOverflow 질문</a>)

    - <strong>해결 방법</strong>
    
        1. <code>jest-environment-jsdom</code>을 따로 설치해준다.

            - 명령어 : <code>npm i -D jest-environment-jsdom</code>

        2. <code>package.json</code>에 아래 코드를 추가하거나, <code>jest.config.js</code> 파일을 만들어 아래 코드를 추가한다.  
        
        (<strong>반드시 둘 중 하나만 해야 한다.</strong>)

            - package.json

            ```json
            "jest":{
                "testEnvironment": "jsdom"
            }
            ```

            - jest.config.js

            ```js
            {
                testEnvironment: 'jsdom',
            };
            ```

<br/>

- <strong>모든 테스트 파일에 적용할 코드 설정하기</strong>

    - <code>jest.config.js</code> 파일에 다음을 추가한다.

        ```js
        // jest.config.js
        module.exports = {
            setupFilesAfterEnv: [
                './jest.setup',
            ],

            // ...
        };

        ```
    
    - <code>jest.setup.js</code> 파일을 <strong>생성</strong>하고, 모든 테스트 파일에 적용할 코드를 그 안에 작성한다.

        ```js
        // jest.setup.js
        import '@testing-library/jest-dom';
        ```
<br/>

- <strong>테스트 코드 작성법</strong>

    - 아직 이해가 잘 되지 않는다. 내일 좀 더 공부를 해봐야 할 듯

<br/><br/>

## Feeling

- 오랜만에 하루종일 기분 좋게 공부를 할 수 있었다. (대략 8시간 공부)

- 저번 주 회고 때 다짐했던 내용 - '내 자신과 타협하려 하기 전에 '그냥' 묵묵히 공부하는 자세 갖기'를 실천한 덕분이다.

- 그리고 어제 트레이너 다희님과의 상담 덕에 걱정과 고민이 어느 정도 해소된 점도 오늘 공부에 긍정적인 영향을 미쳤다.

- (아침에 코로나 검사를 받고 오느라 공부 흐름이 끊길 뻔한 위기가 있었으나 다행이 잘 넘겼다.)

<br/>

- 주간회고 작성 시 다른 사람들이 내 회고를 읽는다는 것을 좀 더 의식해야함을 깨달았다.

- 내가 쓴 글이 다른 사람들에겐 곧 내 얼굴이자 이미지이니까.

- 앞으로 좀 더 신중하게 회고를 작성해야겠다.

    - 지금처럼 솔직하고 진솔하게 적되, 개인적인 감정은 되도록 줄이는 것이 좋겠다.

    - 다른 사람이 읽었을 때 오해할 만하거나 기분이 좋지 않을 만한 내용이 혹 있는지도 다시 한 번 확인해보고.