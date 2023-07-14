# ReactJS로 영화 웹 서비스 만들기 - 강의 내용 필기

<br/>

- React의 탄생 목적

  - 인터렉티브 UI를 위함

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
