# ERROR NOTE - React

#### [22.11.04] DOM에 직접 접근하여 classList 메소드를 통해 클래스를 추가하고 제거했더니 정상적으로 동작하지 않는다.

- <a href="https://sylagape1231.tistory.com/59">블로그 포스트로 작성</a>

<br/><br/>

#### [22.11.04] React에서 특정 요소에 이벤트를 연결하고, event 객체를 매개변수로 받아 활용하는 코드를 작성했는데, <code>event is deprecated</code> 에러가 발생했다.

- <a href="https://sylagape1231.tistory.com/60">블로그 포스트로 작성</a>

<br/><br/>

#### [22.11.15] (Router를 활용한) React 프로젝트를 초기 세팅 완료하고 실행(npm start)해보았는데, 화면에 아무것도 나타나지 않는다.

- <strong>원인</strong> : (모르겠음)

- <strong>해결</strong> : Router 컴포넌트의 코드를 파일 내에서 다시 작성해본다.

<br/><br/>

#### [22.11.15] 아래와 같이 코드를 작성했는데 화면에 아무것도 출력되지 않는다. (상위 컴포넌트는 생략)

```js
// MenuList.js
const MENU_LIST_DATAS = [
  "눈",
  "간",
  "관절 / 뼈",
  "장",
  "다이어트",
  "위 /소화",
  "피부",
  "피로 / 활력",
];

const MenuList = () => {
  return (
    <>
      ...
      <div className="">
        {MENU_LIST_DATAS.forEach((data) => (
          <ListItem name={data} />
        ))}
      </div>
    </>
  );
};

export default MenuList;
```

```js
// Listitem.js
import React from "react";

const ListItem = ({ name }) => {
  return <p>{name}</p>;
};

export default ListItem;
```

- <strong>원인</strong> : 자바스크립트에서 <code>map</code> 메소드는 배열을 반환하지만, React의 JSX에서 <code>map</code> 메소드는 컴포넌트를 반환하는 함수가 인자로 들어가 있으면, 컴포넌트를 여러 개 반환한다.

- <strong>해결</strong> : 상수 데이터 배열에 <code>forEach</code> 메소드가 아닌 <code>map</code> 메소드를 사용해주면 된다.

  ```js
  // MenuList.js
  const MENU_LIST_DATAS = [
    ...
  ];

  const MenuList = () => {
    return (
      <>
        ...
        <div className="">
          {MENU_LIST_DATAS.map((data) => (
            <ListItem name={data} />
          ))}
        </div>
      </>
    );
  };

  export default MenuList;
  ```

<br/>

<!-- #### (문제) [22.00.00(날짜)]

- <strong>원인</strong> :

- <strong>해결</strong> :

<br/> -->

<!-- #### (문제) [22.00.00(날짜)]

- <a href="">블로그 포스트로 작성</a>

<br/> -->
