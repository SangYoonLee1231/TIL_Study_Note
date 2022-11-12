# React JS - 상수 데이터 & Mock Data

> 참고 자료 : 부트캠프 학습 자료

<br/>

### 목차

- <a href="">상수 데이터란?</a>

- <a href="">상수 데이터 활용하기</a>
- <a href="">Mock Data란?</a>
- <a href=""><code>fetch</code> 매서드</a>

<br/><br/>

## 상수 데이터란?

- 변하지 않는 데이터

- React에서 데이터는 UI이다.

<br/>

- 시간이 흐름에 따라 변하는 변수 데이터로 UI를 만들 땐 백엔드 서버에서 데이터를 받아와야 한다.

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

- 이렇게 할 경우, 상수 데이터를 추가하거나 삭제하려면 JSX를 건드릴 필요 없이 상수 데이터 값만 바꾸면 된다.

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

- 그렇기 때문에, Mock Data를 만들 땐 백엔드 API의 구조를 우선적으로 확인해야 한다.

  (API의 key-value를 확인한다. 그 후 <code>json</code> 확장자 명으로 Mock Data를 만든다.)

- 생성한 Mock Data는 <code>public</code> 폴더 하위의 <code>data</code> 폴더에서 관리한다.

<br/>

### Mock Data를 쓰는 이유

- 백엔드 API가 미완성인 상태에서도 차질없이 개발을 진행하기 위해서이다.

- Mock Data를 쓰면 실제 API가 없더라도 API 데이터처럼 UI 랜더링이 가능해진다.

- API가 완성된 이후에 Mock Data에서 실제 API로 원활한 수정이 가능하다.

<br/><br/>

## <code>fetch</code> 매서드

- Mock Data를 만들고 난 후 이를 <strong>호출</strong>할 때 쓰이는 매서드이다.

  (실제 API를 호출할 때도 <code>fetch</code> 매서드를 쓴다.)

  ```js
  fetch("/data/파일명.json");
  ```

  - 파일의 경로는 <code>public</code> 폴더를 기준으로 적는다.

  - <code>public</code> 폴더 하위 <code>data</code> 폴더에 Mock Data 파일이 있기 때문에 위와 같이 경로를 적어준다.

<br/>

### Step 1. Mock Data 받아 state에 저장하기

- <code>fetch</code> 호출 이후에 <code>then()</code> 매서드를 두 번 호출한다.

  ```js
  fetch("/data/파일명.json")
    .then(response -> response.json())
    .then(result => setState(result));
  ```

  - 첫 번째 <code>.then</code> 매서드에 인자로 callBack을 전달하고 <strong>JSON 형태</strong>의 데이터가 들어온다. 이 데이터를 <strong>자바스크립트 형태로 변환</strong>하고 반환한다.

  - 두 번째 <code>.then</code>에서는 인자로 callBack을 전달하고, 매개변수에서는 첫 번째 <code>.then</code>에서 반환된 객체를 result로 받아 <code>setState</code> 함수로 <strong>result를 state에 저장</strong>한다.

- 이렇게 하면 state에 Mock Data를 저장하고, 언제든 꺼내 쓸 수 있게 되었다.

- 하지만 아직 이를 호출하는 작업은 하지 않았는데, 이는 상황에 맞춰 진행하면 된다.

<br/>

### Step 2. 받아온 Mock Data 호출하기

- <strong>데이터를 호출하는 시점은 상황에 따라 각기 다르다.</strong>

  - 버튼을 클릭했을 때 UI가 그려져야 하는 경우도 있고, 페이지를 불러올 때 바로 화면에 UI를 그려줘야 하는 경우도 있다.

  - 이 때 전자는 <code>이벤트 함수</code> 내에서, 후자는 <code>useEffect</code> 안에서 fetch 매서드를 호출하면 된다.
