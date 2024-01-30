# JavaScript - 객체 생성 및 사용법

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_how_to_create_and_use_object.md#%EA%B0%9D%EC%B2%B4-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95">객체 생성 및 사용법</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_how_to_create_and_use_object.md#%ED%95%A8%EC%88%98%EB%A5%BC-%EA%B0%9D%EC%B2%B4-%EB%82%B4%EC%97%90-%EC%84%A0%EC%96%B8-%EB%B0%8F-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0">함수를 객체 내에 선언 및 사용하기</a>

<br/><br/>

## 객체 생성 및 사용법

- 객체(Object)는 속성(property)를 가진 데이터를 저장하는 역할을 한다.

- 객체를 생성할 땐 <strong>중괄호<code>{}</code></strong>를 사용한다.

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

<br/>

- 이렇게 객체 내부에 선언한 함수를 <strong>메서드</strong>라 한다.