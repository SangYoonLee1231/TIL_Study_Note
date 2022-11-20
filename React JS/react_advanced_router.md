# React JS - Dynamic Routing & Query String

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href=""></a>

<br/><br/>

##

### 정적 Routing

- Routing을 설정하는 가장 기본적인 방식은 <strong>정적 Routing</strong>이다.

  - Router 컴포넌트에서 미리 프로젝트에 사용할 경로들과, 보여줄 컴포넌트를 모두 정의해두는 방식

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

  - 하지만 복잡하고 규모가 큰 애플리케이션에서는 경로를 미리 설정하는 방식만으론 처리하기 힘들어질 수 있다. (Route를 유연하게 정의할 수 없다)

<br/><br/>

### 동적 Routing (Dynamic Routing)

- 동적 Routing은 경로를 미리 정해두지 않고 동적으로 설정하는 방식이다.

- 기존 (정적 Routing) 방식처럼 Route 설정 시 URL 전체의 형태를 미리 정의하지 않는다.

- 대신 특정 규칙을 정의한 후 규칙에 부합하는 URL이 있을 경우에 해당 element를 화면에 보여주는 방식으로 정적 Routing에서 발생하는 문제를 해결한다.
