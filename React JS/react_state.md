# React JS - State

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>

<br/>

### 목차

- <a href=""><code></code></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## <code>React.useState()</code> 함수

- React에서 변수를 다루는 유용한 방법

- 반드시 컴포넌트 내부에서만 사용할 수 있다.

<br/>

- <code>React.useState()</code> 호출 시 '<strong>변수값</strong>'과 '<strong>modifier 함수</strong>' 2개의 원소가 배열로 묶여 반환된다.

  ```html
  <script type="text/babel">
    const root = document.getElementById("root");
    const App = () => {
      <!-- 주목할 부분 -->
      const data = React.useState(0);
      console.log(data);
      <!-- 여기까지 -->
      return (
        <div>
          <h3>Total clicks: {counter}</h3>
          <button>Click Me</button>
        </div>
      );
    };
    ReactDOM.render(<App />, root);
  </script>
  ```

  ```
  [undefined, f ]
  ```

  - <strong>undefined</strong> : 데이터 (변수)

  - <strong>f</strong> : 데이터를 바꾸는 modifier 함수

<br/>

- <strong><a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9">구조분해할당</a></strong>을 활용하면 좀 더 효율적으로 코드를 작성할 수 있다.

  ```html
  <script type="text/babel">
    const root = document.getElementById("root");
    const App = () => {
      <!-- 주목할 부분 -->
      const [counter, setCounter] = React.useState(0);
      const onClick = () => {
        setCounter(counter + 1);
      };
      <!-- 여기까지 -->
      return (
        <div>
          <h3>Total clicks: {counter}</h3>
          <button onClick={onClick}>Click Me</button>
        </div>
      );
    };
    ReactDOM.render(<App />, root);
  </script>
  ```
