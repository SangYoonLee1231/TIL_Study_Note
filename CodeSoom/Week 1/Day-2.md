# 1주차 Day 2 TIL

#### 2022.08.02

<br/>

## 배운 것 (간략히 정리)

### 【1】 ESLint (마무리)

- <code>ReferenceError: primordials is not defined</code> 오류 해결

    - NVM으로 Node와 NPM 버전을 계속 바꿔봐도 오류 여전히 발생

    - 그래서 수동으로 코드를 삽입하기로 결정

    - <a href="https://triplexlab.tistory.com/40">해당 포스트</a>에서 <code>.eslintrc.js</code> 코드를 복붙하였으나 실패

    - <code>npx eslint src/index.js</code> 명령어 입력 시 뜨는 터미널 에러 메세지를 관찰하다가 <strong>해결 방법을 찾음</strong>

    - 아래의 5개의 명령어를 입력해 수동 설치 함
        
        - <code>npm install eslint-config-airbnb</code>

        - <code>npm install eslint-plugin-react</code>

        - <code>npm install eslint-plugin-jsx-a11y@latest --save-dev</code>

        - <code>npm install eslint-plugin-import@latest --save-dev</code>

    - <strong>드디어 정상 작동함.</strong>

    <br/>

    - ESLint 관련 유용한 명령어 정리

        - <code>npx eslint [검사할 파일 위치]</code> : 해당 파일을 코드 스타일 검사

        - <code>npx eslint --fix .</code> : 코드 스타일 자동 수정


<br/><br/>

### 【2】 Git Training - PR 연습 (내일로)

- (지금껏 GitHub Desktop을 사용해 커밋을 해왔기에 깃 명령어에 익숙치 않음 + PR 경험 X)