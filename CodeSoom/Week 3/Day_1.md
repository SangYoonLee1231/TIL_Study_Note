# 3주차 Day 1 TIL

#### 2022.08.15

<br/>

## 배운 것 (간략히 정리)

### 【1】 <strong>Special Props Warning 문제에 대한 고찰</strong>

- <strong>저번주에 해결하지 못한 의문점</strong>

    - <a href="https://ko.reactjs.org/warnings/special-props.html">컴포넌트에 key 속성을 부여하면 해당 컴포넌트에서 값을 제대로 읽지 못한다.. 이는 prop이 아니라고 한다.</a>

    - 하지만 <a href="https://ko.reactjs.org/docs/lists-and-keys.html#extracting-components-with-keys">React 공식문서의 해당 부분</a>을 살펴보면, <strong>컴포넌트에 key 속성을 부여하는 것이 옳바른 사용법이다.</strong>

    - 그럼 어떻게 해야 할까?

<br/>

1. 공식 문서를 통해 key 학습

- key를 index으로 부여하면 심각한 문제를 야기할 수 있다. (같은 key 값이 다른 요소에 부여될 수 있음)

- 해당 문제에 별로 도움이 되진 않음

<br/>

2. 다른 자료 참고

    - <a href="https://stackoverflow.com/questions/33661511/reactjs-key-undefined-when-accessed-as-a-prop">Stack Overflow 질문</a>

    - <a href="https://bobbyhadz.com/blog/react-key-is-not-a-prop-trying-to-access-it-results-undefined">해외 포스트</a>


<br/>

- 자료들을 참고하며 공부한 결과, 다음 2가지 사실을 알게 되었다.

    - key에 index를 주게 될 경우 항목이 재배열되면 효율성이 떨어지기 때문에 좋은 방법이 아니다.

      따라서 컴포넌트에 key값을 넘기려면 고유한 id값을 부여해주어야 한다.

    - key는 특수한 prop으로, 접근 시 undefined가 리턴된다.  
    
      따라서 key 대신 다른 이름 (예를 들면 myKey)로 prop 이름을 지어주어야 한다.

<br/>

- 하지만 무언가 찝찝했다. 자료를 찾아보면서 본 여러 예시 코드에선 멀쩡히 부모 컴포넌트에 key값을 부여했는데도 코드가 잘 동작하던데, 왜 내 코드는 에러가 날까.

- 한참을 고민하다 코드숨 대표님께 질문을 드려보기로 했다.

- 하지만 질문을 작성하면서 내가 props의 개념과 문법을 헷갈려한다는 것을 알았다.

- 저런. React와 JavaScript의 기초가 부족한 채로 교육을 따라가다 보니 이렇게 문제가 터지는구나.