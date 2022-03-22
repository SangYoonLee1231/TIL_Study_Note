# JavaScript 기본 6 - nullish 병합 연산자 <code>??</code>, 반복문 (<code>for</code>, <code>while</code>)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 12 ~ 13장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#nullish-%EB%B3%91%ED%95%A9-%EC%97%B0%EC%82%B0%EC%9E%90-">nullish 병합 연산자 <code>??</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#-%EC%99%80--%EC%9D%98-%EC%B0%A8%EC%9D%B4"><code>??</code> 와 <code>||</code> 의 차이</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic6.md#while%EA%B3%BC-for-%EB%B0%98%EB%B3%B5%EB%AC%B8"><code>while</code>과 <code>for</code> 반복문</a>
  - <a href=""><code>while</code> 반복문</a>
  - <a href=""><code>do while</code> 반복문</a>
  - <a href=""><code>for</code> 반복문</a>
- <a href=""><code>break</code> 문과 <code>continue</code> 문</a>
- <a href="">레이블</a>

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

<br/><br/>

## <code>break</code> 문과 <code>continue</code> 문

- 반복문 실행 중 <code>break</code>를 만나면 해당 반복문을 빠져나온다.

  ```javascript
  let sum = 0;

  while (true) {
    let value = +prompt("숫자를 입력하세요.", "");

    if (!value) break; // (*)

    sum += value;
  }
  alert("합계: " + sum);
  ```

<br/>

- 반복문 실행 중 <code>continue</code>를 만나면 현재 실행 중인 이터레이션(iteration)을 멈추고 다음 이터레이션을 강제로 실행시킨다.

  ```javascript
  for (let i = 0; i < 10; i++) {
    // 조건이 참이라면 남아있는 본문은 실행되지 않습니다.
    if (i % 2 == 0) continue;

    alert(i); // 1, 3, 5, 7, 9가 차례대로 출력됨
  }
  ```

<br/>

- <code>break</code>나 <code>continue</code>는 <strong>반복문 내부</strong>에서만 사용할 수 있다.

- <code>?</code> 오른쪽엔 <code>break</code>나 <code>continue</code>가 <strong>올 수 없다</strong>.

<br/><br/>

## 레이블

- <strong>여러 개의 중첩 반복문을 한 번에 빠져나와야 할 때 레이블(<code>label</code>)을 사용할 수 있다.</strong>

- 레이블은 <strong>반복문 앞에 붙여</strong> 사용한다.

<br/>

- 반복문 앞에 콜론(<code>:</code>)과 함께 레이블을 쓴다.

- 반복문 안에 쓰이는 <code>break 레이블이름</code>은 <strong>해당 레이블이름이 붙은 반복문을 찾아</strong> 그 반복문을 빠져나가게 해준다.

  ```javascript
  outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      let input = prompt(`(${i},${j})의 값`, "");

      // 사용자가 아무것도 입력하지 않거나 Cancel 버튼을 누르면 두 반복문 모두를 빠져나옵니다.
      if (!input) break outer; // (*)

      // 입력받은 값을 가지고 무언가를 함
    }
  }
  alert("완료!");
  ```

<br/>

- 레이블은 반드시 <strong><code>break</code> 이나 <code>continue</code> 지시자 위</strong>에 있어야 한다.

  ```javascript
  break label; // 아래 for 문으로 점프할 수 없습니다.

  label: for (...)
  ```
