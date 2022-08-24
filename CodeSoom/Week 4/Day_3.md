# 4주차 Day 3 TIL

#### 2022.08.24

<br/>

## 배운 것 (간략히 정리)

### 【0】 To Do 앱 다시 구현해보기

- 혼자서 스스로 처음부터 끝까지 구현했다. (뿌듯)

<br/>

### 【1】 Redux 학습

#### 개인 학습 - 생활 코딩 (어제에 이어서)
    
- <strong>Redux</strong>

    - JS 앱을 위한, 예측가능한 상태의 저장소

    - 코드의 복잡성을 획기적으로 낮춰줌으로써, 결과를 예측 가능하게 만들어주는 도구

    <br/>

    - 단 하나의 상태(객체)를 갖는다. <- 앱의 모든 데이터를 우겨넣음
    
        - 앱의 복잡성 낮춤

    - 데이터를 외부에서 직접적으로 제어할 수 없음 (정보 은닉과 비슷한 개념)

        - 의도하지 않게 state 값이 변하는 것을 차단 -> 앱을 예측가능하게 만듦

<br/>

- <strong>가능성</strong>

    - Undo와 Redo를 굉장히 쉽게 할 수 있다.

        - 각각의 상태 변화가 서로에게 영향을 주지 않음 (원본을 직접 변화하지 않기 때문)

    - 앱의 과거 상태도 쉽게 알 수 있어 문제 해결을 쉽게 할 수 있도록 도와준다.

    - 모듈 리로딩 - 코드 작성 시 자동으로 앱에 반영

        - 앱은 새로고침 되어도 데이터는 그대로 남아있기에 가능한 일

<br/>

- <strong>Redux 지도</strong>

    <img src="img\redux_map.png">

<br/>

- <code>render</code> 함수는 UI를 그려주는 함수로, <code>getState</code> 함수를 통해 <code>state</code> 값을 참조하여 이를 바탕으로 UI를 그려준다.

- <code>subscribe</code>에 <code>render</code> 함수를 등록하면, <code>state</code> 값이 바뀔 때마다 <code>render</code> 함수가 호출되면서 UI가 새롭게 갱신된다.

<br/>

- 화면에 어떤 조작(액션)이 발생하면, 액션 객체가 dispatch에 전송된다.

- 액션 객체를 받은 dispatch의 역할

    - reducer을 호출하여 state 값을 바꾼다.

        - 이때 현재 state 값과 action 객체를 reducer에 전달한다.

    - 그 작업이 끝난 다음, <code>subscribe</code>을 이용하여 render 함수를 호출한다.

<br/>

- <strong>Presentational Components</strong>

    - redux를 알지 못함.
    
    - 보이는 것(View)에만 집중함.

<br/>

- <strong>Container Components</strong>

    - redux를 알고 있음.

    - 데이터를 가져오고 상태를 업데이트함.

<br/>

#### 코드숨 온라인 강의 학습

- <strong>Provider</strong>

    - React로 작성된 컴포넌트들을 Provider안에 넣으면 하위 컴포넌트들이 Provider를 통해 redux store에 접근이 가능해진다.

<br/>

- 작성한 코드

    - <code>index.jsx</code>

        ```jsx
        import React from 'react';
        import ReactDOM from 'react-dom';
        import { Provider } from 'react-redux';
        import App from './App';

        import store from './store';

        ReactDOM.render(
            (
                <Provider store={store}>
                    <App />
                </Provider>
            ),
            document.getElementById('app'),
        );
        ```

    - <code>App.jsx</code>

        ```jsx
        import React from 'react';
        import { useDispatch, useSelector } from 'react-redux';
        import Page from './Page';

        // action creator
        function updateTask(newTask) {
            return {
                type: 'updateTask',
                payload: {
                    newTask,
                },
            };
        }

        function addTask() {
            return {
                type: 'addTask',
            };
        }

        function deleteTask(id) {
            return {
                type: 'deleteTask',
                payload: {
                    id,
                },
            };
        }

        export default function App() {
            const { newTask, tasks } = useSelector((state) => ({
                newTask: state.newTask,
                tasks: state.tasks,
            }));

            const dispatch = useDispatch();

            function onClickChangeTask(event) {
                dispatch(updateTask(event.target.value));
            }

            function onClickAddTask() {
                dispatch(addTask());
            }

            function onClickDeleteTask(id) {
                dispatch(deleteTask(id));
            }

            return (
                <Page
                    tasks={tasks}
                    newTask={newTask}
                    onClickChangeTask={onClickChangeTask}
                    onClickAddTask={onClickAddTask}
                    onClickDeleteTask={onClickDeleteTask}
                />
            );
        }
        ```

<br/>    
