# JavaScript - 이벤트 활용하기

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_event_listener_utilize.md#%EC%A0%9C%EB%AA%A9%EC%9D%84-%ED%81%B4%EB%A6%AD%ED%95%A0-%EB%95%8C%EB%A7%88%EB%8B%A4-2%EA%B0%9C%EC%9D%98-%EA%B8%80%EC%94%A8-%EC%83%89%EC%9D%B4-%EB%B2%88%EA%B0%88%EC%95%84%EA%B0%80%EB%A9%B0-%EB%B0%94%EB%80%8C%EB%8A%94-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0">제목을 클릭할 때마다 2개의 글씨 색이 번갈아가며 바뀌는 이벤트 만들기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_event_listener_utilize.md#%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A6%AC%EC%8A%A4%EB%84%88%EC%9D%98-%EC%B2%AB-%EC%9D%B8%EC%9E%90event%EB%A5%BC-%ED%86%B5%ED%95%B4-%EC%9D%B4%EB%B2%A4%ED%8A%B8%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EB%8F%99%EC%9E%91-%EB%A7%89%EA%B8%B0">이벤트 리스너의 첫 인자(event)를 통해 이벤트의 기본 동작 막기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_event_listener_utilize.md#input-%EA%B3%B5%EA%B0%84%EC%97%90-%EC%9D%B4%EB%A6%84%EC%9D%84-%EC%9E%85%EB%A0%A5-%ED%9B%84-sumbit%EC%8B%9C-form-%EC%9A%94%EC%86%8C%EA%B0%80-%EC%82%AC%EB%9D%BC%EC%A7%80%EA%B3%A0-%EC%9E%85%EB%A0%A5%ED%95%9C-%EC%9D%B4%EB%A6%84%EC%9D%B4-%ED%99%94%EB%A9%B4%EC%97%90-%EC%B6%9C%EB%A0%A5%EB%90%98%EB%8F%84%EB%A1%9D-%ED%95%98%EA%B8%B0">input 공간에 이름을 입력 후 sumbit시, form 요소가 사라지고 입력한 이름이 화면에 출력되도록 하기</a>

<br/><br/>

### 제목을 클릭할 때마다 2개의 글씨 색이 번갈아가며 바뀌는 이벤트 만들기

- <strong>【방법 1】 style 클래스에 직접 접근하는 방법 (JS만을 활용)</strong>

  ```javascript
  const h1 = document.querySelector(".hello:first-child h1");

  // 옵션 1
  function handleTitleClick() {
    const currentColor = h1.style.color;
    let newColor;
    if (currentColor === "blue") {
      newColor = "tomato";
    } else {
      newColor = "blue";
    }
    h1.style.color = newColor;
  }

  h1.addEventListener("click", handleTitleClick);
  ```

- <strong>문제점</strong> : JS는 애니메이션에 적합한 도구고, CSS는 style 작업에 적합한 도구다. JS에서 style 작업까지 다루는 것은 좋지 않다.

<br/>

- <strong>【방법 2】 JS으로 클래스 이름을 HTML 요소에 추가하는 방법</strong>

  - style.css

    ```css
    body {
      background-color: beige;
    }
    h1 {
      color: cornflowerblue;
      transition: color 0.5s ease-in-out;
    }
    .clicked {
      color: tomato;
    }
    ```

  - app.js

    ```javascript
    const h1 = document.querySelector(".hello:first-child h1");
    function handleTitleClick() {
      const clickedClass = "clicked";
      if (h1.className === clickedClass) {
        h1.className = "";
      } else {
        h1.className = clickedClass;
      }
    }
    ```

- <strong>문제점</strong> : className으로 인해 기존 HTML 요소에 있던 클래스를 모두 잃을 수 있다.

<br/>

- <strong>【방법 3】 JS의 classList를 활용하여 클래스 이름을 HTML 요소에 추가하는 방법</strong>

  - style.css

    ```css
    body {
      background-color: beige;
    }
    h1 {
      color: cornflowerblue;
      transition: color 0.5s ease-in-out;
    }
    .clicked {
      color: tomato;
    }
    ```

  - app.js

    ```javascript
    const h1 = document.querySelector(".hello:first-child h1");

    function handleTitleClick() {
      const clickedClass = "clicked";
      if (h1.classList.contains(clickedClass)) {
        h1.classList.remove(clickedClass);
      } else {
        h1.classList.add(clickedClass);
      }
    }

    h1.addEventListener("click", handleTitleClick);
    ```

<br/>

- <strong>【방법 4】 JS classList의 toggle 함수를 활용하는 방법 (✨추천)</strong>

  - classList의 <code>toggle</code>함수는 class 이름이 요소에 존재하는지 확인한 후, <strong>해당 class 이름이 있으면 이를 제거하고, 없으면 추가한다.</strong>

  - style.css

    ```css
    body {
      background-color: beige;
    }
    h1 {
      color: cornflowerblue;
      transition: color 0.5s ease-in-out;
    }
    .clicked {
      color: tomato;
    }
    ```

  - app.js

    ```javascript
    function handleTitleClick() {
      // clicked 클래스를 한 번만 사용하기 때문에, 따로 변수를 선언해 줄 필요는 없다.
      h1.classList.toggle(clicked);
    }

    h1.addEventListener("click", handleTitleClick);
    ```

<br/><br/>

### 이벤트 리스너의 첫 인자(event)를 통해 이벤트의 기본 동작 막기

- 모든 EventListener 함수의 <strong>첫 번째 인수</strong>는 항상 <strong>방금 일어난 이벤트에 대한 정보</strong>를 담고 있다.

- <code>event.preventDefault()</code> 이 코드를 통해 실행된 함수 <code>preventDefault</code>는 어떤 이벤트의 기본 행동이 발생하지 않도록 막는다.

  - 기본 행동 : 어떤 함수에 대해 브라우저가 기본적으로 수행하는 동작

- index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      ...
    </head>
    <body>
      <form id="login-form">
        <input
          required
          maxlength="15"
          type="text"
          placeholder="What is your name?"
        />
        <button>Log In</button>
      </form>
      <a href="https://nomadcoders.co">Go to courses</a>
      <script src="js/app.js" defer></script>
    </body>
  </html>
  ```

- app.js

  ```javascript
  const loginForm = document.querySelector("#login-form");

  const link = document.querySelector("a");

  function onLoginSubmit(event) {
    event.preventDefault(); // 기본 동작인 submit이 되지 않음
    console.log(event);
  }

  function handleLinkClick(event) {
    event.preventDefault(); // 기본 동작인 다른 페이지로 이동이 되지 않음
    console.log(event);
  }

  loginForm.addEventListener("submit", onLoginSubmit);
  link.addEventListener("click", handleLinkClick);
  ```

- 이벤트의 기본 행동

  - <code>form</code> : submit
  - <code>a(링크)</code> : 클릭 시 다른 페이지로 이동

<br/><br/>

### input 공간에 이름을 입력 후 sumbit시, form 요소가 사라지고 입력한 이름이 화면에 출력되도록 하기

- CSS hidden 이라는 class를 만들어 이를 활용한다.

  ```css
  .hidden {
    display: none;
  }
  ```

<br/>

- 우선 h1 요소에 <code>hidden</code> class를 추가하여 화면에서 가려준다.

- 그리고 sumbit시, form 요소에 <code>hidden</code> class를 추가하고, 반대로 h1 요소의 <code>hidden</code> class를 제거한다.

<br/>

- index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    ...
    <link rel="stylesheet" href="css/style.css" />
    <title>Momentum App</title>
  </head>
  <body>
    <form id="login-form">
      <input
        required
        maxlength="15"
        type="text"
        placeholder="What is your name?"
      />
      <button>Log In</button>
    </form>
    <h1 id="greeting" class="hidden"></h1>
    <script src="js/app.js" defer></script>
  </body>
</html>
```

- style.css

  ```css
  .hidden {
    display: none;
  }
  ```

- app.js

  ```javascript
  const loginForm = document.querySelector("#login-form");
  const loginInput = document.querySelector("#login-form input");
  const greeting = document.querySelector("#greeting");

  const HIDDEN_CLASSNAME = "hidden";

  function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME);
    greeting.classList.remove(HIDDEN_CLASSNAME);
    const username = loginInput.value;
    greeting.innerText = `Hello ${username}`;
  }

  loginForm.addEventListener("submit", onLoginSubmit);
  ```

<br/>

- 백틱을 활용해 문자열에 변수를 추가할 수 있다.

  ```javascript
  const username = "Jason";
  const message = `Hello ${username}`;
  console.log(message);
  ```

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md">조각 지식 모음</a>에 해당 내용을 따로 정리해두었다.

<br/>
