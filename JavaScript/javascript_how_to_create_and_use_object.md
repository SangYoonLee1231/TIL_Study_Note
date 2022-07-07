# JavaScript - 객체 생성 및 사용법

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

  - <a href="">객체 생성 및 사용법</a>
  - <a href="">함수를 객체 내에 선언 및 사용하기</a>

<br/><br/>

## 객체 생성 및 사용법

- 객체(Object)는 속성(property)를 가진 데이터를 저장하는 역할을 한다.

    ```javascript
    const player = {
       name: tomato,
       color: red,
       food: true 
    }

    console.log(player);
    ```
    ```
    {name: "tomato", color: "blue", food: true}
    ```

- property를 불러오는 방법은 다음과 같다.

    - <code>console.log(player.name)</code>
    - <code>console.log(player["name"])</code>

<br/>

- const로 선언힌 object 객체 그 자체는 변경할 수 없다.

- 그러나, object 내부의 <strong>property</strong>는 let 변수처럼 <strong>값을 바꾸는 것이 가능</strong>하다.

    ```javascript
    const player = {
       name: tomato,
       color: red,
       food: true 
    }

    player.color = "blue";
    console.log(player.color);
    ```
    ```
    blue
    ```

- 또한 새로운 property를 추가할 수도 있다.

    ```javascript
    player.koreanName = "토마토";
    console.log(player);
    ```
    ```
    {name: "tomato", color: "blue", food: true, koreaName: "토마토"}
    ```

<br/><br/>

## 함수를 객체 내에 선언 및 사용하기

- 일반적으로 JS에서 함수를 선언하고 호출하는 방식

    ```javascript
    function sayHello(otherName) {
        console.log(`Hello ${otherName}`);
    }

    sayHello("SYL");
    ```

- 객체 내에서 함수를 선언하고 호출하는 방식

    ```javascript
    const object = {
        name: "SangYoon",
        sayHello: function(otherName) {
            console.log(`Hello ${otherName}`);
        }
    }

    object.sayHello("SYL");
    ```