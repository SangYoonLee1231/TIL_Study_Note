# JavaScript - 조각 지식 모음

<br/>

- JavaScript와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%81%AC%EB%A1%AC-%EC%BD%98%EC%86%94%EC%B0%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%A4%84%EB%B0%94%EA%BF%88-%EB%B0%A9%EB%B2%95">크롬 콘솔창에서의 줄 바꿈 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%A6%AC%ED%84%B0%EB%9F%B4-template-literal---%EB%B0%B1%ED%8B%B1%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%91%9C%EA%B8%B0%EB%B2%95">템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#math-%EB%AA%A8%EB%93%88---random-%EA%B8%B0%EB%8A%A5">Math 모듈 - Random 기능</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/>

### 크롬 콘솔창에서의 줄 바꿈 방법

> 참고 자료 : <a href="https://lemeraldl.tistory.com/588">크롬 콘솔창에서 작업 할때 엔터 키 (개인 블로그)</a>

- 크롬 콘솔창에서 작업 시 줄 바꿈을 하려면, <strong>[Shift] + [Enter]</strong> 두 키를 동시에 누르면 된다.

<br/><br/>


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

<br/><br/>

### Math 모듈 - Random 기능

- <strong>0부터 9까지 중 무작위로 숫자 뽑기</strong>

  - <code>Math.random()</code> 코드를 활용한다.

    - 0과 1사이 임의의 소수를 무작위로 반환해주는 코드

  <br/>

  - <code>Math.random()</code>을 통해 임의로 반환된 소수에 <strong>10을 곱한후 정수로 변환</strong>하여 소수점을 버린다.

    ```javascript
    const num = Math.random() * 10;

    /* [방법1] ceil : 올림 */
    const ans = Math.ceil(num) - 1;

    /* [방법2] floor : 버림 */
    const ans = Math.floor(num);

    /* [방법3] round : 반올림 */
    const ans = Math.round(num - 0.5);
    ```