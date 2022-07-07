# JavaScript - 로컬 스토리지 (Local Storage)

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_local_storage.md#%EB%A1%9C%EC%BB%AC-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-local-storage">로컬 스토리지 (Local Storage)</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_local_storage.md#local-storage%EC%9D%98-%ED%95%A8%EC%88%98">Local Storage의 함수</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_local_storage.md#%EB%A1%9C%EC%BB%AC-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-local-storage-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0">로컬 스토리지 (Local Storage) 활용하기</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_local_storage.md#local-storage%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%ED%95%AD%EB%AA%A9%EC%9D%98-%EC%A1%B4%EC%9E%AC-%EC%9C%A0%EB%AC%B4%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8B%A4%EB%A5%B8-%EB%8F%99%EC%9E%91%EC%9D%84-%EC%88%98%ED%96%89%ED%95%98%EB%8F%84%EB%A1%9D-%ED%95%98%EA%B8%B0">Local Storage에서 특정 항목의 존재 유무에 따라 다른 동작을 수행하도록 하기</a>

<br/><br/>

## 로컬 스토리지 (Local Storage)

- 브라우저가 value를 저장하도록 해주는 API

- 작은 미니 DB 같다.

<br/>

### Local Storage의 함수

- <code>setItem</code> : Local Storage에 항목 추가하기

  ```javascript
  localStorage.setItem("Key", "Value");
  ```

- <code>getItem</code> : Local Storage에서 항목 불러오기

  ```javascript
  localStorage.getItem("Key");
  ```

  ```
  "Value"
  ```

- <code>removeItem</code> : Local Storage에 있는 항목 제거하기

  ```javascript
  localStorage.removeItem("Key");
  ```

<br/>

## 로컬 스토리지 (Local Storage) 활용하기

### Local Storage에서 특정 항목의 존재 유무에 따라 다른 동작을 수행하도록 하기

- app.js

  ```javascript
  // Local Storage에 Key와 Value값 저장
  localStorage.setItem("Key", "Value");

  // Key에 해당하는 Value값 불러와 Value 변수에 저장
  const Value = localStorage.getItem("Key");

  // Value 변수값의 존재 유무에 따른 조건문
  if (Value === null) {
    // 특정 Key의 Value값이 없을 경우 해당 블록 실행
  } else {
    // 특정 Key의 Value값이 있을 경우 해당 블록 실행
  }
  ```
