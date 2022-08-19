# 3주차 Day 5 TIL

#### 2022.08.19

<br/>

## 배운 것 (간략히 정리)

### 【1】 테스트 코드 공부 - '<a href="https://www.udemy.com/course/jest-testing-library/">Jest 및 테스팅 라이브러리로 React 테스트하기</a>' Udemy 강의

#### 간단한 React 앱 테스팅하기

- <strong>앱의 기능</strong>

    - 초기 상태

        - '빨간' 버튼 생성, 문구 : 'Change to blue'

    - 빨간 버튼 클릭 시

        - 버튼 색 변경 : '빨간' -> '파란' 버튼

        - 문구 변경 : 'Change to blue' -> 'Change to red'

<br/>

- <strong>App 컴포넌트 코드</strong>

    ```js
    // App.js
    import { useState } from 'react';
    import logo from './logo.svg';
    import './App.css';

    function App() {
        const [ buttonColor, setButtonColor ] = useState('red');
        const newButtonColor = buttonColor === 'red' ? 'blue' : 'red';

        return (
            <div>
                <button 
                    style={{backgroundColor: buttonColor}}
                    onClick={() => setButtonColor(newButtonColor)}
                >
                    Change to {newButtonColor}
                </button>
            </div>
        );
    }

    export default App;
    ```

<br/>

- <strong>App 컴포넌트 테스트 코드</strong>

    ```js
    // App.test.js
    import { render, screen, fireEvent } from '@testing-library/react';
    import App from './App';

    test('button has correct initial color', () => {
        render(<App />);

        // find an element with a role of button and text of 'Change to blue'
        const colorButton = screen.getByRole('button', { name: 'Change to blue' });

        // expect the background color to be red
        expect(colorButton).toHaveStyle({ backgroundColor: 'red' });


        // click button
        fireEvent.click(colorButton);

        // expect the background color to be blue
        expect(colorButton).toHaveStyle({ backgroundColor: 'blue' });

        // expect the button text to be 'Change to red'
        expect(colorButton.textContent).toBe('Change to red');
    });
    ```

<br/>

- <strong>설명</strong> 

    - (기능 테스트의 경우 하나의 테스트에 여러 개의 단언문을 넣어주어도 상관없다.)

    - <strong><code>render(<App />);</code></strong>
    
      - <code>render</code> 매서트로 <code>App</code> 컴포넌트의 가상 DOM을 생성한다.

    - <strong><code>const colorButton = screen.getByRole('button', { name: 'Change to blue' });</code></strong>

      - 생성한 가상 DOM에 접근하여 원하는 요소를 찾기 위해 <code>screen</code> 객체와 <code>getByRole()</code>을 이용한다.

      - <code>getByRole()</code>의 첫 번째 인수는 역할(role)을 나타내는 문자열. 여기서는 <code>button</code>이다.

        - <a href="https://www.w3.org/TR/wai-aria/#role_definitions">역할(role)의 종류 확인하기</a>

        - (존재하지 않는 역할을 넣었을 때, 테스팅 라이브러리의 출력값을 통해 가이드를 받을 수 있다.)

      - <code>getByRole()</code>의 두 번째 인수는 옵션. <code>name</code> 옵션에서 예상하는 것을 입력해서 확인할 수 있다.

    - <strong><code>expect(colorButton).toHaveStyle({ backgroundColor: 'red' })</code></strong>

      - js-dom의 <code>toHaveStyle</code> 매처를 사용하여 버튼의 배경색이 빨간색인지 확인한다.

        - <a href="https://github.com/testing-library/jest-dom">js-dom의 사용자 정의 매처 종류 확인하기</a>

    <br/> 

    - <strong><code>fireEvent.click(colorButton);</code></strong>

      - <code>@testing-library/react</code>에서 가상 DOM과 상호작용을 도와주는 <code>fireEvent</code> 객체를 <code>import</code>한다.

        - <code>import { render, screen, fireEvent } from '@testing-library/react';</code>

      - <code>fireEvent</code>로 <code>colorButton</code>을 클릭하였다.

    - 나머지 두 줄은 위와 동일한 패턴이므로 생략

    <br/> 

    - 하나의 테스트 중 단언에서 실패 결과가 나오면 나머지 코드는 무시된다.

        - 그래서 테스트마다 하나의 단언을 두는 것이 바람직하지만,

        - 기능 테스트를 할 땐 그것이 실용적이지 않다.

<br/>

#### 간단한 React 앱에 추가 기능을 붙여 테스팅하기

- <strong>앱의 기능</strong>

    - 초기 상태

        - '빨간' 버튼 생성, 문구 : 'Change to blue'

        - 체크 박스 생성 - 체크 되지 않음

    - 체크 박스가 체크 X, 빨간 버튼 클릭 시

        - 버튼 색 변경 : '빨간' -> '파란' 버튼

        - 문구 변경 : 'Change to blue' -> 'Change to red'

    - 체크 박스가 체크 시

        - 버튼이 비활성화

<br/>

- <strong>App 컴포넌트 코드</strong>

    ```js
    // App.js
    import { useState } from 'react';

    function App() {
        const [ buttonColor, setButtonColor ] = useState('red');
        const [ disabled, setdisabled ] = useState(false);
        
        const newButtonColor = buttonColor === 'red' ? 'blue' : 'red';
        
        return (
            <div>
                <button
                style={{backgroundColor: buttonColor, color: 'white'}}
                onClick={() => setButtonColor(newButtonColor)}
                disabled={disabled}
            >Change to {newButtonColor}</button>
            <br />
            <input
                type="checkbox"
                id="enable-button-checkbox"
                defaultChecked={disabled}
                aria-checked={disabled}
                onChange={(e) => setdisabled(e.target.checked)} />
            </div>  
        );
    }

    export default App;
    ```

<br/>

- <strong>App 컴포넌트 테스트 코드</strong>

    ```js
    // App.test.js
    import { render, screen, fireEvent } from '@testing-library/react';
    import App from './App';

    test('button has correct initial color', () => {
        render(<App />);

        // find an element with a role of button and text of 'Change to blue'
        const colorButton = screen.getByRole('button', { name: 'Change to blue' });
        // expect the background color to be red
        expect(colorButton).toHaveStyle({ backgroundColor: 'red' });

        // click button
        fireEvent.click(colorButton);
        // expect the background color to be blue
        expect(colorButton).toHaveStyle({ backgroundColor: 'blue' });
        // expect the button text to be 'Change to red'
        expect(colorButton.textContent).toBe('Change to red');
    });

    test('initial conditions', () => {
        render(<App />);

        // check that the button starts out enabled
        const colorButton = screen.getByRole('button', { name : 'Change to blue' });
        expect(colorButton).toBeEnabled();

        // check that the checkbox starts out unchecked
        const checkbox = screen.getByRole('checkbox');
        expect(checkbox).not.toBeChecked();
    });

    test('Checkbox disables button on first click and enables on second click', () => {
        render(<App />);

        const button = screen.getByRole('button');
        const checkbox = screen.getByRole('checkbox');

        fireEvent.click(checkbox);
        expect(button).toBeDisabled();
        fireEvent.click(checkbox);
        expect(button).toBeEnable();
    })
    ```

<br/>

### 【2】 '테스트' 코드숨 온라인 강의 재시청

- 처음에는 이게 뭔 소리야 했는데, Udemy 강의를 통해 학습한 후 야살님 강의를 다시 들어보니 드디어 이해가 된다.

    ```jsx
    // Item.test.jsx
    import React from 'react';
    import { render, fireEvent } from '@testing-library/react';
    import Item from './Item';

    test('Item', () => {
        const task = {
            id: 1,
            title: '아무 것도 하지 않기',
        };

        const handleCilck = jest.fn();

        const { container, getByText } = render(
            <Item task={task} onClick={handleCilck} />,
        );

        expect(container).toHaveTextContent('아무 것도 하지 않기');
        expect(container).toHaveTextContent('완료');

        expect(handleCilck).not.toBeCalled();

        fireEvent.click(getByText('완료'));

        expect(handleCilck).toBeCalledWith(1);
    });
    ```

<br/>

### 【3】 BDD 학습

- <a href="https://ko.javascript.info/testing-mocha#ref-1068">해당 자료</a>를 통해 학습

<br/><br/>

## 과제 진행

### 과제1. To-do 테스트 작성하기

- <a href="https://github.com/CodeSoom/react-week3-assignment-1/pull/150">PR 기록 바로가기</a>

    - Input 컴포넌트의 초기값 확인 테스트 코드만 작성하여 PR을 보냈다.

    - 테스트 코드에서 요소를 가져올 때도 <code>querySelector</code> 를 사용할 수 있구나.

    - 비록 9시를 넘겼지만, Input 컴포넌트 테스트 코드를 빠르게 완성하여 추가 커밋을 진행했다.

<br/><br/>

## Feeling
