# React - 조각 지식 모음

<br/>

- React와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="">Mount의 의미</a>
- <a href="">React에 Font Awesome 적용하기</a>
- <a href="">경로 이동에서 <code>/</code>의 의미</a>
<!-- - <a href=""></a> -->

<br/><br/>

## Mount의 의미

- 최초로 진행되는 렌더링은 브라우저에 처음으로 특정 컴포넌트가 보여졌다는 의미로 <code>mount</code>라 표현한다.

<br/><br/>

## React에 Font Awesome 적용하기

- 우선 아래의 명령어를 입력하여 3개의 패키지를 설치한다.

  ```
  npm install @fortawesome/react-fontawesome
  npm install @fortawesome/free-solid-svg-icons
  npm install @fortawesome/fontawesome-svg-core
  ```

<br/>

- 아래의 예시를 참고하여 React 프로젝트 파일에 Font Awesome 아이콘을 삽입한다.

  ```js
  import React, { useEffect, useState } from "react";
  import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
  import { faMinusCircle, faPlusCircle } from "@fortawesome/free-solid-svg-icons";

  const BuyBar = ({ productData }) => {

  ...

    return (
      <>
      <div className="product-select-quantity">
          <FontAwesomeIcon icon={faMinusCircle} />
          <FontAwesomeIcon icon={faPlusCircle} />
      </div>
      </>
    );
  };
  ```

<br/><br/>

## 경로 이동에서 <code>/</code>의 의미

- 경로 이동에서 <code>/</code>은 절대 경로로 이동하라는 의미이다.

  - <code>localhost:3000/users</code> 경로에서 <code>\<Link to="/followers">See Followers\</Link></code> 클릭 시 ->  
    <code>localhost:3000/followers</code> 경로로 이동

- 반면 <code>/</code>을 붙이지 않으면 상대 경로로 이동하라는 의미이다.

  - <code>localhost:3000/users</code> 경로에서 <code>\<Link to="followers">See Followers\</Link></code> 클릭 시 ->  
    <code>localhost:3000/users/followers</code> 경로로 이동
