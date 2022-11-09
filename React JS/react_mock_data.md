# React JS - 상수 데이터 & Mock Data

> 참고 자료 : 부트캠프 학습 자료

<br/>

### 목차

- <a href="">상수 데이터란?</a>
- <a href="">상수 데이터 활용하기</a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## 상수 데이터란?

- 변하지 않는 데이터

- React에서 데이터는 UI이다.

- 시간이 흐르면서 변하는 변수 데이터로 UI를 만들 땐 백엔드 서버에서 데이터를 받아와야 한다.

- 반면 변하지 않는 상수 데이터로 UI를 만들 땐 백엔드 서버에서 데이터를 받아올 필요가 없다.

<br/><br/>

## 상수 데이터 활용하기

```js
/* App.js */
import React from "react";

const MENU_LIST = [
  { id: 1, menuName: "New Repository" },
  { id: 2, menuName: "Import Repository" },
  { id: 3, menuName: "New Gist" },
  { id: 4, menuName: "New Organization" },
  { id: 5, menuName: "New Project" },
];

const App = () => {
  return (
    <div>
      <ul>
        {MENU_LIST.map((menuList) => {
          return <li key={menuList.id}>{menuList.menuName}</li>;
        })}
      </ul>
    </div>
  );
};
```

- 반복되는 UI 구조는 상수 데이터와 map 매서드를 활용해 간결히 나타낼 수 있다.

- 이렇게 할 경우, 상수 데이터를 추가되거나 삭제하려면 JSX를 건드릴 필요 없이 상수 데이터 값에만 변화를 주면 된다.

<br/>

```js
/* App.js */
import React from "react";
import { MENU_LIST } from "./uiData";

const App = () => {
  return (
    <div>
      <ul>
        {MENU_LIST.map((menuList) => {
          return <li key={menuList.id}>{menuList.menuName}</li>;
        })}
      </ul>
    </div>
  );
};
```

```js
/* uiData.js */
export const MENU_LIST = [
  { id: 1, menuName: "New Repository" },
  { id: 2, menuName: "Import Repository" },
  { id: 3, menuName: "New Gist" },
  { id: 4, menuName: "New Organization" },
  { id: 5, menuName: "New Project" },
];
```

- 상수 데이터가 만일 너무 길어 가독성을 해치는 경우 위처럼 별도의 파일로 분리해서 관리할 수도 있다.

<br/><br/>

## Mock Data란?

- 프론트엔드 개발자가 필요에 의해 백엔드 API처럼 만든 UI (흉내낸) 데이터이다.

- 그렇기 때문에, API의 구조를 확인한 후 Mock Data를 만들어야 한다.

  (API의 key-value를 확인한다. 그 후 json 파일에 Mock Data를 만든다.)

- 생성한 Mock Data는 public 폴더 하위의 data 폴더에서 관리한다.

<br/>

### Mock Data를 쓰는 이유

- 백엔드 API가 미완성인 상태에서도 차질없이 개발하기 위해서이다.

- 실제 API가 없어도 API 데이터처럼 UI 랜더링이 가능하다.

- API가 완성된 이후에 Mock Data에서 실제 API로 원활한 수정이 가능하다.

<br/>

### <code>fetch</code> 매서드

- Mock Data를 호출할 때 쓰이는 매서드이다.

  (실제 API를 호출할 때도 fetch 매서드를 쓴다.)

  ```js
  fetch("/data/파일명.json");
  ```

  - 파일의 경로는 public 폴더를 기준으로 적는다.

  - public 폴더 하위 data 폴더에 Mock Data 파일이 있기 때문에 위와 같이 경로를 적어준다.

- fetch 호출 이후에 then() 매서드를 두 번 호출한다.
