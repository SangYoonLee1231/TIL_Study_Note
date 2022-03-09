# JavaScript 기본 4 - 비교 연산자

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 9장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic4.md#%EB%B9%84%EA%B5%90-%EC%97%B0%EC%82%B0%EC%9E%90%EC%9D%98-%EC%A2%85%EB%A5%98%EC%99%80-%EB%B0%98%ED%99%98%EA%B0%92">비교 연산자의 종류와 반환값</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic4.md#%EB%B9%84%EA%B5%90%ED%95%98%EB%A0%A4%EB%8A%94-%EB%91%90-%EC%9E%90%EB%A3%8C%EA%B0%92%EC%9D%B4-%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EA%B2%BD%EC%9A%B0">비교하려는 두 자료값이 서로 다른 경우</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic4.md#%EC%9D%BC%EC%B9%98-%EC%97%B0%EC%82%B0%EC%9E%90-strict-equality-operator-">일치 연산자 (Strict Equality Operator) <code>===</code></a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic4.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B9%84%EA%B5%90">문자열 비교</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic4.md#%EB%8F%99%EB%93%B1-%EC%97%B0%EC%82%B0%EC%9E%90%EC%9D%98-%ED%8A%B9%EB%B3%84%ED%95%9C-%EA%B7%9C%EC%B9%99-null--undefined">동등 연산자의 특별한 규칙 (<code>null</code>, <code>undefined</code>)</a>

<br/><br/>

## 비교 연산자의 종류와 반환값

- <code>a > b</code>, <code>a < b</code>, <code>a >= b</code>, <code>a <= b</code>

- <code>a == b</code> : 동등 연산자, <code>a != b</code> : 부등 연산자

- <code>a === b</code> : 일치 연산자

<br/>

- 비교 연산자는 불린(boolean)형으로 결과값을 반환한다.

  - 비교 결과가 참이면 <code>true</code>, 거짓이면 <code>false</code>

<br/>

- 반환된 결과값을 변수에 할당하는 것 또한 가능하다.

  ```javascript
  let result1 = 5 != 5;
  alert(result1); // false

  let result2 = 2 > 1;
  alert(result2); // true
  ```

<br/><br/>

## 비교하려는 두 자료값이 서로 다른 경우

- 비교하려는 두 자료값이 서로 다르다면, 모두 숫자형으로 변환된 후 비교가 이루어진다.

  ```javascript
  alert("2" > 1); // true, 문자열 '2'이 숫자 2으로 변환된 후 비교가 진행된다.
  alert("0" == 0); // true, 문자열 '0'이 숫자 0으로 변환된 후 비교가 진행된다.
  alert("01" == 1); // true, 문자열 '01'이 숫자 1로 변환된 후 비교가 진행된다.

  alert(true == 1); // true
  alert(0 == false); // true
  alert("" == false); // true
  ```

<br/>

### 일치 연산자 (Strict Equality Operator) <code>===</code>

- 동등 연산자 (Equality Operator) <code>==</code>와 달리, 일치 연산자 (Strict Equality Operator) <code>===</code>는 형 변환을 하지 않고 값을 비교한다.

- 일치 연산자 <code>===</code>는 자료형의 동등 여부까지 검사하므로, <code>a === b</code>에서 a와 b의 형이 다르면 즉시 false를 반환한다.

- 즉, 일치 연산자 <code>===</code>는 동등 연산자 <code>==</code>의 엄격한 버전으로, 비교 결과가 명확하기 때문에, 에러 확률을 줄여준다.

  ```javascript
  alert(true === 1); // false
  alert(0 === false); // false
  alert("" === false); // false
  ```

<br/>

- 마찬가지로, 불일치 연산자 <code>!==</code>는 부등 연산자 <code>!=</code> 의 엄격한 버전이다.

<br/><br/>

## 문자열 비교

- 자바스크립트는 두 문자열을 비교할 때 사전순을 기준으로 비교한다.

  - 비교는 좌측부터 우측으로 순서대로

  - 사전순으로 뒷 쪽 → 더 큰 값

  - 비교 종료 시 문자열 길이 더 긴쪽이 큰 값, 동일하면 동일하다고 결론.

    ```javascript
    alert("Z" > "A"); // true
    alert("See" > "Sea"); // true
    alert("Bee" > "Be"); // true

    alert("2" > "12"); // true
    ```

<br/>

- 비교 기준이 정확히는 사전순이 아니라 유니코드 순이다.

  - 대문자와 소문자 중 소문자가 더 큰 값을 갖는다.

    ```javascript
    alert("a" > "Z"); // true
    ```

<br/><br/>

## 동등 연산자의 특별한 규칙 (<code>null</code>, <code>undefined</code>)

- ✨ 동등 연산자 <code>==</code>는 피연산자가 <code>null</code>와 <code>undefined</code>일 때, 다른 자료형처럼 숫자형으로 변환 하지 않는다.

  - 다른 비교 연산자에선 <code>null</code>와 <code>undefined</code> 모두 숫자형으로 변환한다.

    - <code>null</code> → <code>0</code>

    - <code>undefined</code> → <code>NaN</code>  
      (<code>NaN</code>이 피연산자인 경우 비교연산자는 항상 <code>false</code>를 반환한다.)

<br/>

- 예시

  ```javascript
  alert(null > 0); // false, null은 0으로 변환
  alert(null == 0); // false, null은 undefined와 비교할 때만 같고, 나머지는 false
  alert(null >= 0); // true, null은 0으로 변환

  alert(undefined > 0); // false, undefined는 NaN으로 변환
  alert(undefined < 0); // false, undefined는 NaN으로 변환
  alert(undefined == 0); // false, undefined는 null과 비교할 때만 같고, 나머지는 false
  ```

<br/>

- 그리고 동등 비교(<code>==</code>)시 <code>null</code>와 <code>undefined</code>는, 서로 같다고 인식해 <code>true</code>를 반환하지만, 다른 값과 비교할 땐 <code>false</code>를 반환한다.

  ```javascript
  alert(null === undefined); // false
  alert(null == undefined); // true
  ```

<br/>

- 이러한 예외 상황은 되도록 피해서 코드를 작성하는 것이 좋다.

  - <code>null</code>이나 <code>undefined</code>가 될 확률이 있는 변수가 <code><</code>,<code>></code>,<code><=</code>,<code>>=</code>의 피연산자로 오지 않도록 한다.

  - 만일 그렇지 못할 경우, <code>null</code>, <code>undefined</code> 여부를 확인하는 코드를 따로 추가한다.
