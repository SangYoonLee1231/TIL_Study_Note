# TypeScript 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-masterclass">노마드 코더 - React JS 마스터클래스</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/about_typescript.md#typescript%EB%9E%80">TypeScript란?</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/about_typescript.md#typescript%EC%9D%98-%ED%8A%B9%EC%A7%95">TypeScript의 특징</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/about_typescript.md#typescript-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0">TypeScript 설치하기</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/about_typescript.md#definitelytyped">DefinitelyTyped</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/TypeScript/about_typescript.md#%EB%B6%80%EB%A1%9D--tsconfigjson-%ED%8C%8C%EC%9D%BC-%EC%84%A4%EC%A0%95-%EC%B6%94%EC%B2%9C"><code>tsconfig.json</code> 파일 설정 추천</a>

<br/><br/>

## TypeScript란?

- JavaScript를 기반으로 한 프로그래밍 언어이다.

  - JavaScript와 문법이 동일하다.

- JavaScript의 슈퍼 셋이다.

  - JavaScript의 기본 기능을 모두 제공하되, 몇 가지 '새로운 기능'을 추가로 더 제공해주는 언어이다.

  - TypeScript의 '새로운 가능' : <strong>명시적인 데이터 유형 설명</strong>

<br/>

- 쉽게 말하면, TypeScript는 JavaScript에 **Type을 부여**한 언어이다.

<br/><br/>

### TypeScript 등장 배경

- JavaScript의 소스 코드가 점점 복잡해지고, JS가 클라이언트 측 언어를 넘어 서버 측 기술로도 활용되기 시작하면서,

- Type 검사 및 컴파일 시 오류 검사의 기능을 수용하여,

- JS를 본격적인 서버 측 기술로 활용할 수 있도록 하기 위해 TypeScript가 제시되었다.

<br/><br/>

### TypeScript의 특징

- **strongly-typed 언어** : 프로그래밍 언어가 작동하기 전에 type를 확인한다.

  - 코드에 타입 관련 오류가 있어도 프로그램 실행 전 TypeScript가 타입 에러를 미리 확인해준다. (타입 실수를 바로 잡아준다)

    ```js
    const plus = (a, b) => a + b;
    ```

    ```ts
    const plus = (a: number, b: number) => a + b;
    ```

<br/>

- TypeScript (TS) 는 브라우저에서 읽을 수 없는 언어이기 때문에 publish 시 JavaScript 언어로 **컴파일**된다.

- TypeScript는 성능 향상과는 관계가 없다.

<br/><br/>

### TypeScript를 사용하는 이유

- TypeScript는 JavaScript 코드를 단순화하여 더 쉽게 읽고 이해 할 수 있다.

- TypeScript는 코드 유형 검사를 통해 JacaScript를 작성할 떄 개발자가 일반적으로 겪는 버그를 미리 예방할 수 있다.

- TypeScript는 ES6 (ECMAScript6) 의 모든 이점과 더 많은 생산성을 제공한다.

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

- (TS로 만들어지지 않은) **유명한 npm 라이브러리**를 TS에서도 지원되도록 **타입을 정의하고 제공**해주는 저장소

  - <a href="https://github.com/DefinitelyTyped/DefinitelyTyped">DefinitelyTyped Repository</a>

- DefinitelyTyped를 통해 TS에서도 JS로 만들어진 라이브러리를 사용할 수 있다.

  - (`@types` 로 시작함)

  ```
  [styled-components를 TS에서도 읽을 수 있도록 해주기]
  npm i -D @types/styled-components @types/
  ```

<br/><br/>

### 부록 : <code>tsconfig.json</code> 파일 설정 추천

> 출처 : https://codingapple.com/unit/typescript-tsconfig-json/

```json
{
  "compilerOptions": {
    "target": "es5", // 'es3', 'es5', 'es2015', 'es2016', 'es2017','es2018', 'esnext' 가능
    "module": "commonjs", //무슨 import 문법 쓸건지 'commonjs', 'amd', 'es2015', 'esnext'
    "allowJs": true, // js 파일들 ts에서 import해서 쓸 수 있는지
    "checkJs": true, // 일반 js 파일에서도 에러체크 여부
    "jsx": "preserve", // tsx 파일을 jsx로 어떻게 컴파일할 것인지 'preserve', 'react-native', 'react'
    "declaration": true, //컴파일시 .d.ts 파일도 자동으로 함께생성 (현재쓰는 모든 타입이 정의된 파일)
    "outFile": "./", //모든 ts파일을 js파일 하나로 컴파일해줌 (module이 none, amd, system일 때만 가능)
    "outDir": "./", //js파일 아웃풋 경로바꾸기
    "rootDir": "./", //루트경로 바꾸기 (js 파일 아웃풋 경로에 영향줌)
    "removeComments": true, //컴파일시 주석제거

    "strict": true, //strict 관련, noimplicit 어쩌구 관련 모드 전부 켜기
    "noImplicitAny": true, //any타입 금지 여부
    "strictNullChecks": true, //null, undefined 타입에 이상한 짓 할시 에러내기
    "strictFunctionTypes": true, //함수파라미터 타입체크 강하게
    "strictPropertyInitialization": true, //class constructor 작성시 타입체크 강하게
    "noImplicitThis": true, //this 키워드가 any 타입일 경우 에러내기
    "alwaysStrict": true, //자바스크립트 "use strict" 모드 켜기

    "noUnusedLocals": true, //쓰지않는 지역변수 있으면 에러내기
    "noUnusedParameters": true, //쓰지않는 파라미터 있으면 에러내기
    "noImplicitReturns": true, //함수에서 return 빼먹으면 에러내기
    "noFallthroughCasesInSwitch": true //switch문 이상하면 에러내기
  }
}
```
