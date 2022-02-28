# JavaScript 기본 1 - 사전 지식 약점 포인트

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 1 ~ 3장 내용

- 모든 내용을 하나부터 열까지 다 기록한 것이 아니라, 잘 몰랐거나 헷갈릴만한 내용들만을 따로 모아 항목 단위로 기록하였다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#%EC%99%B8%EB%B6%80-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%82%BD%EC%9E%85%ED%95%98%EA%B8%B0">외부 스크립트 삽입하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#javascript-%EA%B8%B0%EB%B3%B8-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC">JavaScript 기본 동작 원리</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#javascript%EC%9D%98-%EC%A0%9C%EC%95%BD-%EC%82%AC%ED%95%AD">JavaScript의 제약 사항</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#%EC%84%B8%EB%AF%B8%EC%BD%9C%EB%A1%A0-%EC%9E%90%EB%8F%99-%EC%82%BD%EC%9E%85">세미콜론 자동 삽입</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#%EC%A3%BC%EC%84%9D">주석</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic.md#%EC%97%84%EA%B2%A9-%EB%AA%A8%EB%93%9C-use-strict">엄격 모드 (<code>use strict</code>)</a>

<br/><br/>

## 외부 스크립트 삽입하기

- JavaScript로 작성한 프로그램을 스크립트(script)라 부른다.

<br/>

- <code>\<script></code> 태그를 통해 HTML 문서에 자바스크립트 프로그램을 삽입할 수 있다.

- 삽입 방식은 크게 2가지다.

  - HTML 문서 내에 스크립트를 직접 작성하는 방식

  - 외부 스크립트 파일을 주소를 통해 삽입하는 방식

<br/>

- 외부 스크립트를 삽입할 때는 <code>src</code> 속성을 사용하면 된다.

  ```html
  <body>
    ...
    <script src="/js/script_example.js"></script>
  </body>
  ```

  - 보통 <code>\<body></code> 내부의 가장 밑에 <code>\<script></code>태그를 삽입한다.

<br/>

- 스크립트가 길어지면 별도의 파일로 분리해 저장하는 것이 좋다.

- <code>\<script></code> 태그에 <code>src</code> 속성이 있을 경우, 태그 내부의 코드는 무시된다.

<br/><br/>

## JavaScript 기본 동작 원리

1. 파싱 : 앤진이 스크립트를 읽는다.

2. 컴파일 : 읽어들인 스크립트를 기계어로 번역한다.

3. 변역된 기계어 코드를 실행한다. (기계어로 전환되었으므로 실행 속도가 빠르다.)

<br/>

- JavaScript 엔진은 매 과정에서 최적화를 진행하여 스크립트 실행 속도를 더욱 높인다.

<br/><br/>

## JavaScript의 제약 사항

- JavaScript는 메모리나 CPU 같은 저수준 영역을 함부로 조작할 수 없다. ('안전한' 프로그래밍 언어)

- JavaScript는 보안을 위해, 디스크에 저장된 파일로의 접근을 막거나, 브라우저 내 탭이나 창에서 동의 없이 서로의 정보를 교환할 수 없다는 등의 제약이 걸려있다.

<br/><br/>

## 세미콜론 자동 삽입

- JavaScript에선 줄바꿈이 있을 시, 이를 '암시적' 세미콜론(';')으로 해석한다.

- 즉, 줄바꿈이 세미콜론을 대신할 수 있다는 것이다.

  ```javascript
  alert("Hello");
  alert("Bro");
  ```

<br/>

- 그러나, 자바스크립트가 세미콜론을 자동으로 삽입하지 않는 경우 또한 존재한다.

  ```javascript
  alert(1 + 2 + 3);
  ```

  ```javascript
  alert("Hello World")[(1, 2)].forEach(alert);
  ```

<br/>

- ✨ 따라서, 스크립트를 작성할 때도 문(statement)이 끝날 때마다 C언어처럼 항상 세미콜론을 붙이는 것이 좋다.

  ```javascript
  alert("Hello World");

  [1, 2].forEach(alert);
  ```

<br/><br/>

## 주석

- JavaScript 주석 문법은 C언어와 동일하게 <code>//</code> 또는 <code>/\*</code> <code>\*/</code>을 사용한다.

  - <code>//</code> : 한 줄 주석

    ```javascript
    // 한 줄 주석
    ```

  - <code>/\*</code> <code>\*/</code> : 여러 줄 주석

    ```javascript
    /*
        여러 줄 주석
    */
    ```

<br/>

- <code>/\*</code> <code>\*/</code> 안에 또 다른 <code>/\*</code> <code>\*/</code>이 들어간 중첩 주석은 지원하지 않는다.

<br/><br/>

## 엄격 모드 (<code>use strict</code>)

- JavaScript는 기존의 기능을 유지하면서 발전했다.

- 따라서 JS 창시자들이 했던 실수나 불완전한 경험이 언어 안에 고스란히 남아있었다.

- 2009년, ECMAScript5(EC5)이 새롭게 제정됨으로 인해 기존의 기능 일부가 변경되고 새로운 기능이 추가되었다.

- 이로 인해 생길 호환성 문제를 대비하여, 변경사항 대부분은 엄격 모드을 활성했을 때만 적용된다.

<br/>

- <code>use strict</code>를 코드 상단에 작성하면 엄격 모드가 적용되고, 코드 전체가 "모던한" 방식으로 동작한다.

- 특정 함수에만 엄격 모드를 적용하려면, 함수 본문 맨 앞에 <code>use strict</code>를 작성하면 된다.

<br/>

- <code>use strict</code>는 반드시 최상단에 위치해야 하며, 일단 염격 모드가 적용되면 되돌릴 방법은 없다.

- 클래스(<code>class</code>)나 모듈(<code>import</code>)을 사용하면 <code>use strict</code>가 자동으로 적용된다.
