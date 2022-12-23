# React JS - <code>react-router</code>를 적용한 React 앱을 <strong>webpack</strong>으로 빌드하고 <strong>Github Page</strong>로 배포하기

> 참고 자료 : <a href="https://medium.com/@_diana_lee/react-react-router-적용한-react-앱을-github-pages로-배포하는-법-5f6119c6a5d9">[React] react-router 적용한 React 앱을 github pages로 배포하는 법 (블로그 포스트)</a>, <a href="https://velog.io/@y0ungg/React-웹팩으로-빌드하고-깃허브-배포하기">[React] 웹팩으로 빌드하고 깃허브 페이지 배포하기 (블로그 포스트)</a>

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## 사전 작업

- <code>gh-pages</code> 패키지를 설치한다.

  ```
  npm install gh-pages
  ```

- <code>package.json</code>의 scripts 객체 안에 아래의 코드를 작성해준다.

  ```json
  "scripts": {
    ...
    "build": "webpack --config webpack.config.js",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build",
  },
  ```

<br/><br/>

## Webpack 설정

- <code>webpack.config.js</code>

  ```js
  const path = require("path");
  const HtmlWebpackPlugin = require("html-webpack-plugin");

  module.exports = {
    mode: "development", // 또는 production

    ...

    module: {
      //loaders
      rules: [

        ...

    },
    plugins: [
      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, "./index.html"), //template도 꼭 작성해야 함!!
      }),
    ],
    output: {
      path: path.resolve(__dirname, "docs"), //깃허브 페이지 배포를 위해 docs로 설정해주었다.
      filename: "app.js",
    },
  };
  ```

<br/>

#### 깃허브 배포하기

- <code>npm deploy</code>를 하거나, 깃허브 홈페이지에 가서 [Settings] -> [Pages] -> 'main 브랜치' '/docs 옵션'으로 설정 후 Save 한다.

- <code>npm run build</code>를 한다. 그럼 output의 path에 번들 파일이 저장된다.

- output path를 docs로 설정하고 해당 폴더를 포함하여 깃허브 레포지토리에 push한다. (pages 배포 옵션을 반드시 /docs로 설정해야 한다)

<br/><br/>

## <code>react-router</code> 설정

- <code>package.json</code>에 <code>homepage</code> 필드를 추가한다.

  ```json
  // package.json
  {
    "homepage": "http://SangYoonLee1231.github.io/ERROR_NOTE"
  }
  ```

- BrowserRouter에 <code>basename</code>을 추가한다.

  ```js
  <BrowserRouter basename={process.env.PUBLIC_URL}>
    <Nav />
    <Aside />
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/content/:category" element={<Content />} />
    </Routes>
  </BrowserRouter>
  ```

  - 이 <code>basename</code> props는 프로젝트의 기본 URL을 설정해주는 역할을 한다.

  - Router에게 기본 URL을 제공하여 "<code>/</code>"이 아닌 리포지토리 주소 "<code>/ERROR_NOTE/</code>"로 이동하도록 지시하여 라우팅 오류를 미리 방지해준다.

  - PUBLIC_URL은 <code>package.json</code>의 <code>homepage</code> URL값으로 설정된다.
