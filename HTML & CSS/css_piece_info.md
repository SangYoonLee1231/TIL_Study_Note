# CSS - 조각 지식 모음

<br/>

- CSS와 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#%EC%95%84%EC%9D%B4%EC%BD%98-%EC%82%BD%EC%9E%85%ED%95%98%EA%B8%B0---font-awesome">아이콘 삽입하기 - <a href="https://fontawesome.com/">Font Awesome</a></a>
- <a href="">HTML에 CSS 파일을 연결하기 위해 작성하는 link 태그 단축기 (VS Code)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#reset-css">Reset CSS</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#css-%EB%B3%80%EC%88%98-%EC%84%A0%EC%96%B8-%EB%B0%8F-%EC%82%AC%EC%9A%A9">CSS 변수 선언 및 사용</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#not-%EC%86%8D%EC%84%B1-%EB%B6%80%EC%A0%95-css-%EA%B0%80%EC%83%81-%ED%81%B4%EB%9E%98%EC%8A%A4">not 속성 (부정 CSS 가상 클래스)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#%EA%B1%B0%EB%A6%AC-%EB%8B%A8%EC%9C%84">거리 단위</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#box-sizing-content-box-border-box">Box Sizing (content-box, border-box)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#css-%EC%84%A0%ED%83%9D%EC%9E%90-selector-%EC%9A%B0%EC%84%A0-%EC%88%9C%EC%9C%84">CSS 선택자 (Selector) 우선 순위</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#background-size-%EC%86%8D%EC%84%B1"><code>background-size</code> 속성</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#width-100%EC%9D%98-%EC%9D%98%EB%AF%B8"><code>width: 100%</code>의 의미</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#css-%EC%86%8D%EC%84%B1-%EC%88%9C%EC%84%9C-%EC%BB%A8%EB%B2%A4%EC%85%98">CSS 속성 순서 (컨벤션)</a>
- <a href=""></a>

<br/><br/>

## 아이콘 삽입하기 - <a href="https://fontawesome.com/">Font Awesome</a>

### 아이콘 삽입 방법 (2가지)

- 직접 이미지 아이콘 추가
- SVG (픽셀이 없는 이미지 파일 형식)

### 아이콘 모음 사이트 추천

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

## HTML에 CSS 파일을 연결하기 위해 작성하는 link 태그 단축기 (VS Code)

- head 태그 내부에 <code>link:css</code>라 직성하면 된다.

<br/><br/>

## Reset CSS

- 브라우저에 의해 HTML에 자동으로 적용되는 스타일 (사용자 에이전트 스타일시트) 을 무시하도록 하는 코드

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

## CSS 변수 선언 및 사용

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

## not 속성 (부정 CSS 가상 클래스)

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

## 거리 단위

- <strong><code>px</code></strong> : 가장 기본적으로 사용되는 픽셀 단위 (고정값)

- <strong><code>em</code></strong> : 부모 요소를 기준으로 자식 요소의 크기를 정하는 것 (배수)

  - <code>1.2em</code> : 부모 요소 기준 1.2배수 크기

- <strong><code>vh</code></strong> : viewport(화면) height

  - <code>100vh</code> : 화면 높이의 100%

- <strong><code>vw</code></strong> : viewport(화면) width

  - <code>100vh</code> : 화면 넓이의 100%

<br/><br/>

## Box Sizing (content-box, border-box)

- <strong><code>box-sizing</code></strong>은 박스의 크기를 계산하는 기준을 설정하는 CSS 속성이다.

  - <code>content-box (Default 값)</code> : 콘탠츠 영역를 기준으로 박스 크기를 계산한다.

  - ✨ <code>border-box</code> : 테두리를 기준으로 박스 크기를 계산한다.

    - 개발 시 거의 항상 쓰이는 속성이라 한다.

      ```css
      * {
        box-sizing: border-box;
      }
      ```

  - <code>initial</code> : 기본값으로 설정한다.

  - <code>inherit</code> : 부모 요소의 속성값을 물려받는다.

<br/>

- 어떤 요소의 크기가 <code>width: 200px</code>이고 <code>padding: 40px</code>이라 하면,

  <code>box-sizing: content-box</code>일 경우, 요소의 크기 (<code>width</code>) 는 <code>280px</code>이고,

  <code>box-sizing: border-box</code>일 경우, 요소의 크기 (<code>width</code>) 는 <code>200px</code>이다.

<br/><br/>

## CSS 선택자 (Selector) 우선 순위

- 점수 계산으로 이루어진다.

  - inline styling (HTML 요소에 style 속성을 주어 작성): <strong>1000점</strong>

  - id명: <strong>100점</strong>

  - class 이름: <strong>10점</strong>

  - tag명: <strong>1점</strong>

<br/>

- 요약

  - <strong>tag &nbsp; << &nbsp; class &nbsp; << &nbsp; id &nbsp; << &nbsp; inline styling</strong>

<br/><br/>

## <code>background-size</code> 속성

- 요소 배경 이미지의 크기를 설정한다. (By MDN)

- 가능한 속성값

  - <code>auto</code>, <code>length</code>, <code>cover</code>, <code>contain</code>, <code>initial</code>, <code>inherit</code> 등

<br/><br/>

## <code>width: 100%</code>의 의미

- 어떤 부모 요소의 크기가 <code>width: 200px</code>일 때, 자식 요소의 크기를 <code>width: 100%</code>로 설정하면
  자식의 요소 너비 또한 <code>200px</code>이 된다.

  ```css
  .father {
    width: 200px;
  }

  .child {
    width: 100%;
  }
  ```

<br/><br/>

## CSS 속성 순서 (컨벤션)

- CSS 속성 작성 순서는 성능 향상이나 적용 순서에 유의미한 영향을 주진 않지만, <strong>가독성</strong>과 <strong>유지보수</strong>를 위해 <strong>인접 속성끼리 묶어서 작성</strong>해주는 것이 좋다.

- <strong>권장 순서</strong>

  - Layout Properties (position, float, clear, display)

  - Box Model Properties (width, height, margin, padding)

  - Visual Properties (color, background, border, box-shadow)

  - Typography Properties (font-size, font-family, text-align, text-transform)

  - Misc Properties (cursor, overflow, z-index)

<br/><br/>

## CSS 레이아웃 작성 방식 (bottom-up)

- 레이아웃을 구성할 때 부모 요소의 높이를 미리 정해두고 자식 요소의 크기를 정하는 top-down 방식이 아닌, 자식 요소의 높이에 따라 부모 요소의 높이가 유동적으로 결정되는 bottom-up 방식으로 구성하는 것이 좋다.

- 자식 요소의 크기에 따라 부요 요소의 크기가 유종적으로 조정되어야 유지보수가 더 쉬워지기 때문이다.

  ```css
  // BAD
  .parent {
    height: 100vh;
  }

  .child {
    height: 300px;
  }

  // GOOD
  .parent {
    padding-top: 20px;
  }

  .child {
    height: 300px;
  }
  ```
