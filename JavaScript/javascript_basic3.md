# JavaScript 기본 3 - 기본 연산자

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 8장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EC%97%B0%EC%82%B0%EC%9E%90-%EA%B4%80%EB%A0%A8-%EC%9A%A9%EC%96%B4">연산자 관련 용어</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EC%82%B0%EC%88%A0-%EC%97%B0%EC%82%B0%EC%9E%90">산술 연산자</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#--%EC%97%B0%EC%82%B0%EC%9E%90%EC%9D%98-%EA%B8%B0%EB%8A%A5">'+' 연산자의 기능</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EC%97%B0%EC%82%B0%EC%9E%90-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84">연산자 우선순위</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%ED%95%A0%EB%8B%B9-%EC%97%B0%EC%82%B0%EC%9E%90">할당 연산자</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EC%A6%9D%EA%B0%80%EA%B0%90%EC%86%8C-%EC%97%B0%EC%82%B0%EC%9E%90">증가/감소 연산자</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EB%B9%84%ED%8A%B8-%EC%97%B0%EC%82%B0%EC%9E%90">비트 연산자</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic3.md#%EC%89%BC%ED%91%9C-%EC%97%B0%EC%82%B0%EC%9E%90">쉼표 연산자</a>

<br/><br/>

## 연산자 관련 용어

- 피연산자

  - 연산자가 연산을 수행하는 대상

  - '인수(Agrument)'라고도 부른다.

  - 피연산자의 개수가 1개인지 2개인지에 따라 연산자의 종류가 '단항 연산자' 혹은 '이항 연산자'로 나뉜다.

<br/>

- 단항 (Unary) 연산자

  - 피연산자를 하나만 받아 계산하는 연산자

  - 대표젹인 예로 피연산자의 부호를 뒤집는 딘항 마이너스 연산자 <code>-</code>가 있다.

<br/>

- 이항 (Binary) 연산자

  - 피연산자가 두 개 필요한 연산자

  - <code>5 - 3</code>처럼 뺄셈 연산을 하는 이항 마이너스 연산자 <code>-</code>가 그 예다.

<br/>

- 같은 모양의 연산자라 하더라도 단항 연산자인가 이항 연산자인가에 따라 수행하는 연산 및 연산자 우선순위가 달라진다.

<br/>

## 산술 연산자

- 덧셈 연산자 <code>+</code>

- 뻴셈 연산자 <code>-</code>

- 곱셈 연산자 <code>\*</code>

- 나눗셈 연산자 <code>/</code>

  - 표현식 <code>a % b</code>는 a를 b로 나눈 몫을 반환합니다. 몫이 정수면 정수로, 실수면 실수로 반환합니다.

- 나머지 연산자 <code>%</code>

  - 표현식 <code>a % b</code>는 a를 b로 나눈 후 그 나머지를 정수로 반환합니다.

- 거듭제곱 연산자 <code>a \*\* b</code>

  - 표현식 <code>a \*\* b</code>는 a를 b번 곱한, 즉 a의 b제곱 값을 반환합니다.

  - 이 때 b의 값은 정수가 아닌 숫자에 대해서도 동작한다. b에 <code>1/2</code>을 넣으면 제곱근을 구할 수 있다.

    ```javascript
    alert(4 ** (1 / 2)); // 2
    ```

<br/><br/>

## '+' 연산자의 기능

### 단항 연산자 '+'

- 숫자에 단항 연산자 '+'을 붙이면 아무런 일이 일어나지 않는다.

- 그러나 숫자가 아닌 값이 '+'을 붙이면, 그 피연산자는 <strong>숫자형으로 형변환</strong>이 일어난다.

- 즉, 단항 연산자 '+'은 <code>Number(...)</code>와 동일한 일을 수행하는 것이다.

  ```javascript
  let num1 = -2;
  let num2 = "10";

  alert(+num1); // -2
  alert(+num2); // 10

  alert(+""); // 0
  alert(+undefined); // NaN
  ```

- HTML 폼(form) 필드에서 숫자로 된 문자열 값(예: <code>"2"</code>)을 가져올 때, 단항 연산자를 사용해 숫자로 형변환을 해줄 수 있다.

<br/>

### 이항 연산자 '+'

- 이항 연산자 '+'은 피연산자 2개를 더한 값을 반환한다.

  ```javascript
  alert(3 + 4); // 7
  ```

<br/>

- 그런데 만약 피연산자 2개에 문자열이 전달되면, 덧셈 연산자는 덧셈을 하지 않고 두 문자열을 병합힌다.

  ```javascript
  alert("3" + "4"); // "34"
  ```

<br/>

- 만일 피연산자 2개 중 하나만 문자열이라면, 덧셈 연산자는 <strong>나머지 하나를 문자열로 형변환하고 서로 병합</strong>한다.

  ```javascript
  alert("3" + 4); // "34"

  alert(2 + 3 + "4"); // "54"
  ```

  - 연산은 왼쪽에서 오른쪽으로 진행되므로, <code>2 + 3 + "4"</code>에서 숫자 2와 3이 먼저 더해지고, 그 값 5가 문자열 4와 병합되어 "54"가 되는 것이다.

<br/>

- 반대로 <strong>덧셈 이외의 산술 연산자</strong>는 피연산자가 숫자가 아닌 경우, <strong>그 형을 숫자형으로 변환</strong>한다. (오직 숫자형만 다루는 연산자들이다)

  ```javascript
  alert("-9" - 5); // -14
  alert(2 * "3"); // 6
  alert("6" / "2"); // 3
  ```

<br/><br/>

## 연산자 우선순위

- 하나의 표현식에 둘 이상의 연산자가 있는 경우, 실행 순서는 연산자 우선순위에 의해 결정된다.

- 우선순위가 클수록 먼저 실행된다. 우선순위가 동일하면 왼쪽에서 오른쪽 순으로 실행된다.

- 연산자 우선순위는 기억할 필요 없다. 먼저 계산하고 싶은 연산을 <strong>괄호</strong>로 묶으면 된다.

- 단항 연산자는 이항 연산자보다 높은 우선순위를 갖는다.

  - 단항 덧셈 연산자가 이항 덧셈 연산자보다 먼저 실행되므로, 표현식 <code>" +'1' + +'2' "</code>에선 형변환이 먼저 일어나 <code>3</code>의 값이 된다.

<br/><br/>

## 할당 연산자

- 어떤 값을 변수에 할당하는 연산자 <code>=</code>은 우선순위가 <code>3</code>으로 매우 낮다.

<br/>

### 할당 연산자의 값 반환

- 할당 연산자 <code>=</code> 역시 산술 연산자처럼 값을 반환한다.

  - 예시 1

    ```javascript
    let num = 1000;
    ```

    - 다음 표현식을 호출하면, num에 1000이 할당되고, 이에 더하여 1000이 반환된다.

  <br/>

  - 예시 2

    ```javascript
    let a = 1;
    let b = 2;

    let c = (a = b + 1);

    alert(a); // 3
    alert(c); // 3
    ```

    - 표현식 <code>(a = b + 1)</code>에서 a에 3이 할당되고, 그 값 3이 반환된다.

<br/>

- 여러 자바스크립트 라이브러리에서 이런 식으로 할당 연산자를 사용하고 있으므로 원리를 알고 있어야 하나, 실제로 코드를 이렇게 작성하는 것은 가독성을 떨어뜨리기에 지양해야 한다.

<br/>

### 할당 연산자 체이닝

- 할당 연산자 <code>=</code>을 여러 개 연결하여, 여러 변수에 하나의 값을 할당할 수 있다.

  - <code>x = y = z = 3 \* 5</code>처럼 할당 연산자가 여러 개 연결된 경우, 오른쪽 부터 순서대로 평가가 진행된다.

  - 우선 3 \* 5가 평가되고, 그 값 15가 z, y, x에 순서대로 할당된다.

<br/>

- 그러나 이런 식으로 코드를 작성하는 것은 가독성에 좋지 않다.

- 따라서 아래처럼 한 줄에 하나씩 변수를 할당하자.

  ```javascript
  z = 3 * 5;
  y = z;
  x = z;
  ```

<br/><br/>

## 증가/감소 연산자

- 증가/감소 연산자는 하나의 변수에 붙어 그 값을 1만큼 증가하거나 감소시키는 연산을 수행하는 연산자다.

  - 증가 연산자 <code>++</code>, 감소 연산자 <code>--</code>

<br/>

- 숫자에 증가/감소 연산자를 사용하면 에러가 발생한다. 오직 변수에만 증가/감소 연산자를 쓸 수 있다.

<br/>

### 전위형/후위형

- 증가/감소 연산자는 변수의 앞이나 뒤에 모두 올 수 있다.

  - <strong>후위형</strong> : <code>num++</code> 처럼 피연산자 뒤에 오는 경우

  - <strong>전위형</strong> : <code>++num</code> 처럼 피연산자 앞에 오는 경우

<br/>

- 두 형 모두 변수의 값을 1씩 증가시키나, 어떤 값을 반환하느냐에 따라 다르게 동작한다.

  - <strong>후위형</strong> (<code>num++</code>) : <strong>기존 값을 반환</strong>한 후, 변수 값을 1 증가시킨다.

    ```javascript
    let num = 1;

    alert(2 * num++); // 2
    alert(num); // 2
    ```

  <br/>

  - <strong>전위형</strong> (<code>++num</code>) : 변수 값을 먼저 1 증가시킨 후, <strong>바뀐 새 값을 반환</strong>한다.

    ```javascript
    let num = 1;

    alert(2 * ++num); // 4
    alert(num); // 2
    ```

<br/>

- 위의 예시처럼 코드를 작성하는 것은 가독성에 좋지 않다. 코드 한 줄엔 특정 동작 하나에 관련된 내용만 작성하자.

  ```javascript
  let num = "1";

  alert(num);
  num++;
  ```

<br/><br/>

## 비트 연산자

- 비트 연산자는 인수를 32비트로 전환하여 이진 연산을 수행하는 연산자다.

  - AND <code>&</code>,&nbsp; OR <code>|</code>,&nbsp; XOR <code>^</code>,&nbsp; NOT <code>~</code>

  - 왼쪽 시프트 <code><<</code>,&nbsp; 오른쪽 시프트 <code>>></code>

  - 부호 없는 오른쪽 시프트 <code>>>></code>

<br/>

- 웹 개발에선 비트 연산자가 잘 안쓰이지만, 암호를 다룰 땐 유용하다고 한다.

<br/><br/>

## 쉼표 연산자

- 쉼표 연산자 <code>,</code>는 여러 표현식을 한 줄로 표현하게 헤주되, 마지막 표현식의 평가 결과만을 반환해주는 연산자이다.

  - 예시 1

    ```javascript
    let a = (1 + 2, 3 + 4); // 7
    ```

  - 예시 2

    ```javascript
    for (a = 1, b = 3, c = a + b; a < 10; a++) {
      ...
    }
    ```

<br/>

- 여러 자바스크립트 프레임워크에서 쉼표 연산자를 가끔식 사용하고 있으므로 동작 방식을 알고 있는 것이 좋지만, 가독성은 별로 좋지 않으므로 정말 필요한 경우가 아니라면 사용을 지양하자.
