## JavaScript - 시간과 관련된 함수 및 객체     
(<code>setInterval</code> 함수, <code>setTimeout</code> 함수, <code>Date</code> 객체)

<br/>

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

  - <a href=""></a>
  - <a href=""></a>
  - <a href=""></a>
  - <a href=""></a>
  - <a href=""></a>

<br/><br/>

## <code>setInterval</code> 함수

- <strong><code>setInterval</code> 함수</strong> : 주어진 시간을 주기로 특정 함수를 반복 호출하는 함수

    ```javascript
    function sayHello() {
    console.log("hello");
    }

    setInterval(sayHello, 5000);
    ```

    - <code>setInterval(호출할 함수 이름, 반복 시간 (ms 단위))</code>

<br/>

- 단, 프로그램 시작 후 설정힌 시간 뒤에 함수가 처음으로 호출된다.

- 따라서 프로그램이 시작되자마자 함수가 호출되도록 하려면, 호출할 함수를 <code>setInterval</code> 함수 앞에 따로 선언해주어야 한다.

    ```javascript
    function sayHello() {
    console.log("hello");
    }

    sayHello(); // 따로 선언해주어야 한다.
    setInterval(sayHello, 5000);
    ```

<br/><br/>

## <code>setTimeout</code> 함수

- <strong><code>setTImeout</code> 함수</strong> : 주어진 시간이 흐른 후 특정 함수를 한 번 호출하는 함수

    ```javascript
    function sayHello() {
    console.log("hello");
    }

    setTimeout(sayHello, 5000);
    ```

    - <code>setTimeout(호출할 함수 이름, 지연 시간 (ms 단위))</code>

<br/><br/>

## <code>Date</code> 객체

- <a href="https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date">MDN Web Docs 바로가기</a>

- Date 객체는 현재 시간에 대한 정보를 담고 있다.

    ```javascript
    new Date()
    ```
    ```
    Wed Jul 06 2022 21:31:02 GMT+0900 (한국 표준시)
    ```

<br/>

### 대표적인 Date 객체의 내장 함수

- <code>new Date().getFullYear()</code> : 현재 년도를 반환

- <code>new Date().getMonth()</code> : 현재 몇 월인지 숫자로 반환 (1월 = 0, 2월 = 1, ... , 12월 = 11)

- <code>new Date().getDate()</code> : 현재 이번 달의 몇 일인지 반환

- <code>new Date().getDay()</code> : 현재 무슨 요일인지 숫자로 반환 (일 = 0, 월 = 1, ... , 토 = 6)

- <code>new Date().getHours()</code> : 현재 시각이 몇 시인지 반환

- <code>new Date().getMinutes()</code> : 현재 시각이 몇 분인지 반환

- <code>new Date().getSeconds()</code> : 현재 시각이 몇 초인지 반환

<br/><br/>

## 활용

### 현재 시간을 실시간으로 알려주는 전자 시계 만들기

- Step 1 > <code>Date</code>객체와 <code>setInterval()</code>함수를 활용하여 기능 구현하기

    - index.html

        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
                ...
            </head>
            <body>
                ...
                <h2 id="clock">00:00:00</h2>
                ...
                <script src="js/greetings.js" defer></script>
                <script src="js/clock.js" defer></script>
            </body>
        </html>
        ```

    - clock.js

        ```javascript
        const clock = document.querySelector("h2#clock");

        function getClock() {
            const date = new Date();
            const hour = date.getHours();
            const min = date.getMinutes();
            const sec = date.getSeconds();
            clock.innerText = `${hour}:${min}:${sec}`;
        }

        getClock();
        setInterval(getClock, 1000);
        ```

    - <strong>문제점</strong> : 숫지가 한 자리일 때 한 자리의 공간만 표시해준다. ex) 17:01:8

<br/>

- Step 2 > <code>padStart()</code> 함수를 추가하여 자리 수 맞추기 (Step 1 문제점 해결)

    - <code>padStart()</code> 함수 : 문자열 앞에 새 문자열을 삽입하여, 문자열을 원하는 길이로 만드는 함수

        - <code>"문자열".padStart(원하는 문자열 길이, "짧을 경우 앞에 삽입할 문자열")</code>

        ```javascript
        "1".padStart(2, "0");
        ```
        ```
        "01"
        ```

        <br/>

        ```javascript
        "12".padStart(2, "0");
        ```
        ```
        "12"
        ```

    <br/>

    - 코드

    - index.html

        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
                ...
            </head>
            <body>
                ...
                <h2 id="clock">00:00:00</h2>
                ...
                <script src="js/greetings.js" defer></script>
                <script src="js/clock.js" defer></script>
            </body>
        </html>
        ```

    - clock.js

        ```javascript
        const clock = document.querySelector("h2#clock");

        function getClock() {
            const date = new Date();

            // 숫자로 반환되기 때문에, 문자열로 형변환 후 padStart() 함수를 적용해줘야 한다.
            const hour = String(date.getHours()).padStart(2, "0");
            const min = String(date.getMinutes()).padStart(2, "0");
            const sec = String(date.getSeconds()).padStart(2, "0");

            clock.innerText = `${hour}:${min}:${sec}`;
        }

        getClock();
        setInterval(getClock, 1000);
        ```