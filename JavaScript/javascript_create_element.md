# JavaScript - JS로 HTML 요소를 생성하여 삽입하기 (<code>createElement</code>)

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>

<br/><br/>

## JS로 HTML 요소를 생성하여 삽입하기

### 생성

- <code>document</code>의 함수 <code>createElement("태그")</code>를 통해 HTML 요소를 생성할 수 있다.

- 이를 변수에 담고, 속성을 부여해 줄 수도 있다.

    ```javascript
    const newTag = document.createElement("img");
    newTag.src = "img/img.png";
    ```

<br/>

### 삽입

- JS에 생성한 코드를 HTML에 삽입하고자 할 떈, <code>appendChild(태그)</code> 함수를 이용하면 된다.

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