# JavaScript - 비동기 프로그래밍 (Execution Context)

> 참고 자료 : 책 '모단 자바스크립트 Deep Dive'

<!-- <br/> -->

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Basic_Language/JavaScript/javascript_asynchronous.md#%EB%8F%99%EA%B8%B0-%EC%B2%98%EB%A6%AC%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%B2%98%EB%A6%AC">동기 처리와 비동기 처리</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Basic_Language/JavaScript/javascript_asynchronous.md#%EF%B8%8F-%EB%8F%99%EA%B8%B0-vs-%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%95%94%EA%B8%B0%EC%9A%A9-%ED%82%A4%EC%9B%8C%EB%93%9C">⭐️ 동기 vs 비동기 (암기용 키워드)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Basic_Language/JavaScript/javascript_asynchronous.md#%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84%EC%99%80-%ED%83%9C%EC%8A%A4%ED%81%AC-%ED%81%90">이벤트 루프와 태스크 큐</a>
  <!-- - <a href=""></a> -->
  <!-- - <a href=""></a> -->

<br/><br/>

- 사전 지식 : <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Basic_Language/JavaScript/javascript_execution_context.md">실행 컨텍스트</a>

<br/>

## 동기 처리와 비동기 처리

### 자바스크립트에서 함수의 실행 과정

- 함수가 호출되면 함수 코드가 평가되고, '함수 실행 컨텍스트'가 생성된다.

- '실행 컨텍스트 스택'에 이 생성된 '함수 실행 컨텍스트'가 push되고, 함수 코드가 수행된다.

- 함수 코드가 모두 실행되면 '실행 컨텍스트 스택'에서 해당 '함수 실행 컨텍스트가' pop되어 제거된다.

<br/>

- 스택 자료구조의 특성으로 인해 함수가 호출된 순서대로 실행된다.

<br/>

#### 예시

```js
const hello = () => {};
const bye = () => {};

hello();
bye();
```

- 실행 컨텍스트 스택

  ```
  1. [ ]
  2. [ <전역 실행 컨텍스트> ]
  3. [ <전역 실행 컨텍스트> <hello 함수 실행 컨텍스트> ]
  4. [ <전역 실행 컨텍스트> ]
  5. [ <전역 실행 컨텍스트> <bye 함수 실행 컨텍스트> ]
  6. [ <전역 실행 컨텍스트> ]
  7. [ ]
  ```

<br/>

### 자바스크립트의 특징

- JS는 오직 하나의 '실행 컨텍스트 스택'을 갖는다.

- JS 엔진은 하나에 단 하나의 테스크를 수행하는 싱글 스레드(Single Thread) 방식으로 동작한다.

- 즉, JS에서는 한 번에 오직 하나의 함수만 실행될 수 있고, 동시에 2개 이상의 함수가 실행될 순 없다.

<br/>

### 동기 방식

- 이때 만일 처리 시간이 긴 테스크가 실행된다면, 이를 기다려야 하는 다른 테스크에서는 블로킹(Blocking / 작업 중단)이 발생하게 된다.

- 이치럼 어떠한 작업으로 인해 다른 작업들이 제때 수행되지 못하고 밀릴 위험이 있는 작업 방식을 **동기 방식**이라 한다.

- 예를 들어, A 함수가 실행한 후 3초 뒤에 B 함수가 실행된다고 하면, A 함수의 실행이 3초보다 더 오래 걸릴 경우, B 함수의 실행은 뒤로 미뤄지게 되는 것(**Blocking**)이 동기 방식인 것이다.

- **동기 방식은 작업을 순서대로 처리한다.** 그렇기에 실행 순서가 보장된다는 이점이 있지만, 앞선 작업이 종료될 때까지 다른 이후 테스크들이 블로킹 된다는 단점이 있다.

<br/>

### 비동기 방식

- 반면, **비동기 방식**은 현재 실행중인 테스크가 종료되지 않더라도 다음 테스크가 곧바로 실행될 수 있는 방식이다.

- 예를 들어, A 함수가 실행한 후 3초 뒤에 B 함수가 실행된다고 하면, A 함수의 실행이 끝나지 않더라도 3초가 지날 경우 B 함수가 비동기적으로 실행되는 방식이다.

- 이때, 비동기 함수인 B 함수가 A 함수의 완료를 기다리지 않고, 브라우저에서 제공하는 Web API의 자체적으로 독립적인 스레드 또는 시스템 리소스를 사용하여 백그라운드에서 실행되므로, 프로그램이 블록되지 않는 특성을 가지게 된다.

- 비동기 방식은 앞 테스크가 끝나지 않더라도 다음 테스크가 곧바로 실행되므로 블로킹이 발생하지 않는다는 장점이 있지만, 실행 순서가 보장되지 않는다는 단점이 있다.

- 비동기 처리를 수행하는 비동기 함수는 콜백 패턴을 전통적으로 사용한다. 하지만 이는 콜백 헬을 발생시켜 가독성을 떨어뜨리고, 비동기 처리 중 발생한 에러의 예외 처리가 곤란해지게 하며, 여러 비동기 처리를 한 번에 수행함에도 한계가 있다. (Promise에 대해 살펴볼 떄 다룸)

- 비동기 처리 함수 예: `setTimeout`, `setInterval`, HTTP 요청, 이벤트 헨들러

<br/>

### ⭐️ 동기 vs 비동기 (암기용 키워드)

- **동기**: 순서대로 실행, Blocking (미뤄짐)

- **비동기**: 끼어들기, 제때 실행, Non-Blocking (안 미뤄짐)

<br/><br/>

## 이벤트 루프와 태스크 큐

- 다음은 이벤트 루프와 브라우저 환경을 나타내는 그림이다.

  <img src="img/event_loop.png" width="500"/>

  - **콜 스택 (Call Stack)**: 실행 컨텍스트 스택

  - **힙 (Heap)**: 객체가 동적으로 할당되어 저장되는 메모리 공간

<br/>

- 비동기 처리에서 소소코드의 평가와 실행은 자바스크립트 엔진에서 담당하고, 그 외 모든 처리는 자바스크립트 엔진을 구동하는 환경인 브라우저 or Node.js가 담당한다.

  - 예) setTimeout 콜백 함수

    - 콜백 함수의 처리 → 자바스크립트 엔진 담당

    - 콜백 함수의 호출 스케쥴링을 위한 타이머 설정, 콜백 함수의 등록 → 브라우저 또는 Node.js 담당

- 이를 위해 브라우저 환경은 태스크 큐(혹은 이벤트 큐, 콜백 큐)와 이벤트 루프를 제공한다.

- 자바스크립트는 싱글 스레드로 동작하지만, 브라우저는 멀티 스레드로 동작한다.

<br/>

### 테스크 큐 (Task Queue / Event Queue / Callback Queue)

- 비동기 함수의 콜백 함수 또는 이벤트 핸들러가 일시적으로 보관되는 영역이다.

- 테스크 큐에 들어간 비동기 함수는, 콜 스택이 비어있을 때 이벤트 루프에 의해 콜 스택으로 옮겨저 (바동기 처리 방식대로) 실행된다.

<br/>

### 이벤트 루프 (Event Loop)

- 싱글 스레드인 자바스크립트가 한 번에 하나의 일만 처리 가능함에도, 여러 일을 동시에 처리하는 것처럼 보이게 하는, 즉 동시성을 지원해주는 기능이다.

- 이벤트 루프는 콜 스택과 테스크 큐를 반복해서 확인한다.

- 이 때 콜 스택이 비어있고, 테스크 큐에 대기 중인 함수가 있다면 이벤트 루프는 순차적(FIFO)으로 이를 콜 스택으로 이동시킨다.

<br/>

- 즉, 비동기 함수(ex. 콜백 함수)는 태스크 큐에 푸쉬되어 대기하다가 콜 스택이 비게 되면, 즉, 전역 코드 및 명식적으로 호출된 함수가 모두 종료하면 비로소 콜 스택에 푸쉬되어 실행된다.

- 전역 실행 컨텍스트도 콜 스택에 있으므로, 전역 함수 실행이 종료 되어야 비로소 콜 스택이 비게 되어, 테스크 큐에서 대기 중인 콜백 함수가 이벤트 루프에 의해 콜 스택에 삽입되고 해당 함수의 실행 컨택스트가 만들어져 실행이 되는 것이다.

<br/><br/>

> ### 🗯️ 개념 보충 with Chat GPT
>
> #### ☝🏻 Q. 자바스크립트 동기, 비동기에 관해 질문이 있습니다.
>
> #### 자바스크립트의 비동기 방식은 자바스크립트 엔진의 콜 스택이 비어야만 태스크 큐에서 대기하고 있던 콜백 함수가 콜 스택으로 이동하여 실행이 됩니다. 즉, 어떤 콜백 함수가 예상한 타이밍에 바로 실행되지 않고 뒤로 미뤄질 수 있다는 의미입니다. 그럼 콜백 함수 입장에서는 이 또한 Blocking이 발생하는 경우인 것 같은데, 이것이 동기 방식과 무슨 차이가 나는 건지 이해가 잘 되지 않습니다.
>
> A. 좋은 질문입니다. 비동기 방식에서 콜백 함수가 콜 스택으로 이동하여 실행되기까지 콜 스택이 비어 있어야 하는데, 이로 인해 콜백 함수가 기다리는 동안 다른 작업을 수행할 수 있다는 특성이 있습니다. 이것이 동기 방식과 어떻게 다른지 설명해보겠습니다.
>
> - 동기 방식 (Synchronous):
>
>   - 코드는 위에서부터 아래로 순차적으로 실행됩니다.
>   - 한 작업이 끝나야 다음 작업이 실행됩니다.
>   - 함수 호출이 발생하면 해당 함수가 실행을 완료할 때까지 다음 코드가 실행되지 않습니다.
>   - 이 때문에 하나의 작업이 시간이 오래 걸리면 전체 프로그램이 블록되는 현상이 발생할 수 있습니다.
>
> - 비동기 방식 (Asynchronous):
>
>   - 코드는 위에서부터 아래로 순차적으로 실행되지만, 비동기 함수가 호출되면 해당 함수의 작업이 백그라운드에서 수행됩니다.
>   - 콜백 함수는 비동기 함수의 작업이 완료되면 큐(Queue)에 추가되고, 콜 스택이 비어 있을 때 콜백 함수가 콜 스택으로 이동하여 실행됩니다.
>   - 프로그램이 블록되지 않고 다른 작업을 수행할 수 있습니다.
>
> 따라서 콜백 함수가 콜 스택으로 이동하여 실행되기를 기다리는 동안 다른 작업을 수행할 수 있다는 점이 동기 방식과의 주요 차이입니다. 비동기 방식에서는 콜백 함수의 실행을 기다리는 동안에도 다른 비동기 작업이나 코드를 실행할 수 있어서 전체적인 프로그램이 효율적으로 동작할 수 있습니다.
>
>  <br/>
>
> #### ☝🏻 Q. 비동기 방식에서 비동기 함수의 작업이 백그라운드에서 수행된다고 했는데, 자바스크립트는 싱글 스레드로 한 번에 하나의 함수밖에 실행하지 못한다고 알고 있습니다. 함수의 처리는 자바스크립트 엔진에서 처리하는 걸로 알고 있는데, 그럼 이 비동기 함수의 작업을 수행하는 백그라운드의 정체는 무엇인가요?
>
> A. 맞습니다. 자바스크립트는 기본적으로 싱글 스레드로 동작하며, 이는 하나의 메인 스레드에서 코드를 실행한다는 의미입니다. 하지만 비동기 작업을 처리하기 위해 백그라운드에서 추가적인 도움을 받습니다.
>
> 비동기 함수의 작업이 백그라운드에서 수행되는 구조는 다음과 같습니다:
>
> - Web API:
>
>   - 브라우저 환경에서는 Web API가 비동기 작업을 처리합니다. 예를 들면, setTimeout, AJAX 요청, DOM 이벤트 등이 여기에 해당합니다.
>   - Web API는 자체적으로 독립적인 스레드 또는 시스템 리소스를 사용하여 작업을 처리합니다.
>   - 비동기 작업이 완료되면 콜백 함수가 작업이 완료되었다는 신호를 큐(Queue)에 넣습니다.
>
> - Callback Queue (태스크 큐):
>
>   - 콜백 함수는 완료된 순서대로 Callback Queue에 쌓입니다.
>   - 콜 스택이 비어있을 때 (메인 스레드가 아무런 작업을 수행하지 않을 때), Callback Queue의 콜백 함수가 순서대로 콜 스택으로 이동하여 실행됩니다.
>
> - 이벤트 루프 (Event Loop):
>
>   - 이벤트 루프는 콜 스택, Callback Queue를 지속적으로 모니터링하면서, 콜 스택이 비어있을 때 콜백 함수를 가져와 실행시킵니다.
>   - 이로써 비동기 작업이 메인 스레드가 다른 작업을 수행하면서도 백그라운드에서 병렬적으로 처리될 수 있습니다.
>
> 요약하면, 비동기 함수의 작업은 Web API에 의해 백그라운드에서 처리되며, 작업이 완료되면 이를 콜백 함수로 큐에 보내어 이벤트 루프에 의해 메인 스레드에서 실행되게 됩니다. 이를 통해 비동기적으로 여러 작업을 다룰 수 있습니다.

<br/>

#### 결론

- Blocking을 따지는 것은 콜백 함수의 입장에서 생각하는 것이 아니라, 전역 코드에 선언되어 있는 비동기 함수를 대상으로 생각하면 되는 것이다.

- 비동기 함수는 브라우저의 Web API에서 독자적으로 실행되므로, 병렬적으로 함수 처리가 가능해지는 것이다. 이로 인해 자바스크립트는 비동기 처리를 브라우저에게 맡겨놓고 다른 함수를 처리할 수 있게 된다. 이것이 비동기 방식의 장점이다.

<br/><br/>