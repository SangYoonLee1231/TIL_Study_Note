# React JS - SPA & Routing

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, <a href="https://nomadcoders.co/react-masterclass">노마드 코더 - React JS 마스터클래스</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#spa--routing">SPA & Routing</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#spa-single-page-application-%EC%9D%98-%EA%B0%9C%EB%85%90">SPA (Single Page Application) 의 개념</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#routing%EC%9D%98-%EA%B0%9C%EB%85%90">Routing의 개념</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#routing---by-browserrouter-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">Routing - By <code>BrowserRouter</code> 컴포넌트</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#routing-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0">Routing 기능 구현하기</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#react-router-dom%EC%97%90%EC%84%9C-%EC%A0%9C%EA%B3%B5%ED%95%98%EB%8A%94-%EA%B2%BD%EB%A1%9C-%EC%9D%B4%EB%8F%99-%EB%B0%A9%EB%B2%95-2%EA%B0%80%EC%A7%80"><code>react-router-dom</code>에서 제공하는 경로 이동 방법 2가지</a>
    - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#1-link-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">1. <code>Link</code> 컴포넌트</a>
    - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#2-usenavigate-hook">2. <code>useNavigate</code> hook</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_spa_routing.md#routing---by-createbrowserrouter-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">Routing - By <code>createBrowserRouter</code> 컴포넌트</a>

<br/><br/>

## SPA & Routing

### SPA (Single Page Application) 의 개념

- SPA는 <strong>페이지가 하나인 웹 어플리케이션</strong>을 의미한다.

- 여기서 페이지란 html 파일을 뜻하기 때문에, SPA는 웹 사이트 전체에 HTML 파일이 하나인 웹 어플리케이션이다.

- MPA와 달리, SPA는 html이 하나 뿐이므로 여러 페이지(UI)를 하나의 페이지에 보여주기 위해선 <strong>Routing 기능</strong>이 필요하다.

<br/>

### Routing의 개념

- SPA에서 경로에 따라 다른 페이지를 브라우저 화면에 보여주는 것을 Routing이라 한다.

- React 자체에는 Routing 기능이 없기 때문에, 대신 React-Router라는 라이브러리를 별도로 설치해주어야 한다.

  - React-Router 설치 명령어 : <code>npm install react-router-dom</code>

<br/><br/><br/>

## Routing - By <code>BrowserRouter</code> 컴포넌트

### Routing 기능 구현하기

- <code>react-router-dom</code> v.6.4.3 버전

```js
/* index.js */
import React from "react";
import ReactDOM from "react-dom/client";
import Router from "./Router";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Router />);
```

```js
/* Router.js */
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./Login/Login";
import Main from "./Main/Main";

const Router = () => {
  return (
    <BrowserRouter>
      <Nav />
      <Routes>
        <Route path="/" element={<Login />} />
        {/* <Route path="/signup" element={<Signup />} /> */}
        <Route path="/main" element={<Main />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
};

export default Router;
```

#### 각 컴포넌트의 기능

- <code>BrowserRouter</code> : 경로 변경에 대해 여러 편의 기능을 제공

  - 예 : 페이지를 새로고침하지 않아도 주소 변경을 가능하게 하는 기능

- <code>Routes</code> : 여러 Route 컴포넌트를 감싸서, Route에 지정된 경로와 브라우저 주소창에 입력한 URL 경로가 딱 맞는 컴포넌트가 있다면 이를 브라우저에 그림.

- <code>Route</code> : 브라우저에 랜더링 할 컴포넌트와 경로를 지정하는 역할

  - Route 컴포넌트에 속성으로 path와 element를 부여

    - <code>path</code> ➡️ 브라우저에 랜더링 할 컴포넌트의 경로를 할당

    - <code>element</code> ➡️ 경로애 따라 랜더링 될 컴포넌트를 할당

<br/>

- 경로(URL)가 바뀌든 말든, 브라우저에 항상 보이는 컴포넌트를 작성하는 방법은 <code>\<Routes></code> 컴포넌트 외부에 컴포넌트를 작성해주는 것이다.

<br/><br/>

## <code>react-router-dom</code>에서 제공하는 경로 이동 방법 2가지

### 1. <code>Link</code> 컴포넌트

```js
/* Main.js */

import React from "react";
import { Link } from "react-router-dom";
import "./Main.css";

export default function Main() {
  return (
    <>
      <h1>Main</h1>
      <div>
        <h2>Log out</h2>
        <Link to="/">Login으로 이동</Link>
      </div>
    </>
  );
}
```

- 클릭 시 바로 페이지를 이동하기 때문에, 조건 없이 페이지를 이동할 때 적합하다.

- Nav Bar의 메뉴 혹은 Aside Menu 등 바로 페이지를 이동하는 경우 사용하는 것이 좋다.

<br/><br/>

### 2. <code>useNavigate</code> Hook

```js
/* Login.js */

import React from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

export default function Login() {
  const navigate = useNavigate();

  return (
    <>
      <h1>Login</h1>
      <div>
        <h2>Sign Up</h2>
        <button
          onClick={() => {
            navigate("/main");
          }}
        >
          Main으로 이동
        </button>
      </div>
    </>
  );
}
```

- 조건에 따라 페이지를 전환해야 할 때 사용하기 적합하다.

- 로그인 버튼 클릭 시에 백엔드 API로 데이터를 전송하는 작업을 한 뒤 페이지를 이동하거나 userData의 인증 혹은 인가가 필요한 경우, 혹은 로그인 작업 이후 응답 메시지에 따른 분기 처리를 해야 하는 상황일 때, useNavigate를 사용하는 것이 좋다.

<br/><br/><br/>

## Routing - By <code>createBrowserRouter</code> 컴포넌트

### Routing 기능 구현하기

- <code>react-router-dom</code> v.6.4.3 버전

```js
/* index.tsx */
import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import router from "./Router";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
```

```js
/* Root.jsx (혹은 App.jsx) */
import React from "react";
import { Outlet } from "react-router-dom";
import Header from "./screens/components/Header";

function Root() {
  return (
    <div>
      <Header />
      <Outlet />
    </div>
  );
}

export default Root;
```

```jsx
/* Router.js */
import { createBrowserRouter } from "react-router-dom";
import Home from "./screens/Home";
import About from "./screens/About";
import Root from "./Root";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root /> /* 기본적으로 Root 컴포넌트를 render 한다 */,
    children: [
      {
        path: "",
        element: <Home /> /* Root의 Outlet이 Home 컴포넌트로 대체 */,
        errorElement: (
          <ErrorComponent />
        ) /* Home 컴포넌트에서 에러 발생시 ErrorComponent를 render 한다 (여기서 다른 컴포넌트로 이동 가능) */,
      },
      {
        path: "about",
        element: <About /> /* Root의 Outlet이 About 컴포넌트로 대체 */,
      },
    ],
    errorElement: (
      <NotFound />
    ) /* URL에 맞는 컴포넌트의 위치를 찾지 못할 때 NotFound 컴포넌트를 render 한다 */,
  },
]);

export default router;
```

<br/>

#### <code>Outlet</code> 컴포넌트의 역할 : 자식 경로의 컴포넌트로 대체

```js
// Router.tsx

// .. (생략) ..

const router = createBrowserRouter([
  {
    path: "",
    element: <Root />,
    children: [
      {
        path: "",
        element: <Home />,
        errorElement: <ErrorComponent />,
      },
      {
        path: "about",
        element: <About />,
        errorElement: <ErrorComponent />,
      },
      {
        path: "users/:userId",
        element: <User />,
        errorElement: <ErrorComponent />,
        children: [
          {
            path: "followers",
            element: <Followers />,
          },
        ],
      },
    ],
    errorElement: <NotFound />,
  },
]);

export default router;
```

```js
// User.tsx
import { useParams, Outlet, Link } from "react-router-dom";
import { users } from "../../db";

function User() {
  const { userId } = useParams();

  return (
    <div>
      <div>
        <h1>User</h1>
        <h3>ID : {userId}</h3>
        <h3>Name : {users[Number(userId) - 1].name}</h3>
      </div>
      <hr />
      <Outlet />
      <Link to="followers">See Followers</Link>
    </div>
  );
}

export default User;
```
