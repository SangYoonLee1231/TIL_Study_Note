# Next JS란?

> 참고 자료 : <a href="https://www.inflearn.com/course/lecture?courseSlug=%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A0%88%EB%94%A7&unitId=123111&tab=curriculum">인프런 - 따라하며 배우는 노드, 리액트 시리즈 - 레딧 사이트 만들기(NextJS) (John Ahn님)</a>

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## Next JS란?

- React에서 <strong>SSR(Server Side Rendering)</strong>을 쉽게 구현할 수 있도록 도와주는 간단한 **프레임워크**이다.

- 리엑트로 개발할 땐 SPA(Single Page Application)를 이용하여 CSR(Client Side Rendering)을 하지만, 이 방식은 검색 엔진 최적화(SEO) 부분에서 단점이 존재한다.

  - 왜 이러한 단점이 있는지는 <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NextJS/ssr_vs_csr.md">여기</a>를 참고하여 짚고 넘어가자.

<br/>

### Next JS 설치

- `npx create-next-app@latest`

- 타입스크립트를 사용한다면 `npx create-next-app@latest --typescript`

- 현재 디렉토리에 설치하려 한다면 `npx create-next-app@latest --typescript./`

<br/><br/>

## Next JS 기본 파일 구조

- (설치 시 src 폴더를 생성하지 않는다고 설정했음을 가정한다)

  <div align="center">

    <img src="img/nextjs-file-structure.png" width="120">

  </div>

<br/>

### pages

- 페이지들을 생성하는 폴더

  - 페이지 이름에 `.jsx`, 타입스크립트를 쓴다면 `.tsx`를 붙여 페이지를 생성한다.

  - `about` 페이지 생성 → `about.jsx` 혹은 `about.tsx`

- `_app.tsx` : 페이지의 공통된 레이아웃을 작성하는 곳

  - 특정 페이지로 진입하기 전에 먼저 통과하는 인터셉터 페이지이다.

  - 즉, 이 곳에서 렌더링 하는 값은 모든 페이지에 적용된다.

- `document.tsx` : meta 태그를 정의하거나, 전체 페이지에 관여하는 컴포넌트이다.

- `index.tsx` : 앱의 첫 `"/"`(루트) 페이지

<br/>

### public

- 정적 에셋들을 보관하는 폴더

  - 예 : 이미지

<br/>

### styles

- CSS 스타일링을 처리해주는 폴더

- 글로벌 스타일은 `_app.tsx`에서만 정의해줄 수 있다.

- 컴포넌트에 종속적으로 스타일링을 주기 위해 모듈(module) CSS를 사용할 수 있다.

  - `index.tsx`(홈 컴포넌트)에 종속적으로 스타일링을 해주려면 `Home.module.css` 파일명을 이 폴더에 만들고, 이 파일에 CSS 코드를 삽입하면 된다.

<br/>

- NextJS는 webpack을 기본 번들러로 사용한다.

- 그래서 webpack 관련 설정들은 `next.config.js`에서 한다.

<br/><br/>

## Pre-rendering

- Next
