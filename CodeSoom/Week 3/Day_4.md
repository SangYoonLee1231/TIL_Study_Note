# 3주차 Day 4 TIL

#### 2022.08.18

<br/>

## 배운 것 (간략히 정리)

### 【1】 2주차 과제2 - 간단한 Todo App 만들기 과제 2차 복습

- 해설 강의의 도움을 받아 최대한 혼자 힘으로 코드를 다시 작성해봄

    - 이해도 ↑

<br/>

### 【2】 테스트 코드 공부 - '<a href="https://www.udemy.com/course/jest-testing-library/">Jest 및 테스팅 라이브러리로 React 테스트하기</a>' Udemy 강의

#### React Testing Library (RTL)

- 라이브러리 작성 방식이 특정 관행을 권장 -> React 테스트가 그 권장 사례

- 사용자 사용 방식으로 소프트웨어를 테스트하는 것

- 내부 구현 테스트를 대신하는 것

    - 내부 구현 => 소프트웨어의 작성법

- '소프트웨어가 원래대로 동작하는 지'가 중요

- 접근성 마커로 요소를 찾는 것 (테스트 ID 사용 대신)

<br/>

#### RTL vs Jest (역할의 관점)

- <strong>RTL</strong>

    - 테스트를 위한 가상 DOM 제공 (<code>render</code> 매서드로 생성)
    
    - 브라우저 없이 테스트를 진행하려면 클릭 요소와 같은 작업을 할 때 가상 DOM 필요

        - 가상 DOM과 상호작용하여 요소를 클릭하거나 텍스트를 입력
    
    - 가상 DOM이 원하는 대로 동작하는 지 확인 가능

- <strong>Jest</strong>

    - 테스트 러너

    - 테스트를 찾고 실행하는 것과, 테스트 통과 여부를 결정하는 역할을 한다.

    - Jest를 실행하는 방법으로 Watch 모드가 있다.

        - Watch 모드 : 마지막 커밋 이후 파일의 모든 변경 사항 확인, 변경된 파일과 연관된 테스트만 실행

<br/>

#### <code>create-react-app</code>

- React 애플리케이션 생성을 도와주는 npm 패캐지

- 테스팅 라이브러리를 포함하고 있다.

- 사실 <code>create-react-app</code>은 컴퓨터에 설치되지 않고 npx를 실행할 때마다 최신 버전을 가져온다.

<br/>

#### 첫 테스트 코드 분석

```js
// App.test.js
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
    render(<App />);
    const linkElement = screen.getByText(/learn react/i);
    expect(linkElement).toBeInTheDocument();
});
```

<br/>

- <strong><code>render</code> 매서드</strong>

    - <strong>제공되는 인수의 (JSX에 관한) 가상 DOM을 생성</strong>

    - <code>screen</code> global 객체로 가상 DOM에 액세스

    - <code>render</code> 매서드와 screen global 객체 모두 RTL의 <code>@testing-library/react</code>를 import해서 가져옴

<br/>

- <strong>screen.getByText(/learn react/i)</strong>

    - <code>screen</code> 객체에서 <code>getByText</code> 매서드를 실행

        - 표시되는 모든 텍스트를 기반으로 DOM에서 요소를 찾는다.

    - <code>getByText</code>의 인수 <code>/learn react/i</code>는 정규 표현식

        - i가 붙으면 문자열의 대소문자 구분 X (case insensitive)

        - 정규 표현식 대신 문자열을 사용해도 된다.

<br/>

- <strong>expect(linkElement).toBeInTheDocument();</strong>

    - Jest 단언문 (Assertion)

    - 테스트 통과 여부를 결정 (테스트 성공과 실패의 원인)

    - expect 매서드 + 매처(Matcher)로 구성

        - expect 매서드 <- Jest 전역 매서드

        - Matcher <- Jest DOM에서 옴

            - Matcher 종류에 따라 인수가 있을 수도 없을 수도 있음

        ```javascript
        test('테스트 이름', 테스트 할 코드를 실행하는 함수 {
            expect(A).toBe(B)
            => '실제값(A)'이 '기대값(B)'이기를 기대한다.
        })
        ```

    - 테스트 통과 원리

        - 테스트는 테스트 함수가 에러를 발생하면 실패한다.

        - 그리고 단언은 예상이 틀렸을 때 에러가 발생하도록 한다.

        - 에러가 없으면 테스트에 통과한다.

<br/>

#### jest-dom

- <code>create-react-app</code>과 함께 제공

- <code>src/setupTests.js</code> 파일을 사용하여 각 테스트 전에 jest-dom을 가져온다.

- 즉, 모든 테스트에서 Jest DOM 매처(Matcher)를 사용할 수 있는 것이다.

    - <code>toBeInTheDocuemnt()</code> 매처는 Jest DOM 매처이다.

<br/>

#### 매처 (Matcher) 의 종류

- <strong>일반적인 매처(Matcher)</strong>

    - 모든 노드에 적용할 수 있음

    - 예 : <code>toBe()</code>, <code>toHaveLength()</code>

- <strong>DOM 기반(based) 매처(Matcher)</strong>

    - 가상 DOM에만 적용할 수 있음

    - 예 : <code>toBeInTheDocuemnt()</code>, <code>toBeVisible()</code>, <code>toBeChecked()</code>

<br/>

### 테스트의 유형

- <strong>유닛 테스트 (Unit Tests)</strong>

    - 보통 함수나 별개의 React 컴포넌트 코드의 한 유닛 혹은 단위를 테스트

    - 유닛끼리 상호 작용하는 것은 테스트하지 않음

- <strong>통합 테스트 (Integration Tests)</strong>

    - 여러 유닛이 함께 작동하는 방식을 테스트

    - 유닛 간의 상호 작용을 테스트  
      (컴포넌트 간의 상호 작용, 마이크로 서비스 간의 상호 작용)

- <strong>기능 테스트 (Functional Tests)</strong>

    - 소프트웨어의 특정 기능을 테스트

    - 코드가 아닌 동작을 테스트

        - 특정 코드 함수가 아닌 소프트웨어의 일반적인 동작을 테스트 (Function의 동작과 관련한 의미)

    - RTL은 기능 테스트를 권장

- <strong>인수 테스트 (Acceptance) 혹은 End-to-End 테스트 (E2E Tests)</strong>

    - 실제 브라우저와, 앱이 연결된 서버가 필요 (Cypress, Selenium이 가장 인기 있는 도구)

    - RTL을 위해 설계된 테스트는 아님

<br/>

### 유닛 테스트 vs 기능 테스트

- <strong>유닛 테스트 (Unit Tests)</strong>

    - 유닛 테스트는 테스트를 최대한 격리

    - 그래서 함수나 컴포넌트를 테스트할 때 의존성을 표시

    - 격리된 유닛에서 실패를 쉽고 정확하게 파악할 수 있다.

<br/><br/>

## 과제 진행

(진행하지 못함)

<br/><br/>

## Feeling
