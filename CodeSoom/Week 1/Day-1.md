# Day 1 (2022.08.01) TIL

<br/>

## 배운 것 (목차)

### 【1】 Node.js

- Node.js의 간단한 개념

- Node.js 설치하기

<br/>

### 【2】 npm

- npm의 간단한 개념

- 코드숨 전용 디렉토리 생성 및 npm 프로젝트 생성

- npm 설치 명령어 (+ 지역 설치 vs 전역 설치, 개발용 vs 배포용)

- npm 버전 관리 (자세히 학습하진 않았음)

- npm 커스텀 명령어

<br/>

### 【3】 Webpack

- Webpack 개념을 이해하기 위한 사전 지식 학습 (모듈, 모듈 번들러)

- JS 모듈화의 배경

- Webpack 사용 이유 (4가지)

  - 변수 범위로 인해 의도치 않게 변수 값이 변경되는 문제 (모듈로 관리 시)  
     => JS 변수 유효 범위 문제 해결 (By ES6 모듈 문법)

  - HTTP 요청 수 제한 문제 해결

  - 자동 새로고침 가능 (여러 모듈을 자동으로 묶어서 업뎃)  
     => 웹 개발 작업 자동화 도구

  - 웹 애플리케이션의 빠른 로딩 속도와 높은 성능 확보 (By 파일 압축 병합, Code Splitting , ..etc)

<br/>

### 【4】 Webapck 설치 (+ npm 명령어 익숙해지기)

- npm 명령어 정리

  - <code>npm init (-y)</code> : NPM 프로젝트 생성하여 package.json 생성 (-y : 개별 설정 X)

  - <code>npm install</code> : NPM 의존성 추가 (NPM 패키지 설치)

  - <code>npx serve</code> : 웹서버를 띄우는 (가장) 쉬운 방법

  - <code>^C (컨트롤 + C)</code> : 나가짐

  - <code>npx webpack serve --mode development</code> : 개발용 서버 실행

    - Cannot GET / 에러 때문에 좀 고생했으나, 전 기수의 채널을 참고해서 해결! (<code>/public/index.html</code> 경로로 수정)

- 정상 동작 확인!

<br/>

### 【5】 EsLint

<br/>

### 【6】 Git Training - PR 연습

- (지금껏 GitHub Desktop을 사용해 커밋을 해왔기에 깃 명령어에 익숙치 않음 + PR 경험 X)

<br/><br/>

## 과제 진행
