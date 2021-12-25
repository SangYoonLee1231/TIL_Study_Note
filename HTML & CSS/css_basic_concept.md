# CSS의 기본

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## 🗨 CSS란

*  CSS는, 선택자(Selector)를 통해 HTML 태그를 가리키고, 디자인 효과를 부여하는 역할을 한다.

* CSS = <strong>Cascading</strong> Style Sheet : 위에서 아래로 코드를 읽는다.  
☞ 같은 속성 코드가 중복 작성 시, <strong>제일 마지막 줄이 브라우저에 반영</strong>

<br/>

## HTML 파일에 CSS를 추가하는 방법

*  【inline CSS】 html 문서의 \<style>태그 사이에 css 코드를 직접 작성한다.  
(\<style>태그는 \<head>태그 사이에 작성한다.)

```html
<head>
    <style>
        /* 이 곳에 CSS 코드를 작성 */
    </style>
</head>
```

*  【external CSS】 css 파일을 따로 생성한 후, html 문서에서 \<link> 태그를 이용하여 html 파일과 css파일을 서로 연결한다.  
(더 좋은 방법)
```html
/* link 태그 속성 작성법 */
<link href="styles.css (css 파일 이름)" rel="stylesheet" />
```

<br/>

## CSS 기본 문법

* 용어 정리  
: 선택자(Selector), 속성 (속성이름, 속성값)
```css
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

## ✨ Block VS inline

* Block

  * Block 태그 옆엔 다른 요소가 <strong>올 수 없다.</strong>  

  * Block은 <strong>높이(height)와 너비(width)를 가진다.</strong>  

  * <strong>Block은 Box</strong>이고, 3가지 중요한 특징을 가진다.  
  :   <strong>margin, border, padding</strong>  

  *  ex) \<div>, \<p>, \<address>
  
* inline

  * inline 태그 옆에 다른 요소들이 <strong>올 수 있다.</strong>   

  * inline은 <strong>높이(height)와 너비(width)를 가질 수 없다.</strong>  

  * ex) \<span>, \<a>, \<image>

<br/>

## Box가 갖는 속성 1 : 《 margin 》

* margin은 box의 경계(border)의 바깥에 있는 영역이다.

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

* user agent stylesheet :  
브라우저가 기본적으로 부여한 style 속성  
  ex) body { margin : 8px; }

* Collasping Margins :  
box 요소의 경계가 부모 box 요소의 경계가 일치하면, 이 두 margin이 하나로 취급되는 현상