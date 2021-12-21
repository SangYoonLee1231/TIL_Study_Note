# CSS의 기본

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## 🗨 CSS란

*  CSS는 선택자(Selector)를 통해 HTML 태그를 가리키고, 디자인 효과를 부여하는 역할을 한다.

* CSS = Cascading Style Sheet : 위에서 아래로 코드를 읽는다.  
☞ 같은 속성 코드가 중복 작성 시, <strong>제일 마지막 줄이 브라우저에 반영</strong>

<br/>

## HTML 파일에 CSS를 추가하는 방법

*  【inline CSS】 \<style> 태그 이용하여 html 파일에 직접 작성한다.

```html
<head>
    <style>
        CSS 작성
    </style>
</head>
```

*  【external CSS】 css 파일을 따로 생성한 후, html 문서에서 \<link> 태그를 이용하여 html 파일과 css파일을 서로 연결한다.
```html
<link href="styles.css (css 파일 이름)" rel="stylesheet" />
```

<br/>

## CSS 기본 문법

* 용어 정리 :  
선택자(Selector), 속성 (속성이름, 속성값)
```css
 ↙ 선택자 (Selector)
h1 {
    font-style: italic;
        ↑          ↑
     속성 이름   속성 값
    (Property)  (Value)
}
```

* 속성 이름은 띄어쓰기를 해선 안 된다. (font-style처럼 '-'를 이용하여 작성)

* 각 줄은 세미콜론(';')으로 끝나야 한다.

* 속성 값(Value)엔 해당 속성(Property)에 맞는 값을 넣어야 한다.

* 역시 모든 속성을 외우려 하지 말고 모르면 구글링한다.

<br/>

## Block VS inline

* Block 태그 옆엔 다른 요소가 올 수 없다.  
ex) \<div>, \<p>, \<address>

* inline 태그 옆에 다른 요소들이 올 수 있다.  
ex) \<span>, \<a>, \<image>

<br/>