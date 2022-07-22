# React JS 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react%EC%9D%98-%EB%AA%A9%EC%A0%81">React의 목적</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-%EC%84%A4%EC%B9%98">React 설치</a>
- <a href=""></a>

<br/><br/>

## React JS의 목적

- React JS는 UI를 interactive하게 만들어준다. (React가 탄생한 이유)

- React JS는 모든 것이 JavaScript에서 시작한다. HTML 요소를 JS에서 직접 만들어서 HTML에 반영한다.

<br/><br/>

## React JS 설치

### 방법 1 : HTML 문서에 <code>react</code>, <code>react-dom</code>을 import하는 방법

- React JS를 설치하기 위힌 하나의 방법으로, 두 개의 Javascript 코드를 HTML에 import 해준다.

  - <code>react</code>, <code>react-dom</code>

    - React JS는 어플리케이션이 interactive하도록 만들어주는 library이다.

    - react-dom은 모든 React element들을 HTML에 둘 수 있도록 해주는 library 또는 package이다.

  ```html
  <!-- React 17.0.2 버전 -->
  <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.development.js"></script>
  ```

<br/><br/>

##