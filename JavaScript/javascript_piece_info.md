## JavaScript - 조각 지식 모음

<br/>

- JavaScript와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%81%AC%EB%A1%AC-%EC%BD%98%EC%86%94%EC%B0%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%A4%84%EB%B0%94%EA%BF%88-%EB%B0%A9%EB%B2%95">크롬 콘솔창에서의 줄 바꿈 방법</a>
- <a href="">템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/>

### 크롬 콘솔창에서의 줄 바꿈 방법

> 참고 자료 : <a href="https://lemeraldl.tistory.com/588">크롬 콘솔창에서 작업 할때 엔터 키 (개인 블로그)</a>

- 크롬 콘솔창에서 작업 시 줄 바꿈을 하려면, <strong>[Shift] + [Enter]</strong> 두 키를 동시에 누르면 된다.

<br/>

### 템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법

> 참고 자료 : <a href="https://nomadcoders.co/javascript-for-beginners">노마드 코더 - 바닐라 JS로 크롬 앱 만들기</a>, <a href="https://leeborn.tistory.com/entry/JavaScript-ES2015-%EB%B0%B1%ED%8B%B1%EA%B3%BC-%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%AC%B8%EC%9E%90%EC%97%B4">\[JavaScript] ES2015 백틱(`)과 템플릿 문자열 (블로그 포스트)</a>

- 백틱을 사용해 문자열에 변수를 추가할 수 있다.

  ```javascript
  const username = "Jason";
  const message = `Hello ${username}`;
  console.log(message);
  ```

- 백틱 내에선 줄바꿈도 자동으로 적용된다.

  ```javascript
  console.log(`first line
  second line`);
  ```
