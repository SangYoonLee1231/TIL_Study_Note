# 1주차 Day 5 TIL

#### 2022.08.05

<br/>

## 오늘 한 것 (+ 학습한 것)

### 【1】 React 개념 학습 (By 공식 문서)

- React 공식 문서의 '<strong>2. JSX 소개</strong>', '<strong>3. 엘리먼트 렌더링</strong>', '<strong>4. Component와 Props</strong>' 이 세 파트를 공부했다.

  - <strong>JSX</strong>

    - 유저에게 보여지는 UI를 더 쉽게 파악할 수 있는 (이해하기 쉬운) 코드를 작성하도록 돕는다.

    - JS의 확장 문법으로 HTML 형태와 유사하다.

<br/><br/>

### 【2】 JavaScript '객체' 학습

- 객체는 key와 value 한 쌍의 데이터(프로퍼티)를 여러 개 저장할 수 있는 데이터 구조이다.

- 프로퍼티 key는 문자열이어야 하지만, value는 어떤 자료형도 상관 없다.

- 객체는 중괄호를 이용해 만들 수 있다. ('객체 리터럴' 문법) / 혹은 생성자를 이용하여 만들 수도 있다. ('객체 생성자' 문법)

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

      - <code>Object.keys(obj)</code> – 객체의 key만 담은 배열을 반환힌디.
      - <code>Object.values(obj)</code> – 객체의 value만 담은 배열을 반환힌디.
      - <code>Object.entries(obj)</code> – [key, value] 쌍을 담은 배열을 반환힌디.

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

          children.flat().forEach((child) => {
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

- (드디어) <strong>과제 1 뼈대 코드 완성</strong>

  (문제가 될 수 있으니 코드는 올리지 않겠습니다.)

<br/><br/>

## 과제 진행

### 과제1. let을 제거해보자

- <a href="https://github.com/CodeSoom/react-week1-assignment-1/pull/193">PR 기록 바로가기</a>

  - 스크립트를 저장하면 ESLint가 바로 적용이 된다고 생각하여, Lint 테스트를 돌려보지 않은 채 PR을 보내고 말았다. 다음부턴 PR 전 꼭 Lint 테스트를 돌려보자.

<br/>

### 과제 2 - 간단한 사칙 연산 계산기 구현

(수행하지 못함)

<br/><br/>

## Feeling

- 오늘 드디어 첫 번째 과제를 수행하여 PR을 날렸다. 며칠 전까지만 해도 과연 내가 시간 내에 과제를 수행할 수 있을까 싶었는데 포기하지 않고 꾸준히 하니 결국 해냈다.

- 비록 두 번째 과제는 같은 기수 분들 중 유일하게 코드 제출을 하지 못했지만, 그래도 정말 뿌듯했다. 역시 하면 되는구나.

- 한 주 동안 고생 많았다. 그렇지만 이제 시작이구나.  
  나중에 가면 현업 개발자 수강생 분들도 쩔쩔맬만큼 과정이 어려워진다던데, 과연 내가 그걸 해낼 수 있을까?

  솔직히 좀 불안하지만, 최선을 다해보면 어떻게든 된다는 걸 믿기에 일단 지금 미리 걱정하진 않기로.
