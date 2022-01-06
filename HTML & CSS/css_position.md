# CSS - Position

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

* CSS의 Position 속성은 HTML 요소의 위치 설정 방식을 결정한다.

<br/>

## Position 속성1 : Fixed

* fixed 요소는, <strong>스크롤을 내려도 계속 처음 그 자리에 위치</strong>한다.

* top, bottom, left, right 속성 중 하나라도 수정 시, 해당 요소는 <strong>초기 위치가 무시</strong>되고, <strong>앞 쪽의 레이어로 넘어간다</strong>.

```css
div {
    position: fixed;
    top: 20px;
    right: 15px;
}
```

<br/>

## Position 속성2 : Static

* <strong>Default(초기)값</strong>이다.

* 요소의 위치를 지정하지 않는다.

```css
div {
    position: static;
}
```

<br/>

## Position 속성3 : Relative

* relative 요소는, <strong>처음 위치하는 곳을 기준</strong>으로 top, bottom, left, right 속성의 값만큼 위치를 (미세하게) 이동한다.

```css
div {
    position: relative;
    top: 10px;
    right: 20px;
    /* 처음 위치를 기준으로 위로 10px, 오른쪽으로 20px 이동 */
}
```

<br/>

## Position 속성4 : Absolute

* ✨absolute 요소는, <strong>가장 가까운 relative 부모를 기준</strong>으로, 해당 영역 내에서 top, bottom, left, right 속성을 통해 요소를 배치한다.

    * 이때, relative처럼 요소를 (미세하게) 이동하는 것이 아니라,  

        각 방향의 맨 끝에서 top, bottom, left, right 속성값만큼 떨어진 곳에 요소를 배치하는 것이다.

* ✨만일 부모 중에 <strong>relative 요소가 없으면, body를 기준</strong>으로 삼는다.

```css
div {
    width: 300px;
    height: 300px;
    background-color: wheat;

    position: relative;
}
div > div {
    width: 100px;
    height: 100px;
    background-color: teal;

    position: absolute;
    bottom: 10px;  
    right: 20px;
    /* 가장 가까운 relative 부모(div)의 영역을 기준으로, 맨 아래에서 10px, 맨 우측에서 20px 떨어진 곳에 배치 */
}
```

### 의문점

```css
div {
    background-color: wheat;
    width: 300px;
    height: 300px;

    position: relative;
    ✔top: 0px;
}
.green {
    background-color: teal;
    height: 100px;
    width: 100px;

    position: absolute;
    ✔bottom: 10px;
    left: 20px;
}
```
    부모 relative 속성에 top:0px를 주면, 자식 absolute 속성에서 bottomL 10px가 제대로 동작하지 않는다. 그 이유는 뭘까..