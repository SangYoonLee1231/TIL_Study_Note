# React JS 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료, <a href="https://fastcampus.co.kr/dev_academy_kmt2">김민태의 프론트엔드 아카데미 2강<a/>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-js%EC%9D%98-%EA%B0%9C%EB%85%90%EA%B3%BC-%ED%83%84%EC%83%9D-%EB%B0%B0%EA%B2%BD">React JS의 개녕과 탄생 배경</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-%ED%83%84%EC%83%9D-%EB%B0%B0%EA%B2%BD">React 탄생 배경</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-js%EB%9E%80">React JS란?</a>
  - <a href="">React의 핵심 개념 및 특징</a>
  - <a href="">React에서 가상 DOM을 만들게 된 배경</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-%EC%84%A4%EC%B9%98">React 설치</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#%EB%B0%A9%EB%B2%95-1--html-%EB%AC%B8%EC%84%9C%EC%97%90-react-react-dom%EC%9D%84-import%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95">방법 1 : HTML 문서에 <code>react</code>, <code>react-dom</code>을 import하는 방법</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#-%EB%B0%A9%EB%B2%95-2--nodejs%EB%A5%BC-%ED%86%B5%ED%95%B4-%EC%84%A4%EC%B9%98---cra-create-react-app">방법 2 : Node.js를 통해 설치 - CRA (Create React App)</a>

<br/><br/>

## React JS의 개념과 탄생 배경

### React 탄생 배경

- 웹 애플리캐이션이 등장함에 따라 웹 개발의 복잡성이 증가하게 되었다.

  - <strong>웹 애플리케이션</strong> : 웹 브라우저를 통해 응용 소프트웨어의 기능을 이용할 수 있도록 만든 웹 서비스

- 이에 따라 DOM을 직접 조작하는 (Vanila JS, jQuery를 이용하는) 기존의 개발 방법으로는 한계가 생겼다.

- 이러한 상황에서 자연스럽게 프론트엔드 개발의 생산성 향상과 난이도 하향을 위한 여러 라이브러리 및 프레임워크가 탄생하였다.

  - 이 중 현재 제일 많이 사용되는 것은 React, Angular, Vue이다.

<br/><br/>

### React JS란?

- React JS (혹은 React)는 <strong>UI를 구축</strong>하고 어플리케이션이 <strong>interactive</strong>하도록 만들어주는 <strong>프레임워크 (Framework)</strong>이자 <strong>라이브러리 (Library)</strong>이다.

  <img src="img/react-is-both.png" width="650">

  - React는 보통 <strong>프레임워크</strong>로 분류되나, UI를 만드는 기능만을 제공해주기에 라이브러리 하나로만 분류하는 관점도 존재한다.

<br/>

> < <strong>Framework VS Library</strong> >
>
> <strong>공통점</strong> : 복잡한 개발을 편리하게 할 수 있도록, 필요한 기능들을 미리 만들어 사용할 수 있는 형태로 제공된 코드
>
> <strong>차이점</strong> : <strong>Framework</strong>은 전체적인 틀(Frame)을 제공해주기 때문에, 개발자가 그 틀 안에서 그 방식에 맞춰 작업을 해야만 한다. / 반면 <strong>Library</strong>는 하나의 기능만을 도구로써 제공해주기 때문에, 개발자 본인이 필요한 여러 도구들을 직접 가져와서 조립히여 사용해야 한다.

<br/>

- React JS는 <strong>모든 것이 JavaScript에서 시작한다.</strong> HTML 요소를 JS에서 직접 만들어서 HTML에 반영한다.

  - 이를 CSR(Client Side Rendering)이라 부른다.

  - (CSR에 대한 자세한 내용은 <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NextJS/ssr_vs_csr.md">여기</a>를 참고)

<br/><br/>

### <strong>React의 핵심 개념 및 특징</strong>

- Angular처럼 재사용이 가능한 <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_jsx.md#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8">컴포넌트(Component)</a>를 조합하여 웹사이트(앱)를 만드는데 도움을 주는 라이브러리다.

  - Angular 프레임워크는 데이터의 흐름을 파악하기 어려운 문제가 있으므로, 이를 해결하기 위해 페이스북에서 React라는 새 프레임워크를 개발하였다.

- <strong>가상 DOM을 생성하고, render시 이를 실제 DOM과 비교하여 변화된 부분만 찾아 앱에 반영한다.</strong>

- React는 일방향적인 데이터 흐름을 보여준다.

  - state ⇒ component ⇒ 가상 DOM ⇒ 실제 DOM과 비교 ⇒ 화면에 그리기

- React는 UI 라이브러리에 불과하다. 하지만 이로 인해 오히려 다른 플랫폼에서도 React를 활용할 수 있다.

<br/><br/>

### <strong>React에서 가상 DOM을 만들게 된 배경</strong>

- React는 가상 DOM을 통해 개발자가 직접 DOM을 조작하지 않도록 하는 개발 방식을 택하였다.

- 그 이유는, DOM API는 너무나 많은 기능을 재공해주는 방대한 API이지만, 웹 애플리케이션 개발에 최적화된 형태로 되어있진 않기 때문이다.

- 이로 인해 애플리케이션이 복잡해질수록 DOM API를 가지고 UI를 만들 때 더 많은 문제들이 발생할 수 있다. (아래는 DOM API의 문제점이다.)

  - DOM은 일관적이지 않다.

  - DOM은 라이브 오브젝트라는 컨셉을 가지고 있어 어떤 API는 DOM 객체를 참조하지만(NodeList), 어떤 API는 DOM 객체를 참조하지 않는다(HTMLCollection).

  - 또한, 엄청나게 다양한 브라우저로 인한 크로스 브라우징 이슈도 개발자에게 고통을 주는 중대한 요소이다.

<br/>

- 그래서 React팀은 DOM을 다루기 위해 과감하게 DOM을 쓰지 말자는 결정을 내렸다.

- 대신 DOM의 모조품인 '가상 DOM'을 만들어, <strong>DOM에 대한 직접적인 조작은 React 쪽에서 감당하고, 개발자에게는 훨씬 다루기 편한 가상 DOM을 주어</strong> 더 쉽고 편리한 개발 환경을 제공해주었다.

- 이렇게 '다루기 까다로운 무언가가 있다면, 더 다루기 쉬운 포멧으로 바꿔서 다루자'는 아이디어는 소프트웨어 개발에 많이 사용되는 중요한 개념이다.

<br/><br/><br/>

## React JS 설치

### 방법 1 : HTML 문서에 <code>react</code>, <code>react-dom</code>을 import하는 방법

- 따로 다른 프로그램을 PC에 설치하지 않는 방법으로, 두 개의 Javascript 코드(<code>react</code>, <code>react-dom</code>)를 HTML에 import 해준다.

  ```html
  <!-- React 17.0.2 버전 -->
  <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.development.js"></script>
  ```

  (<code>react-dom</code>은 모든 React element들을 HTML에 둘 수 있도록 해주는 library 또는 package이다.)

<br/><br/>

### ✨ 방법 2 : Node.js를 통해 설치 - CRA (Create React App)

- 사전 지식 : <a href="">Node JS & NPM 소개 및 설치</a>

- React도 일종의 패키지이므로 다운로드 받기 위해선 NPM이 필요하다.

- 또한 React를 이용해서 개발환경을 구축하려면 다른 패키지들과 이를 함께 실행할 환경이 제공되어야 하므로, NPM과 Node JS의 설치는 필수적이다.

<br/>

- React 개발에 필요한 패키지를 일일이 찾아 설치하는 방법도 있지만, 이는 까다로운 과정이기에, 대신 React와 필요한 도구들을 미리 조합하여 설정해둔 "툴체인"을 활용할 수 있다.

  - (<strong>툴체인</strong> : 여러 도구들을 연결해놓은 것)

- React 공식문서에서는 'React를 배우고 있거나, 새로운 싱글 페이지 앱(SPA)를 만들고 싶다면 <strong>Create React App</strong> 툴체인을 사용할 것을 권장한다.'라고 적혀 있다.

  - <strong>CRA 설치 명령어</strong> : <code>npx create-react-app [프로젝트 이름]</code>

<br/>
