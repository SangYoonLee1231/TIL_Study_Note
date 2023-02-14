# React JS - JSX와 컴포넌트 (Component)

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#createelement%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EA%B8%B0%EC%A1%B4%EC%9D%98-%EB%B0%A9%EB%B2%95%EC%9C%BC%EB%A1%9C-html-%EC%9A%94%EC%86%8C-%EB%8B%A4%EB%A3%A8%EA%B8%B0%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0"><code>createElement</code>를 이용한 기존의 방법으로 HTML 요소 다루기/추가하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#jsx">JSX</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#jsx%EC%9D%98-%ED%8A%B9%EC%A7%95">JSX의 특징</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#createelement-vs-jsx"><code>createElement</code> vs JSX</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#babel">Babel</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">컴포넌트</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-component-%EB%9E%80">컴포넌트 (Component) 란?</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-vs-%ED%95%A8%EC%88%98-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">클래스 컴포넌트 vs 함수 컴포넌트</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EC%83%9D%EC%84%B1--%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EB%A5%BC-%EB%8B%A4%EB%A5%B8-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%97%90-%EB%84%A3%EA%B8%B0-1">컴포넌트 생성 & 컴포넌트를 다른 컴포넌트에 넣기</a>

<br/><br/>

## <code>createElement</code>를 이용한 기존의 방법으로 HTML 요소 다루기/추가하기

- <strong>구현 목표</strong>

    <img src="img/react_jsx1.png">

  - 1.&nbsp;&nbsp;<code>Hello I'm a span</code>에 마우스 닿을 시, 콘솔 창에 <code>mouse enter</code> 문구 표시

  - 2.&nbsp;&nbsp;<code>Click me</code> 버튼 클릭 시, 콘솔 창에 <code>i clicked</code> 문구 표시

<br/><br/>

- <strong>Vanila JS</strong>로 구현

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <body>
      <h3 id="text">Hello. I'm a span.</h3>
      <button id="btn">Click Me</button>
    </body>
    <script>
      const text = document.getElementById("text");
      const button = document.getElementById("btn");

      text.id = "title";
      button.style.backgroundColor = "tomato";

      function handleClick() {
        console.log("i clicked");
      }

      function handleMouseEnter() {
        console.log("mouse enter");
      }

      button.addEventListener("click", handleClick);
      text.addEventListener("mouseenter", handleMouseEnter);
    </script>
  </html>
  ```

<br/><br/>

- <strong>React JS</strong>로 구현 + <code>createElement</code> 함수 활용

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <body>
      <div id="root"></div>
    </body>
    <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.development.js"></script>
    <script>
      const root = document.getElementById("root");

      const title = React.createElement(
        "h3",
        {
          id: "title",
          onMouseEnter: () => console.log("mouse enter"),
        },
        "Hello. I'm a title."
      );

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

      const container = React.createElement("div", null, [h3, btn]);
      ReactDOM.render(container, root);
    </script>
  </html>
  ```

<br/>

- <strong>React JS를 이용하는 것</strong>이 Vanila JS를 이용하는 것보다 <strong>더 편리함</strong>을 확인할 수 있다.

  - <strong>JS에서 직접 HTML 요소를 생성</strong>한 후 <strong>필요한 기능을 한 번에 붙인 뒤</strong> HTML에 삽입하기만 하면 되므로

<br/>

- 하지만 <code>createElement</code>를 사용한 위 두 방법보다 <strong>더 편리하게</strong> HTML 요소를 만들어 넣는 방법이 있다.

  => <strong>JSX</strong>

<br/><br/>

### 참고 : Vanila JS로 <code>React.createElement()</code> 직접 구현하기

```js
// Vanila JS로 React.createElement 함수 직접 구현 (하드 코딩)

function createElement(tagName, ...children) {
  const element = document.createElement(tagName);

  children.forEach((child) => {
    element.appendChild(child);
  });

  return element;
}

// 구현한 createElement 함수 활용법

document
  .getElementById("app")
  .appendChild(
    createElement(
      "div",
      createElement(
        "p",
        ...["!!!", "!!!!!"].map((c) =>
          document.createTextNode(`Hello World${c}`)
        )
      ),
      createElement("p", document.createTextNode("Hi!!!"))
    )
  );
```

<br/><br/><br/>

## JSX

- <strong>JSX</strong>는 <strong>JavaScript의 문법을 확장</strong>한 React만의 문법으로, <strong>JavaScript 내에서 HTML 마크업을 사용할 수 있도록 한 것</strong>이다.

- 마크업과 자바스크립트 로직이 서로 연결되어 있다고 판단하여 이를 한 번에 작성할 수 있는 방법을 고민한 결과 생겨난 문법이다.

- JavaScript 내에서 마크업을 작성할 수 있고, JS 로직도 함께 작성할 수 있다.

<br/>

- <strong>JavaScript 정식 문법은 아니기 때문에 브라우저에서 이를 해석할 수 없다.</strong>

  따라서 <strong>Babel</strong> 변역기를 통해 이를 <code>React.createElement()</code> 함수로 변환하는 과정이 반드시 필요하다.

<br/><br/>

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
      return <h1 style={{
        color: "red",
        backgroundColor: "yellow",
      }}
      >
        Hello 이코딩
      </h1>;
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

<br/>

#### Babel 사용법

- <strong>1.</strong> Babel standalone를 이용하여 변환기 설치하기

  - HTML에 다음을 삽입한다.

    ```html
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    ```

  - 그리고 JS 코드를 작성할 때 script 태그의 속성(property)에 <code>type="text/babel"</code>를 부여해준다.

    ```html
    <script type="text/babel">
      // JS 코드를 작성하는 곳
    </script>
    ```

  <br/>

  - 이 방식은 느리기 때문에 혼자할 때는 절대 이렇게 할 일이 없을 것이다. 이보다 더 나은 방식이 있다.

<br/>

- <strong>2. Node.js를 통해 설치하기</strong>

  - 사전 지식 : <a href="">Node JS & NPM 소개 및 설치</a>

  <br/>

  - <strong>설치 명령어</strong>

    - <code>npm i -D babel-loader</code> : Webpack에서 Babel을 쓸 수 있도록 도와줌
    - <code>webpack.config.js</code> 파일 : webpack 설정 파일
    - <code>npm i -D @babel/core</code>
    - <code>npm i -D @babel/preset-env @babel/preset-react</code>

  <br/>

  - <strong>config 설정</strong>

    - <code>webpack.config.js</code>

      ```javascript
      module.exports = {
        mode: "development",
        module: {
          rules: [
            {
              test: /\.(js|jsx)?$/,
              loader: "babel-loader",
              options: {
                presets: ["@babel/preset-env", "@babel/preset-react"],
              },
            },
          ],
        },
        resolve: { extensions: [".js", ".jsx"] },
      };
      ```

    - <code>babel.config.js</code>

      ```javascript
      module.exports = {
        presets: [
          [
            "@babel/preset-env",
            {
              targets: {
                node: "current",
                chrome: "79",
              },
            },
          ],
          "@babel/preset-react",
        ],
      };
      ```

<br/><br/><br/>

## 컴포넌트

### 컴포넌트 (Component) 란?

- 컴퓨터 과학에서 컴포넌트란?

  - <strong>독립적이고, 재사용할 수 있는 소프트웨어 구성</strong>

<br/>

- 프론트엔드에서 컴포넌트란?

  - <strong>독립적이고, 재사용할 수 있는 UI 단위</strong>

  - 로고 블록을 조립해서 큰 성을 만들듯이, 작은 UI를 조합해서 큰 UI를 구성할 수 있다.

<br/>

- 컴포넌트란 <strong>JSX를 반환하는 함수</strong>이다. (<strong>함수형 컴포넌트</strong>)

- 임의의 입력값(props)을 받아 화면에 어떻게 표시할 지를 기술하는 React 엘리먼트(element)를 반환한다.

- 일반 element를 함수형으로 바꾸면 컴포넌트(사용자 정의 태그)로 인식된다.

<br/>

- ✨ 직접 만든 컴포넌트를 렌더링해서 다른 곳에 사용할 때는 <strong>이름이 항상 대문자로 시작</strong>되어야 한다.

- ✨ 컴포넌트를 리렌더링 시, 전체를 전부 재생산하지 않고 <strong>전과 달리진 부분만 새로 생성</strong>한다.

<br/><br/>

### 클래스 컴포넌트 vs 함수 컴포넌트

- <strong>클래스 컴포넌트</strong>

  ```js
  class Component {
    render() {
      <section>
        <h1>Hello World</h1>
      </section>;
    }
  }
  ```

  - state, lifeCycle 등의 기능을 이용할 수 있어 초항기에 많이 사용된 방식이다.

  - 하지만, Class의 문법과 동작이 복잡하다는 단점이 존재한다.

<br/>

- <strong>함수 컴포넌트</strong>

  ```js
  function Component() {
    return (
      <section>
        <h1>Hello World</h1>
      </section>
    );
  }
  ```

  ```js
  const Component = () => (
    <section>
      <h1>Hello World</h1>
    </section>
  );
  ```

  - 클래스에 비해 직관적이고 사용하기 쉽지만, state, lifeCycle 등의 기능을 이용할 순 없었다.

  - 하지만 React 16.8 버전에서 Hook이란 개념의 등장으로 위 기능들을 함수 컴포넌트에서도 사용할 수 있게 되었다.

  - 그로 인해 <strong>현재 React 생태계에서는 함수 컴포넌트를 가장 많이 사용한다.</strong>

<br/><br/>

### 컴포넌트 생성 & 컴포넌트를 다른 컴포넌트에 넣기

```javascript
const root = document.getElementById("root");

// Title 컴포넌트
const Title = () => (
  <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
    Hello I'm a title
  </h3>
);

// Btn 컴포넌트
const Btn = () => (
  <button
    style={{
      backgroundColor: "tomato",
    }}
    onClick={() => console.log("i clicked")}
  >
    Click Me
  </button>
);

// Title, Btn 컴포넌트를 포함하는 Container 컴포넌트
const Container = () => (
  <>
    <Title />
    <Btn />
  </>
);

// Title, Btn, Container와 같이 이름이 대문자로 시작되어야만 React에서 컴포넌트를 컴포넌트로 바르게 인식한다.

ReactDOM.render(<Container />, root);
```
