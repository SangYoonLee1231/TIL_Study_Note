# CSS - Flexbox

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## Flexbox란

* HTML 요소의 배치를 바꾸는 쉬운 방법

* display의 하나의 속성

```css
body {
    display: flex;
}
```

* display: flex로 만드는 것을 flex 컨테이너로 만든다라고 말해도 된다.

<br/>

## ✨ Flexbox 사용 시 지켜야 할 3가지 Rule

* Rule 1. 반드시 flex를 적용하고자 하는 Element(요소)의 <strong>부모 Element</strong>에 display: flex를 명시해야 한다.

    * display: flex == 이 box '<strong>안</strong>'에 들어있는 Element들을 이제부터 flex로 관리한다.

    * <strong>자식 Element에 display: flex 작성 금지</strong> (처음에 하기 쉬운 실수)

* Rule 2.

```css
body {
    display: flex;
    
}
```