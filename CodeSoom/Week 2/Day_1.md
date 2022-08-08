# 2주차 Day 1 TIL

#### 2022.08.08

<br/>

## 배운 것 (간략히 정리)

### 【1】 React

- <strong>React 탄생 배경</strong>

    - 자바스크립트의 중요성이 커지면서, JS로 대부분의 처리를 하는 Single Page Application이 등장

    - 이를 바탕으로, 작은 컴포넌트들이 모여 하나의 웹 페이지를 구성하도록 하는 Angular 프레임워크가 등장

    - 하지만 이렇게 되니 데이터의 흐름을 파악하기 너무 어려워지는 문제가 발생

    - 이를 해결하기 위해 데이터의 흐름을 명확히 파악할 수 있도록 페이스북에서 개발한 React 프레임워크가 등장

<br/>

- <strong>React 핵심 개념</strong>

    - Angular처럼 (재사용이 가능한) 컴포넌트(Component)를 조합하여 웹사이트(앱)를 만드는데 도움을 주는 라이브러리 이다.

    - 가상 DOM을 생성하고, render시 이를 실제 DOM과 비교하여 변화된 부분만 찾아 앱에 반영한다.

    - 일방향적인 데이터 흐름을 보여준다.

        - state ⇒ component ⇒ 가상 DOM ⇒ 실제 DOM과 비교 ⇒ 화면에 그리기

        - (아직 React를 많이 사용해보지 않아, 이 부분에 대한 개념이 잘 와닿진 않는다.)

    - React는 UI 라이브러리에 불과하다. 하지만 이로 인해 오히려 다른 플랫폼에서도 React를 활용할 수 있다.

<br/>

- <strong>ReactDOM</strong>

    - React에서 DOM에 특화된 메서드를 사용할 수 있도록 API를 제공한다.
    
    - 예를 들면, React 요소들을 DOM으로 렌더링하는 <code>render</code> 함수를 제공한다.

<br/>

- <strong>React 프로젝트를 위한 기본 세팅</strong>

    - 리엑트 설치 : <code>npm install react react-dom</code>

    - 스크립트에서 React.createElement가 JSX를 컴파일 할 수 있도록, React를 직접 사용하지 않더라도 import 해줘야 된다.
    
        ```javascript
        import React from 'react';
        import ReactDOM from 'react-dom';
        ```

<br/>

- <strong>React 관련 추가 학습</strong>

    - <a href="https://velog.io/@yesbb/virtual-dom의-성능이-더-좋은이유">왜 virtual dom이 더 좋은가? (feat.React fiber)</a>

    - <a href="https://github.com/appear/reactjs-interview-questions-ko">reactjs-interview-questions-ko ✨</a>

<br/><br/>

### 【2】 1주차 복습 (코드 이해하기) + α

- <strong>복습 이유</strong>

    - 저번 주 과제 코드를 다시 봤는데, 이게 무슨 코드인지 도저히 이해가 되지 않았다.

    - 아직 난 React 코드에 익숙치 않고 JavaScript 문법도 모르는 내용이 너무 많은 것 같다.

    - 이대로 그냥 진행하면 2주차 과제는 손대기도 힘들 것 같아, 코드 이해를 위주로 1주차 내용을 다시 복습해보기로 했다.

<br/>

- <strong>createElement 함수 구현 복습</strong>

    - 1주차 강의를 돌려보며 <strong>createElement 함수를 구현하는 과정부터</strong> 다시 천천히 살펴보았다.

    - <strong>과제 1 해설코드</strong>까지 이해 완료


    <br/>

    - <strong>복습 중 추가 학습</strong> 

        - <strong>논리 연산자 || - JS 추가 기능</strong>

            - 각 피연산자 중 맨 왼쪽 값부터 순서대로 불린형으로 변환한다.

            - 변환 값이 <code>true</code>인 첫 번째 피연산자를 찾아 변환 전 원래 값을 반환한다.

            - 모든 피연산자가 <code>false</code>라면 제일 마지막 피연산자를 원래 값으로 반환한다.

        - <strong>Guard Clause 학습</strong>

            - if/else문을 중첩하여 사용하면 가독성이 떨어지기에, 이를 방지하기 위한 방법

            - 중첩된 조건문을 평탄화

            - <code>if (guard) {...}</code> => <code>if(not guard) { return; } ...</code>

                - guard 조건을 not guard의 조건으로 바꾸고 조기에 return한다. (return early)
                
                -  그 다음, 기존의 guard 조건을 가진 분기의 코드 블록(<code>...</code>)을 not guard 이후에 작성한다.

<br/><br/>

## 과제 진행

(진행 하지 못함)

<br/><br/>

## Feeling

- 저번 주에 힘을 많이 쓴 탓일까, 이번 주는 의욕이 좀 떨어진 것 같다.

- 공부를 많이 하긴 했으나 저번 주 월요일만큼 하진 못했다. 게다가 오늘은 코테 대비 수업도 있었고.

- 조금 아쉬운 하루였다. 코드숨 교육을 끝까지 잘 소화하려면 <strong>페이스 조절도 잘 해야할 것 같다.</strong>

- 오늘은 일부러 조금 설렁설렁 했으니 내일은 다시 최선을 다해보자.

<br/>

- 오늘 첫 날은 이번 주 새 진도를 나가는 것보다 저번 주 이해하지 못한 부분을 복습하는 것에 더 치중했다.

- 그 이유는 저번 주 과제 코드를 이해하지 못하는 내 모습을 보고 이대로 가면 안되겠다는 생각이 들었기 때문이다.

- 아무래도 옳은 선택을 한 것 같다.  
복습해보니 (나도 모르게) 이해하지 못하고 그냥 넘어갔던 부분에서 '아하' 모멘트가 여러 번 왔다.

- 과제 1 해설코드를 기준으로 <strong>아래 두 가지만 결국 이해하지 못했고</strong> 나머지 코드는 비로소 다 이해했다.

    - 11번째 줄에서 flat 함수를 쓴 이유

        ```javascript
        children.flat().forEach((child) => { ...
        ```

    - 함수를 축약해서 쓸 때 내부 코드 불록을 언제 중괄호로 묶는지 아님 소괄호로 묶는지

        ```javascript
        <p>
            {[1, 2, 3].map((i) => (
            <button type="button" onClick={() => handleClick(i)}>
                {i}
            </button>
            ))}
        </p>
        ```
<br/>

- 내일은 저번 주 과제 2 코드도 한 번 잘 이해해보고 2주차 진도도 쭉쭉 빼서 될 수 있으면 새로운 과제까지 한 번 건드려보자.
