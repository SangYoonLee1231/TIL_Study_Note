# JavaScript - 조각 지식 모음

<br/>

- JavaScript와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%81%AC%EB%A1%AC-%EC%BD%98%EC%86%94%EC%B0%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%A4%84%EB%B0%94%EA%BF%88-%EB%B0%A9%EB%B2%95">크롬 콘솔창에서의 줄 바꿈 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%A6%AC%ED%84%B0%EB%9F%B4-template-literal---%EB%B0%B1%ED%8B%B1%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%91%9C%EA%B8%B0%EB%B2%95">템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#math-%EB%AA%A8%EB%93%88---random-%EA%B8%B0%EB%8A%A5">Math 모듈 - Random 기능</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#json%EC%9D%B4%EB%9E%80">JSON이란?</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#jsonstringify---%EB%AA%A8%EB%93%A0-%EA%B2%83%EC%9D%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C-%EB%B3%80%ED%99%98%EC%8B%9C%ED%82%A4%EB%8A%94-%ED%95%A8%EC%88%98"><code>JSON.stringify()</code> - 모든 것을 문자열로 변환시키는 함수</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9">구조 분해 할당</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/JavaScript/javascript_piece_info.md#%EB%B0%B0%EC%97%B4-%EA%B0%9D%EC%B2%B4%EA%B0%80-%EB%B9%84%EC%96%B4%EC%9E%88%EB%8A%94%EC%A7%80%EB%A5%BC-%EC%A1%B0%EA%B1%B4%EB%AC%B8%EC%9D%84-%ED%86%B5%ED%95%B4-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-truthy-falsy-%EC%8B%AC%ED%99%94">배열, 객체가 비어있는지를 조건문을 통해 확인하기 (<code>truthy</code>, <code>falsy</code> 심화)</a>
- <a href=""></a>

<br/>

## 크롬 콘솔창에서의 줄 바꿈 방법

> 참고 자료 : <a href="https://lemeraldl.tistory.com/588">크롬 콘솔창에서 작업 할때 엔터 키 (개인 블로그)</a>

- 크롬 콘솔창에서 작업 시 줄 바꿈을 하려면, <strong>[Shift] + [Enter]</strong> 두 키를 동시에 누르면 된다.

<br/><br/>

## 템플릿 리터럴 (Template Literal) - 백틱을 사용하는 문자열 표기법

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

## Math 모듈 - Random 기능

- <strong>0부터 9까지 중 무작위로 숫자 뽑기</strong>

  - <code>Math.random()</code> 코드를 활용한다.

    - 0과 1사이 임의의 소수를 무작위로 반환해주는 코드

  <br/>

  - <code>Math.random()</code>을 통해 임의로 반환된 소수에 <strong>10을 곱한후 소수점을 버린다</strong>.

    ```javascript
    const num = Math.random() * 10;

    /* [방법1] ceil : 올림 */
    const ans = Math.ceil(num) - 1;

    /* [방법2] floor : 버림 */
    const ans = Math.floor(num);

    /* [방법3] round : 반올림 */
    const ans = Math.round(num - 0.5);
    ```

<br/><br/>

## JSON이란?

- 프로그래머가 파일에 정보를 저장하기 위해 만든 하나의 방식

```json
{
  "name": "my-project"
}
```

- 예) <code>package.json</code>

<br/><br/>

## <code>JSON.stringify()</code> - 모든 것을 문자열로 변환시키는 함수

- <code>JSON.stringify(어떤것)</code> 함수는 JS object나 array 또는 어떤 JS 코드이건 간에, 문자열로 변환시켜주는 함수이다.

  ```javascript
  const player = { name: "Sang Yoon Lee" };

  JSON.stringify(player);
  ```

<br/>

- 이를 다시 객체(혹은 배열)로 변환하려면 <code>JSON.parse(어떤것)</code> 함수를 사용하면 된다.

  ```javascript
  JSON.parse(player);
  ```

<br/><br/>

## 구조 분해 할당

- 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있도록 하는 JS 표현식이다.

- 파이썬의 unpacking과 같은 개념이다.

  ```javascript
  const numList = [1, 2, 3];

  const firstNum = numList[0];
  const secondNum = numList[1];
  const thirdNum = numList[2];
  ```

  ```javascript
  const numList = [1, 2, 3];

  const [firstNum, secondNum, thirdNum] = numList;
  ```

<br/><br/>

## 배열, 객체가 비어있는지를 조건문을 통해 확인하기 (<code>truthy</code>, <code>falsy</code> 심화)

### 배열

- (<code>''</code>은 <code>falsy</code>한 값이나) <code>[]</code>은 <code>truthy</code>한 값이다.

- 따라서 배열이 비어있는지를 조건문을 통해 확인하려면, 조건식이 <code>[]</code>이 아닌 <code>[].length</code>으로 주어야 한다.

  ```js
  const array = [];

  if (array.length) {
    console.log("array is empty");
  } else {
    console.log("array is not empty");
  }
  ```

<br/>

### 객체

- 객체가 비어있는지를 조건문을 통해 확인하려면 역시 <code>length</code>를 활용하면 된다.

  ```js
  const obj = {};

  const isObjEmpty = Object.keys(obj).length == 0;

  if (isObjEmpty) {
    console.log("Object is Empty");
  } else {
    console.log("Object is not Empty");
  }
  ```

<br/>

###
