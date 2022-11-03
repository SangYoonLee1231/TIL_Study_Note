# SASS

<br/>

> 참고 자료 : 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#css-%EC%A0%84%EC%B2%98%EB%A6%AC%EA%B8%B0%EB%9E%80">CSS 전처리기란?</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#sass-syntactically-awesome-style-sheets">SASS (Syntactically Awesome Style Sheets)</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#sass-vs-scss">SASS vs SCSS</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#sass-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0">SASS 적용하기</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#sass-%EB%AC%B8%EB%B2%95">SASS 문법</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#nesting">Nesting</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#%EB%B3%80%EC%88%98">변수</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_sass.md#%EB%B6%80%EB%AA%A8%EC%84%A0%ED%83%9D%EC%9E%90--mixin--optional-arguments">부모선택자 (&), mixin (+ optional arguments)</a>

<br/><br/>

## CSS 전처리기란?

- CSS 문법의 불편함을 개선하고자 나온 기술

- CSS 전처리기의 양식에 맞게 파일을 작성해두면, 실제 실행 전 이를 브라우저가 읽을 수 있는 CSS 파일로 변환해준다.

<br/>

- CSS 전처리기는 여러 종류가 있다. SCSS도 그 중 하나이다.

<br/><br/>

## SASS (Syntactically Awesome Style Sheets)

- SASS 설치 명령어 : <code>npm install sass</code>

- SASS 공식 문서 : 👉 <a href="https://sass-lang.com/documentation/">바로가기</a>

<br/>

### SASS vs SCSS

- SASS를 작성하는 방법은 2가지가 있다. 이 중 <strong>SCSS 문법을 사용하는 것을 권장</strong>한다.

- 왜냐하면 SASS의 문법 개선을 통해 나온 것이 SCSS이기도 하고, 여러 가지 문법의 차이가 있지만 <strong>SCSS가 더 넓은 범용성과 CSS의 호환성</strong> 등의 장점이 있기 때문이다.

  - SASS 문법

    ```scss
    nav
    ul
        margin: 0
        padding: 0
        list-style: none

    li
        display: inline-block

    a
        display: block
        padding: 6px 12px
        text-decoration: none


    ```

  - SCSS 문법

    ```scss
    nav {
      ul {
        margin: 0;
        padding: 0;
        list-style: none;
      }

      li {
        display: inline-block;
      }

      a {
        display: block;
        padding: 6px 12px;
        text-decoration: none;
      }
    }
    ```

<br/>

### SASS 적용하기

- 확장자 명 : <code>.scss</code>

  - 기존 css 파일이 있다면 확장자명을 scss로 변경해준다. (JS로 import 시도 마찬가지)

- SPA 환경에서는 각각의 JS 파일에서 독립적으로 CSS 파일을 import 했다 하더라도, <code>Router.js</code>에 모든 페이지 컴포넌트가 모이고, <code>index.js</code>를 거쳐 결국 <code>index.html</code>에 모이게 되는 구조기 때문에 각각의 CSS 파일에서 겹치는 선택자가 있다면, 스타일이 깨지게 된다.

  - 위와 같은 문제를 해결하기 위해 CSS의 자손 결합자를 사용하거나, 더 나은 방법으로 SASS에서 쓰이는 <strong>Nesting 방식</strong>을 활용하자.

- 변수나 mixin은 여러 파일에서 공통으로 사용할 수 있도록 <code>variables.scss</code> 파일에 작성하여 따로 관리를 하는 것이 좋다.

<br/><br/>

## SASS 문법

### Nesting

```scss
/* nav */
.nav {
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 100vw;
  border-bottom: 1px solid $borderColor;
  background-color: white;

  /* .nav div */
  div {
    width: 33%;
  }

  /* .nav__logo */
  &__logo {
    @include flex(0, flex-start, 0);
    padding-left: 5vw;
  }

  /* .nav__icon */
  &__icon {
    @include flex(0, center, 0);
    margin: 20px 0px;
  }

  /* .nav__text */
  &__text {
    @include flex(0, flex-end, 0);
    margin: 20px 0px;
    font-family: "Lobster", cursive;
    font-size: 20px;
  }
}
```

<br/>

### 변수

```scss
$primary-color: #dbdbdb;

body {
  border: 1px solid black;
  color: $primary-color;
}

.inverse {
  background-color: $primary-color;
  color: white;
}
```

<br/>

### 부모선택자 (&), mixin (+ optional arguments)

```scss
@mixin flex($direction: row, $justify: flex-start, $align: flex-start) {
  display: flex;
  flex-direction: $direction;
  align-items: $align;
  justify-content: $justify;
}

/* nav */
.nav {
  @include flex(0, space-around, center);
  width: 100vw;
  border-bottom: 1px solid $borderColor;
  background-color: white;

  /* .nav div */
  div {
    width: 33%;
  }

  /* .nav__logo */
  &__logo {
    @include flex(0, flex-start, 0);
    padding-left: 5vw;
  }

  /* .nav__icon */
  &__icon {
    @include flex(0, center, 0);
    margin: 20px 0px;
  }

  /* .nav__text */
  &__text {
    @include flex(0, flex-end, 0);
    margin: 20px 0px;
    font-family: "Lobster", cursive;
    font-size: 20px;
  }
}
```
