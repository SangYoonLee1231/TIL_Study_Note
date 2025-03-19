# JavaScript - Promise 객체

> 참고 자료 : 책 '모단 자바스크립트 Deep Dive'

<!-- <br/> -->

<br/><br/>

## 비동기 처리란?

- JavaScript는 기본적으로 <strong>싱글 스레드(Single-thread)</strong>에서 동작하며, 한 번에 하나의 작업만 실행할 수 있다.

- 하지만, 네트워크 요청, 파일 읽기, 타이머 같은 **비동기 작업**을 처리하기 위해 <strong>이벤트 루프(Event Loop)</strong>와 <strong>비동기 API(Web API)</strong>를 활용한다.

- 비동기 작업의 대표적인 예시는 다음과 같다.

  - **네트워크 요청**: `fetch()`, `XMLHttpRequest`
  - **타이머**: `setTimeout()`, `setInterval()`
  - **이벤트 리스너**: `addEventListener()`
  - **파일 읽기/쓰기**: `FileReader`, `fs.readFile()`

- JavaScript는 이러한 비동기 작업이 완료될 때까지 기다리지 않고, 나머지 코드들을 먼저 실행하며

  <strong>이벤트 루프(Event Loop)</strong>를 통해 비동기 코드가 실행될 수 있도록 한다.

<br/><br/>

## Promise 객체란?

### (1) Promise의 개념

- `Promise`는 **비동기 작업의 완료 또는 실패를 나타내는 객체**이다. 네트워크 요청처럼 시간이 걸리는 작업을 수행하고, **작업이 완료되었을 때 결과 값을 제공하거나 실패 시 오류를 반환**한다.

<br/>

### (2) Promise의 상태

- Promise 객체는 다음 **세 가지 상태**를 가진다.

  - **Pending (대기 상태)**: 비동기 작업이 아직 완료되지 않은 초기 상태
  - **Fulfilled (성공 상태)**: 비동기 작업이 성공적으로 완료되어 결과를 반환한 상태
  - **Rejected (실패 상태)**: 비동기 작업이 실패하여 오류를 반환한 상태

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Success!"); // 1초 후 성공 처리
  }, 1000);
});

console.log(promise); // Promise { <pending> }
```

<br/><br/>

## Promise 객체의 활용

### (1) `.then()`과 `.catch()`를 사용한 비동기 처리

- `Promise`는 `.then()`을 사용하여 성공적인 결과를 처리하고, `.catch()`를 사용하여 에러를 처리할 수 있다.

```js
fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then((response) => response.json()) // 응답을 JSON으로 변환
  .then((data) => console.log(data)) // 변환된 데이터를 출력
  .catch((error) => console.error("Error:", error)); // 오류 처리
```

- `.then()`을 통해 비동기 작업의 결과를 순차적으로 처리할 수 있다.
- `.catch()`를 사용하면 네트워크 요청 실패 시 오류를 잡아낼 수 있다.

<br/>

### (2) `setTimeout`을 Promise로 감싸기

- JavaScript의 `setTimeout`은 기본적으로 `Promise`를 반환하지 않는다. 이를 직접 `Promise`로 감싸면 더욱 유연하게 사용할 수 있다.

```js
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

delay(2000).then(() => console.log("2초 후 실행"));
```

<br/><br/>

## 직접 구현한 Promise 클래스

### (1) 간단한 형태의 Promise 클래스 구현

```js
class MyPromise {
  // 생성자
  constructor(promiseCallback) {
    this.promiseCallback = promiseCallback;
    promiseCallback(this.resolve.bind(this), this.reject);
    this.thenCallback = [];
  }

  // resolve의 매개변수를 then의 콜백 함수의 매개변수로 전달
  resolve(message) {
    this.thenCallback[0](message);
  }

  reject() {}

  // 전달받은 콜백을 등록한다.
  then(fn) {
    this.thenCallback.push(fn);
  }
}

const myPromise = new MyPromise((resolve, reject) => {
  setTimeout(() => {
    resolve("success");
  }, 1000);
});

myPromise.then((successMessage) => {
  console.log(successMessage);
});
```

<br/>

### (2) 다시 구현해본 Promise 클래스

```js
class MyPromise2 {
  // 생성자: resolve와 reject 함수를 매개변수로 받는 함수 실행
  constructor(fn) {
    fn(this.resolve.bind(this), this.reject.bind(this));
    this.thenCallback = [];
    this.i = 0;
  }

  // resolve 함수 -> then 콜백 함수 실행, 매개변수를 then의 콜백 매개변수로 전달
  resolve(message) {
    this.thenCallback[this.i](message);
    this.i++;
  }

  // reject 함수 -> then 콜백 함수 실행, 매개변수를 then의 콜백 매개변수로 전달
  reject() {}

  // then 콜백 함수 등록
  then(cb) {
    this.thenCallback.push(cb);
  }
}

let myFirstPromise = new MyPromise2((resolve, reject) => {
  setTimeout(() => {
    resolve("Success!");
  }, 1000);
});

myFirstPromise.then((successMessage) => {
  console.log("Yay! " + successMessage);
});
```

<br/><br/>

## async/await과 Promise의 관계

### (1) async/await의 개념

`async/await`는 `Promise`를 더욱 쉽게 사용할 수 있도록 도와주는 문법적 기능(Syntactic Sugar)이다.  
기본적으로 `async` 키워드가 붙은 함수는 항상 `Promise`를 반환하며, 함수 내부에서 `await` 키워드를 사용하면 `Promise`가 해결될 때까지 **해당 함수의 실행이 일시 중단**된다.

```js
async function fetchData() {
  return "Hello";
}

console.log(fetchData()); // Promise { "Hello" }
```

위 코드에서 `async function fetchData()`는 자동으로 `Promise`를 반환하며, `fetchData()`를 호출하면 `Promise (Pending)` 상태가 반환된다.

<br/>

### (2) await을 사용하여 Promise 값을 기다리기

`await` 키워드는 `Promise`가 완료될 때까지 **함수 실행을 일시 중단**한 후, `Promise`가 해결되면 그 값을 반환한다.

```js
async function getTodo() {
  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}
getTodo();
```

#### 코드 실행 흐름

1. `fetch()`가 실행되면서 `Promise (Pending)` 상태가 반환된다.
2. `await fetch(...)`를 만나면, **해당 함수(`getTodo`)의 실행이 일시 중단**되지만, JavaScript의 이벤트 루프는 다른 동기 코드 실행을 계속할 수 있다.
3. 네트워크 요청이 완료되면 `response` 변수에 응답이 저장되고, 다음 줄의 `await response.json();`이 실행된다.
4. JSON 변환이 완료되면 데이터가 `data` 변수에 저장되고, 마지막으로 `console.log(data);`가 실행된다.

<br/>

### (3) Promise와 async/await 비교

| 방식        | `Promise.then()`                      | `async/await`                                      |
| ----------- | ------------------------------------- | -------------------------------------------------- |
| 코드 가독성 | 체이닝이 길어질 경우 가독성이 떨어짐  | 동기 코드처럼 직관적으로 보임                      |
| 예외 처리   | `.catch()` 사용                       | `try...catch` 사용                                 |
| 실행 방식   | 이벤트 루프를 통해 `.then()`이 실행됨 | `await`이 `Promise`가 끝날 때까지 함수 실행을 중단 |

<br/>

#### **예제 비교**

##### **Promise 체이닝 방식**

```js
fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

##### **async/await 방식**

```js
async function getTodo() {
  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}
getTodo();
```

- `async/await`을 사용하면 코드가 더욱 간결해지고 가독성이 좋아진다.

<br/>

### (4) 이벤트 루프와 async/await의 관계

JavaScript는 <strong>비동기 실행 모델(Asynchronous Execution Model)</strong>을 사용하며, <strong>이벤트 루프(Event Loop)</strong>가 이를 관리한다.

1. `fetch()`가 호출되면 브라우저의 **Web API**가 네트워크 요청을 처리하고 <strong>Promise (Pending 상태)</strong>를 반환한다.
2. 자바스크립트는 `then()`을 만나도 실행을 멈추지 않고 다음 동기 코드를 계속 실행한다.
3. 네트워크 요청이 완료되면 <strong>마이크로태스크 큐(Microtask Queue)</strong>에 `then()` 콜백을 등록하고, 이벤트 루프가 메인 스레드가 비었을 때 실행한다.
4. `await`은 `Promise`가 완료될 때까지 <strong>해당 함수의 실행을 일시 중단(suspend)</strong>하지만, 전체 프로그램은 멈추지 않고 다른 작업을 수행할 수 있다.

<br/><br/>
