# CSS - 색상 체계, 사용자 지정 CSS 속성 (변수)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## 색상 체계 (Color System)

* CSS는 색상 이름을 통해 140가지의 색상을 지원한다. (☞ <a href="https://www.w3schools.com/cssref/css_colors.asp">지원하는 색상 이름 확인</a>)

* 그러나 여러 색상 체계를 통해 이보다 더 다채로운 색상을 브라우저에 표현할 수 있다.

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

## 사용자 지정 CSS 속성 (Custom Properties)

* ☞ <a href="https://developer.mozilla.org/ko/docs/Web/CSS/Using_CSS_custom_properties">공식 문서 바로가기</a>

* CSS에서 사용하는 <strong>변수</strong>이다. (CSS 변수)

* 반복적으로 사용하는 값을 변수로 저장하여 한 번에 관리할 수 있다.

<br/>

* 사용자 지정 속성은 <strong>전용 표기법</strong>을 사용해 정의하고, <strong>var() 함수</strong>를 사용해 접근할 수 있다.

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

* <strong>변수 이름 전용 표기법</strong>

    * 맨 앞에 dash 2개를 붙인다.

    * 아름 사이에 여백이 있으면 안되므로, 띄어쓰기는 dash 하나로 표현한다.