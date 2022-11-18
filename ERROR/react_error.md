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

#### [22.11.18] 슬라이더를 리엑트로 구현하였는데, 처음에 시간 간격에 따라 페이지가 이동할 때 화면에 사진이 사라지는 문제

- <strong>원인</strong> : <code>slideLength</code> 값 ( === <code>sliderData.length</code>)에 정상적으로 값이 나오지 않고 0이 찍힌다.

  - 0이 찍힌 이유는 useState 문제인 줄 알았는데, 아니었던 것 같다. 정확한 원인을 파악하지 못한 채 문제 해결

  - 다음 부터는 문제가 발생하면 해결하기 전에 미리 문제 상황을 잘 기록해두자..

- <strong>해결</strong> : 선행되는 데이터는 상단에 미리 작성하기, useEffect의 의존성 배열에 <code>auto</code> 함수 삽입

  ```js
  const PromotionSlide = () => {
    const [currentSlide, setCurrentSlide] = useState(0);
    const [sliderData, setSliderData] = useState([]);
    const slideLength = sliderData.length;

    useEffect(() => {
      fetch("/data/sliderData.json", {
        method: "GET",
      })
        .then((res) => res.json())
        .then((data) => {
          setSliderData(data);
        });
    }, []);

    useEffect(() => {
      setCurrentSlide(0);
    }, []);

    const auto = () => {
      slideInterval = setInterval(nextSlide, intervalTime);
    };

    let slideInterval = null;
    let intervalTime = 5500;

    useEffect(() => {
      auto();
      return () => clearInterval(slideInterval);
    }, [auto, currentSlide, slideInterval]);

    const nextSlide = () => {
      setCurrentSlide((currentSlide + 1) % slideLength);
    };

    const prevSlide = () => {
      setCurrentSlide((currentSlide - 1 + 4) % slideLength);
    };

    return (...);
  };
  ```

<br/>

<!-- #### (문제) [22.00.00(날짜)]

- <strong>원인</strong> :

- <strong>해결</strong> :

<br/> -->

<!-- #### (문제) [22.00.00(날짜)]

- <a href="">블로그 포스트로 작성</a>

<br/> -->
