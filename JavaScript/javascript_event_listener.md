# JavaScript - 이벤트 리스너 (Event Listener)

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_event_listener.md#%EC%84%9C%EB%A1%A0">서론</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_event_listener.md#%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A6%AC%EC%8A%A4%EB%84%88-event-listener">이벤트 리스너 (Event Listener)</a>
- <a href="">이벤트 종류</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 서론

- HTML에서 특정한 요소를 JS로 가져온 후 그 요소(element)의 <strong>내부</strong>를 보려면, 다음과 같이 코드를 작성하면 된다.

    ```javascript
    console.dir(element 이름);
    ```

    <br/>

    <img src="img/console_dir1.png"> <img src="img/console_dir2.png">

    <br/>

    - 그럼 위과 같이 object로 표시한 element를 전부 볼 수 있다. (✨<strong>이 항목들은 모두 JavaScript Object이다.</strong>)

    - 이 중에서 앞에 <code>on</code>이 붙은 요소들이 바로 <strong>event</strong>이다.

<br/>

- HTML의 요소 중엔 <code>style</code>이란 Object도 존재한다.  

    즉, <strong>JS로 특정 요소의 style도 바꿀 수 있다</strong>는 소리다.

    ```javascript
    const title = document.querySelector(".hello:first-child h1");

    title.style.color = "blue";
    ``` 

<br/><br/>

## 이벤트 리스너 (Event Listener)

- <strong>이벤트 (Event)</strong> : 어떤 행위를 하는 것

    - 예) 클릭, 입력 끝내기, 이름 적기, enter 누르기, wifi에서 접속 헤제 등등

- JavaScript는 이 모든 이벤트를 listen할 수 있다.

<br/>

- <strong><code>eventListener</code></strong> : event를 listen한다.

- <strong><code>title.addEventListener("click")</code></strong> : title이 <strong>click</strong>되는 event를 listen한다.

<br/>

- 이 때, 특정 이벤트가 listen될 시, 어떤 동작이 이루어지게 할 것인지를 설정하기 위해  

     <strong>새로운 함수를 선언</strong>하여 <code>addEventListener</code> 함수에 연결해준다.

    ```javascript
    function handleTitleClick() {
        console.log("Title was clicked!");
    }

    title.addEventListener("click", handleTitleClick);
    ```

<br/>

- 함수 사용 예시

  - index.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        ...
        <title>Momentum App</title>
      </head>
      <body>
        <div id="hi" class="hello">
          <h1>Grab Me! 1</h1>
        </div>
        <div class="hello">
          <h2>Grab Me! 2</h2>
        </div>
        <div class="hello">
          <h3>Grab Me! 3</h3>
        </div>
        <script src="js/app.js"></script>
      </body>
    </html>
    ```

  - app.js

    ```javascript
    const title = document.querySelector(".hello:first-child h1");

    console.log(title);
    title.innerText = "Click Me!";
    console.log(title);

    function handleTitleClick() {
        console.log("Title was clicked!");
        title.style.color = "blue";
    }

    title.addEventListener("click", handleTitleClick);
    ```

<br/><br/>

## 이벤트 종류

- listen하고 싶은 event를 찾는 한 가지 방법으로 <code>console.dir(element 이름);</code>을 통해 어떤 요소의 내부를 확인하면, 앞에 <code>on</code>이 붙은 다양한 <strong>event</strong> 요소들을 확인할 수 있다.

  <img src="img/console_dir2.png">

<br/>

- listen하고 싶은 event를 찾는 <strong>가장 좋은 방법</strong>은 mdn web docs 페이지에 찾아가서 확인하는 것이다.  
👉 <a href="https://developer.mozilla.org/ko/docs/Web/Events">바로가기</a>

<br/>

- 대표적인 event 예시 (노마드코더 강의에서 소개한)

  - <code>click</code> : 마우스로 해당 요소를 클릭할 때
  - <code>mouseenter</code> : 마우스를 해당 요소에 올렸을 때
  - <code>mouseleave</code> : 마우스를 해당 요소에 올린 후 벗어날 때

<br/>

- 코드 예시

  ```javascript
  const title = document.querySelector(".hello:first-child h1");

  title.innerText = "Click Me!";

  function handleTitleClick() {
    console.log("Title was clicked");
    title.style.color = "blue";
  }

  function handleMouseEnter() {
    title.innerText = "Mouse is here";
  }

  function handleMouseLeave() {
    title.innerText = "Mouse is gone";
  }

  title.addEventListener("click", handleTitleClick);
  title.addEventListener("mouseenter", handleMouseEnter);
  title.addEventListener("mouseleave", handleMouseLeave);
  ```