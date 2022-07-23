# React JS 소개 및 설치

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react%EC%9D%98-%EB%AA%A9%EC%A0%81">React의 목적</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/about_react.md#react-%EC%84%A4%EC%B9%98">React 설치</a>
- <a href=""></a>

<br/><br/>

## React JS의 목적

- React JS는 어플리케이션이 <strong>interactive</strong>하도록 만들어주는 <strong>framework</strong>이자 <strong>library</strong>이다. (React 탄생 이유)

  <img src="img/react-is-both.png" width="650">

- React JS는 <strong>모든 것이 JavaScript에서 시작한다.</strong> HTML 요소를 JS에서 직접 만들어서 HTML에 반영한다.

<br/><br/>

## React JS 설치

### 방법 1 : HTML 문서에 <code>react</code>, <code>react-dom</code>을 import하는 방법

- 따로 다른 프로그램을 PC에 설치하지 않는 방법으로, 두 개의 Javascript 코드를 HTML에 import 해준다.

  - <code>react</code>, <code>react-dom</code>

    - react-dom은 모든 React element들을 HTML에 둘 수 있도록 해주는 library 또는 package이다.

  ```html
  <!-- React 17.0.2 버전 -->
  <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.development.js"></script>
  ```

<br/><br/>

##
