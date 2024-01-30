# JavaScript 기본 7 - 함수

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 15장 내용

<br/>

### 목차

- <a href="">함수</a>
- <a href="">지역 변수, 전역 변수</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 함수

- 여러 번 쓰이는 코드를 블록 단위로 묶어 함수로 만들면, 중복되는 코드를 줄일 수 있다.

<br/>

### 함수 선언 및 호출 방법 (간단 정리)

- 기본 포멧은 아래와 같다.

  ```javascript
  function func(x) {
    x += 10;

    return x;
  }

  let val = func(10);
  alert(val);
  ```

### 용어정리

- <strong>매개변수 (parameter)</strong> : 인수 (argument) 라고도 불리며, 함수의 입력값에 해당한다. 없을 수도 있다.

  - 매개변수(parameter)는 이름이고 인자(argument)는 값이다.

- <strong>함수 본문 (body)</strong> : 함수의 대괄호 내 영역으로 함수의 기능을 구현하는 코드의 모임이다.

- <strong>반환 값 (<code>return</code>)</strong> : 함수의 출력값이다. 함수 호출 시, 그 함수는 자신의 기능을 수행한 후 호출한 그 곳에 특정값을 반환한다. 반환 값이 없을 수도 있다.  
  (자세한 내용은 아래에서 다룬다)

  - 반환 값이 없어도 함수는 무언가를 반환한다. 그 무언가는 <code>undefined</code>다.

<br/><br/>

## 지역 변수, 전역 변수

- 함수 내부에서 선언한 변수를 <strong>지역 변수</strong>, 함수 외부에서 선언한 변수를 <strong>전역 변수</strong>라 한다.

- 전역 변수는 <strong>같은 이름을 가진 지역 변수에 의해 가려지지만 않는다면</strong> 모든 함수에서 접근할 수 있다.

- 헷갈리기 쉬운 두 예제

  ```javascript
  let userName = "John";

  function showMessage() {
    userName = "Bob"; // (1) 외부 변수를 수정함

    let message = "Hello, " + userName;
    alert(message);
  }

  alert(userName); // 함수 호출 전이므로 John 이 출력됨

  showMessage();

  alert(userName); // 함수에 의해 Bob 으로 값이 바뀜
  ```

  ```javascript
  let userName = "John";

  function showMessage() {
    let userName = "Bob"; // 같은 이름을 가진 지역 변수를 선언

    let message = "Hello, " + userName; // Bob
    alert(message);
  }

  // 함수는 내부 변수인 userName만 사용
  showMessage();

  alert(userName); // 함수는 외부 변수에 접근하지 않는다. 따라서 값이 변경되지 않고, John이 출력된다.
  ```

- 전역 변수는 되도록 사용하지 않는 것이 좋다. 다만 전역 변수를 쓰는 것이 유용한 경우도 있다.

<!-- <br/><br/>

## 매개변수 기본값 -->
