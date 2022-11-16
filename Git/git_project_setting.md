# Git - CRA를 통해 (팀) 프로젝트 초기 세팅하기

> 참고 자료 : 공식 문서, 부트캠프 학습 자료

<br/>

### 목차

- <a href="">0. 사전 작업</a>

- <a href="">1. CRA 패키지 설치</a>
- <a href="">2. Third-Party Library Setting</a>
- <a href="">3. 폴더 구조 생성 (폴더 및 파일 구성) 및 <code>.gitignore</code> 세팅</a>
- <a href="">4. 초기 세팅 완료 후 원격 저장소로 push</a>

<br/><br/>

## 0. 사전 작업

- 프로젝트를 진행할 공용 레포지토리를 깃허브에 생성한다.

- 팀원 한 명이 대표로 초기 세팅을 진행하기 위해, 생성한 공용 레포지토리를 자신의 로컬 저장소와 연결한다.

  - 명령어 : <code>git remote add origin [원격저장소 URL]</code>

<br/>

- 그 후 로컬 저장소에 아래의 과정에 따라 초기 세팅을 진행하면 된다.

<br/><br/><br/>

## 1. CRA 패캐지 설치

- 우선 <code>npx create-react-app [프로젝트명]</code> 명령어를 입력하여 CRA 패키지를 설치한다.

- 프로젝트 폴더가 생성되면, 이 곳으로 이동한 후 폴더 및 패키지 세팅을 진행한다.

<br/><br/><br/>

## 2. Third-Party Library Setting

- Routing

  - 라우팅 기능을 설치하기 위해, 많이 사용되고 있는 react-router-dom을 설치한다.

    ```
    npm install react-router-dom
    ```

<br/>

- Styling

  - 스타일링을 위해, SASS와 styled-components 중 각 프로젝트에 필요한 라이브러리를 선택해 설치한다.

    ```
    npm install sass
    ```

    ```
    npm install styled-components styled-reset
    ```

<br/><br/>

### ESLint / Prettier / Stylelint

- VS Code의 Extensions에서 ESLint, Prettier, Stylelint(v1.2.3)를 모두 설치한다.

<br/>

#### npm 패키지

```
# 1. prettier eslint-prettier configuration
$ npm install -D prettier eslint-config-prettier eslint-plugin-prettier

# 2. stylelint with scss, prettier 패키지 설치
$ npm install -D stylelint stylelint-scss stylelint-config-prettier-scss

# 3. 추가 config 패키지 설치 (recommended rules, smacss property sort order)
$ npm install -D stylelint-config-recommended-scss stylelint-config-property-sort-order-smacss

```

<br/>

- 설치 후 제대로 설치되었는지 확인

  ```json
  // package.json

  "eslintConfig": {
    "extends": "react-app",
    ...
  }
  ```

  ```json
  // package.json

  "dependencies": {
      "@testing-library/jest-dom": "^5.16.5",
      "@testing-library/react": "^13.4.0",
      "@testing-library/user-event": "^13.5.0",
      "react": "^18.2.0",
      "react-dom": "^18.2.0",
      "react-router-dom": "^6.4.1",
      "react-scripts": "5.0.1",
      "sass": "^1.55.0",
      "web-vitals":"^2.1.4"
  },
  "devDependencies": {
      "eslint-config-prettier": "^8.1.0",
      "eslint-plugin-prettier": "^3.4.1",
      "prettier": "^2.7.1",
      "stylelint": "^14.13.0",
      "stylelint-config-prettier-scss": "^0.0.1",
      "stylelint-config-property-sort-order-smacss": "^9.0.0",
      "stylelint-config-recommended-scss": "^7.0.0",
      "stylelint-scss": "^4.3.0",
  },
  ```

  <br/>

- <strong>각 패키지에 대한 설명</strong>

  - prettier

    - ESLint 등 코드 포맷터의 설정에 맞게 코드 스타일을 자동으로 맞춰주기 위해서 사용하는 패키지

  - eslint-config-prettier

    - prettier와 출돌하는 eslint규칙을 비활성화하는 패키지

  - eslint-plugin-prettier
    - prettier를 eslint 규칙으로 실행하고 차이점을 eslint에게 전달하는 패키지
  - stylelint
    - stylelint 사용을 위해 설치해야할 기본 패키지
  - stylelint-scss
    - .scss 파일을 linting 하기 위해 설치해야할 패키지
  - stylelint-config-prettier-scss
    - prettier와 충돌되는 stylelint규칙을 비활성화하는 패키지
  - stylelint-config-recommended-scss

    - stylelint에서 표준으로 제공하는 scss규칙 패키지 둘 중 하나 선택하여 설치 recommended가 느슨한 rule

  - stylelint-config-standard-scss

    - standard가 엄격한 rule

  - stylelint-config-property-sort-order-smacss

    - recommended style property sort order를 지원하는 패키지

    - (style property sort order는 smacss, rational, recess 등이 있습니다. 각 팀의 컨벤션에 맞추어 설정해주면 된다)

<br/><br/>

#### 추천 세팅

- 다양한 설정파일이 존재할 때에는 차례대로 적용한 뒤 마지막에 적용되는 설정이 최종적으로 적용되기 때문에 settings.json → .editorconfig → .prettierrc 순서로 설정이 적용됩니다. 아래 설정들은 자동으로 포맷팅 하기 위한 최소한의 사항일 뿐이기 때문에 팀 컨벤션에 따라 원하는 옵션을 추가하거나, 빼도 무방합니다. 더 자세한 내용은 공식문서에 잘 나와 있으니 참고해 보세요. settings.json, .eslintrc, .prettierrc, .stylelint 파일을 아래와 같이 프로젝트 루트 폴더에 생성하고 내용을 기입하면, 프로젝트에 한해서, 해당 설정이 우선으로 적용됩니다.

<br/>

- <strong><code>.vscode/settings.json</code></strong>

  - 프로젝트 최상위에 .vscode 폴더를 생성하여, settings.json 파일을 만들어 아래의 코드를 입력해주세요.

    ```json
    // .vscode/settings.json

    {
      "editor.defaultFormatter": "esbenp.prettier-vscode",
      "editor.tabSize": 2,
      "editor.insertSpaces": true,
      "editor.formatOnSave": true,
      "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true,
        "source.fixAll.stylelint": true
      },
      "css.validate": false,
      "scss.validate": false,
      "stylelint.validate": ["css", "scss", ".module.scss"],
      "stylelint.enable": true,
      "javascript.format.enable": false,
      "eslint.alwaysShowStatus": true,
      "files.autoSave": "onFocusChange"
    }
    ```

<br/>

- <strong><code>.eslintrc</code></strong>

  - 프로젝트 최상위에 .eslintrc 파일을 만들어 아래의 코드를 입력해주세요. 팀원이 모두 맥 유저일 경우와, 그렇지 않은 경우의 세팅이 다르니 확인 후에 적용해주세요.

    - 팀원이 모두 맥 유저일 경우

      ```json
      // .eslintrc

      {
        "extends": ["react-app", "plugin:prettier/recommended"],
        "rules": {
          "no-var": "warn", // var 금지
          "no-multiple-empty-lines": "warn", // 여러 줄 공백 금지
          "no-console": ["warn", { "allow": ["warn", "error"] }], // console.log() 금지
          "eqeqeq": "warn", // 일치 연산자 사용 필수
          "dot-notation": "warn", // 가능하다면 dot notation 사용
          "no-unused-vars": "warn", // 사용하지 않는 변수 금지
          "react/destructuring-assignment": "warn", // state, prop 등에 구조분해 할당 적용
          "react/jsx-pascal-case": "warn", // 컴포넌트 이름은 PascalCase로
          "react/no-direct-mutation-state": "warn", // state 직접 수정 금지
          "react/jsx-no-useless-fragment": "warn", // 불필요한 fragment 금지
          "react/no-unused-state": "warn", // 사용되지 않는 state
          "react/jsx-key": "warn", // 반복문으로 생성하는 요소에 key 강제
          "react/self-closing-comp": "warn", // 셀프 클로징 태그 가능하면 적용
          "react/jsx-curly-brace-presence": "warn" // jsx 내 불필요한 중괄호 금지
        }
      }
      ```

    - 팀원 중 윈도우 유저가 있을 경우

      ```json
      // .eslintrc

      {
        "extends": ["react-app", "plugin:prettier/recommended"],
        "rules": {
          "no-var": "warn", // var 금지
          "no-multiple-empty-lines": "warn", // 여러 줄 공백 금지
          "no-console": ["warn", { "allow": ["warn", "error"] }], // console.log() 금지
          "eqeqeq": "warn", // 일치 연산자 사용 필수
          "dot-notation": "warn", // 가능하다면 dot notation 사용
          "no-unused-vars": "warn", // 사용하지 않는 변수 금지
          "react/destructuring-assignment": "warn", // state, prop 등에 구조분해 할당 적용
          "react/jsx-pascal-case": "warn", // 컴포넌트 이름은 PascalCase로
          "react/no-direct-mutation-state": "warn", // state 직접 수정 금지
          "react/jsx-no-useless-fragment": "warn", // 불필요한 fragment 금지
          "react/no-unused-state": "warn", // 사용되지 않는 state
          "react/jsx-key": "warn", // 반복문으로 생성하는 요소에 key 강제
          "react/self-closing-comp": "warn", // 셀프 클로징 태그 가능하면 적용
          "react/jsx-curly-brace-presence": "warn", // jsx 내 불필요한 중괄호 금지
          "prettier/prettier": [
            "error",
            {
              "endOfLine": "auto"
            }
          ]
        }
      }
      ```

<br/>

- <strong><code>.prettierrc</code></strong>

  - 프로젝트 최상위에 .prettierrc 파일을 만들어 아래의 코드를 입력해주세요.

    ```json
    // .prettierrc

    {
      "tabWidth": 2,
      "endOfLine": "lf",
      "arrowParens": "avoid",
      "singleQuote": true
    }
    ```

<br/>

- <strong><code>.stylelintrc.js</code></strong>

  - 프로젝트 최상위에 .stylelintrc.js 파일을 만들어 아래의 코드를 입력해주세요.

    ```js
    // .stylelintrc.js

    module.exports = {
      extends: [
        "stylelint-config-recommended-scss",
        // scss standard rule 적용 (recommended로 설치했다면 recommended로 standard로 설치 했다면 standard로 입력해주세요)
        "stylelint-config-prettier-scss",
        // prettier와 충돌하는 부분을 해결
        "stylelint-config-property-sort-order-smacss", // SMACSS 기반으로 속성 정렬
      ],
      plugins: ["stylelint-scss"], // scss 문법을 위한 플러그인
      ignoreFiles: ["src/styles/reset.scss", "src/styles/common.scss"], // reset과 common scss는 ignore합니다.
      rules: {
        "at-rule-no-unknown": null,
        // scss를 사용하기 때문에 css영역에선 null로 처리합니다.
        "selector-class-pattern": "^([a-z][a-z0-9]*)(-[a-z0-9]+)*$",
        // Team내 컨벤션으로 수정 (현재 kebab-case)
        "keyframes-name-pattern": /^([a-z][a-z0-9]*)(-[a-z0-9]+)*$/,
        // Team내 컨벤션으로 수정 (현재 kebab-case)
        "max-nesting-depth": 3, // 최대 nesting은 3depth 까지
        "no-descending-specificity": null,
        "string-quotes": "single", // single quotes
        "scss/at-rule-conditional-no-parentheses": null,
        // 조건부 @ 규칙(if, elsif, while)(자동 수정 가능)에서 괄호를 허용합니다.
      },
    };
    ```

<br/><br/><br/>

## 3. 폴더 구조 생성 (폴더 및 파일 구성) 및 <code>.gitignore</code> 세팅

- 폴더 구조 예시

  <img src="img/git_project_folder_tree.png">

<br/><br/>

### 각 폴더의 역할

- (준비 중) (<a href="https://study.wecode.co.kr/session/content/301">여기 참고</a>)

<br/><br/>

### <code>.gitignore</code> 세팅

```
# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*

.eslintcache
```

<br/><br/><br/>

## 4. 초기 세팅 완료 후 원격 저장소로 push

- 위의 모든 과정이 끝났으면 원격 저장소로 push한다.

- 다른 팀원들은 각자의 로컬 저장소에서 초기 세팅이 완료된 폴더 구조를 pull 한 후, 각자 맡은 기능에 따른 브랜치를 생성해서 작업을 시작하면 된다.

- 이제 main 브랜치는 더 이상 커밋을 통해 직접 수정되선 안 되고, 다른 브랜치와의 병합을 통해서만 수정되여야 한다.
