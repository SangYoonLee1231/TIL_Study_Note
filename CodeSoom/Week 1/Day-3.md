# 1주차 Day 3 TIL

#### 2022.08.03

<br/>

## 오늘 한 것 (+ 학습한 것)

### 【1】 Babel + JSX

- <strong>Babel이란?</strong>

    - 브라우저마다 사용하는 언어가 달라 발생하는 크로스브라우징 이슈를 해결하기 위해, 스크립트를 모든 브라우저에서 동작할 수 있는 코드로 '트랜스파일'해주는 장치

        - 트랜스파일 : 추상화 수준이 같은 코드로 변환해주는 것 (vs 빌드)

    - ECMAScript2015 이상의 코드를 적당한 하위 버전으로 변환

    - TypeScript나 JSX도 Babel의 변환 대상이다.

<br/>

- <strong>Babel 설치</strong>

    - <strong>그 외 설치 명령어</strong>

        - <code>npm i -D babel-loader</code> : Webpack에서 Babel을 쓸 수 있도록 도와줌
        - <code>webpack.config.js</code> 파일 : webpack 설정 파일
        - <code>npm i -D @babel/core npm i</code> 
        - <code>npm i -D @babel/preset-env @babel/preset-react</code>

    - <strong>config 설정</strong>

        - <code>webpack.config.js</code>

            ```javascript
            module.exports = {
                mode: 'development',
                module: {
                    rules: [{
                        test: /\.(js|jsx)?$/,
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env', '@babel/preset-react'],
                        },
                    }],
                },
                resolve: { extensions: ['.js', '.jsx'] },
            };

            ```

        - <code>babel.config.js</code>

            ```javascript
            module.exports = {
                presets:
                [
                    [
                        '@babel/preset-env',
                        {
                            targets: {
                                node: 'current',
                                chrome: '79',
                            },
                        },
                    ],
                    '@babel/preset-react',
                ],
            };
            ```
    <br/>

    - <strong>에러 발생!</strong> - Babel을 설치했음에도 index.js 파일에서 

        - <strong>해결</strong> : 알고보니 소괄호 대신 중괄호를 써서 생긴 오류였다.

            ```javascript
            // 이렇게 말이다
            const element = {
                <div>
                    <p>Hello World!</p>
                </div>
            };

            // 이렇게 했어야 했는데
            const element = (
                <div>
                    <p>Hello World!</p>
                </div>
            );
            ```

    <br/>

    - 😰 <strong>총체적 난국</strong>

        - jsx가 <code>.js</code>에 적용이 되지 않아 Stack Overflow를 통해 해결했다. (<a href="https://stackoverflow.com/questions/43031126/jsx-not-allowed-in-files-with-extension-js-with-eslint-config-airbnb/49505827#49505827">도움받은 질문글</a>)

        - 그랬더니 이젠 <code>src/index.js</code>의 변경사항이 Webpack에 의해 실시간으로 반영이 되지 않는다. (정확히 말하면 반영은 되는데 <code>[webpack-dev-server] Nothing changed.</code>문구가 뜨고 콘솔에 결과가 출력되지 않는다)

        - 이쯤되니 뭘 어떻게 해야할 지 모르겠다.

        - 그래서 <strong>폴더 안 내용을 싹 지우고 개발 환경 설치부터 전부 다시 하기로 했다.</strong>
        
<br/><br/>

### 【2】 개발 환경 세팅부터 재진행

<br/><br/>

### Git Training - PR 연습 (내일로)

- (지금껏 GitHub Desktop을 사용해 커밋을 해왔기에 깃 명령어에 익숙치 않음 + PR 경험 X)