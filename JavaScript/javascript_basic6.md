# JavaScript 기본 6 - nullish 병합 연산자 <code>??</code>, 반복문 (<code>for</code>, <code>while</code>)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 12 ~ 13장 내용

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

## <code>while</code>과 <code>for</code> 반복문

- 개발을 하면서 어떤 동작을 반복하는 코드를 작성하는 것은 필수 불가결이다.

- 따라서 반복문은 (조건문과 함께) 매우 중요하고 기초적인 문법으로 꼽힌다.

<br/>

- 자바스크립트에서의 반복문은 C언어의 문법과 크게 다르지 않다.

<br/>

### <code>while</code> 반복문

- <code>while</code>문 예시

  ```javascript
  let i = 0;
  while (i < 10) {
    alert(i);
    i++;
  }
  ```

<br/>

- <code>while</code>문의 조건식 평가 값이 <code>true</code>면, 대괄호로 묶인 반복문 본문의 코드가 실행된다.

- 본문의 코드가 모두 실행된 후 조건식을 다시 평가한다.

<br/>

- 반복문의 조건식엔 모든 종류의 표현식, 변수가 올 수 있다.

- 만일 반복문의 본문이 한 줄이라면, 대괄호를 쓰지 않아도 된다.

  ```javascript
  let i = 0;
  while (i < 10) i++;
  ```

<br/>

- 반복문 본문이 한 번 실행되는 것을 <strong>이터레이션</strong>(iteration, 반복)이라 부른다.

  - 위의 예시 코드에선 반복문이 10번의 이터레이션을 만든다.

<br/>

### <code>do while</code> 반복문

- <code>do..while</code>문 예시

  ```javascript
  let i = 0;
  do {
    alert(i);
    i++;
  } while (i < 10);
  ```

<br/>

- 반복문 본문을 우선 실행한 후 조건식을 평가한다. 그 값이 <code>true</code>면 본문을 처음부터 다시 실행한다.

- 본문을 <strong>최소한 한 번</strong>이라도 실행해야 할 때만 사용해야 한다.

### <code>for</code> 반복문

- <code>for</code>문 예시

  ```javascript
  let i = 0;
  for (i = 0; i < 10; i++) {
    alert(i);
  }
  ```

- 인라인 변수 선언 방식

  ```javascript
  for (let i = 0; i < 10; i++) {
    alert(i);
  }
  ```

<br/>

- <code>for</code>문의 구성 요소를 생략할 수도 있다.

  ```javascript
  let i = 0;

  for (; i < 3; ) {
    alert(i++);
  }
  ```

  ```javascript
  for (let i = 0; ; i++) {
    alert(i);
  }
  // 이 반복문은 무한 루프(Infinity Loop)를 돈다.
  ```

  - 각 구성요소를 <strong>2개 이상</strong> 생략하는 것도 가능하다. 다만 세미콜론은 확실히 넣어주어야 에러가 나지 않는다.

<br/>

### <code>break</code> 문, <code>continue</code> 문

<br/>

### 레이블
