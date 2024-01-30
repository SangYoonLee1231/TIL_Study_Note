# JavaScript 기본 5 - 조건문 (<code>if</code>, <code>else</code>, <code>switch</code>), 논리 연산자

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 10 ~ 11, 14장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#%EC%A1%B0%EA%B1%B4%EB%AC%B8-if-else-%EA%B0%84%EB%8B%A8-%EC%A0%95%EB%A6%AC">조건문 (<code>if</code>, <code>else</code>) (간단 정리)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#switch%EB%AC%B8"><code>switch</code>문 (간단 정리)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#%EC%A1%B0%EA%B1%B4%EB%B6%80-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%AC%BC%EC%9D%8C%ED%91%9C-%EC%97%B0%EC%82%B0%EC%9E%90-">조건부 연산자 (물음표 연산자) <code>?</code></a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#%EB%85%BC%EB%A6%AC-%EC%97%B0%EC%82%B0%EC%9E%90">논리 연산자</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#or-%EC%97%B0%EC%82%B0%EC%9E%90-">OR 연산자 <code>||</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#and-%EC%97%B0%EC%82%B0%EC%9E%90-">AND 연산자 <code>&&</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#or-%EC%97%B0%EC%82%B0%EC%9E%90--%EC%99%80-and-%EC%97%B0%EC%82%B0%EC%9E%90--%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC">OR 연산자 <code>||</code> 와 AND 연산자 <code>&&</code> 의 동작 원리</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#not-%EC%97%B0%EC%82%B0%EC%9E%90-">NOT 연산자 <code>!</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic5.md#etc">Etc.</a>

<br/><br/>

## 조건문 (<code>if</code>, <code>else</code>) (간단 정리)

- <code>if</code>문은 조건을 처리하여 분기를 할 수 있는 문법이다.

<br/>

- <code>if (...)</code>문의 괄호 안에 들어가는 조건식(표현식)은 <strong>불린형 값을 반환</strong>하고, 만일 그 값이 <code>true</code>면 코드 블록을 실행한다.

  - 불린형으로 변환 시 true가 되는 값은 '<strong>truthy(참 같은)</strong>' 값이라 한다. (예 : <code>0</code>, <code>""</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code>)

  - 반대로, 불린형으로 변환 시 false가 되는 값은 '<strong>falsy(거짓 같은)</strong>' 값이라 한다.

<br/>

- 이 때, <strong>코드 블록이 한 줄 뿐이더라도 중괄호 <code>{}</code>로 코드 블록을 항상 감싸주는 것이 좋다.</strong> 중괄호로 감싸는 것이 가독성에 좋기 때문이다.

<br/>

- <code>else</code>문은 <code>if</code>문에 붙어 조건이 거짓일 때 뒤에 이어지는 코드 블록을 실행시키는 문법이다.

  참고로 <code>else</code>문은 필수가 아닌 선택 사항이다.

<br/>

- <code>if</code>문과 <code>else</code>문 중간에 <code>else if</code>를 사용하면, 조건 여러 개를 처리할 수 있다.

  ```javascript
  let age = prompt("당신의 나이는 몇 살입니까?", "");

  if (age < 3) {
    message = "헬로 베이비?";
  } else if (age < 18) {
    message = "헬로 브로?";
  } else if (age < 100) {
    message = "헬로?";
  } else {
    message = "나이가 아주 많으시거나, 잘못된 값을 입력하셨군요?";
  }

  alert(message);
  ```

<br/><br/>

## <code>switch</code>문

- <code>switch</code>문은 특정 변수가 어떤 값인가에 따라 다른 코드를 실행시키는 문법이다.

  ```javascript
  switch (x) {
    case 1:
      ...
      break

    case 2:
      ...
      break

    default:
      ...
      break
  }
  ```

  - 변수 <code>x</code>의 값과 <code>case</code>문의 값을 순서대로 일치 비교하고, 일치하는 값을 찾으면 해당 <code>case</code>문을 <strong>시작점</strong>으로 잡는다.

  - <strong>시작점</strong>으로 잡은 <code>case</code>문 아래의 코드를 <code>break</code>문을 만날 때까지 모두 실행한다. 이 때, <strong>다른 <code>case</code>문을 만나도 일치 비교를 하지 않고 넘어간다.</strong>

  - 값과 일치하는 <code>case</code>문이 없으면, <code>default</code>문 아래의 코드를 실행한다. (<strong><code>default</code>문은 없어도 된다.</strong>)

<br/>

- <code>switch</code>문과 <code>case</code>문의 인수엔 <strong>어떤 표현식이 와도 상관없다.</strong>

- <code>switch</code>문 일치 비교 시, <strong>값과 자료형이 모두 동일</strong>해야 해당 <code>case</code>문이 실행된다.

  ```javascript
  let a = "10";
  let b = 0;

  switch (+a) {
    case b + 10:
      alert("표현식 +a는 10, 표현식 b+10는 10이므로, 이 코드는 실행된다.");
      break;

    case "10":
      alert('10과 "10"은 자료형이 다르므로, 이 코드는 실행되지 않는다.');

    ...

    default:
      alert("이 코드는 실행되지 않는다.");
  }
  ```

<br/><br/>

## 조건부 연산자 (물음표 연산자) <code>?</code>

- 자바스크립트에서 <strong>피연산자를 3개 받는</strong> 유일한 연산자로, C++의 삼항 연산자와 동일한 문법을 가졌다.

- <strong>조건</strong>에 따라 반환 값을 달리하려는 목적으로 만들어졌다.

  ```javascript
  let = result = condition ? value1 : value2;
  ```

  - 평가 대상인 <code>condition</code>이 truthy라면 <code>value1</code>이 반환되고, 그렇지 않다면 <code>value2</code>가 반환된다.

<br/>

- 예시

  ```javascript
  let age = prompt("당신의 나이는 몇 살입니까?", "");

  let accessAllowed = age > 18 ? true : false;
  ```

<br/>

- 물음표 연산자 <code>?</code>를 여러 개 연결하면, <code>else if</code>문을 사용하는 것처럼, 복수의 조건을 처리할 수 있다.

- 하지만 이보단 <code>else if</code>문을 사용하는 것이 가독성에 좋다.

<br/><br/>

## 논리 연산자

- 자바스크립트엔 OR 연산자 <code>||</code>, AND 연산자 <code>&&</code>, NOT 연산자 <code>!</code> 이렇게 3가지 논리 연산자가 존재한다.

- 논리 연산자는 피연산자로 불린형 및 모든 타입의 값을 받을 수 있다.

- 연산의 결과 역시 모든 타입이 될 수 있다.

<br/>

### OR 연산자 <code>||</code>

- 인수 중 하나라도 <code>true</code>라면 <code>true</code>를 반환하고, 그렇지 않으면 <code>false</code>를 반환한다.

  ```javascript
  alert(true || true); // true
  alert(true || false); // true
  alert(false || true); // true
  alert(false || false); // false
  ```

<br/>

- 인수가 <strong>불린형이 아닐 경우</strong>, 평가를 위해 <strong>불린형으로 형변환</strong>된다.

  - 그럼 불린형으로의 형 변환 시 적용되는 규칙을 다시 한 번 짚어보자.

    - <code>0</code>이나 비어있다고 보이는 값들은 <code>false</code>로, 나머지는 <code>true</code>로 변환된다고 우선 생각하면 좋다.

    <br/>

    - <code>0</code>, <code>""</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code> &nbsp; → &nbsp; <code>false</code>

    - 그 외의 값 &nbsp; → &nbsp; <code>true</code>

    <br/>

    - 다만, 문자열 <code>"0"</code>과, 공백 <code>" "</code>은 비어있지 않은 문자열이므로, <code>true</code>로 변환된다.

    - 또한, <code>-1</code>과 같은 음수 값도 <code>true</code>로 변환된다.

    <br/>

    - 그러나, 숫자 <code>0</code>과, 빈 문자열 <code>""</code>은 <code>false</code>로 변환된다.

<br/>

- OR 연산자 <code>||</code> 은 <code>if</code>문의 조건식에 자주 사용된다.

  ```javascript
  if (1 || 0) {
    alert("trurhy");
  }
  ```

<br/>

### AND 연산자 <code>&&</code>

- 엠퍼센트 <code>&</code>를 연달아 써서 만들 수 있다.

- 인수가 모두 참일 경우 <code>true</code>를 반환하고, 인수 중 하나라도 <code>false</code>면 <code>false</code>를 반환한다.

  ```javascript
  alert(true && true); // true
  alert(true && false); // true
  alert(false && true); // true
  alert(false && false); // false
  ```

<br/>

- 인수가 <strong>불린형이 아닐 경우</strong>, OR 연산자 <code>||</code> 와 마찬가지로, <strong>불린형으로 변환</strong>된 후 평가를 진행한다.

<br/>

### OR 연산자 <code>||</code> 와 AND 연산자 <code>&&</code> 의 동작 원리

- 자바스크립트에서만 해당되는, 두 논리 연산자 <code>&&</code> 와 <code>||</code> 의 <strong>동작 원리</strong>에 대해 알아보자.

- 결론적으로, 두 논리 연산자 <code>&&</code> 와 <code>||</code> 도 <strong>값을 반환하는 연산</strong>이다.

<br/>

- <strong>OR 연산자 <code>||</code> 의 동작 순서</strong>

  - 가장 왼쪽부터 오른쪽으로 나아가며 피연산자를 평가한다. 이 때, 각 피연산자는 <strong>불린형</strong>으로 바뀐다.

  - 평가 중 <strong>피연산자 값이 <code>true</code>로 나오면</strong>, 그 즉시 연산을 멈추고 해당 피연산자의 <strong>원래 값</strong>을 반환한다.

  - <strong>피연산자가 모두 <code>false</code>로 평가되면</strong>, 맨 마지막 피연산자의 <strong>원래 값</strong>을 반환한다.

    ```javascript
    alert(1 || 0); // 1
    alert(null || 1); // 1
    alert(null || 0 || 1); // 1
    alert(undefined || null || 0); // 0 (모두 falsy, 마자막 값 반환)
    ```

<br/>

- <strong>AND 연산자 <code>&&</code> 의 동작 순서</strong>

  - 가장 왼쪽부터 오른쪽으로 나아가며 피연산자를 평가한다. 이 때, 각 피연산자는 <strong>불린형</strong>으로 바뀐다.

  - 평가 중 피연산자 값이 <code>false</code>로 나오면</strong>, 그 즉시 연산을 멈추고 해당 피연산자의 <strong>원래 값</strong>을 반환한다.

  - <strong>피연산자가 모두 <code>true</code>로 평가되면</strong>, 맨 마지막 피연산자의 <strong>원래 값</strong>을 반환한다.

    ```javascript
    alert(1 && 0); // 0
    alert(1 && 5); // 5
    alert(1 && null && 2); // null (null은 falsy)
    alert(1 && 2 && 3); // 3 (모두 truthy, 마자막 값 반환)
    ```

<br/>

### NOT 연산자 <code>!</code>

- 느낌표 <code>!</code>를 써서 만들 수 있다.

- 인수를 불린형으로 변환하고, 그 값의 역을 반환한다.

  ```javascript
  alert(!true); // false
  alert(!0); // true
  ```

<br/>

- NOT 연산자를 두 개 연달아 사용(<code>!!</code>)하면 값을 불린형으로 변환할 수 있다.

  ```javascript
  alert(Boolean("")); // false
  alert(!!""); // false

  alert(Boolean(-1)); // true
  alert(!!-1); // true
  ```

<br/>

### Etc.

- <code>&&</code>의 우선순위가 <code>||</code> 보다 높다.

  ```javascript
  alert(null || (2 && 3) || 4); // alert(null || 3 || 4) → 3 반환
  ```

<br/>

- <strong><code>alert()</code> 메소드의 반환값은 <code>undefined</code>이다.</strong>

  ```javascript
  alert(alert(1) || 2 || alert(3)); // 1, 2 출력
  ```

  - 우선 <code>alert(1)</code>을 평가한다. → 얼릿 창에 <code>1</code> 출력

  - <code>alert(1)</code>은 <code>undefined</code>를 반환하므로, 다음으로 <code>2</code>를 평가한다. → <code>alert(undefined || 2 || alert(3));</code>

  - <code>2</code>는 truthy이므로, 실행이 멈추고 <code>2</code>가 반환된다.

  - <code>alert(3)</code>은 실행되지 않는다.
