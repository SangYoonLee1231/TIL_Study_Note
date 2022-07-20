# CSS - 조각 지식 모음

<br/>

- CSS와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#%EC%95%84%EC%9D%B4%EC%BD%98-%EC%82%BD%EC%9E%85%ED%95%98%EA%B8%B0---font-awesome">아이콘 삽입하기 - <a href="https://fontawesome.com/">Font Awesome</a></a>
- <a href="">HTML에 CSS 파일을 연결하기 위해 작성하는 link 태그 단축기</a>
- <a href="">Reset CSS</a>
- <a href="">CSS 변수 선언 및 사용</a>
- <a href="">not 속성 (부정 CSS 가상 클래스)</a>
- <a href="">Border Box</a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

### 아이콘 삽입하기 - <a href="https://fontawesome.com/">Font Awesome</a>

- 아이콘 삽입 방법 (2가지)

  - 직접 이미지 아이콘 추가
  - SVG (픽셀이 없는 이미지 파일 형식)

- 아이콘 모음 사이트 추천

  - <a href="https://heroicons.dev/">Heroicons [Heroicons - Free Open Source SVG Icon Library]</a>

  - <a href="https://fontawesome.com/">Fontawesome [Font Awesome]</a>

<br/>

- Font Awesome에서 폰트 및 아이콘을 사용하려면 Code Kit이 필요하다.

  (Code Kit은 JavaScript 파일이다.)

  ```html
  <!-- 니꼬샘이 주신 무료 버전 Code Kit -->
  <script
    src="https://kit.fontawesome.com/6478f529f2.js"
    crossorigin="anonymous"
  ></script>
  ```

  - 무료 버전 Code Kit이기 때문에, 버전은 5.15.4로 낮추고 icon을 검색해야 정상적으로 icon이 잘 뜬다.

<br/><br/>

### HTML에 CSS 파일을 연결하기 위해 작성하는 link 태그 단축기

- head 태그 내부에 <code>link:css</code>라 직성하면 된다.

<br/><br/>

### Reset CSS

- 브라우저에 의해 HTML에 자동으로 적용되는 스타일을 무시하도록 하는 코드

- 대부부분의 태그에 <code>margin:0</code>, <code>padding:0</code>, <code>border:0</code> 등을 가진 css 파일

<br/>

- reset.css (<a href="https://meyerweb.com/eric/tools/css/reset/">출처</a>)

  ```css
  /* http://meyerweb.com/eric/tools/css/reset/ 
  v2.0 | 20110126
  License: none (public domain)
  */

  html,
  body,
  div,
  span,
  applet,
  object,
  iframe,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  p,
  blockquote,
  pre,
  a,
  abbr,
  acronym,
  address,
  big,
  cite,
  code,
  del,
  dfn,
  em,
  img,
  ins,
  kbd,
  q,
  s,
  samp,
  small,
  strike,
  strong,
  sub,
  sup,
  tt,
  var,
  b,
  u,
  i,
  center,
  dl,
  dt,
  dd,
  ol,
  ul,
  li,
  fieldset,
  form,
  label,
  legend,
  table,
  caption,
  tbody,
  tfoot,
  thead,
  tr,
  th,
  td,
  article,
  aside,
  canvas,
  details,
  embed,
  figure,
  figcaption,
  footer,
  header,
  hgroup,
  menu,
  nav,
  output,
  ruby,
  section,
  summary,
  time,
  mark,
  audio,
  video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
  }
  /* HTML5 display-role reset for older browsers */
  article,
  aside,
  details,
  figcaption,
  figure,
  footer,
  header,
  hgroup,
  menu,
  nav,
  section {
    display: block;
  }
  body {
    line-height: 1;
  }
  ol,
  ul {
    list-style: none;
  }
  blockquote,
  q {
    quotes: none;
  }
  blockquote:before,
  blockquote:after,
  q:before,
  q:after {
    content: "";
    content: none;
  }
  table {
    border-collapse: collapse;
    border-spacing: 0;
  }
  ```

<br/><br/>

### CSS 변수 선언 및 사용

- variables.css (변수 선언)

  ```css
  :root {
    --yellow: #fae100;
  }
  ```

- styles.css (변수 사용)

  ```css
  @import "variables.css";

  body {
    color: var(--yellow);
  }
  ```

- variables.css 파일을 반드시 import 해주어야 하는 것을 잊지 말자.

<br/><br/>

### not 속성 (부정 CSS 가상 클래스)

- 특정 선택자가 없을 때에 대한 스타일 처리를 하고자 할 때 사용한다.

- <code>:not()</code> 형태로 쓰는 가상 클래스 개념이다.

- <code>:not(X)</code> 은 임의 요소 X가 아닌 모든 요소와 일치한다.

<br/>

- 사용 예시

  ```css
  .login-form input:not([type="submit"]) {
    ...;
  }
  ```

<br/><br/>

### Border Box
