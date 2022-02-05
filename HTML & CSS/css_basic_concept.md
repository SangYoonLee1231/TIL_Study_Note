# CSS의 소개와 기본 문법

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## 🗨 CSS 소개

* <strong>CSS</strong>는, <strong>선택자(Selector)</strong>를 통해 HTML 태그를 가리키고, 디자인 효과(스타일)를 부여하는 역할을 한다.

* <strong>CSS</strong> = <strong>Cascading</strong> Style Sheet : 위에서 아래로 코드를 읽는다.  

  ☞ 같은 속성 코드가 중복 작성 시, <strong>제일 마지막 줄이 브라우저에 반영</strong>

<br/>

## HTML 파일에 CSS를 추가하는 방법

*  【<strong>inline CSS</strong>】 html 문서의 <code>\<style></code>태그 사이에 css 코드를 <strong>직접 작성</strong>한다.  

   (<code>\<style></code>태그는 <code>\<head></code>태그 사이에 작성한다.)

```html
<head>
    <style>
        /* 이 곳에 CSS 코드를 작성 */
    </style>
</head>
```

<br/>

*  【<strong>external CSS</strong>】 css 파일을 <strong>따로 생성</strong>한 후, html 문서에서 <code>\<link></code>태그를 이용하여 html 파일과 css 파일을 서로 연결한다.  

   (더 좋은 방법)

```html
/* link 태그 속성 작성법 */
<head>
    <link href="styles.css (css 파일 이름)" rel="stylesheet" />
</head>
```

<br/>

## CSS 기본 문법

* 용어 정리  

    : <strong>선택자(Selector), 속성 (속성이름, 속성값)</strong>

```
 ↙ 선택자 (Selector)
h1 {
    font-style: italic;
        ↑          ↑
     속성 이름   속성 값
    (Property)  (Value)
}
```

* 속성 이름은 띄어쓰기를 해선 안 된다. (font-style처럼 '-'를 이용하여 띄어쓰기 표시)

* 각 줄은 세미콜론(';')으로 끝나야 한다.

* 속성 값(Value)엔 해당 속성(Property)에 맞는 값을 넣어주어야 한다.

* 역시 모든 속성을 외우려 하지 말고 모르면 구글링하면 된다는 마인드로.

<br/>
<br/>

> 참고1 : 선택자 <code>*</code>는 모든 요소를 가리킨다.
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