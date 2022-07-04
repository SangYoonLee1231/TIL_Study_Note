# CSS - BEM (Block Element Modifier)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## BEM (Block Element Modifier) 이란

- 클래스의 이름을 지을 때, 더 편하게 코드를 읽을 수 있도록 하기 위해 만든 '<strong>클래스 이름 짓기 규칙</strong>'

- 좀 더 쉽게 읽히는 CSS를 가지는 것이다.

- 기본적으로 id를 사용하지 않고, HTML의 모든 요소가 클래스만 가지도록 한다.

<br/>

## 규칙

- <code>.block {}</code> : 블록, class 같은 개념

    - 재사용 가능한, 기능적으로 독립된 페이지 컴포넌트

- <code>.block__element {}</code> : 블록을 구성하는 단위
    - 블록에 의존적인 형태. 자신이 속한 블록 내에서만 의미를 가짐

- <code>.block--modifier {}</code> : 블록이나 엘리멘트의 속성

    - 조금 다르게 동작하는 블록이나 엘리먼트를 만들 때 사용할 수 있다.

```css
/*.block {} 예시*/
.btn {}

/*.block__element {} 예시*/
.btn__price {}

/*.block__element--modifier {} 예시*/
.btn__price--big {}
```

<br/><br/>

## 주의점

- block은 block을 감쌀 수 있다.

    ```html
    <div class="header">
        <div class="logo">
            <h1 class="logo__name"></h1>
        </div>
    </div>
    ```

<br/>

- element을 여러 번 중첨할 때, 하위 엘리멘트 개념을 고려하지 않고 같은 block의 element로 취급한다.

    - 잘못된 예시

        ```html
        <form class="search-form">
            <div class="search-form__content">
                <input class="search-form__content__input"/>
                <button class="search-form__content__button">Search</button>
            </div>
        </form>
        ```

    - 올바른 예시

        ```html
        <form class="search-form">
        <div class="search-form__content">
            <input class="search-form__input"/>
            <button class="search-form__button">Search</button>
        </div>
        </form>
        ```

<br/>

- modifier을 작성할 떄 2가지 Type으로 작성할 수 있다.

    - boolean 타입

        ```css
        .tab-item--focused {}
        ```

    - key-value 타입

        ```css
        .form-login--theme-normal {}

        .title--color-gray {}
        ```

<br/><br/>

## 장단점

- 장점

    - 클래스 이름만으로 마크업 구조를 알 수 있다.

    - 코드의 가독성이 높아진다.

- 단점

    - 코드의 길이가 늘어난다.

    - 클래스의 이름이 길어질 수 있다.

<br/>

> 추가 참고 자료 : <a href="https://nykim.work/15">[CSS 방법론] BEM 방식 (블로그 포스트)</a>