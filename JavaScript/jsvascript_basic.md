# JavaScript 기초 문법 (주의 포인트만)

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

* 자바스크립트의 문법을 전반적으로 다 기록하는 것이 아니라, 잘 몰랐거나 헷갈릴 내용들만을 항목 단위로 기록한다.

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