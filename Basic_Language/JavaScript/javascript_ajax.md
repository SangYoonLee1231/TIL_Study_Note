# JavaScript - Ajax, JSON, HTTP 통신

> 참고 자료 : 책 '모단 자바스크립트 Deep Dive'

<!-- <br/> -->

### 목차

- <a href="">Ajax</a>
- <a href="">JSON</a>
- <a href="">XMLHttpRequest</a>
<!-- - <a href=""></a> -->

<br/><br/>

## Ajax

- 자바스크립트를 통해 웹 클라이언트와 서버가 서로 데이터를 주고받으며 웹페이지를 동적으로 갱신하는 프로그래밍 방식이다.

- Ajax는 브라우저 제공 Web API인 `XMLHttpRequest` 객체를 기반으로 동작한다.

- `XMLHttpRequest`는 HTTP 비동기 통신을 위한 메서드와 프로퍼티를 제공한다.

<br/>

### 전통적인 데이터 통신 방식

- 이전의 웹페이지는 통신 시 완전한 html(html 태그 사이 코드)을 서버로부터 전송받아 **웹페이지 전체를 처음부터 다시 렌더링하는 방식**으로 동작했다.

- 따라서 화면이 전환될 경우 서버로부터 새로운 HTML을 전송받아 웹페이지 전체를 처음부터 다시 렌더링했다.

- 이와 같은 방식은 불필요한 데이터 통신을 발생시키고, 화면 전환 시 순간 깜박임 현상을 일으키며, 동기 방식으로 동작하기에 서버에 응답이 없으면 다음 처리가 계속 블로킹 된다는 단점이 존재한다.

<br/>

### Ajax 등장 이후의 데이터 통신 방식

- Ajax로 인해 이제 웹페이지에서 **변경이 필요한 데이터만 비동기 방식으로 전송**을 받아, 변경이 필요 없는 부분은 가만히 놔두고, **변경이 필요한 부분만 랜더링하는 방식**이 가능해졌다.

- 이를 통해 불필요한 데이터 통신을 막을 수 있게 되었고, 데스크톱 앱과 유사한 빠른 퍼포먼스와 부드러운 화면 전환이 가능해졌다.

- 또 비동기 방식으로 동작하기에 서버 요청 이후 블로킹 또한 발생하지 않는다.

<br/><br/>

## JSON

- 자바스크립트에 종속되지 않는 언어 독립형 텍스트 데이터 포멧이다.

- 클라이언트와 서버 간의 HTTP 통신에서 사용한다.

<br/>

### JSON 표기 방식

- JSON은 키와 값으로 구성되어 있다.

  ```json
  {
    "name": "Lee Sang Yoon",
    "age": 26,
    "grade": 4,
    "hobby": ["room escape", "travel", "watching webtoons"]
  }
  ```

- JSON의 키는 반드시 큰따옴표로 묶어야 한다.

- JSON의 값은 객체 리터럴돠 같은 표기법을 그대로 사용한다. (문자열은 반드시 큰따옴표로 묶어야 한다.)

- <주의> 큰따옴표 대신 작은따옴표는 사용할 수 없다.

<br/>

### JSON.stringify와 JSON.parse

- JSON.stringify는 JSON을 문자열로 변환한다.

- 클라이언트에서 서버로 객체를 전송하려면 객체를 문자열화 해야한다. 이를 직렬화(Serializing)라 한다.

  ```js
  const obj = {
    name: "Lee Sang Yoon",
    age: 26,
    grade: 4,
    hobby: ["room escape", "travel", "watching webtoons"],
  };

  const json = JSON.stringify(obj);

  console.log(typeof json);
  // string

  console.log(json);
  // {"name": "Lee Sang Yoon","age": 26,"grade": 4,"hobby": ["room escape", "travel", "watching webtoons"]}
  ```

<br/>

- JSON.parse는 반대로 JSON 포멧의 문자열을 객체로 변환한다.

- 서버에서 클라이언트로 전송된 JSON 문자열 데이터를 객체로 변환해주어야 사용할 수 있다. 이 과정을 역정렬화(Deserializing)라 한다.

  ```js
  const obj = {
    name: "Lee Sang Yoon",
    age: 26,
    grade: 4,
    hobby: ["room escape", "travel", "watching webtoons"],
  };

  const json = JSON.stringify(obj);
  const parsed = JSON.parse(json);

  console.log(typeof parsed);
  // object

  console.log(parsed);
  // {"name": "Lee Sang Yoon","age": 26,"grade": 4,"hobby": ["room escape", "travel", "watching webtoons"]}
  ```

<br/><br/>

## XMLHttpRequest

- 자바스크립트를 통해 HTTP 요청을 전송하려면 `XMLHttpRequest` 객체를 사용한다.

- Web API인 `XMLHttpRequest` 객체는 HTTP 요청 전송과 HTTP 응답 수신을 위한 다양한 메서드와 프로퍼티를 제공한다.

<br/>

### HTTP 요청 전송

#### 순서

1. `XMLHttpRequest` 객체 생성 - By `XMLHttpRequest` 생성자 함수

2. HTTP 요청 초기화 - By `XMLHttpRequest.prototype.open` 메서드

3. 특정 HTTP 요청의 헤더 값 설정 - By `XMLHttpRequest.prototype.setRequestHeader` 메서드

4. HTTP 요청 전송 - By `XMLHttpRequest.prototype.send` 메서드

```js
// `XMLHttpRequest` 객체 생성
const xhr = new XMLHttpRequest();

// HTTP 요청 초기화
xhr.open("GET", "/users");

// 특정 HTTP 요청의 헤더 값 설정
xhr.setRequestHeader("content-type", "application/json");

// HTTP 요청 전송
xhr.send();
```

<br/>

#### `XMLHttpRequest.prototype.open` 메서드

- open 메서드는 서버에 전송할 HTTP 요청을 초기화한다.

```js
xhr.open(method, url[, async]);
```

- `method`: HTTP 요청 메서드 ("GET", "POST", "PUT", "DELETE" 등)

- `url`: HTTP 요청을 전송할 URL

- `async`: 옵션값, 비동기 요청 여부, 기본값 = true, 비동기 방식으로 동작

<br/>

#### HTTP 요청 메서드

- **GET**: 모든/특정 리소스 취득 (index/retrieve)

- **POST**: 리소스 생성 (create)

- **PUT**: 리소스 전체 교체 (replace)

- **PATCH**: 리소스의 일부 수정 (modify)

- **DELETE**: 모든/특정 리소스 삭제 (delete)

<br/>

#### `XMLHttpRequest.prototype.send` 메서드

- send 메서드는 **open 메서드로 초기화된 HTTP 요청을 서버에 전송한다.**

- GET, POST 요청 매서드에 따라 서버로 전송하는 데이터의 전송 방식에 차이가 있다.

  - **GET 요청 메서드**: 데이터를 URL의 일부인 쿼리 문자열(Query String)로 서버에 전송한다.

  - **POST 요청 메서드**: 데이터(페이로드)를 요청 몸체(request body)에 담아 전송한다.

- send 메서드에는 요청 몸체에 담아 전송할 데이터(페이로드)를 인수로 전달할 수 있다.

- 이때 페이로드가 객체인 경우 반드시 `JSON.stringify` 메서드를 통해 직렬화 헌 다음 전달해야 한다.

  ```js
  const obj = {
    name: "Lee Sang Yoon",
    age: 26,
    grade: 4,
    hobby: ["room escape", "travel", "watching webtoons"],
  };

  const json = JSON.stringify(obj);

  xhr.send(json);
  ```

- HTTP 요청 메서드가 GET인 경우 send 메서드에 페이로드로 전달한 인수는 무시되고 요청 몸체는 null로 설정된다.

<br/>

#### `XMLHttpRequest.prototype.setRequestHeader` 메서드

- setRequestHeader 메서드는 **특정 HTTP 요청의 헤더 값을 설정한다.**

- 반드시 open 메서드 호출 이후에 호출해야 한다.

- **HTTP 요청 헤더**

  - `Content-type`: Request Body에 담아 전송할 데이터의 MIME 타입 정보를 표현한다. MIME 타입은 서버로부터 받은 데이터가 어떤 종류의 데이터인지를 나타낸다.

    ```js
    xhr.setRequestHeader("content-type", "application/json");
    ```

  - `Accept`: 클라이언트가 서버에게 어떤 미디어 타입이나 데이터 형식을 받을 수 있는지를 나타낸다.

    ```js
    xhr.setRequestHeader("accept", "application/json");
    ```

    - 만약 Accept 헤더를 설정하지 않으면, send 메서드가 호출될 때 Accept 헤더가 */*로 전송된다.

- **MIME (Multipurpose Internet Mail Extensions) 타입**

  - `text`: text/plain, text/html, text/css, text/javascript

  - `application`: application/json, application/x-www-form-urlencode

  - `multipart`: multipart/formed-data

<br/>
