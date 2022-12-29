# TypeScript 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-masterclass">노마드 코더 - React JS 마스터클래스</a>

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## TypeScript란?

- JavaScript를 기반으로 한 프로그래밍 언어이다.

  - JavaScript와 문법이 동일하다.

- JavaScript의 슈퍼 셋이다.

  - JavaScript의 기본 기능을 모두 제공하되 몇 가지 '새로운 기능'을 추가로 더 제공해주는 언어이다.

  - TypeScript의 '새로운 가능' : <strong>명시적인 데이터 유형 설명</strong>

<br/><br/>

### TypeScript의 특징

- strongly-typed 언어 : 프로그래밍 언어가 작동하기 전에 type를 확인한다.

  - 코드에 타입 관련 오류가 있어도 프로그램 실행 전 TypeScript가 타입 에러를 확인하다. (타입 실수를 바로 잡아준다)

    ```js
    const plus = (a, b) => a + b;
    ```

    ```ts
    const plus = (a: number, b: number) => a + b;
    ```

<br/>

- TypeScript (TS) 는 브라우저에서 읽을 수 없는 언어이기 때문에 publish 시 JavaScript 언어로 컴파일된다.

<br/><br/>

## TypeScript 설치하기

- [방법 1] Create React App을 통해 설치하기

  ```
  npx create-react-app [프로젝트(엡) 이름] --template typescript
  ```

- [빙법 2] 필요한 패키지 모두 설치하기

  ```
  npm install --save typescript @types/node @types/react @types/react-dom @types/jest
  ```

<br/>

### DefinitelyTyped

- (TS로 만들어지지 않은) 유명한 npm 라이브러리를 TS에서도 지원되도록 타입을 제공해주는 저장소

  - <a href="https://github.com/DefinitelyTyped/DefinitelyTyped">DefinitelyTyped Repository</a>

- DefinitelyTyped를 통해 TS에서도 JS로 만들어진 라이브러리를 사용할 수 있다.

  ```
  npm i -D @types/styled-components @types/
  ```
