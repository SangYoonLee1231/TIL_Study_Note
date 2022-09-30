# JavaScript 배열 관련 메서드 정리 (+ 화살표 함수)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 8장 내용

<br/>

### 목차

- <a href=""><code>forEach</code> 메서드</a>
- <a href=""><code>filter</code> 메세드</a>
- <a href="">화살표 함수 (array function)</a>
- <a href=""></a>

<br/><br/>

## <code>forEach</code> 매서드

- 주어진 배열의 각 요소가 순서대로 '<code>forEach</code>의 인자로 주어진 함수'의 인자값으로 넘겨진다.

- 주어진 함수에 인자를 부여하면, 배열의 각 요소를 함수 내부에서 사용할 수 있다.

  ```javascript
  const numList = [1, 2, 3, 4, 5];

  function sayHello(item) {
    console.log("Say Hello to " + item);
  }

  newList = numList.forEach(sayHello);
  ```

  ```
  Say Hello to 1
  Say Hello to 2
  Say Hello to 3
  Say Hello to 4
  Say Hello to 5
  ```

  - <code>forEach</code>문은 <code>numList</code> 배열 내 각각의 <code>item</code>에 대해 <code>sayHello</code> 함수를 실행시킨다.

<br/>

- 화살표 함수(arrow function) <code>=></code>를 활용하면 위 코드를 다음과 같이 줄여서 쓸 수 있다.

  ```javascript
  const numList = [1, 2, 3, 4, 5];

  numList.forEach((item) => console.log("Say Hello to " + item));
  ```

<br/><br/>

## <code>filter</code> 함수

- 주어진 배열을 <strong>필터링</strong>하여 새로운 배열을 생성해 반환한다.

- <code>filter</code> 함수에 인자로 주어진 함수(이하 필터링 함수)가 필터링 역할을 수행한다.

  - <code>[주어진 배열].filter(필터링 함수)</code>

  - <code>forEach</code> 함수와 마찬가지로, 주어진 배열의 각 요소가 순서대로 필터링 함수의 인자값으로 넘겨진다.

  - ✨ 그 중 필터링 함수에서 true로 반환된 요소만 새 배열에 삽입된다.

  ```javascript
  const numList = [1, 2, 3, 4, 5];
  const newList = [];

  function sexyFilter(item) {
    return item != 3;
  }

  const newList = numList.filter(sexyFilter);
  console.log(newList);
  ```

  ```
  [1, 2, 4, 5]
  ```

  <br/>

  - <code>filter</code> 함수 역시 화살표 함수(arrow function) <code>=></code>를 활용하면 코드를 간략하게 쓸 수 있다.

    ```javascript
    const numList = [1, 2, 3, 4, 5];
    const newList = [];

    newList = numList.filter((item) => item > 3);
    console.log(newList);
    ```

    ```
    [4, 5]
    ```

<br/><br/>

## 화살표 함수 (array function)

- 전통적인 함수 표현(function)의 간편한 대안이다.

- <a href="https://ko.javascript.info/arrow-functions-basics">javascript.info '화살표 함수 기본' 링크</a>

  ```javascript
  function title() {
    return (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );
  }
  ```

  ```javascript
  const title = () => (
    <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
      Hello I'm a title
    </h3>
  );
  ```

<br/><br/>

##