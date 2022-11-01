# Node JS & NPM 소개 및 설치

> 참고 자료 : 공식 문서, 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NodeJS/about_nodejs.md#node-js%EB%9E%80">Node JS란?</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NodeJS/about_nodejs.md#node-js-%ED%83%84%EC%83%9D-%EB%B0%B0%EA%B2%BD">Node JS 탄생 배경</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NodeJS/about_nodejs.md#npm-node-package-manager-%EC%9D%B4%EB%9E%80">NPM (Node Package Manager) 이란?</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NodeJS/about_nodejs.md#node-js--npm-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0">Node JS & NPM 설치하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/NodeJS/about_nodejs.md#%EC%9C%A0%EC%9A%A9%ED%95%9C-npm-%EB%AA%85%EB%A0%B9%EC%96%B4">유용한 NPM 명령어</a>

<br/><br/>

## Node JS란?

- Node JS란 Chrome V8 JavaScript 엔진으로 빌드된 JavaScript 런타임(실행 환경)이다.

  - 실행 환경 : 특정 프로그램을 실행하기 위해서 필요한 환경

  - JavaScript 실행 환경 : JavaScript를 실행할 수 있도록 해주는 환경  
    (JavaScript 엔진 + 파일 읽고 쓰는 기능 + 입출력 기능 등등)

- Node JS란 (V8 엔진으로 빌드된) <strong>단순한 문자의 나열인 JavaScript 코드를 해석하고 실행할 수 있도록 제공된 환경</strong>이다.

<br/>

### Node JS 탄생 배경

- 웹 브라우저는 대표적인 JavaScript의 실행환경이다.

- 애초에 JavaScript 언어는 브라우저에서 간단한 스크립트를 실행하기 위해 탄생한 언어이다.

- 그렇기 때문에, JavaScript는 브라우저 이외의 실행 환경이 필요로 하지 않았다.

<br/>

- 하지만, 웹 개발 시장이 커지게 됨에 따라 JavaScript를 다룰 수 있는 웹 개발자가 늘어났고

- 브라우저 외부 환경에서 구동되는 애플리케이션을 구현할 때 굳이 다른 언어를 사용하는 대신 JavaScript 언어만으로 개발을 하고자 하는 (개발자들의) 니즈가 생기게 되었다.

- 즉, 브라우저 외부에서도 JS를 동작할 수 있는 실행 환경이 필요해졌다.

<br/>

- 그 결과, 브라우저가 아닌 환경에서 JS를 실행할 수 있게 해주는 실행환경인 Node.js가 탄생하였다.

<br/><br/>

## NPM (Node Package Manager) 이란?

- Node로 실행할 수 있는 패키지(JS 파일 묶음)들을 관리하는 도구이다.

- NPM을 통해 필요항 패캐지를 다운로드 받고, 업데이트 하고, 삭제할 수 있다.

<br/>

- 비유

  - Node JS : 스마트폰 (엡을 실행할 수 있는 환경)

  - 패키지 : 애플리케이션

  - NPM : 앱 스토어

<br/><br/>

## Node JS & NPM 설치하기

- Node JS 홈페이지에 접속하여 Node JS를 설치한다.

  - 패캐지 호환성을을 고려하여 LTS 버전을 설치하는 것이 좋다.

  - Node JS를 설치하면 NPM은 자동으로 설치된다.

<br/>

- 제대로 설치 되었는지 확인하는 방법

  - 터미널을 실행하여 다음 두 명령어를 순서대로 입력한다.

    ```
    node --version
    ```

    ```
    node --version
    ```

    - 오류가 발생하지 않고 버전이 나온다면 잘 설치된 것이다.

<br/>

## 유용한 NPM 명령어

- <code>npm install</code> : package.json의 dependencies 항목을 분석해서 필요한 패캐지들을 모두 설치해주는 명령어

  - NPM으로 설치한 패키지의 소스파일(node_modules에 없음)은 직접 수정할 수도 없고 깃으로 관리하기엔 용량이 너무 크다. 따라서 <code>.gitignore</code>에 등록하여 git으로 관리하지 않도록 설정해준다.

  - 이러면, 만일 같이 작업하는 다른 사람이 git clone을 통해 코드를 가져올 경우 패키지 소스 파일을 가져올 수 없는 문제가 생긴다. 이때 이 명령어를 입력해주면 된다.

<br/>

- npx 명령어 : 해당 패키지를 실행하겠다는 의미이다.
