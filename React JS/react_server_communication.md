# React JS - 프론트엔드 서버 통신

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_server_communication.md#%EC%84%9C%EB%B2%84-%ED%86%B5%EC%8B%A0-3%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95">서버 통신 3가지 방법 (ajax, fetch, axios)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_server_communication.md#%EB%8D%B0%EC%9D%B4%ED%84%B0-get-%EC%9A%94%EC%B2%AD---fetch">데이터 GET 요청 - Fetch</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_server_communication.md#%EB%8D%B0%EC%9D%B4%ED%84%B0-post-%EC%9A%94%EC%B2%AD---fetch">데이터 POST 요청 - Fetch</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_server_communication.md#axios%EB%A1%9C-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0">axios로 변경하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_server_communication.md#msw">MSW</a>
<!-- - <a href=""></a> -->

<br/><br/><br/>

## 서버 통신 3가지 방법

- **서버 주소**와 **HTTP 메소드** 이 두 가지 만으로 데이터를 요청할 수 있다.

<br/>

### 1. ajax

- **Asynchronous JavaScript And XML**의 약자로,
  자바스크립트를 이용해 클라이언트와 서버 간에 데이터를 주고받는 비동기 HTTP 통신이다.

- 가장 오래된 형태의 비동기 통신 방법 중 하나이다.

<br/>

- 장점
  - Jquery를 통해 쉽게 구현 가능
  - Error, Success, Complete의 상태를 통해 실행 흐름 조절 가능
- 단점
  - Jquery를 사용해야 간편하고 호환성이 보장됨
  - Promise 기반이 아님
- 예시

  ```jsx
  const serverAddress = "https://localhost:3000";

  // jQuery의 .get 메소드 사용
  $.ajax({
    url: serverAddress,
    type: "GET",
    success: function onData(data) {
      console.log(data);
    },
    error: function onError(error) {
      console.error(error);
    },
  });
  ```

<br/><br/>

### 2. fetch

- ES6부터 들어온 JavaScript 내장 라이브러리

- Promise를 기반으로 한 비동기적인 특성을 지니고 있음

  → 간단한 API 구조를 가지고 있어, 간단한 HTTP 요청을 만들 때 유용하다.

<br/>

- 장점
  - 자바스크립트의 내장 라이브러리이므로 별도로 import 할 필요가 없음
  - Promise 기반으로 만들어졌기 때문에 데이터 다루기 편리
  - 내장 라이브러리이기 때문에 업데이트에 따른 에러 방지가 가능
- 단점
  - 지원하지 않는 브라우저가 존재 (IE11...)
  - 네트워크 에러 발생 시 response timeout이 없어 기다려야 함
  - JSON으로 변환해주는 과정 필요
  - 상대적으로 axios에 비해 기능이 부족
- 사용 예시

  ```jsx
  fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data))
    **.catch(error => console.error("Error:", error));**
  ```

<br/><br/>

### 3. axios

- Node.js와 브라우저를 위한 Promise API를 활용하는 비동기 HTTP 통신 라이브러리

- 외부 라이브러리로, 모든 브라우저에서 사용 가능하다.

<br/>

- 장점
  - response timeout(fetch에는 없는 기능) 처리 방법이 존재
  - Promise 기반으로 만들어졌기 때문에 데이터 다루기 편리
  - 브라우저 호환성이 뛰어남
  - JSON 외에도 다양한 형식의 데이터 취급 가능
- 단점
  - 사용을 위해 모듈 설치 필요
- 사용 예시

  ```jsx
  import axios from "axios";

  axios
    .get("https://api.example.com/data")
    .then((response) => console.log(response.data))
    .catch((error) => console.error("Error:", error));
  ```

<br/><br/>

### 서로 비교해보자

- 브라우저 지원

  - `fetch`는 최신 브라우저에서 네이티브로 지원 / `axios`와 `ajax`는 모든 주요 브라우저에서 지원

- API 편의성

  - `axios`는 기능적으로 우수 / `fetch`는 비교적 간단한 API

- Promise 지원

  - `fetch`와 `axios`는 Promise 기반 / `ajax`는 jQuery와 함께 사용될 때 콜백 기반의 구조 지님

- CSRF 등의 기능

  - `axios`는 요청 및 응답 인터셉터를 통해 CSRF 보호와 같은 고급 기능을 지원
  - `fetch`도 유사한 기능을 사용할 수 있지만, 구현이 더 복잡할 수 있다.
  - `ajax`는 이러한 기능을 직접 제공하지 않지만, jQuery와 함께 사용할 때 편리한 인터페이스를 제공

<br/><br/><br/>

## 데이터 GET 요청 - Fetch

### 1. `fetch` 사용하여 데이터 받아오기

```jsx
function App() {
  fetch("http://localhost:4000/api/diary")
    .then((res) => res.json())
    .then((data) => console.log(data));
  return <>// ...</>;
}

export default App;
```

- …! 에러가 발생한다!

<br/><br/>

### 2. CORS 에러

- `Cross Origin Resource Sharing` 의 약자로, 보안 상의 이유로 브라우저에서 실행되는 웹 페이지가 다른 도메인의 리소스에 접근할 때 발생하는 보안 정책

<aside>

💡 **예시**

- 클라이언트의 접근
  http://localhost:3000/
- 서버의 접근
  http://localhost:4000/

**→ Origin이 다른 곳(3000포트와 4000포트)으로 데이터 접근이 이루어지고 있다!**

</aside>

<br/><br/>

### 3. CORS 에러 해결

**CORS 에러의 해결은 서버에서!**

1. cors 라이브러리 설치하기(server 디렉토리)

   ```jsx
   npm install cors
   ```

2. 이제 server/app.js에 middleware를 추가

   ```jsx
   const cors = require("cors");

   app.use(cors());
   ```

   다시 node app.js로 서버 폴더에서 서버를 실행시켜주고, 4000포트 주소로 들어가보면 에러가 해결된 것을 확인할 수 있다.

3. 에러 해결 확인하기

   `node app.js` → 서버 실행 → http://localhost:4000/

   `npm start` → 클라이언트 실행 → http://localhost:3000/

<br/><br/>

### 4. 데이터 저장하여 화면에 띄우기

```jsx
import { useState } from "react";

function App() {
  const [diaryList, setDiaryList] = useState(null);
  fetch("http://localhost:4000/api/diary")
    .then((res) => res.json())
    .then((data) => setDiaryList(data));
  return (
    <>
      <p>일기를 써봅시다!</p>
    </>
  );
}

export default App;
```

- 에러가… 난다.

<br/><br/>

### 5. 무한 리렌더링 에러

<aside>

💡 **리액트의 무한 리렌더링**

- 컴포넌트가 계속해서 다시 렌더링되는 현상.

- 일반적으로 컴포넌트의 상태(State)나 속성(Props)이 변경될 때 발생한다.

- 리액트는 상태값이 업데이트 될 때마다 컴포넌트의 리렌더링이 일어난다.

</aside>

```jsx
import { useState } from "react";

function App() {
  1️⃣ const [diaryList, setDiaryList] = useState(null)
  2️⃣ fetch("http://localhost:4000/api/diary")
    .then((res) => res.json())
    .then((data) => setDiaryList(data));
  3️⃣ return (
    <>
      <p>일기를 써봅시다!</p>
    </>
  );
}

export default App;
```

- 1️⃣ 2️⃣ 3️⃣ 순서대로 실행

- `setDiaryList(data)` → 문제의 코드

  : 상태변화함수이므로 리액트 컴포넌트 상태를 변경시킨다. 즉, 페이지가 재실행된다. 해당 과정이 무한으로 반복하여 오류가 발생한다.

<br/><br/>

### 6. 리랜더링 무한반복 해결하기

<aside>

💡 **`useEffect`**

- React가 DOM을 랜더링한 이후 추가로 코드를 실행해야 하는 경우 사용한다.

- 첫 번째 랜더링과 dependancy 리스트 안에 있는 요소의 값이 변할 때마다 수행된다.

</aside>

```jsx
useEffect(() => {
  fetch("http://localhost:4000/api/diary")
    .then((res) => res.json())
    .then((data) => setDiaryList(data));
}, []);
```

→ 의존성 리스트 비워두기

<br/><br/>

### 7. 화면 구성하기

```jsx
return (
    <>
      <Container>
        <Title>일기를 써봅시다!</Title>
        {diaryList && (
          <DiaryList>
            {diaryList.map((diary) => (
              <DiaryItem key={diary.id}>
								<div>
                  <DiaryTitle>{diary.title}</DiaryTitle>
                  <DiaryContent>{diary.content}</DiaryContent>
                </div>
              </DiaryItem>
            ))}
          </DiaryList>
        )}
      </Container>
    </>
  );
}

export default App;

const Container = styled.div`
  display: flex;
  width: 100vw;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 30px;
`;

const Title = styled.p`
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
`;

const DiaryList = styled.ul`
  list-style: none;
  padding: 0;
  width: 60%;
`;

const DiaryItem = styled.li`
  border-bottom: 1px solid #eee;
  padding: 20px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const DiaryTitle = styled.h3`
  font-size: 18px;
  margin-bottom: 10px;
`;

const DiaryContent = styled.p`
  font-size: 16px;
  color: #555;
`;
```

<br/><br/><br/>

## 데이터 POST 요청 - Fetch

1. UI 작성

   ```jsx
   <form onSubmit={onSubmitHandler}>
     <input name="title" />
     <input name="content" />
     <input type="submit" value="추가" />
   </form>
   ```

   form 태그로 감싸주기!

<br/>

2. 제출 시 실행될 함수 생성

   ```jsx
   const onSubmitHandler = (e) => {
     e.preventDefault();
     const title = e.target.text.value;
     const content = e.target.text.value;
     fetch("http//localhost:4000/api/diary", {
       method: "POST",
       body: JSON.stringify({
         title,
         content,
       }),
     });
   };
   ```

   - `fetch`

   - `POST` : 클라이언트가 서버로 데이터를 전송하기 위해 사용되는 요청 메서드

   - `JSON.stringfy` : JavaScript 객체나 값의 직렬화(serialize)를 수행하는 메서드

   - `e.preventDefault()` submit의 기본 동작(POST 후 GET)을 막기 위해 작성

<br/>

3. `Content-Type` 설정

   ```jsx
   const onSubmitHandler = (e) => {
     e.preventDefault();
     const title = e.target.title.value;
     const content = e.target.content.value;
     fetch("http://localhost:4000/api/diary", {
       method: "POST",
       headers: {
         "Content-Type": "application/json",
       },
       body: JSON.stringify({
         title,
         content,
       }),
     });
   };
   ```

   - 내가 보내는 데이터의 타입을 명시하는 것!

<br/>

4. 데이터 실시간 반영하기

   - 데이터를 `GET` 하는 코드만 적절히 배치해도 데이터를 실시간 반영할 수 있다!
     → 자주 사용하게 될 코드는 함수로 만들 것! (`fetchDiary`)
   - 제출 이후 한 번 더 데이터를 받아온다!

     ```jsx
     useEffect(() => {
       fetchDiary();
     }, []);

     const fetchDiary = () => {
       fetch("http://localhost:4000/api/diary")
         .then((res) => res.json())
         .then((data) => setDiaryList(data));
     };

     const onSubmitHandler = (e) => {
       e.preventDefault();
       const title = e.target.title.value;
       const content = e.target.content.value;
       fetch("http://localhost:4000/api/diary", {
         method: "POST",
         headers: {
           "Content-Type": "application/json",
         },
         body: JSON.stringify({
           title,
           content,
         }),
       }).then(() => fetchDiary());
     };
     ```

<br/>

5. 꾸미기

   ```jsx

   return (
       <>
         <Container>
           <Title>일기를 써봅시다!</Title>
           <Form onSubmit={onSubmitHandler}>
             <Input name="title" placeholder="제목" />
             <TextArea name="content" placeholder="내용" />
             <SubmitButton type="submit">추가</SubmitButton>
           </Form>
           {diaryList && (
             <DiaryList>
               {diaryList.map((diary) => (
                 <DiaryItem key={diary.id}>
                   <div>
                     <DiaryTitle>{diary.title}</DiaryTitle>
                     <DiaryContent>{diary.content}</DiaryContent>
                   </div>
                 </DiaryItem>
               ))}
             </DiaryList>
           )}
         </Container>
       </>
     );
   }

   export default App;

   const Container = styled.div`
     display: flex;
     width: 100vw;
     justify-content: center;
     align-items: center;
     flex-direction: column;
     margin-top: 30px;
   `;

   const Title = styled.p`
     font-size: 24px;
     font-weight: bold;
     margin-bottom: 20px;
   `;

   const Form = styled.form`
     width: 60%;
     display: flex;
     justify-content: center;
     align-items: center;
     flex-direction: column;
     margin-bottom: 20px;
   `;

   const Input = styled.input`
     width: 100%;
     padding: 10px;
     margin-bottom: 10px;
     font-size: 16px;
   `;

   const TextArea = styled.textarea`
     width: 100%;
     padding: 10px;
     margin-bottom: 10px;
     font-size: 16px;
   `;

   const SubmitButton = styled.button`
     padding: 10px;
     width: 50%;
     background-color: #4caf50;
     color: white;
     border: none;
     cursor: pointer;

     &:hover {
       background-color: #45a049;
     }
   `;

   const DiaryList = styled.ul`
     list-style: none;
     width: 60%;
     box-shadow: 0 0 4px rgba(0, 0, 0, 0.25);
   `;

   const DiaryItem = styled.li`
     border-bottom: 1px solid #eee;
     padding: 20px 0;
     display: flex;
     justify-content: space-between;
     align-items: center;
   `;

   const DiaryTitle = styled.h3`
     font-size: 18px;
     margin-bottom: 10px;
   `;

   const DiaryContent = styled.p`
     font-size: 16px;
     color: #555;
   `;
   ```

<br/><br/><br/>

## axios로 변경하기

1. axios 설치

   > client/diary 디렉토리에서 실행한다.

   ```jsx
   npm install axios
   ```

<br/>

2. 불러오기

   ```jsx
   // client/App.js

   import axios from "axios";
   ```

<br/>

3. `GET` 메서드

   ```jsx
   const fetchDiary = async () => {
     const res = await axios.get("http://localhost:4000/api/diary");
     setDiaryList(res.data);
   };
   ```

   → 변수에 담아서 사용할 수 있다!

<br/>

4. `POST` 메서드

   ```jsx
   const onSubmitHandler = (e) => {
     e.preventDefault();
     const title = e.target.title.value;
     const content = e.target.content.value;
     axios.post("http://localhost:4000/api/diary", { title, content });
     fetchDiary();
   };
   ```

   - header의 Content-Type 생략 가능!

   - body 직렬화 코드 생략 가능!

   - `axios.post`의 형식

   - `fetchDiary()`

<br/><br/><br/>

## MSW

<aside>
💡 <strong>MSW (Mock Service Worker)</strong>

- 서비스 워커(Service Worker)를 사용하여 **네트워크 호출을 가로채는 API 모킹** 라이브러리
  즉, API인 척! 프론트엔드의 요청에 가짜 데이터를 응답해준다.

</aside>

1. 사용하는 경우

   - 백엔드 API 개발과 프론트엔드 UI 개발이 동시에 진행되야하는 경우, 백엔드 API 구현이 완료될 때까지 프론트엔드 팀에서 임시로 사용하기 위한 가짜(mock) API를 서비스 워커로 돌리기 위해서.

   - 테스트를 실행 시 실제 백엔드 API에 네트워크 호출을 하는 대신에 훨씬 빠르고 안정적인 가짜 API 서버를 구축하기 위해서

<br/>

2. 장점

   - 네트워크 단에서 일어나기 때문에 프론트엔드 코드를 실제 백엔드 API와 네트워크 통신하는 것과 크게 다르지 않게 작성할 수 있다

   - REST API 모킹과 GraphQL API 모킹을 모두 지원한다

<br/>

3. 단점

   - 일부 브라우저에서 지원하지 않는다.

<br/>
