# Express 프레임워크를 이용한 웹 서버 구축해보기

<br/><br/>

<!-- ### 목차 -->

<!-- - <a href=""></a> -->
<!-- - <a href=""></a> -->

<!-- <br/><br/> -->

## Express 설치

- **Express** : 웹 서버 구축에 사용되는 대포적인 프레임워크이다.

<br/>

- node.js 프로젝트 시작하기

  ```cmd
  npm init
  ```

- Express 설치

  ```
  npm install --save express
  ```

- app.js 파일 만들기

- 콜백 함수 생성

  ```js
  // server/app.js

  const express = require("express");
  const app = express();

  app.get("/", function (req, res) {
    res.send("Hello World");
  });

  app.listen(3000, () => {
    console.log("server start!");
  });
  ```

<br/><br/>

## 샘플 코드

```js
// 일기장 만들기

const express = require("express");
const app = express();
const cors = require("cors"); // CORS 에러 방지용 코드

app.use(cors()); // CORS 에러 방지용 코드

// 프론트에서 API 호출 시 body에 입력한 값을 확인하기 위해 필요한 body-parser
app.use(express.json()); // for parsing application/json
app.use(express.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

let id = 2;
const diaryList = [
  {
    id: 1,
    title: "오늘은 리엑트 세션",
    content: "CS는 왜 이렇게 노잼일까",
  },
];

app.get("/", function (req, res) {
  res.send("Hello World");
});

app.get("/api/diary", function (req, res) {
  res.json(diaryList);
});

app.post("/api/diary", (req, res) => {
  const { title, content } = req.body;
  diaryList.push({
    id: id++,
    title,
    content,
  });
  return res.send("success");
});

// 서버 포트 설정
app.listen(4000, () => {
  console.log("server start!");
});
```

<br/>

### 코드 뜯어보기

```js
app.get("/", function (req, res) {
  res.send("Hello World");
});
```

- `app.get("/", function(req, res) {...})`는 HTTP GET 요청이 "/" 경로로 전송될 때 실행될 함수를 정의한다.

- 이 함수의 매개변수 *req*와 *res*는 각각 요청(request)과 응답(response)을 나타냅니다.

  - <strong>req (요청 객체 - Request Object)</strong>: 클라이언트로부터 서버로 전송된 HTTP 요청에 대한 정보를 포함하는 객체이다. 이 객체는 요청 헤더, 요청 본문, URL 매개변수, 쿼리 매개변수 등과 같은 다양한 정보에 접근할 수 있는 메서드 및 속성을 제공한다.

  - <strong>res (응답 객체 - Response Object)</strong>: 서버에서 클라이언트로 전송할 HTTP 응답을 나타내는 객체이다. 이 객체를 사용하여 응답 상태 코드, 응답 헤더, 응답 본문 등을 설정하고 클라이언트에게 응답을 보낸다.

- 여기서 `res.send("Hello World");`는 간단한 텍스트 응답을 보내는 메소드이다. 클라이언트가 서버에 HTTP GET 요청을 보내면, 서버는 "Hello World"라는 텍스트를 응답으로 보내게 된다.

<br/>
