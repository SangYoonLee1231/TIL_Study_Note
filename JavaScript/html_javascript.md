# JavaScript 통해 HTML 요소에 접근하기 + HTML 요소 생성해 삽입하기

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/html_javascript.md#document-%EA%B0%9D%EC%B2%B4object">Document 객체(Object)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/html_javascript.md#js%EC%97%90%EC%84%9C-html-%EC%9A%94%EC%86%8C%EC%97%90-%EC%A0%91%EA%B7%BC%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95">JS에서 HTML 요소에 접근하는 다양한 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/html_javascript.md#js%EB%A5%BC-%ED%86%B5%ED%95%B4-html-%EC%9A%94%EC%86%8C-%EC%83%9D%EC%84%B1%ED%95%98%EC%97%AC-html-%ED%8C%8C%EC%9D%BC%EC%97%90-%EC%82%BD%EC%9E%85%ED%95%98%EA%B8%B0">JS를 통해 HTML 요소 생성하여 HTML 파일에 삽입하기</a>

<br/><br/>

## Document 객체(Object)

- JavaScript를 사용하는 이유는 <strong>HTML과 상호작용</strong>하기 위해서이다.

- 그러기 위해 JS에선 <strong>HTML의 요소(Element)에 접근하고 읽을 수 있도록</strong> 이미 설정되어 있다.

- 이를 통해 우리는 HTML의 요소를 JS를 통해 변경하고 읽을 수 있다.

<br/>

- <strong>document 객체</strong>는 JavaScript에 이미 정의된 객체로, <strong>HTML</strong> 그 자체를 가리킨다.

  ```javascript
  document;
  ```

- <strong>document 객체</strong>를 통해 <strong>HTML 요소에 접근</strong>하고 이를 마음대로 <strong>변경</strong>할 수 있다.

  ```javascript
  document.body; // HTML의 body에 접근할 수 있다.
  document.title; // HTML의 (head 태그 안에 있는) title에 접근한다.
  document.title = "Momentum"; // HTML의 title 값을 "Momentum"으로 변경한다.
  ```

<br/>

- 하지만 <code>div</code>나 <code>h1</code>같은 HTML 요소는 document 객체를 통해 접근하여 JS로 가져올 수 <strong>없다</strong>.  

  즉, document 객체를 통해 접근할 수 있는 HTML 요소가 <strong>한정되어 있다</strong>는 것이다.

- 따라서, 이러한 HTML 요소도 모두 접근할 수 있는 <strong>다른 방법</strong>이 필요하다.

<br/><br/>

## JS에서 HTML 요소에 접근하는 다양한 방법

- HTML에서 특정한 요소를 JS로 가져오기 위해 다양한 <strong>document 맴버 함수</strong>가 존재한다.

  - <strong><code>document.getElementById("hi")</code></strong> : HTML에 "hi" id값을 가진 요소 하나를 찾아 반환
  - <strong><code>document.getElementByClassName("hello")</code></strong> : HTML에 "hello" class 요소를 모두 찾아 <strong>Array</strong>로 반환

  - <strong><code>document.getElementByTagName("h1")</code></strong> : HTML에 "h1" 태그를 모두 찾아 <strong>Array</strong>로 반환

  <br/>

  - ✨ <strong><code>document.querySelector(".hello h1")</code></strong> : <strong>CSS selector</strong>를 통해 HTML의 특정 요소를 찾아 <strong>하나만</strong> 반환  
    (해당되는 요소가 여러 개일 경우 <strong>첫 번째 요소</strong>만 반환)

  - <strong><code>document.querySelectorAll(".hello h1")</code></strong> : <strong>CSS selector</strong>를 통해 해당되는 HTML의 요소 <strong>모두</strong>를 <strong>Array</strong>로 반환  
     (querySelector와 달리, 해당되는 요소를 <strong>전부 배열로 묶어</strong> 반환)

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
    const title = document.getElementById("hi");
    const title2 = document.querySelector("#hi");

    console.log(title); // <div id="hi" class="hello">...</div>
    console.log(title.id); // hi
    console.log(title.className); // hello

    console.log(title2); // <div id="hi" class="hello">...</div>

    const title3 = document.querySelector(".hello h1");

    title3.innerText = "Hello";
    console.log(title3); // <h1>Hello</h1>
    ```

<br/><br/>

## JS를 통해 HTML 요소 생성하여 HTML 파일에 삽입하기

### 생성

- <code>document</code>의 함수 <code>createElement("태그")</code>를 통해 HTML 요소를 생성할 수 있다.

- 이를 변수에 담고, 속성을 부여해 줄 수도 있다.

- 예시 1

  ```javascript
  const newTag = document.createElement("img");
  newTag.src = "img/img.png";
  ```

- 예시 2

  ```javascript
  const li = document.createElement("li");
  const span = document.createElement("span");

  li.appendChild(span);

  span.innerText = "Hello World";
  ```

<br/>

### 삽입

- JS에 생성한 코드를 HTML에 삽입하고자 할 떈, <code>appendChild(태그)</code> 함수를 이용하면 된다.

- 예시 1

  ```javascript
  const element = document.querySelector("ul");
  element.appendChild(li);
  ```

- 예시 2

  - background.js

    ```javascript
    const newTag = document.createElement("img");
    newTag.src = "img/image.png";

    document.body.appendChild(newTag);
    ```

  - 위 JS 코드 실행 결과 (index.html)

    ```html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            ...
        </head>
        <body>
            ...
            <script src="js/background.js" defer></script>
            <!-- 해당 위치에 요소 삽입 -->
            <img src="img/image.png">
        </body>
    </html>

    ```

  - <code>appendChild()</code> 대신 <code>append()</code> 함수를 써도 된다.

  - <code>prepend()</code> 함수를 쓰면 주어진 태그 내부의 최상단에 코드가 삽입된다.