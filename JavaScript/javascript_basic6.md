# JavaScript 기본 6 - nullish 병합 연산자 <code>??</code>, 반복문 (<code>for</code>, <code>while</code>)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 12장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#nullish-%EB%B3%91%ED%95%A9-%EC%97%B0%EC%82%B0%EC%9E%90-">nullish 병합 연산자 <code>??</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#-%EC%99%80--%EC%9D%98-%EC%B0%A8%EC%9D%B4"><code>??</code> 와 <code>||</code> 의 차이</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#while%EA%B3%BC-for-%EB%B0%98%EB%B3%B5%EB%AC%B8">while과 for 반복문</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## nullish 병합 연산자 <code>??</code>

- <code>??</code> 연산자는 왼쪽부터 탐색 중, <strong>첫 번째로 정의된(defined)</strong> 값을 그대로 반환한다.

<br/>

- <code>a ?? b</code> 평가 결과

  - a가 <code>null</code>도, <code>undefined</code>도 아니라면, 그대로 a로 평가한다.

  - a가 <code>null</code>이나 <code>undefined</code>면, a 대신 b로 평가한다.

    ```javascript
    x = a != null && a != undefined ? a : b;
    ```

<br/>

- <code>??</code> 연산자를 연달아 사용한 경우

  ```javascript
  alert(null || "마이클" || "익명"); // "마이클"

  alert(null || null || "익명"); // "익명"
  ```

<br/>

- <code>??</code> 연산자는 우선순위는 5로 애매하므로, 복잡한 표현식 안에선 괄호<code>()</code>로 묶어서 사용하는 것이 좋다.

  ```javascript
  let height = null;
  let width = null;

  let area = (height ?? 100) * (width ?? 50);

  alert(area);
  ```

<br/>

- <code>??</code> 연산자는 안정성 관련 이슈로 인해 <code>||</code>나 <code>&&</code>와 함께 쓰이지 못하므로, 이때도 괄호<code>()</code>를 사용하여 제약을 피해야 한다.

  ```javascript
  alert(1 ?? 2 && 3); // SyntaxError: Unexpected token '??'

  alert(1 ?? (2 && 3));
  ```

<br/>

### <code>??</code> 와 <code>||</code> 의 차이

- <code>a || b</code> 평가 결과

  - a가 불린형으로 변환시 <code>true</code>면, 그대로 a로 평가한다.

  - a가 불린형으로 변환시 <code>false</code>면, b로 평가한다.

<br/>

- <code>??</code> 연산자와 <code>||</code> 연산자의 평가 결과는 유사해보이나, 0이 할당될 땐
  다른 결과가 나타난다.

  ```javascript
  alert(0 || 10); // 10
  alert(0 ?? 10); // 0
  ```

<br/><br/>

## while과 for 반복문
