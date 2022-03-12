# JavaScript 기본 5 - 조건 연산자, 논리 연산자

> 참고 자료 : <a href="https://ko.javascript.info/">javascript.info</a>

<br/>

- <a href="https://ko.javascript.info/">javascript.info</a>의 【자바스크립트 기본】 챕터 10 ~ 11장 내용

<br/>

### 목차

- <a href="">조건 연산자 (간단 정리)</a>
- <a href="">조건부 연산자 (물음표 연산자) <code>?</code></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 조건 연산자 (간단 정리)

* <code>if</code>문은 조건을 처리하여 분기를 할 수 있는 문법이다.

<br/>

* <code>if (...)</code>문의 괄호 안에 들어가는 조건식(표현식)은 불린형 값을 반환하고, 만일 그 값이 <code>true</code>면 코드 블록을 실행한다.

    * 불린형으로 변환 시 true가 되는 값은 'truthy(참 같은) 값이라 한다. (예 : <code>0</code>, <code>""</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code>)

    * 반대로, 불린형으로 변환 시 false가 되는 값은 'falsy(거짓 같은) 값이라 한다.

<br/>

* 이 떄, 중괄호 <code>{}</code>로 코드 불록을 항상 감싸준다. 코드 블록이 한 줄 뿐이더라도 중괄호로 감싸는 것이 가독성에 좋기 떄문이다.

<br/>

* <code>else</code>문은 <code>if</code>문에 붙여, 조건이 거짓일 때 뒤에 이어지는 코드 블록을 실행하는 문법이다. <code>else</code>문은 필수가 아닌 선택 사항이다.

* <code>if</code>문과 <code>else</code>문 중간에 <code>else if</code>를 사용하면, 조건 여러 개를 처리할 수 있다.

    ```javascript
    let age = prompt('당신의 나이는 몇 살입니까?', '');

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

## 조건부 연산자 (물음표 연산자) <code>?</code>

* 자바스크립트에서 피연산자를 3개 받는 유일한 연산자로, C++의 삼항 연산자와 동일한 문법을 가졌다.

* 조건에 따라 반환 값을 달리하려는 목적으로 만들어졌다.

    ```javascript
    let = result = condition ? value1 : value2;
    ```

    * 평가 대상인 <code>condition</code>이 truthy라면 <code>value1</code>이 반환되고, 그렇지 않다면 <code>value2</code>가 반환된다.

<br/>

* 예시

    ```javascript
    let age = prompt('당신의 나이는 몇 살입니까?', '');

    let accessAllowed = (age > 18) ? true : false;
    ```

<br/>

* 물음표 연산자 <code>?</code>를 여러 개 연결하면, <code>else if</code>문을 사용하는 것처럼, 복수의 조건을 처리할 수 있다.

* 하지만 이보단 <code>else if</code>문을 사용하는 것이 가독성에 좋다.