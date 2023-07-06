## Chapter 8. CSS Beginner

<br/>

### 1. CSS 적용

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

<br/>

### 2. CSS 구성(1) : Box Sizing (content-box, border-box)

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

### 3. CSS 구성(2)

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

- 역시 모든 속성을 외우려 하지 말고 모르면 구글링하면 된다는 마인드로.

<br/><br/>

> 참고1 : 선택자 <code>\*</code>는 모든 요소를 가리킨다.

```css
* {
  border: 1px dashed black;
}
```

<br/>

> 참고2 : <code>border-radius</code> 속성에 50% 속성값을 주면 경계선은 원모양이 된다.

```css
* {
  border-radius: 50%;
}
```
