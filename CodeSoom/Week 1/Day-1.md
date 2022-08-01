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

### 【5】 ESLint (진행 중)

- 개발팀 내에서 원할한 협업을 위해 코드 스타일을 하나로 통일하기 위한 도구중 하나

- <strong>ESLint 설치 및 초기화</strong>

  - <code>npm i -D eslint</code> : 개발자 모드로 ESLint 설치

  - 추가로 VS Code에서 ESLint 확장 프로그램을 설치하면 자동 실행 기능을 이용할 수 있다.

  - <code>npm init @eslint/config</code> 또는 <code>npx eslint --init</code> : ESLint 초기화 및 초기 설정

    - <strong>그러나 버전 오류 발생</strong> (<code>ReferenceError: primordials is not defined</code>)

    - 이를 해결하기 위해 노력하다 결국 코드숨 대표님께 문의 => 수동으로 코드 삽입하면 된다는 답변 받음

    - 공식 문서와 공식 GitHub 계정을 열심히 찾아봄 (<a href="https://github.com/eslint/eslint/blob/main/.eslintrc.js">코드</a> 하나를 찾았으나 해결X)

    - 결국 Node와 NPM의 버전을 변경하기로 결정 => NVM 설치 이용

    - NVM exit 1, exit 5 에러 발생 -> 구글링으로 해결

      - exit 1 : 관리자 권한으로 실행

      - exit 5 : 설치 경로에 공백 있으면 안되기에, 삭제 후 바탕화면에 재설치

    - NVM으로 Node와 NPM 버전을 바꿔봤으나 여전히 안됨

      - (Node 기준 안되는 버전 : 16.16.0, 18, 14.17.5)

    - <strong>아직 미해결</strong>

<br/><br/>

## 과제 진행

(진행 하지 못함)

<br/><br/>

## Feeling

- 처음부터 끝까지 다 처음 배우는 내용이라 많이 생소하고 낯설었지만, 그렇기에 많은 것을 배울 수 있어 좋았고 재밌었다.

  하지만 진도가 느려 과제를 커녕 개발환경 구축도 못 끝내고 하루가 끝나버렸다..

- 막판에 알 수 없는 에러로 인해 내 인내심이 많이 시험당했다. 결국 이 문제를 해결하지 못한 채 하루가 끝났다.

  - 적어도 나 외에 이런 문제를 겪은 사람이 이 세상 어딘가엔 있을텐데, 왜 구글링 해도 유용한 정보가 이렇게 안 나오는 거지?

  - 심지어 Stack Overflow에서도 관련 에러에 대한 정보를 거의 찾아볼 수 없었다.  
    (다행이도 이 문제가 '버전 호환성'과 관련된 것이라는 실마리를 얻었지만)

  - 이 문제 때문에 언어 안가리고 공식 문서, 깃허브, 그 외 수많은 페이지를 돌아다니며 해결법을 찾아봤으나 결국 못 찾음.  
    결국 코드숨 대표님께 여쭤봐서 실마리를 하나 더 얻었음. 그럼에도 문제를 해결하진 못헀음.

  - 꼬리에 꼬리를 무는 에러로 인해 오는 고통은 이번에 처음 겪어봤다. (NVM use 오류를 봤을 땐..)

  - 이 정도로 오류 해결에 난항을 겪은 처음이다. 내일이 오면 이 문제를 해결할 수 있을까?

<br/>

- 예상했던 만큼 교육 내용이 쉽지 않았다. 하지만 생각 이상으로 재밌었고 하루 만에 node.js에 가까워진 것 같아 만족스럽다.

- 하지만 여전히 걱정 되는 점은 '내가 제대로 코드 리뷰를 받을 수 있을까', '이 교육을 최대한 잘 활용할 수 있을까', '실력 부족으로 성장의 기회를 계속 놓치게 되는 건 아닐까' 하는 점이다. 

- 게다기 학교에서 진행하는 코딩테스트 대비 캠프 내일부터 시작해 시간이 더 부족하다. 어쩌면 내일도 PR를 날리지 못하는 불상사가 생길 수 있다. 

- 하지만 이럴 때일수롣 위기를 기회로 삼는 마음가짐이 필요하다. 무리하지 않는 선에서 좀 더 최선을 다해보자.
