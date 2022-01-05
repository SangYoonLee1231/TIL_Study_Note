# CSS - Position

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

* CSS의 Position 속성은 특정 요소의 위치를 미세하게 옮기고 싶을 때 사용한다.

* HTML 요소의 위치 설정 방식을 결정한다.

```css
div {
    position: absolute;
}
```

## Position 속성1 : Fixed

* 어떤 요소의 position을 fixed로 설정하면, <strong>스크롤을 내려도 그 요소는 계속 그 자리에 위치</strong>하게 된다.

* top, bottom, left, right 속성 중 하나라도 수정 시, 해당 요소는 <strong>초기 위치가 무시</strong>되고, <strong>앞 쪽의 레이어로 넘어간다</strong>.