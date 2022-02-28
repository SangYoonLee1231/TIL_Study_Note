# JavaScript 기초 문법 - 약점 포인트 1

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

* 자바스크립트의 문법을 하나부터 열까지 다 기록하는 것이 아니라, 잘 몰랐거나 헷갈릴 내용들만을 따로 모아 항목 단위로 묶어 기록한다.

<br/>

### 목차

* <a href="">외부 스크립트 삽입하기</a>
* <a href="">JavaScript 기본 동작 원리</a>
* <a href="">JavaScript의 제약 사항</a>
* <a href="">세미콜론 자동 삽입</a>
* <a href="">주석</a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>

<br/><br/>

### 외부 스크립트 삽입하기

* JavaScript로 작성한 프로그램을 스크립트(script)라 부른다.

<br/>

* <code>\<script></code> 태그를 통해 HTML 문서에 자바스크립트 프로그램을 삽입할 수 있다.

* 삽입 방식은 크게 2가지다.

    * HTML 문서 내에 스크립트를 직접 작성하는 방식

    * 외부 스크립트 파일을 주소를 통해 삽입하는 방식

<br/>

* 외부 스크립트를 삽입할 때는 <code>src</code> 속성을 사용하면 된다.

    ```html
    <script src="/js/script_example.js"></script>
    ```

<br/>

* 스크립트가 길어지면 별도의 파일로 분리해 저장하는 것이 좋다.

* <code>\<script></code> 태그에 <code>src</code> 속성이 있을 경우, 태그 내부의 코드는 무시된다.

<br/><br/>

### JavaScript 기본 동작 원리

1. 파싱 : 앤진이 스크립트를 읽는다.

2. 컴파일 : 읽어들인 스크립트를 기계어로 번역한다.

3. 변역된 기계어 코드를 실행한다. (기계어로 전환되었으므로 실행 속도가 빠르다.)

<br/>

* JavaScript 엔진은 매 과정에서 최적화를 진행하여 스크립트 실행 속도를 더욱 높인다.

<br/><br/>

### JavaScript의 제약 사항

* JavaScript는 메모리나 CPU 같은 저수준 영역을 함부로 조작할 수 없다. ('안전한' 프로그래밍 언어)

* JavaScript는 보안을 위해, 디스크에 저장된 파일로의 접근을 막거나, 브라우저 내 탭이나 창에서 동의 없이 서로의 정보가 교환될 수 없다는 등의 제약이 걸려있다.

<br/><br/>

### 세미콜론 자동 삽입

* JavaScript에선 줄바꿈이 있을 시, 이를 '암시적' 세미콜론(';')으로 해석한다.

* 즉, 줄바꿈이 세미콜론을 대신할 수 있다는 것이다.

    ```javascript
    alert("Hello")
    alert("Bro")
    ```

<br/>

* 그러나, 자바스크립트가 세미콜론을 자동으로 삽입하지 않는 경우 또한 존재한다.

    ```javascript
    alert(1 + 
    2
    + 3);
    ```

    ```javascript
    alert("Hello World")

    [1, 2].forEach(alert)
    ```

<br/>

* ✨ 따라서, 문(statement)이 끝날 때마다 C언어처럼 항상 세미콜론을 붙이는 것이 좋다.

    ```javascript
    alert("Hello World");

    [1, 2].forEach(alert);
    ```

<br/><br/>

### 주석

* JavaScript 주석 문법은 C언어와 동일하게 <code>//</code> 또는 <code>/\*</code> <code>*/</code>을 사용한다.

    * <code>//</code> : 한 줄 주석

        ```javascript
        // 한 줄 주석
        ```

    * <code>/\*</code> <code>*/</code> : 여러 줄 주석

        ```javascript
        /*
            여러 줄 주석
        */
        ```

<br/>

* <code>/\*</code> <code>*/</code> 안에 또 다른 <code>/\*</code> <code>\*/</code>이 들어간 중첩 주석은 지원하지 않는다.

<br/><br/>

### 엄격 모드 (<code>use strict</code>)

* JavaScript는 기존의 기능을 유지하면서 발전해왔다. 

* 따라서 JS 창시자들이 했던 실수나 불완전한 경험이 언어 안에 고스란히 남아있었다.

* 2009년, ECMAScript5(EC5)이 새롭게 제정됨으로 인해 기존의 기능 일부가 변경되고 새로운 기능이 추가되었다.

* 이로 인해 생길 호환성 문제를 대비하여, 변경사항 대부분은 엄격 모드을 활성했을 때만 적용된다.

<br/>

* <code>use strict</code>를 코드 상단에 작성하면 엄격 모드가 적용되고, 코드 전체가 "모던한" 방식으로 동작한다.

* 특정 함수에만 엄격 모드를 적용하려면, 함수 본문 맨 앞에 <code>use strict</code>를 작성하면 된다.

<br/>

* <code>use strict</code>는 반드시 최상단에 위치해야 하며, 일단 염격 모드가 적용되면 되돌릴 방법은 없다.

* 클래스(<code>class</code>)나 모듈(<code>import</code>)을 사용하면 <code>use strict</code>가 자동으로 적용된다.


<br/><br/>

### 변수 (약점 Point)

* 변수 명명 시,

    * 오직 문자와 숫자, 기호 <code>$</code>와 <code>_</code>만 사용할 수 있다.

    * 첫 글자는 숫자가 될 수 없다.

    * 예약어 목록애 있는 단어로 작성할 수 없다.

    <br/>

    * 카맬 표기법(camelCase)로 작성하는 것이 좋다.

    * 간결하고 명확하되, 서술적으로 명명하여 변수가 담고 있는 것이 무엇인지 잘 설명할 수 있도록 하는 것이 중요하다.
    
        ```javascript
        let ourPlanetName = "Earth";
        let currentUserName = "John";
        ```
        
        * (data나 value는 나쁜 이름의 예시)


<br/>

* 변수를 선언 시, 자료형을 반드시 앞에 붙여서 선언하는 것이 중요하다.

    ```javascript
    let num = 5

    // num = 5
    /* 이런 식으로 작성 X
    엄격 모드에선 오류 발생 */
    ```

* 상수 중 코드가 실행되기 전에 이미 값을 알고 있는 경우, 상수명을 대문자로 작성하는 것이 좋다.

    ```javascript
    const COLOR_RED = "#F00";
    const PI = "3.14";
    ```

* 개발 시, 새로운 변수를 추가하는 것은 좋은 습관이다.   

    (변수를 재사용하면 디버깅에 10배 많은 시간을 쏟아야 한다.)

<br/><br/>

### 자료형

* JavaScript엔 8가지 기본 자료형이 있다.

* JavaScript는 하나의 변수에 저장되는 값의 종류가 자유롭게 바뀔 수 있는 '동적 타입(Dynamically Typed) 언어'이다.

<br/>

* <code>숫자형</code>

    * 정수, 부동 소숫점 숫자 등을 나타낼 때 사용한다.

    * 그 외애도 <code>Infinity</code>, <code>-Infinity</code>,<code>NaN</code> 같은 특수 숫자 값이 있다.

    * 이러한 특수 숫자 값 덕분에 스크립트는 말도 안되는 수학 연산을 하더라도 치명적인 에러를 내뿜으며 죽지 않는다. (수학 연산은 안전하다)

        ```javascript
        alert( 1 / 0 ); // Infinity
        alert(Infinity); // Infinity
        
        alert( "나는 빡빡이다" / 3 + 7); // NaN
        ```

    * 정수의 한계는 ±2^53이다.

* <code>bigint</code>

    * 길이 제약 없이 정수형을 나타낼 수 있다.

    * 정수 리터럴 끝에 n을 붙이면 만들 수 있다.

        ```javascript
        const bigInt = 1234567890123456789012345678901234567890n;
        ```

* <code>문자형</code>

    * 글자들로 이루어진 문자열을 나타낸다.
    
    * 비어있거나 한 글자여도 문자형으로 취급한다.

    * 역 따옴표(백틱)을 사용하면 문자열 중간에 변수나 표현식을 쉽게 삽입할 수 있다. (문자열의 일부로 출력된다.)

        ```javascript
        score = 100
        alert(`I got ${score} in test!`);
        alert(`I got ${50 + 50} in test!`);
        ```

* <code>boolean형</code>

    * <code>true</code>, <code>false</code>값을 나타낼 떄 사용된다.

* <code>null</code>

    * <code>null</code> 값만을 위한 독립 자료형이다.

    * 존재하지 않는 값, 비어 있는 값, 알 수 없는 값을 나타내는 데 사용된다.

* <code>undefined</code>

    * <code>undefined</code> 값만을 위한 독립 자료형이다.

    * 값이 할당되지 않은 상태를 나타낸다.

    * 변수를 선언했지만, 값을 할당하지 않은 경우, 해당 변수에 <code>undefined</code>가 자동으로 할당된다.

    * 변수에 <code>undefined</code>를 직접 할당하는 것은 권장하지 않는다.

* <code>객체형</code>

    * 데이터 컬렉션이나 복잡한 객체를 표현할 떄 사용한다.

* <code>심볼형</code>

    * 객체의 고유한 식별자를 만들 때 사용한다.

<br/>

* <code>typeof</code> 연산자는 피연산자의 자료형을 문자열 형태로 반환한다.

* 연산자 형태 <code>typeof x</code> 또는 함수 형태 <code>typeof(x)</code>로 사용된다.

<br/>

* <code>null</code>의 typeof 연산은 <code>"object"</code>인데, 이는 언어상의 오류다. null은 객체가 아니다.

* 함수(예:<code>alert</code>)의 typeof 연산은 <code>"function"</code>인데, '함수'형은 따로 존재하지 않는다. 함수는 객체형에 속한다. 이 또한 오류이나, 하위 호환성 문제로 인해 언어에 남겨져 있다.