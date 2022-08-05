# 1주차 Day 5 TIL

#### 2022.08.05

<br/>

## 오늘 한 것 (+ 학습한 것)

### 【1】 React 개념 학습 (By 공식 문서)

- React 공식 문서의 '<strong>2. JSX 소개</strong>', '<strong>3. 엘리먼트 렌더링</strong>', '<strong>4. Component와 Props</strong>' 이 세 파트를 공부했다.

    - <strong>JSX</strong>

        - 유저에게 보여지는 UI를 더 쉽게 파악할 수 있는 (이해하기 쉬운) 코드를 작성하도록 돕는다.

        - JS의 확장 문번으로 HTML 형태와 유사하다.

<br/><br/>

### 【2】 JavaScript '객체' 학습

- 객체는 key와 value 한 쌍의 데이터(프로퍼티)를 여러 개 저장할 수 있는 데이터 구조이다.

- 프로퍼티 key는 문자열이어야 하지만, value는 어떤 자료형도 상관 없다.

- 객체는 중괄호를 이용해 만들 수 있다. ('객체 리터럴' 문법) 혹은 생성자를 이용하여 만들 수도 있다. ('객체 생성자' 문법)

- 객체는 참조에 의해 저장되고 복사된다. (by reference)

<br/>

- <strong>점 표기법</strong> vs <strong>대괄호 표기법</strong>

    - 대괄호 표기법은 프로퍼티 이름과 값의 제약을 없애주기 때문에 점 표기법보다 훨씬 강력하지만, 작성하기 번거롭다는 단점이 있다.

    - 이런 이유로 보통 프로퍼티 이름이 확정되었고 단순하다면 처음엔 점 표기법을 사용하다가, 나중에 뭔가 복잡한 상황이 발생했을 때 대괄호 표기법으로 바꿔준다.

- <strong>단축 프로퍼티</strong>

- <strong>프로퍼티 이름의 제약사항</strong>

- <strong><code>in</code> 연산자</strong>

- <strong>for...in 반복문</strong>

- <strong>객체 정렬 디폴트 방식</strong>

<br/>

- <strong>Object.keys(), values(), entries()</strong>

    - <code>Object.keys(obj)</code> – 객체의 key만 담은 배열을 반환합니다.
    - <code>Object.values(obj)</code> – 객체의 value만 담은 배열을 반환합니다.
    - <code>Object.entries(obj)</code> – [key, value] 쌍을 담은 배열을 반환합니다.

        ```javascript
        let user = {
            name: "John",
            age: 30
        };

        Object.keys(user) => ["name", "age"]
        Object.values(user) => ["John", 30]
        Object.entries(user) => [ ["name","John"], ["age",30] ]
        ```

        ```javascript
        const object1 = {
            a: 'somestring',
            b: 42
        };

        for (const [key, value] of Object.entries(object1)) {
            console.log(`${key}: ${value}`);
        }

        // expected output:
        // "a: somestring"
        // "b: 42"
        ```
<br/>

- <strong>instanceof 연산자</strong>

    - 객체가 특정 클래스에 속하거나, 특정 클래스를 상속받으면 true를 반환하는 연산자

<br/><br/>

### 【3】 코드숨 JSX 파트 마무리

- <strong><code>React.createElement()</code> 함수 직접 구현해보기</strong>

    ```javascript
    /* @jsx createElement */

    function createElement(tagName, props, ...children) {
        const element = document.createElement(tagName);

        Object.entries(props || {}).forEach(([key, value]) => {
            element[key.toLowerCase()] = value;
        });

        children.forEach((child) => {
            if (child instanceof Node) {
                element.appendChild(child);
                return;
            }
            element.appendChild(document.createTextNode(child));
        });

        return element;
    }
    ```
<br/>

- <strong>과제 1 뼈대 코드 완성</strong>

    (문제가 될 수 있으니 코드는 올리지 않겠습니다.)