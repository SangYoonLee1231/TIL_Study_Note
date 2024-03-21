# JavaScript - 클로저

> 참고 자료 : 책 '모단 자바스크립트 Deep Dive', 김민태님 프론트엔드 스쿨 강의

<!-- <br/> -->

<!-- ### 목차 -->

  <!-- - <a href=""></a> -->
  <!-- - <a href=""></a> -->

<br/>

## 클로저의 예시

```js
function increment() {
  let saveNumber = 1;

  return function () {
    return saveNumber++;
  };
}

const inc = increment();

inc(); // 1
inc(); // 2
inc(); // 3
```

- 내부 함수에서 외부 함수에 있는 변수(saveNumber)에 접근하고자 할 때, 원래라면 사라져야 할 이 지역 변수는 클로저라는 공간에 저장되어, 내부 함수에서 이 외부 함수의 지역 변수에 접근을 할 수 있게 된다.

<br/>

## 클로저의 장점

- 함수가 리턴되도 내부 지역 변수는 보호되어 계속 사용될 수 있다.

- 더불어, 이 변수가 보호되었기 때문에 바깥 공간에선 어떤 방법으로든 이 내부 지역 변수에 접근할 길이 없다.

  - 클로저는 완벽하게 보호되는 공간

<br/>

## TypeScript로 클로저 구현하기

```ts
class MyObj {
  private saveNumber: number;
}
```

<br/>
