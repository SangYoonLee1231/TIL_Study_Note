# 5주차 Day 6-7 TIL

#### 2022.09.03 - 2022.09.04

<br/>

## 배운 것 (간략히 정리)

### 【1】 비동기 처리와 콜백 함수

- '특정 로직'의 실행이 끝날 때까지 기다려주지 않고 나머지 코드를 먼저 실행해주는 것

- 병렬적으로 테스크를 수행하는 방식.

<br/>

- <strong>콜백 함수</strong> : '특정 로직'이 끝났을 때 원하는 동작을 실행시킬 수 있도록 하는 함수

- 콜백 지옥 (Callback hell) : 콜백 함수를 연속해서 사용할 때 발생하는 문제

    - 코드 가독성 저하, 로직 변경의 어려움

<br/>

- 참고 자료

    - <a href="https://poiemaweb.com/js-async">Poiemaweb</a>

    - <a href="https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/">CAPTAIN PANGYO</a>

<br/>

### 【2】 Promise

- 자바스크립트 비동기 처리에 사용되는 객체

- 콜백 지옥을 더 편하게 해결할 수 있다.

    ```javascript
    new Promise(function(resolve, reject) {
        // ...
    });
    ```

<br/>

#### 프로미스의 3가지 상태

- <strong>Pending (대기)</strong> : 비동기 처리 로직이 아직 완료되지 않은 상태

    - <code>new Promise()</code> 매서드 호출 시 대기 상태가 된다.

- <strong>Fulfilled (이행)</strong> : 비동기 처리가 완료되어 Promise가 결과 값을 반환해준 상태

    - <code>resolve</code> 호출 시 이행 상태가 된다.

    - <code>then()</code>을 이용하여 처리 결과 값을 받는다.

- <strong>Rejected (실패)</strong> : 비동기 처리가 실패하거나 오류가 발생한 상태

    - <code>reject</code> 호출 시 실패 상태가 된다.

    - <code>catch()</code>로 실패 처리의 결과 값을 받는다.

<br/>

#### 여러 개의 프로미스 연결하기

<br/>

#### 프로미스 에러 처리 방법

- 프로미스의 reject 매서드가 호출되어 실패 상태가 된 경우

    - <code>then()</code>의 두 번째 인자로 에러를 처리하는 방법

    - <code>catch()</code>를 이용하는 방법