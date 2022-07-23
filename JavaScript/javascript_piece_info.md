# JavaScript - 조각 지식 모음

<br/>

- JavaScript와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%81%AC%EB%A1%AC-%EC%BD%98%EC%86%94%EC%B0%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%A4%84%EB%B0%94%EA%BF%88-%EB%B0%A9%EB%B2%95">크롬 콘솔창에서의 줄 바꿈 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%A6%AC%ED%84%B0%EB%9F%B4-template-literal---%EB%B0%B1%ED%8B%B1%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%91%9C%EA%B8%B0%EB%B2%95">템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#math-%EB%AA%A8%EB%93%88---random-%EA%B8%B0%EB%8A%A5">Math 모듈 - Random 기능</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#jsonstringify---%EB%AA%A8%EB%93%A0-%EA%B2%83%EC%9D%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C-%EB%B3%80%ED%99%98%EC%8B%9C%ED%82%A4%EB%8A%94-%ED%95%A8%EC%88%98"><code>JSON.stringify()</code> - 모든 것을 문자열로 변환시키는 함수</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#foreach%EB%AC%B8"><code>forEach</code>문</a>
- <a href="">화살표 함수 (array function)</a>
- <a href=""></a>

<br/>

### 크롬 콘솔창에서의 줄 바꿈 방법

> 참고 자료 : <a href="https://lemeraldl.tistory.com/588">크롬 콘솔창에서 작업 할때 엔터 키 (개인 블로그)</a>

- 크롬 콘솔창에서 작업 시 줄 바꿈을 하려면, <strong>[Shift] + [Enter]</strong> 두 키를 동시에 누르면 된다.

<br/><br/>

### 템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>, <a href="https://leeborn.tistory.com/entry/JavaScript-ES2015-%EB%B0%B1%ED%8B%B1%EA%B3%BC-%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%AC%B8%EC%9E%90%EC%97%B4">\[JavaScript] ES2015 백틱(`)과 템플릿 문자열 (블로그 포스트)</a>

- 백틱을 사용해 문자열에 변수를 추가할 수 있다.

  ```javascript
  const username = "Jason";
  const message = `Hello ${username}`;
  console.log(message);
  ```

- 백틱 내에선 줄바꿈도 자동으로 적용된다.

  ```javascript
  console.log(`first line
  second line`);
  ```

<br/><br/>

### Math 모듈 - Random 기능

- <strong>0부터 9까지 중 무작위로 숫자 뽑기</strong>

  - <code>Math.random()</code> 코드를 활용한다.

    - 0과 1사이 임의의 소수를 무작위로 반환해주는 코드

  <br/>

  - <code>Math.random()</code>을 통해 임의로 반환된 소수에 <strong>10을 곱한후 소수점을 버린다</strong>.

    ```javascript
    const num = Math.random() * 10;

    /* [방법1] ceil : 올림 */
    const ans = Math.ceil(num) - 1;

    /* [방법2] floor : 버림 */
    const ans = Math.floor(num);

    /* [방법3] round : 반올림 */
    const ans = Math.round(num - 0.5);
    ```

<br/><br/>

### <code>JSON.stringify()</code> - 모든 것을 문자열로 변환시키는 함수

- <code>JSON.stringify(어떤것)</code> 함수는 JS object나 array 또는 어떤 JS 코드이건 간에, 문자열로 변환시켜주는 함수이다.

  ```javascript
  const player = { name: "Sang Yoon Lee" };

  JSON.stringify(player);
  ```

<br/>

- 이를 다시 객체(혹은 배열)로 변환하려면 <code>JSON.parse(어떤것)</code> 함수를 사용하면 된다.

  ```javascript
  JSON.parse(player);
  ```

<br/><br/>

### <code>forEach</code>문

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

### <code>filter</code> 함수

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

### 화살표 함수 (array function)

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
