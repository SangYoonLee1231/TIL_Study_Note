# ReactJS로 영화 웹 서비스 만들기 - 강의 내용 필기

<br/>

- React의 탄생 목적 및 사용 이유

  - 인터렉티브 UI를 위함 (리렌더링 시 바뀐 부분만 반영하여 업데이트)

<br/>

- React JS는 어플리케이션이 아주 interactive하도록 만들어주는 라이브러리이고

- React DOM은 모든 React element를 HTML Body에 둘 수 있도록 해주는 라이브러리 또는 패키지이다.

<br/>

- `React.createElement();`: HTML 요소를 생성해주는 React의 createElement 함수

  - 첫 번째 인자: 생성하려는 HTML 요소의 태그 이름

  - 두 번째 인자: 생성하려는 HTML 요소의 property

  - 세 번째 인자: 생성하려는 HTML 요소의 content

- `ReactDOM.render()`: React element를 가지고 HTML로 만들어 배치한다. (React element를 사용자에게 보여준다)

- 사용 예시

  ```js
  const root = document.getElementById("root");
  const span = React.createElement(
    "span",
    {
      id: "sexy-span",
      style: { color: "red" },
    },
    "Hello, I'm a span"
  );
  ReactDOM.render(span, root);
  ```

<br/>

- React JS는 **모든 것이 JavaScript에서 시작**한다. HTML 요소를 JS에서 직접 만들어서 HTML에 반영한다.

- 이를 CSR(Client Side Rendering)이라 부른다.

<br/>

- 인터렉티브한 어플리케이션에서 하는 작업은 결국 **모든 event들을 감지**하고, 그에 맞는 특정 동작을 수행하도록 하는 것이다.

<br/>

- <strong>JSX</strong>는 <strong>JavaScript의 문법을 확장</strong>한 React만의 문법으로, <strong>JavaScript 내에서 HTML 마크업을 사용할 수 있도록 한 것</strong>이다.

- 마크업과 자바스크립트 로직이 서로 연결되어 있다고 판단하여 이를 한 번에 작성할 수 있는 방법을 고민한 결과 생겨난 문법이다.

- JavaScript 내에서 마크업을 작성할 수 있고, JS 로직도 함께 작성할 수 있다.

<br/>

- <strong>JavaScript 정식 문법은 아니기 때문에 브라우저에서 이를 해석할 수 없다.</strong>

  따라서 <strong>Babel</strong> 변역기를 통해 이를 <code>React.createElement()</code> 함수로 변환하는 과정이 반드시 필요하다.

<br/><br/>

## JSX

- <strong>JSX</strong>는 <strong>JavaScript의 문법을 확장</strong>한 React만의 문법으로, <strong>JavaScript 내에서 HTML 마크업을 사용할 수 있도록 한 것</strong>이다.

- 마크업과 자바스크립트 로직이 서로 연결되어 있다고 판단하여 이를 한 번에 작성할 수 있는 방법을 고민한 결과 생겨난 문법이다.

- JavaScript 내에서 마크업을 작성할 수 있고, JS 로직도 함께 작성할 수 있다.

<br/>

- <strong>JavaScript 정식 문법은 아니기 때문에 브라우저에서 이를 해석할 수 없다.</strong>

  따라서 <strong>Babel</strong> 변역기를 통해 이를 <code>React.createElement()</code> 함수로 변환하는 과정이 반드시 필요하다.

<br/>

### JSX의 특징

- <strong>JSX는 자바스크립트의 값이다.</strong>

  - 특정한 변수에 이 값을 담을 수 있고, 함수의 인자로 전달하거나 함수의 리턴값으로 사용할 수 있다.

    ```js
    function App() {
      return <h1>Hello 이코딩</h1>;
    }

    const hello = App();
    ```

<br/>

- <strong>JSX는 자바스크립트 값을 포함할 수 있다.</strong>

  - 중괄호를 이용해서 자바스크립트의 값을 감싸주면 된다.

  - 함수의 반환 값도 값이므로, (반환값이 있는) 함수를 중괄호로 감싸 JSX 내부에서 사용할 수 있다.

    ```js
    function App() {
      const name = "이코딩";

      return <h1>Hello {name}</h1>;
    }
    ```

    ```js
    function App() {
      return <h1>Hello {() => "이코딩"}</h1>;
    }
    ```

<br/>

- <strong>JSX 안에서 태그의 속성(Attribute)을 정의할 수 있다.</strong>

  - 문자열로 줄 수도 있고 중괄호를 사용하여 JS 값으로 줄 수도 있다.

    ```js
    function App() {
      const class = "title";

      return <h1 className={class}>Hello 이코딩</h1>;
    }
    ```

<br/>

- <strong>JSX에서 요소에 inline 방식으로 이벤트 라스너를 등록할 수 있다.</strong>

  - 태그를 작성할 때 <code>on</code> 뒤에 이벤트 명을 작성하는 방식으로 바로 이벤트 리스너를 부착할 수 있다.

    ```js
    const introduce = () => alert("Hello World");

    function App() {
      return <h1 onClick={introduce}>Hello 이코딩</h1>;
    }
    ```

<br/>

- <strong>JSX에서 요소에 JavaScript 객체 형태로 inline style을 줄 수 있다.</strong>

  - key-value 형태로 작성한 객체의 이름을 원하는 요소에 style 속성의 속성값으로 주면 된다.

    ```js
    const style = {
      color: "red",
      backgroundColor: "yellow",
    };

    function App() {
      return <h1 style={style}>Hello 이코딩</h1>;
    }
    ```

  - JSX 내부에서 바로 스타일 객체를 선언하고 싶은 경우, 아래처럼 태그의 style 속성값에 객체를 작성하면 된다.

    ```js
    function App() {
      return (
        <h1
          style={{
            color: "red",
            backgroundColor: "yellow",
          }}
        >
          Hello 이코딩
        </h1>
      );
    }
    ```

<br/>

- <strong>JSX 요소는 반환값 전체가 하나의 부모 태그로만 감싸져 있어야 한다.</strong>

  - <code>React.Fragment</code> 태그를 활용하자. (실제로 이 태그는 브라우저에 표시되지 않는다)

    ```js
    function App() {
      return (
        <React.Fragment>
          <h1>Hello 이코딩</h1>
          <p>
            Who is 이코딩? For the blind, He is vision. For the hungry, He is
            the chef. For the thirsty, He is water. If 이코딩 thinks, I agree.
            If 이코딩 speaks, I’m listening. If 이코딩 has one fan, it is me. If
            이코딩 has no fans, I do not exist.
          </p>
        </React.Fragment>
      );
    }
    ```

  - <code>\<></code>, <code>\</></code> 로 단축해서 쓸 수도 있다.

    ```js
    function App() {
      return (
        <>
          <h1>Hello 이코딩</h1>
          <p>
            Who is 이코딩? For the blind, He is vision. For the hungry, He is
            the chef. For the thirsty, He is water. If 이코딩 thinks, I agree.
            If 이코딩 speaks, I’m listening. If 이코딩 has one fan, it is me. If
            이코딩 has no fans, I do not exist.
          </p>
        </>
      );
    }
    ```

<br/>

- 그 외 JSX의 특징 및 규칙

  - <strong>JSX 태그는 확실하게 닫아주어야 한다.</strong>

<br/>

### <code>createElement</code> vs <strong>JSX</strong>

- <code>createElement</code>로 작성된 코드와 <strong>JSX</strong> 문법으로 작성된 코드를 서로 비교해보면 <strong>JSX</strong> 문법의 강력함을 알 수 있다.

  - 예시 1

    - <code>createElement</code>

      ```javascript
      const title = React.createElement(
        "h3",
        {
          id: "title",
          onMouseEnter: () => console.log("mouse enter"),
        },
        "Hello. I'm a title."
      );
      ```

    - <strong>JSX</strong>

      ```javascript
      const title = (
        <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
          Hello I'm a title
        </h3>
      );
      ```

  <br/>

  - 예시 2

    - <code>createElement</code>

      ```javascript
      const btn = React.createElement(
        "button",
        {
          onClick: () => console.log("i clicked"),
          style: {
            backgroundColor: "tomato",
          },
        },
        "Click Me"
      );
      ```

    - <strong>JSX</strong>

      ```javascript
      const btn = (
        <button
          style={{
            backgroundColor: "tomato",
          }}
          onClick={() => console.log("i clicked")}
        >
          Click Me
        </button>
      );
      ```

<br/>

- JSX 문법은 HTML과 유사하나 다른 점도 존재함을 기억해야 한다.

  - <code>class</code>나 <code>for</code>같은 키워드는 React JS에서 제대로 동작하지 않을 수 있다.

    (<strong><code>class</code> => <code>className</code>, <code>for</code> => <code>htmlFor</code>을 써야 한다.</strong>)

<br/>

- (위에서 언급했지만) JSX 문법으로 작성한 코드는 브라우저가 바로 이해할 수 없기 때문에, 브라우저가 이해할 수 있는 형태로 변환해주는 장치가 필요하다.

  => <strong>Babel</strong>

<br/><br/>

### Babel

- <strong>Babel이란?</strong>

  - 브라우저마다 사용하는 언어가 달라 발생하는 크로스 브라우징 이슈를 해결하기 위해, 스크립트를 '트랜스파일'하여 모든 브라우저에서 동작할 수 있도록 하는 장치

    - 트랜스파일 : 추상화 수준이 같은 코드로 변환해주는 것 (vs 빌드)

  - ECMAScript2015 이상의 코드를 적당한 하위 버전으로 변환

  - TypeScript나 JSX은 Babel의 변환 대상이다.

  - <a href="https://babeljs.io/">Babel 홈페이지 바로가기</a>

<br/><br/><br/>

## State란?

- 컴포넌트 내부에서 가지고 있는 컴포넌트의 상태값

- 컴포넌트 내에서 정의하고 사용하며, 변수처럼 얼마든지 변경할 수 있다.

<br/><br/>

## <code>React.useState()</code> 함수

- <strong>React의 내장 Hook</strong>으로, React에서 변수를 다루는 유용한 방법이다.

- Hook이기 때문에 <strong>반드시 컴포넌트 내부에서만 사용할 수 있다.</strong>

<br/>

- <code>React.useState()</code> 호출 시 '<strong>변수값</strong>'과 '<strong>modifier 함수</strong>' 2개의 원소가 배열로 묶여 반환된다.

  ```javascript
  const root = document.getElementById("root");

  const App = () => {
    // 주목할 부분!!
    const data = React.useState(0);
    console.log(data);
    // 여기까지!!

    return (
      <div>
        <h3>Total clicks: {counter}</h3>
        <button>Click Me</button>
      </div>
    );
  };
  ReactDOM.render(<App />, root);
  ```

  ```
  [undefined, f ]
  ```

  - 첫 번째 요소 : <strong>undefined</strong>

    ➡️ 데이터 (변수)

  - 두 번째 요소 : <strong>f</strong>

    ➡️ 데이터를 바꾸는 Modifier 함수

<br/>

- <strong><a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9">구조분해할당</a></strong>을 활용하면 좀 더 효율적으로 코드를 작성할 수 있다.

  ```javascript
  const root = document.getElementById("root");

  const App = () => {
    // 주목할 부분!!
    const [counter, setCounter] = React.useState(0);

    const onClick = () => {
      setCounter(counter + 1);
    };
    // 여기까지!!

    return (
      <div>
        <h3>Total clicks: {counter}</h3>
        <button onClick={onClick}>Click Me</button>
      </div>
    );
  };
  ReactDOM.render(<App />, root);
  ```

<br/>

- ✨ <strong>modifier 함수를 통해 state(값)을 변경하면 컴포넌트가 새 값을 가지고 재생성 (리랜더링) 된다.</strong>

  이것이 React에서 변수 대신 <strong>State를 사용하는 이유</strong>이다.

<br/><br/><br/>

## <code>React.useState()</code>의 Modifier 함수

- <strong>setState 함수는 비동기적으로 동작한다.</strong> 따라서 의도한 대로 동작하지 않을 수 있다.

  - 관련 내용에 대해 정리한 블로그 포스트 👉<a href="https://sylagape1231.tistory.com/61">바로가기</a>

- state 변경 시 이전 값을 바탕으로 현재 값을 설정하는 더 안전한 방법은 <strong>함수를 사용하는 것</strong>이다.

  ```javascript
  // 덜 안전한 방법
  const [counter, setCounter] = React.useState(0);

  const onClick = () => {
    setCounter(counter + 1);
  };
  ```

  ```javascript
  // 더 안전한 방법 - 함수 사용
  const [counter, setCounter] = React.useState(0);

  const onClick = () => {
    setCounter((current) => current + 1);
  };
  ```

- 함수를 사용하면 state 값이 외부에서 변경되는 경우로 인해 예상과 다른 결과가 나오는 상황을 대비할 수 있다.

<br/>

- ❓ modifier 함수 (setState 함수) 내에 변수 명을 current로 설정해도 무방한 이유

  - setState는 그 인자값이 객체인지 함수인지 판별하는 부분이 있다. 만일 함수일 경우 알아서 현재 state값을 찾아 매핑해준다.
