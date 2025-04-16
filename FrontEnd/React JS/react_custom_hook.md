# Custom Hooks란?

- React의 Custom Hooks는 여러 컴포넌트에서 **공통 로직**을 재사용할 수 있도록 만들어진 함수이다.

- 즉, 특정 기능(예: API 호출, Form 데이터 관리, 로컬 스토리지 접근 등)을 여러 컴포넌트에서 반복해서 사용할 때,

- 그 코드를 Custom Hook으로 분리하여 <strong>관심사의 분리(Separation of Concerns)</strong>를 실현할 수 있다.

<br/>

## 왜 Custom Hooks를 사용할까?

- <strong>관심사의 분리 (Separation of Concerns):</strong>  
  컴포넌트에서는 주로 UI 렌더링에 집중하고, 부수적인 로직(API 호출, 이벤트 핸들링 등)은 Custom Hook으로 분리할 수 있다.  
  이를 통해 각 컴포넌트가 담당하는 역할이 명확해지고, 코드가 더욱 깔끔해진다.

- <strong>재사용성 및 유지보수:</strong>  
  한 번 작성한 Custom Hook은 여러 컴포넌트에서 손쉽게 재사용할 수 있다.  
  또한, 공통 로직이 별도로 분리되어 있기 때문에 수정이 필요할 때도 한 곳만 업데이트하면 되어 유지보수가 편리하다.

- <strong>연결 (Concerns Integration):</strong>  
  Custom Hooks는 여러 관련 기능들을 하나의 Hook 안에 묶어 관리할 수 있다.  
  예를 들어, 데이터 페칭, 로딩 상태 관리, 에러 처리를 한 Hook으로 처리하면 기능들이 유기적으로 연결되어 관리되기 때문에, 서로를 잘 보완하는 구조를 만들 수 있다.

<br/>

## Custom Hooks 예시

- 다음은 API 호출 로직을 Custom Hook으로 분리한 예시이다.

```jsx
// useFetch.js
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // API 호출 시에 로딩 상태를 true로 설정
    setLoading(true);

    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("네트워크 응답에 문제가 있습니다");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, [url]); // url이 변경될 때마다 새로운 API 요청 발생

  return { data, loading, error };
}

export default useFetch;
```

이제 위의 Custom Hook을 컴포넌트에서 다음과 같이 사용할 수 있다.

```jsx
// ExampleComponent.js
import React from "react";
import useFetch from "./useFetch";

function ExampleComponent() {
  const { data, loading, error } = useFetch("https://api.example.com/data");

  if (loading) return <p>로딩중...</p>;
  if (error) return <p>에러 발생: {error.message}</p>;

  return (
    <div>
      <h2>데이터</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default ExampleComponent;
```

<br/>

## 정리

- **Custom Hooks**는 공통 로직을 함수형 컴포넌트에서 별도로 분리하여 재사용성을 높이는 도구아다.
- 이를 통해 <strong>관심사의 분리(Separation of Concerns)</strong>가 이루어지며, 각 컴포넌트는 UI 렌더링에 집중할 수 있다.
- 동시에 관련된 기능들을 한데 묶어 <strong>연결(Concerns Integration)</strong>하여 관리하면, 전체 코드의 가독성과 유지보수가 크게 향상된다.

<br/>
