# Chapter 8. CSS Beginner

<br/>

## 1. CSS 적용

- 【<strong>external CSS</strong>】 css 파일을 <strong>따로 생성</strong>한 후, html 문서에서 <code>\<link></code>태그를 이용하여 html 파일과 css 파일을 서로 연결한다.

  (더 좋은 방법)

  ```html
  /* link 태그 속성 작성법 */
  <head>
    <link
      href="./styles.css (css 파일 이름)"
      rel="stylesheet"
      type="text/css"
    />
  </head>
  ```

  - <strong><code>link</code></strong> : link 태그로 사용할 css 파일을 링크해준다.

  - <strong><code>href</code></strong> : href 속성에 css 파일 경로를 작성한다.

  - <strong><code>type</code></strong> : link 태그로 연결되는 파일이 어떤 것인지 알려준다. 여기서 css 파일을 연결하므로 type 값은 항상 <code>text/css</code>이다.

  - <strong><code>rel</code></strong> : rel은 HTML 파일과 CSS 파일과의 관계를 설명하는 속성이다. css 파일을 링크할 때는 항상 <code>stylesheet</code> 값을 대입해준다.

<br/><br/>

## 2. CSS 구성(1) : Box Sizing (content-box, border-box)

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

<br/><br/>

## 3. CSS 구성(2)

- 용어 정리

  - <strong>선택자(Selector), 속성 (속성이름, 속성값)</strong>

    ```css
    ↙ 선택자 (Selector)
    h1 {
        font-style: italic;  ← 선언 (Declaration)
            ↑          ↑
        속성 이름   속성 값
        (Property)  (Value)
    }
    ```

<br/>

- 속성 이름은 띄어쓰기를 해선 안 된다. (font-style처럼 '-'를 이용하여 띄어쓰기 표시)

- 각 줄은 세미콜론(';')으로 끝나야 한다.

- 속성 값(Value)엔 해당 속성(Property)에 맞는 값을 넣어주어야 한다.

<br/>

### ID

- id는 <strong>고유한 값</strong>으로 한 요소당 하나만 가질 수 있다.

- id명을 통해 <strong>특정 요소를 직접</strong> 가리킬 수 있다.

<br/>

- CSS 코드에서 선택자로 id를 쓸 때, 값 앞에 <code>#</code>을 붙여서 쓴다.

```css
#first {
  padding: 20px 15px;
}
#second {
  background-color: tomato;
}
```

```html
<div id="first">
  <div id="second"></div>
</div>
```

<br/>

- 여러 같은 html 태그를 생성하였을 때, id를 이용하여 각각을 구분할 수 있고, 서로 다른 속성을 적용시킬 수 있다.

- CSS 코드의 id명은 HTML 코드에서 썼던 id명과 동일해야 한다.

</br><br/>

### Class

- class는 id와 달리, <strong>여러 요소에 같은 이름으로</strong> 부여할 수 있다.

- class명을 통해 <strong>여러 요소를 동시에</strong> 가리킬 수 있다.

<br/>

- CSS 코드에서 선택자로 class를 쓸 때, 값 앞에 <code>.</code>을 붙여쓴다.

- 하나의 HTML 요소에 여러 종류의 class가 쓰일 수 있다.

```css
.btn {
  width: 50px;
  height: 25px;
  border-radius: 5px;
}
.tomato {
  background-color: tomato;
}
.potato {
  background-color: teal;
}
```

```html
<span class="btn tomato">HELLO!</span> <span class="btn potato">HELLO!</span>
```

<br/>

- class 특징을 활용하여 <strong>반복되는 코드를 하나로 묶음</strong>으로써 코드 길이를 줄일 수 있다.

  (위의 btn class처럼)

<br/>

### 선택자 (Selector)

- 선택자의 기본 3가지 종류

  - 태그의 이름을 쓰는 선택자

  - 점<code>.</code>을 쓰고 클래스 이름을 쓰는 선택자

  - 해시 기호<code>#</code>를 쓰고 id값을 쓰는 선택자

- 이 외에, 좀 더 세부적으로 Element를 선택하는 도구(선택자)가 있다.

<br/>

### 결합자 (Combinator)

- 여러 선택자를 결합하여, 더 정밀히 요소를 찾아 가리키는 선택자를 결합자(Combinator)라 한다.

<br/>

- <strong>자손 결합자</strong> : <code>A B</code>

  ```css
  p span {
    ...;
  }
  ```

  p 안의 모든 span을 가리킨다.

  ```css
  div p span {
    ...;
  }
  ```

  div 안의 모든 p, 그 모든 p 안의 모든 span을 가리킨다.

<br/>

### CSS 주석

```css
/* h1 {
    color: brown;
}
*/
```

<br/><br/>

## 4. CSS 특성

### Cascading (폭포수)

- CSS = <strong>Cascading Style Sheet</strong> : 위에서 아래로 코드를 읽는다.

  ☞ 같은 속성 코드가 중복 작성 시, <strong>제일 마지막 줄이 브라우저에 반영</strong>

### Inheritance (상속)

- 부모 요소의 CSS 규칙을 자식 요소가 상속하여 적용

- 그렇지만, 만일 자식 요소가 CSS 규칙을 가지고 있다면 이를 우선하여 적용한다.

### Specificity (우선순위)

- CSS 규칙이 서로 충돌할 때 어떤 것을 적용할지?

- 점수 계산으로 이루어진다.

  - inline styling (HTML 요소에 style 속성을 주어 작성): <strong>1000점</strong>

  - id명: <strong>100점</strong>

  - class 이름: <strong>10점</strong>

  - tag명: <strong>1점</strong>

- 요약

  - <strong>tag &nbsp; << &nbsp; class &nbsp; << &nbsp; id &nbsp; << &nbsp; inline styling</strong>

- TIP

  - **inlince styling은 지향하자.**

<br/><br/>

## 5. Box Model

### Block VS Inline

- <strong>Block</strong>

  - <code>block</code> 태그 옆엔 <strong>다른 요소가 올 수 없다.</strong>

  - <code>block</code>은 <strong>높이</strong>(<code>height</code>)와 <strong>너비</strong>(<code>width</code>)를 가진다.

  - <code>block</code>은 <strong>Box</strong>이고, 여백과 관련된 3가지 중요한 특징을 가진다.

    : <code>margin</code>, <code>border</code>, <code>padding</code>

    (<code>inline</code>도 가지고 있는 특징이다. 상하 margin만 제외하고)

  - Block 속성을 갖는 HTML 요소 : <code>\<div></code>, <code>\<p></code>, <code>\<address></code>, ..

  - Block 속성을 갖는 HTML 요소는 <code>width</code> 속성을 부여하지 않으면 기본적으로 화면 크기의 좌우 끝 전체를 차지한다.

<br/>

- <strong>Inline</strong>

  - <code>inline</code> 태그 옆에 <strong>다른 요소가 올 수 있다.</strong>

  - <code>inline</code>은 ✨<strong>높이</strong>(<code>height</code>)와 <strong>너비</strong>(<code>width</code>)를 <strong>가질 수 없다.</strong>

    - 따라서 ✨<strong>위, 아래에 </strong><code>margin</code><strong>을 가지지 않는다.</strong>

      (가지도록 하려면 <code>display</code> 속성을 <code>inline-block</code>으로 바꾸어야 한다)

  - Inline 속성을 갖는 HTML 요소 : <code>\<span></code>, <code>\<a></code>, <code>\<img></code>, ..

<br/>

### Box Model

#### 여백과 관련된 속성 1 : margin

- <code>margin</code>은 <strong>요소의 경계(border)의 바깥에 있는 영역</strong>이다.

- <code>block</code>과 <code>inline</code> 요소 모두 가지고 있는 특징이나, <code>inline</code>은 <strong>상하에</strong> <code>margin</code><strong>을 가지지 않는다.</strong>

  ```css
  div {
    margin: 20px; /* 전방향 */
    margin: 20px 15px; /* 상하 좌우 */
    margin: 20px 5px 15px 10px; /* 상 우 하 좌 */

    margin-top: 20px;
    margin-bottom: 15px;
    margin-right: 5px;
    margin-left: 10px;
  }
  ```

<br/>

- <code>margin</code>에 <strong><code>auto</code></strong> 값을 주면 요소를 해당 방향의 중앙에 배치시킬 수 있다.

  ```css
  .center {
    margin: 10px auto;
  }
  /* 요소를 좌우, 즉 가로 방향 기준으로 중앙에 배치한다. */
  ```

<br/>

- <strong>user agent stylesheet</strong> :

  브라우저가 기본적으로 부여한 style 속성  
  ex) <code>body { margin : 8px; }</code>

  - 이를 없에려면 <strong><a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_piece_info.md#reset-css">Reset CSS</a></strong>를 적용해주면 된다.

- <strong>Collasping Margins</strong> :

  box 요소의 경계가 부모 box 요소의 경계와 일치하면, 이 두 <code>margin</code>이 하나로 취급되는 현상

  - 위, 아래에서만 일어난다.

<br/>

#### 여백과 관련된 속성 2 : padding

- <code>padding</code>은 <strong>box의 경계(border)로부터 안쪽에 있는 영역</strong>이다.

- <code>block</code>과 <code>inline</code> 요소 모두 가지고 있는 특징이다.

```css
div {
  padding: 20px; /* 전방향 */
  padding: 20px 15px; /* 상하 좌우 */
  padding: 20px 5px 15px 10px; /* 상 우 하 좌 */

  padding-top: 20px;
  padding-bottom: 15px;
  padding-right: 5px;
  padding-left: 10px;

  /* 규칙은 margin과 동일하다. */
}
```

<br/>

#### 여백과 관련된 속성 3 : border

- <code>border</code>은 말 그대로 박스의 '<strong>경계</strong>'이다.

- <code>block</code>과 <code>inline</code> 요소 모두 가지고 있는 특징이다.

- <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-style">border 스타일 종류 확인하기 (MDN 문서)</a>

  ```css
  div {
    border: 1px solid black;
    /* border: 너비 스타일 색깔 */
  }
  span {
    border: 2px dotted blue;
  }
  ```

<br/>

- <code>border</code>은 다양한 속성값이 존재하나 대부분 이쁘지 않으므로 거의 한 종류만 쓴다.

<br/><br/>

## 6. Box Sizing

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

## 7. CSS 단위

- 예) px, %, rem, em

#### px

- 픽셀값, 절댓값

- 스크린을 구성하는 작은 점

#### %

- 상댓값

- 부모 요소를 기준으로 크기를 결정

#### em / rem

- 폰트 크기에 비례하여 크기 설정

- 상댓값

- <strong><code>em</code></strong> : 부모 요소의 폰트 크기 (배수)

- <strong><code>rem</code></strong> (root rm) : 루트 요소의 폰트 크기

  - <code>5rem</code> : \<html> 요소 기준 5배수 크기

  ```css
  html {
    font-size: 10px;
  }

  div.inner {
    width: 5rem;
    /* 10px * 5 = 50px */
  }
  ```

  - **통일된 기준을 잡기 위해서는 rem 단위 사용 권장**

#### vw / vh

- <strong><code>vh</code></strong> : viewport(화면) height

  - <code>100vh</code> : 화면 높이의 100%

- <strong><code>vw</code></strong> : viewport(화면) width

  - <code>100vh</code> : 화면 넓이의 100%

<br/><br/>

## 8. 이미지 다루기

<br/>

- <strong><code>\<img></code></strong> : 이미지 삽입 태그 (Self-Closing Tag)

  - <code>\<img src="... .jpg" width="150" height="200" alt="사진 없음 아무튼 없음"></code>

    ```css
    img {
      max-width: 100%;
    }
    /* 부모 영역에서 벗어나지 않도록 이미지의 너비 상한선을 100%로 설정 */
    ```

    ```css
    img {
      object-fit: cover;
    }
    /* 이미지를 부모 요소의 영역의 크기 만큼 확대/축소하여 채움 */
    ```

    ```css
    img {
      object-fit: contain;
    }
    /* 이미지의 비율을 유지하면서 크기를 변경하여 부모 요소를 채움 */
    ```

    ```css
    img {
      object-fit: fill;
    }
    /* 이미지의 비율을 유지하지 않고 부모 요소의 크기에 맞게 변경하여 채움 */
    ```

<br/><br/>

## 9. Overflow

- Overflow: 요소가 넘처흐른다.

- 브라우저 입장에서 요소가 넘치는 것은 에러가 아님

- 넘처흐르는 요소를 어떻게 처리할 수 있느냐? → CSS의 Overflow 프로퍼티의 역할

  ```css
  div.overflow {
    border: 2px solid black;
    width: 180px;
    font-size: 50px;
    overflow: auto;
  }
  ```

- `overflow: hidden` : 넘쳐흐르는 부분을 보여주지 않는다

- `overflow: scroll` : 사용자가 스크롤을 넘겨서 넘처흐르는 요소를 볼 수 있도록 한다

- 브라우저에서 쓸 데 없는 스크롤이 나오지 않도록 방지

  - `overflow-x: scroll;` (가로 스크롤)

  - `overflow-y: scroll;` (세로 스크롤)

- 요소가 넘치지 않으면 스크롤를 주지 않도록 하는 것이 사용자 입장에서 좋은 경험이다.

  → `overflow: auto`

<br/><br/>

## 10-11. 폰트 / 이미지 꾸미기

### 색상 체계 (Color System)

- CSS는 색상 이름을 통해 140가지의 색상을 지원한다. (☞ <a href="https://www.w3schools.com/cssref/css_colors.asp">지원하는 색상 이름 확인</a>)

- 그러나 여러 색상 체계를 통해 이보다 더 다채로운 색상을 브라우저에 표현할 수 있다.

<br/>

1. <strong>hex code</strong>

```css
p {
  color: #059669;
  /* 16진수 색상코드 */
}
```

2. <strong>rgb</strong>

```css
p {
  color: rgb(252, 206, 0);
  /* 각각 red, green, blue를 의미 */
}
```

3. <strong>rgba</strong>

```css
p {
  color: rgba(252, 206, 0, 0.8);
  /* 각각 red, green, blue, '투명도'를 의미 */

  /* 투명도는 0(투명)~1(불투명) 사이의 값으로 조절할 수 있다. */
}
```

<br/>

### 사용자 지정 CSS 속성 (Custom Properties)

- ☞ <a href="https://developer.mozilla.org/ko/docs/Web/CSS/Using_CSS_custom_properties">공식 문서 바로가기</a>

- CSS에서 사용하는 <strong>변수</strong>이다. (CSS 변수)

- 반복적으로 사용하는 값을 변수로 저장하여 한 번에 관리할 수 있다.

<br/>

- 사용자 지정 속성은 <strong>전용 표기법</strong>을 사용해 정의하고, <strong>var() 함수</strong>를 사용해 접근할 수 있다.

```css
:root {
  --main-color: #fcce00;
  --default-border: 1px solid var(--main-color);
}
/* :root는 모든 document의 뿌리를 뜻함 */

a {
  color: var(--main-color);
  border: var(--default-border);
}
```

- <strong>변수 이름 전용 표기법</strong>

  - 맨 앞에 dash 2개를 붙인다.

  - 아름 사이에 여백이 있으면 안되므로, 띄어쓰기는 dash 하나로 표현한다.

<br/>

### 폰트 꾸미기 예시

```html
<div class="container">
  <p>Hello:)</p>
  <a href="...">링크</a>
</div>
```

```css
html {
  font-size: 10px;
}

p {
  font-size: 0.5rem;
  font-weight: bold;
  text-decoration: underline;
}

a {
  text-decoration: none; /* 링크 태그 밑줄 표시 제거 */
}

a:link {
  color: black; /* 클릭한 적이 없는 링크 */
}

a:visited {
  color: black; /*  방문했던 링크  */
}

/* a:link와 a:visited 작성 순서를 지켜주어야 한다. */
```

<br/>

### 테두리 꾸미기 예시

```html
<div class="container"></div>
```

```css
.container {
  border: 2px solid blue;
  border-radius: 20px; /* 반경 값을 넣어 모서리를 둥글게 */
}
```

- 테두리는 별도 선언이 없으면 none 값이 적용되어 보이지 않는다.

<br/><br/>

## 12. 배경 이미지 설정

### 배경 색 설정

```html
<div class="container">
  <p>안녕하세요!</p>
</div>
```

```css
.container {
  background-color: blue;
}

p {
  background-color: skyblue;
}
```

<br/>

### 배경 이미지 넣기

```html
<div class="container"></div>
```

```css
.container {
  background-image: url("imoji.png");
  background-repeat: no-repeat;
  background-size: contain; /* 이미지가 온전히 표시되는 것이 우선 */
  background-position: center; /* 배경 이미지를 정중앙에 배치 */
}
```

- 이미지를 레이아웃에 맞는 해상도로 크롭해서 사용하는 것이 가장 좋다.

<br/><br/>

## 13. 요소 정렬하기

### 요소를 가운데로 정렬하기

#### 정중앙 정렬하는 전통적인 방법

```css
div {
  margin: 0 auto;
}
```

- 부모 block 요소의 width를 기준으로 자동으로 margin 계산

- 부모 block 요소 자체를 중앙으로 정렬함

<br/>

#### 정중앙 정렬하는 또다른 방법

```css
div {
  text-align: center;
}
```

- 부모 요소가 block이고, 정렬하고자 하는 자식 요소가 inline 요소일 때 가능

<br/>
