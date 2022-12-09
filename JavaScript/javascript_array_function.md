# JavaScript - 배열 관련 메서드 정리 (+ 화살표 함수)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 8장 내용

<br/>

### 목차

- <a href="">화살표 함수 (array function)</a>
- <a href=""><code>forEach</code> 메서드</a>
- <a href=""><code>filter</code> 메세드</a>
- <a href=""><code>map</code> 메세드</a>

<br/><br/>

## 화살표 함수 (array function)

- 전통적인 함수 표현(function)의 간편한 대안이다.

- 익명의 함수를 선언해 변수에 할당하는 방식으로 사용한다.

- <a href="https://ko.javascript.info/arrow-functions-basics">javascript.info '화살표 함수 기본' 링크</a>

<br/>

- <storng>코드 예시</storng>

  ```javascript
  function title() {
    return (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );
  }
  ```

- 아래 두 함수는 위 <code>title</code> 함수를 화살표 함수로 나타낸 것이다.

  - 예시 1 : <strong>중괄호</strong> 사용 (내부에는 <strong>함수 본문 내용</strong>을 작성)

    ```javascript
    const title = () => {
      return (
        <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
          Hello I'm a title
        </h3>
      );
    };
    ```

  - 예시 2 : <strong>소괄호</strong> 사용 (내부에한 함수의 <strong>반환값</strong>을 작성)

    ```javascript
    const title = () => (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );
    ```

    - 소괄호는 반환값이 간단할 경우 생략 가능하다.



<br/><br/>

## <code>forEach</code> 함수

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

## <code>map</code> 함수

- 주어진 배열의 각 요소을 대상으로 '함수'를 실행하고, 그 결과를 새로운 배열로 반환해준다.

  - 이 '함수'는 <code>map</code>에 인자로 넣은 함수아다.

- 새로운 배열을 반환해주므로, <strong>이를 변수에 할당해주어야 사용할 수 있다.</strong>

  - 어딘가에 할당해주지 않고 <code>newArr.map((item) => Number(item));</code> 이런 식으로만 쓴다면 아무 일도 일어나지 않는다.

<br/>

- <storng>코드 예시</storng>

  ```js
  let array = [ '1', '1', '1\r' ];

  array = array.map((item) => Number(item));

  console.log(array); // [ 1, 1, 1 ]
  ```
