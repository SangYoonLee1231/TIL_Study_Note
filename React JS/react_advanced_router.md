# React JS - Dynamic Routing & Query String

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="">Dynamic Routing (동적 라우팅)</a>

- <a href=""><code>useParams</code> Hook</a>

<br/><br/>

## Dynamic Routing (동적 라우팅)

### 정적 Routing

- Routing을 설정하는 가장 기본적인 방식은 <strong>정적 Routing</strong>이다.

  - 정적 라우팅은 Router 컴포넌트에서 미리 프로젝트에 사용할 경로들과 보여줄 컴포넌트들을 모두 정의해두는 방식이다.

    ```js
    import React from 'react';
    import { BrowserRouter, Route, Routes } from 'react-router-dom';

    const Router = () => {
      return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/post/1" element={<PageOne />} />
            <Route path="/post/2" element={<PageTwo />} />
            <Route path="/post/3" element={<PageThree />} />
          </Routes>
        </BrowsweRouter>
      )
    }

    export default Router;
    ```

  - 하지만 복잡하고 규모가 큰 애플리케이션에서는 경로를 미리 설정하는 Routing 방식만으론 처리하기 힘든 작업이 존재할 수 있다.

    (Route를 유연하게 정의할 수 없으므로)

<br/><br/>

### 동적 라우팅 (Dynamic Routing) 이란?

- 동적 Routing은 경로를 미리 정해두지 않고 동적으로 설정하는 방식이다.

<br/>

- 동적 Routing은 기존 (정적 Routing) 방식처럼 Route 설정 시 URL 전체의 형태를 미리 정의하지 않는다.

- 대신 특정 규칙을 만들고, 그 규칙과 부합하는 URL이 있을 경우에만 해당 element를 화면에 보여주는 방식으로 정적 Routing의 문제를 해결한다.

  - 특정 규칙의 예시 : <strong><code>/post/</code>로 시작하는 모든 URL은 상세페이지로 연결된다.</strong>

<br/>

- 동적 Routing을 사용하면 <code>/post/1</code> ,<code>/post/1000</code>, <code>/post/100000</code> 등 규칙을 만족하는 모든 URL을 상세페이지로 연결시킬 수 있기 때문에 더 확장성 있는 애플리케이션을 개발할 수 있다.

- 따라서 포스트가 추가되거나 삭제되는 등 변동이 생긴다 하더라도 Router 컴포넌트를 직접 수정할 필요가 없다.

<br/>

- <code>react-router-dom</code>에서 동적 라우팅을 구현하는 방법은 Route 컴포넌트의 path prop에 <code>:</code> 기호를 활용하는 것이다.

- <code>경로/:문자열</code>형태로 path를 설정하면 URL에서 <code>경로/</code> 뒤에 무슨 글자가 오든 이 Route로 연결된다.

  ```js
  import React from "react";
  import { BrowserRouter, Route, Routes } from "react-router-dom";

  export default function Router() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ListComponent />} />
          <Route path="/post/:id" element={<DetailPageComponent />} />
        </Routes>
      </BrowserRouter>
    );
  }
  ```

- 여기서 <code>:</code> 기호 뒤에 붙는 문자열(<code>id</code>)이 path parameter이다.

- path parameter는 URL에 있는 값을 마치 매개변수(parameter)처럼 사용하는 것이다.

- path parameter를 이용하면 사용자가 같은 페이지로 접속하더라도, 큰 틀은 동일하되 다른 UI를 보여주도록 처리할 수 있다.

<br/><br/>

## <code>useParams</code> Hook

- <code>useParams</code>는 <code>react-router-dom</code>에서 제공하는 React Hook으로, path params의 값을 객체 형태로 반환해준다.

  - <strong>key</strong> : Route에서 설정한 path paramenter의 이름

  - <strong>value</strong> : Route에서 설정한 path paramenter에 실제로 전달된 값

    - <code>/post/:id</code>로 path를 설정했을 때, 유저가 <code>/post/1</code>로 접속할 경우 <code>useParams</code>가 반환하는 객체의 <strong>key</strong>는 <code>id</code>이고, <strong>value</strong>는 <code>1</code>이다.

  ```js
  // src/Router.js
  import { BrowserRouter, Routes, Route } from "react-router-dom";
  import List from "./pages/List";
  import Detail from "./pages/Detail";

  const App = () => {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<List />} />
          <Route path="/detail/:id" element={<Detail />} />
        </Routes>
      </BrowserRouter>
    );
  };

  export default App;
  ```

  ```js
  // src/Detail.js
  import React, { useState, useEffect } from "react";
  import { useParams } from "react-router-dom";

  const Detail = () => {
    const { id } = useParams();

    const [user, setUser] = useState({});

    useEffect(() => {
      fetch(`https://reqres.in/api/users/${id}`)
        .then((response) => response.json())
        .then((result) => setUser(result.data));
    }, [id]); // 4

    const { first_name, email, avatar } = user;

    return (
      <section>
        <article>
          <p>
            <strong>{first_name}</strong>
          </p>
          <p>{email}</p>
          <img alt="avatar" src={avatar} />
        </article>
      </section>
    );
  };

  export default Detail;
  ```

<br/><br/>

## Query String (쿼리 스트링)
