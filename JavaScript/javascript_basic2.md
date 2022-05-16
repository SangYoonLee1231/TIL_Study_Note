# JavaScript 기본 2 - 변수와 자료형, 상호작용, 형 변환

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 4 ~ 7장 내용

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic2.md#%EB%B3%80%EC%88%98-%EC%95%BD%EC%A0%90-point-%EC%9C%84%EC%A3%BC">변수 (약점 Point 위주)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic2.md#%EC%9E%90%EB%A3%8C%ED%98%95">자료형</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic2.md#%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%99%80%EC%9D%98-%EC%83%81%ED%98%B8%EC%9E%91%EC%9A%A9-alert-prompt-confirm">브라우저와의 상호작용 (<code>alert</code>, <code>prompt</code>, <code>confirm</code>)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_basic2.md#%ED%98%95-%EB%B3%80%ED%99%98">형 변환</a>

<br/><br/>

## 변수 (약점 Point 위주)

- 변수 명명 시,

  - 오직 문자와 숫자, 기호 <code>$</code>와 <code>\_</code>만 사용할 수 있다.

  - 첫 글자는 숫자가 될 수 없다.

  - 예약어 목록에 있는 단어로 작성할 수 없다.

    <br/>

  - <strong>카맬 표기법(camelCase)</strong>로 작성하는 것이 좋다.

  - <strong>간결하고 명확하되, 서술적으로 명명</strong>하여 변수가 담고 있는 것이 무엇인지 잘 설명할 수 있도록 하는 것이 중요하다.

    ```javascript
    let ourPlanetName = "Earth";
    let currentUserName = "John";
    ```

    - (data나 value는 나쁜 이름의 예시)

<br/>

- 변수 선언 시, <code>let</code>을 반드시 앞에 붙여서 선언하는 것이 중요하다.

  ```javascript
  let num = 5;

  // num = 5
  /* 이런 식으로 작성 X
  엄격 모드에선 오류 발생 */
  ```

<br/>

- 상수 중 코드가 실행되기 전에 이미 값을 알고 있는 경우, 상수명을 대문자로 작성하는 것이 좋다.

  ```javascript
  const COLOR_RED = "#F00";
  const PI = "3.14";
  ```

<br/>

- 개발 시, 새로운 변수를 추가하는 것은 좋은 습관이다.

  (변수를 재사용하면 디버깅에 10배 많은 시간을 쏟아야 한다.)

<br/><br/>

## 자료형

- JavaScript엔 8가지 기본 자료형이 있다.

- JavaScript는 하나의 변수에 저장되는 값의 종류가 자유롭게 바뀔 수 있는 '동적 타입(Dynamically Typed)' 언어이다.

<br/>

- <code>숫자형</code>

  - 정수, 부동 소숫점 숫자 등을 나타내는 자료형이다.

  - 그 외애도 <code>Infinity</code>, <code>-Infinity</code>, <code>NaN</code> 같은 특수 숫자 값이 있다.

  - 이러한 특수 숫자 값 덕분에 스크립트는 말도 안되는 수학 연산을 하더라도 치명적인 에러를 내뿜으며 죽지 않는다.  
    (수학 연산은 안전하다)

    ```javascript
    alert(1 / 0); // Infinity
    alert(Infinity); // Infinity

    alert("나는 빡빡이다" / 3 + 7); // NaN
    ```

  - 정수의 한계는 ±2^53이다.

<br/>

- <code>bigint</code>

  - 길이 제약 없이 정수형을 나타낼 수 있다.

  - 정수 리터럴 끝에 n을 붙이면 만들 수 있다.

    ```javascript
    const bigInt = 1234567890123456789012345678901234567890n;
    ```

<br/>

- <code>문자형</code>

  - 글자들로 이루어진 문자열을 나타낸다.

  - 비어있거나 한 글자여도 문자형으로 취급한다.

  - 역 따옴표(백틱)을 사용하면 문자열 중간에 변수나 표현식을 쉽게 삽입할 수 있다. (문자열의 일부로 출력된다.)

    ```javascript
    score = 100;
    alert(`I got ${score} in test!`);
    alert(`I got ${50 + 50} in test!`);
    ```

<br/>

- <code>boolean형</code>

  - <code>true</code>, <code>false</code>값을 나타내는 자료형이다.

<br/>

- <code>null</code>

  - <code>null</code> 값만을 위한 독립 자료형이다.

  - 존재하지 않는 값, 비어 있는 값, 알 수 없는 값임을 <strong>확실히 나타내고자 할 때</strong> 사용한다.

<br/>

- <code>undefined</code>

  - <code>undefined</code> 값만을 위한 독립 자료형이다.

  - <strong>값이 할당되지 않은 상태</strong>를 나타낸다.

  - 변수를 선언했지만, 값을 할당하지 않은 경우, 해당 변수에 <code>undefined</code>가 자동으로 할당된다.

  - 변수에 <code>undefined</code>를 직접 할당하는 것이 가능하나, 권장하지 않는다.

<br/>

- <code>객체형</code>

  - 데이터 컬렉션이나 복잡한 객체를 표현할 때 사용한다.

<br/>

- <code>심볼형</code>

  - 객체의 고유한 식별자를 만들 때 사용한다.

<br/>

- <code>typeof</code> 연산자는 피연산자의 자료형을 문자열 형태로 반환한다.

- 연산자 형태 <code>typeof x</code> 또는 함수 형태 <code>typeof(x)</code>로 사용할 수 있다.

<br/>

- <code>null</code>의 typeof 연산은 <code>"object"</code>인데, 이는 언어상의 오류다. null은 객체가 아니다.

- 함수(예:<code>alert</code>)의 typeof 연산은 <code>"function"</code>인데, '함수'형은 따로 존재하지 않는다. 함수는 객체형에 속한다.  
  이 또한 오류이나, 하위 호환성 문제로 인해 언어에 남겨져 있다.

<br/><br/>

## 브라우저와의 상호작용 (<code>alert</code>, <code>prompt</code>, <code>confirm</code>)

- 브라우저는 사용자가 브라우저와 상호작용을 할 수 있도록 스크립트의 3가지 함수를 제공한다.

<br/>

- <code>alert</code>

  - 사용자에게 메세지를 보여주는 모달 창(Modal Window)을 띄운다.

    ```javascript
    alert("Hello User");
    ```

<br/>

- <code>prompt</code>

  - 사용자에게 메세지와 입력 필드를 함께 보여주는 모달 창(Modal Window)을 띄운다.

  - [확인]을 누르면 사용자가 입력 필드에 입력한 문자열이 반환되고,  
    [취소] 또는 Esc를 누르면 <code>null</code>이 반환된다.

  - 반환된 값은 변수에 할당하여 다른 곳에 활용할 수 있다.

    ```javascript
    result = prompt(title, [default]);
    ```

    - title : 사용자에게 보여줄 문자열

    - default : 입력 필드의 초기값  
       (인수를 감싸는 대괄호 <code>[]</code>는 필수가 아닌 선택값이란 의미)

<br/>

- <code>confirm</code>

  - 사용자에게 메세지, [확인]과 [취소] 버튼을 모달 창(Modal Window)을 통해 보여준다.

  - 사용자가 [확인] 버튼을 누르면 <code>True</code>, [취소] 버튼을 누르면 <code>False</code>가 반환된다.

  - <code>prompt</code> 함수와 마찬가지로, 반환된 값은 변수에 할당하여 다른 곳에 활용할 수 있다.

    ```javascript
    let isContinue = confirm("계속 진행하시겠습니까?");

    if (isContinue) {
      alert("다음으로 넘아갑니다");
    } else {
      alert("여기서 중단합니다");
    }
    ```

    <br/>

  - 위 3개의 함수를 통해 모달 창(Modal Window)이 사용자에게 띄워지면, 스크립트의 실행이 일시 중단되고, 사용자는 창을 닫기 전까진 나머지 페이지와 상호작용 할 수 없다.

    - '모달’이란 단어엔 페이지의 나머지 부분과 상호 작용할 수 없다는 의미가 내포되어 있다.

  <br/>

  - 모딜 창의 위치와 모양은 수정할 수 없다. 이러한 제약사항은 간결성을 위해 치러야 할 대가이다.

<br/><br/>

## 형 변환

- 어떤 값의 자료형이 다른 자료형으로 변환되는 과정을 <strong>형 변환(Type Conversion)</strong>이라 한다.

* 형 변환엔 크게 2가지 종류가 있다.

  - <strong>자동 형 변환</strong> : 상황에 따라 값의 자료형이 자동으로 바뀌는 과정

  - <strong>명시적 형 변환</strong> : 전달받은 값을 의도를 갖고 원하는 자료형으로 직접 변환해주는 과정

<br/>

### 문자형으로 변환

- 문자형 자동 형 변환

  - <code>alert</code> 메서드는 매개변수로 문자형을 받기 때문에, <code>alert(value)</code>에서 value가 문자형이 아니라면, value 값을 문자형으로 자동 형변환한다.

    ```javascript
    alert(123456); // 123456이 문자열로 자동 변환되어 출력된다.
    ```

<br/>

- 문자형 명시적 형 변환

  - <code>String(value)</code> 함수를 호출하여 문자열이 아닌 값을 문자열로 직접 명시해서 변환해줄 수 있다.

    ```javascript
    let val = true;
    alert(typeof val); // boolean

    val = String(val);
    alert(typeof val); // string
    ```

<br/>

- 문자형으로의 형변환은 그 결과가 대부분 예측 가능한 방식으로 일어난다.

  - <code>"true"</code> → <code>true</code>, &nbsp; <code>"null"</code> → <code>null</code>

<br/>

### 숫자형으로 변환

- 숫자형 자동 형 변환

  - 주로 수학과 관련된 함수에서 자동으로 형 변환이 일어난다.

    ```javascript
    alert("6" / "2"); // 3
    ```

<br/>

- 숫자형 명시적 형 변환

  - <code>Number(value)</code> 함수를 호출하여 주어진 value값을 숫자형으로 직접 변환할 수 있다.

    ```javascript
    let val = "1234";
    alert(typeof val); // string

    val = Number(val);
    alert(typeof val); // number
    ```

- 어떤 값을 문자 기반 폼으로 입력받아 숫자형으로 사용하고자 할 때, 명시적 형 변환을 꼭 해주어야 한다.

<br/>

- 숫자형으로의 변환은 그 결과가 일부 예측하기 어렵다. 따라서 변환 시 적용되는 규칙을 잘 숙지하고 있는 것이 중요하다.

  - ✨ <code>Number(undefined)</code> &nbsp; → &nbsp; <code>NaN</code> &nbsp; (<code>0</code>이 아님에 유의)

  - <code>Number(null)</code> &nbsp; → &nbsp; <code>0</code>

  - <code>Number(true)</code> / <code>Number(false)</code> &nbsp; → &nbsp; <code>1</code> / <code>0</code>

  - <code>string</code> &nbsp; → &nbsp; 전달받은 문자열을, 앞 뒤 공백 무시하고, <strong>그대로</strong> 읽는다. 단, 문자열이 비어있으면 <code>0</code>, 변환에 실패하면 <code>NaN</code>이 된다.

<br/>

### 불린형으로 변환

- 불린형 자동 형 변환

  - 논리 연산을 수행할 때 발생한다.

<br/>

- 불린형 명시적 형 변환

  - <code>Boolean(value)</code> 함수를 호출하면 명시적으로 불린형으로의 형 변환을 수행할 수 있다.

<br/>

- 불린형으로의 형 변환 시 적용되는 규칙은,

  숫자 <code>0</code> 혹은 비어있다고 보이는 값들은 <code>false</code>로, 나머지는 <code>true</code>로 바뀐다는 것이다.

  - <code>0</code>, <code>""</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code> &nbsp; → &nbsp; <code>false</code>

  - 그 외의 값 &nbsp; → &nbsp; <code>true</code>

    <br/>

  - ✨ 문자열 <code>"0"</code>과, 공백 <code>" "</code>은 비어있지 않은 문자열이므로, 불린형으로 변환 시 <code>true</code>가 됨에 유의한다.

    (반면, 숫자 <code>0</code>과, 빈 문자열 <code>""</code>은 불린형으로 변환 시 <code>false</code>가 된다.)

    <br/>

  - ✨ 또한, <code>-1</code>과 같은 음수 값 또한 불린형으로 변환 시 <code>true</code>가 됨에 유의한다.
