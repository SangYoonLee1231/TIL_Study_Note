# 1주차 Day 1 TIL

#### 2022.08.01

<br/>

## 배운 것 (간략히 정리)

### 【1】 Node.js

- <strong>Node.js의 간단한 개념</strong>

  - 웹 브라우저가 아닌 외부 환경에서도 JS를 실행할 수 있도록 하는 환경

  - Chrome V8 JS Engine으로 빌드되었다.

<br/>

- <strong>Node.js 설치하기</strong>

  - LTS 버전으로 설치 + 터미널에서 정상적으로 설치되었는지 확인

<br/><br/>

### 【2】 NPM

- <strong>NPM의 간단한 개념</strong>

  - JS 라이브러리 설치 및 관리 역할 (패키지 매니저)

<br/>

- <strong>코드숨 전용 디렉토리 생성 및 npm 프로젝트 생성</strong>

  - 터미널에서 코드숨 전용 디렉토리로 이동한 후 아래 npm 명령어 실행

    - <code>npm init (-y)</code> : NPM 프로젝트 생성하여 package.json 생성 (-y : 개별 설정 X)

    - <code>npm install [이름]</code> (<code>npm i [이름]</code>) : NPM 의존성 추가 (NPM 패키지 설치)

<br/>

- <strong>NPM 지역 설치 vs 전역 설치</strong>

  - NPM 지역 설치 : 프로젝트 레벨에서 사용할 라이브러리 설치

    - <code>npm install [이름] (--save prod 또는 --save-dev)</code> (--save prod는 배포용, --save-dev는 개발용)

  - NPM 전역 설치 : 시스템 레벨에서 사용할 라이브러리 설치

    - <code>npm install [이름] (--global 또는 -g)</code>

    - 라이브러리 설치 후, 라이브러리 이름은 이제 명령어로 인식됨

<br/>

- <strong>NPM 개발용 라이브러리 vs 배포용 라이브러리</strong>

  - 개발용 : 배포시 라이브러리 적용 X

    - <code>npm install [이름] -D</code>

  - 배포용 : 배포시 라이브러리 적용 O

    - <code>npm install [이름]</code>

<br/>

- <strong>npm 버전 관리</strong> (자세히 학습하진 않았음)

  - 유의적 버전 : 버전 번호의 관리 체계 (주.부.수)

<br/>

- <strong>npm 커스텀 명령어</strong>

  - 사용자가 패키지 관리 파일(<code>package.json</code>)에서 직접 정의하여 쓰는 npm 명령어

  - 사용 예시

    ```javascript
    //package.json
    {
        ...
        "server" : "npx webpack serve --mode development"
    }
    ```

    ```sh
    npm run server
    ```

    - 긴 명령어를 단축하여 쓸 때 유용하다.

<br/><br/>

### 【3】 Webpack

- Webpack 개념을 이해하기 위한 사전 지식 학습 (<strong>모듈</strong>, <strong>모듈 번들러</strong>)

  - 모듈 : 특정한 기능을 수행하는 코드 묶음 단위. 비슷한 기능을 하는 코드를 하나의 파일로 묶은 것.

    - 웹에서의 모듈 : 웹 애플리케이션을 구성하는 모든 자원(파일)

  - 모듈 번들러 : 여러 모듈을 하나로 묶는(병합 및 압축하는) 동작

<br/>

- <strong>JS 모듈화의 배경</strong>

  - 주로 작은 기능만을 수행했던 초창기 JS 프로그램과 달리, 시간이 지날수록 JS 프로그램이 더 많은 기능을 수행하게 되었다.

  - 그에 따라 필요한 기능을 그때그때 가져오도록 하기 위하여 스크립트를 기능별로 분할해서 관리할 필요성이 대두되었다.

  - 브라우저에선 ES2015부터 모듈을 지원해주기 시작했다. Webpack은 이러한 모듈을 하나로 합쳐주는 역할을 수행하는 모듈 번들러이다.

<br/>

- <strong>Webpack 사용 이유 (4가지)</strong>

  - 모듈로 관리되는 스크립트의 변수 범위로 인해 의도치 않게 변수 값이 변경되는 문제 해결
    => JS 변수 유효 범위 문제 해결 (By ES6 모듈 문법)

  - HTTP 요청 수 제한 문제 해결

  - 자동 새로고침 가능 (여러 모듈을 자동으로 묶어서 업데이트 수행)  
     => 웹 개발 작업 자동화 도구

  - 웹 애플리케이션의 빠른 로딩 속도와 높은 성능 확보 (By 파일 압축 병합, Code Splitting , etc..)

<br/><br/>

### 【4】 Webapck 설치 (+ npm 명령어 익숙해지기)

- <strong>npm 명령어에 익숙해지기 위해 정리하였다.</strong>

  - <code>npm init (-y)</code> : NPM 프로젝트 생성하여 package.json 생성 (-y : 개별 설정 X)

  - <code>npm install</code> : NPM 의존성 추가 (NPM 패키지 설치)

  - <code>npx serve</code> : 웹서버를 띄우는 (가장) 쉬운 방법

  - <code>^C (컨트롤 + C)</code> : 나가짐

  - <code>npx webpack serve --mode development</code> : 개발용 서버 실행

    - Cannot GET / 에러 때문에 좀 고생했으나, 전 기수의 채널을 참고해서 해결! (<code>/public/index.html</code> 경로로 수정)

<br/>

- <strong>정상 동작 확인!</strong>

<br/><br/>

### 【5】 ESLint

- 개발팀 내에서 원할한 협업을 위해 코드 스타일을 하나로 통일하기 위한 도구중 하나

- <strong>ESLint 설치 및 초기화</strong>

  - <code>npm i -D eslint</code> : 개발자 모드로 ESLint 설치

  - 추가로 VS Code에서 ESLint 확장 프로그램을 설치하면 자동 실행 기능을 이용할 수 있다.

  - <code>npm init @eslint/config</code> : ESLint 초기화 및 초기 설정

    (<code>npx eslint --init</code> 명령어로 입력했더니 <code>ReferenceError: primordials is not defined</code> 오류 발생)

<br/><br/>

### 【6】 Git Training - PR 연습

- (지금껏 GitHub Desktop을 사용해 커밋을 해왔기에 깃 명령어에 익숙치 않음 + PR 경험 X)

<br/><br/>

## 과제 진행

(진행 X)
