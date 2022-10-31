# React JS 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="">React JS의 개녕과 탄생 배경</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-%EC%84%A4%EC%B9%98">React 설치</a>
- <a href=""></a>

<br/><br/>

## React JS의 개념과 탄생 배경

### React 탄생 배경

- 웹 애플리캐이션의 등장에 따라 웹 개발의 복잡성이 증가하게 되었다.

  - <strong>웹 애플리케이션</strong> : 웹 브라우저를 통해 응용 소프트웨어의 기능을 이용할 수 있도록 만든 웹 서비스

- 이에 따라 DOM을 직접 조작하는 (Vanila JS, jQuery를 이용하는) 기존의 개발 방법으론 한계가 생기게 되었다.

- 이러한 상황에서 자연스럽게 프론트엔드 개발의 생산성 향상과 난이도 하향을 위한 여러 라이브러리 및 프레임워크가 탄생하였다.

  - 이 중 제일 많이 사용되는 것은, React, Angular, Vue이다.

<br/><br/>

### React JS란?

- React JS (혹은 React)는 어플리케이션이 <strong>interactive</strong>하도록 만들어주는 <strong>프레임워크 (Framework) </strong>이자 <strong>라이브러리 (Library) </strong>이다.

  <img src="img/react-is-both.png" width="650">

  - React 는 UI를 만드는 기능만을 제공해주기에, 라이브러리 하나로만 분류하는 관점도 존재한다.

<br/>

> < <strong>Framework VS Library</strong> >
>
> <strong>공통점</strong> : 복잡한 개발을 편리하게 하도록, 필요 기능들을 미리 만들어 사용할 수 있는 형태로 제공된 코드
>
> <strong>차이점</strong> : <strong>Framework</strong>은 전체적인 틀(Frame)을 제공해주기 때문에, 개발자가 그 틀 안에서 그 방식에 맞춰 작업해야 한다. 반면 <strong>Library</strong>는 틀이 아닌 하나의 기능만을 도구처럼 제공해주기 때문에, 개발자가 필요한 여러 도구를 가져와 조립해서 사용해야 한다.

<br/>

- React JS는 <strong>모든 것이 JavaScript에서 시작한다.</strong> HTML 요소를 JS에서 직접 만들어서 HTML에 반영한다.

<br/><br/><br/>

## React JS의 장점

- 다른 프레임워크 (혹은 라이브러리)에 비해 문법이 자바스크립트를 그대로 사용하기 때문에, React를 사용하는 것만으로도 JS 문법과 훨씬 더 친숙해질 수 있다.

- Meta(구 Facebook)에서 지속적으로 관리해주는 라이브러리로, 사용자가 많아 생태계가 잘 활성화되어 있다. (현재 FE에서 가장 많이 사용)

  - 이에 따라 React에 대해 개발자들이 고민하고 도출한 많은 해결방법이 존재한다.

  - 또한 React 기반으로 개발된 기술이나 서비스가 많이 존재하고 제공된다.

  - 이는 곧 React를 이용한 개발의 생산성이 높아진다는 것을 의마한다.

- UI를 구축하는 기능만을 담당하므로, 유연하게 확장해서 사용할 수 있는 기술이다. (ex : React Native)

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

### ✨ 방법 2 : Node.js를 통해 설치 - CRA

- 사전 지식 : <a href="">Node JS & NPM 소개 및 설치</a>

- React도 일종의 패키지이므로 다운로드 받기 위해선 NPM이 필요하다.

- 또한 React를 이용해서 개발환경을 구축하려면 다른 패키지도 필요하고, 이 패키지들을 함께 실행할 환경도 제공되어야 하므로 NPM과 Node JS의 설치는 필수이다.

<br/>

- React 개발에 필요한 패캐지를 일일이 찾아 설치할 수도 있지만, 이는 까다로운 과정이기에, 대신 React와 필요한 도구들을 미리 조합해서 설정해둔 "툴체인"을 활용할 수 있다.

  - (<strong>툴체인</strong>> : 여러 도구들을 연결해놓은 것)

- React 공식문서에서는 'React를 배우고 있거나, 새로운 싱글 페이지 앱(SPA)를 만들고 싶다면 <strong>Create React App</strong> 툴체인 사용을 권장한다.'

  - CRA 설치 명령어 : <code>npx create-react-app westagram-react</code>
